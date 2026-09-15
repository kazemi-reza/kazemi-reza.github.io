---
title: Monte Carlo sampling near a critical point
status: Completed
order: 3
meta:
  - 2024–2025
  - undergraduate thesis
---

Critical slowing down makes local Metropolis updates useless near $T_c$: the
autocorrelation time diverges as $\tau \sim \xi^{\,z}$ with $z \approx 2$ for
the two-dimensional Ising model. Cluster algorithms sidestep this by flipping
correlated regions in a single move, dropping the dynamical exponent to
$z \approx 0.35$.

I implemented Wolff cluster updates and measured the critical exponents by
finite-size scaling, recovering $\beta/\nu = 0.125$ and $\gamma/\nu = 1.75$ to
within statistical error on lattices up to $L = 512$.

**Status:** finished. Write-up and code are on
[GitHub](https://github.com/kazemi-reza).
