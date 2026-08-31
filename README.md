# rezakaze.github.io

A hand-written static site — plain HTML and CSS, no Jekyll, no build step, no
dependencies to install. Edit a file, commit, push; GitHub Pages serves it as-is.

The `.nojekyll` file at the repo root is what tells GitHub Pages to skip Jekyll
processing entirely. Don't delete it.

## Pages

| File | Tab |
| --- | --- |
| `index.html` | About — bio and links to the other tabs |
| `classes.html` | Classes taken, by term, with links to notes |
| `research.html` | Research projects, each with a description |
| `blog.html` | Blog post index |
| `404.html` | Shown for any URL that doesn't exist |

Longer content lives one directory down:

- `blog/` — one HTML file per post, plus `_template.html` to copy
- `notes/` — one HTML file per set of course notes, plus `_template.html`

Shared assets:

- `assets/css/style.css` — the whole stylesheet
- `assets/js/site.js` — MathJax configuration, LaTeX macros, footer year
- `assets/favicon.svg`
- `assets/vendor/mathjax/` — MathJax 3.2.2, self-hosted (Apache-2.0, license
  included). Nothing is loaded from a CDN, so the site has no external runtime
  dependency and renders offline. To upgrade: `npm pack mathjax@<version>`, then
  replace `tex-chtml.js` and `output/chtml/fonts/woff-v2/` with the copies from
  the tarball's `package/es5/`.

## Writing LaTeX

Type LaTeX straight into the HTML. A self-hosted copy of MathJax typesets it in
the browser on every page — no CDN, no network dependency at page load.

- Inline: `$e^{i\pi} + 1 = 0$` or `\(e^{i\pi} + 1 = 0\)`
- Display: `$$ ... $$` or `\[ ... \]`
- Environments: `\begin{align} ... \end{align}`, `pmatrix`, `cases`, and so on

Wrap display math in `<div class="math-block">` so it scrolls sideways on a phone
instead of overflowing the page.

Two things to know:

- A bare `$` starts inline math. Write a literal dollar sign as `\$`.
- Anything inside `<code>` or `<pre>` is **not** typeset, so you can show LaTeX
  source. To show it, HTML-escape `<` as `&lt;`.

Shorthand macros are defined in the `macros` block of `assets/js/site.js`:
`\RR \NN \ZZ \CC \QQ \EE` for blackboard letters, and `\diff{x} \abs{x}
\norm{x} \set{x} \inner{x}` for auto-sized delimiters. Add your own there and
they work on every page at once.

## Adding content

**A blog post.** Copy `blog/_template.html` to `blog/YYYY-MM-DD-slug.html`, write
the body, then add a matching `<article class="entry">` block at the top of the
list in `blog.html`.

**A class.** Add a `<div class="entry">` block to the right term section in
`classes.html`, and a row to the summary table at the bottom.

**Course notes.** Copy `notes/_template.html` to `notes/course-name.html` and link
to it from that class's `note-links` list.

**A research project.** Add an `<article class="entry">` block to `research.html`.

Placeholders to replace are marked `[like this]`, and each page has an
`EDIT ME` comment at the top of its content section.

## Colors

The palette is four colors and tints/shades of them, all defined as custom
properties at the top of `style.css`:

| | Hex | Used for |
| --- | --- | --- |
| Ink | `#224248` | Headings, strong text |
| Slate | `#325E6A` | Links, section headings |
| Teal | `#44A1A4` | Accents, rules, list markers |
| Amber | `#FF9A00` | Highlights, active tab, focus ring |

Dark mode reuses the same four via `prefers-color-scheme` — change a variable in
one place and it propagates.

## Previewing locally

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>. (Open the files directly with `file://` and
relative links still work, but the 404 page's absolute paths won't.)
