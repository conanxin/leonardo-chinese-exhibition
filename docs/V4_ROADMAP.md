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

**Goal.** Apply the source-acceptance rule and the rights-risk register to every candidate asset from v4.1.

**Tasks.**

- For each `pending` row: verify the source URL is reachable, the rights statement is locatable, the credit line is composable, the source note is reconstructable, and the asset is not a search-result or memory import.
- Promote rows that pass all five checks to `verified` (Low or Medium).
- Downgrade rows that fail any check to `blocked` (High or Blocked) or `excluded`.
- Write the per-asset credit line verbatim from the source page's rights statement.
- Produce a single source-audit manifest, ordered by section.

**Do NOT do in v4.2.**

- Do not start the build.
- Do not "soft-include" any High / Blocked row by uncrediting or unfootnoting it.
- Do not move or rewrite any existing tag or GitHub Release.

**Exit criteria for v4.2.**

- Source-audit manifest exists with one row per asset.
- Zero `verified` rows are at High or Blocked.
- All `verified` rows carry all 14 metadata fields.
- `template_quality_gate.py` still PASS.
- Live byte size still **92,976 B**.

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

## v4.4 — QA and Stable Freeze

**Goal.** Run the full quality gate, confirm the live site is unaffected, and freeze a stable tag / GitHub Release for the second exhibition.

**Tasks.**

- Run `template_quality_gate.py` one final time.
- Confirm the existing live site (`site/`) is unchanged: byte size, v2.9 marker, `image-placeholder-pro` count, pilot title count.
- Confirm `_template/site/` and `_template/data/` are unchanged from the v3.4 baseline.
- Confirm `_pilots/second-exhibition-pilot/` is unchanged.
- Confirm the v4.3 working tree contains only `verified` rows from v4.2.
- Write `reports/leonardo_chinese_exhibition_v4_4_<short-name>_freeze_report.md` with the commit SHA + verified live byte + verified tag three-piece evidence (per the v3.4 freeze discipline).
- Create a tag for v4.4 (e.g., `v4.4-<short-name>`) only after the above passes.
- Create a GitHub Release for v4.4 only after the tag is verified.

**Do NOT do in v4.4.**

- Do not move or rewrite any pre-existing tag (`v2.0` through `v3.4`).
- Do not modify any pre-existing GitHub Release.
- Do not "publish" the new exhibition to the live site before the live-no-change check passes.

**Exit criteria for v4.4.**

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
| v4.4 | QA and Stable Freeze | No (still pilot-only) | Yes (v4.4) | Yes (v4.4) |

The second exhibition's live publication is **explicitly not on this roadmap**. v4.4 produces a tag and a Release that mark the *repository* state of the second exhibition, but the live site is not updated until a separate, future round explicitly authorizes live publication and runs the full source-and-rights audit a second time on the *to-be-deployed* working tree.