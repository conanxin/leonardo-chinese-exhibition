/* v3.1 second exhibition pilot — minimal JS
   目标：验证模板骨架的 JS 占位（section nav / lightbox placeholder / guided-mode placeholder）可独立运行。
   不引用 live site script.js。 */

(function () {
  'use strict';

  // 1. section nav active state（占位）
  // - 给当前 viewport 内的 section 加上 .is-active 类
  // - 这是模板的轻量占位实现，不依赖外部库
  function initSectionNav() {
    var sections = document.querySelectorAll('.pilot-section, .pilot-map, .pilot-glossary, .pilot-rights');
    if (!sections.length) return;
    var navLinks = document.querySelectorAll('.pilot-quick a');
    if (!navLinks.length) return;

    function update() {
      var scrollY = window.scrollY || window.pageYOffset;
      var currentId = null;
      sections.forEach(function (sec) {
        var top = sec.offsetTop;
        if (scrollY + 120 >= top) {
          currentId = sec.id;
        }
      });
      navLinks.forEach(function (a) {
        var href = a.getAttribute('href') || '';
        if (href === '#' + currentId) {
          a.style.background = 'rgba(75,58,42,0.12)';
        } else {
          a.style.background = '';
        }
      });
    }
    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  // 2. lightbox placeholder（占位）
  // - 模板演示用：点击 .template-artifact-card img 时打开一个简单 overlay
  // - 真实展览中可被替换为更复杂的实现
  function initLightboxPlaceholder() {
    var imgs = document.querySelectorAll('.template-artifact-card img');
    if (!imgs.length) return;

    imgs.forEach(function (img) {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function () {
        var overlay = document.createElement('div');
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-label', 'lightbox');
        overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.85);display:flex;align-items:center;justify-content:center;z-index:9999;padding:1.5rem;';
        var big = document.createElement('img');
        big.src = img.src;
        big.alt = img.alt;
        big.style.cssText = 'max-width:95vw;max-height:95vh;background:#fff;padding:0.5rem;';
        overlay.appendChild(big);
        overlay.addEventListener('click', function () {
          document.body.removeChild(overlay);
        });
        document.body.appendChild(overlay);
      });
    });
  }

  // 3. guided-mode placeholder（占位）
  // - 模板演示用：连续滚动所有 section，每节停顿 8 秒
  // - 当前 pilot 不启用（仅留函数作为占位），由具体展览项目决定是否激活
  function guidedModePlaceholder() {
    /* eslint-disable no-unused-vars */
    var stop = function () { /* stop scrolling */ };
    var start = function () { /* start auto-scroll */ };
    return { start: start, stop: stop };
  }

  // 4. accessibility helper（占位）
  // - 监听 Tab 键，给键盘焦点元素加 .is-focused
  function initA11yHelper() {
    function onKeydown(e) {
      if (e.key === 'Tab') {
        document.body.classList.add('is-keyboard-nav');
      }
    }
    function onMousedown() {
      document.body.classList.remove('is-keyboard-nav');
    }
    document.addEventListener('keydown', onKeydown);
    document.addEventListener('mousedown', onMousedown);
  }

  // 5. pilot-v0.1 marker console（占位）
  // - 模板约定：每个 pilot 启动时在 console 打印自己的 marker，便于审计
  function announcePilot() {
    if (window.console && console.log) {
      console.log('pilot-v0.1 · v3.1 second exhibition pilot · source template: v3.0-real-template-extraction-audit');
    }
  }

  // bootstrap
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initSectionNav();
      initLightboxPlaceholder();
      initA11yHelper();
      announcePilot();
    });
  } else {
    initSectionNav();
    initLightboxPlaceholder();
    initA11yHelper();
    announcePilot();
  }

  // expose guided-mode placeholder for projects that want to wire it up
  window.__pilotGuidedMode = guidedModePlaceholder();
})();
