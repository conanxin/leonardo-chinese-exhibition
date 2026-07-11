#!/usr/bin/env node
/**
 * v4.8 Second Exhibition Browser QA Runner (ESM)
 *
 * Does not modify the repository. Does not access the public network.
 * Requires a local HTTP server to be running, e.g.:
 *   python3 -m http.server 8770 --directory second-exhibition
 *
 * Exit codes:
 *   0 - PASS
 *   1 - QA failure
 *   2 - Browser environment not available
 *
 * Environment variables:
 *   SECOND_EXHIBITION_QA_URL (default: http://127.0.0.1:8770/site/)
 *   PLAYWRIGHT_CHROMIUM_EXECUTABLE - path to a Chromium executable
 *   PLAYWRIGHT_NODE_PATH             - extra path to require('playwright') from
 */

import fs from "node:fs";
import path from "node:path";
import http from "node:http";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

const DEFAULT_URL = "http://127.0.0.1:8770/site/";
const TARGET_URL = process.env.SECOND_EXHIBITION_QA_URL || DEFAULT_URL;

const RESULTS = {
  status: "unknown",
  viewportMatrix: [],
  interaction: {},
  a11y: {},
  noJs: {},
  reducedMotion: {},
  externalRequests: 0,
  failedRequests: 0,
  consoleErrors: 0,
  pageErrors: 0,
  browser: {
    executable: null,
    version: null,
    source: null,
  },
  url: TARGET_URL,
  startedAt: new Date().toISOString(),
  finishedAt: null,
};

function log(group, message) {
  console.log(`[${group}] ${message}`);
}

function printSummary() {
  RESULTS.finishedAt = new Date().toISOString();
  console.log("\n=== Browser QA Summary ===");
  console.log(JSON.stringify(RESULTS, null, 2));
}

async function checkServer() {
  const u = new URL(TARGET_URL);
  return new Promise((resolve) => {
    const req = http.get(
      { hostname: u.hostname, port: u.port, path: u.pathname },
      (res) => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          resolve(true);
        } else {
          resolve(false);
        }
      }
    );
    req.on("error", () => resolve(false));
    req.setTimeout(5000, () => {
      req.destroy();
      resolve(false);
    });
  });
}

function loadPlaywright() {
  const extraPaths = [];
  if (process.env.PLAYWRIGHT_NODE_PATH) {
    extraPaths.push(process.env.PLAYWRIGHT_NODE_PATH);
  }
  extraPaths.push("/tmp/playwright-test/node_modules/playwright");
  extraPaths.push("/tmp/playwright-test/node_modules/playwright-core");

  const errors = [];
  for (const p of extraPaths) {
    if (fs.existsSync(p)) {
      try {
        const mod = require(p);
        RESULTS.browser.source = p;
        return mod;
      } catch (e) {
        errors.push(`${p}: ${e.message}`);
      }
    }
  }
  try {
    const mod = require("playwright");
    RESULTS.browser.source = "playwright";
    return mod;
  } catch (e) {
    errors.push(`playwright: ${e.message}`);
  }
  try {
    const mod = require("playwright-core");
    RESULTS.browser.source = "playwright-core";
    return mod;
  } catch (e) {
    errors.push(`playwright-core: ${e.message}`);
  }
  log("ENV", "Playwright not found: " + errors.join("; "));
  return null;
}

function findExecutable(chromium) {
  if (process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE) {
    return process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE;
  }
  if (chromium && typeof chromium.executablePath === "function") {
    return chromium.executablePath();
  }
  return null;
}

async function launchBrowser(playwright) {
  const executablePath = findExecutable(playwright.chromium);
  if (executablePath && !fs.existsSync(executablePath)) {
    log("ENV", `executable not found: ${executablePath}, trying default launch`);
  }
  const launchOptions = { headless: true };
  if (executablePath && fs.existsSync(executablePath)) {
    launchOptions.executablePath = executablePath;
  }
  const browser = await playwright.chromium.launch(launchOptions);
  RESULTS.browser.executable = await browser.version();
  RESULTS.browser.version = await browser.version();
  return browser;
}

async function runViewport(page, viewport) {
  await page.setViewportSize(viewport);
  await page.goto(TARGET_URL, { waitUntil: "networkidle" });
  await page.waitForLoadState("networkidle");

  // Force all lazy-loaded images into view by scrolling to bottom.
  await page.evaluate(async () => {
    await new Promise((resolve) => {
      let total = 0;
      const step = 200;
      const timer = setInterval(() => {
        window.scrollBy(0, step);
        total += step;
        if (total >= document.body.scrollHeight) {
          clearInterval(timer);
          window.scrollTo(0, 0);
          resolve();
        }
      }, 50);
    });
  });
  await new Promise((r) => setTimeout(r, 800));

  const metrics = await page.evaluate(() => {
    const sections = document.querySelectorAll(".exhibition-section");
    const cards = document.querySelectorAll(".artifact-card");
    const glossaryItems = document.querySelectorAll(".glossary-item");
    const sourceNotes = document.querySelectorAll(".source-note");
    const creditLines = document.querySelectorAll(".credit-line");
    const images = Array.from(document.querySelectorAll(".artifact-card img"));
    const h1 = document.querySelector("h1");
    const title = document.title;
    const repoStatus = document.querySelector(".repository-status");
    const bodyWidth = document.body.scrollWidth;
    const docWidth = document.documentElement.scrollWidth;
    const viewportWidth = window.innerWidth;

    return Promise.all(images.map((img) =>
      new Promise((resolve) => {
        if (img.complete && img.naturalWidth > 0) return resolve(true);
        if (img.complete) return resolve(false);
        let done = false;
        const finish = (ok) => {
          if (done) return;
          done = true;
          resolve(ok);
        };
        img.addEventListener("load", () => finish(img.naturalWidth > 0), { once: true });
        img.addEventListener("error", () => finish(false), { once: true });
        setTimeout(() => finish(img.naturalWidth > 0), 3000);
      })
    )).then((loaded) => ({
      title,
      h1Text: h1 ? h1.textContent : "",
      sectionCount: sections.length,
      cardCount: cards.length,
      glossaryCount: glossaryItems.length,
      sourceNoteCount: sourceNotes.length,
      creditLineCount: creditLines.length,
      imageCount: images.length,
      imagesLoaded: loaded.filter(Boolean).length,
      repoStatusVisible: repoStatus ? repoStatus.checkVisibility() : false,
      repoStatusText: repoStatus ? repoStatus.textContent : "",
      bodyText: document.body.textContent,
      bodyOverflow: bodyWidth > viewportWidth,
      docOverflow: docWidth > viewportWidth,
      viewportWidth,
    }));
  });

  const checks = [];
  const check = (cond, msg) => checks.push({ ok: cond, msg });

  check(metrics.title.includes("植物图谱与视觉分类"), "title contains 植物图谱与视觉分类");
  check(metrics.h1Text.includes("植物图谱与视觉分类"), "h1 contains 植物图谱与视觉分类");
  check(metrics.sectionCount === 4, `sections = ${metrics.sectionCount}`);
  check(metrics.cardCount === 6, `artifact cards = ${metrics.cardCount}`);
  check(metrics.glossaryCount >= 10, `glossary items = ${metrics.glossaryCount}`);
  check(metrics.sourceNoteCount >= 6, `source notes = ${metrics.sourceNoteCount}`);
  check(metrics.creditLineCount >= 6, `credit lines = ${metrics.creditLineCount}`);
  check(metrics.imageCount === 6, `images = ${metrics.imageCount}`);
  check(metrics.imagesLoaded === 6, `images loaded = ${metrics.imagesLoaded}`);
  check(metrics.repoStatusVisible, "repository status visible");
  check(!metrics.bodyOverflow, "no body overflow");
  check(!metrics.docOverflow, "no document overflow");

  // v5.3b: current publication status must be visible on the page
  check(metrics.bodyText.includes("production-deployed-v5.3"), "page declares current publication status 'production-deployed-v5.3'");
  check(metrics.bodyText.includes("published-in-v5.3"), "page declares per-asset publication status 'published-in-v5.3'");
  // Historical import record must remain visible (immutable v4.5 evidence)
  check(metrics.bodyText.includes("imported-not-deployed"), "page preserves historical import record 'imported-not-deployed'");
  // Stale current-status phrasing must NOT appear
  check(!metrics.bodyText.includes("本展览未部署到 GitHub Pages"), "page does not currently claim 'this exhibition is not deployed'");

  const failed = checks.filter((c) => !c.ok);
  const result = {
    viewport: `${viewport.width}x${viewport.height}`,
    metrics,
    checks,
    pass: failed.length === 0,
  };
  RESULTS.viewportMatrix.push(result);
  return result.pass;
}

async function runInteractionChecks(page) {
  // Guided toggle
  await page.goto(TARGET_URL, { waitUntil: "networkidle" });
  await page.click("#guided-toggle");
  await new Promise((r) => setTimeout(r, 200));
  const bannerVisible = await page.evaluate(() => {
    const b = document.getElementById("guided-mode-banner");
    return b ? !b.hidden : false;
  });
  const togglePressed = await page.evaluate(() => {
    const b = document.getElementById("guided-toggle");
    return b ? b.getAttribute("aria-pressed") === "true" : false;
  });
  RESULTS.interaction.guidedToggle = bannerVisible && togglePressed;

  // Lightbox C-01
  await page.goto(TARGET_URL, { waitUntil: "networkidle" });
  const c01Card = await page.locator('.artifact-card[data-candidate-id="C-01"]').first();
  await c01Card.click();
  await new Promise((r) => setTimeout(r, 300));
  const lightbox = await page.locator("#lightbox");
  const lightboxHidden = await lightbox.isHidden();
  const lightboxRole = await page.evaluate(() => {
    const el = document.getElementById("lightbox");
    return el ? el.getAttribute("role") : null;
  });
  const accessibleName = await page.evaluate(() => {
    const el = document.getElementById("lightbox");
    return el ? el.getAttribute("aria-label") || el.getAttribute("aria-labelledby") : null;
  });
  const lightboxOpen = !lightboxHidden;
  RESULTS.interaction.lightboxOpen = lightboxOpen;
  RESULTS.interaction.lightboxRole = lightboxRole;
  RESULTS.interaction.lightboxAccessibleName = accessibleName;

  // Close button focus
  const closeFocused = await page.evaluate(() => {
    const active = document.activeElement;
    return active && active.classList.contains("lightbox-close");
  });
  RESULTS.interaction.closeButtonFocused = closeFocused;

  // ESC close
  await page.keyboard.press("Escape");
  await new Promise((r) => setTimeout(r, 300));
  const lightboxClosed = await lightbox.isHidden();
  RESULTS.interaction.escClose = lightboxClosed;

  // Focus return to trigger image
  const focusReturned = await page.evaluate(() => {
    const active = document.activeElement;
    return active && active.closest('.artifact-card[data-candidate-id="C-01"]') !== null;
  });
  RESULTS.interaction.focusReturn = focusReturned;

  // C-06 lightbox disabled
  const c06Card = await page.locator('.artifact-card[data-candidate-id="C-06"]').first();
  await c06Card.click();
  await new Promise((r) => setTimeout(r, 300));
  const c06LightboxOpen = await (await lightbox.isHidden()) === false;
  RESULTS.interaction.c06LightboxOpen = c06LightboxOpen;

  // Section navigation
  await page.goto(TARGET_URL, { waitUntil: "networkidle" });
  await page.click('a[href="#section-2-classification"]');
  await new Promise((r) => setTimeout(r, 300));
  const sectionInView = await page.evaluate(() => {
    const el = document.getElementById("section-2-classification");
    if (!el) return false;
    const rect = el.getBoundingClientRect();
    return rect.top >= 0 && rect.top < window.innerHeight;
  });
  RESULTS.interaction.sectionNav = sectionInView;

  // Tab focus on main button
  await page.keyboard.press("Tab");
  await new Promise((r) => setTimeout(r, 100));
  const focusable = await page.evaluate(() => {
    const active = document.activeElement;
    const tag = active ? active.tagName.toLowerCase() : "";
    return tag === "button" || tag === "a" || active?.getAttribute("tabindex") === "0";
  });
  RESULTS.interaction.tabFocusable = focusable;
}

async function runA11yChecks(page) {
  await page.goto(TARGET_URL, { waitUntil: "networkidle" });
  const a11y = await page.evaluate(() => {
    const h1s = document.querySelectorAll("h1");
    const imgs = Array.from(document.querySelectorAll(".artifact-card img"));
    const buttons = Array.from(document.querySelectorAll("button"));
    const headings = Array.from(document.querySelectorAll("h1,h2,h3,h4,h5,h6")).map(
      (h) => parseInt(h.tagName.slice(1))
    );
    let jump = false;
    let prev = 1;
    for (const lvl of headings) {
      if (lvl - prev > 1) jump = true;
      prev = lvl;
    }
    const titleEl = document.getElementById("lightbox-title");
    const titleStyle = titleEl ? window.getComputedStyle(titleEl) : null;
    return {
      h1Count: h1s.length,
      imgMissingAlt: imgs.filter((img) => !img.alt || img.alt.trim() === "").length,
      buttonMissingName: buttons.filter((b) => {
        const txt = b.textContent.trim();
        return !txt && !b.getAttribute("aria-label") && !b.getAttribute("aria-labelledby");
      }).length,
      headingJump: jump,
      titleHiddenDisplay: titleStyle ? titleStyle.display === "none" : false,
      titleHiddenVisibility: titleStyle ? titleStyle.visibility === "hidden" : false,
      titlePosition: titleStyle ? titleStyle.position : null,
      titleWidth: titleStyle ? titleStyle.width : null,
      titleHeight: titleStyle ? titleStyle.height : null,
    };
  });
  RESULTS.a11y = a11y;
}

async function runNoJsCheck(page) {
  await page.addInitScript(() => {
    Object.defineProperty(window, "scriptEnabled", { value: false });
  });
  await page.goto("about:blank");
  await page.goto(TARGET_URL, { waitUntil: "domcontentloaded" });
  await new Promise((r) => setTimeout(r, 300));
  const result = await page.evaluate(() => {
    const cards = document.querySelectorAll(".artifact-card");
    const sourceNotes = document.querySelectorAll(".source-note");
    const creditLines = document.querySelectorAll(".credit-line");
    const repoStatus = document.querySelector(".repository-status");
    return {
      cardCount: cards.length,
      sourceNotes: sourceNotes.length,
      creditLines: creditLines.length,
      repoStatusVisible: repoStatus ? repoStatus.checkVisibility() : false,
      bodyText: document.body.textContent.includes("植物图谱与视觉分类"),
    };
  });
  RESULTS.noJs = result;
}

async function runReducedMotionCheck(page) {
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.goto(TARGET_URL, { waitUntil: "networkidle" });
  await page.click('.artifact-card[data-candidate-id="C-01"]');
  await new Promise((r) => setTimeout(r, 300));
  const lightboxVisible = await (await page.locator("#lightbox").isHidden()) === false;
  await page.keyboard.press("Escape");
  await new Promise((r) => setTimeout(r, 300));
  const lightboxClosed = await page.locator("#lightbox").isHidden();
  RESULTS.reducedMotion = {
    lightboxOpen: lightboxVisible,
    escClose: lightboxClosed,
  };
}

async function trackRequests(page) {
  const external = [];
  const failed = [];
  const consoleErrors = [];
  const pageErrors = [];
  page.on("request", (req) => {
    const url = req.url();
    if (url.startsWith("http://127.0.0.1") || url.startsWith("http://localhost") || url.startsWith("data:")) {
      return;
    }
    external.push(url);
  });
  page.on("requestfailed", (req) => {
    failed.push(`${req.url()}: ${req.failure().errorText}`);
  });
  page.on("console", (msg) => {
    if (msg.type() === "error") {
      const text = msg.text();
      const loc = msg.location()?.url || "";
      // Filter out favicon 404 noise (browser auto-requests /favicon.ico).
      if (text.includes("favicon.ico") || loc.includes("favicon.ico")) {
        return;
      }
      consoleErrors.push(text);
      console.log(`[console-error] ${text} at ${loc}`);
    }
  });
  page.on("pageerror", (err) => {
    pageErrors.push(err.message);
    console.log(`[page-error] ${err.message}`);
  });
  return { external, failed, consoleErrors, pageErrors };
}

async function main() {
  const serverOk = await checkServer();
  if (!serverOk) {
    console.error(`Server not responding at ${TARGET_URL}`);
    console.error("Start it with: python3 -m http.server 8770 --directory second-exhibition");
    process.exit(2);
  }
  log("ENV", `Server responding at ${TARGET_URL}`);

  const playwright = loadPlaywright();
  if (!playwright) {
    console.error("Playwright not available.");
    console.error("Install with: npm install -g playwright or npx playwright install chromium");
    console.error("Then set PLAYWRIGHT_NODE_PATH if needed.");
    process.exit(2);
  }
  log("ENV", `Playwright loaded from ${RESULTS.browser.source}`);

  let browser;
  try {
    browser = await launchBrowser(playwright);
  } catch (e) {
    console.error(`Browser launch failed: ${e.message}`);
    process.exit(2);
  }

  const context = await browser.newContext();
  const page = await context.newPage();
  const tracker = await trackRequests(page);

  const viewports = [
    { width: 1440, height: 1000 },
    { width: 1280, height: 900 },
    { width: 768, height: 1024 },
    { width: 390, height: 844 },
    { width: 320, height: 700 },
  ];

  let allViewportsPass = true;
  for (const vp of viewports) {
    log("VIEWPORT", `${vp.width}x${vp.height}`);
    const pass = await runViewport(page, vp);
    if (!pass) allViewportsPass = false;
  }

  await runInteractionChecks(page);
  await runA11yChecks(page);
  await runNoJsCheck(page);
  await runReducedMotionCheck(page);

  RESULTS.externalRequests = tracker.external.length;
  RESULTS.failedRequests = tracker.failed.length;
  RESULTS.consoleErrors = tracker.consoleErrors.length;
  RESULTS.pageErrors = tracker.pageErrors.length;

  await browser.close();

  const failures = [];
  if (!allViewportsPass) failures.push("viewport matrix");
  if (!RESULTS.interaction.guidedToggle) failures.push("guided toggle");
  if (!RESULTS.interaction.lightboxOpen) failures.push("lightbox open");
  if (RESULTS.interaction.lightboxAccessibleName !== "lightbox-title") failures.push("lightbox accessible name");
  if (!RESULTS.interaction.closeButtonFocused) failures.push("close button focus");
  if (!RESULTS.interaction.escClose) failures.push("ESC close");
  if (!RESULTS.interaction.focusReturn) failures.push("focus return");
  if (RESULTS.interaction.c06LightboxOpen) failures.push("C-06 lightbox unexpectedly enabled");
  if (!RESULTS.interaction.sectionNav) failures.push("section navigation");
  if (!RESULTS.interaction.tabFocusable) failures.push("tab focus");
  if (RESULTS.a11y.h1Count !== 1) failures.push("h1 count");
  if (RESULTS.a11y.imgMissingAlt > 0) failures.push("missing alt");
  if (RESULTS.a11y.buttonMissingName > 0) failures.push("button missing name");
  if (RESULTS.a11y.headingJump) failures.push("heading jump");
  if (RESULTS.a11y.titleHiddenDisplay || RESULTS.a11y.titleHiddenVisibility) failures.push("lightbox title hidden from AT");
  if (!RESULTS.noJs.bodyText) failures.push("no-JS body text");
  if (RESULTS.noJs.cardCount < 6) failures.push("no-JS card count");
  if (!RESULTS.noJs.repoStatusVisible) failures.push("no-JS repo status");
  if (!RESULTS.reducedMotion.lightboxOpen || !RESULTS.reducedMotion.escClose) failures.push("reduced motion");
  if (RESULTS.externalRequests > 0) failures.push("external requests detected");
  if (RESULTS.failedRequests > 0) failures.push("failed requests");
  if (RESULTS.consoleErrors > 0) failures.push("console errors");
  if (RESULTS.pageErrors > 0) failures.push("page errors");
  // v5.3b: per-viewport current publication status check (all 5 viewports must have seen it)
  const viewportsWithCurrentStatus = (RESULTS.viewportMatrix || []).filter(v => v.metrics && v.metrics.bodyText && v.metrics.bodyText.includes("production-deployed-v5.3") && v.metrics.bodyText.includes("published-in-v5.3")).length;
  if (viewportsWithCurrentStatus < 5) failures.push(`current publication status visible in only ${viewportsWithCurrentStatus}/5 viewports`);

  if (failures.length > 0) {
    RESULTS.status = "FAIL";
    log("RESULT", `FAIL: ${failures.join(", ")}`);
  } else {
    RESULTS.status = "PASS";
    log("RESULT", "PASS");
  }
  printSummary();
  process.exit(RESULTS.status === "PASS" ? 0 : 1);
}

main().catch((e) => {
  console.error(`Unexpected error: ${e.message}`);
  console.error(e.stack);
  process.exit(2);
});