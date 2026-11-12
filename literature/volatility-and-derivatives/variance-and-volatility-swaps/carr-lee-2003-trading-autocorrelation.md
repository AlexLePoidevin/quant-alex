# Trading Autocorrelation

| | |
|---|---|
| **Authors** | Peter Carr (Courant Institute, NYU), Roger Lee (Stanford) |
| **Year** | 2003 (May; presented at ICBI Barcelona and Amsterdam) |
| **Type** | Slides, 29pp |
| **PDF** | Not hosted in this repository (conference slides, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Trading+Autocorrelation%22+Carr) for the title and authors |
| **BibTeX** | `carr2003trading` |
| **Status** | Reference: covariance swaps, hyper options, the volatility-definition puzzle and up/down-crossers are the main results |

## What it is

A model-free look at contracts that pay on whether a market trends or reverts. Nothing is
assumed about the price process beyond no arbitrage and frictionless trading.

- **Trending and reverting, defined.** A price path is trending if the average product of
  adjacent returns is positive, and reverting if it is negative.
- **Covariance swaps are worth zero.** A swap paying the average product of adjacent
  futures returns can be replicated by a simple futures strategy: hold a position
  proportional to the last return. The strategy is self-financing from a zero start, so
  the fair swap rate is zero. Under the pricing measure the futures price is a martingale,
  and martingale increments are uncorrelated. No arbitrage therefore requires both
  trending and reverting paths to be possible.
- **Hyper options.** An option that can be exercised any number of times, and switches
  between call and put each time. It is a bet on reversion towards the strike. The
  surprising result is that a hyper option on a forward has the same value as a European
  option, and can be hedged by a "polarity matching" strategy in European options.
- **What counts as volatility depends on who is asking.** On a binomial tree, compare a
  steadily trending path with a zig-zag path. A probabilist measuring quadratic variation
  sees the same volatility on both. A statistician sees different volatilities. An option
  writer who delta-hedges loses on the reverting path near the strike, while one who does
  not hedge cares only about where the path ends.
- **European option values need not rise with variance.** A two-period example shows an
  at-the-money call worth more when variance is lower, in a model-free setting. The common
  belief that option prices always increase with volatility is a feature of particular
  models, not a law.
- **Overshooters, upcrossers and downcrossers.** Modified hyper options with forced
  exercise at barriers. One pays the number of times the price crosses up through an
  interval, and it too can be valued from European options. The construction also gives
  new bounds on barrier options.

## Why it's in the library

**Serial correlation is tradable, and its fair price under no arbitrage is zero.** Any
expected profit from betting on trend or reversion has to come from the real-world
probability differing from the risk-neutral one, not from the contract's pricing.

**Short-gamma positions are short reversion near the strike.** Selling an option at a
given implied volatility and delta-hedging loses on paths that hover near the strike. A
hedged option seller is betting on trend, and that is one reason realized volatility alone
does not settle an option's profit and loss.

**"Volatility" is not one number.** Path shape, not just quadratic variation, decides who
wins on an option trade. That matters when comparing realized and implied volatility.

## Links

- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  model-free replication of variance that these contracts extend to covariance
- [[dupire-2006-model-free-results-on-volatility-derivatives]] — other model-free bounds,
  including business-time hedging of options
