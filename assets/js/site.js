/* Site-wide behaviour. Loaded synchronously in <head>, BEFORE MathJax, so the
   configuration below is in place by the time MathJax boots. */

/* ---------------------------------------------------------------- MathJax */
/* Write LaTeX directly in the HTML of any page:
     inline   ->  $E = mc^2$        or  \(E = mc^2\)
     display  ->  $$ ... $$         or  \[ ... \]
     env      ->  \begin{align} ... \end{align}
   Anything inside <code> or <pre> is left alone, so you can show LaTeX
   source without it being typeset. */
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    tags: 'ams',
    macros: {
      RR: '{\\mathbb{R}}',
      NN: '{\\mathbb{N}}',
      ZZ: '{\\mathbb{Z}}',
      CC: '{\\mathbb{C}}',
      QQ: '{\\mathbb{Q}}',
      EE: '{\\mathbb{E}}',
      diff: ['{\\mathrm{d}#1}', 1],
      abs: ['{\\left|#1\\right|}', 1],
      norm: ['{\\left\\lVert#1\\right\\rVert}', 1],
      set: ['{\\left\\{#1\\right\\}}', 1],
      inner: ['{\\left\\langle#1\\right\\rangle}', 1]
    }
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    ignoreHtmlClass: 'no-mathjax',
    processHtmlClass: 'mathjax'
  },
  chtml: { displayAlign: 'left', displayIndent: '0' },
  startup: {
    typeset: true,
    ready: function () {
      MathJax.startup.defaultReady();
      document.documentElement.classList.add('mathjax-ready');
    }
  }
};

/* ------------------------------------------------------------ small stuff */
document.addEventListener('DOMContentLoaded', function () {
  // Current year in the footer.
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());

  // Mark the current tab, in case a page did not set aria-current itself.
  var here = location.pathname.replace(/\/index\.html$/, '/').replace(/\/+$/, '/');
  document.querySelectorAll('.nav a').forEach(function (link) {
    var there = link.pathname.replace(/\/index\.html$/, '/').replace(/\/+$/, '/');
    if (there === here && !document.querySelector('.nav a[aria-current]')) {
      link.setAttribute('aria-current', 'page');
    }
  });
});
