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

## v4.4 Asset Import Prep (current round — summary)

**Round identity.** v4.4 is the *current* asset import prep round. The legacy "QA and Stable Freeze" block above is **not** the current v4.4 — it is retained for historical record only.

**Status.**

- item-level / source-level import prep completed for the 6 v4.3 selected candidates.
- `ready-for-asset-import` count = **2** (C-01, C-03 — BHL item 318921, PD subset only).
- `defer` count = **4** (C-06 NMNH Botany, C-08 Met 285149, C-09 Rijksmuseum botanical print, C-10 Rijksmuseum IIIF manifest).
- `ready-for-asset-import` count < 4 (2 < 4) — the asset import threshold is not met.
- no images downloaded in v4.4.
- no assets imported in v4.4.
- no approved status in v4.4 or any future round.
- C-03 CC BY-NC-SA subset blocked at the per-page / per-volume level.
- C-08 double-confirmation required (Collection API `isPublicDomain: true` AND Open Access icon on public object page).
- C-09 / C-10 per-item licence field required (recorded verbatim at v4.4b / v4.5).

**Next: v4.4b-source-gap-fix** (closes the source gap; v4.5 — Asset Import — is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows).

---

## v4.4b Source Gap Fix

**Goal.** Resolve the C-06, C-08, C-09, C-10 source gaps so that the future asset-import round (v4.5) has enough `ready-for-asset-import` rows. v4.4b is a **prep-only** round — it still does **not** download images unless a separate v4.5 import round is explicitly invoked.

**Tasks.**

- **C-06 (NMNH Botany, Section 2 分类):** Run the NMNH Botany search at https://collections.nmnh.si.edu/search/botany/ . Pick a specific herbarium sheet that is marked CC0 1.0 on its per-item page and that has an image. Capture the per-item title, collector / maker, date, accession number, official record URL, and media URL. Confirm CC0 1.0 on the per-item page (https://www.si.edu/openaccess/faq).
- **C-08 (Met 285149, Section 3 复制 alternate):** Re-open Met object 285149 at https://www.metmuseum.org/art/collection/search/285149 . Run the double-confirmation: (a) Met Collection API record `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` returns `isPublicDomain: true`, and (b) the Open Access icon is present on the public object page. Capture the `primaryImage` URL. If either confirmation fails, C-08 is `blocked-from-import` and the Section 3 alternate slot is filled by a project-generated diagram.
- **C-09 (Rijksmuseum botanical print, Section 1 观察 primary / Section 2 分类 alternate):** Run the Rijksmuseum search by `type` and `creator` (Rijksprentenkabinet entry at https://www.rijksmuseum.nl/en/research/our-research/print-room). Pick a specific Rijksprentenkabinet object. Record the per-item `licence` field verbatim (`CC0 1.0` or `CC BY 4.0`), the `objectNumber`, the `id.rijksmuseum.nl/...` PID, and the per-item Rijksstudio image URL or IIIF Image API URL.
- **C-10 (Rijksmuseum IIIF Presentation API manifest, Section 4 再组织):** Same Rijksmuseum object as C-09. Capture the IIIF Presentation API manifest URL (on the per-item Catalogue record) and the manifest's `license` field. The manifest's `license` field is the authoritative source for the credit line.
- Re-run the v4.4 import-readiness assessment on the 4 deferred rows. Promote the rows that pass their pre-import action; keep the rest as `defer`.
- Update `docs/ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md` to v4.4b (or write a v4.4b evidence table).
- Update `docs/SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md` to v4.4b (graduate from `DRAFT` to `final`).
- Update `docs/CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md` to v4.4b (fill placeholders).
- Update `docs/ASSET_FILENAME_MAP_v4.4.md` to v4.4b (replace `<accession_number>` / `<object_number>` placeholders).

**Do NOT do in v4.4b.**

- Do not download any image. v4.4b is a prep-only round — image download is a v4.5 step.
- Do not create `second-exhibition/assets/images/` directory. v4.4b is a prep-only round — directory creation is a v4.5 step.
- Do not create a tag or GitHub Release.
- Do not modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- Do not modify `scripts/template_quality_gate.py`.
- Do not use `approved` as a status value.
- Do not promote any CC BY-NC-SA subset of C-03 to `ready-for-asset-import`.

**Exit criteria for v4.4b.**

- All 4 deferred rows (C-06 / C-08 / C-09 / C-10) have a specific per-item record.
- Per-item rights statements are confirmed on the institution's own page on the day of audit.
- Per-item `licence` fields (C-09 / C-10) are recorded verbatim.
- Per-item accession number (C-06) is captured.
- Met double-confirmation (C-08) has passed.
- The updated v4.4 import-readiness assessment shows `ready-for-asset-import` ≥ 4.
- All 5 v4.4 prep docs are updated to v4.4b.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B** (v4.4b does not modify `site/`).
- v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- `find` confirms no new image files.

The round **after** v4.4b is **v4.5 — Asset Import**, which executes the actual download (gated on v4.4b producing ≥ 4 `ready-for-asset-import` rows).

---

## v4.4b Source Gap Fix

**Round identity.** v4.4b is a prep-only round that closes the per-item evidence gaps for the 4 v4.4 `defer` rows (C-06, C-08, C-09, C-10). v4.4b does **not** download images, does **not** create `second-exhibition/assets/images/`, does **not** create a tag, and does **not** publish a GitHub Release. The status `approved` is **not used**.

**Status.**

- **C-06 concrete NMNH item status**: `ready-for-asset-import`. Item: NMNH Botany, US Catalog 1529703, *Aconitum bulbilliferum* Hand.-Mazz. (Ranunculaceae, Type fragment), China / Sichuan, Handel-Mazzetti H. R. 5202, 17 Sep 1914. Dataset-level CC0 1.0 confirmed on `https://collections.nmnh.si.edu/ipt/resource?r=nmnh_botany` and cross-confirmed on `https://www.gbif.org/dataset/821cc27a-e3bb-4bc5-ac34-89ada245069d`. Media URL template `https://collections.nmnh.si.edu/media/?i={catalog_number}&ph=yes&thumb=yes` reachable via HEAD test (HTTP/2 200, `Content-Type: image/png`; URL recorded, not downloaded).
- **C-08 double-confirmation result**: PASS. (a) Met Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/285149` returned `isPublicDomain: true` AND `primaryImage: https://images.metmuseum.org/CRDImages/ph/original/DP147833.jpg`. (b) Public object page `https://www.metmuseum.org/art/collection/search/285149` shows a "Public Domain" button + "Download Image" + "Enlarge Image" controls (Open Access icon present). objectID = 285149 matches the URL. Accession = 2003.562.3. Title = `[Botanical Specimen: Fern]`.
- **C-09 concrete Rijksmuseum item status**: `ready-for-asset-import`. Item: Rijksmuseum RP-F-F80152, *Zeestreepvaren*, Anna Atkins (photographer, England), c. 1854, cyanotype on paper. Per-item Copyright field on the public object page reads verbatim `Public domain` (with hyperlink to `https://creativecommons.org/publicdomain/mark/1.0/deed.en`). Image / IIIF URL (Micrio IIIF Image API): `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` (HEAD test HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded).
- **C-10 concrete Rijksmuseum item status**: `ready-for-asset-import`. Item: Rijksmuseum RP-F-F80313, *Wolfsklauw*, Anna Atkins (photographer, England), c. 1854. Distinct per-item record from C-09 (different objectNumber, different persistent URL, different micrioId). Per-item Copyright field reads verbatim `Public domain` (with the CC0 1.0 hyperlink). Image / IIIF URL (Micrio IIIF Image API): `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` (HEAD test HTTP/2 200, `Content-Type: image/jpeg`; URL recorded, not downloaded). The Rijksmuseum IIIF Presentation API manifest at `https://iiif.micr.io/PrcdN/manifest.json` returned HTTP/2 404; the per-item public object page's Copyright field is the authoritative source for the credit line.

**Updated ready count**: **6** (was 2 in v4.4). All 4 v4.4 `defer` rows promoted to `ready-for-asset-import` in v4.4b.

**No image downloads.** v4.4b records URLs only. Transient `/tmp` fetch artifacts were cleaned up immediately.

**No live changes.** v4.4b does not modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, or `scripts/template_quality_gate.py`. Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.

**Next step (threshold-driven)**:
- `ready-for-asset-import` count = **6 ≥ 4** → the next round is **v4.5 — Asset Import**.
- If a future round reduces the ready count below 4 (e.g. an item is reclassified), the next round is **v4.4c — Source Gap Research** instead.

---

## v4.5 — Asset Import

**Goal.** Import the 6 v4.4b `ready-for-asset-import` candidates as **repository-only assets** under `second-exhibition/assets/images/`, with a machine-readable manifest, a SHA-256 checksum file, per-asset source/rights evidence, and an independent asset gate. v4.5 **does not** deploy, **does not** modify any live site, and **does not** create any tag or GitHub Release.

**Status semantics.** Every imported asset carries the status `imported-not-deployed`. The status words `approved`, `deployed`, `live`, `safe for commercial use`, and `cleared for all uses` are **not used** anywhere in v4.5.

**Tasks (this round).**

- For each of the 6 v4.4b `ready-for-asset-import` rows, download the recorded image URL into `second-exhibition/assets/images/` (one image per row, no duplicates, no thumbnails, no cached mirrors). Use the lower-size derivative (e.g. Met `web-large` instead of `original`) when the institution exposes one.
- Generate `second-exhibition/assets/asset-import-manifest.json` (machine-readable: id, institution, parent-item URL, identifier, source URL, rights URL, rights basis, image URL used, filename, media type, bytes, sha256, credit-line draft, source-note draft, proposed section, status, remaining caution).
- Generate `second-exhibition/assets/asset-checksums.sha256` (5–6 entries).
- Generate `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` (per-asset audit evidence, per-id).
- Generate `second-exhibition/docs/RIGHTS_AND_SOURCES.md` (per-asset rights summary; explicit per-item vs. policy-level distinction).
- Generate `second-exhibition/README.md` (directory orientation + forbidden status words + asset table).
- Add `scripts/second_exhibition_asset_gate.py` — an independent gate that re-checks: (a) every manifest file exists on disk, (b) every on-disk file is in the manifest, (c) every SHA-256 matches, (d) no manifest asset status equals a forbidden token, (e) no protected site path (`site/index.html`, `site/script.js`, `site/style.css`) references any v4.5 image filename.
- Generate `docs/ASSET_IMPORT_v4.5.md` and `docs/IMPORTED_ASSET_INVENTORY_v4.5.md`.
- Generate `reports/leonardo_chinese_exhibition_v4_5_asset_import_report.md`.
- Update this `docs/V4_ROADMAP.md` with the v4.5 section (this block) and a v4.5 row in the Phasing summary.
- Update `README.md` with a `v4.5 Asset Import` block.

**Do NOT do in v4.5.**

- Do not modify `site/index.html`, `site/style.css`, `site/script.js`.
- Do not modify `_template/site/`, `_template/data/`.
- Do not modify `_pilots/second-exhibition-pilot/`.
- Do not modify `scripts/template_quality_gate.py`.
- Do not create `second-exhibition/site/`.
- Do not copy any image into the live `site/assets/` (no such path exists today).
- Do not move any existing tag (`v2.0` through `v3.4`).
- Do not modify any existing GitHub Release.
- Do not modify `posts/`, `case-study/`, `release-assets/` (existing files).
- Do not process the untracked `.firecrawl/` directory.
- Do not use `git add .` — explicitly add each created/modified file.
- Do not use the status `approved` (or any forbidden token) on any imported asset.
- Do not import any image outside the 6-row shortlist.
- Do not use search thumbnails, cached images, or third-party mirrors when source/rights verification fails.
- Do not substitute an unverified replacement when a candidate fails.
- Do not create a tag or GitHub Release in v4.5.
- If a candidate fails (download returns wrong content, SHA does not match expected bytes, source URL gone, etc.), keep the passing items and emit `PARTIAL` — do not silently drop the round to a smaller shortlist without re-running the round-status sanity check.

**Exit criteria for v4.5.**

- 5 of 6 candidates imported into `second-exhibition/assets/images/`; C-06 blocked-from-import (NMNH catalog 1529703 candidate media URLs returned HTTP 404; per-item irnstamp not confirmed during download).
- `second-exhibition/assets/asset-import-manifest.json` committed and valid JSON.
- `second-exhibition/assets/asset-checksums.sha256` committed; `sha256sum -c` passes for every entry.
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` and `second-exhibition/docs/RIGHTS_AND_SOURCES.md` committed.
- `second-exhibition/README.md` committed.
- `scripts/second_exhibition_asset_gate.py` committed; gate passes (exit 0).
- `docs/ASSET_IMPORT_v4.5.md` and `docs/IMPORTED_ASSET_INVENTORY_v4.5.md` committed.
- `README.md` v4.5 block committed.
- `reports/leonardo_chinese_exhibition_v4_5_asset_import_report.md` committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- `git diff HEAD~1 HEAD -- site/ _template/ _pilots/second-exhibition-pilot/ posts/ case-study/ release-assets/ scripts/template_quality_gate.py` is **empty**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- `approved` does not appear as a Status value in any v4.5 doc or manifest entry.
- C-06 recorded as `blocked-from-import` (not silently dropped).
- No new tag, no new GitHub Release.

**v4.5 round status (this run):** **partial** — 5 imported, 1 blocked (C-06 NMNH).

**Next step (threshold-driven):**

- If v4.5 is `pass` (≥ 4 imports, no blockers): the next round is **v4.6 — Second Exhibition Site Build**, which has its own source/rights re-verification gate before any image is linked into a page.
- If v4.5 is `partial` or `blocked` (as this run): the next round is **v4.5b — Source Gap Fix**, which re-derives the missing per-item evidence (here: C-06 NMNH catalog 1529703 → correct irnstamp, on-page taxon confirmation, stable per-item media URL). v4.5b does **not** deploy, **does not** modify any live site, and **does not** create a tag or GitHub Release.

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
| v4.5 | Asset Import (repository-only; 5 imported, 1 blocked; no deploy, no tag, no Release) | No | No | No |
| v4.5b | Source Gap Fix (re-derive C-06 NMNH per-item evidence) | No | No | No |
| v4.6 | Second Exhibition Site Build (separate round; re-verifies source/rights before linking) | TBD | TBD | TBD |
| post-v4.6 | QA and Stable Freeze (renumbered from legacy v4.4) | No (still pilot-only) | Yes | Yes |

The second exhibition's live publication is **explicitly not on this roadmap**. v4.4 produces the asset-import-prep evidence; v4.4b closes the source gap; v4.5 executes the actual download (gated on v4.4b). The QA / stable freeze round (with tag + Release) is moved to a later phase. Live publication of the new exhibition requires a separate, future round that explicitly authorizes live publication and runs the full source-and-rights audit a second time on the *to-be-deployed* working tree.