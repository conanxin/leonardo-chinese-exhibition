# Incident Response and Rollback

This document is the agreed procedure for handling an incident on the
public second-exhibition surface or on the wider site, and for rolling
back to a known-good state without losing history.

## Severity levels

- **P0 — site unavailable or internal files exposed**
  Symptoms: `curl` to root or `/second-exhibition/` returns non-200,
  or any of the forbidden paths under the security boundary returns 200.
  Examples: Pages deploy failure exposing the full repo, accidental
  workflow change that uploads the repository root, DNS / Pages outage.

- **P1 — second exhibition unavailable / corrupted / checksum mismatch**
  Symptoms: second-exhibition HTTP 500 / 404, index byte differs from
  baseline, any of the six image SHA-256 differs, status phrase counts
  drift from baseline.

- **P2 — interaction / accessibility regression**
  Symptoms: lightbox no longer opens, ESC / focus return broken, alt
  coverage drops, overflow reappears, console / page / network errors
  reappear in `scripts/second_exhibition_browser_qa.mjs`.

- **P3 — wording / documentation issue**
  Symptoms: status phrase off by one, manifest / report description
  mismatch, link rot. The live surface still functions, only the
  text reads wrong.

## Immediate checks

Run these in order. Capture their output into the incident report.

1. **GitHub Actions latest run on `main`**

   ```bash
   gh run list --limit 5
   gh run view <run-id> --log | tail -100
   ```

2. **Root HTTP / byte / hash**

   ```bash
   curl -L -sS -o /tmp/inc-root.html https://conanxin.github.io/leonardo-chinese-exhibition/
   wc -c /tmp/inc-root.html
   sha256sum /tmp/inc-root.html
   ```

3. **Second-exhibition HTTP / byte / hash**

   ```bash
   curl -L -sS -o /tmp/inc-second.html \
     https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/
   wc -c /tmp/inc-second.html
   sha256sum /tmp/inc-second.html
   ```

4. **Six image HTTP / SHA**

   ```bash
   sha256sum -c second-exhibition/assets/asset-checksums.sha256
   for p in \
     bhl-318921-page-603998-c01.webp \
     bhl-318921-page-603962-c03.webp \
     smithsonian-nmnh-1529703.png \
     met-285149.jpg \
     rijksmuseum-rp-f-f80152.jpg \
     rijksmuseum-rp-f-f80313.jpg; do
     curl -L -sS \
       "https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/images/$p" \
       -o /tmp/inc-$p
     ls -la /tmp/inc-$p
   done
   sha256sum /tmp/inc-*.webp /tmp/inc-*.png /tmp/inc-*.jpg
   ```

5. **Forbidden paths**

   ```bash
   python3 scripts/second_exhibition_production_healthcheck.py
   ```

6. **Workflow diff**

   ```bash
   git log --oneline --decorate -20
   git show <last-known-good-commit-sha>:.github/workflows/pages.yml \
     > /tmp/wf-good.yml
   diff /tmp/wf-good.yml .github/workflows/pages.yml || true
   ```

7. **Production healthcheck JSON**

   ```bash
   python3 scripts/second_exhibition_production_healthcheck.py \
     --json-output /tmp/inc-health.json
   ```

## Rollback principles

- **Always add a new revert commit.** Do not reset history.
- **No force push.** Force push destroys collaborators' local repos and
  invalidates signed tags.
- **Do not move the stable tag** (`v5.0-real-second-exstitution-deployment`
  in this cycle). It must continue to point at `ac0f19e2c03b09738ae49b4a15c629a1f2177068`.
- **Do not overwrite the GitHub Release.** Re-publish a new Release if
  the live surface is rebuilt under a new freeze.

## Roll back the latest content commit

If only the most recent content commit (a small text fix, an image
description edit, etc.) is broken:

```bash
git revert --no-edit <bad-commit-sha>
git push origin main
```

Wait for the Actions run on the new revert commit to succeed, then
re-run the production health check.

## Roll back controlled deployment wiring

If the second exhibition itself is the source of the incident (e.g. an
interaction regression introduced under v5.3 / v5.3b / v5.3c), revert the
deployment wiring chain in **reverse chronological order**:

```bash
git revert --no-edit 52504047a966c0dd9a60b569a63b1857168a498f
git revert --no-edit 83ab6d8bc8a3f278d53c72516cf72d1a747e13bd
git revert --no-edit f84e53f7f1c5fa20fc8fc40e747bbf934cdfdf92
git push origin main
```

What this does:

- `f84e53f` — wires the v5.3 controlled second-exhibition deployment
  into Pages workflow. Reverting this restores the prior workflow that
  served only the top-level site.
- `83ab6d8` — passes `--audit` to the staging builder. Reverting this
  removes the audit flag from the builder call.
- `5250404` — reconciles the second-exhibition production state
  (v5.3b). Reverting this undoes the v5.3b reconciliation commit.

After all three reverts push and the Actions run succeeds:

- The Pages workflow deploys only the top-level site.
- The `/second-exhibition/` path returns 404.
- The root stays at 92,976 bytes (byte-identical to its v5.0 state).
- The image directory under `/second-exhibition/assets/images/` is no
  longer deployed.

To restore the second exhibition, run a fresh controlled deployment
round (analogous to v5.3 / v5.3b / v5.3c) and freeze it under a new
annotated tag.

## Roll back the freeze commit

If the freeze commit itself (`ac0f19e`) is the problem:

```bash
git revert --no-edit ac0f19e2c03b09738ae49b4a15c629a1f2177068
git push origin main
```

The Pages workflow stays the same (because the freeze commit changes
only docs and reports), so the live surface should remain stable across
this revert. Verify with the production health check.

The stable tag `v5.0-real-second-exhibition-deployment` continues to
point at `ac0f19e`, which is still in history. Any new freeze that is
built on top of this revert should publish its own annotated tag — see
the Tag and Release rule in
`docs/PUBLIC_DEPLOYMENT_MAINTENANCE_RUNBOOK_v5.5.md`.

## Post-rollback verification

After any rollback sequence:

```bash
gh run list --limit 5
python3 scripts/template_quality_gate.py
python3 scripts/second_exhibition_build_gate.py
python3 scripts/second_exhibition_repository_qa.py
sha256sum -c second-exhibition/assets/asset-checksums.sha256
python3 scripts/second_exhibition_production_healthcheck.py
SECOND_EXHIBITION_QA_URL="https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/" \
  node scripts/second_exhibition_browser_qa.mjs
```

Expected results depending on the rollback scope:

| Rollback | Root 200 | Root byte/hash preserved | `/second-exhibition/` |
|---|---|---|---|
| Latest content commit only | yes | yes | 200, baseline recovered |
| Deployment wiring chain | yes | yes (root is stable) | 404 (v5.0 surface withdrawn) |
| Freeze commit | yes | yes (freeze commit is docs-only) | 200, baseline recovered |

Confirm at the end:

- All pre-existing tags unchanged.
- All pre-existing Releases unchanged.
- Stable tag continues to point at `ac0f19e2c03b09738ae49b4a15c629a1f2177068`.
- Workflow file unchanged (`git diff` empty for `.github/workflows/`).
- `site/`, `second-exhibition/`, and the six images / manifest /
  checksums file are untouched unless that was the explicit purpose of
  the rollback.

## Evidence capture

Save the following into an incident report under `reports/`:

- The bad commit SHA and message.
- Each revert commit SHA and message (if applicable).
- GitHub Actions run IDs (before / after).
- HTTP response matrix (root, `/second-exhibition/`, 6 images, forbidden list).
- SHA-256 of all six images, before and after rollback.
- Browser QA output (5 viewports, console / page / failed requests,
  overflow counts).
- Root and second-exhibition byte counts, before and after rollback.
- A short timeline (UTC) of: incident detected, mitigation chosen, push
  performed, Pages deploy success, health check returned to 0.
- The freeze tag confirmation: `git cat-file -p
  v5.0-real-second-exhibition-deployment` shows type `tag` and target
  `ac0f19e2c03b09738ae49b4a15c629a1f2177068` throughout.
