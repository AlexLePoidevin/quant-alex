# Volatility as an Asset Class: Holding VIX in a Portfolio

| | |
|---|---|
| **Authors** | James S. Doran (University of New South Wales) |
| **Year** | 2020 (*Journal of Futures Markets* 40(6), 841–859; SSRN 3514141 working version dated 2 January 2020) |
| **Type** | Journal article, 19pp. S&P 500 and VIX 1990–2017; SPX options (OptionMetrics) 1996–2017 |
| **PDF** | Not hosted in this repository (the Wiley published version; the SSRN working version is in the same source folder and has the same results) |
| **Find it** | [doi.org/10.1002/fut.22094](https://doi.org/10.1002/fut.22094) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Volatility+as+an+Asset+Class%3A+Holding+VIX+in+a+Portfolio%22+Doran) |
| **BibTeX** | `doran2020vix` |
| **Status** | Reference: §3 (cash VIX as a hedge), §4.1 (which SPX options drive VIX changes) and §4.2–4.3 (the synthetic VIX hedge and its limits) carry the results |

## What it is

A paper in three steps on whether volatility can be held as a hedge for an equity
portfolio, and if the VIX itself can't be bought, what can stand in for it.

- **If VIX were investable, it would be a very good hedge.** Monthly S&P 500 and VIX
  returns, 1990–2017, have correlation −0.64. The response is asymmetric: in down months
  the VIX rises 16.25% on average, in up months it falls 6.83%. A regression puts the VIX
  move at about −5.4% per −1% in the index when the market falls, and close to zero when it
  rises. A portfolio of S&P 500 plus a regression-sized VIX sleeve (5% on average) that drops
  the hedge when VIX is above its mean plus one standard deviation earns significant CAPM,
  4-factor and 6-factor alphas, and ends at almost twice the buy-and-hold dollar value.
- **Tradable VIX products don't deliver that.** Portfolios hedged with VIX futures
  underperform the cash-VIX version by 44bp a month (4-factor, 2006–2017) and underperform
  the S&P 500 itself; SPX puts, VIX calls and VXX do about as badly. The futures price in the
  mean reversion that makes cash VIX valuable.
- **Which options move the VIX.** Regressing daily log VIX changes on the price and moneyness
  changes of every SPX option (about 2.5 million option-days) finds that put price changes
  and call moneyness changes drive VIX. Via put–call parity this means in-the-money puts,
  which are not in the VIX formula at all, track VIX best.
- **A synthetic VIX hedge (VIXo+).** Each month buy a 5% ITM–5% OTM put spread and sell an
  ATM–5% OTM call spread on the S&P 500, sized as above, and switch it off when VIX is above
  mean + 1 SD. Over 1996–2017 this returns 10.1% a year at 15.2% volatility, 1.8% a year more
  than buy-and-hold with 3.7 points less volatility, after bid-ask costs; alphas are
  significant at 5%. The edge comes from bad markets (about +18% relative on average, +45% in
  2000, +34% in 2008), paid for in good ones (about −5%). Always-on, the same hedge
  underperforms the index.
- **What it cannot do.** The hedge misses the extreme spikes: in the 28 months with S&P losses
  worse than 5%, the index lost 7.82% on average and the switched hedge portfolio still lost
  5.97%. Since 2011 it has lagged the index in return (not risk-adjusted), because the short
  call spread is effectively a covered call.

## Why it's in the library

It answers the question the long-VIX papers leave open. Szado shows what VIX futures and
calls did for a 60/40 portfolio; Doran shows why cash VIX would hedge well but the tradable
products don't, and builds the hedge from SPX options instead. Two points worth keeping:

- **The on/off threshold does a lot of the work.** The always-on versions underperform; the
  results depend on removing the hedge when VIX is already high, a rule chosen with the same
  data it is tested on. The threshold is reported as robust between the mean and mean + 2 SD,
  but there is no out-of-sample test.
- **The structure caps upside.** Selling the call spread is what makes the hedge cheap, and it
  is also why it trails in strong bull markets. The trade-off is the usual one: full
  crash protection costs more than it pays over a long sample.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  same question with tradable VIX futures and calls in a 60/40 portfolio
- [[carr-wu-2006-a-tale-of-two-indices]] — what the VIX formula measures, the formula this
  paper deconstructs option by option
- [[carr-wu-2009-variance-risk-premia]] — the variance risk premium that makes holding
  long volatility a steady cost
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — a manager's argument that rule-based tail hedges bleed, which this paper's always-on
  results illustrate
- [[ang-chen-2002]] — correlations rising in down markets, the reason diversifying assets fail
  as hedges in 2008
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  option-strip replication behind the VIX
