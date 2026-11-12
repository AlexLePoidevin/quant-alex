# Strategic Rebalancing

| | |
|---|---|
| **Authors** | Sandy Rattray, Nicolas Granger, Campbell R. Harvey, Otto Van Hemert (Man Group; Harvey also at Duke) |
| **Year** | 2020 (working version dated 19 December 2019) |
| **Type** | Paper. SSRN 3330134, 25pp; published in *Journal of Portfolio Management* 46(6), 10–31 (2020). Data 1960–2017 (1927 onwards for illustrations) |
| **PDF** | Not hosted in this repository (SSRN download of a Man Group working paper; no open licence) |
| **Find it** | [doi.org/10.3905/jpm.2020.1.150](https://doi.org/10.3905/jpm.2020.1.150) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Strategic+Rebalancing%22+Rattray) |
| **BibTeX** | `rattray2020strategic` |
| **Status** | Reference: §1 (why rebalancing is concave), §2 (trend allocation) and §3 (rebalancing rules) carry the results |

## What it is

The follow-up to Granger et al. (2014): rebalancing a 60/40 portfolio is an active
strategy that hurts in sustained sell-offs, and trend signals can offset it.

- **Rebalancing versus buy-and-hold, in one line.** In a two-period model the return of a
  rebalanced portfolio minus buy-and-hold is −w_S·w_B·κ₁·κ₂, where κ is the stock-minus-bond
  return in each period. If relative performance trends (κ₁ and κ₂ have the same sign),
  rebalancing loses; if it reverses, rebalancing gains. Rebalancing is a bet on mean
  reversion.
- **The problem in practice.** Buy-and-hold is not an option either: a 60/40 mix started in
  1927 drifts to 76% stocks by 1929, 32% by 1932 and towards 100% over time. In 2007–09 the
  monthly-rebalanced 60/40 portfolio's maximum drawdown was about 5 percentage points (1.2×)
  worse than buy-and-hold.
- **Fix 1: a trend allocation.** Putting 10% in a trend strategy on stocks and bonds and 90%
  in the rebalanced 60/40 improved the average of the five worst 60/40 drawdowns since 1960
  by about 5 percentage points, with no loss of average return over the sample. Black
  Monday 1987 is the one crisis where it did not help.
- **Fix 2: strategic rebalancing.** Common heuristics (rebalancing less often, thresholds,
  partial rebalancing) cut the average maximum drawdown by at most about 1 point. Rules that
  delay rebalancing while the stock or stock-minus-bond trend is negative improved it by
  2–3 points, without any explicit trend position.
- **The two fixes behave alike.** Their return impact on the rebalanced portfolio has a
  0.62 correlation; both help mainly when stocks fall relative to bonds.

## Why it's in the library

**It names a hidden risk in the default portfolio.** Monthly rebalancing to fixed weights
sells the asset that is rising and buys the one that is falling. That earns a small
premium when markets mean-revert and costs a lot when a sell-off keeps going, which is
exactly when losses hurt most.

**It gives two concrete, cheap remedies.** A modest trend sleeve, or simply timing the
rebalancing trades with a trend signal. The second needs no new product, only a change to
when existing trades are made.

**Limits.** Five crises in one 58-year US sample, results before costs in most tables, and
trend strategies sold by the authors' firm. The size of the improvement depends on how
trending the next crisis is.

## Links

- [[booth-fama-1992]] — the case for rebalancing: diversification returns from holding fixed weights
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — when trend rules are optimal, given persistent bull and bear regimes
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — how persistent bear markets are, and the rallies inside them
- [[hoffstein-sibears-2018-diversifying-the-what-how-and-when-of-trend-following]] — how much a trend rule's result depends on the rebalance week, signal and lookback
- [[pedersen-2021-does-volatility-harvesting-really-work]] — rebalanced portfolios lag in declines and lead in recoveries, on 920 US stocks
