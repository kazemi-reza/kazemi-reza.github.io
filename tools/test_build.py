#!/usr/bin/env python3
"""Checks for the Markdown-to-HTML conversion: python3 tools/test_build.py

Every case here is something that has actually gone wrong: Markdown eating
LaTeX punctuation, a `---` inside a post truncating the body, an escaped dollar
turning into live math in the browser.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build import parse_front_matter, render_markdown  # noqa: E402

FAILURES = []


def check(name: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"  ok    {name}")
    else:
        print(f"  FAIL  {name} {detail}")
        FAILURES.append(name)


def contains(name: str, haystack: str, needle: str) -> None:
    check(name, needle in haystack, f"\n        expected to find: {needle!r}")


def absent(name: str, haystack: str, needle: str) -> None:
    check(name, needle not in haystack, f"\n        should not contain: {needle!r}")


print("front matter")
meta, body = parse_front_matter(
    "---\ntitle: T\ndate: 2026-01-01\n---\n\nintro\n\n```\n---\nnot front matter\n---\n```\n\nend\n",
    Path("sample.md"),
)
check("title parsed", meta["title"] == "T", f"got {meta.get('title')!r}")
contains("body survives a later ---", body, "end")
contains("code block kept intact", body, "not front matter")

print("\nmath vs markdown")
html = render_markdown("Subscripts $x_1$ and $x_2$ stay math, but _this_ is emphasis.")
contains("subscripts untouched", html, "$x_1$")
contains("emphasis still works", html, "<em>this</em>")

html = render_markdown(r"Compare $a < b$ and $p \& q$.")
contains("less-than escaped", html, "$a &lt; b$")
contains("ampersand escaped", html, r"$p \&amp; q$")

html = render_markdown(r"It cost \$5 and \$10.")
contains("escaped dollar keeps its backslash", html, r"\$5")
absent("escaped dollar does not open math", html, ">It cost $5")

html = render_markdown("Inline `$e^{i\\pi}$` and:\n\n```\n$$ \\alpha_1 $$\n```\n")
contains("math in a code span stays source", html, "<code>$e^{i\\pi}$</code>")
contains("math in a code fence stays source", html, "$$ \\alpha_1 $$")

print("\nblocks")
html = render_markdown("Before\n\n$$\n  E = mc^2\n$$\n\nAfter\n")
contains("display math gets a scrollable block", html, '<div class="math-block">')
absent("block is not nested in a paragraph", html, '<p><div class="math-block">')

html = render_markdown("\\begin{align}\n  a &= b \\\\\n  c &= d\n\\end{align}\n")
contains("align environment survives", html, "\\begin{align}")
contains("alignment ampersands escaped", html, "a &amp;= b")

html = render_markdown("> **Careful**\n> Body with $x$.\n\nAfter the callout.\n\n1. item\n")
contains("callout rendered", html, '<p class="callout-title">Careful</p>')
check("callout closes before what follows",
      html.index("</div>") < html.index("After the callout"),
      "— the callout swallowed the rest of the post")

html = render_markdown("| a | b |\n| --- | --- |\n| $x$ | 2 |\n")
contains("tables work", html, "<table>")
contains("math inside a table cell", html, "<td>$x$</td>")

print()
if FAILURES:
    print(f"{len(FAILURES)} failed: {', '.join(FAILURES)}")
    raise SystemExit(1)
print("all checks passed")
