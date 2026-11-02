// Progressive enhancement only: the BibTeX block is fully readable and
// selectable without JavaScript, so the button is added only if JS runs.
(function () {
  var pre = document.getElementById('bibtex');
  if (!pre || !pre.parentNode) return;
  // No Clipboard API (file://, plain http, older browser) means no button,
  // rather than a button that looks live and does nothing.
  if (!navigator.clipboard || !navigator.clipboard.writeText) return;
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'copy';
  btn.textContent = 'Copy BibTeX';
  var reset = function () {
    setTimeout(function () { btn.textContent = 'Copy BibTeX'; }, 2000);
  };
  btn.addEventListener('click', function () {
    navigator.clipboard.writeText(pre.textContent).then(function () {
      btn.textContent = 'Copied';
      reset();
    }, function () {
      btn.textContent = 'Copy failed — select the text instead';
      reset();
    });
  });
  pre.parentNode.insertBefore(btn, pre);
})();
