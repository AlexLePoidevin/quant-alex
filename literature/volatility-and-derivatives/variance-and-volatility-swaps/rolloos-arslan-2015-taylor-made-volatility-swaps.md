# Taylor-made Volatility Swaps

| | |
|---|---|
| **Authors** | Frido Rolloos (Aegon Asset Management), Melih Arslan (Deutsche Bank Securities) |
| **Year** | 2015 (dated December 2015; SSRN 2702714) |
| **Type** | Short note, 9pp |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Taylor-made+Volatility+Swaps%22+Rolloos) for the title and authors |
| **BibTeX** | `rolloos2015taylor` |
| **Status** | Reference: §5 (the derivation) and §6 (Table 1) are the whole result |

## What it is

A rule of thumb for the fair strike of a volatility swap, proved with little more than a
Taylor expansion.

- **The problem.** A volatility swap pays realised volatility minus a fixed strike. Unlike
  a variance swap, it cannot be replicated from a strip of options, because volatility is
  the square root of variance. The variance-swap strike is only an upper bound
  (Jensen's inequality). If spot and volatility were uncorrelated, the at-the-money implied
  volatility would be a good approximation, but in equity markets they are strongly
  negatively correlated.
- **The result.** The volatility-swap strike is approximately the implied volatility at the
  strike where a vanilla option's vanna and volga are zero. In Black–Scholes both are
  proportional to d₂, so this is the strike where d₂ = 0. The derivation writes the
  option price as an average of Black–Scholes prices over realised volatility (the
  "mixing formula"), Taylor-expands, and uses the zero vanna and volga to kill the
  second-order and correlation terms. The approximation is immune to spot–volatility
  correlation to first order.
- **Test against exact Heston prices.** Across maturities 0.5–5 years and correlations
  from −0.9 to +0.9:
  - At 1 year the exact strike is 18.74. The zero-vanna approximation gives 18.37–18.74
    and the at-the-money volatility gives 17.85–18.98.
  - At 5 years with correlation −0.9 the exact strike is 19.12. The approximation gives
    18.54 and at-the-money gives 17.60.
  - At 0.5 years it matches the more involved Carr–Lee approximation almost exactly.
  - Accuracy degrades for long maturities as correlation approaches +1. Beyond about two
    years, stochastic interest rates would need adjusting for.
- **What it does not give.** Unlike Carr and Lee, it says nothing about the hedge. The
  follow-up on forward-starting swaps adds one.

## Why it's in the library

- It turns volatility-swap pricing into something readable straight off a smile: find the
  zero-vanna strike, read its implied volatility.
- It makes the gap between variance and volatility (the convexity of the square root, and
  the effect of skew) concrete.

## Links

- [[rolloos-2018-model-free-pricing-and-hedging-of-forward-starting-volatility-swaps]] —
  the extension to forward-starting swaps, with a hedge
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — the VIX as the
  square root of a variance-swap price, the same variance-versus-volatility gap
- [[roring-2017-volatility-and-variance-swaps]] — an empirical comparison that includes this estimator
