# V4 Roadmap

> Scope of this document: phase v4.0 → v4.4 from planning to stable freeze for the second real exhibition. Companion to `docs/SECOND_EXHIBITION_PLAN_v4.0.md`, `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md`, `docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md`, and `docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md`.

---

## v4.0 — Real Second Exhibition Plan

**Goal.** Decide theme, source scope, rights posture, content outline, and execution roadmap *before* any download or page edit.

**Deliverables.**

- `docs/SECOND_EXHIBITION_PLAN_v4.0.md` — theme + MVE + non-goals.
- `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` — preferred source types + candidate institutions + required metadata per asset + source acceptance rule.
- `docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md` — risk levels + known risk categories + register table + release blocker rule.
- `docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md` — working title + sections + artifact types + glossary candidates + writing tasks.
- `docs/V4_ROADMAP.md` — this file.
- `README.md` updated with a `v4.0 Real Second Exhibition Plan` block.
- `reports/leonardo_chinese_exhibition_v4_0_real_second_exhibition_plan_report.md`.

**Do NOT do in v4.0.**

- Do not deploy.
- Do not download or import any real image.
- Do not create or modify `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`.
- Do not create a tag or GitHub Release.
- Do not move or rewrite any existing tag (`v2.0` through `v3.4`) or any existing GitHub Release.
- Do not modify `posts/`, `case-study/`, or `release-assets/`.

**Exit criteria for v4.0.**

- The five planning docs above committed.
- `README.md` v4.0 block committed.
- `scripts/template_quality_gate.py` → PASS, 37/37.
- `git diff` against `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` is empty.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**, pilot title in live still **0**.
- Report committed.
- No new tag, no new GitHub Release.

---

## v4.1 — Source Candidate Research

**Goal.** Populate the candidate source table for the recommended direction (botanical plates and visual taxonomy). **No download, no asset approval, no live change.**

**Tasks.**

- Research each of the six candidate institutions (BHL, Wellcome, Smithsonian Open Access, The Met Open Access, Rijksmuseum, Library of Congress) at the **collection / search-page level** — not the individual asset level.
- For each candidate institution: record overall rights posture, API or IIIF availability, per-item rights-metadata field, identifier persistence.
- Generate the source candidate table — at least 12 rows, ≥ 1 row per institution, every row's status is one of `candidate` / `needs rights audit` / `excluded` (never `approved`).
- Generate per-institution policy notes: official rights / terms URL, open-access / public-domain wording *as written*, attribution expectation, download / API note, uncertainty, v4.2 audit question.
- Generate the asset candidate matrix aligned with the v4.0 content outline's 4 sections (观察 / 分类 / 复制 / 再组织), with candidate asset types, possible source institutions, source / search URLs, rights risk, fit, and whether a project-generated diagram may substitute.
- Generate preliminary rights-screening decisions: `keep for v4.2 audit` / `exclude` / `replace with project-generated diagram`. **v4.1 does not approve any asset.** Low risk is still only a candidate. High-risk platform screenshots are replaced with project-generated diagrams by default.

**Deliverables (this round).**

- `docs/SOURCE_CANDIDATES_v4.1.md` — institution summaries + 10–12 candidate directions.
- `docs/SOURCE_CANDIDATE_TABLE_v4.1.md` — table with ≥ 12 rows, ≥ 1 per institution, status limited to `candidate` / `needs rights audit` / `excluded`.
- `docs/INSTITUTION_POLICY_NOTES_v4.1.md` — per-institution policy notes (no legal conclusions; exact wording recorded).
- `docs/ASSET_CANDIDATE_MATRIX_v4.1.md` — 4-section matrix with candidate asset types, source institutions, source / search URLs, rights risk, fit, and project-generated substitution guidance.
- `docs/RIGHTS_SCREENING_DECISIONS_v4.1.md` — preliminary decision rules + per-row table.
- `README.md` updated with a `v4.1 Source Candidate Research` block.
- `reports/leonardo_chinese_exhibition_v4_1_source_candidate_research_report.md`.

**Do NOT do in v4.1.**

- Do not download or import any image file into the working tree.
- Do not add any image file to the repository.
- Do not write into `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`.
- Do not modify `scripts/template_quality_gate.py`.
- Do not start the template instantiation.
- Do not mark any candidate `approved`. The status `approved` is **not used** in v4.1.
- Do not create a tag or GitHub Release.
- Do not move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.
- Do not process the untracked `.firecrawl/` directory.

**Exit criteria for v4.1.**

- All five v4.1 candidate docs (`SOURCE_CANDIDATES`, `SOURCE_CANDIDATE_TABLE`, `INSTITUTION_POLICY_NOTES`, `ASSET_CANDIDATE_MATRIX`, `RIGHTS_SCREENING_DECISIONS`) exist and are committed.
- `README.md` v4.1 block committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff` against `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**, pilot title in live still **0**.
- `find` confirms no new image files (`.jpg` / `.jpeg` / `.png` / `.webp` / `.tif` / `.tiff`).
- `approved` does not appear as a Status value in `SOURCE_CANDIDATE_TABLE_v4.1.md`.
- No new tag, no new GitHub Release.

---

## v4.2 — Rights Audit

**Goal.** Per-candidate verification of the 12-row v4.1 shortlist against 5 source-acceptance checks. **No download, no asset import, no live change.** The v4.2 statuses are `verified` / `needs clarification` / `blocked` / `excluded` — **`approved` is not used.**

**Tasks.**

- Re-open the official source page (or its API documentation) for each of the 12 v4.1 shortlist rows.
- Apply the 5 acceptance checks (source URL exists, rights statement exists, identifier exists, metadata sufficient, credit line basis).
- Assign each row one of the 4 v4.2 statuses. `verified` is granted only when the mechanism is in place (i.e., the institution's own page exposes a named rights statement, a persistent identifier, sufficient metadata, and a composable credit line) — per-item selection is deferred to v4.3.
- Produce a verified source shortlist (rows that may enter v4.3 build planning).
- Produce a blocked / excluded sources table (rows that did not pass, with follow-up actions).
- Update the rights risk register with per-row levels and open risks.

**Deliverables (this round).**

- `docs/SOURCE_ACCEPTANCE_CHECKS_v4.2.md` — 5 acceptance checks + status definitions.
- `docs/RIGHTS_AUDIT_v4.2.md` — 12-row per-candidate audit table.
- `docs/VERIFIED_SOURCE_SHORTLIST_v4.2.md` — verified candidates only.
- `docs/BLOCKED_OR_EXCLUDED_SOURCES_v4.2.md` — blocked / excluded / needs-clarification rows.
- `docs/RIGHTS_RISK_REGISTER_v4.2.md` — per-row risk levels + open risks + release blocker rule.
- `README.md` updated with a `v4.2 Rights Audit` block.
- `reports/leonardo_chinese_exhibition_v4_2_rights_audit_report.md`.

**Do NOT do in v4.2.**

- Do not download any image.
- Do not add any image file to the repository.
- Do not write into `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`.
- Do not modify `scripts/template_quality_gate.py`.
- Do not mark any candidate `approved`. The status `approved` is **not used** in v4.2.
- Do not create a tag or GitHub Release.
- Do not move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.
- Do not process the untracked `.firecrawl/` directory.

**Exit criteria for v4.2.**

- All five v4.2 candidate docs exist and are committed.
- `README.md` v4.2 block committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff` against `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**, pilot title in live still **0**.
- `find` confirms no new image files (`.jpg` / `.jpeg` / `.png` / `.webp` / `.tif` / `.tiff`).
- `approved` does not appear as a status value in any v4.2 doc.
- No new tag, no new GitHub Release.

**v4.2 → next round.**

- If the verified count is **≥ 4**, the next round is **v4.3 Second Exhibition Build Planning**.
- If the verified count is **< 4**, the next round is **v4.1b Source Candidate Research Extension**.

---

## v4.3 — Second Exhibition Build Planning

**Goal.** Turn the 6 v4.2 verified candidates into a build plan. **No download, no asset import, no live change.** The v4.3 statuses are `selected-for-build-planning` / `defer` / `replace-with-project-generated-diagram` / `blocked-from-build` — **`approved` is not used.**

**Tasks.**

- For each of the 6 v4.2 verified candidates, assign a v4.3 status.
- Build a 4-section scope with one primary candidate per section + 0–1 alternate + 1–2 project-generated diagrams per section.
- Record the per-item evidence plan (the dossier) so that a future asset-import round can re-check the same fields.
- Record the content draft brief (tone, hero, 3-minute guide, section briefs, artifact card briefs) so the future build round has a starting point.
- Record the asset import plan (the 11-step import rule, the per-candidate import table, the file naming convention).
- Make sure the C-03 CC BY-NC-SA subset is `blocked-from-build`.

**Deliverables (this round).**

- `docs/SECOND_EXHIBITION_BUILD_PLAN_v4.3.md` — candidate selection + minimum build set.
- `docs/ITEM_EVIDENCE_DOSSIER_v4.3.md` — per-candidate evidence plan (6 entries, one per `selected-for-build-planning` row).
- `docs/BUILD_SCOPE_v4.3.md` — section scope + page structure.
- `docs/CONTENT_DRAFT_BRIEF_v4.3.md` — tone + hero + 3-minute guide + section drafts + artifact card briefs.
- `docs/ASSET_IMPORT_PLAN_v4.3.md` — import rule + per-candidate import table + file naming convention.
- `README.md` updated with a `v4.3 Second Exhibition Build Planning` block.
- `reports/leonardo_chinese_exhibition_v4_3_second_exhibition_build_planning_report.md`.

**Do NOT do in v4.3.**

- Do not download any image.
- Do not add any image file to the repository.
- Do not write into `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`.
- Do not modify `scripts/template_quality_gate.py`.
- Do not mark any candidate `approved`. The status `approved` is **not used** in v4.3 or any future round.
- Do not pick a specific per-item selection (e.g., a specific BHL volume). Per-item selection is a v4.4 step.
- Do not write the section bodies, the hero, the 3-minute guide, the artifact card captions, the curatorial essay, or the source notes. The content draft is a *brief*; the actual writing is a future round.
- Do not draw any project-generated diagram. The diagrams are *planned*; the actual drawing is a future round.
- Do not re-introduce any `needs clarification` candidate as `selected-for-build-planning`.
- Do not re-introduce the v4.1 `replace with project-generated diagram` rows (C-02, Section-4 screenshot) as `selected-for-build-planning`.
- Do not re-introduce the v4.1 `excluded` row (C-14, BHL CC BY-NC-SA) as `selected-for-build-planning`.
- Do not create a tag or GitHub Release.
- Do not move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.
- Do not process the untracked `.firecrawl/` directory.

**Exit criteria for v4.3.**

- All five v4.3 planning docs exist and are committed.
- `README.md` v4.3 block committed.
- `docs/V4_ROADMAP.md` v4.3 section rewritten.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff` against `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**, pilot title in live still **0**.
- `find` confirms no new image files (`.jpg` / `.jpeg` / `.png` / `.webp` / `.tif` / `.tiff`).
- `selected-for-build-planning` count is **≥ 4**.
- `approved` does not appear as a status value in any v4.3 doc.
- C-03's `CC BY-NC-SA subset blocked` is recorded in the build plan.
- No new tag, no new GitHub Release.

**v4.3 → next round.**

- The next round is **v4.4 — Asset Import Prep** (or, equivalently, the round that does the actual image download per the asset import plan). v4.4 picks one specific item per `selected-for-build-planning` row and runs the 11-step import rule.

---

## v4.3 — Second Exhibition Build

**Goal.** Instantiate the template into a new second exhibition working directory and write the content.

**Tasks.**

- Instantiate the template into a new directory under a clearly-named path (e.g., `_exhibitions/second-botanical-taxonomy/` or equivalent; the exact path is decided in v4.3, not in v4.0).
- Copy approved assets into the local working tree.
- Write the hero, 3-minute guide, section bodies, artifact card captions, glossary, curatorial essay, source notes, credit lines, and rights notes — using only `verified` rows from v4.2.
- Local-render the exhibition locally (no live deploy).
- Run `template_quality_gate.py` against the new structure.

**Do NOT do in v4.3.**

- Do not push to `origin/main` from the live `site/` directory.
- Do not modify the existing pilot (`_pilots/second-exhibition-pilot/`).
- Do not modify `_template/site/` or `_template/data/`.
- Do not include any High / Blocked asset, even uncredited.

**Exit criteria for v4.3.**

- Local render renders cleanly with no broken images and no missing required text slots.
- `template_quality_gate.py` PASS.
- All required metadata, credit lines, source notes, and rights notes are present.
- No High / Blocked asset in the local working tree.

---

## v4.4 — Asset Import Prep (renumbered from earlier draft "QA and Stable Freeze")

> **v4.4 was redefined during v4.4 prep.** The earlier draft of this section named v4.4 "QA and Stable Freeze" and placed the QA freeze + tag + Release at v4.4. The actual v4.4 round is **Asset Import Prep** — it records per-item evidence, draft credit lines, draft source notes, and a filename map for the 6 v4.3 selected candidates. v4.4 does **not** download images, does **not** create a tag, and does **not** publish a GitHub Release. The QA / freeze round is moved to a later phase (post v4.5). The legacy "QA and Stable Freeze" content below is retained as a historical record of the *earlier* draft plan, with an explicit marker that the round was renamed.

**Goal (current v4.4).** Record per-item evidence for the 6 v4.3 `selected-for-build-planning` candidates so that a future asset-import round can execute the 11-step import rule. v4.4 only writes the *plan*; v4.4 does not download images.

**Tasks (current v4.4).**

- Re-open each v4.3 selected candidate's official page (BHL item 318921, NMNH Botany search, Met object 285149, Rijksprentenkabinet entry).
- Capture the 14 v4.4 per-item fields per row (item URL, institution, title, creator / maker, date, identifier, rights statement, rights / terms URL, image / IIIF URL pattern, proposed filename, alt text, caption, source note, credit line).
- Apply the 4 v4.4 statuses (`ready-for-asset-import` / `defer` / `blocked-from-import` / `replace-with-project-generated-diagram`). The status `approved` is **not used**.
- Produce 5 v4.4 prep docs in `docs/`: `ASSET_IMPORT_PREP_v4.4.md`, `ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md`, `SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md`, `CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md`, `ASSET_FILENAME_MAP_v4.4.md`.
- Write `reports/leonardo_chinese_exhibition_v4_4_asset_import_prep_report.md` with the commit SHA + verified live byte + verified quality-gate three-piece evidence.
- Update `README.md` v4.4 block to match the redefined scope (v4.4 does **not** download images).

**Do NOT do in v4.4 (current).**

- Do not download any image.
- Do not create any image file (`*.jpg` / `*.jpeg` / `*.png` / `*.webp` / `*.tif` / `*.tiff`).
- Do not modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- Do not modify `scripts/template_quality_gate.py`.
- Do not mark any candidate `approved`.
- Do not create a tag or GitHub Release in v4.4.
- Do not move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.

**Exit criteria for v4.4 (current).**

- All 5 v4.4 prep docs committed.
- `README.md` v4.4 block committed (and corrected: v4.4 does not download images).
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**, `image-placeholder-pro` still **0**.
- `find` confirms no new image files.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` is empty.
- `ready-for-asset-import` count is recorded (2 in this round, < 4 → v4.4b is the next round).
- `approved` does not appear as a status value in any v4.4 doc.
- v4.4 report carries the commit SHA + verified live byte + verified quality-gate three-piece.

---

## v4.4 (legacy draft, retained for historical record) — "QA and Stable Freeze"

> The following block was the original v4.4 definition in an earlier draft of `V4_ROADMAP.md`. It is **not** the current v4.4 — see "v4.4 — Asset Import Prep (renumbered from earlier draft "QA and Stable Freeze")" above for the current round. The legacy block is retained so that the QA / freeze plan is not silently dropped; it is now scheduled for a later phase (post v4.5).

**Goal (legacy draft).** Run the full quality gate, confirm the live site is unaffected, and freeze a stable tag / GitHub Release for the second exhibition.

**Tasks (legacy draft).**

- Run `template_quality_gate.py` one final time.
- Confirm the existing live site (`site/`) is unchanged: byte size, v2.9 marker, `image-placeholder-pro` count, pilot title count.
- Confirm `_template/site/` and `_template/data/` are unchanged from the v3.4 baseline.
- Confirm `_pilots/second-exhibition-pilot/` is unchanged.
- Confirm the v4.3 working tree contains only `verified` rows from v4.2.
- Write `reports/leonardo_chinese_exhibition_v4_4_<short-name>_freeze_report.md` with the commit SHA + verified live byte + verified tag three-piece evidence (per the v3.4 freeze discipline).
- Create a tag for v4.4 (e.g., `v4.4-<short-name>`) only after the above passes.
- Create a GitHub Release for v4.4 only after the tag is verified.

**Do NOT do in v4.4 (legacy draft).**

- Do not move or rewrite any pre-existing tag (`v2.0` through `v3.4`).
- Do not modify any pre-existing GitHub Release.
- Do not "publish" the new exhibition to the live site before the live-no-change check passes.

**Exit criteria for v4.4 (legacy draft).**

- Quality gate PASS.
- Live no-change confirmed (byte size still 92,976 B; markers unchanged).
- Tag exists, points to the v4.4 freeze commit, and is the latest tag in the project's history.
- GitHub Release exists and is marked Latest.
- Freeze report carries the commit SHA + verified live byte + verified tag three-piece.

---

## Phasing summary

| Phase | Theme | Deploy? | Tag? | Release? |
|---|---|---|---|---|
| v4.0 | Real Second Exhibition Plan | No | No | No |
| v4.1 | Source Candidate Research | No | No | No |
| v4.2 | Rights Audit | No | No | No |
| v4.3 | Second Exhibition Build | No (local render only) | No | No |
| v4.4 | Asset Import Prep (no download, no tag, no Release) | No (still pilot-only) | No | No |
| v4.4b | Source Gap Fix (per-item selection for the 4 deferred rows) | No | No | No |
| v4.5 | Asset Import (downloads the per-item images; gated on v4.4b producing ≥ 4 `ready-for-asset-import` rows) | TBD | TBD | TBD |
| post-v4.5 | QA and Stable Freeze (renumbered from legacy v4.4) | No (still pilot-only) | Yes | Yes |

The second exhibition's live publication is **explicitly not on this roadmap**. v4.4 produces the asset-import-prep evidence; v4.4b closes the source gap; v4.5 executes the actual download (gated on v4.4b). The QA / stable freeze round (with tag + Release) is moved to a later phase. Live publication of the new exhibition requires a separate, future round that explicitly authorizes live publication and runs the full source-and-rights audit a second time on the *to-be-deployed* working tree.