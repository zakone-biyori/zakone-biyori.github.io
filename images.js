"use strict";
// Replace a slot automatically when an image is supplied at its documented path.
document.querySelectorAll("[data-image]").forEach(function (slot) {
  var img = new Image();
  img.alt = slot.textContent.trim();
  img.onload = function () { slot.replaceChildren(img); slot.classList.add("loaded"); };
  img.onerror = function () { /* Keep the neutral empty frame. */ };
  img.src = slot.dataset.image;
});
