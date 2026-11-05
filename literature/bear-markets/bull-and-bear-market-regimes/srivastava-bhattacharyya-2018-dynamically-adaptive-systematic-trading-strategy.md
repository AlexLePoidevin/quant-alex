# Evaluating the Building Blocks of a Dynamically Adaptive Systematic Trading Strategy

| | |
|---|---|
| **Authors** | Sonam Srivastava, with Ritabrata Bhattacharyya as mentor (WorldQuant University) |
| **Year** | 2018 |
| **Type** | MSc capstone paper (WorldQuant University, MSc in Financial Engineering). arXiv:1812.02527 (December 2018); SSRN 3144169 |
| **PDF** | `srivastava-bhattacharyya-2018-dynamically-adaptive-systematic-trading-strategy.pdf`: the arXiv copy (arXiv non-exclusive distribution licence), identical to the SSRN download |
| **BibTeX** | `srivastava2018adaptive` |
| **Status** | Reference: Table 3 (regime return statistics), Tables 4–5 (asset and sector returns by regime) and Tables 6–10 (backtests) carry the results |

## What it is

A student project that splits the S&P 500 from 2000 to 2017 into four regimes, matches a
trading rule to each, and combines them into one switching strategy.

- **Regimes.** A two-state Markov-switching model with switching variance (after Kim, 1991)
  gives low- and high-variance states. A 250-day triangular moving average, with a one-ATR
  Keltner band to stop whipsaws, then labels each state bullish or bearish. That gives four
  regimes, mapped loosely onto Wyckoff's market cycle: bullish low variance (advance),
  bearish high variance (decline), bullish high variance (accumulation) and bearish low
  variance (distribution).
- **Regime statistics.** Mean daily S&P returns are −0.041% in the bearish high-variance
  regime (2,011 days), 0.011% bearish low variance (564 days), 0.085% bullish high variance
  (363 days) and 0.039% bullish low variance (3,649 days). Regimes last 77 days on average,
  with a median of 15.
- **Assets and sectors.** Equity indices rise in bullish regimes and fall in bearish ones;
  gold and Treasuries are flat to positive in both; oil is inconsistent. Correlations across
  assets and sectors are higher in high-variance regimes.
- **Rules per regime.** Bollinger bands, RSI, Fibonacci retracement levels, MACD and a
  10-day EMA, combined into long pullback-buying rules for the bullish regimes and short
  rally-selling rules for the bearish ones, with ATR-based profit targets and stops. The
  paper says the exact thresholds were chosen by trial for the best fit in each regime.
- **Backtests.** With 3 bps of costs per trade, the four single rules run over the whole
  period give CAGRs of 6.6%, 6.3%, 0.9% and 1.9%, Sharpe ratios of 0.29, 0.29, 0.05 and
  0.12, and drawdowns of 38–58%. The switching strategy gives a 12.5% CAGR, Sharpe 0.69 and
  a 22% maximum drawdown.

## Why it's in the library

- **A clear map of how a regime overlay is put together.** Volatility states plus a trend
  filter, then different rules per state, is a common structure. This paper lays out each
  step and the regime-by-regime statistics.
- **Why its results should not be trusted as stated.** The regimes come from the
  full-sample smoothed probabilities, so the switching strategy knows each day's regime with
  hindsight. The trading thresholds were tuned on the same 2000–2017 data, and there is no
  out-of-sample period. The Sharpe ratio of 0.69 is what an in-sample fit with look-ahead
  produces, not evidence that the approach works.
- **What is still useful.** The descriptive results, such as higher cross-asset
  correlation in high-variance regimes and gold's behaviour in bear regimes, do not depend
  on the trading rules.

## Links

- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — the
  Markov-switching bull/bear model with volatility as the separating feature, and the same
  warning about full-sample smoothed states
- [[botte-bao-2021-a-machine-learning-approach-to-regime-modeling]] — a more careful regime
  model built for asset allocation
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a trend rule
  derived from a two-state model rather than fitted by trial
- [[harvey-liu-zhu-2016]] — why rules tuned on the same data they are tested on overstate
  performance
- [[keller-keuning-2016-paa]] — a rule-based allocation that switches to safe assets in bad
  markets, with its parameters fixed in advance
- [[awoga-2018-momentum-market-regime-and-stocks-and-options-trading-strategies]] — a companion capstone from the same programme, with the same full-sample regime problem
- [[chang-chang-chou-2022-the-trend-is-your-friend-ensemble-learning]] — another trend-state labelling approach, where accurate classifiers still lose money
