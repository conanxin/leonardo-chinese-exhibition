/* =============================================================
 * 中文数字展览模板 / Chinese Digital Exhibition Template
 * Source case: v2.9-real-source-rights-audit
 * Template version: v3.0-template-skeleton
 *
 * 骨架脚本。特点：
 * - 无外部依赖
 * - 仅占位函数：section-nav / lightbox / guided-mode / a11y
 * - 不绑定任何具体 section id 或项目专属选择器
 * - 不从站点文本读取 Leonardo / Codex Atlanticus 等项目专属词
 * - 项目接入时只需在 init() 处绑定具体 section id
 * ============================================================= */

(function () {
  'use strict';

  // ---------- Accessibility helpers ----------
  function prefersReducedMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function trapFocus(container) {
    if (!container) return function () {};
    var focusable = container.querySelectorAll(
      'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'
    );
    if (!focusable.length) return function () {};
    var first = focusable[0];
    var last = focusable[focusable.length - 1];
    function handler(event) {
      if (event.key !== 'Tab') return;
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
    container.addEventListener('keydown', handler);
    return function release() {
      container.removeEventListener('keydown', handler);
    };
  }

  // ---------- Section nav placeholder ----------
  // 真实项目应在此处绑定具体 section id 与高亮规则。
  // 当前骨架仅演示 IntersectionObserver 注册方式。
  function initSectionNav() {
    var sections = document.querySelectorAll('[data-section-id]');
    if (!sections.length || !('IntersectionObserver' in window)) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in-view');
        }
      });
    }, {
      rootMargin: '0px 0px -40% 0px',
      threshold: 0.1
    });

    sections.forEach(function (section) {
      observer.observe(section);
    });
  }

  // ---------- Lightbox placeholder ----------
  // 真实项目应在此处绑定 artifact-card 点击 → 打开 lightbox。
  // 当前骨架仅暴露 open/close API。
  var lightboxEl = null;
  var lightboxImg = null;
  var lightboxCaption = null;
  var lightboxCredit = null;
  var lightboxCloseBtn = null;
  var lightboxReleaseFocus = null;

  function openLightbox(imageSrc, alt, caption, credit) {
    if (!lightboxEl) return;
    lightboxImg.src = imageSrc;
    lightboxImg.alt = alt || '';
    lightboxCaption.textContent = caption || '';
    lightboxCredit.textContent = credit || '';
    lightboxEl.hidden = false;
    lightboxReleaseFocus = trapFocus(lightboxEl);
    lightboxCloseBtn && lightboxCloseBtn.focus();
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightboxEl) return;
    lightboxEl.hidden = true;
    lightboxImg.src = '';
    lightboxImg.alt = '';
    lightboxCaption.textContent = '';
    lightboxCredit.textContent = '';
    document.body.style.overflow = '';
    if (lightboxReleaseFocus) {
      lightboxReleaseFocus();
      lightboxReleaseFocus = null;
    }
  }

  function initLightbox() {
    lightboxEl = document.getElementById('lightbox');
    if (!lightboxEl) return;
    lightboxImg = lightboxEl.querySelector('.lightbox-image');
    lightboxCaption = lightboxEl.querySelector('.lightbox-caption');
    lightboxCredit = lightboxEl.querySelector('.lightbox-credit');
    lightboxCloseBtn = lightboxEl.querySelector('.lightbox-close');

    if (lightboxCloseBtn) {
      lightboxCloseBtn.addEventListener('click', closeLightbox);
    }
    lightboxEl.addEventListener('click', function (event) {
      if (event.target === lightboxEl) closeLightbox();
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && lightboxEl && !lightboxEl.hidden) {
        closeLightbox();
      }
    });

    // 真实项目在此处绑定：
    // document.querySelectorAll('.artifact-card img').forEach(function (img) {
    //   img.addEventListener('click', function () {
    //     var card = img.closest('.artifact-card');
    //     openLightbox(
    //       img.getAttribute('src'),
    //       img.getAttribute('alt'),
    //       card && card.querySelector('.artifact-caption') && card.querySelector('.artifact-caption').textContent,
    //       card && card.querySelector('.credit-line') && card.querySelector('.credit-line').textContent
    //     );
    //   });
    // });
  }

  // ---------- Guided mode placeholder ----------
  // 真实项目应在此处绑定具体步骤列表。
  var guidedEl = null;
  var guidedSteps = null;
  var guidedCurrent = 0;

  function showGuidedStep(index) {
    if (!guidedSteps || !guidedSteps.length) return;
    guidedCurrent = (index + guidedSteps.length) % guidedSteps.length;
    guidedSteps.forEach(function (el, i) {
      el.classList.toggle('is-active', i === guidedCurrent);
    });
    var target = guidedSteps[guidedCurrent];
    if (target && target.dataset && target.dataset.targetId) {
      var destination = document.getElementById(target.dataset.targetId);
      if (destination) {
        destination.scrollIntoView({
          behavior: prefersReducedMotion() ? 'auto' : 'smooth',
          block: 'start'
        });
      }
    }
  }

  function exitGuidedMode() {
    if (!guidedEl) return;
    guidedEl.hidden = true;
    guidedCurrent = 0;
  }

  function initGuidedMode() {
    guidedEl = document.getElementById('guided-mode');
    if (!guidedEl) return;
    guidedSteps = guidedEl.querySelectorAll('.guided-steps li');

    var prevBtn = guidedEl.querySelector('.guided-prev');
    var nextBtn = guidedEl.querySelector('.guided-next');
    var exitBtn = guidedEl.querySelector('.guided-exit');

    if (prevBtn) prevBtn.addEventListener('click', function () { showGuidedStep(guidedCurrent - 1); });
    if (nextBtn) nextBtn.addEventListener('click', function () { showGuidedStep(guidedCurrent + 1); });
    if (exitBtn) exitBtn.addEventListener('click', exitGuidedMode);
  }

  // ---------- Bootstrap ----------
  function init() {
    initSectionNav();
    initLightbox();
    initGuidedMode();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();