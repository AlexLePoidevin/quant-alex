# Model-Free Pricing and Hedging of Forward Starting Volatility Swaps

| | |
|---|---|
| **Authors** | Frido Rolloos |
| **Year** | 2018 (dated 27 April 2018; SSRN 3177299) |
| **Type** | Short note, 8pp |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `rolloos2018forward` |
| **Status** | Reference: §4.1 (pricing) and §4.2 (hedging) are the result |

## What it is

The forward-starting version of the zero-vanna rule for volatility swaps, plus a hedge.

- **The instrument.** A forward-starting volatility swap pays the volatility realised over
  a future window [T, T′] that has not started yet. The paper uses forward-starting
  options whose strike is set as a fraction of the spot price on the start date, and
  assumes these trade liquidly (reasonable for major equity indices and FX pairs).
- **Pricing.** The fair strike is approximately the forward-starting implied volatility at
  the strike where the option's vanna and volga are zero (d₂ = 0). This generalises the
  spot-starting result of Rolloos and Arslan, and holds for a wide class of stochastic
  volatility models with zero rates and dividends.
- **Hedging.** The zero-vanna strike moves as the smile moves, so a fixed-strike option
  stops being zero-vanna. The paper shows the change in the swap strike can be hedged
  approximately, without a model, by trading zero-vanna forward-starting straddles. The
  notional is vega-weighted and scaled by a skew adjustment, one plus the forward
  implied volatility times the time to expiry times the skew at that strike. The author
  calls this the first non-parametric result for forward-starting volatility swaps.
- **No numerical test.** Unlike the spot-starting note, there is no table against an
  exact model price; the accuracy is argued, not shown.

## Why it's in the library

- It gives a replicating recipe for exposure to future realised volatility, which is what
  a VIX future approximates on the variance side.
- The skew-adjusted hedge ratio shows how the slope of the smile enters the hedging of
  volatility products.

## Links

- [[rolloos-arslan-2015-taylor-made-volatility-swaps]] — the spot-starting result this
  extends
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] —
  long positions in forward volatility (VIX futures) used as a portfolio hedge
