---
title: Variational estimates for bound-state energies
status: Ongoing
order: 2
meta:
  - 2026–present
  - solo
---

How good a bound can you get on a ground-state energy with a trial wavefunction
you can actually write down? The Rayleigh–Ritz principle guarantees the
direction of the error but says nothing useful about its size:

$$
  E_0 \;\le\; \frac{\inner{\psi | \hat H | \psi}}{\inner{\psi | \psi}}
  \qquad \text{for every } \psi \in \mathcal{H}.
$$

The project is to pair that upper bound with a computable lower bound from the
variance $\sigma^2 = \inner{\hat H^2} - \inner{\hat H}^2$, so a single
variational calculation brackets the true energy instead of only bounding it
from above.

**Status:** working for the one-dimensional test potentials; the open question
is how the bracket degrades when the spectrum is nearly degenerate.
