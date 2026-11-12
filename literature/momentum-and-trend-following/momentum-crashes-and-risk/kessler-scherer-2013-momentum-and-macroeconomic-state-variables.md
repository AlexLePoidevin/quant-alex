# Momentum and Macroeconomic State Variables

| | |
|---|---|
| **Authors** | Stephan Kessler (University of St. Gallen) and Bernd Scherer (FTC Capital) |
| **Year** | 2013 |
| **Type** | Journal article, *Financial Markets and Portfolio Management* 27(4), 335–363. Monthly excess returns on 22 asset-class indices (equities, bonds, commodities, currencies, REITs), January 1984 to April 2010 |
| **PDF** | Not hosted in this repository (Springer journal article, © Swiss Society for Financial Market Research) |
| **Find it** | [doi.org/10.1007/s11408-013-0215-8](https://doi.org/10.1007/s11408-013-0215-8) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Momentum+and+Macroeconomic+State+Variables%22+Kessler) |
| **BibTeX** | `kessler2013macro` |
| **Status** | Reference: Table 1 (strategy), Table 3 (expansions vs contractions), Table 5 (two-way sorts) and Table 6 (conditional factor model) carry the result |

## What it is

A test of whether momentum across asset classes is a reward for reacting to the business
cycle. The authors call it "macro momentum": each month, go long the asset classes whose
past return is above the cross-sectional median and short those below it. The book is
scaled to 1% volatility. This is cross-asset momentum on prices, not the
fundamentals-based "macro momentum" of AQR.

- **The strategy works.** Over 1984–2010 the 1-month signal has a Sharpe ratio of 0.79 and
  the 12-minus-1-month signal 0.86. The two correlate at only 0.24, and an equal mix earns
  0.98 (t = 5.2), against 0.38 for the S&P 500.
  - **Significance:** a block bootstrap rejects equal Sharpe ratios with the S&P 500 at
    p = 0.036.
  - **Robustness:** dropping equities leaves 0.95, and so does removing the volatility
    scaling. One-month momentum works here, unlike the one-month reversal in single stocks.
- **A macro forecasting alternative.** Rolling 60-month regressions on four lagged state
  variables (changes in default spread, term spread, dividend yield and T-bill rate)
  forecast each asset's return. A long/short book on those forecasts earns a Sharpe ratio
  of 0.42. Adding unemployment and producer confidence lifts it to 0.53. Both are well below
  momentum.
- **It earns its money in recessions.** Across three NBER contractions, the 1-month
  momentum earned 3.0% a year at 1% volatility, against 0.6% in expansions. The difference
  is 228bp a year and significant. The 12-1 signal shows no significant difference.
  - **What it holds:** in the 2000–01 and 2008 recessions it went long bonds and short
    equities, a safe-haven trade reached by a purely statistical rule.
- **The link to macro.** Two tests tie the strategy to the business cycle:
  - **Two-way sorts:** sorting first on the macro forecast and then on momentum cuts the
    momentum spread's Sharpe ratio from 1.06 to 0.53–0.61. Random first-stage sorts almost
    never cut it that much (7 of 10,000).
  - **Conditional factor model:** let the exposures to the Fung–Hsieh hedge-fund factors
    vary with the four state variables (Ferson–Schadt). The alpha falls from 1.57% a year
    (t = 7.4) to an insignificant 0.1%, and the explanatory power rises from an R² of 0.30
    to 0.41.

## Why it's in the library

**It reads momentum as a business-cycle hedge.** Cross-asset momentum does best when the
economy turns down, because asset classes reprice in opposite directions: equities fall,
bonds rally. That is the opposite of single-stock momentum, which tends to do worse after
market falls. It is a useful counterweight to the crash literature in this folder.

**It shows what "explaining away" alpha means.** Once exposures are allowed to move with
observable state variables, the alpha disappears. The authors' point is that this doesn't
make the strategy useless. It means momentum is a cheap, model-free way to get the
exposure a good macro forecasting model would give.

**Limits.** The data are Datastream index excess returns standing in for futures. The
universe is small, and Table 7 lists 22 assets although the text says 21. There are only
three recessions in the sample. Transaction-cost checks are described as robust but not
shown. The strategy lost money in the 2009–10 recovery, the momentum-crash period.

## Links

- [[brooks-2017-a-half-century-of-macro-momentum]] — AQR's macro momentum, built on trends in economic fundamentals rather than prices; a different strategy with the same name
- [[keller-keuning-2016-paa]] — a practitioner cross-asset momentum allocation that moves to bonds in bad markets
- [[liu-moench-2016-what-predicts-us-recessions]] — which state variables actually lead recessions, the predictors this paper conditions on
- [[butt-virk-2020-momentum-crashes-and-variations-to-market-liquidity]] — single-stock momentum after down markets, where the business-cycle sign is reversed
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — time-series trend across futures, which also earns most in the worst markets
