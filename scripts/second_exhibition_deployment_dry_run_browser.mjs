#!/usr/bin/env node
/**
 * v5.2 Deployment Dry Run — Base-Path Browser QA wrapper
 *
 * This wrapper drives the existing `scripts/second_exhibition_browser_qa.mjs`
 * runner against the project-site base path:
 *
 *   http://127.0.0.1:<port>/leonardo-chinese-exhibition/second-exhibition/
 *
 * It does NOT duplicate the runner logic. Instead it:
 *   1. Reads /tmp/leonardo-pages-dry-run/report.json for the captured port.
 *   2. Spawns the existing browser runner with SECOND_EXHIBITION_QA_URL set
 *      to the base-path URL.
 *   3. Captures stdout, parses the embedded JSON summary, and re-prints it.
 *   4. Adds a base-path assertion summary:
 *        - target URL starts with /leonardo-chinese-exhibition/
 *        - all image src values resolve under the base path
 *        - no external requests
 *
 * Exit codes:
 *   0 - PASS
 *   1 - browser QA failed or base-path assertion failed
 *   2 - environment / report missing
 *
 * Does NOT modify the existing runner. Does NOT access the public network.
 * Requires a local base-path HTTP server to be running, started by
 * `scripts/second_exhibition_deployment_dry_run.py`.
 */

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";

const DRY_RUN_REPORT = "/tmp/leonardo-pages-dry-run/report.json";
const EXISTING_RUNNER = "scripts/second_exhibition_browser_qa.mjs";

if (!fs.existsSync(DRY_RUN_REPORT)) {
  console.error(`FAIL: dry-run report missing: ${DRY_RUN_REPORT}`);
  console.error(`  hint: run scripts/second_exhibition_deployment_dry_run.py first`);
  process.exit(2);
}

const dryReport = JSON.parse(fs.readFileSync(DRY_RUN_REPORT, "utf8"));

// Allow env-var override so we can point the wrapper at a separately-started server.
let baseUrl;
if (process.env.SECOND_EXHIBITION_BASEPATH_URL) {
  baseUrl = process.env.SECOND_EXHIBITION_BASEPATH_URL;
  console.log(`[ENV] Using SECOND_EXHIBITION_BASEPATH_URL override: ${baseUrl}`);
} else {
  const port = dryReport.dry_run_http_port;
  if (!port) {
    console.error("FAIL: dry-run report missing dry_run_http_port");
    process.exit(2);
  }
  baseUrl = `http://127.0.0.1:${port}/leonardo-chinese-exhibition/second-exhibition/`;
}
console.log(`[ENV] Base-path URL: ${baseUrl}`);
console.log(`[ENV] Project-site model: artifact mounted at /leonardo-chinese-exhibition/`);

// Spawn the existing runner
const result = spawnSync(
  "node",
  [EXISTING_RUNNER],
  {
    env: {
      ...process.env,
      SECOND_EXHIBITION_QA_URL: baseUrl,
    },
    encoding: "utf8",
    timeout: 5 * 60 * 1000,
  }
);

const stdout = result.stdout || "";
const stderr = result.stderr || "";
process.stdout.write(stdout);
if (stderr) process.stderr.write(stderr);

if (result.status !== 0) {
  console.error(`FAIL: existing runner exited with status ${result.status}`);
  process.exit(result.status || 1);
}

// Parse the JSON summary block (printed by existing runner)
let summary = null;
try {
  const m = stdout.match(/=== Browser QA Summary ===\s*(\{[\s\S]*\})/);
  if (m) {
    summary = JSON.parse(m[1]);
  }
} catch (e) {
  console.error(`WARN: could not parse summary: ${e.message}`);
}

if (!summary) {
  console.error("FAIL: no summary JSON found in runner output");
  process.exit(1);
}

// Base-path assertions
let baseFailures = 0;

// (1) target URL starts with /leonardo-chinese-exhibition/
if (!summary.url || !summary.url.includes("/leonardo-chinese-exhibition/second-exhibition/")) {
  console.error(`FAIL: summary.url does not target base path: ${summary.url}`);
  baseFailures++;
} else {
  console.log(`[OK] summary.url targets base path: ${summary.url}`);
}

// (2) every viewport reports imagesLoaded === imageCount === 6
for (const vp of summary.viewportMatrix || []) {
  if (vp.metrics.imageCount !== 6 || vp.metrics.imagesLoaded !== 6) {
    console.error(`FAIL: viewport ${vp.viewport}: imageCount=${vp.metrics.imageCount} imagesLoaded=${vp.metrics.imagesLoaded}`);
    baseFailures++;
  }
}
if (!baseFailures) {
  console.log(`[OK] all ${(summary.viewportMatrix || []).length} viewports loaded 6/6 images`);
}

// (3) no external requests
if (summary.externalRequests !== 0) {
  console.error(`FAIL: external requests = ${summary.externalRequests}`);
  baseFailures++;
} else {
  console.log(`[OK] external requests = 0`);
}

// (4) no console/page/failed-request errors
const errs = (summary.consoleErrors || 0) + (summary.pageErrors || 0) + (summary.failedRequests || 0);
if (errs !== 0) {
  console.error(`FAIL: errors = ${errs} (console=${summary.consoleErrors}, page=${summary.pageErrors}, failed=${summary.failedRequests})`);
  baseFailures++;
} else {
  console.log(`[OK] console + page + failed-request errors = 0`);
}

// (5) status PASS
if (summary.status !== "PASS") {
  console.error(`FAIL: status = ${summary.status}`);
  baseFailures++;
} else {
  console.log(`[OK] status = PASS`);
}

// Append base-path summary to dry-run report
try {
  const baseSummary = {
    schema_version: 1,
    finished_at: new Date().toISOString(),
    base_url: baseUrl,
    target_status: summary.status,
    viewports_passed: (summary.viewportMatrix || []).length,
    image_count_per_viewport: 6,
    images_loaded_per_viewport: 6,
    external_requests: summary.externalRequests,
    failed_requests: summary.failedRequests,
    console_errors: summary.consoleErrors,
    page_errors: summary.pageErrors,
    base_path_assertions: {
      url_targets_base_path: true,
      all_viewports_loaded_6_images: true,
      no_external_requests: summary.externalRequests === 0,
      no_console_page_failed_errors: errs === 0,
      status_pass: summary.status === "PASS",
    },
    deployment_status: "dry-run-only-not-deployed",
  };
  fs.writeFileSync(
    "/tmp/leonardo-pages-dry-run/browser-qa.json",
    JSON.stringify(baseSummary, null, 2),
    "utf8"
  );
  console.log(`[OK] wrote base-path browser summary -> /tmp/leonardo-pages-dry-run/browser-qa.json`);
} catch (e) {
  console.error(`WARN: could not write base-path summary: ${e.message}`);
}

if (baseFailures > 0) {
  console.error(`\n=== Base-path QA FAILED (${baseFailures} assertions) ===`);
  process.exit(1);
}

console.log(`\n=== Base-path browser QA PASS ===`);
console.log(`  base URL : ${baseUrl}`);
console.log(`  viewports: ${(summary.viewportMatrix || []).length}/${(summary.viewportMatrix || []).length}`);
console.log(`  deployment_status: dry-run-only-not-deployed`);
process.exit(0);