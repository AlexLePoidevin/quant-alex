# Trends Everywhere

| | |
|---|---|
| **Authors** | Abhilash Babu, Ari Levine, Yao Hua Ooi, Erik Stamelos (AQR) and Lasse Heje Pedersen (AQR, Copenhagen Business School, NYU) |
| **Year** | 2020 (Journal of Investment Management); this copy is the working paper marked "forthcoming Journal of Investment Management" (SSRN 3386035) |
| **Type** | Journal article (working-paper version), 26pp. 12-month time-series momentum on 156 assets and factors, January 1985 to December 2017 |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `babu2020trends` |
| **Status** | Reference: Table 2 (performance by group), Figure 1 (predictability regressions), Table 3 (alpha over passive volatility-scaled portfolios) carry the results |

## What it is

An out-of-sample test of time-series momentum in a new sense: not later dates, but assets
that the original studies never looked at.

- **Three groups of test assets.**
  - 58 *traditional* assets: the futures and forwards of Moskowitz, Ooi and Pedersen
    (2012), extended to 2017.
  - 82 *alternative* assets: 7 emerging-market equity index futures, 17 interest-rate
    swaps, 24 emerging-market currency pairs, 21 less-traded commodity futures, 5 credit
    default swap indices and 8 volatility futures. Start dates range from 1973 to 2008.
  - 16 long-short US equity *factors* (value, size, investment, profitability, beta and
    similar), built from top and bottom 30% of stocks in large and small caps.
- **Strategy.** The standard one: long if the past 12-month excess return is positive,
  short if negative, each position scaled to 40% ex ante volatility, monthly, equal
  weight within a group. Returns are **gross of transaction costs**.
- **Results (gross Sharpe ratios).** Traditional assets 1.17, alternative assets 1.34,
  equity factors 0.95, and all three combined 1.60. The median single-asset Sharpe ratio
  is positive in every group, and portfolio Sharpe ratios are well above the medians
  because the strategies are weakly correlated with each other.
- **Regression evidence.** Pooled regressions of volatility-scaled returns on the sign of
  the lagged return show positive t-statistics at lags of 1 to 12 months in all three
  groups, and mixed or negative ones beyond.
- **Not just volatility scaling or static bets.** Kim et al. (2016) and Huang et al.
  (2018) argued that time-series momentum profits come mainly from volatility scaling and
  from being long assets with high average returns. Regressing each trend strategy on a
  passive long-only portfolio built the same way (volatility-scaled, sign fixed at +1)
  leaves significant alpha across look-backs from 1 to 12 months and for the groups in
  aggregate (4 of 6 alternative asset classes individually).
- **Diversification.** Traditional-asset trend has a correlation of 0.30 with factor trend
  and 0.49 with alternative-asset trend, and low correlations with the S&P 500, MSCI World,
  the US Aggregate bond index and the GSCI. Quarterly returns against MSCI World show the
  "smile": best in strong bull and bear quarters, weakest in flat ones.

## Why it's in the library

**It is the broadest evidence that trend following is not a quirk of the original 58
futures.** Testing on assets nobody used to discover the effect is a cleaner
out-of-sample check than extending the dates, and the direct test against a matched
passive portfolio is a useful answer to the "it's just volatility scaling" critique.

**Caveats.**
- Results are gross of costs. Alternative assets and equity factors are more expensive to
  trade, which the authors acknowledge and address only by preferring the low-turnover
  12-month signal.
- Many alternative assets have short histories (some start in 2008), so "out of sample"
  here is about assets, not about time.
- The authors are at AQR, which manages trend-following funds.

## Links

- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the original study whose method
  and asset list this extends
- [[hutchinson-obrien-2014-is-this-time-different-trend-following-and-financial-crises]] —
  when the same strategy does poorly: the years after financial crises
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — long-history
  evidence on traditional markets, the complement to this cross-asset breadth
- [[roncalli-2017-keep-up-the-momentum]] — a theoretical account of the trend payoff,
  including why it looks like a long-volatility "smile"
