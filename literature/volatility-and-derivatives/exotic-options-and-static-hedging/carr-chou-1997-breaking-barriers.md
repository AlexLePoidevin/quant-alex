# Breaking Barriers

| | |
|---|---|
| **Authors** | Peter Carr, Andrew Chou |
| **Year** | 1997 |
| **Type** | Article — *Risk* 10(9), September 1997, pp. 139–145 |
| **PDF** | Not hosted in this repository (*Risk* magazine article, publisher copyright) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Breaking+Barriers%22+Carr) for the title and authors |
| **BibTeX** | `carr1997breaking` |
| **Status** | Reference: the "Static replication with Arrows" section (equations 1–9) and "The hedging technique" (adjusted payouts, table A) carry the argument; the full derivation is in Carr and Chou's working paper |

## What it is

A short practitioner article showing how to hedge a barrier option with a portfolio of
ordinary European options that is set up once and unwound only at expiry or when the
barrier is hit, instead of trading the underlying continuously.

- **Arrows from butterflies.** A butterfly spread of down-and-in calls, scaled so its
  payoff triangle has area one, tends to a "down-and-in Arrow": a claim paying at one
  final price provided the barrier was touched. Its value is the second derivative of
  the down-and-in call price with respect to strike.
- **Any payoff from options (equation 7).** A European payoff f(S) equals f(κ) bonds plus
  f′(κ) forwards struck at κ, plus f″(K)dK puts at every strike below κ and calls at every
  strike above κ. With κ set to the forward, this splits any claim into intrinsic value
  and a time value made of out-of-the-money options weighted by the payoff's convexity.
  The same decomposition holds for down-and-in claims with barrier versions of each piece.
- **The barrier hedge.** In the Black-Scholes model, a down-and-in claim with payoff f has
  the same value as a European claim with an *adjusted payout*: f(S) below the barrier,
  and (S/H)^p · f(H²/S) above it, where p = 1 − 2(r − d)/σ². The reflected part is built
  so its value matches the claim's whenever the price sits at the barrier. Down-and-out
  claims follow from in-out parity; up claims by symmetry.
- **When it is exact.** If r = d then p = 1, the adjusted payouts are piecewise linear,
  and a finite number of vanilla options replicates the barrier exactly (the Bowie and
  Carr 1994 result). Otherwise the adjusted payouts are curved but close to piecewise
  linear, so a handful of strikes approximates them well.
- **A recipe.** Given any known closed-form price for a barrier claim, drop the
  restriction that the price is above the barrier, take its limit at expiry to get the
  adjusted payout, and read off the static hedge from equation 7.

## Why it's in the library

**Equation 7 is one of the most reused identities in derivatives.** Writing any smooth
payoff as bonds, a forward and a strip of options weighted by its second derivative is
the basis for replicating variance swaps (the 1/K² strip of the log contract), for
model-free bounds, and for reading risk-neutral densities off option prices. This short
article states it cleanly.

**It explains why static hedges are used in practice.** Dynamic delta hedging of a
barrier fails where gamma and vega are large near the barrier; a static hedge needs only
the implied volatilities at inception and when the barrier is hit, not the realised path.
The cost is that it relies on liquid vanilla options across strikes, and on a model
(here Black-Scholes with constant volatility and no jumps) for the reflection. With
jumps, the price can cross the barrier and the hedge over- or under-replicates, which the
authors note can be anticipated in advance.

**It is a model-dependent result.** The reflection uses a constant-volatility lognormal
model. With a volatility smile the adjusted payout changes, and the hedge is only as good
as the model linking prices at the barrier to prices today.

## Links

- [[shreve-2004]] — the reflection principle and barrier-option pricing in continuous time
- [[merton-1976]] — jumps, the case where the price can cross the barrier and the static
  hedge breaks
- [[derman-et-al-1995-static-options-replication]] — static barrier replication with a fixed set of vanillas
- [[carr-lorig-2015-robust-replication-of-barrier-style-claims]] — robust replication extended to claims on price and volatility
