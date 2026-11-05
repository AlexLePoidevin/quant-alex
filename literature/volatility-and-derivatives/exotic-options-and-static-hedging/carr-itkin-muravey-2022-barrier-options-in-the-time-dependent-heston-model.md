# Semi-analytical Pricing of Barrier Options in the Time-dependent Heston Model

| | |
|---|---|
| **Authors** | Peter Carr (NYU Tandon); Andrey Itkin (NYU Tandon); Dmitry Muravey (Moscow State University) |
| **Year** | 2022 (arXiv 2202.06177, February 2022; no journal version found) |
| **Type** | Working paper (arXiv version, 29pp). Theory plus numerical tests on made-up parameters |
| **PDF** | `carr-itkin-muravey-2022-barrier-options-in-the-time-dependent-heston-model.pdf` (arXiv version) |
| **BibTeX** | `carr2022barrierheston` |
| **Status** | Reference: the introduction (why the problem is hard), §5 (numerical results, Tables 3–4) and §6 (discussion of speed) |

## What it is

A method for pricing barrier options when volatility is stochastic and every model
parameter can change over time.

- **The setting.** In the Heston model, variance mean-reverts and is correlated with the
  stock. With constant parameters, European options have near closed-form prices. To fit
  the term structure of market prices, though, the parameters need to vary with time, and
  then there is no closed form even for vanilla options, let alone barriers. Practitioners
  fall back on Monte Carlo or finite-difference grids.
- **The method.** The authors extend their "generalized integral transform" technique from
  one dimension to two. A down-and-out put's price is written as a two-dimensional
  integral of an unknown function: the slope of the solution at the moving barrier. That
  function solves a linear integral equation (of mixed Volterra–Fredholm type), which is
  solved numerically with radial basis functions. The barrier itself can move with time.
- **Other barrier types.** Down-and-in puts follow from in–out parity with the vanilla
  Heston put. Up barriers follow by a change of variable, and calls are handled the same
  way.
- **An error in earlier work.** The introduction notes that a 2019 semi-analytical Heston
  barrier formula by other authors contains an error, confirmed by those authors.
- **Results.** Compared with a second-order finite-difference reference solution, the new
  method's errors vary a lot. They are a few percent for high strikes and short
  maturities, 20–40% at intermediate maturities (about 8% at the money), and between a
  few percent and 30% at long maturities. Speed is similar to finite differences at long
  maturities, and finite differences are faster at short ones. Ninety percent of the time
  goes on filling a dense matrix.

## Why it's in the library

**It shows why barrier options are hard to price under realistic volatility.** Barrier
prices depend on the whole path of volatility, not just its average, so the smile models
that fit vanilla options do not settle them. Even a semi-analytical method leaves a
numerical integral equation to solve.

**The reported accuracy is weaker than the abstract suggests.** The abstract promises
high speed and accuracy. The tables show errors of 20–40% against finite differences at
some maturities and no speed advantage at short ones, with improvements left to future
work. The value is the formulation, which drops one dimension from the problem, rather
than a ready-to-use pricer.

## Links

- [[merton-1976]] — jump risk, which this diffusion model leaves out and which matters
  most for options that knock out on a large move
- [[lipton-sepp-2022-hybrid-method-for-pricing-barrier-options-with-stochastic-volatility]] — another fast method for barriers under stochastic volatility
- [[howison-2006-barrier-options]] — the constant-volatility barrier formulas this extends
