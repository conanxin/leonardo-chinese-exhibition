/* leonardo-chinese-exhibition
 * v2.2 — Exhibition Experience Upgrade (lightbox)
 * v2.5-real — Guided Tour + Interaction Accessibility
 *   - runtime-generated section-nav
 *   - tour progress bar (sticky, lightweight)
 *   - 5-min guided mode with skip notes
 *   - lightbox a11y: focus trap, focus return
 *   - image lazy-loading belt-and-suspenders
 * Native JS, no external deps.
 */

(function () {
  'use strict';

  // ============================================================
  // Lightbox (v2.2 baseline + v2.5-real a11y hardening)
  // ============================================================
  function collectLightboxTargets() {
    const explicit = Array.from(document.querySelectorAll('img[data-lightbox]'));
    const artifactImgs = Array.from(document.querySelectorAll('.artifact-image img'))
      .filter((img) => !img.matches('[data-skip-lightbox]'));
    const readingImgs = Array.from(document.querySelectorAll('.reading-image img'));
    const seen = new Set();
    const out = [];
    [...explicit, ...artifactImgs, ...readingImgs].forEach((img) => {
      if (seen.has(img)) return;
      seen.add(img);
      out.push(img);
    });
    return out;
  }

  let lastLightboxTrigger = null;

  function ensureLightboxDom() {
    let lb = document.querySelector('.lightbox');
    if (lb) return lb;
    lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-hidden', 'true');
    lb.setAttribute('aria-labelledby', 'lb-title');
    lb.innerHTML = `
      <div class="lightbox-panel" role="document">
        <button type="button" class="close-lightbox" aria-label="关闭展品大图">×</button>
        <div class="lightbox-image"><img alt=""></div>
        <div class="lightbox-meta">
          <p class="lb-tag">展品细看</p>
          <h3 class="lb-title" id="lb-title"></h3>
          <p class="lb-subtitle"></p>
          <p class="lb-section-label">版权与来源</p>
          <p class="lb-credit"></p>
          <p class="lightbox-viewing-label">观看提示</p>
          <p class="lb-viewing"></p>
          <p class="lb-hint">提示：按 <strong>ESC</strong>、点空白处、或点 × 关闭。</p>
        </div>
      </div>`;
    document.body.appendChild(lb);
    return lb;
  }

  function readMetadata(img) {
    const alt = img.getAttribute('alt') || '';
    const dTitle = img.getAttribute('data-title');
    const dSubtitle = img.getAttribute('data-subtitle');
    const dCredit = img.getAttribute('data-credit');
    const dViewing = img.getAttribute('data-viewing');
    const dSection = img.getAttribute('data-section');

    let cardTitle = '';
    let cardKind = '';
    const card = img.closest('.artifact-card, .reading-card');
    if (card) {
      const t = card.querySelector('.exhibit-title, .reading-title');
      const k = card.querySelector('.exhibit-kind, .reading-meta');
      if (t) cardTitle = t.textContent.trim();
      if (k) cardKind = k.textContent.trim();
    }

    return {
      title: dTitle || cardTitle || alt.split(/[，。·,]/)[0].trim() || '展品细看',
      subtitle: dSubtitle || cardKind || alt.slice(0, 80) || '',
      credit: dCredit || extractNearestCreditLine(card) || '公共域 · Wikimedia Commons',
      viewing: dViewing || '把这张图当成一项独立的实验：先看构图、再看笔触密度、最后看达·芬奇留下了什么"未完成的推论"。',
      section: dSection || '未标注展区'
    };
  }

  function extractNearestCreditLine(card) {
    if (!card) return '';
    const el = card.querySelector('.credit-line');
    return el ? el.textContent.trim() : '';
  }

  function openLightbox(img, triggerEl) {
    const lb = ensureLightboxDom();
    const meta = readMetadata(img);
    const panelImg = lb.querySelector('.lightbox-image img');
    panelImg.src = img.currentSrc || img.src;
    panelImg.alt = meta.title;
    lb.querySelector('.lb-title').textContent = meta.title;
    lb.querySelector('.lb-subtitle').textContent = meta.subtitle;
    lb.querySelector('.lb-credit').textContent = meta.credit;
    lb.querySelector('.lb-viewing').textContent = meta.viewing;
    lb.querySelector('.lb-tag').textContent =
      img.closest('.reading-card') ? '展品细读' : '展品细看 · ' + meta.section;
    lb.setAttribute('aria-hidden', 'false');
    document.body.classList.add('lb-open');
    lastLightboxTrigger = triggerEl || img;
    const closeBtn = lb.querySelector('.close-lightbox');
    if (closeBtn) closeBtn.focus({ preventScroll: true });
  }

  function closeLightbox() {
    const lb = document.querySelector('.lightbox');
    if (!lb) return;
    lb.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lb-open');
    if (lastLightboxTrigger && typeof lastLightboxTrigger.focus === 'function') {
      try { lastLightboxTrigger.focus({ preventScroll: true }); } catch (e) { /* ignore */ }
    }
    lastLightboxTrigger = null;
  }

  function wireLightbox() {
    const targets = collectLightboxTargets();
    if (targets.length === 0) return;

    ensureLightboxDom();
    const lb = document.querySelector('.lightbox');

    targets.forEach((img) => {
      img.setAttribute('role', 'button');
      img.setAttribute('tabindex', '0');
      img.setAttribute('aria-label', '点击放大查看：' + (img.getAttribute('alt') || '展品'));
      if (!img.getAttribute('data-section')) {
        const sec = img.closest('section[id]');
        if (sec) img.setAttribute('data-section', sec.id);
      }
      img.addEventListener('click', (e) => {
        e.preventDefault();
        openLightbox(img, img);
      });
      img.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openLightbox(img, img);
        }
      });
    });

    // Lightweight focus trap
    lb.addEventListener('keydown', (e) => {
      if (e.key !== 'Tab') return;
      const focusable = lb.querySelectorAll('button, [href], [tabindex]:not([tabindex="-1"])');
      if (focusable.length === 0) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });

    lb.addEventListener('click', (e) => {
      if (e.target === lb) closeLightbox();
    });
    lb.querySelector('.close-lightbox').addEventListener('click', closeLightbox);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lb.getAttribute('aria-hidden') === 'false') closeLightbox();
    });
  }

  // ============================================================
  // v2.5-real — Tour sections registry
  // ============================================================
  function getTourSections() {
    const allowedPrefixes = ['section1', 'section2', 'section3', 'section4',
      'section5', 'section6', 'section7', 'section8', 'section-1', 'section-2',
      'section-3', 'section-4', 'section-5', 'section-6', 'section-7', 'section-8'];
    const allowedIds = new Set(['intro', 'prologue', 'exhibit-index', 'visit-routes', 'sources']);
    return Array.from(document.querySelectorAll('main section[id], body > section[id]'))
      .filter((sec) => {
        if (!sec.id) return false;
        if (allowedIds.has(sec.id)) return true;
        return allowedPrefixes.some((p) => sec.id === p);
      });
  }

  function getSectionLabel(section) {
    if (!section) return '';
    if (section.dataset && section.dataset.sectionLabel) return section.dataset.sectionLabel;
    if (section.querySelector) {
      const h2 = section.querySelector('h2');
      if (h2 && h2.textContent) return h2.textContent.trim();
    }
    return section.id || '';
  }

  // ============================================================
  // v2.5-real — runtime section-nav
  // ============================================================
  function createSectionNav() {
    const sections = getTourSections();
    sections.forEach((section, index) => {
      if (section.querySelector('.section-nav')) return; // skip if already there

      const prev = sections[index - 1];
      const next = sections[index + 1];

      const nav = document.createElement('nav');
      nav.className = 'section-nav';
      nav.setAttribute('aria-label', '展区导览 · ' + getSectionLabel(section));

      const links = [];
      if (prev) {
        links.push(`<a class="section-nav-link" href="#${prev.id}">← 上一站：${getSectionLabel(prev)}</a>`);
      }
      links.push(`<a class="section-nav-link is-map" href="#exhibition-map">返回展览地图</a>`);
      if (next) {
        links.push(`<a class="section-nav-link" href="#${next.id}">下一站：${getSectionLabel(next)} →</a>`);
      }
      nav.innerHTML = links.join('');

      section.appendChild(nav);
    });
  }

  // ============================================================
  // v2.5-real — tour progress (sticky bar + jump list)
  // ============================================================
  function buildTourProgress() {
    const sections = getTourSections();
    if (sections.length === 0) return;

    const progressEl = document.querySelector('[data-tour-progress]');
    if (!progressEl) return;

    const currentLabel = progressEl.querySelector('[data-tour-current] .tour-current-label');
    const currentMeta = progressEl.querySelector('[data-tour-current-meta]');
    const fillEl = progressEl.querySelector('[data-tour-progress-fill]');
    const jumpList = progressEl.querySelector('[data-tour-jump-list]');

    // Build jump list
    jumpList.innerHTML = sections.map((sec, i) => {
      const label = getSectionLabel(sec) || sec.id;
      return `<li><a href="#${sec.id}" data-tour-jump="${sec.id}">${i + 1}. ${label}</a></li>`;
    }).join('');

    // Toggle jump list on current button click
    const currentBtn = progressEl.querySelector('[data-tour-current]');
    currentBtn.addEventListener('click', () => {
      const open = jumpList.getAttribute('data-open') === 'true';
      jumpList.setAttribute('data-open', open ? 'false' : 'true');
      currentBtn.setAttribute('aria-expanded', open ? 'false' : 'true');
    });

    // IntersectionObserver to update current section
    const setActive = (id) => {
      const idx = sections.findIndex((s) => s.id === id);
      if (idx < 0) return;
      const label = getSectionLabel(sections[idx]) || sections[idx].id;
      currentLabel.textContent = label;
      currentMeta.textContent = (idx + 1) + ' / ' + sections.length;
      fillEl.style.width = Math.round(((idx + 1) / sections.length) * 100) + '%';
      jumpList.querySelectorAll('a').forEach((a) => {
        if (a.getAttribute('data-tour-jump') === id) {
          a.setAttribute('aria-current', 'true');
        } else {
          a.removeAttribute('aria-current');
        }
      });
    };

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (visible && visible.target && visible.target.id) {
          setActive(visible.target.id);
        }
      },
      { rootMargin: '-30% 0px -50% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] }
    );
    sections.forEach((sec) => observer.observe(sec));

    // Initial state
    if (sections[0]) setActive(sections[0].id);
  }

  // ============================================================
  // v2.5-real — 5-min guided mode
  // ============================================================
  const GUIDED_HIGHLIGHT_IDS = new Set(['exhibit-index', 'section3', 'section4', 'section7']);

  function applyGuidedMode(active) {
    document.body.classList.toggle('guided-mode', active);
    // aria-pressed
    document.querySelectorAll('[data-guided-toggle]').forEach((btn) => {
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
    // Tag sections
    const sections = getTourSections();
    sections.forEach((sec) => {
      if (GUIDED_HIGHLIGHT_IDS.has(sec.id)) {
        sec.classList.add('guided-highlight');
        sec.classList.remove('guided-skip-note');
      } else {
        sec.classList.add('guided-skip-note');
        sec.classList.remove('guided-highlight');
      }
    });
    // Banner
    let banner = document.querySelector('.guided-mode-banner');
    if (active && !banner) {
      banner = document.createElement('div');
      banner.className = 'guided-mode-banner';
      banner.setAttribute('role', 'status');
      banner.setAttribute('aria-live', 'polite');
      banner.innerHTML = '<span>5 分钟导览模式已开启</span><button type="button" data-guided-exit>退出</button>';
      document.body.appendChild(banner);
      banner.querySelector('[data-guided-exit]').addEventListener('click', () => {
        applyGuidedMode(false);
      });
    } else if (!active && banner) {
      banner.remove();
    }
  }

  function wireGuidedMode() {
    document.addEventListener('click', (e) => {
      const t = e.target.closest('[data-guided-toggle]');
      if (t) {
        e.preventDefault();
        const active = !document.body.classList.contains('guided-mode');
        applyGuidedMode(active);
      }
    });
  }

  // ============================================================
  // v2.5-real — image lazy belt-and-suspenders
  // ============================================================
  function ensureLazyImages() {
    // The static HTML should already have loading="lazy" on non-hero imgs.
    // For any img that JS-injects (e.g. from data-src), set loading="lazy" by default.
    document.querySelectorAll('img').forEach((img) => {
      if (img.matches('[data-no-lazy]')) return;
      if (!img.hasAttribute('loading')) img.setAttribute('loading', 'lazy');
      if (!img.hasAttribute('decoding')) img.setAttribute('decoding', 'async');
    });
  }

  // ============================================================
  // Init
  // ============================================================
  function init() {
    ensureLazyImages();
    wireLightbox();
    createSectionNav();
    buildTourProgress();
    wireGuidedMode();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
