// Small behaviours: screenshot strips, enlarge-on-click with previous/next, opening a card from a link.
(function () {
  // Each strip: arrows step one image at a time, and a "2 of 5" count follows the scroll.
  document.querySelectorAll('.strip-wrap').forEach(function (wrap) {
    var strip = wrap.querySelector('.strip');
    var shots = Array.prototype.slice.call(strip.querySelectorAll('.shot'));
    var prev = wrap.querySelector('[data-dir="-1"]');
    var next = wrap.querySelector('[data-dir="1"]');
    var count = wrap.querySelector('.count');
    if (!strip || !shots.length) return;

    function current() {
      var left = strip.getBoundingClientRect().left;
      var best = 0, bestDist = Infinity;
      shots.forEach(function (s, i) {
        var d = Math.abs(s.getBoundingClientRect().left - left);
        if (d < bestDist) { bestDist = d; best = i; }
      });
      return best;
    }
    function update() {
      var max = strip.scrollWidth - strip.clientWidth - 2;
      var i = current();
      if (count) count.textContent = (i + 1) + ' of ' + shots.length;
      if (prev) prev.disabled = strip.scrollLeft <= 2;
      if (next) next.disabled = strip.scrollLeft >= max;
    }
    function go(i) {
      i = Math.max(0, Math.min(shots.length - 1, i));
      strip.scrollTo({ left: shots[i].offsetLeft - shots[0].offsetLeft, behavior: 'smooth' });
    }
    if (prev) prev.addEventListener('click', function () { go(current() - 1); });
    if (next) next.addEventListener('click', function () { go(current() + 1); });
    strip.addEventListener('scroll', function () { window.requestAnimationFrame(update); }, { passive: true });
    window.addEventListener('resize', update);
    var card = wrap.closest('details');
    if (card) card.addEventListener('toggle', function () { window.requestAnimationFrame(update); });
    update();
  });

  // Enlarge: steps through the images of the strip the click came from.
  var box = document.getElementById('lightbox');
  if (box && box.showModal) {
    var bigImg = box.querySelector('img');
    var cap = box.querySelector('[data-caption]');
    var desc = box.querySelector('[data-desc]');
    var cnt = box.querySelector('[data-count]');
    var stepPrev = box.querySelector('[data-step="-1"]');
    var stepNext = box.querySelector('[data-step="1"]');
    var group = [], index = 0, opener = null;

    function show(i) {
      index = Math.max(0, Math.min(group.length - 1, i));
      var btn = group[index];
      var src = btn.querySelector('img');
      bigImg.src = src.currentSrc || src.src;
      bigImg.alt = src.alt;
      cap.textContent = btn.getAttribute('data-caption') || '';
      desc.textContent = btn.getAttribute('data-desc') || '';
      cnt.textContent = group.length > 1 ? (index + 1) + ' of ' + group.length : '';
      stepPrev.hidden = stepNext.hidden = group.length < 2;
      stepPrev.disabled = index === 0;
      stepNext.disabled = index === group.length - 1;
    }
    document.querySelectorAll('.shot button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        group = Array.prototype.slice.call(btn.closest('.strip').querySelectorAll('.shot button'));
        opener = btn;
        show(group.indexOf(btn));
        box.showModal();
      });
    });
    stepPrev.addEventListener('click', function () { show(index - 1); });
    stepNext.addEventListener('click', function () { show(index + 1); });
    box.querySelector('[data-close]').addEventListener('click', function () { box.close(); });
    box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { e.preventDefault(); show(index - 1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); show(index + 1); }
    });
    box.addEventListener('close', function () { if (opener) opener.focus(); });
  }

  // A link such as /#onboarding opens that card.
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
