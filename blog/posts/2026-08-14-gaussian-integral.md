---
title: Why the Gaussian integral keeps showing up
date: 2026-08-14
summary: $\int_{-\infty}^{\infty} e^{-x^2}\,\diff{x} = \sqrt{\pi}$ is the one integral worth memorising, and the trick that evaluates it is the seed of half of statistics.
---

There is no elementary antiderivative for $e^{-x^2}$. You cannot integrate it
the way you integrate a polynomial, and yet the definite integral over the whole
line is as clean as it gets:

$$
  \int_{-\infty}^{\infty} e^{-x^2}\,\diff{x} = \sqrt{\pi}.
$$

## The trick

Square it, and read the product as a double integral over the plane:

\begin{align}
  I^2 &= \left(\int_{-\infty}^{\infty} e^{-x^2}\,\diff{x}\right)
         \left(\int_{-\infty}^{\infty} e^{-y^2}\,\diff{y}\right) \\
      &= \iint_{\RR^2} e^{-(x^2 + y^2)} \,\diff{x}\,\diff{y}.
\end{align}

In polar coordinates $x^2 + y^2 = r^2$ and the area element brings down a factor
of $r$ — which is exactly the factor needed to make the radial integral
elementary:

$$
  I^2 = \int_0^{2\pi}\!\!\int_0^{\infty} e^{-r^2}\, r \,\diff{r}\,\diff{\theta}
      = 2\pi \cdot \tfrac{1}{2} = \pi.
$$

The whole difficulty vanished because of the $r$. In one dimension there is
nothing to cancel the derivative of the exponent; in two, the geometry supplies
it.

## Why it keeps coming back

> **The shape of the argument**
> A hard integral becomes easy in a coordinate system that matches the symmetry
> of the integrand. That is the entire content of the trick, and it generalises
> far past this one case.

The same Gaussian shows up as the normalisation of the normal distribution, as
the free-field partition function, and as the leading term in the saddle-point
approximation, where a peaked integrand is replaced by the Gaussian that matches
its value and curvature at the maximum.

*[More to say here — the saddle-point connection deserves its own section.]*
