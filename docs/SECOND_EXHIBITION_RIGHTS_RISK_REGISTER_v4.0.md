# v4.0 Rights Risk Register

> Scope of this document: classify rights risk for any candidate asset of the second exhibition, and define the release blocker rule. Companion to `docs/SECOND_EXHIBITION_PLAN_v4.0.md` and `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md`.

---

## Risk levels

Every candidate asset is assigned exactly one risk level at the end of v4.2 audit. The four levels are:

| Level | Definition | Disposition |
|---|---|---|
| **Low** | Rights statement is clear, public domain or equivalent open license; credit line is straightforward; source note reconstructable. | Eligible for v4.3 build without further review. |
| **Medium** | Rights statement is clear but usage requires a specific credit string, attribution template, or non-commercial clause that must be preserved verbatim. | Eligible for v4.3 build **only if** the required credit string is recorded in the asset's metadata and reproduced verbatim in the rendered artifact card. |
| **High** | Rights statement is unclear, partially restricted, or has unresolved conflicts (e.g., institution terms + platform terms disagree). | **Not eligible** for v4.3 build. May be revisited in v4.5 or later; in v4.0–v4.4 it stays at `audit status = blocked`. |
| **Blocked** | Rights are clearly restrictive (e.g., "all rights reserved", no reuse clause, image not locatable, or terms explicitly forbid derivative use in this kind of exhibition). | **Permanently excluded** for v4.0–v4.4. Will not be revisited unless the source changes its terms. |

---

## Known risk categories

The following eight categories cover the risk surface observed in the v2.9 rights-audit and v3.4 hardening cycles. Any candidate asset must be checked against all eight before being labeled.

| # | Category | What it means | Typical default level |
|---|---|---|---|
| 1 | **public domain status unclear** | The work is old enough to *probably* be public domain, but the source page does not say so explicitly. | High |
| 2 | **institution terms restrict reuse** | The institution's terms page requires attribution, non-commercial use, or prohibits derivative works. | Medium–High |
| 3 | **platform screenshot ambiguity** | The image is reachable only through a third-party platform (e.g., a blog, a Pinterest board, a social-media post); the rights holder is the original creator, not the platform. | High |
| 4 | **missing image URL** | A collection page exists but no direct image URL (or IIIF service URL) is published. | Blocked |
| 5 | **missing object identifier** | The asset cannot be cited by a persistent identifier — only by a transient URL. | High |
| 6 | **derivative diagram not clearly labeled** | The asset is a project-generated diagram that has been combined with a third-party image without a clear separation layer. | High |
| 7 | **AI-generated or edited image unclear** | The asset is AI-generated or AI-edited, and the rights status of the underlying training material is not auditable. | Blocked (in v4.0–v4.4) |
| 8 | **no credit line** | The asset's rights statement is locatable, but no composable credit line can be written from the institution + rights statement + identifier. | High |
| 9 | **no source note** | The asset was located via a search result or memory, with no citable source page. | Blocked |

Categories 4, 7, and 9 are **immediate Blocked** by default. The remaining categories are **High by default** until evidence lowers them to Medium or Low.

---

## Risk register table

The risk register itself is *not* populated in v4.0 — there are no candidate assets yet. The schema is fixed here; v4.1 populates candidate rows; v4.2 promotes or downgrades them.

| ID | Asset / source candidate | Risk category | Risk level | Evidence | Decision | Follow-up owner | Status |
|---|---|---|---|---|---|---|---|
| (empty) | — | — | — | — | — | — | — |

When v4.1 begins, each row will be filled with one of the following statuses, never left blank:

- `pending` — evidence collected, level not yet assigned.
- `verified` — Low or Medium, all five source-acceptance criteria met.
- `blocked` — High or Blocked, ineligible for v4.3 build.
- `excluded` — Removed from scope for any reason (not just rights: scope, topic fit, availability).

---

## Release blocker rule

> **High / Blocked risk items cannot enter a stable release unless resolved or excluded.**

This rule is **hard**. It applies to:

- `v4.3` build (no High / Blocked asset enters the working tree).
- `v4.4` freeze (the manifest and source-audit table must show zero High / Blocked rows in the *accepted* set; High / Blocked rows may exist in the register, but only with status `blocked` or `excluded`, never `verified`).
- Any future tag / GitHub Release that references this exhibition's source list.

The rule has exactly three escape paths:

1. **Resolve.** New evidence lowers the asset to Low or Medium *and* the asset's metadata row carries the new evidence (rights statement copy, credit line, source note).
2. **Exclude.** The asset is moved to `audit status = excluded` with a one-line reason; it does not enter the build and does not appear in the manifest.
3. **Defer.** The asset is moved to `audit status = blocked` and tagged for a future round (v4.5 or later); it does not enter the v4.4 build.

No fourth path exists. Specifically: **a High or Blocked asset cannot be "soft-included" by being uncredited or unfootnoted**. If the audit cannot reach a clean Low or Medium, the asset does not enter the release.

---

## Relation to the source-scope rule

The rights-risk register operates on assets that have already passed the **source-acceptance rule** defined in `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md`. In other words:

- The source-scope doc says *what may enter the candidate set*.
- This register says *what may enter the build, once in the candidate set*.

The two documents together form the source-and-rights gate. v4.3 build is allowed to read assets only from the intersection: in the candidate set, AND at Low or Medium, AND with all five source-acceptance criteria recorded.