# Regime Switches in Interest Rates

| | |
|---|---|
| **Authors** | Andrew Ang and Geert Bekaert (Stanford) |
| **Year** | 2002 |
| **Type** | Paper. *Journal of Business & Economic Statistics* 20(2), 163–182 (doi 10.1198/073500102317351930); the copy is the March 1998 working paper (NBER w6508), 70pp |
| **PDF** | Not hosted in this repository (working-paper version of a Taylor & Francis journal article; no open licence) |
| **Find it** | [doi.org/10.1198/073500102317351930](https://doi.org/10.1198/073500102317351930) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Regime+Switches+in+Interest+Rates%22+Ang) |
| **BibTeX** | `ang2002regime` |
| **Status** | Reference: §2 and Table 2 (rates across business cycles), §5.4–5.5 (moments and out-of-sample forecasts, Tables 10–12), §5.6 and Table 15 (regimes against recessions) carry the results |

## What it is

An econometric study of regime-switching models for short-term interest rates in the US,
Germany and the UK. The data are monthly 3-month and 5-year zero-coupon yields from January
1972 to August 1996, with the last 30 months held out for forecasting.

The models range from a univariate regime-switching AR(1) and CIR model to versions that add
other countries' short rates and the domestic term spread. Some let the transition
probabilities depend on the data.

What it finds:

- **Two regimes, separated by volatility and mean reversion.** In one regime the short rate has
  low volatility and behaves almost like a random walk. In the other it is high, volatile and
  strongly mean-reverting. Because the mean-reverting regime recurs, the whole process stays
  stationary even though one regime has a unit root. That is how these models capture the
  near-unit-root persistence of rates.
- **The volatile regime is the recession regime, at least in the US.** The ex-ante regime
  probabilities predict 84% of US recessions one month ahead in-sample, better than the term
  spread at one and two months. At longer horizons the spread is the better predictor, and it
  is better at all horizons for Germany and the UK. The 1979–82 Volcker monetary-targeting
  period falls in the volatile regime.
- **Regime models forecast better but fit moments worse.** One-regime models match the
  sample mean, variance, skewness and kurtosis better. Regime-switching models forecast the
  short rate better out of sample in all three countries, especially when they use
  international rates or the term spread. A simulation shows the same pattern when the true
  model is regime-switching, because these models need very large samples to pin down their
  unconditional moments.
- **Univariate estimates are unreliable.** Single-country estimates are probably inconsistent,
  and estimation often fails to converge.

## Why it's in the library

It is the reference model for **interest-rate regimes**: calm, near-random-walk rates in normal
times, and volatile, mean-reverting rates around recessions and policy shifts. That background
matters for the inflation, Fed and stock–bond correlation papers in this section, which all
assume rates behave differently across regimes.

It is also a useful warning about the method. Regime models can forecast well while fitting
the data's moments badly, and the estimation is fragile. The out-of-sample test covers only 30
months, from 1994 to 1996.

## Links

- [[ang-timmermann-2012-regime-changes-and-financial-markets]] — the later survey that summarises
  this model alongside equity and currency regimes
- [[haase-neuenkirch-2023-predictability-of-bull-and-bear-markets]] — regime switching with
  time-varying transition probabilities applied to stock market regimes
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — the same two-regime idea applied to
  equity volatility
