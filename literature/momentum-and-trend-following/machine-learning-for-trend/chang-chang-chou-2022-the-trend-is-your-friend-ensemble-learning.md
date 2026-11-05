# The Trend is Your Friend: A Note on An Ensemble Learning Approach to Finding It

| | |
|---|---|
| **Authors** | Tzu-Pu Chang, Yu-Cheng Chang, Po-Ching Chou (National Yunlin University of Science and Technology, Taiwan) |
| **Year** | 2022 (Bulletin of Applied Economics 9(1), 19–25; published online 3 January 2022) |
| **Type** | Journal note, 7pp. Taiwan Top 50 ETF (0050), daily, May 2004 – November 2018; last 15% of days as the test set |
| **PDF** | Local copy only (journal PDF with no stated licence) |
| **BibTeX** | `chang2022trendensemble` |
| **Status** | Reference: Tables 1 and 2 hold all the results |

## What it is

A short note that labels each trading day of one ETF as part of an uptrend or a
downtrend, trains classifiers to predict tomorrow's label, and trades the predicted
trend changes.

- **The target.** Peaks and troughs are found with a non-parametric rule: a price is a
  peak if it is higher than the prices n days before and after it (the value of n is not
  given). Days from a trough to the next peak are "uptrend", from a peak to the next
  trough "downtrend". The model predicts the next day's label.
- **The inputs.** Open, high, low, close and volume; twenty technical indicators;
  fourteen measures of institutional and retail positioning (margin purchases, short
  sales, institutional net buying); and whether the NASDAQ was in a bull or bear state the
  previous day. All are standardised and lagged one day.
- **The models.** A support vector machine, a multilayer perceptron, AdaBoost and
  XGBoost as base learners, combined by a decision-tree meta-learner (two-layer
  stacking). Trades are at the next day's open when the predicted label flips, with a
  0.5% cost per trade.
- **Results on the test set.**
  - The base learners classify 60–69% of days correctly but all lose money (−10% to
    −31% total return), with roughly 30% of trades profitable.
  - The stacked model classifies 66% correctly, makes 31 trades and returns +19.4%,
    against +11.1% for buy-and-hold over the same period. 45% of its trades are
    profitable.
  - 20-day and 60-day moving-average crossovers lose 27.0% and 20.6%.
- **The authors' conclusion.** Accuracy does not translate into profit: the most
  accurate classifiers lost the most, and stacking produced the only positive return.

## Why it's in the library

**It is a compact example of why classification accuracy is the wrong yardstick for a
trading signal.** Models that get 69% of days right lose 30%, because what matters is
being right around the turns and not over-trading, which a per-day accuracy score does
not measure.

**It is also an example of how not to evaluate one.** The test is a single
period of about 540 trading days on one ETF, with 31 trades. The result is a single
total return, with no Sharpe ratio, significance test or comparison across periods, and
drawdowns are given in Taiwan dollars per 1,000 shares rather than as percentages. Five
models and two moving-average rules were compared on the same test set, and the
number of days n used to define peaks, which shapes the target, is not reported. The
input list is "available on request". A 19% return against 11% for buy-and-hold,
after one strategy out of several was singled out, is weak evidence.

**The labelling idea is reusable.** Defining trend states from turning points, then
predicting the state rather than the next return, is a common way to turn trend
following into a supervised problem; the same caveats about look-ahead in the labels
and test-set selection apply wherever it is used.

## Links

- [[srivastava-bhattacharyya-2018-dynamically-adaptive-systematic-trading-strategy]] — another regime-labelling approach to trend and volatility states, with similar in-sample caveats
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — why selecting rules on a backtest overstates them
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]] — why boosted trees are the usual baseline on tabular features like these
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the simple trend rule that machine-learning approaches are trying to beat
