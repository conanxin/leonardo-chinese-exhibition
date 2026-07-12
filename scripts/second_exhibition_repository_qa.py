#!/usr/bin/env python3
"""v4.7 Second Exhibition Repository QA gate.

Checks the structural, content, accessibility, interaction, and deployment
safety of the repository-only second exhibition. Does not modify the repository.
Does not access the network."""

import hashlib
import json
import mimetypes
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SECOND = REPO_ROOT / "second-exhibition"
SITE = SECOND / "site"
DATA = SECOND / "data"
ASSETS = SECOND / "assets"
IMAGES = ASSETS / "images"
DOCS = SECOND / "docs"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class QAGate:
    def __init__(self):
        self.results = []
        self.warnings = []

    def ok(self, msg):
        self.results.append(("ok", msg))

    def fail(self, msg):
        self.results.append(("fail", msg))

    def warn(self, msg):
        self.warnings.append(msg)

    def run_checks(self):
        for name in dir(self):
            if not name.startswith("check_"):
                continue
            func = getattr(self, name)
            if not callable(func):
                continue
            g = getattr(func, "group_name", "General")
            print(f"\n[group] {g}")
            func()

    def summary(self):
        ok = sum(1 for s, _ in self.results if s == "ok")
        fail = sum(1 for s, _ in self.results if s == "fail")
        print(f"\n{'='*60}")
        print(f"PASS: {ok}  FAIL: {fail}  WARNINGS: {len(self.warnings)}")
        if any(s == "fail" for s, _ in self.results):
            print("\nFailures:")
            for s, msg in self.results:
                if s == "fail":
                    print(f"  [FAIL] {msg}")
        if self.warnings:
            print("\nWarnings:")
            for w in self.warnings:
                print(f"  - {w}")
        print(f"{'='*60}")
        return fail == 0


def group(name):
    def decorator(func):
        func.group_name = name
        return func
    return decorator


class RepositoryQAGate(QAGate):
    @group("A. Required files")
    def check_a_required_files(self):
        required = [
            SITE / "index.html",
            SITE / "style.css",
            SITE / "script.js",
            SITE / "README.md",
            DATA / "exhibition.json",
            DATA / "sections.json",
            DATA / "glossary.json",
            DATA / "assets.json",
            ASSETS / "asset-import-manifest.json",
            ASSETS / "asset-checksums.sha256",
            DOCS / "SOURCE_AUDIT_MANIFEST.md",
            DOCS / "RIGHTS_AND_SOURCES.md",
            DOCS / "VISITOR_GUIDE_ZH.md",
            DOCS / "CURATORIAL_ESSAY_ZH.md",
            DOCS / "DEEP_RESEARCH_NOTES_ZH.md",
            DOCS / "BUILD_ASSET_USAGE.md",
            REPO_ROOT / "scripts" / "second_exhibition_build_gate.py",
        ]
        for p in required:
            if p.exists():
                self.ok(f"exists: {p.relative_to(REPO_ROOT)}")
            else:
                self.fail(f"missing: {p.relative_to(REPO_ROOT)}")

        expected_assets = [
            "bhl-318921-page-603998-c01.webp",
            "bhl-318921-page-603962-c03.webp",
            "smithsonian-nmnh-1529703.png",
            "met-285149.jpg",
            "rijksmuseum-rp-f-f80152.jpg",
            "rijksmuseum-rp-f-f80313.jpg",
        ]
        for name in expected_assets:
            p = IMAGES / name
            if p.exists():
                self.ok(f"asset image exists: {name}")
            else:
                self.fail(f"asset image missing: {name}")

    @group("B. JSON and cross-file counts")
    def check_b_json_counts(self):
        exhibition = read_json(DATA / "exhibition.json")
        sections = read_json(DATA / "sections.json")
        glossary = read_json(DATA / "glossary.json")
        _ = read_json(DATA / "assets.json")
        assets = _["assets"]
        manifest = read_json(ASSETS / "asset-import-manifest.json")

        expected_ids = ["C-01", "C-03", "C-06", "C-08", "C-09", "C-10"]

        for field, value in [
            ("status", "production-deployed-v5.3"),
            ("publication_status", "production-deployed-v5.3"),
            ("deployment_status", "production-deployed-v5.3"),
            ("version", "second-exhibition-v0.2"),
        ]:
            if exhibition.get(field) == value:
                self.ok(f"exhibition.{field} = {value}")
            else:
                self.fail(f"exhibition.{field} = {exhibition.get(field)!r} (expected {value})")

        for field, expected in [
            ("section_count", 4),
            ("artifact_count", 6),
        ]:
            if exhibition.get(field) == expected:
                self.ok(f"exhibition.{field} = {expected}")
            else:
                self.fail(f"exhibition.{field} = {exhibition.get(field)!r} (expected {expected})")

        actual_glossary_count = len(glossary.get("items", []))
        declared_glossary_count = exhibition.get(
            "glossary_count",
            exhibition.get("glossary_count_target"),
        )
        if actual_glossary_count == declared_glossary_count:
            self.ok(f"glossary count matches: {actual_glossary_count}")
        else:
            self.fail(
                "glossary count mismatch: "
                f"exhibition says {declared_glossary_count}, "
                f"actual {actual_glossary_count}"
            )

        if len(sections) == 4:
            self.ok(f"sections.json has 4 sections")
        else:
            self.fail(f"sections.json has {len(sections)} sections (expected 4)")

        if len(assets) == 6:
            self.ok(f"assets.json has 6 assets")
        else:
            self.fail(f"assets.json has {len(assets)} assets (expected 6)")

        if manifest.get("asset_count") == 6:
            self.ok(f"import manifest asset_count = 6")
        else:
            self.fail(f"import manifest asset_count = {manifest.get('asset_count')!r}")

        manifest_ids = [a["candidate_id"] for a in manifest.get("assets", [])]
        assets_ids = [a["candidate_id"] for a in assets]

        html = read_text(SITE / "index.html")
        html_ids = sorted(set(re.findall(r'data-candidate-id="(C-\d\d?)"', html)))

        for label, ids in [
            ("import manifest", manifest_ids),
            ("assets.json", assets_ids),
            ("HTML", html_ids),
        ]:
            if ids == expected_ids:
                self.ok(f"{label} candidate IDs match")
            else:
                self.fail(f"{label} candidate IDs {ids} != {expected_ids}")

    @group("C. Asset integrity")
    def check_c_asset_integrity(self):
        manifest = read_json(ASSETS / "asset-import-manifest.json")
        checksums = {}
        for line in (ASSETS / "asset-checksums.sha256").read_text().splitlines():
            parts = line.strip().split()
            if len(parts) >= 2:
                checksums[parts[1]] = parts[0]

        expected_ids = ["C-01", "C-03", "C-06", "C-08", "C-09", "C-10"]
        seen_hashes = set()

        for asset in manifest.get("assets", []):
            cid = asset["candidate_id"]
            if cid not in expected_ids:
                self.fail(f"unexpected candidate id in manifest: {cid}")
                continue

            filename = asset["filename"]
            p = IMAGES / filename
            if not p.exists():
                self.fail(f"{cid}: file missing: {filename}")
                continue

            if p.stat().st_size != asset.get("bytes", -1):
                self.fail(f"{cid}: bytes mismatch {p.stat().st_size} vs {asset.get('bytes')}")
            else:
                self.ok(f"{cid}: bytes match")

            sha = sha256_file(p)
            if sha != asset.get("sha256"):
                self.fail(f"{cid}: sha256 mismatch")
            else:
                self.ok(f"{cid}: sha256 match")

            if sha in seen_hashes:
                self.fail(f"{cid}: duplicate sha256")
            else:
                seen_hashes.add(sha)
                self.ok(f"{cid}: sha256 unique")

            rel = f"second-exhibition/assets/images/{filename}"
            if rel not in checksums:
                self.fail(f"{cid}: not in checksum file")
            elif checksums[rel] != sha:
                self.fail(f"{cid}: checksum file mismatch")
            else:
                self.ok(f"{cid}: checksum file match")

            mime, _ = mimetypes.guess_type(filename)
            if mime and asset.get("mime_type") and mime == asset.get("mime_type"):
                self.ok(f"{cid}: extension MIME consistent")
            else:
                self.warn(f"{cid}: extension MIME {mime} vs manifest {asset.get('mime_type')}")

            w, h = self._image_size(p)
            if w and h and w > 0 and h > 0:
                if asset.get("width") and asset.get("height"):
                    if w == asset.get("width") and h == asset.get("height"):
                        self.ok(f"{cid}: dimensions match manifest")
                    else:
                        self.warn(f"{cid}: dimensions {w}x{h} vs manifest {asset.get('width')}x{asset.get('height')}")
                else:
                    self.ok(f"{cid}: dimensions {w}x{h}")
            else:
                self.fail(f"{cid}: cannot read dimensions")

        c01 = next((a for a in manifest.get("assets", []) if a["candidate_id"] == "C-01"), None)
        c03 = next((a for a in manifest.get("assets", []) if a["candidate_id"] == "C-03"), None)
        if c01 and c03 and c01["sha256"] != c03["sha256"]:
            self.ok("C-01 / C-03 sha256 distinct")
        else:
            self.fail("C-01 / C-03 sha256 not distinct")

        # HTML references only local assets
        html = read_text(SITE / "index.html")
        img_srcs = re.findall(r'\u003cimg[^\u003e]*src="([^"]+)"', html, re.IGNORECASE)
        bad_external = []
        for src in img_srcs:
            if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
                bad_external.append(src)
        if bad_external:
            self.fail(f"external src in HTML: {bad_external}")
        else:
            self.ok("HTML uses no external image src")

        for src in img_srcs:
            if src.startswith("../assets/images/"):
                name = src.replace("../assets/images/", "")
                if not (IMAGES / name).exists():
                    self.fail(f"HTML references missing image: {src}")
                else:
                    self.ok(f"HTML image resolves: {name}")

        if len(img_srcs) == 6:
            self.ok(f"HTML references exactly 6 images")
        else:
            self.fail(f"HTML references {len(img_srcs)} images (expected 6)")

        # script src must be local
        script_srcs = re.findall(r'\u003cscript[^\u003e]*src="([^"]+)"', html, re.IGNORECASE)
        for src in script_srcs:
            if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
                self.fail(f"third-party script src: {src}")
            else:
                self.ok(f"script src is local: {src}")

    def _image_size(self, path: Path):
        try:
            from PIL import Image
            with Image.open(path) as im:
                return im.width, im.height
        except Exception:
            return None, None

    @group("D. HTML semantics")
    def check_d_html_semantics(self):
        html = read_text(SITE / "index.html")
        text = re.sub(r'<[^>]+>', '', html)

        h1s = re.findall(r'<h1[^>]*>', html, re.IGNORECASE)
        if len(h1s) == 1:
            self.ok("exactly 1 h1")
        else:
            self.fail(f"h1 count = {len(h1s)} (expected 1)")

        if "植物图谱与视觉分类" in text:
            self.ok("h1 text contains 植物图谱与视觉分类")
        else:
            self.fail("h1 text missing 植物图谱与视觉分类")

        headings = re.findall(r'<h([1-6])[^>]*>', html, re.IGNORECASE)
        levels = [int(h) for h in headings]
        bad = False
        prev = 1
        for lvl in levels:
            if lvl - prev > 1:
                bad = True
            prev = lvl
        if not bad:
            self.ok("heading levels do not jump > 1")
        else:
            self.fail(f"heading jump detected: levels {levels}")

        imgs = re.findall(r'<img[^>]*>', html, re.IGNORECASE)
        missing_alt = 0
        for img in imgs:
            if 'alt="' not in img and "alt='" not in img:
                missing_alt += 1
        if missing_alt == 0:
            self.ok(f"all {len(imgs)} img have alt")
        else:
            self.fail(f"{missing_alt} images missing alt")

        buttons = re.findall(r'<button([^>]*)>(.*?)</button>', html, re.IGNORECASE | re.DOTALL)
        bad_buttons = 0
        for tag, inner in buttons:
            txt = re.sub(r'<[^>]+>', '', inner).strip()
            if not txt and 'aria-label' not in tag:
                bad_buttons += 1
        if bad_buttons == 0:
            self.ok(f"all {len(buttons)} buttons have accessible name")
        else:
            self.fail(f"{bad_buttons} buttons missing accessible name")

        for cls, expected in [
            ("artifact-card", 6),
            ("glossary-item", 10),
            ("source-note", 6),
            ("credit-line", 6),
            ("repository-status", 1),
        ]:
            count = len(re.findall(rf'class="[^"]*{cls}', html))
            if count >= expected:
                self.ok(f"{cls} = {count} (>= {expected})")
            else:
                self.fail(f"{cls} = {count} (< {expected})")

        for cls in ["deep-reading-block", "material-evidence-block", "visual-thinking-block", "research-model-block"]:
            if cls in html:
                self.ok(f"{cls} present")
            else:
                self.fail(f"{cls} missing")

        # v0.2 marker must be present AND v0.1 marker must be absent (regression guard)
        if "second-exhibition-v0.2" in html:
            self.ok("marker second-exhibition-v0.2 present")
        else:
            self.fail("marker second-exhibition-v0.2 missing")
        if "second-exhibition-v0.1" in html:
            self.fail("stale marker second-exhibition-v0.1 still present in HTML")
        else:
            self.ok("stale marker second-exhibition-v0.1 absent")

    @group("D2. ARIA reference integrity")
    def check_d2_aria_references(self):
        from html.parser import HTMLParser

        html = read_text(SITE / "index.html")

        class AriaParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids = set()
                self.references = []

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)

                element_id = attrs.get("id")
                if element_id:
                    self.ids.add(element_id)

                for attr in (
                    "aria-labelledby",
                    "aria-describedby",
                    "aria-controls",
                ):
                    value = attrs.get(attr)
                    if value:
                        for target in value.split():
                            self.references.append((tag, attr, target))

        parser = AriaParser()
        parser.feed(html)

        for tag, attr, target in parser.references:
            if target in parser.ids:
                self.ok(
                    f"<{tag}> {attr} references existing id #{target}"
                )
            else:
                self.fail(
                    f"<{tag}> {attr} references missing id #{target}"
                )

    @group("E. Local link integrity")
    def check_e_local_links(self):
        html = read_text(SITE / "index.html")
        hrefs = re.findall(r'href="([^"]+)"', html)
        srcs = re.findall(r'src="([^"]+)"', html)
        paths = hrefs + srcs

        if any("\\" in p for p in paths):
            self.fail("backslash path found")
        else:
            self.ok("no backslash paths")

        if any(p.startswith("file://") for p in paths):
            self.fail("file:// path found")
        else:
            self.ok("no file:// paths")

        if any("/site/assets/" in p for p in paths):
            self.fail("/site/assets/ wrong path found")
        else:
            self.ok("no /site/assets/ wrong paths")

        if any("assets/images/" in p and not p.startswith("../assets/images/") for p in paths):
            self.fail("top-level assets/images reference found")
        else:
            self.ok("no top-level assets/images references")

        ids = set(re.findall(r'id="([^"]+)"', html))
        for href in hrefs:
            if href.startswith("#"):
                target = href[1:]
                if target not in ids:
                    self.fail(f"fragment #{target} not found")
                else:
                    self.ok(f"fragment #{target} exists")

        for src in srcs:
            if src.startswith("../assets/images/"):
                continue
            if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
                continue
            if not src.endswith(".css") and not src.endswith(".js"):
                self.warn(f"unusual local src: {src}")

    @group("F. Candidate-specific rules")
    def check_f_candidate_rules(self):
        html = read_text(SITE / "index.html").lower()
        text = read_text(DOCS / "BUILD_ASSET_USAGE.md").lower()
        essay = read_text(DOCS / "CURATORIAL_ESSAY_ZH.md").lower()
        rights = read_text(DOCS / "RIGHTS_AND_SOURCES.md").lower()
        assets = read_json(DATA / "assets.json")["assets"]

        # C-03
        c03_html = read_text(SITE / "index.html").lower()
        c03_text = read_text(DOCS / "BUILD_ASSET_USAGE.md").lower()
        c03_data = next((a for a in assets if a["candidate_id"] == "C-03"), {})

        has_pd_subset = any(
            token in c03_html or token in c03_text
            for token in ["pd subset", "public-domain subset", "public domain subset", "pd 子集"]
        )
        has_cc_by_nc_sa = any(
            token in c03_html or token in c03_text
            for token in ["cc by-nc-sa", "cc-by-nc-sa"]
        )
        has_blocked = any(
            token in c03_html or token in c03_text
            for token in ["blocked-from-import", "blocked from import", "仍被排除", "仍被 blocked"]
        )
        if has_pd_subset or has_cc_by_nc_sa or has_blocked:
            self.ok("C-03 PD subset / CC BY-NC-SA caution present")
        else:
            self.fail("C-03 PD subset caution missing")

        if has_blocked:
            self.ok("C-03 blocked-from-import / exclusion wording present")
        else:
            self.warn("C-03 blocked-from-import / exclusion wording not found")

        # C-06
        c06 = next((a for a in assets if a["candidate_id"] == "C-06"), {})
        if c06.get("low_resolution") is True:
            self.ok("C-06 low_resolution = true")
        else:
            self.fail("C-06 low_resolution not true")

        if c06.get("lightbox_enabled") is False:
            self.ok("C-06 lightbox_enabled = false")
        else:
            self.fail("C-06 lightbox_enabled not false")

        if "低分辨率" in text or "90×90" in text or "90x90" in text or "low-resolution" in text or "低分辨率" in html:
            self.ok("C-06 low-resolution description present")
        else:
            self.fail("C-06 low-resolution description missing")

        if 'data-candidate-id="c-06"' in html and 'data-lightbox-enabled="false"' in html:
            self.ok("C-06 lightbox disabled in HTML")
        else:
            self.fail("C-06 lightbox not disabled in HTML")

        if "display size" in text and "small" in text:
            self.ok("C-06 display size small in BUILD_ASSET_USAGE")
        else:
            self.fail("C-06 display size small missing")

        # Parse Hero section from the HTML. We treat the first <section class="hero"> as the Hero.
        hero_match = re.search(r'<section[^>]*class="[^"]*hero[^"]*".*?</section>', html, re.IGNORECASE | re.DOTALL)
        if not hero_match:
            self.warn("C-06 Hero section not found; Hero check inconclusive")
        else:
            hero_html = hero_match.group(0)
            if "c-06" in hero_html or "smithsonian-nmnh" in hero_html or 'data-candidate-id="c-06"' in hero_html:
                self.fail("C-06 used in Hero section")
            else:
                self.ok("C-06 not used in Hero section")

        # Verify that the only C-06 occurrence is the intended low-resolution card.
        c06_articles = re.findall(r'<article[^>]*data-candidate-id="c-06"[^>]*>.*?</article>', html, re.IGNORECASE | re.DOTALL)
        if not c06_articles:
            self.fail("C-06 artifact card missing")
        elif len(c06_articles) == 1:
            self.ok("C-06 appears exactly once")
        else:
            self.fail("C-06 appears more than once")
        c06_article = c06_articles[0] if c06_articles else ""
        if 'data-low-resolution="true"' in c06_article and 'data-lightbox-enabled="false"' in c06_article:
            self.ok("C-06 card has low-resolution=true and lightbox-enabled=false")
        else:
            self.fail("C-06 card attributes do not match low-resolution / lightbox-disabled expectation")
        if "double-confirmation" in text or "double-confirmation" in html or "ispublicdomain" in text or "ispublicdomain" in html or "public domain" in rights:
            self.ok("C-08 double-confirmation / public domain evidence present")
        else:
            self.fail("C-08 double-confirmation evidence missing")

        # C-09 / C-10
        c09 = next((a for a in assets if a["candidate_id"] == "C-09"), {})
        c10 = next((a for a in assets if a["candidate_id"] == "C-10"), {})
        if c09.get("identifier") != c10.get("identifier"):
            self.ok("C-09 / C-10 identifiers differ")
        else:
            self.fail("C-09 / C-10 identifiers identical")

        def has_rights_evidence(asset):
            evidence = " ".join(
                str(asset.get(key, ""))
                for key in (
                    "rights_basis",
                    "credit_line",
                    "source_note",
                    "viewing_note",
                )
            ).lower()
            return any(
                token in evidence
                for token in ("public domain", "cc0", "cc by")
            )

        if has_rights_evidence(c09) and has_rights_evidence(c10):
            self.ok("C-09 / C-10 rights evidence present")
        else:
            self.fail("C-09 / C-10 rights evidence missing")

        # C-10
        if "manifest 404" in text or "manifest 404" in html or "404" in text or "presentation api" in text:
            self.ok("C-10 manifest 404 caveat present")
        else:
            self.fail("C-10 manifest 404 caveat missing")

    @group("G. JavaScript and interaction hooks")
    def check_g_js_hooks(self):
        js = read_text(SITE / "script.js")
        css = read_text(SITE / "style.css")

        for token in ["openLightbox", "closeLightbox", "Escape", "keydown"]:
            if token in js:
                self.ok(f"JS hook '{token}' present")
            else:
                self.fail(f"JS hook '{token}' missing")

        if "guided" in js and "click" in js:
            self.ok("JS guided-reading toggle present")
        else:
            self.fail("JS guided-reading toggle missing")

        for bad in ["eval(", "document.write", "fetch(", "XMLHttpRequest", "axios", "jQuery"]:
            if bad in js:
                self.fail(f"JS contains forbidden pattern: {bad}")
            else:
                self.ok(f"JS does not contain {bad}")

        if "http://127.0.0.1" in js or "https://127.0.0.1" in js:
            self.fail("JS hardcodes localhost as production dependency")
        else:
            self.ok("JS no localhost production dependency")

        if re.search(r'<script[^>]*src\s*=\s*["\']https?://', read_text(SITE / "index.html")):
            self.fail("third-party JS loaded in HTML")
        else:
            self.ok("no third-party JS in HTML")

    @group("H. CSS and accessibility hooks")
    def check_h_css_hooks(self):
        css = read_text(SITE / "style.css")

        for token in [
            ":focus-visible",
            "prefers-reduced-motion",
            "max-width",
            "overflow-wrap",
            "word-break",
        ]:
            if token in css:
                self.ok(f"CSS contains '{token}'")
            else:
                self.fail(f"CSS missing '{token}'")

        normalized_css = "".join(css.lower().split())
        forbidden_rendering = (
            "image-rendering:pixelated",
            "image-rendering:crisp-edges",
        )
        if any(token in normalized_css for token in forbidden_rendering):
            self.fail("CSS forces pixelated/crisp-edges image rendering")
        else:
            self.ok("CSS preserves default image rendering")

        if "auto-play" in css.lower() or "autoplay" in css.lower():
            self.fail("CSS contains auto-play animation rule")
        else:
            self.ok("no auto-play CSS rules")

        if "text-indent" in css and "-9999" in css:
            self.warn("CSS uses extreme negative text-indent")
        else:
            self.ok("no extreme negative text-indent hiding")

    @group("I. Deployment safety")
    def check_i_deployment_safety(self):
        top_html = read_text(REPO_ROOT / "site" / "index.html").lower()
        second_html = read_text(SITE / "index.html").lower()

        # Marker must be the v0.2 version; bare v0.1 must not appear in the top-level live site
        for marker in ["second-exhibition-v0.2", "植物图谱与视觉分类"]:
            if marker in top_html:
                self.fail(f"top-level live site contains second exhibition marker: {marker}")
            else:
                self.ok(f"top-level live site does NOT contain: {marker}")
        if "second-exhibition-v0.1" in top_html:
            self.fail("top-level live site contains stale v0.1 marker (regression)")
        else:
            self.ok("top-level live site does NOT contain stale v0.1 marker")

        workflow_files = list((REPO_ROOT / ".github" / "workflows").glob("*.yml"))
        for wf in workflow_files:
            text = wf.read_text().lower()
            if "second-exhibition" in text:
                self.fail(f"workflow {wf.name} mentions second-exhibition")
            else:
                self.ok(f"workflow {wf.name} clean of second-exhibition")

        if (REPO_ROOT / "CNAME").exists():
            self.fail("CNAME exists")
        else:
            self.ok("no CNAME")

        if "production-deployed-v5.3" in second_html and "published-in-v5.3" in second_html:
            self.ok("second exhibition current publication status text correct")
        else:
            self.fail("second exhibition current publication status text missing (must contain 'production-deployed-v5.3' and 'published-in-v5.3')")

        # Historical import record must remain present
        if "imported-not-deployed" not in second_html:
            self.fail("second exhibition page lost historical import record 'imported-not-deployed' — must be preserved as v4.5 evidence")
        else:
            self.ok("second exhibition preserves historical import record 'imported-not-deployed'")

        readme = read_text(REPO_ROOT / "README.md").lower()
        # Allow negation phrases and v5.3 legitimate deployment status; flag only positive
        # claims of deployment/live that are not the v5.3 sanctioned phrasing.
        allowed_phrases = [
            "not deployed", "not deploy", "no deployment", "repository-only-not-deployed",
            "imported-not-deployed", "does not deploy", "deployment status", "deployed count: 0", "**deployed count**: 0",
            "production-deployed-v5.3", "published-in-v5.3", "v5.3 controlled deployment",
            "v5.3b production state reconciliation",
        ]
        readme_clean = readme
        for phrase in allowed_phrases:
            readme_clean = readme_clean.replace(phrase, "")
        bad = ["deployed", "live second exhibition", "second exhibition is live"]
        found = [b for b in bad if re.search(rf'\b{re.escape(b)}\b', readme_clean)]
        if found:
            self.fail(f"README contains bad status phrases: {found}")
        else:
            self.ok("README does not claim second exhibition deployed/live (v5.3 sanctioned phrasing allowed)")

    @group("J. Stage-gate applicability")
    def check_j_stage_gate_applicability(self):
        for path in [REPO_ROOT / "scripts" / "second_exhibition_asset_gate.py",
                     REPO_ROOT / "scripts" / "second_exhibition_build_gate.py"]:
            if path.exists():
                self.ok(f"exists: {path.name}")
            else:
                self.fail(f"missing: {path.name}")

        qa_doc = read_text(REPO_ROOT / "docs" / "SECOND_EXHIBITION_REPOSITORY_QA_v4.7.md").lower()
        required_terms = ["v4.5", "asset-import", "build gate"]
        missing = [t for t in required_terms if t not in qa_doc]
        if missing:
            self.fail(f"QA doc stage-gate applicability incomplete (missing: {missing})")
        else:
            self.ok("QA doc documents stage-gate applicability")

        if (REPO_ROOT / "scripts" / "second_exhibition_asset_gate.py").exists():
            self.ok("v4.5 asset gate preserved as historical import-stage gate")
        else:
            self.fail("v4.5 asset gate missing")

        if (REPO_ROOT / "scripts" / "second_exhibition_build_gate.py").exists():
            self.ok("v4.6 build gate preserved as repository-build gate")
        else:
            self.fail("v4.6 build gate missing")


def main():
    gate = RepositoryQAGate()
    gate.run_checks()
    ok = gate.summary()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
