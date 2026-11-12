# Three Quant Lessons from COVID-19

| | |
|---|---|
| **Authors** | Alex Lipton (Hebrew University; MIT) and Marcos López de Prado (Cornell; Lawrence Berkeley National Laboratory) |
| **Year** | 2020 (30 April) |
| **Type** | Short essay, SSRN 3580185, 6pp (figures not reproduced in this copy) |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3580185](https://doi.org/10.2139/ssrn.3580185) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Three+Quant+Lessons+from+COVID-19%22+Lipton) |
| **BibTeX** | `lipton2020covid` |
| **Status** | Reference: read in full; short |

## What it is

A brief opinion piece written during the COVID-19 selloff, when the S&P 500 had fallen 35%
from its 19 February 2020 peak and many quant funds, including market-neutral ones, had lost
money. It draws three lessons.

1. **More nowcasting, less forecasting.** Instead of long-range predictions from structured
   data, use real-time unstructured data (web-scraped prices for inflation, satellite images
   of car parks for retail sales) to estimate the present. The authors compare it with
   earthquake early-warning systems and argue that supply-chain disruption in China gave
   warning days before the selloff, so it was "a Black Swan to market forecasters" but
   predictable to nowcasters.
2. **Develop theories, not trading rules.** Running thousands of backtests and reporting the
   best one makes most published findings false. Backtests should validate a cause-and-effect
   theory, not generate one. Their example: test whether persistent order-flow imbalance
   precedes panic selling, as in the 2010 flash crash, by looking at which market makers lost
   money and whether they withdrew.
3. **Avoid all-weather strategies.** There is little reason to expect any source of returns
   to work in every regime. Instead, build strategies for well-defined regimes, nowcast the
   probability that the market is in each, and blend the strategies by those probabilities.

## Why it's in the library

It is a compact statement of three positions López de Prado develops at length elsewhere:
backtest overfitting, the case for theory-driven research, and regime-dependent portfolios.
The regime point is the one most relevant to bear markets: a strategy built to survive every
regime gives up the edge it could have in any one of them.

It is an essay, not evidence. The claim that the selloff was predictable to nowcasters is
asserted with hindsight and not tested, and the regime-ensemble approach depends on
identifying regimes in real time, which the note does not show how to do.

## Links

- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — the
  "rules from a model, not from a backtest search" idea worked out
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — the order-flow-toxicity account
  of the flash crash that the second lesson points to
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a model of market
  regimes that can be estimated in real time
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a trading
  rule derived for a two-regime market
- [[kakushadze-2020-quant-bust-2020]] — the mechanism behind the 2020 quant drawdowns: why mean-reversion statistical arbitrage breaks in a liquidation
