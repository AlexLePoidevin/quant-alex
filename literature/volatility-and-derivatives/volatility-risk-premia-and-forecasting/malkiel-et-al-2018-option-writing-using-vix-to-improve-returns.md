# Option Writing: Using VIX to Improve Returns

| | |
|---|---|
| **Authors** | Burton G. Malkiel (Princeton), Alex Rinaudo and Atanu Saha (Data Science Partners) |
| **Year** | 2018 (*Journal of Derivatives* 26(2), 38–49) |
| **Type** | Empirical paper, 12pp. VIX and S&P 500, 1990–June 2018; Cboe BXM and PUT indexes, with the strategy tested from 1995 |
| **PDF** | Local copy only (journal download, © Institutional Investor LLC) |
| **BibTeX** | `malkiel2018optionwriting` |
| **Status** | Reference: Exhibits 2 (VIX overstatement by quartile), 5–7 (conditional strategy) and 10 (random-period check) carry the results |

## What it is

A simple rule for when to sell options. Option writing earns the volatility risk premium:
implied volatility, here the VIX, is usually higher than the volatility that follows. The
paper's point is that the premium is larger when the VIX is high.

- **VIX overstates future volatility, more so when it is high.** Over 1990–June 2018 the VIX
  exceeds the next 21 days' realised volatility by about 4.1 points on average: 2.9 points in
  the lowest VIX quartile and 5.3 in the highest. Relative to the average gap, the VIX
  *understates* forward volatility in the two lower quartiles and overstates it in the two
  upper ones.
- **So option-selling indexes beat the market only in high-VIX months.** Excess returns of the
  Cboe buy-write (BXM) and put-write (PUT) indexes over the S&P 500 total return, 1995–2018:
  −4.1% and −4.3% a year in the lowest quartile, −6.4% and −4.8% in the second, +0.4% and
  +3.3% in the third, +1.6% and +2.4% in the highest. The quartile cut-offs use only past data.
- **The conditional rule.** Each month, hold the S&P 500 if last month's median VIX is below
  its historical median; otherwise switch to the buy-write or put-write index. Over
  1995–June 2018 (annualised average monthly log returns):

  | | S&P 500 | BXM | PUT | Conditional BXM | Conditional PUT |
  |---|---|---|---|---|---|
  | Return | 9.49% | 7.64% | 8.67% | 10.09% | 10.88% |
  | Volatility | 14.63% | 10.59% | 10.40% | 11.58% | 11.36% |
  | Sharpe | 0.49 | 0.50 | 0.61 | 0.67 | 0.75 |
  | Sortino | 0.71 | 0.69 | 0.81 | 0.95 | 1.05 |

- **Where the gain comes from.** By year, the rule stays fully in the S&P in 7 of the 23.5
  years, beats it in 7 (on average by about 9.7 points) and lags it in 9 (by about 3.8
  points). The wins are concentrated in 2000–02 and 2007–09: in 2008 the S&P lost 46.2% (log
  return) against 33.8% and 31.2% for the conditional strategies. The losing years are bull
  markets with elevated volatility, notably the late 1990s.
- **Robustness.** In 10,000 random sub-periods of at least 12 months, the conditional
  strategies beat the S&P 500 and the unconditional indexes on return, Sharpe and Sortino in
  76–95% of cases. The same rule also improves four Cboe buy-write variants.

## Why it's in the library

It is a clean, documented example of the variance risk premium being state-dependent, and of
a way to exploit that with only index data and one switch per month. The quartile table is
useful on its own: selling options when the VIX is low has historically cost money against
just holding equities.

Limits worth keeping in mind:

- The outperformance rests on two bear markets (2000–02 and 2008). Most of the Sharpe gain
  comes from being partly hedged when the market fell, not from harvesting more premium.
- Results use Cboe index returns with no trading costs, and the rule switches between the
  index and the option strategy many times.
- The random-period check reuses overlapping windows of the same history, so it is not an
  independent test.
- The authors include a commercial firm, and the closing suggestion to apply the idea to
  emerging markets cites one fund without data.

## Links

- [[carr-wu-2009-variance-risk-premia]] — measuring the variance risk premium that option
  writing collects
- [[carr-wu-2016-analyzing-volatility-risk-and-risk-premium-in-option-contracts]] — how the
  volatility risk premium varies over time and what it predicts
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  other side of the trade: what buying volatility does to a portfolio, 2006–2017
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]] —
  why systematic option buying bleeds, the cost that option writers are paid
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — VIX regimes modelled formally, a
  more careful version of the high/low split used here
