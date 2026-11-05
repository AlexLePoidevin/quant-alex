# A Model-Free Backward and Forward Nonlinear PDEs for Implied Volatility

| | |
|---|---|
| **Authors** | Peter Carr, Andrey Itkin (NYU Tandon), Sasha Stoikov (Cornell) |
| **Year** | 2019 |
| **Type** | Working paper, arXiv [1907.07305](https://arxiv.org/abs/1907.07305) (q-fin.CP), 31pp |
| **PDF** | `carr-et-al-2019-model-free-pdes-for-implied-volatility.pdf` (arXiv version) |
| **BibTeX** | `carr2019pdeiv` |
| **Status** | Reference: §1–2 (the derivations) and §6–7 (the speed test and its caveats) |

## What it is

A derivation of partial differential equations that the Black–Scholes implied volatility
itself satisfies, plus a numerical method to solve them. The idea is to compute a whole
grid of implied volatilities in one pass, instead of running a root-finder separately at
every strike and price.

- **The derivation.** Implied volatility Σ is defined implicitly: Black–Scholes(S, Σ, t)
  = observed price Z. Differentiate that identity with respect to time and to the
  stock price, and substitute into the Black–Scholes PDE. The result is a quasilinear
  parabolic PDE for Σ as a function of (S, t, Z).
  - A "forward" version does the same in strike and maturity, giving Σ(K, T, Z).
  - The paper also derives first-order nonlinear hyperbolic PDEs.
  - The equations need only that the claim's Black–Scholes value increases with
    volatility. That covers European options, and convex payoffs at a possibly random
    time such as barrier options. In that sense they are "model-free".
- **Boundary and initial conditions.** Section 3 works these out. At maturity the
  initial condition is Σ = 0, which makes the gradients blow up at the first time step.
- **Numerics.** An iterative finite-difference scheme, second order in space and time,
  unconditionally stable and positivity-preserving.
- **The test.**
  - The grid is 200 × 100 points in transformed (price, strike) coordinates, with
    S = 100, r = 5%, q = 1% and maturities to one year. The root-finder (Matlab's
    `blsimpv`) took about 6 ms a point, or 113 seconds for 20,000 points.
  - After the first step, the PDE solver needed 3 iterations a step and 2.8 seconds,
    with errors against the root-finder of 1e-6 to 1e-7 relative.
  - The authors report the PDE approach as almost 40 times faster.
- **The caveats, in the authors' words.**
  - The first time step cannot be solved by the PDE, because the initial condition is
    degenerate, so it is seeded with the root-finder.
  - Boundary values also come from the root-finder.
  - Error builds up over time steps, reaching 20–50 bp by T = 0.2. The largest errors
    are at deep out-of-the-money points.
  - Modern root-finders (Jäckel's 2015 method, Chebyshev interpolation, neural
    networks trained offline) are much faster than `blsimpv`, so the comparison is
    against a slow baseline.

## Why it's in the library

**It is a new way to look at implied volatility, not a better calculator.** That
implied volatility obeys its own PDE, with no model for the underlying, is a neat
structural fact. It is closely related to how local-volatility and forward equations
(Dupire) describe the smile across strikes and maturities.

**The speed claim should be read with its caveats.** The comparison is against a
generic Matlab solver, run point by point. The PDE still relies on the root-finder for
its boundaries and first step, and loses accuracy as it marches forward. For practical
work, Jäckel's method or a precomputed interpolation is the stronger benchmark, as the
paper itself notes.

## Links

- [[carr-wu-2006-a-tale-of-two-indices]] — the other way to read the option surface: as the price of a variance swap, which needs no implied volatility at all
- [[carr-wu-2011-a-new-simple-approach-for-constructing-implied-volatility-surfaces]] — modelling the implied-volatility surface directly rather than prices
- [[carr-wu-2016-analyzing-volatility-risk-and-risk-premium-in-option-contracts]] — the published theory of implied-volatility dynamics
