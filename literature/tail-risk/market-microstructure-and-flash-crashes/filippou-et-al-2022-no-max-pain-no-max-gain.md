# No Max Pain, No Max Gain: Stock Price Predictability at Options Expiration

| | |
|---|---|
| **Authors** | Ilias Filippou (Washington University in St. Louis); Pedro A. Garcia-Ares (ITAM); Fernando Zapatero (Boston University) |
| **Year** | 2022 (version dated 19 June 2022) |
| **Type** | Working paper, SSRN 4140487, 43pp with tables |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22No+Max+Pain%2C+No+Max+Gain%3A+Stock+Price+Predictability+at+Options+Expiration%22+Filippou) for the title and authors |
| **BibTeX** | `filippou2022maxpain` |
| **Status** | Reference: §3 (the measure), Table 2 (the main result), Tables 4, 8 and 12 (timing, placebo and the no-options control) |

## What it is

An empirical test of the "max pain" idea from options folklore: that as expiration
approaches, a stock's price drifts towards the strike at which the options written on it
pay out the least in total.

- **The measure.** For each stock and expiry, take every listed strike and compute what
  all the calls and puts (weighted by open interest) would pay if the stock finished
  exactly there. The strike with the smallest total payout is the max pain strike. The
  signal is the gap between that strike and the stock price on the second Friday of the
  month, (X_maxpain − S)/S.
- **The test.** US common stocks with listed options, January 1996 to December 2021
  (CRSP, Compustat, OptionMetrics; prices above $5). Each month, on the second Friday,
  stocks are sorted into deciles on the signal and held for one week to expiry. A
  zero-cost portfolio buys the top decile (max pain strike above the price) and sells the
  bottom decile.
- **The headline numbers.** The spread earns about 0.4% a week, equal- or value-weighted
  (t = 3.28 and 3.01), with CAPM and Fama–French three-factor alphas of 0.3–0.4% a week,
  all significant. In Fama–MacBeth regressions the max pain coefficient stays positive and
  significant after controlling for size, price, book-to-market, illiquidity, volume,
  institutional ownership, idiosyncratic volatility, momentum and weekly and monthly
  reversals. It is larger for small and illiquid stocks.
- **Timing.** The effect is concentrated in the last week. Portfolios formed three or four
  weeks before expiry earn positive but insignificant returns; formed two weeks before,
  the raw spread is significant but the alphas are not. A placebo that holds for the week
  *before* the final week finds nothing.
- **Who trades.** High max pain stocks show significantly higher abnormal volume and net
  buying (signed TAQ trades, 2006–2021) in the final week. Retail order imbalance shows no
  significant difference, which the authors read as institutional activity.
- **Controls.** Matching each optionable stock to a similar stock without options (by size
  and volume) and giving it the same signal produces no spread at all (t = −0.61 and
  0.06). Index options sorted the same way show no effect.
- **Interpretation.** The authors point to two mechanisms: hedge rebalancing by option
  dealers pulling prices towards heavily traded strikes (Avellaneda–Lipkin, Ni–Pearson–
  Poteshman's evidence of price clustering at strikes), and deliberate manipulation by
  holders of large short option positions.

## Why it's in the library

**It is evidence that options positioning moves the underlying.** The no-options control
is the strongest part: the same signal attached to a similar stock without listed options
predicts nothing. Whatever the mechanism, the effect comes from the options market. This
is the single-stock, week-of-expiry version of the dealer-hedging flows that the tail-risk
notes describe for the index.

**It is a small, short-horizon effect in hard-to-trade stocks.** About 0.4% a week before
costs, rebalanced weekly, strongest in small, illiquid growth stocks. The paper reports no
transaction costs, and a weekly decile spread in those names would pay a large share of
the edge in spreads.

**It is a working paper with loose ends.** Several table captions describe "call option
returns" when the tables report stock returns, and the conclusion describes the placebo
and the two-week formation results differently from the body. The manipulation story is
inferred from the timing and the institutional order flow, not observed directly.

## Links

- [[fama-french-1993]] — the three-factor model the alphas are measured against
- [[carhart-1997]] — momentum, one of the controls that does not explain the effect
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — option hedging flows feeding back
  into the underlying, at the scale of the whole market
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — dealer hedging as the channel by which option positions move the underlying
