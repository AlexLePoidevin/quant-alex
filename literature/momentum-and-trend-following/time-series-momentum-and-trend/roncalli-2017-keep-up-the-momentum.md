# Keep Up The Momentum

| | |
|---|---|
| **Authors** | Thierry Roncalli (Amundi Asset Management) |
| **Year** | 2017 (discussion paper dated December 2017; published in *Journal of Asset Management* 19(5), 351–361, 2018) |
| **Type** | Non-technical discussion paper, 16pp. Simulations and stylised figures, no new empirical backtest |
| **PDF** | Not hosted in this repository (Amundi discussion paper / SSRN 3083921; journal version © Springer) |
| **Find it** | [doi.org/10.1057/s41260-018-0078-7](https://doi.org/10.1057/s41260-018-0078-7) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Keep+Up+The+Momentum%22+Roncalli) |
| **BibTeX** | `roncalli2017momentum` |
| **Status** | Reference: the key takeaways (p. 2) and the sections on payoff, correlation and hidden risks summarise the technical companion paper |

## What it is

A plain-language summary of Jusselin et al. (2017), "Understanding the Momentum Risk
Premium", which derives the return distribution of trend-following strategies
mathematically. Its main claims:

- **Convex payoff.** A trend-following strategy pays off like a long straddle: losses are
  bounded and gains are not, so returns are positively skewed. The strategy is short
  short-term volatility (it pays "gamma costs" in choppy markets), so it loses more often
  than it wins and earns its keep in a few big trends.
- **What drives it.** Performance depends on the absolute size of assets' Sharpe ratios
  (a trend down is as good as a trend up), the correlation between assets, and the length
  of the moving average. Compared with simply holding the asset, trend following has the
  better Sharpe ratio when the asset's Sharpe ratio is below about 0.35.
- **Time series vs cross-section.** Time-series momentum works best with uncorrelated
  assets, so it belongs in a multi-asset futures universe. Cross-sectional momentum
  (winners minus losers) works best with highly correlated assets, so it belongs inside a
  homogeneous universe such as one region's stocks.
- **Horizon.** Short-term trend is riskier, more sensitive to how the trend is estimated,
  and has a lower Sharpe ratio than long-term trend.
- **Hidden risks.** Too much leverage hurts, because gamma costs do not scale linearly, and
  the convexity assumes no price jumps. Trend helps in high-volatility crises like 2008,
  but not necessarily in sudden jump crashes.
- **The conclusion.** Momentum is a beta strategy with time-varying sign, positive in good
  times and negative in bad, so its job is diversification in bad times rather than
  standalone return. "Beta is beautiful, but convex beta is precious and scarce."

## Why it's in the library

It is the clearest short statement of why trend following is held as a crisis diversifier
rather than for its Sharpe ratio, and of when it should and should not be expected to help.
The split between time-series momentum (wants uncorrelated assets) and cross-sectional
momentum (wants correlated ones) is a useful rule for choosing a universe.

The results come from stylised models (Brownian prices, no jumps, continuous trading), so
the numbers are illustrative; the companion paper has the derivations.

## Links

- [[jusselin-et-al-2017-understanding-the-momentum-risk-premium]] — the technical companion
  paper with the derivations summarised here
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the empirical evidence for
  time-series momentum across futures markets
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the empirical case
  that trend paid in equity and bond bear markets
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — trend
  against puts as a hedge, tested on the ten worst S&P 500 months
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the
  optimal moving average when markets switch between bull and bear states
- [[brooks-2017-a-half-century-of-macro-momentum]] — momentum in macro fundamentals rather
  than prices, as a diversifier for price trend
- [[harvey-et-al-2020-strategic-risk-management-out-of-sample-evidence-from-covid-19]] —
  a sudden crash in which fast trend still helped
- [[bruder-et-al-2011-trend-filtering-methods-for-momentum-strategies]] — the earlier Lyxor survey of the filters used to estimate the trend itself
