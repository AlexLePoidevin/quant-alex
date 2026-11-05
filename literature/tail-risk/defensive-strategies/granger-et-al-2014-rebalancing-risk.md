# Rebalancing Risk

| | |
|---|---|
| **Authors** | Nick Granger, Doug Greenig, Campbell R. Harvey, Sandy Rattray, David Zou (Man-AHL; Greenig independent; Harvey also at Duke) |
| **Year** | 2014 (version dated 3 October 2014; first posted 27 August 2014) |
| **Type** | Working paper, SSRN 2488552, 34pp, with a technical appendix. Data 1990–2014 plus simulations |
| **PDF** | Local copy only (SSRN download; no open licence) |
| **BibTeX** | `granger2014rebalancing` |
| **Status** | Reference: Figures 1–3 (the payoff of rebalancing), Figure 6 and Table 1 (the momentum overlay); the appendix gives the analytic argument |

## What it is

The original Man-AHL paper making the point that a fixed-weight portfolio carries option
risk.

- **Rebalancing is a short straddle.** Rebalancing to fixed weights is equivalent to
  buy-and-hold plus a short straddle on the relative performance of the assets. When
  stocks and bonds move together nothing needs trading; when they diverge, rebalancing
  keeps buying the loser. Small divergences earn a small "rebalancing premium"; large ones
  cost a lot.
- **The evidence.** In both 2008–09 and 2001–02, a monthly-rebalanced 60/40 S&P 500 / 10-year
  Treasury portfolio had a deeper drawdown than the drifting one, by 5.7 and 3.7
  percentage points; the rebalanced portfolio eventually caught up. One-year returns of
  rebalanced minus buy-and-hold, plotted against stock-minus-bond performance, form an
  inverted smile, in data since 1990 and in simulation.
- **Why it matters for 60/40.** About 85% of a 60/40 portfolio's risk comes from equities,
  whose downside tail is fat. Rebalancing does not just inherit that tail, it deepens it.
- **The overlay.** Momentum (trend) trading has the opposite payoff, a long-straddle shape,
  which the authors had shown analytically in an earlier *Risk* article. Adding a trend
  overlay sized at 10% of the portfolio's risk, run on the same stocks and bonds, cut the
  maximum drawdown materially, raised the Sharpe ratio modestly and improved skewness, at both rebalancing frequencies tested. The appendix argues the effect follows from the
  trading rules themselves, not from a particular history.

## Why it's in the library

**It gives the mechanism behind a widely used portfolio.** Seeing rebalancing as a sold
option on relative performance explains why a 60/40 fund loses more than buy-and-hold in a
trending crash and earns a little in choppy markets. That is concrete enough to size and to
hedge.

**It is the starting point for the later Man papers.** Strategic rebalancing and the
crisis-alpha work build on this paper's claim that trend is the natural hedge for
rebalancing.

**Limits.** Short empirical sample (1990–2014), two crises, a proprietary moving-average
model for the overlay, and no out-of-sample test. The analytic argument is the stronger
part.

## Links

- [[booth-fama-1992]] — diversification returns: the benefit side of rebalancing
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the trend rule as an optimal response to persistent regimes
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — other portfolio rules that are implicitly short volatility
- [[hong-meyer-brauns-2021-portfolio-rebalancing-tradeoffs-and-decisions]] — choosing a rebalancing rule on turnover against tracking error rather than on return
- [[pedersen-2021-does-volatility-harvesting-really-work]] — random-portfolio evidence that the rebalancing premium is near zero outside crash recoveries
