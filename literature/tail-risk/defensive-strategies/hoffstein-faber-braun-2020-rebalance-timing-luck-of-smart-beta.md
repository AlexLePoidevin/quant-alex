# Rebalance Timing Luck: The (Dumb) Luck of Smart Beta

| | |
|---|---|
| **Authors** | Corey Hoffstein, Nathan Faber, Steven Braun (Newfound Research) |
| **Year** | 2020 (February; SSRN 3673910) |
| **Type** | Practitioner working paper, 22pp. S&P 500 universe, Sharadar data, July 2000 – September 2019, gross of all costs |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `hoffstein2020timingluck` |
| **Status** | Reference: Exhibit 1 (timing luck by style, size and frequency), Exhibit 3 (momentum sub-indexes) and the S&P index replications carry the results |

## What it is

A measurement of how much a factor portfolio's results depend on nothing more than the
calendar months in which it happens to rebalance.

- **Definition.** Two portfolios built by exactly the same rules but rebalanced on
  different dates (say every January and July versus every April and October) drift
  apart. The authors call the spread *rebalance timing luck* (RTL). They measure it as the
  annualised volatility of each version's returns against an equal-weighted blend of all
  versions, the "overlapping" or tranched portfolio.
- **What drives it.** From the authors' earlier paper (Hoffstein, Sibears and Faber 2019),
  RTL ≈ (turnover × rebalance interval / 2) × S, where S is the volatility of the gap
  between what the portfolio holds and what it could hold. Faster signals, fewer holdings
  and less frequent rebalancing all raise it.
- **Size of the effect.** Long-only equal-weighted S&P 500 portfolios on value (earnings
  yield), momentum (12-1 month return), quality (ROE, accruals, leverage) and low
  volatility. For 100 stocks rebalanced semi-annually, RTL is 2.5% (value), 4.4%
  (momentum), 2.0% (quality) and 1.1% (low volatility) a year. With 50 stocks rebalanced
  annually, momentum's RTL is 7.4%. Treating two versions as independent, the gap between
  them has volatility √2 × RTL, so two "identical" 100-stock momentum funds could differ by
  about ±12 points in a year at 95% confidence.
- **No schedule is better.** For the semi-annual 100-stock momentum strategy the six
  versions return between 6.1% and 7.9% a year, with tracking error to the blend of 2.9–4.6%.
  None of the pairwise long–short differences is statistically significant, so the luck is
  uncompensated risk rather than a timing edge. Shifting the schedule by one month produced
  a 20-point gap over one 252-day window.
- **Real index rules.** Replicating the S&P 500 Enhanced Value, Momentum, Quality and Low
  Volatility index methodologies, the best and worst schedules differ by 100, 192, 106
  and 25 basis points a year. In 2009 the Enhanced Value replication rebalanced in
  January/July beat the June/December version by 41.7 points. No schedule wins across
  styles, and dispersion rises in volatile years (2002, 2009).

## Why it's in the library

**It puts a number on a source of noise that most backtests ignore.** A single backtest
with one rebalance date reports one draw from a distribution of possible results. For
concentrated, high-turnover strategies that distribution is wide enough to swamp the
differences people usually argue about.

**The fix is cheap.** Splitting the portfolio into tranches rebalanced on staggered dates
removes the luck without changing the strategy. That matters both for running money and
for judging managers and benchmarks, which can carry hundreds of basis points of timing
luck themselves.

**Limits.** One universe, one data vendor, a 19-year sample and gross returns. The ±12
point range assumes the versions' deviations are independent, which they are not quite.
The conclusion also quotes a ±1.5% range for low-turnover strategies, while the body's
own figures imply about ±3% for low volatility; the body figures are the ones to use.

## Links

- [[hong-meyer-brauns-2021-portfolio-rebalancing-tradeoffs-and-decisions]] — rebalancing rules for a fixed-weight portfolio, compared on cost and tracking error
- [[granger-et-al-2014-rebalancing-risk]] — the option-like payoff of fixed-weight rebalancing
- [[arnott-et-al-2019-alices-adventures-in-factorland]] — other reasons factor backtests overstate what investors get
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — the wider problem of reading too much into a single backtest path
