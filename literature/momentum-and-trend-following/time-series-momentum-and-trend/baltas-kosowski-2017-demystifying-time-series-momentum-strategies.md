# Demystifying Time-Series Momentum Strategies: Volatility Estimators, Trading Rules and Pairwise Correlations

| | |
|---|---|
| **Authors** | Nick Baltas (UBS; Imperial College); Robert Kosowski (Imperial College; Oxford-Man Institute) |
| **Year** | 2017 (book chapter); the copy is the working paper dated 1 October 2015, earlier circulated as "Improving Time-Series Momentum Strategies" (SSRN 2140091) |
| **Type** | Book chapter, ch. 3 in *Market Momentum: Theory and Practice*, ed. S. Satchell and A. Grant (Wiley), pp. 30–67. Doi 10.1002/9781119599364.ch3. 75 futures contracts, December 1974 to February 2013 |
| **PDF** | Not hosted in this repository (SSRN working paper; no open licence) |
| **Find it** | [doi.org/10.1002/9781119599364.ch3](https://doi.org/10.1002/9781119599364.ch3) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Demystifying+Time-Series+Momentum+Strategies%3A+Volatility+Estimators%2C+Trading+Rules+and+Pairwise+Correlations%22+Baltas) |
| **BibTeX** | `baltas2017demystifying` |
| **Status** | Reference: Tables II–III (volatility estimator and trading rule), §5 (correlation adjustment) and Table V (after costs) |

## What it is

A study of three design choices inside a standard time-series momentum (trend-following)
portfolio: go long or short each futures contract on the sign of its past twelve-month return,
and scale each position to a volatility target. The authors ask what each choice does to
turnover and to returns after costs.

- **The volatility estimator.** Replacing close-to-close standard deviation with the
  Yang–Zhang range estimator (using open, high, low and close) cuts turnover by about a
  tenth (8% for the trend portfolio), with no change in the before-cost Sharpe ratio (about
  0.82). A hypothetical "perfect forecast" of next month's volatility would raise the Sharpe
  ratio to 1.30, which shows how much better volatility forecasts could matter.
- **The trading rule.** A rule that only takes a position when the twelve-month price trend
  is statistically significant (Newey–West t-statistic beyond ±2), and otherwise stays flat,
  has the same Sharpe ratio as the sign rule (0.99 against 1.04, not significantly different)
  with about one third of the turnover. The cut is 55–85% across individual contracts.
- **Correlations.** The strategy's weak 2009–2013 period lines up with a rise in average
  pairwise correlation across futures, which shrinks the diversification the volatility
  target assumes. A correlation factor that reduces leverage when average correlation is
  high doubles the post-crisis Sharpe ratio, from 0.14 to 0.29, at the cost of 40–50% more
  trading.
- **After costs.** With trading costs modelled as turnover times a constant market impact of
  10bp or 50bp, the turnover savings from the first two changes barely raise the
  after-cost Sharpe ratio. The correlation adjustment survives costs: 0.12 against 0.26 at
  10bp, and 0.05 against 0.14 at 50bp, for 2009–2013.

## Why it's in the library

It takes apart the standard trend-following recipe into its pieces and measures each one,
which most papers on the topic do not:

- **Turnover and Sharpe ratio are separate questions.** Big turnover cuts did not translate
  into better after-cost results under the cost model used. The authors say that model is
  crude (constant impact, proportional to turnover), so the conclusion is provisional.
- **Correlation is the hidden input.** Volatility targeting per asset assumes the assets
  diversify each other; when correlations rise, the portfolio is levered into one bet. The
  correlation adjustment is a simple fix for that.
- **Caveat on the post-crisis result.** The headline improvement is measured over five years
  (2009–2013) and the correlation factor was motivated by looking at that same period, so it
  is suggestive rather than out-of-sample evidence.

## Links

- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the same kind of futures trend strategy, measured over 1960–2015 and in crises
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — what volatility targeting does to Sharpe ratios and tails across asset classes
- [[molyboga-swedroe-qian-2020-short-term-trend-a-jewel-hidden-in-daily-returns]] — faster trend signals on a similar futures universe, also judged after costs
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a model in which a trend rule is optimal
- [[hoffstein-sibears-2018-diversifying-the-what-how-and-when-of-trend-following]] — diversifying trend signals, lookbacks and rebalance dates instead of picking one
