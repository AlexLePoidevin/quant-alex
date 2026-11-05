# Applied Machine Learning for Systematic Equities Trading: Trend Detection, Portfolio Construction and Order Execution

| | |
|---|---|
| **Authors** | Mininder Sethi (supervised by Philip Treleaven, University College London) |
| **Year** | 2016 |
| **Type** | PhD thesis, Department of Computer Science, University College London, 153pp. Parts were published at IEEE CSCI 2014, IJCNN 2014 and IJCNN 2015 |
| **PDF** | Local copy only (thesis with no licence statement) |
| **BibTeX** | `sethi2016applied` |
| **Status** | Reference: Ch. 3 (trend detection, Tables 3.1, 3.7, 3.10–3.11), Ch. 4 (portfolio construction, Table 4.2) and Ch. 5 (order timing) carry the results; Ch. 2 is a literature review |

## What it is

A practitioner's PhD that builds the three pieces of a short-horizon US equity strategy
with machine learning: when to trade a stock, how to weight the stocks that signal, and
when in the day to send the orders.

- **Trend detection with two features.** For each stock, a "short-term efficiency level"
  (Kaufman's efficiency ratio: net price change over 10 days divided by the sum of absolute
  daily changes, so 1 is a straight line and 0 is no net move) and its 20-day average. A
  trade either follows the recent 10-day direction (where the stock's history shows
  momentum under those conditions) or bets against it (where it shows overreaction), held
  for at most a few days; most of the time the stock is left alone.
  - *Without ML*: regions fitted on 2003–2010 for 20 Dow stocks and applied to 2010–2013
    left an average stock up 4.4% over three years, in a trade 13% of days.
  - *With a radial basis function network*: trained per stock on the two features, with
    trade outcomes binned into nine categories so outliers have their own class, "zero
    appending" (artificial no-trade points that keep the network out of empty regions of
    feature space) and output smoothing. On 100 stocks retrained yearly from 2006 to 2013,
    53–58% of trades were profitable, at −0.03% to +0.71% per trade depending on the year.
  - *Tuned*: parameters set by simulated annealing on the 2007–08 year, then linked to
    each stock's realised volatility. With 4bp costs per trade, the average per-stock
    "annualised information ratio" over 2008–2013 was 1.36, against 0.63 for the S&P 500;
    a second, disjoint set of 100 stocks gave similar figures (0.74–2.12 by year).
- **Portfolio construction.** Mean-variance needs correlations between stocks that rarely
  signal on the same day, so the thesis uses a Markov chain over the stocks signalling a
  buy, adapted from Google's PageRank: money moves between neighbouring stocks through
  equal-weighted "bridge portfolios", with transition scores from the historical probability
  of beating a return threshold, and the long-run distribution gives the weights. A genetic
  algorithm chooses the chain order that uses the most data. In 1,024 random universes
  drawn from the May 2006 S&P 500, $100 invested from 2006 to 2013 grew on average to $399
  with the optimised chain against $369 equal-weighted (100-stock universes), and to $675
  against $575 (400-stock universes).
- **Order timing.** Two "experts" predict the next move in the best bid (continue the last
  tick, or reverse it), combined by follow-the-leader or weighted-majority online learning.
  Tested on 15-second best-bid samples for 32 stocks on a single day (29 April 2016), the
  reversing expert is usually preferred: the bid tends to tick up and down.

## Why it's in the library

**The efficiency ratio is a useful trend feature.** Measuring trend strength as net move
over total path, and conditioning on whether the short-term and average trend agree, is a
compact way to separate momentum-like from reversal-like conditions in a single stock. The
point that a model should be allowed to say "no trade" most of the time is also sound.

**It treats the full pipeline, including the parts papers skip.** Weighting stocks with
sparse overlapping signals, and the timing of execution within the day, are real problems;
the thesis at least frames them.

**The evidence is much weaker than the conclusions.** The trend-detection universe is
the 2013 S&P 500 members with ten years of history, so it has survivorship bias. The headline
"information ratio" is an average over single stocks, annualised by days in trade on the
assumption that capital could always be redeployed into another equally good trade; it is
not the ratio of any implementable portfolio, and comparing it with the S&P 500's ratio is
not like for like. The portfolio tests are long-only over a period that includes the
2009–2013 recovery, report terminal wealth with no volatility, drawdown or cost figures,
and include the 2007–08 year on which the signals were tuned. The execution study is one
day. Read it as a source of ideas (the efficiency-ratio features, the no-trade class), not
as evidence that the strategy works.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a model
  in which the optimal trend rule and its lookback can be derived rather than tuned
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — evidence on short-term
  reversals in large US stocks, the "overreaction" side of the thesis's signal
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  choosing profit-taking and stop-loss levels from a fitted model instead of a backtest
  search
- [[harvey-liu-zhu-2016]] — the multiple-testing problem behind tuning many parameters on
  one sample
- [[markowitz-1952]] — the mean-variance framework Ch. 4 argues is unsuited to short,
  sparse holdings
