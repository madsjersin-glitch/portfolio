// Small behaviours: screenshot strips, enlarge-on-click, opening a card from a link.
(function () {
  // Arrows on each screenshot strip
  document.querySelectorAll('.strip-wrap').forEach(function (wrap) {
    var strip = wrap.querySelector('.strip');
    var prev = wrap.querySelector('[data-dir="-1"]');
    var next = wrap.querySelector('[data-dir="1"]');
    if (!strip || !prev || !next) return;
    function update() {
      var max = strip.scrollWidth - strip.clientWidth - 2;
      prev.disabled = strip.scrollLeft <= 2;
      next.disabled = strip.scrollLeft >= max;
    }
    function slide(dir) {
      strip.scrollBy({ left: dir * Math.max(240, strip.clientWidth * 0.8), behavior: 'smooth' });
    }
    prev.addEventListener('click', function () { slide(-1); });
    next.addEventListener('click', function () { slide(1); });
    strip.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    var card = wrap.closest('details');
    if (card) card.addEventListener('toggle', function () { requestAnimationFrame(update); });
    update();
  });

  // Click a screenshot to enlarge it
  var box = document.getElementById('lightbox');
  if (box && box.showModal) {
    var img = box.querySelector('img');
    var cap = box.querySelector('[data-caption]');
    document.querySelectorAll('.shot button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var src = btn.querySelector('img');
        img.src = src.currentSrc || src.src;
        img.alt = src.alt;
        cap.textContent = btn.getAttribute('data-caption') || '';
        box.showModal();
      });
    });
    box.addEventListener('click', function (e) {
      if (e.target === box || e.target.closest('button')) box.close();
    });
  }

  // A link such as /#onboarding opens that card
  function openFromHash() {
    var id = location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (el && el.tagName === 'DETAILS') {
      el.open = true;
      el.scrollIntoView({ block: 'start' });
    }
  }
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
