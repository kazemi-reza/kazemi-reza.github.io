#!/usr/bin/env python3
"""Checks for the Markdown-to-HTML conversion: python3 tools/test_build.py

Every case here is something that has actually gone wrong: Markdown eating
LaTeX punctuation, a `---` inside a post truncating the body, an escaped dollar
turning into live math in the browser.
"""

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build import BuildError, Entry, parse_front_matter, render_markdown  # noqa: E402

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

print("\nfront matter lists")
meta, _ = parse_front_matter(
    "---\ntitle: T\nmeta:\n  - Instructor: X\n  - 3 credits\nstatus: Ongoing\n---\n\nbody\n",
    Path("sample.md"),
)
check("list collected", meta["meta"] == ["Instructor: X", "3 credits"], f"got {meta.get('meta')!r}")
check("key after a list still parses", meta.get("status") == "Ongoing", f"got {meta.get('status')!r}")

try:
    parse_front_matter("---\ntitle: T\n  - orphan\n---\n\nbody\n", Path("bad.md"))
    check("orphan list item rejected", False, "no error raised")
except BuildError:
    check("orphan list item rejected", True)

print("\nentries")
tmp = Path(tempfile.mkdtemp())
(tmp / "a.md").write_text(
    "---\ntitle: Real Analysis\ncourse: MATH 405\nterm: Fall 2026\nstatus: In progress\n"
    "meta:\n  - 3 credits\nnotes:\n  - \"[Lecture notes](notes/x.html)\"\n---\n\n"
    "Body with $L^p$ math.\n"
)
entry = Entry(tmp / "a.md", "class")
html = entry.render()
contains("heading joins course and title", html, "MATH 405 &middot; Real Analysis")
contains("in-progress status is highlighted", html, '<span class="tag tag--active">')
contains("extra meta rendered", html, "<span>3 credits</span>")
contains("note link rendered", html, 'href="notes/x.html"')
contains("body math preserved", html, "$L^p$")

(tmp / "b.md").write_text(
    "---\ntitle: Old\ncourse: X 1\nterm: Spring 2025\nstatus: Completed\n---\n\nBody.\n"
)
done = Entry(tmp / "b.md", "class")
contains("completed status is a plain tag", done.render(), '<span class="tag">Completed</span>')
check("terms sort newest first", entry.term_key > done.term_key,
      f"{entry.term_key} should outrank {done.term_key}")
check("term parsed into (year, season)", entry.term_key == (2026, 3), f"got {entry.term_key}")

try:
    (tmp / "c.md").write_text("---\ntitle: No term\n---\n\nBody.\n")
    Entry(tmp / "c.md", "class")
    check("a class without a term is rejected", False, "no error raised")
except BuildError:
    check("a class without a term is rejected", True)

shutil.rmtree(tmp)

print()
if FAILURES:
    print(f"{len(FAILURES)} failed: {', '.join(FAILURES)}")
    raise SystemExit(1)
print("all checks passed")
