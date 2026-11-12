# Two Centuries of Multi-Asset Momentum (Equities, Bonds, Currencies, Commodities, Sectors and Stocks)

| | |
|---|---|
| **Authors** | Christopher C. Geczy (Wharton) and Mikhail Samonov (Forefront Analytics; Wharton) |
| **Year** | 2017 (version of 15 January 2017; first posted to SSRN in 2015 as 2607730) |
| **Type** | Working paper, 77pp. Cross-sectional momentum in six asset classes and across them, monthly, 1800–2014 |
| **PDF** | Not hosted in this repository (SSRN working paper, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.2607730](https://doi.org/10.2139/ssrn.2607730) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Two+Centuries+of+Multi-Asset+Momentum+%28Equities%2C+Bonds%2C+Currencies%2C+Commodities%2C+Sectors+and+Stocks%29%22+Geczy) |
| **BibTeX** | `geczy2017multiasset` |
| **Status** | Reference: Table II (spreads by asset class), §III.E (commodity spot mean reversion), §IV (correlations and dynamic betas), §VI.A (trend versus momentum) carry the results |

## What it is

The longest test of cross-sectional momentum across asset classes: buy the third of
assets with the best past 10 months (skipping the latest two months), sell the worst
third, equal weight, rebalance monthly.

- **Data.** Global Financial Data back to 1798, plus Bloomberg and CRSP: 47 country equity
  indices, 48 currencies, 43 government bond indices, 76 commodities (spot prices), 301
  country sectors in 33 countries, and 34,006 US stocks. The authors say early index
  quality is weaker than modern data.
- **Spreads, 1800–2014 (winners minus losers, per month).**
  - Country equities 0.88% (t = 10.6); currencies 0.51% (t = 9.6); US stocks 0.51%
    (t = 6.0); country-neutral sectors 0.36% (t = 6.6); government bonds 0.13% (t = 2.3).
  - Across asset classes (equities, bonds, currencies, commodities): 0.45% (t = 10.2).
  - An equal-weight combination of all seven: 0.45% a month (t = 15.4) in price terms,
    similar in size to the global equity premium over the same period (about 0.5%).
- **Commodity spot prices mean-revert.** Using spot prices (futures only exist from 1959),
  commodity momentum is significantly *negative*: −0.46% a month since 1800, −0.57% since
  1531. The reversal disappears after 1959 for the 46 commodities that have futures
  (−0.07% a month) but persists for the 30 without futures (−0.82%). The authors read this
  as possible evidence that futures trading removes spot mean reversion. Removing
  seasonality does not explain it.
- **Long bad stretches.** The combined strategy has negative rolling 10-year returns in the
  1820s, 1850s and 1860s. Country equity momentum was negative over rolling 10-year
  windows for the whole of 1840–1872 (only five countries had data). Currency momentum
  returns cluster in a few turbulent decades (1920s, 1940s, 1980s).
- **Dynamic beta.** Momentum portfolios load on whatever the asset class has been doing:
  equity momentum's beta is 0.63 in up markets and −0.56 in down markets, and the longer a
  market state lasts, the larger the beta in its direction. That is the setup for a crash
  when the market turns.
- **Rising correlations.** The average rolling five-year correlation between the seven
  momentum strategies is 9% over the full history but reached an all-time high of 41% in
  May 2014, up from a previous peak of 22% in 1934. The authors flag crowding.
- **Trend versus momentum.** A trend version using the same 10-month signal (winners are
  assets with a positive return, losers negative) earns 0.38% a month (t = 14.5) against
  momentum's 0.45%, with a 0.76 correlation between them.
- **Other findings.** No short-term reversal at the asset level (only US stocks reverse at
  one and two months); long-term reversal after about 10 months in all classes; some
  momentum in the momentum strategies themselves; and country bond momentum predicting
  country equity returns (0.59% a month since 1846).

## Why it's in the library

**It is the long-run stress test for momentum as a multi-asset premium.** Two centuries of
data show the effect in every asset class, but also decade-long losing stretches that a
post-1950 sample would hide, beta that swings with the market state, and correlations
between momentum strategies that had risen to record levels by 2014. Those last two are
the practical risks for anyone combining momentum across assets.

**Caveats.** Pre-1900 data are thin (a handful of countries in some decades) and of
uneven quality; spreads are before trading costs and before any feasibility constraint
(the authors note multi-asset investing was not possible for most of the sample); and the
commodity results use spot prices, which are not tradable returns.

## Links

- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the time-series version of
  momentum that §VI.A compares against
- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — momentum and long-run
  reversal as time-varying exposures, consistent with the dynamic betas documented here
- [[butt-virk-2020-momentum-crashes-and-variations-to-market-liquidity]] — when momentum
  crashes, the risk that the up/down-market beta swing creates
- [[resolve-2019-global-equity-momentum-a-craftsmans-perspective]] — a practitioner's
  equity-index momentum design, the asset class with the largest spread here
- [[brooks-2017-a-half-century-of-macro-momentum]] — momentum in economic fundamentals
  rather than prices, over a shorter multi-asset sample
