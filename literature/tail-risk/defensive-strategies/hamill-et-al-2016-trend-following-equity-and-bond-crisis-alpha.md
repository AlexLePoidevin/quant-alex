# Trend Following: Equity and Bond Crisis Alpha

| | |
|---|---|
| **Authors** | Carl Hamill, Sandy Rattray, Otto Van Hemert (Man AHL) |
| **Year** | 2016 (version dated 30 August 2016) |
| **Type** | Working paper, SSRN 2831926, 19pp. Monthly data on bonds, commodities, currencies and equity indices, 1960–2015 |
| **PDF** | Not hosted in this repository (SSRN download; no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.2831926](https://doi.org/10.2139/ssrn.2831926) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Trend+Following%3A+Equity+and+Bond+Crisis+Alpha%22+Hamill) |
| **BibTeX** | `hamill2016trend` |
| **Status** | Reference: Table 2 (Sharpe ratios), §4 (skewness) and §5 (performance by equity and bond quintile) |

## What it is

A long-history test of futures trend following, built to answer whether its record depends
on the bond bull market that began in 1985.

- **The strategy.** A barebones time-series momentum strategy ("momCTA") on bonds,
  commodities, currencies and equity indices, built to track the BTOP50 CTA index, plus
  versions using returns at lags 1–4, 5–8 and 9–11 months. Pre-futures history is
  proxied with cash returns financed at local short rates.
- **It worked before and after 1985.** Performance was consistent in 1960–1985, when bonds
  had negative excess returns, and afterwards, when bonds rallied. Gross Sharpe ratios over
  1960–2015 are 1.56 for momCTA across all assets (1.18 bonds, 1.07 commodities, 0.57
  currencies, 0.64 equities), 1.30 for lags 1–4, 0.64 for lags 5–8 and 1.12 for lags 9–11.
  These exclude costs and fees.
- **Positive skew.** Over 3- and 12-month windows, momCTA and the short-lag version show
  clearly positive skewness, robust to alternative skewness measures. The authors explain
  it with a picture: a trend follower's position, as a function of past returns, looks like
  the delta of a long straddle.
- **Crisis alpha in stocks and bonds.** Sorted by rolling three-month S&P 500 and 10-year
  Treasury returns, momCTA does best in the worst quintile for equities and also the worst
  for bonds, and well in the best quintiles too: an "equity smile" and a less familiar,
  stronger "bond smile". The short lags (1–4 months) provide most of the crisis alpha.
- **Removing long equity and bond positions.** Capping equity (or bond) positions at zero
  improves performance in the corresponding crises but lowers the average return.

## Why it's in the library

**It answers the obvious objection to trend following's record.** The post-1985 history is
flattered by falling yields; this paper shows the strategy also worked through the bond
bear market of the 1960s and 1970s, and protected against bond as well as equity sell-offs.

**It is the building block for the other Man papers.** The long-straddle view of trend, and
the finding that faster trend gives more crisis protection, are reused in the
crisis-proofing, rebalancing and volatility-targeting papers.

**Limits.** Gross returns, ex-post volatility scaling, monthly data with cash-based proxies
for early futures, and a strategy chosen to match an existing CTA index. The authors manage
trend-following funds.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a model in which trend following is the optimal rule
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bull and bear market persistence, the condition trend following needs
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — an option-based alternative for crisis protection, with its carry cost
- [[babu-et-al-2020-you-cant-always-trend-when-you-want]] — why trend's weak 2010s came from small market moves, not lost efficacy or diversification
- [[baltas-kosowski-2017-demystifying-time-series-momentum-strategies]] — how the volatility estimate, trend rule and correlations change the same kind of strategy
- [[clare-et-al-2017-reducing-sequence-risk-using-trend-following-and-the-cape-ratio]] — a single-index trend filter applied to retirement withdrawals
- [[dugan-greyserman-2019-the-impact-of-skew-on-performance-and-bias]] — why positively skewed strategies like trend look worse than they are over short windows
- [[hutchinson-obrien-2014-is-this-time-different-trend-following-and-financial-crises]] — the other half of the cycle: trend goes sideways for years after a crisis
- [[jusselin-et-al-2017-understanding-the-momentum-risk-premium]] — a model of why trend following is positively skewed and protects against gradual selloffs but not jumps
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the original time-series momentum paper, 1985–2009, with its smile against the market
- [[roncalli-2017-keep-up-the-momentum]] — why trend's payoff is convex and when it should help in a crisis
- [[sepp-2018-trend-following-strategies-for-tail-risk-hedging-and-alpha-generation]] — why trend's crisis convexity depends on signal half-life and return-measurement frequency
