# Strategic Risk Management: Out-of-Sample Evidence from the COVID-19 Equity Selloff

| | |
|---|---|
| **Authors** | Campbell R. Harvey (Duke; adviser to Man Group), Edward Hoyle, Sandy Rattray, Otto Van Hemert (Man Group) |
| **Year** | 2020 (version of 18 July 2020) |
| **Type** | Working paper, SSRN 3655196, 11pp. Not peer reviewed. Data January 1985 to March 2020 |
| **PDF** | Not hosted in this repository (SSRN download with no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3655196](https://doi.org/10.2139/ssrn.3655196) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Strategic+Risk+Management%3A+Out-of-Sample+Evidence+from+the+COVID-19+Equity+Selloff%22+Harvey) |
| **BibTeX** | `harvey2020covid` |
| **Status** | Reference: §1 (best strategies in the selloff, Table 1), §2 (trend: MOM vs moving-average crossovers), §3 (volatility targeting) and §4 (strategic rebalancing) |

## What it is

A short follow-up by Man Group to its 2016–2019 "strategic risk management" series. The
February–March 2020 selloff happened after those papers were written, so the authors use it
as an out-of-sample test of three of their recommendations. The selloff is defined as the
S&P 500 drawdown from the close of 19 February to the close of 23 March 2020 (about −34%).

- **Which defensive assets and strategies paid off.** This extends the "Best Strategies"
  table to a ninth drawdown of −15% or worse:
  - **Passive hedges:** one-month at-the-money S&P puts returned about +33% over the episode.
    Short credit risk, levered to 10% volatility, returned about +102% in excess of bills.
    Ten-year Treasuries paid only modestly, and gold was slightly down.
  - **Trend:** every time-series momentum (MOM) strategy made money, and the 1-month
    version did best, as you would expect in a fast selloff. Capping equity positions so they
    can only be short added another 5 to 9 percentage points.
  - **Quality stocks:** profitability and growth long-short portfolios held up. Safety (low
    risk) did badly, especially beta-neutral, as it did in 2007–2009. The authors put this
    down to tightening credit conditions hurting levered low-risk positions.
- **Why real trend followers did worse than the paper's MOM.** The SG CTA index lost 4.8%
  over the episode; the trend-only and mutual-fund versions did a little better. The authors
  give three reasons:
  - CTAs also run carry and other non-trend strategies, which lost money.
  - Most trend followers use moving-average crossovers (MACs). A MAC matched to a MOM
    signal correlates 0.9 or more with it, but puts little weight on the latest returns. It
    therefore reacts more slowly to a sudden fall. For example, MAC(50, 200) was barely
    positive over the crisis, while the matching 12-month MOM made money.
  - Trend followers tend to run slower models, and here the fastest models did best.
- **Volatility targeting.** Sizing US equities to a constant volatility, rather than a constant
  notional, meant holding more than 100% in a calm January and cutting exposure from late
  February as volatility rose. The authors report it roughly halved the 2020Q1 drawdown
  compared with constant notional, which fell below −30%.
- **Strategic rebalancing.** The rule rebalances a 60-40 portfolio back to target only if
  the stock-minus-bond trend (1, 3 or 12 months) is above its long-run average, and then
  only halfway. At end-February 2020 every version said to wait. The cumulative 2020Q1
  return was −7.2% to −7.4%, against −8.0% for always rebalancing. That is a 0.6–0.8 point
  gain, much smaller than the roughly 5 points the rule saved in 2007–2009, when the fall was
  slower and longer.

## Why it's in the library

- **It is an honest out-of-sample check.** Most crisis-strategy papers are fitted to the
  crises they describe. This one tests rules published beforehand on an event that came
  afterwards, which is the only kind of evidence that counts. It is one event, though, and a
  very fast one. Results that favoured fast trend and fast volatility estimates might not
  repeat in a slow bear market such as 2000–2002.
- **The MOM-versus-MAC point is practical and checkable.** Two trend signals that correlate at
  0.9 can still behave very differently in a crash, because they weight recent days
  differently. It is a concrete case of correlation hiding a difference in tail behaviour.
- **Read it as the summary of a series.** The underlying studies are the "Best Strategies for
  the Worst of Times" paper, the volatility-targeting paper, the strategic rebalancing paper
  and the drawdowns paper. All of them are by the same Man Group team, which also sells trend
  and risk-managed products.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  other way to hedge a selloff: long VIX futures and calls, and what they cost in normal years
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — why rule-based put hedges bleed between crises
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — which moving
  average is optimal for trend following, and why the window matters
- [[keller-keuning-2016-paa]] — a tactical allocation rule that moves to safety when breadth
  deteriorates, an alternative crash-protection mechanism
