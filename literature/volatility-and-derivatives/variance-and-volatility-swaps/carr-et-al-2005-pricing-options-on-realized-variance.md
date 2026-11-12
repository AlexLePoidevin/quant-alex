# Pricing Options on Realized Variance

| | |
|---|---|
| **Authors** | Peter Carr, Hélyette Geman, Dilip B. Madan, Marc Yor |
| **Year** | 2005 (working paper dated 26 January 2005; published in *Finance and Stochastics* 9(4), 2005) |
| **Type** | Paper, 26pp (working-paper version) |
| **PDF** | Not hosted in this repository (pre-publication draft, no open licence) |
| **Find it** | [doi.org/10.1007/s00780-005-0155-x](https://doi.org/10.1007/s00780-005-0155-x) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Pricing+Options+on+Realized+Variance%22+Carr) |
| **BibTeX** | `carr2005realizedvariance` |
| **Status** | Reference: §1 (motivation), §5 (Laplace transform to option prices), §6 (time change vs quadratic variation) and §7 (the S&P 500 numbers) carry the argument; §2–3 are the self-decomposability theory |

## What it is

A method for pricing options on realized variance and realized volatility when returns
follow a pure-jump process, and a test of a shortcut that is exact only when returns are
continuous.

- **The problem.** Variance swaps pay realized variance (the sum of squared daily log
  returns), and by 2005 volatility swaps and options on realized variance were trading
  over the counter. Pricing them needs the risk-neutral distribution of future realized
  variance. Black–Scholes gives it no uncertainty at all. Earlier work (Heston-type
  stochastic volatility) kept continuous paths and added a second state variable.
- **The approach.** Keep a one-dimensional model with independent increments but drop path
  continuity: model returns as pure-jump Lévy processes, or as Sato processes (additive,
  self-similar, time-inhomogeneous), calibrated to the vanilla smile. The quadratic
  variation of such a process is itself an increasing process whose jump density follows
  from the return jump density. The paper then derives which properties pass from returns
  to quadratic variation (infinite activity, complete monotonicity, self-decomposability).
- **Self-decomposability and its hierarchy.** Self-decomposable laws are limit laws and are
  unimodal. For forward returns to be self-decomposable as well, the unit-time law has to
  sit in the subclass L1; for return spreads, L2. Variance gamma is self-decomposable but
  not in L1. CGMY enters L1 and L2 for large enough Y, and the authors' computations
  suggest it never gets past L6.
- **Prices.** For CGMY the paper gives the Laplace transform of quadratic variation in
  closed form. Options on realized variance are priced by Laplace inversion in the strike,
  the same trick as Carr and Madan's FFT method for vanillas. Options on realized
  volatility are built as portfolios of options on variance.
- **Clock versus quadratic variation.** Any martingale can be written as Brownian motion
  run on a random clock. When paths are continuous the clock equals quadratic variation,
  so options on the clock can be priced from vanilla options alone (Carr and Lee). With
  jumps the two differ. The paper checks whether the clock is a usable proxy and finds it
  is not.
- **The numbers.** CGMY calibrated to S&P 500 options on 2 June 2003 at maturities of 0.80
  and 1.05 years. Expected realized volatility: 22.28% and 22.61%.
  - **Options on variance.** At volatility strikes of 10%, 20% and 30% they cost 19.68,
    15.38 and 11.89 at the shorter maturity, and 20.57, 16.73 and 13.40 at the longer one,
    in the paper's volatility-point units.
  - **Realized volatility.** Bending a tangent hedge with options gives quotes of 17.47 and
    20.93, well below the Jensen upper bound of about 22.
  - **The Brownian clock.** Its expected value is only 16.64% and 16.43% in volatility
    terms, and the square root of the clock is quoted at 14.21% at the shorter maturity.
    The clock understates quadratic variation substantially.

## Why it's in the library

**Realized-variance products depend on the jump assumption.** Under continuous paths a
variance swap is replicated by a static strip of options, and options on the clock equal
options on quadratic variation. This paper shows that once returns jump, that equality
breaks, and by a large amount in a calibrated model. Any model-free claim about volatility
derivatives should be read with that in mind.

**It is the volatility-swap convexity problem in numbers.** The gap between the volatility
quote (17.47) and the square root of expected variance (about 22) is the convexity
adjustment a volatility-swap dealer has to charge for, here priced from the vanilla smile.

**It is a theory-heavy paper with one calibration.** The numbers come from one day and one
index, and the self-decomposability hierarchy is more relevant to model choice than to
pricing. The working-paper copy has garbled symbols in places; the published version is
cleaner.

## Links

- [[carr-et-al-2007-time-for-a-change-variance-gamma-model]] — the intuition for pure-jump
  return models that this paper builds on
- [[carr-et-al-2003-stochastic-volatility-for-levy-processes]] — the same model family with
  a stochastic clock, the other way to make realized variance random
- [[merton-1976]] — jumps in returns, the feature that separates quadratic variation from
  the Brownian clock
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — measuring realized
  variance from noisy high-frequency data, the quantity these contracts settle on
- [[carr-lee-2007-realized-volatility-and-variance-options-via-swaps]] — pricing the same options model-free from swap prices
