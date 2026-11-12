# Diversifying the What, How, and When of Trend Following

| | |
|---|---|
| **Authors** | Corey Hoffstein, Justin Sibears (Newfound Research) |
| **Year** | 2018 (commentary dated 2 April 2018) |
| **Type** | Practitioner commentary, 16pp. Backtests on Kenneth French US equity and sector data from 1927 and MSCI country indices from 1969; gross of all costs |
| **PDF** | Not hosted in this repository (Newfound Research, all rights reserved) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Diversifying+the+What%2C+How%2C+and+When+of+Trend+Following%22+Hoffstein) for the title and authors |
| **BibTeX** | `hoffstein2018diversifying` |
| **Status** | Reference: the three sections (what, how, when) and their charts are the whole piece |

## What it is

A short argument that a simple long/flat trend rule on US equities (hold the index when its
12-1 month return is positive, otherwise cash) carries risks that its long backtest hides,
and that each can be diversified away rather than optimised.

- **What you apply it to.** The same rule on six randomly chosen foreign markets (US-dollar
  returns, against a 50% equity / 50% cash benchmark) was much less consistent than on US
  equities. Running the rule on each US sector and averaging gives a result similar to the
  index rule but with more internal diversification.
- **How you measure the trend.** Moving-average crossovers, price-minus-moving-average,
  change in moving-average direction and time-series momentum are mathematically related
  (the piece cites Bruder et al., Levine and Pedersen, Zakamulin and others). Over rolling
  five-year windows, the gap between the best and worst of four such rules averaged 348bp a
  year (median 306bp), and no rule was consistently best: scored 1 (best) to 4 (worst) on each
  window's trailing returns, their long-run averages were 2.09, 2.67, 2.40 and 2.79. Lookback length matters just as much. From 8/1927 to 12/1934
  an 11-1 rule returned 136% while a 6-1 rule lost 25%; from 12/1951 to 12/1971 the 6-1 rule
  returned 723% against 361%.
- **When you rebalance.** Four copies of the same monthly rule, each trading in a different
  week of the month, turned $1 into anywhere from $4,139 to $6,797 since 1927. The fix is to
  hold all four ("tranching"), so the result does not depend on the rebalance date.

## Why it's in the library

It names three choices that every trend-following backtest makes and that are usually
treated as fixed: the asset, the signal and its lookback, and the rebalance date. The point
is that these are uncompensated risks. Choosing the historically best one is overfitting,
while spreading across them costs little.

- **The rebalance-date effect is large.** A gap of $4,139 against $6,797 from nothing but
  the trading week is the clearest illustration in the library of why monthly strategies
  should be tranched or phase-averaged before their results are trusted.
- **Limits.** It is marketing commentary from a firm selling tactical strategies. The
  backtests are gross of all costs, the foreign markets were chosen at random from those
  available, and nothing is tested statistically. Read it for the framework and the
  magnitudes, not as proof.

## Links

- [[baltas-kosowski-2017-demystifying-time-series-momentum-strategies]] — a formal test of how the trend rule and volatility estimate change turnover and returns
- [[rattray-et-al-2020-strategic-rebalancing]] — rebalancing choices and trend overlays in a 60/40 portfolio
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — moving-average rules derived as optimal in a bull/bear model
- [[keller-keuning-2018-daa]] — a momentum-based tactical allocation rule of the kind these risks apply to
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — choosing rule parameters from a model rather than by searching backtests
