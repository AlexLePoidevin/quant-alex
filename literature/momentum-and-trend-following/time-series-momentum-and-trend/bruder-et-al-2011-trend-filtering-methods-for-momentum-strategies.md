# Trend Filtering Methods for Momentum Strategies

| | |
|---|---|
| **Authors** | Benjamin Bruder, Tung-Lam Dao, Jean-Charles Richard, Thierry Roncalli (Lyxor Asset Management R&D, Paris) |
| **Year** | 2011 (December 2011; Lyxor white paper, posted to SSRN as 2289097 in 2013) |
| **Type** | Survey / white paper, 49pp, with S&P 500 illustrations and a statistical appendix (Kalman filter, L1 filtering, wavelets, SVM, singular spectrum analysis) |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.2289097](https://doi.org/10.2139/ssrn.2289097) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Trend+Filtering+Methods+for+Momentum+Strategies%22+Bruder) |
| **BibTeX** | `bruder2011trend` |
| **Status** | Reference: §2 (the catalogue of filters) and §3 (calibration, estimator variance, detection versus filtering, filtering versus forecasting) are the useful parts |

## What it is

A survey of the econometrics of extracting a trend from a price series, written by
Lyxor's research team as the toolkit behind momentum and CTA strategies. The model is
`y_t = x_t + ε_t`: log price is a smooth trend plus noise, and a filter estimates the trend
`x̂_t` and, more usefully for trading, its slope `µ̂_t`.

- **Linear filters are convolutions with a window.** A moving average of returns is
  just the cumulative return over the window. A moving-average crossover is a triangular
  weighting of past returns, peaked at the short window's length. Other kernels
  (asymmetric, Lanczos) trade off lag against noise.
- **Least-squares filters.** The Hodrick–Prescott (L2) filter penalises curvature. The
  local linear trend model solved by a Kalman filter turns out to be an exponential
  moving average whose decay is set by the Kalman gain (for λ = 5% the half-life is
  about 14 days).
- **Nonlinear filters.** Kernel, loess and spline regression; L1 trend filtering, which
  produces piecewise-linear trends and so detects breaks; wavelets; and appendices on SVM
  regression and singular spectrum analysis.
- **Multivariate filtering.** Common trends across several assets via error-correction
  and common stochastic trend models (for example a common emerging-market trend from
  several country indices).
- **Calibration.** Fitting the local-linear-trend model by maximum likelihood gives
  very short-term trends, because the likelihood uses one-step innovations. The authors
  prefer cross-validation on the forecast horizon you care about (an L1 filter on the
  S&P 500 with a 50-day horizon gives λ* = 7.03), or matching a filter's spectral width
  to a moving average of known length (the HP smoothing parameter for an n-day average is
  roughly 10.27 times a closed-form value).
- **An estimate is not a trend.** The slope estimator has a distribution, and its
  variance rises with volatility and falls with window length. The Mann–Kendall statistic
  tests whether a trend exists at all. On the S&P 500 the no-trend hypothesis is rejected
  (90% level) 97% of the time with a one-year window but only 58% of the time with a
  10-day window, and the filtered slope can be positive while the test statistic is
  negative.
- **Filtering the past is not forecasting the future.** Simulated driftless random walks
  show apparent trends after the fact. The test that matters is whether past trends
  predict future returns. A simple check (Table 3, 1995–2011): the average one-month
  return after a positive three-month return beats the average after a negative one for
  all eight indices shown, for example 1.1% versus 0.2% for the Eurostoxx 50 and 1.9%
  versus −0.3% for MSCI EM. No significance tests are given.

## Why it's in the library

**It is the reference for the signal-processing side of trend following.** Most trend
papers fix a signal (12-month return sign, a moving-average cross) and study the
strategy; this one catalogues the estimators themselves, shows the equivalences between
them (crossovers as weighted return averages, Kalman as an EMA) and is honest that a
filtered trend is a noisy estimate whose predictive value has to be tested separately.

**Caveats.** It is a practitioner survey from a manager that runs momentum strategies,
with illustrations rather than tests; the one predictive table has no standard errors and
the paper stops short of turning signals into positions, which the authors say is the
harder part.

## Links

- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the strategy-level evidence that
  the simplest of these filters (the 12-month return sign) predicts returns
- [[roncalli-2017-keep-up-the-momentum]] — Roncalli's later, more theoretical treatment of
  the same momentum risk premium
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a proof
  that the exponential moving average is optimal in a two-state model, matching this
  paper's Kalman-equals-EMA result
- [[benhamou-2016-trend-without-hiccups-a-kalman-filter-approach]] — a practitioner's
  Kalman-filter trading rule built on this paper's local linear trend model
