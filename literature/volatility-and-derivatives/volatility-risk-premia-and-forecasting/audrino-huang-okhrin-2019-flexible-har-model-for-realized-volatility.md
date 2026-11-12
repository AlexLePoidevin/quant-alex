# Flexible HAR Model for Realized Volatility

| | |
|---|---|
| **Authors** | Francesco Audrino (St. Gallen), Chen Huang (Humboldt-Universität zu Berlin), Ostap Okhrin (TU Dresden) |
| **Year** | 2019 |
| **Type** | Journal article, *Studies in Nonlinear Dynamics & Econometrics* 23(3), 2019 (online November 2018). doi:10.1515/snde-2017-0080. The copy is the April 2016 working paper |
| **PDF** | `audrino-huang-okhrin-2019-flexible-har-model-for-realized-volatility.pdf` (kept locally; working paper with no open licence) |
| **Find it** | [doi.org/10.1515/snde-2017-0080](https://doi.org/10.1515/snde-2017-0080) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Flexible+HAR+Model+for+Realized+Volatility%22+Audrino) |
| **BibTeX** | `audrino2019flexiblehar` |
| **Status** | Reference: Section 4.2 (lag selection), Tables 4.2–4.3 (forecast comparison and SPA tests) and Section 4.4 (group LASSO tests) carry the results |

## What it is

A test of whether the standard daily–weekly–monthly structure of the HAR model for realised
volatility is the right one, using the adaptive LASSO to let the data choose the lags.

- **Background.** The HAR model (Corsi) forecasts tomorrow's realised volatility from its
  average over the last 1, 5 and 22 days, standing for daily, weekly and monthly traders.
  It is the standard benchmark for volatility forecasting.
- **The flexible model.** Allow averages over any horizon from 1 to p days (p = 50), keep
  the HAR form, and let the adaptive LASSO pick which horizons enter. False positives are
  then removed with individual tests and a conservative stepwise joint test on lags beyond
  22.
- **Data.** Five-minute realised volatility for ten NYSE stocks (Boeing, IBM, J&J, Coca-Cola,
  Walmart, Caterpillar, Disney, Pfizer, UnitedHealth, Exxon), September 2003 to August 2015,
  in rolling 1,000-day windows.
- **Lag findings.** Lags beyond 22 are mostly insignificant, which supports a one-month
  maximum. But the exact (1, 5, 22) structure is not recovered. The monthly term is often
  not needed, and small peaks appear every two weeks or so (lags 9–11, 19–20, 29–31,
  39–41).
- **Forecasts.** Out of sample, the flexible HAR slightly beats HAR(1, 5, 22) and is the
  best of the HAR-type models. A plain AR model with lag length chosen by AIC is better both
  in and out of sample. The HARQ model (with realised quarticity) forecasts worst, possibly
  because no outlier filter was applied. Superior-predictive-ability tests cannot reject
  that the flexible HAR is as good as any competitor, and the model confidence set keeps
  HAR(1, 5, 22), the flexible HAR, AR-AIC and two others.
- **Group LASSO test.** Grouping AR lags as {1}, {2–5}, {6–22}, {23–50}, only 0.73% of
  windows pass every test that the classic HAR structure implies. Acceptance is highest in
  2003–2004 and near zero during the crisis.

## Why it's in the library

- **How much the HAR structure matters.** The (1, 5, 22) lags are a convention, not a
  finding. The forecasting gain from choosing them by data is small, so the classic HAR
  remains a reasonable default, but its structure fails most formally in unstable markets.
- **A careful use of LASSO for time series.** The paper tests the variables the LASSO
  selects for false positives, rather than taking the selection at face value.
- **Limits.** Ten large stocks over twelve years, with forecast error ratios reported only
  as averages. The best overall forecaster was an unrestricted AR model, which the authors
  mention but do not emphasise.

## Links

- [[carr-wu-zhang-2019-using-machine-learning-to-predict-realized-variance]] — forecasting
  realised variance from option prices instead of from its own past
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]] — how realised
  volatility is measured from intraday data, and why microstructure noise matters
- [[doman-doman-2020-daily-fx-volatility-and-the-time-of-day]] — another check on a
  convention in volatility measurement, the choice of daily close
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching in volatility, the
  instability this paper finds the HAR structure breaks down under
