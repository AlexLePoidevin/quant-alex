# Understanding the Momentum Risk Premium: An In-Depth Journey Through Trend-Following Strategies

| | |
|---|---|
| **Authors** | Paul Jusselin, Edmond Lezmi, Hassan Malongo, Côme Masselin, Thierry Roncalli (Amundi Asset Management), Tung-Lam Dao |
| **Year** | 2017 (September 2017) |
| **Type** | Paper. SSRN 3042173, 102pp (57pp of text plus long appendices). Continuous-time theory with an empirical section on 20 futures markets |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3042173](https://doi.org/10.2139/ssrn.3042173) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Understanding+the+Momentum+Risk+Premium%3A+An+In-Depth+Journey+Through+Trend-Following+Strategies%22+Jusselin) |
| **BibTeX** | `jusselin2017momentum` |
| **Status** | Reference: §2 (the Bruder–Gaussel model and its multivariate extension), §3.4 (replicating the SG CTA Index), §4 (hedging and skewness events) and §5 (conclusion) |

## What it is

A theory paper on trend following. It extends Bruder and Gaussel's (2011) single-asset
model to many assets, and uses it to explain the properties that the empirical literature
reports for trend-following (time-series momentum) strategies.

- **The model.** Prices follow geometric Brownian motion with an unobserved, randomly
  drifting trend. The best estimate of that trend is an exponentially weighted moving
  average, and its optimal speed is the ratio of trend volatility to price volatility. The
  strategy holds a position proportional to the estimated trend.
- **The P&L splits into two parts.** An *option profile*, which is convex in the trend
  estimate (the lookback-straddle shape Fung and Hsieh found), and a *trading impact*, which
  depends on the asset's Sharpe ratio and the moving-average speed. The paper finds the
  trading impact is the first-order effect and the convexity second-order.
- **Statistical properties.** Losses are bounded and gains are not, so the P&L is
  positively skewed and close to a chi-square distribution rather than a normal one. When the
  absolute Sharpe ratio of the underlying is low (below about 0.35 in their example, with 30%
  volatility and a one-year average) the hit ratio is under 50%: trend followers lose more
  often than they win, but win more when they do. The strategy has negative vega: it dislikes
  rising volatility.
- **Diversification works differently from a long-only portfolio.** For time-series
  momentum the best case is uncorrelated assets (a correlation of +1 and −1 both leave a
  single trend). It prefers a few markets with large absolute Sharpe ratios to many weak
  ones, and concentrating on the big trend beats spreading risk. Cross-sectional momentum is
  the opposite: it prefers highly correlated assets and a wide dispersion of Sharpe ratios.
  A multivariate moving average estimates trends better than separate univariate ones, but
  getting the window slightly wrong (a 3- or 6-month average for a 4-month trend) costs
  little.
- **Replicating CTAs.** An equal-weighted set of single-market trend strategies on 20
  futures, each targeting 20% volatility, reaches a daily correlation of 78% with the SG CTA
  Index at a moving-average duration of about five months. Replicating asset class by asset
  class gives correlations mostly below 50%: diversification across classes is what makes
  the index.
- **2008.** The authors argue trend's 2008 gain came more from long bond positions (a
  strong, low-volatility trend) than from short equities (a strong but very volatile one).
- **Hedging.** Trend following protects against gradual declines (volatility risk) but not
  against sudden jumps (skewness events), and the protection is weaker when the hedged asset
  is a diversified multi-asset portfolio. They cite CTAs in January 2015 as an example.
- **Leverage.** As with CPPI, too much leverage in high volatility makes the "gamma cost"
  of the strategy prohibitive.

## Why it's in the library

**It is the clearest analytical account of why trend following has the return profile it
does**: positive skew, a low hit ratio, bounded losses and negative vega. These are usually
shown by backtests; here they follow from a simple model.

**The diversification result is useful in practice.** It explains why time-series momentum
is run across many asset classes and cross-sectional momentum within one, and why adding
more weakly trending markets to a trend book can lower its expected gain.

**It separates downside protection from tail protection.** Trend hedges slow selloffs, not
crashes. That is the same distinction the Man Group and AQR defensive-strategy papers make
from data.

**Limits.** The authors call it a toy model. It assumes continuous rebalancing with no
transaction costs or fees, fixed allocations and known price dynamics without jumps. The SG
CTA replication is also gross of costs and fees.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — another model in which a moving-average rule is the optimal trend filter
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the empirical crisis-alpha evidence for multi-asset trend following
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility scaling as an implicit momentum position
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — puts versus trend as hedges, the empirical side of the downside-versus-tail distinction
- [[molyboga-swedroe-qian-2020-short-term-trend-a-jewel-hidden-in-daily-returns]] — the effect of the moving-average window in practice
