# rezakaze.github.io

A static site with no Jekyll and nothing to install. Blog posts are written in
Markdown and turned into plain HTML by a small script here in the repo; the rest
of the pages are hand-written HTML. GitHub Pages only ever serves finished HTML,
so there is no build on their side that can fail.

The `.nojekyll` file at the repo root is what tells GitHub Pages to skip Jekyll
processing entirely. Don't delete it.

## Writing a blog post

```sh
cp blog/posts/_template.md blog/posts/2026-09-20-my-post.md
python3 tools/build.py --serve
```

Write Markdown (with LaTeX in it) in that file. The page rebuilds every time you
save, at <http://127.0.0.1:8000/blog.html>. When you're happy, stop the server,
run `python3 tools/build.py` once, and commit both the `.md` and the generated
`.html`.

Each post starts with a front matter block:

```yaml
---
title: Why the Gaussian integral keeps showing up
date: 2026-09-20
summary: One sentence; it becomes the blurb in the post list.
draft: true
---
```

`title` is required. `date` is too, unless the filename starts with one.
`draft: true` keeps a post out of the site until you remove the line — and if
you draft or delete a post that was published, its page is cleaned up on the
next build. Reading time is counted automatically.

Markdown gets the usual: headings, lists, tables, footnotes, fenced code,
links, `**bold**`, `*italic*`. One extra: a blockquote whose first line is bold
becomes a callout box.

```md
> **One thing to watch**
> Because a bare `$` opens inline math, write a literal dollar sign as `\$`.
```

The build refuses to write anything if a post is malformed, and says which file
and what's wrong. `python3 tools/test_build.py` checks the conversion itself —
worth running if you ever change `tools/build.py`.

## Pages

| File | Tab |
| --- | --- |
| `index.html` | About — bio and links to the other tabs |
| `classes.html` | Classes taken, by term, with links to notes |
| `research.html` | Research projects, each with a description |
| `blog.html` | Blog post index |
| `404.html` | Shown for any URL that doesn't exist |

Longer content lives one directory down:

- `blog/posts/` — **one Markdown file per post — this is where you write**, plus
  `_template.md` to copy
- `blog/*.html` — generated from those Markdown files; don't edit by hand
- `notes/` — one HTML file per set of course notes, plus `_template.html`

Shared assets:

- `assets/css/style.css` — the whole stylesheet
- `assets/js/site.js` — MathJax configuration, LaTeX macros, footer year
- `assets/favicon.svg`
- `tools/build.py` — turns `blog/posts/*.md` into post pages and rebuilds the
  post list in `blog.html`
- `tools/vendor/markdown2.py` — the Markdown converter, vendored (MIT, license
  included) so the build needs no `pip install`
- `assets/vendor/mathjax/` — MathJax 3.2.2, self-hosted (Apache-2.0, license
  included). Nothing is loaded from a CDN, so the site has no external runtime
  dependency and renders offline. To upgrade: `npm pack mathjax@<version>`, then
  replace `tex-chtml.js` and `output/chtml/fonts/woff-v2/` with the copies from
  the tarball's `package/es5/`.

## Writing LaTeX

The same LaTeX works everywhere — in a Markdown post, and typed straight into
any of the hand-written HTML pages. A self-hosted copy of MathJax typesets it in
the browser — no CDN, no network dependency at page load.

- Inline: `$e^{i\pi} + 1 = 0$` or `\(e^{i\pi} + 1 = 0\)`
- Display: `$$ ... $$` or `\[ ... \]`
- Environments: `\begin{align} ... \end{align}`, `pmatrix`, `cases`, and so on

Markdown and LaTeX compete for the same punctuation — `_`, `*`, `\\` — so the
build lifts every math span out of a post before the Markdown pass and puts it
back untouched afterwards. Subscripts like `$x_1$` and matrices full of `\\`
survive, and `<`, `>` and `&` inside math are escaped for you.

Two things to know:

- A bare `$` starts inline math. Write a literal dollar sign as `\$`.
- Anything in backticks or a fenced code block is left alone — no Markdown, no
  math — so you can show LaTeX source verbatim.

In a Markdown post, display math is wrapped in `<div class="math-block">` for
you, so it scrolls sideways on a phone instead of overflowing the page. In the
hand-written HTML pages, write that wrapper yourself.

Shorthand macros are defined in the `macros` block of `assets/js/site.js`:
`\RR \NN \ZZ \CC \QQ \EE` for blackboard letters, and `\diff{x} \abs{x}
\norm{x} \set{x} \inner{x}` for auto-sized delimiters. Add your own there and
they work on every page at once.

## Adding content

**A blog post.** Copy `blog/posts/_template.md` to
`blog/posts/YYYY-MM-DD-slug.md`, write it in Markdown, and run the build. The
post list in `blog.html` is regenerated from the files themselves, so there is
nothing to update by hand.

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
python3 tools/build.py --serve     # builds, serves, and rebuilds as you write
python3 -m http.server 8000        # no rebuilding, just serves what's there
```

Then open <http://localhost:8000>. (Open the files directly with `file://` and
relative links still work, but the 404 page's absolute paths won't.)

`tools/build.py` needs only Python 3.9+ — no packages, no network.
