# A Machine Learning Approach to Predict Turning Points for Chaotic Financial Time Series

| | |
|---|---|
| **Authors** | Xiuquan Li, Zhidong Deng (Tsinghua University) |
| **Year** | 2007 |
| **Type** | Conference paper, *19th IEEE International Conference on Tools with Artificial Intelligence (ICTAI 2007)*, 331–335 |
| **PDF** | Not hosted in this repository (IEEE copyright; the copy is a ResearchGate download) |
| **Find it** | [doi.org/10.1109/ICTAI.2007.105](https://doi.org/10.1109/ICTAI.2007.105) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22A+Machine+Learning+Approach+to+Predict+Turning+Points+for+Chaotic+Financial+Time+Series%22+Li) |
| **BibTeX** | `li2007turning` |
| **Status** | Reference: §3.2 (turning-point definition), §3.4 (threshold) and §4 (two examples). Results are shown only as figures |

## What it is

A short paper that treats price series as low-dimensional chaos and trains a neural
network to flag peaks and troughs a few steps ahead.

- **Chaos assumption.** Takens' embedding theorem says a deterministic chaotic system can be
  reconstructed from lagged copies of one observed series. The authors estimate an
  embedding dimension (8), a delay (1) and a largest Lyapunov exponent (about 0.14) for
  TESCO and the Dow Jones Industrial Average, and take the Lyapunov time (about 7 days) as
  the horizon over which the future is predictable. A "theorem" then says the next few
  values are a smooth function of the last m lags.
- **Turning points as labels.** A peak (trough) is a point after which the price falls
  (rises) by more than a set percentage within the horizon, with peaks and troughs forced
  to alternate. Each point gets a "turning indicator": 1 at peaks, 0 at troughs, linear in
  between.
- **Model and threshold.** A radial basis function network maps the last m prices to the
  turning indicator. A threshold on the output (0.20 for TESCO, 0.23 for the DJIA) is
  chosen on a validation period to maximise the sum of the true-positive and true-negative
  rates, and outputs beyond it are called peaks or troughs.
- **Data.** TESCO: 721 daily prices, January 2004 to October 2006, with about two and a
  half months of test data. DJIA: September 2001 to February 2006, with three months of test
  data.

## Why it's in the library

**As an example of turning-point prediction framed as classification.** Labelling
reversals by a forward move of a given size, then learning a score and a decision threshold
on held-out data, is a reasonable template, and the labels are a cleaner target than
next-day returns.

**As a cautionary example of what such papers often omit.** The test results are shown
only as charts, with no hit rates, no benchmark (not even a moving-average crossover), no
trading rule, no costs and no significance test, on a few months of data for two series.
The chaos premise is asserted rather than tested: a positive Lyapunov estimate from a few
hundred noisy prices does not establish deterministic chaos, and other work on market data
reports negative exponents. The "theorem" restates Takens' embedding and adds little.
Treat the paper as a method sketch, not evidence that turning points are predictable.

## Links

- [[demos-et-al-2015-some-statistical-properties-of-the-mini-flash-crashes]] — chaos tests
  on market data where the estimated Lyapunov exponents come out negative, against the
  chaos premise used here
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a model in
  which turning points between bull and bear states have a precise meaning, and the
  optimal rule to trade them can be derived
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  setting exit rules from a fitted model instead of searching thresholds on a short sample
- [[harvey-liu-zhu-2016]] — why results chosen on a short sample need a much higher bar
