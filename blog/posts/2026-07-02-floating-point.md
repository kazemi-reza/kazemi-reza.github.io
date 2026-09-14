---
title: Floating point will betray you eventually
date: 2026-07-02
summary: A short catalogue of the ways $\mathrm{fl}(a + b) \ne a + b$ has cost me an afternoon.
---

Everyone learns that `0.1 + 0.2 != 0.3`, decides floating point is quirky, and
moves on. That example is the least interesting one, because it is visible. The
failures worth worrying about are the ones that produce a plausible number.

## Catastrophic cancellation

Subtracting two nearly equal numbers destroys the significant digits they had in
common and promotes rounding error into the leading position. The textbook case
is the quadratic formula: when $b^2 \gg 4ac$, the root

$$
  x = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
$$

subtracts two numbers that agree to most of their digits. Computing the other
root and using $x_1 x_2 = c/a$ to recover this one avoids the subtraction
entirely.

## Summation order

Addition is not associative in floating point. Summing a long list from largest
to smallest loses the small terms into the rounding gap of the running total;
summing from smallest to largest keeps them. For a sum of $n$ terms the naive
error grows like $O(n\varepsilon)$, while compensated summation holds it near
$O(\varepsilon)$ by carrying the lost low-order bits along in a second variable.

> **The rule of thumb**
> Ask what the condition number is before trusting the output. If
> $\kappa = \norm{A}\,\norm{A^{-1}}$ is $10^{k}$, expect to lose about $k$
> digits — no algorithm recovers information the problem itself has discarded.

*[Add the accumulated-drift example from the ODE integrator here.]*
