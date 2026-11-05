# Time for a Change: The Variance Gamma Model and Option Pricing

| | |
|---|---|
| **Authors** | Peter Carr, Apollo Hogan, Harvey Stein (Quantitative Finance R&D, Bloomberg LP) |
| **Year** | 2007 (dated 11 January 2007, revision 1.28) |
| **Type** | Practitioner article written for Bloomberg users, 12pp. Introduces the variance gamma model as implemented in the terminal's SKEW function |
| **PDF** | Local copy only (Bloomberg document with no open licence) |
| **BibTeX** | `carr2007vgbloomberg` |
| **Status** | Reference: the whole piece is short; §I builds the model, §II shows the fit, the sidebar argues for a model over interpolation |

## What it is

A non-technical introduction to the variance gamma (VG) model, built up from a story about
how news reaches a market, followed by a walk-through of fitting it to S&P 500 options.

- **From the binomial tree to news arrivals.** In the binomial model the price moves once
  per step by a fixed percentage, as if news arrived at a constant rate and every item had
  the same impact. The authors instead model the waiting times to good and bad news as
  exponential, and each news item's return impact as a gamma-distributed jump (up for good
  news, down for bad). Returns are then the difference of two compound Poisson processes.
- **Letting the arrival rates go to infinity.** To capture the "jitter" seen in
  short-dated options as well as jumps, the arrival rates are sent to infinity. What is
  left is the difference of two independent gamma processes: a pure-jump process with
  infinitely many small jumps in any interval and no Brownian component.
- **Three parameters.** With a common shape for the two gamma processes, the model has
  three parameters, σ, θ and ν. Each is the main driver of one moment: σ the standard
  deviation, θ the sign of the skewness, ν the excess kurtosis. The name comes from the
  fact that the return density is a normal density averaged over a gamma-distributed
  variance (Madan and Seneta, 1990).
- **The fit.** On S&P 500 options the VG implied volatilities sit within 0.6 volatility
  points of the market smile in the example shown. The remaining gaps come from fitting
  calls and puts at once (calls trade at higher implied volatility than puts despite
  put-call parity), from the different liquidity of in- and out-of-the-money options, and
  from transaction costs in the wings. Bloomberg fits only out-of-the-money options.
- **Time-adjusted moneyness.** Plotting implied volatility against ln(K/S)/(σ√t) rather
  than strike shows the skew does not flatten with maturity the way it seems to in strike
  space.
- **Why not just interpolate implied volatility (sidebar).** A model gives arbitrage-free
  prices across strikes, a principled way to price strikes outside the quoted range,
  Greeks that include the change in implied volatility as spot moves, and a smooth
  density. Linear interpolation of implied volatility can imply jumps in the density.

## Why it's in the library

**It is the clearest plain-language route into pure-jump option models.** The "news
arrives at random times with random impact" story explains why a pure-jump process with
infinite activity can stand in for Brownian motion, and why three parameters can capture
volatility, skew and kurtosis. The technical papers on the same model family
([[carr-et-al-2003-stochastic-volatility-for-levy-processes]],
[[carr-et-al-2004-from-local-volatility-to-local-levy-models]],
[[carr-et-al-2005-pricing-options-on-realized-variance]]) assume you already have this
picture.

**The sidebar is a good checklist for any volatility surface.** Its four reasons to prefer
a model over interpolating quotes (no-arbitrage, extrapolation, hedge ratios, smoothness)
apply whatever model is used.

**It is a vendor article.** It shows one example fit and makes no systematic comparison
with other models. The comparisons are in the papers above.

## Links

- [[merton-1976]] — the first jump model for option pricing, with finite-activity jumps
  added to a diffusion; VG drops the diffusion altogether
- [[carr-et-al-2003-stochastic-volatility-for-levy-processes]] — VG and its relatives
  given stochastic volatility, so they fit across maturities as well as strikes
- [[carr-et-al-2004-from-local-volatility-to-local-levy-models]] — VG run at a speed that
  depends on price and time, the jump analogue of local volatility
- [[carr-et-al-2005-pricing-options-on-realized-variance]] — the same pure-jump models used
  to price options on realized variance
- [[carr-wu-2007-stochastic-skew-in-currency-options]] — the up-jump/down-jump split taken
  further: separate random clocks for each side give a skew that changes sign
