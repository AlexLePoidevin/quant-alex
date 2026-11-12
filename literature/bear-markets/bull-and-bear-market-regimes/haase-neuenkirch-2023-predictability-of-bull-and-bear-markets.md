# Predictability of Bull and Bear Markets: A New Look at Forecasting Stock Market Regimes (and Returns) in the US

| | |
|---|---|
| **Authors** | Felix Haase and Matthias Neuenkirch (University of Trier) |
| **Year** | 2023 |
| **Type** | Paper. *International Journal of Forecasting* 39(2), 587–605 (doi 10.1016/j.ijforecast.2022.01.004); the copy is CESifo Working Paper 8828 (January 2021, SSRN 3767700), 63pp |
| **PDF** | Not hosted in this repository (working-paper download; the journal version is Elsevier copyright and no open licence is stated) |
| **Find it** | [doi.org/10.1016/j.ijforecast.2022.01.004](https://doi.org/10.1016/j.ijforecast.2022.01.004) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Predictability+of+Bull+and+Bear+Markets%3A+A+New+Look+at+Forecasting+Stock+Market+Regimes+%28and+Returns%29+in+the+US%22+Haase) |
| **BibTeX** | `haase2023predictability` |
| **Status** | Reference: §3 (method), §4.2 (the Lunde–Timmermann dating, Table 2), Table 3 (regime forecast accuracy), Table 4 (economic value) and Tables 5–6 (return forecasts) carry the results |

## What it is

A forecasting study of US bull and bear markets on weekly S&P 500 data, November 1989 to
July 2020. It combines three tools that each have a track record in the return-prediction
literature:

1. **Diffusion indices.** 115 weekly macro and financial variables, with publication lags and
   data revisions respected, are compressed into a few factors by principal components. Some
   variants use shrinkage (sparse PCA, or soft thresholding to pick targeted predictors).
2. **Markov switching with time-varying transition probabilities.** Each model uses one factor
   to move the probability of switching between a bull and a bear state. Model A also lets the
   factor enter the return equation; Model B uses it only in the switching equation.
3. **Forecast combination.** The many one-factor models are pooled within clusters by simple
   averaging, inverse rank or Bayesian model averaging.

Forecasts are made in real time for the last 820 weeks (October 2004 to July 2020). They are
scored against bear markets dated ex post with the Lunde–Timmermann rule: a fall of 10% from a
peak starts a bear market, and a rise of 15% from a trough ends it.

What it finds:

- **Regimes are predictable.** Most combinations classify more than 80% of weeks correctly and
  70–75% of bear weeks. The best (sparse PCA, Model B, Bayesian averaging) reaches an AUC of
  0.877. A 12-month moving average gets 82% of weeks right overall but only 52% of bear weeks.
  A plain Markov-switching model with constant transition probabilities gets 79% and 76%.
- **The forecasts pay in a switching strategy.** Moving between the S&P 500 and short-term
  government bonds on the regime call, with 10 basis points per trade, most specifications earn
  Sharpe ratios of 0.7–0.9 against 0.37 for the index. Their maximum drawdown is 12% against
  55% for the index. The best (A-TSPC-BMA) earns 11.8% a year at 10.6% volatility.
- **Return forecasts do not beat the historical mean.** The same machinery used to forecast
  weekly returns gives negative out-of-sample R², none significant, even though following
  those forecasts adds some certainty-equivalent return.

## Why it's in the library

It is the most careful attempt in this folder to forecast bull and bear markets in real time
rather than date them afterwards. It respects data publication lags, charges trading costs, and
reports the result most papers leave out: regimes can be forecast even when returns cannot.

What to keep in mind:
- **The benchmark is already strong.** The simple constant-probability Markov-switching model
  earns a Sharpe ratio of 0.63 and a 14.5% drawdown. The gain from 115 variables is the step
  from 0.63 to about 0.8, not the step from the index's 0.37.
- **There are many specifications.** The paper reports 30 combinations without adjusting for
  having tried them all. The spread across them (Sharpe 0.47–0.90) is a rough guide to how much
  of the best number is luck.
- **There are few events.** The out-of-sample period covers 2008, a handful of 10% corrections
  and the 2020 crash. Most specifications share the same 12.25% maximum drawdown, so they are
  largely making the same calls.
- **"Bear market" means a 10% fall here.** That is a correction by most practitioners'
  definitions, so this is the frequent-regime end of the literature.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a richer four-state model
  that the authors cite as a direction for more than two regimes
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — Markov switching applied to volatility
  rather than returns
- [[yang-wagner-2014-optimal-probabilistic-market-timing-using-bull-bear-cycle-statistics]] — a
  bull/bear switching rule built from price data alone
- [[harvey-liu-zhu-2016]] — why choosing the best of many specifications overstates performance
- [[keller-keuning-2016-paa]] — a rule-based tactical allocation with the same risk-on/risk-off
  switch to bonds
