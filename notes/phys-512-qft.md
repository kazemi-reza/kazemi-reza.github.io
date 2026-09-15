---
title: PHYS 512 · Lecture notes
lede: Quantum Field Theory I — Fall 2026. Typed up as the course goes; expect gaps and the occasional sign error.
---

## 1. The free scalar field

Start from the Klein–Gordon Lagrangian density for a real scalar field of mass $m$:

$$
  \mathcal{L} = \tfrac{1}{2}\,\partial_\mu \phi \,\partial^\mu \phi
              - \tfrac{1}{2}\,m^2 \phi^2 .
$$

The Euler–Lagrange equation gives $(\Box + m^2)\phi = 0$, whose plane-wave
solutions satisfy the on-shell condition $p^2 = m^2$, i.e.
$p^0 = \omega_{\mathbf{p}} = \sqrt{\abs{\mathbf{p}}^2 + m^2}$.

## 2. Canonical quantization

Promote the field and its conjugate momentum $\pi = \dot\phi$ to operators
obeying equal-time commutation relations,

$$
  \bigl[\phi(\mathbf{x}, t),\, \pi(\mathbf{y}, t)\bigr]
    = i\,\delta^{(3)}(\mathbf{x} - \mathbf{y}),
  \qquad
  \bigl[\phi(\mathbf{x}, t),\, \phi(\mathbf{y}, t)\bigr] = 0,
$$

and expand in creation and annihilation operators:

$$
  \phi(x) = \int \frac{\diff{^3 p}}{(2\pi)^3}
    \frac{1}{\sqrt{2\omega_{\mathbf{p}}}}
    \left( a_{\mathbf{p}}\, e^{-i p \cdot x}
         + a^{\dagger}_{\mathbf{p}}\, e^{+i p \cdot x} \right),
  \qquad
  \bigl[a_{\mathbf{p}},\, a^{\dagger}_{\mathbf{q}}\bigr]
    = (2\pi)^3\, \delta^{(3)}(\mathbf{p} - \mathbf{q}).
$$

> **Careful**
> The Hamiltonian comes out with a divergent zero-point term,
> $H = \int \frac{\diff{^3p}}{(2\pi)^3}\, \omega_{\mathbf{p}}
> ( a^{\dagger}_{\mathbf{p}} a_{\mathbf{p}} + \tfrac{1}{2}(2\pi)^3 \delta^{(3)}(0) )$.
> Normal ordering discards it, which is legitimate here only because nothing in
> this theory couples to an absolute energy.

## 3. The Feynman propagator

The time-ordered two-point function is the object every perturbative
calculation is built from:

\begin{align}
  D_F(x - y) &= \inner{0 | T\,\phi(x)\phi(y) | 0} \\
             &= \int \frac{\diff{^4 p}}{(2\pi)^4}
                \frac{i\, e^{-i p\cdot(x-y)}}{p^2 - m^2 + i\epsilon}.
\end{align}

The $i\epsilon$ is not decoration: it fixes which way the contour dodges the
poles at $p^0 = \pm\omega_{\mathbf{p}}$, and so encodes the boundary condition
that positive frequencies propagate forward in time and negative frequencies
backward.

## 4. To do

- Wick's theorem and the combinatorics of contractions.
- $\phi^4$ interactions: the vertex factor $-i\lambda$ and the first loop.
- Regularization — why $\int \diff{^4 k}\, (k^2 - m^2)^{-2}$ diverges logarithmically.
