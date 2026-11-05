# Global Equity Momentum: A Craftsman's Perspective

| | |
|---|---|
| **Authors** | ReSolve Asset Management (no individual authors named) |
| **Year** | 2019 (PDF dated April 2019; data to September 2018) |
| **Type** | Practitioner white paper, 39pp. Monthly backtests 1950–September 2018, all marked hypothetical and gross of costs |
| **PDF** | Local copy only (manager white paper, no licence) |
| **BibTeX** | `resolve2019gem` |
| **Status** | Reference: the bootstrap test (pp. 12–15), the in- vs out-of-sample check (pp. 16–18) and Table 1 carry the argument |

## What it is

A robustness study of Gary Antonacci's Global Equity Momentum (GEM), the "dual momentum"
rule: each month, if the S&P 500's 12-month return beats cash, hold whichever of US or
foreign equities had the higher 12-month return; otherwise hold bonds. ReSolve replicates
the original (15.2% a year, Sharpe 0.93, maximum drawdown −19.1%, against 15.8%, 0.95 and
−17.8% as reported) and then asks whether the 12 × 12-month choice is special.

- **1,225 variants.** Trend and relative-momentum lookbacks of 1–18 months, a
  moving-average version (2–18 months), and two switch rules (S&P 500 alone, or US and
  foreign equities both in downtrend).
- **Specification risk is large.** Over 2009–2018 a 10-month GEM returned 146% and a
  9-month GEM 43%. Across all specifications there is a 5% chance of trailing another
  specification by 64 percentage points over five years.
- **No variant is better than another.** Block bootstraps (15,000 samples per variant) put
  the original ahead of the average variant by only 0.8% a year, ahead in about 61% of
  samples, and even against the worst variant only 93% of the time, short of 95%.
- **In-sample flattery shows up.** On the original paper's 1974–2011 window the 12 × 12
  rule sits near the top of the distribution; on the out-of-sample years (1950–73 and
  2012–18) it returns 13.14% against a median of 12.92%, the 58th percentile.
- **The ensemble.** Averaging the holdings of all variants each month gives about the
  same return as the median variant (14.2% vs 14.1%) with a better Sharpe ratio (0.93 vs
  0.83), shallower average worst-five drawdowns (−13.2% vs −17.4%), a better worst decade
  (+90% vs +72%) and a better worst-five-year average. Synthetic indexes built from random
  country and style portfolios give the same picture.
- **Taxes.** The ensemble trades far more (1,867 trades vs 105) and realises more
  short-term gains; a trade filter is said to remove most of the extra tax drag.

## Why it's in the library

It is the clearest worked example of parameter risk in a simple momentum rule: a lookback
that looks optimal in-sample regressed to the median as soon as new data arrived, and
neighbouring lookbacks gave very different decade-long outcomes. The remedy, averaging
across many equally justified specifications rather than picking one, is the same idea as
an ensemble of models, and it improves the path (drawdowns, worst decade) more than the
average return.

It is a manager's paper and every figure is a gross-of-cost backtest on index data. The
statistical test is honest about failing to separate the variants, but the case for the
ensemble rests on the same 1950–2018 history.

## Links

- [[keller-keuning-2016-paa]] — another rules-based momentum allocation in the same
  family, with its own choice of lookbacks
- [[keller-keuning-2018-daa]] — dual momentum with a "canary" crash-protection signal
- [[harvey-liu-zhu-2016]] — why the best of many tested specifications overstates what
  any one will earn
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  choosing rule parameters without searching over backtests
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — trend across
  lookbacks of 1–12 months, where the shorter ones did the crisis work
- [[geczy-samonov-2017-two-centuries-of-multi-asset-momentum]] — country equity momentum back to 1800, the largest spread of any asset class there
