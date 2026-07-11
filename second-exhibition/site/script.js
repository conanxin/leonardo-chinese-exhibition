// Second Exhibition (v0.1) — repository-only page script.
// No third-party JS. No network requests. No auto-play.
// Pure DOM enhancement: lightbox open/close, ESC handler, guided-mode toggle.

(function () {
  "use strict";

  var lightbox = document.getElementById("lightbox");
  var lightboxImg = document.getElementById("lightbox-img");
  var lightboxCaption = document.getElementById("lightbox-caption");
  var lightboxSourceNote = document.getElementById("lightbox-source-note");
  var lightboxCreditLine = document.getElementById("lightbox-credit-line");
  var guidedToggle = document.getElementById("guided-toggle");
  var guidedBanner = document.getElementById("guided-mode-banner");

  function openLightbox(card) {
    if (!lightbox || !lightboxImg) return;
    var img = card.querySelector("img");
    if (!img) return;
    var caption = card.querySelector(".caption");
    var sourceNote = card.querySelector(".source-note");
    var creditLine = card.querySelector(".credit-line");
    lightboxImg.src = img.src;
    lightboxImg.alt = img.alt || "";
    lightboxCaption.textContent = caption ? caption.textContent : "";
    lightboxSourceNote.innerHTML = sourceNote ? sourceNote.innerHTML : "";
    lightboxCreditLine.innerHTML = creditLine ? creditLine.innerHTML : "";
    lightbox.hidden = false;
    lightbox.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    var closeBtn = lightbox.querySelector(".lightbox-close");
    if (closeBtn) {
      closeBtn.focus();
    }
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.hidden = true;
    lightbox.setAttribute("aria-hidden", "true");
    lightboxImg.src = "";
    document.body.style.overflow = "";
  }

  function attachArtifactCardListeners() {
    var cards = document.querySelectorAll(".artifact-card");
    Array.prototype.forEach.call(cards, function (card) {
      var enabled = card.getAttribute("data-lightbox-enabled") === "true";
      if (!enabled) return;
      var img = card.querySelector("img");
      if (!img) return;
      img.addEventListener("click", function () {
        openLightbox(card);
      });
      img.addEventListener("keydown", function (ev) {
        if (ev.key === "Enter" || ev.key === " ") {
          ev.preventDefault();
          openLightbox(card);
        }
      });
      img.setAttribute("tabindex", "0");
      img.setAttribute("role", "button");
      img.setAttribute("aria-label", "在 lightbox 中查看 " + (card.getAttribute("data-candidate-id") || ""));
    });
  }

  function attachLightboxListeners() {
    if (!lightbox) return;
    var closers = lightbox.querySelectorAll("[data-lightbox-close]");
    Array.prototype.forEach.call(closers, function (el) {
      el.addEventListener("click", function () {
        closeLightbox();
      });
    });
  }

  function attachEscListener() {
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" || ev.key === "Esc") {
        if (lightbox && !lightbox.hidden) {
          closeLightbox();
        }
      }
    });
  }

  function attachGuidedToggle() {
    if (!guidedToggle || !guidedBanner) return;
    guidedToggle.addEventListener("click", function () {
      var pressed = guidedToggle.getAttribute("aria-pressed") === "true";
      var next = !pressed;
      guidedToggle.setAttribute("aria-pressed", next ? "true" : "false");
      guidedToggle.textContent = next ? "关闭导览模式" : "开启导览模式";
      guidedBanner.hidden = !next;
    });
  }

  function init() {
    attachArtifactCardListeners();
    attachLightboxListeners();
    attachEscListener();
    attachGuidedToggle();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();