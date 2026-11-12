# Model Free Results on Volatility Derivatives

| | |
|---|---|
| **Authors** | Bruno Dupire (Bloomberg NY) |
| **Year** | 2006 (talk at SAMSI, Research Triangle Park, 27 February 2006) |
| **Type** | Slides, 41pp |
| **PDF** | Not hosted in this repository (conference slides, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Model+Free+Results+on+Volatility+Derivatives%22+Dupire) for the title and authors |
| **BibTeX** | `dupire2006modelfree` |
| **Status** | Reference: part I (VIX futures pricing) and part III (lower bound on variance calls) carry the results; the slides have little text, so read them with [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] for the background |

## What it is

A talk on what can be said about volatility derivatives without assuming a model for how
volatility moves.

- **VIX is a variance swap rate.** The 2003 VIX squared is the price of a 1/K²-weighted
  strip of out-of-the-money options, the log-contract replication of a variance swap.
  Holding options of two maturities (buy T2, sell T1) locks in the forward VIX² for the
  later date.
- **VIX futures have a model-free upper bound.** A VIX future pays VIX, the square root of
  that forward variance. Because the square root is concave, the future is worth at most
  the square root of the forward variance price. The gap is the variance of the future VIX
  (convexity), so FVIX ≈ √(forward variance − Var[VIX at T1]). The variance can be
  estimated from the historical volatility of the futures and of spot VIX. After launch,
  futures were at least 20× cheaper to trade than the option strip, so the direction of
  replication reversed: use futures to hedge the strip, not the other way round.
- **A short survey of volatility models.** Neuberger (1990), Dupire (1992), Heston (1993),
  Dupire (1996) and Derman–Kani (1997), Carr–Lee (2003) and others, with their limits:
  stochastic-volatility models price volatility claims but give no natural hedge; Carr–Lee
  needs spot and volatility to be uncorrelated, which forces symmetric smiles.
- **Skew implies volatility of volatility.** A skewed smile means the spot and its
  volatility are correlated. A non-flat smile therefore puts a lower bound on how variable
  realized variance must be.
- **The trader's puzzle.** If you know realized volatility will be 10% and sell a put at
  15%, can you be sure of a profit? Delta-hedging on a calendar clock can still lose,
  because big moves near the strike at expiry hit large negative gamma. Hedging in
  "business time" (adjusting the hedge by the variance realized so far, not by the
  calendar) locks in Put(15%) − Put(10%) for sure.
- **A lower bound for variance calls.** Sell a convex payoff on the spot and delta-hedge it
  in business time. The replication works until the quadratic variation runs out, and a
  call on realized variance covers the rest. This gives a lower bound on the price of a
  variance call from today's vanilla option prices alone. If the call trades below it,
  there is an arbitrage: buy the variance call, sell all options whose implied variance is
  above the strike, and hedge in business time.

## Why it's in the library

**It explains the convexity gap between VIX futures and variance.** A VIX future trades
below the square root of the forward variance, and the gap is larger when volatility of
volatility is high. That matters when comparing VIX futures with variance swaps or with
the VIX index itself.

**The smile carries information about volatility of volatility.** The steeper the skew,
the more variable future realized variance must be. Option prices alone say something
about how much volatility will move, before any model is fitted.

**Business-time hedging is a useful idea beyond this talk.** Hedging by the variance
realized rather than the time elapsed separates the profit on a volatility view from the
path the price takes.

## Links

- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  log-contract replication of variance that the VIX formula and this talk build on
- [[carr-lee-2003-trading-autocorrelation]] — model-free hedging of other path-dependent
  volatility claims
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — pricing VIX futures
  with an explicit mean-reverting variance model instead of a bound
- [[merton-1976]] — jumps, which the continuity assumption behind every bound here rules out
