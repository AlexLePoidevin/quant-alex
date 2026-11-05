# A Simple Approximate Long-Memory Model of Realized Volatility

| | |
|---|---|
| **Authors** | Fulvio Corsi (University of Lugano; Swiss Finance Institute) |
| **Year** | 2009 |
| **Type** | Journal article, *Journal of Financial Econometrics* 7(2), 174–196. Tick data for USD/CHF (1989–2003), S&P 500 futures (1990–2007) and 30-year Treasury bond futures |
| **PDF** | Local copy only (Oxford University Press; library download) |
| **BibTeX** | `corsi2009har` |
| **Status** | Reference: §2 (the volatility cascade and the HAR-RV model) and §4 (in- and out-of-sample forecasts) |

## What it is

The paper that introduced HAR-RV, the standard benchmark for forecasting realised
volatility.

- **Idea.** Markets contain traders with different horizons: intraday, weekly and
  monthly or longer. Each group reacts to volatility measured over its own horizon, and
  longer-horizon volatility feeds into shorter-horizon volatility. This "volatility
  cascade" is the Heterogeneous Market Hypothesis of Müller et al. (1993).
- **The model.** Tomorrow's daily realised volatility is regressed on three terms:
  today's daily realised volatility, the average over the past week (5 days) and the
  average over the past month (22 days). It is a restricted AR(22) estimated by ordinary
  least squares, with just four parameters.
- **Long memory without long memory.** Volatility's autocorrelation decays slowly for
  months, which usually calls for fractionally integrated models (ARFIMA, FIGARCH) that
  are awkward to estimate. HAR is not formally long-memory. Summing three horizons is
  enough to reproduce the slow decay, the fat tails and the scaling of returns across
  horizons in simulation.
- **Forecasts.** Models are re-estimated daily on a rolling 1,000-day window.
  - Out of sample, HAR beats AR(1) and AR(3) at one day, one week and two weeks ahead on
    all three series.
  - It is about as good as ARFIMA(5,d,0): slightly better at daily and weekly horizons,
    slightly worse at two weeks.
  - Short-memory models fall behind at longer horizons because their forecasts revert to
    the mean too quickly.

## Why it's in the library

**It is the baseline every realised-volatility forecast is compared with.** Four
coefficients, OLS, daily, weekly and monthly averages: any more complex volatility
forecaster, machine learning included, should be judged on how much it beats HAR.

**It is also a statement about market structure.** The cascade from long to short
horizons gives an economic reading of why volatility persists. Volatility clustering
comes from participants working on different clocks, not only from news arriving in
bursts.

**Limits.** Three long series and point forecasts only, with no density or risk forecasts. Later work
adds jumps, leverage effects and semivariances to the same frame.

## Links

- [[carr-wu-zhang-2019-using-machine-learning-to-predict-realized-variance]] — machine
  learning on option prices to forecast realised variance, with option-implied
  benchmarks
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — measuring
  realised volatility from tick data when bid-ask noise distorts it
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching as another way
  to model persistent volatility
- [[asgharian-christiansen-hou-2023-effect-of-uncertainty-on-volatility-and-correlation]] — HAR extended with risk-aversion and uncertainty predictors
