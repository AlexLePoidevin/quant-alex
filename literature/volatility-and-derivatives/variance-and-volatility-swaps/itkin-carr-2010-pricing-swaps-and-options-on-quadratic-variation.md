# Pricing Swaps and Options on Quadratic Variation under Stochastic Time Change Models — Discrete Observations Case

| | |
|---|---|
| **Authors** | Andrey Itkin (Rutgers), Peter Carr (Bloomberg LP and NYU) |
| **Year** | 2010 (*Review of Derivatives Research* 13:141–176; published online November 2009) |
| **Type** | Paper, 36pp |
| **PDF** | Not hosted in this repository (Springer journal version) |
| **Find it** | [doi.org/10.1007/s11147-009-9048-z](https://doi.org/10.1007/s11147-009-9048-z) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Pricing+Swaps+and+Options+on+Quadratic+Variation+under+Stochastic+Time+Change+Models+%E2%80%94+Discrete+Observations+Case%22+Itkin) |
| **BibTeX** | `itkin2010quadratic` |
| **Status** | Reference: §1 (contributions), Theorems 1–3 and §7 (comparison with market data) carry the results |

## What it is

A method for pricing variance swaps, volatility swaps and options on variance when realised
variance is measured from discrete (for example daily) observations and the underlying
follows a jump model with stochastic volatility.

- **The textbook replication and its gaps.** A variance swap can be replicated with a
  strip of options across all strikes plus dynamic trading in the underlying (the "log
  contract"). In practice strikes are missing, deep out-of-the-money options are
  illiquid, and jumps add error through the third and higher powers of returns. That is
  the case for pricing with a model consistent with the option surface.
- **Model class.** Lévy processes run on a stochastic clock (time-changed Lévy processes),
  which capture the smile across strikes and maturities. Examples: Heston (Black–Scholes
  on a CIR clock), a normal inverse Gaussian process on a CIR clock, Carr and Wu's
  stochastic skew model, and a non-affine "3/2 power" clock.
- **Results.** Using a forward characteristic function and an expansion in the time
  between observations:
  - Theorem 1: with a diffusive clock, annualised discretely sampled quadratic variation
    equals annualised realised variance times a constant ξ fixed by the Lévy process.
  - Theorem 2: with a jumping clock, the same plus a constant η.
  - Theorem 3: when observations are further apart, two extra terms appear, one depending
    on the sampling interval and a convexity-type term in the square of variance. So with
    sparse observations the standard log-contract price is no longer the fair strike.
  - Closed-form strikes for the CIR and 3/2-power clocks, and Carr–Madan-style transforms
    for volatility swaps and options on variance.
- **Market test.** Models calibrated to 480 S&P 500 and Google option prices on 14
  August 2006 were compared with log-contract variance-swap strikes from Bloomberg. The
  stochastic skew model fit slightly better than Heston, but all three models missed the
  term structure of variance-swap prices by a substantial margin, especially at long
  maturities. The authors suggest a stochastic long-run variance level as the fix.

## Why it's in the library

- It quantifies a gap between textbook and contract: real variance swaps settle on daily
  returns, and jumps and discrete sampling change the fair strike.
- The negative empirical finding is useful: models that fit the option smile on one date
  still did not reproduce the term structure of variance-swap prices.

## Links

- [[merton-1976]] — jumps in prices, the reason the log-contract replication of variance
  is not exact
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — how sampling
  frequency changes measured realised variance
- [[shreve-2004]] — characteristic functions, change of time and the stochastic calculus
  behind the derivations
