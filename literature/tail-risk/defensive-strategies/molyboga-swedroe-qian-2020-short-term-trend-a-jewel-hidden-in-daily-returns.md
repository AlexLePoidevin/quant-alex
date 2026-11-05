# Short-Term Trend: A Jewel Hidden in Daily Returns

| | |
|---|---|
| **Authors** | Marat Molyboga (Efficient Capital Management), Larry Swedroe (Buckingham), Junkai Qian (Illinois Institute of Technology; Efficient Capital) |
| **Year** | 2020 |
| **Type** | Journal article, *The Journal of Portfolio Management* 47(1), 154–167 (doi 10.3905/jpm.2020.1.186). The copy is the authors' review draft from ResearchGate, 15pp. Daily returns on 78 futures markets, 1984/85–2017 |
| **PDF** | Local copy only (author draft of a JPM article, no open licence) |
| **BibTeX** | `molyboga2020shortterm` |
| **Status** | Reference: the introduction states every headline number; the portfolio and transaction-cost section is the one that matters |

## What it is

A study of time-series momentum (trend following) in futures built from daily rather than
monthly data. Each strategy goes long a market whose return over a lookback window is
positive and short one whose return is negative, with each position scaled to a 40%
volatility target as in Moskowitz, Ooi and Pedersen (2012). The data cover 28 commodity, 20
equity, 19 fixed-income and 11 currency futures.

- **Daily versions of the standard strategies.** Lookbacks of 252, 63 and 21 trading days,
  each held for 21 days (written 252-21, 63-21, 21-21), behave much like the familiar 12-, 3-
  and 1-month monthly strategies. The exception is equities, where the daily 252-21 strategy
  has a Sharpe ratio of 0.60 against 0.80 for the monthly one. The authors trace the gap to a
  few intramonth events such as October 1987. Volatility scaling lifts each asset class's
  Sharpe ratio by at least 0.23. A one-day delay between signal and trade costs little.
- **A short-term strategy.** A 21-day lookback held for five days (21-5, rebalanced weekly),
  which monthly data cannot reproduce. Its correlations with the other three run from 0.21
  (with 252-21) to 0.61 (with 21-21).
- **Adding it to a trend portfolio, before costs.** An equal-weight mix of 252-21, 63-21 and
  21-21 (the Hurst, Ooi and Pedersen 2017 portfolio) has a Sharpe ratio of 1.10. Replacing
  21-21 with 21-5, or splitting its weight between the two, gives 1.28 or 1.21.
- **After costs.** With Hurst, Ooi and Pedersen's conservative cost estimates the short-term
  sleeve adds nothing. With costs at half that level, net Sharpe rises from 0.92 to
  0.98–1.01, significant at the 10% and 5% levels. Commodities are dropped from the
  short-term sleeve because they trade less electronically; this barely changes the results.
- **Why it helps.** The authors separate two explanations: trading more often, and holding a
  different signal. Faster rebalancing helps before costs but not after. The short-term
  strategy, by contrast, tends to make money in the worst periods for 12-month trend, so its
  value is diversification.

## Why it's in the library

Slow trend following is valued as crisis protection, but it is slowest exactly when a market
turns, and its worst periods are reversals. This paper shows that a faster trend signal
partly fills that gap, and it is honest that the benefit survives only if execution is good:
at the conservative cost assumption it disappears, and the case rests on assuming costs half
as large because large managers execute well.

Points to keep in mind. The authors are practitioners at a managed-futures allocator, the
cost assumption is the hinge of the conclusion, and the paper's own abstract (1985) and data
section (1984) give different start years. The equity result also shows that a daily
strategy's performance can hinge on a handful of days.

## Links

- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the trend
  window derived from a bull/bear model rather than chosen by backtest
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  setting a trading rule's parameters without searching over backtests
- [[keller-keuning-2016-paa]] — a momentum rule applied to asset allocation with a crash
  filter
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bear rallies and bull
  corrections, the short reversals that whipsaw slow trend signals
- [[babu-et-al-2020-you-cant-always-trend-when-you-want]] — decomposing trend performance into market moves, efficacy and diversification
