---
title: Spectral methods for stiff transport equations
status: Ongoing
order: 1
meta:
  - 2025–present
  - with [collaborator], [institution]
---

Advection–diffusion problems in the stiff limit, where the Péclet number
$\mathrm{Pe} = UL/D$ is large, punish standard explicit schemes: the stable time
step collapses like $\Delta t \sim \Delta x^2 / D$ and the computation stops
being affordable long before it stops being interesting.

We're building an implicit–explicit spectral scheme that treats the diffusive
operator implicitly in Fourier space while keeping the nonlinear advection
explicit, so the cost per step stays $O(N \log N)$:

$$
  \frac{\partial u}{\partial t} + \nabla \cdot (\mathbf{v}\,u)
    = D\,\nabla^2 u + S(\mathbf{x}, t),
  \qquad
  \hat u^{n+1}_{\mathbf{k}}
    = \frac{\hat u^{n}_{\mathbf{k}} + \Delta t \,\widehat{N}^{\,n}_{\mathbf{k}}}
           {1 + \Delta t \, D \abs{\mathbf{k}}^2}.
$$

**Status:** the 2D solver reproduces the manufactured solutions to spectral
accuracy; the 3D version and a proper stability analysis are next.
