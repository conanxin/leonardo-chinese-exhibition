/* leonardo-chinese-exhibition v2.2 — Exhibition Experience Upgrade
 * Native JS, no external deps.
 * - Lightbox: click any [data-lightbox] image (or any .artifact-image img)
 *   to open a full-view experience with title/subtitle/credit/viewing-note.
 * - ESC, click on backdrop, or X button to close.
 * - Mobile-friendly (touch / swipe).
 * - Fully progressive: if no lightbox images on page, does nothing.
 */

(function () {
  'use strict';

  // Resolve all lightbox-eligible images.
  // First: explicit data-lightbox images anywhere on the page.
  // Second: all .artifact-image > img (real manuscript images).
  // Third: .reading-image > img (reading-module thumbnails).
  function collectLightboxTargets() {
    const explicit = Array.from(document.querySelectorAll('img[data-lightbox]'));
    const artifactImgs = Array.from(document.querySelectorAll('.artifact-image img'))
      .filter((img) => !img.matches('[data-skip-lightbox]'));
    const readingImgs = Array.from(document.querySelectorAll('.reading-image img'));
    // De-duplicate by element reference
    const seen = new Set();
    const out = [];
    [...explicit, ...artifactImgs, ...readingImgs].forEach((img) => {
      if (seen.has(img)) return;
      seen.add(img);
      out.push(img);
    });
    return out;
  }

  // Build the lightbox DOM once, append to <body>.
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
        <button type="button" class="close-lightbox" aria-label="关闭 lightbox">×</button>
        <div class="lightbox-image"><img alt=""></div>
        <div class="lightbox-meta">
          <p class="lb-tag">展品细看</p>
          <h3 class="lb-title" id="lb-title"></h3>
          <p class="lb-subtitle"></p>
          <p class="lb-section-label">版权与来源</p>
          <p class="lb-credit"></p>
          <p class="lb-section-label">如何观看</p>
          <p class="lb-viewing"></p>
          <p class="lb-hint">提示：按 <strong>ESC</strong>、点空白处、或点 × 关闭。</p>
        </div>
      </div>`;
    document.body.appendChild(lb);
    return lb;
  }

  // Extract metadata from image, with sensible fallbacks.
  function readMetadata(img) {
    const alt = img.getAttribute('alt') || '';
    const dTitle = img.getAttribute('data-title');
    const dSubtitle = img.getAttribute('data-subtitle');
    const dCredit = img.getAttribute('data-credit');
    const dViewing = img.getAttribute('data-viewing');
    const dSection = img.getAttribute('data-section');

    // Try to find a sibling/parent .artifact-card and read its exhibit-title.
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
      subtitle:
        dSubtitle ||
        cardKind ||
        img.getAttribute('data-subtitle') ||
        alt.slice(0, 80) || '',
      credit:
        dCredit || extractNearestCreditLine(card) || '公共域 · Wikimedia Commons',
      viewing: dViewing || '把这张图当成一项独立的实验：先看构图、再看笔触密度、最后看达·芬奇留下了什么"未完成的推论"。',
      section: dSection || '未标注展区'
    };
  }

  function extractNearestCreditLine(card) {
    if (!card) return '';
    const el = card.querySelector('.credit-line');
    return el ? el.textContent.trim() : '';
  }

  // Open lightbox for a given image.
  function openLightbox(img) {
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
    // Move focus to close button for keyboard users
    const closeBtn = lb.querySelector('.close-lightbox');
    if (closeBtn) closeBtn.focus({ preventScroll: true });
  }

  function closeLightbox() {
    const lb = document.querySelector('.lightbox');
    if (!lb) return;
    lb.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lb-open');
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
      // Add data-section from the nearest section id
      if (!img.getAttribute('data-section')) {
        const sec = img.closest('section[id]');
        if (sec) img.setAttribute('data-section', sec.id);
      }
      img.addEventListener('click', (e) => {
        e.preventDefault();
        openLightbox(img);
      });
      img.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openLightbox(img);
        }
      });
    });

    // Close behaviors
    lb.addEventListener('click', (e) => {
      // Click on backdrop (not on panel / not on close button) closes
      if (e.target === lb) closeLightbox();
    });
    lb.querySelector('.close-lightbox').addEventListener('click', closeLightbox);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  // Init once DOM is parsed.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wireLightbox);
  } else {
    wireLightbox();
  }
})();
