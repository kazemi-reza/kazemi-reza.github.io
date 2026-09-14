---
title: Writing math on this site
date: 2026-08-31
summary: Posts are Markdown files with LaTeX in them. Here is the whole workflow, and where the edges are.
---

Posts on this site are Markdown files in `blog/posts/`. You write one, run the
build script, and it becomes a page — with the LaTeX typeset, the post list
updated, and no HTML typed by hand.

## The loop

```sh
python3 tools/build.py --serve
```

That builds every post, serves the site at <http://127.0.0.1:8000/blog.html>,
and rebuilds whenever you save. Leave it running while you write. When you're
done, commit the `.md` file along with the `.html` it produced.

Without `--serve` it just builds once and exits, which is what you want before
a commit.

## Inline math

Wrap it in single dollar signs or `\(…\)`. So typing `$e^{i\pi} + 1 = 0$` gives
$e^{i\pi} + 1 = 0$, and `\(\zeta(2) = \pi^2/6\)` gives \(\zeta(2) = \pi^2/6\) —
both sit on the text baseline without disturbing the line height.

Markdown and LaTeX want the same punctuation — `_` for emphasis, `*` for bold,
`\\` for a line break — so the build lifts every math span out before the
Markdown pass and puts it back afterwards untouched. Subscripts like $x_1$ and
$x_2$ survive; so does a matrix full of `\\`.

## Display math

Double dollars or `\[…\]` on their own line break the equation out. The Fourier
transform, for instance:

$$
  \hat f(\xi) = \int_{-\infty}^{\infty} f(x)\, e^{-2\pi i x \xi} \,\diff{x}.
$$

Anything set off this way gets a block that scrolls sideways on a narrow screen
rather than stretching the page.

## Multi-line derivations

LaTeX environments work as written. An `align` block, aligned on the equals
signs, evaluating the Gaussian integral the usual way:

\begin{align}
  I^2 &= \left(\int_{-\infty}^{\infty} e^{-x^2}\,\diff{x}\right)
         \left(\int_{-\infty}^{\infty} e^{-y^2}\,\diff{y}\right) \\
      &= \int_0^{2\pi}\!\!\int_0^{\infty} e^{-r^2}\, r \,\diff{r}\,\diff{\theta} \\
      &= 2\pi \cdot \tfrac{1}{2} \;=\; \pi,
\end{align}

so $I = \sqrt{\pi}$. Equations in an `align` are numbered automatically; use
`align*` if you would rather they weren't.

## Matrices, cases, and the rest

$$
  A = \begin{pmatrix} a & b \\ c & d \end{pmatrix},
  \qquad
  A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
$$

Piecewise definitions with `cases`:

$$
  \operatorname{sgn}(x) = \begin{cases}
    +1 & x > 0, \\
    \phantom{+}0 & x = 0, \\
    -1 & x < 0.
  \end{cases}
$$

## Shorthands

A few macros are predefined in `assets/js/site.js`, so common things stay short.
`\RR`, `\NN`, `\ZZ`, `\CC`, `\QQ` and `\EE` give the blackboard letters — $\RR$,
$\NN$, $\ZZ$, $\CC$, $\QQ$, $\EE$ — while `\diff{x}`, `\abs{x}`, `\norm{x}`,
`\set{x}` and `\inner{x}` give $\diff{x}$, $\abs{x}$, $\norm{x}$, $\set{x}$ and
$\inner{x}$ with auto-sized delimiters. Add your own to the `macros` block in
that file and they work on every page at once.

## Callouts

A blockquote whose first line is bold becomes a callout box:

> **One thing to watch**
> Because a bare `$` opens inline math, write a literal dollar sign as `\$` —
> otherwise a sentence with two prices in it turns into an equation.

## Showing LaTeX source

Anything inside backticks or a fenced code block is left alone — no Markdown, no
math — so you can print source verbatim:

```latex
$$
  \norm{u}_{L^2}^2 = \int_\Omega \abs{u(x)}^2 \,\diff{x}
$$
```

## Front matter

Every post starts with a small block between `---` lines:

```yaml
---
title: Writing math on this site
date: 2026-08-31
summary: One sentence; it becomes the blurb in the post list.
draft: true
---
```

`title` and `date` are required — though if the filename starts with a date, as
`2026-08-31-writing-math-here.md` does, you can leave `date` out. `draft: true`
keeps a post off the site until you delete the line. Reading time is counted for
you.

## Adding a post

Copy `blog/posts/_template.md` to `blog/posts/YYYY-MM-DD-slug.md` and write. The
post list on the blog page is regenerated from the files themselves, so there is
nothing to update by hand and no way for the list to drift out of sync with
what's actually published.
