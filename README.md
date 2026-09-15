# kazemi-reza.github.io

A static site with no Jekyll and nothing to install. **Every page is written in
Markdown** and turned into plain HTML by a small script here in the repo.
GitHub Pages only ever serves finished HTML, so there is no build on their side
that can fail.

Edit a Markdown file — on github.com or locally — and the site rebuilds itself.
You should never need to open a `.html` file.

The `.nojekyll` file at the repo root is what tells GitHub Pages to skip Jekyll
processing entirely. Don't delete it.

## Writing a blog post

**On github.com** — add or edit any Markdown file and commit it. That's the whole
job. A GitHub Action (`.github/workflows/build-site.yml`) rebuilds the affected
pages, commits the result, and asks Pages to redeploy. Give it a minute, then
reload the site.

If a file has a mistake in it — a bad date, a missing title, a class with no
term — the Action fails instead of publishing, and the site stays exactly as it
was. The Actions tab shows which file and what was wrong.

**Locally**, if you'd rather see it before pushing:

```sh
cp blog/posts/_template.md blog/posts/2026-09-20-my-post.md
python3 tools/build.py --serve
```

The page rebuilds every time you save, at <http://127.0.0.1:8000/blog.html>.
Commit the `.md` and the generated `.html` together — or just commit the `.md`
and let the Action produce the rest.

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

## Where to edit what

**Everything you edit is Markdown.** Everything else is generated.

| To change… | Edit | Which generates |
| --- | --- | --- |
| Your bio, role line, links | `content/pages/index.md` | `index.html` |
| The Classes page heading and intro | `content/pages/classes.md` | `classes.html` |
| The Research page heading and intro | `content/pages/research.md` | `research.html` |
| A class you took | `content/classes/<course>.md` | an entry on `classes.html` |
| A research project | `content/research/<project>.md` | an entry on `research.html` |
| A set of course notes | `notes/<course>.md` | `notes/<course>.html` |
| A blog post | `blog/posts/<date>-<slug>.md` | `blog/<date>-<slug>.html` |
| Your name, email, GitHub link | `content/site.md` | the header and footer everywhere |

Each of those directories has a `_template.md` to copy. Generated `.html` files
carry a comment at the top naming the Markdown file they came from.

`404.html` is the one hand-written page left; it is chrome, not content.

Shared assets:

- `assets/css/style.css` — the whole stylesheet
- `assets/js/site.js` — MathJax configuration, LaTeX macros, footer year
- `assets/favicon.svg`
- `tools/build.py` — turns every Markdown source into its page
- `.github/workflows/build-site.yml` — runs that build on GitHub whenever any
  content changes, so editing in the browser is enough to publish
- `tools/vendor/markdown2.py` — the Markdown converter, vendored (MIT, license
  included) so the build needs no `pip install`
- `assets/vendor/mathjax/` — MathJax 3.2.2, self-hosted (Apache-2.0, license
  included). Nothing is loaded from a CDN, so the site has no external runtime
  dependency and renders offline. To upgrade: `npm pack mathjax@<version>`, then
  replace `tex-chtml.js` and `output/chtml/fonts/woff-v2/` with the copies from
  the tarball's `package/es5/`.

## Writing LaTeX

The same LaTeX works in every Markdown file on the site — posts, notes, class
descriptions, research write-ups, even your bio. A self-hosted copy of MathJax
typesets it in the browser — no CDN, no network dependency at page load.

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

Display math is wrapped in a scrollable block for you, so a wide equation
scrolls sideways on a phone instead of overflowing the page.

Shorthand macros are defined in the `macros` block of `assets/js/site.js`:
`\RR \NN \ZZ \CC \QQ \EE` for blackboard letters, and `\diff{x} \abs{x}
\norm{x} \set{x} \inner{x}` for auto-sized delimiters. Add your own there and
they work on every page at once.

## Adding content

**A blog post.** Copy `blog/posts/_template.md` to
`blog/posts/YYYY-MM-DD-slug.md` and write. The post list on `blog.html` is
regenerated from the files themselves, so there is nothing to update by hand.

**A class.** Copy `content/classes/_template.md` to
`content/classes/2026-fall-phys512.md` and fill in the front matter:

```yaml
---
title: Quantum Field Theory I
course: PHYS 512
term: Fall 2026          # groups the entry; terms sort newest first
status: In progress      # "In progress"/"Ongoing" highlights the tag
order: 1                 # position within the term
meta:                    # each line becomes one item in the grey meta row
  - "Instructor: [name]"
  - 4 credits
notes:                   # Markdown links to your notes pages
  - "[Lecture notes](notes/phys-512-qft.html)"
---
```

The body below the front matter is the description. Term headings, the ordering,
the "— in progress" label and the summary table at the bottom of the page are
all derived from these files — there is no second list to keep in sync.

**Course notes.** Copy `notes/_template.md` to `notes/phys-512-qft.md`, then link
to `notes/phys-512-qft.html` from that class's `notes:` list.

**A research project.** Copy `content/research/_template.md`. Same shape as a
class, without `course` or `term`; `order` sets the position on the page.

Placeholders to replace are marked `[like this]`.

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
