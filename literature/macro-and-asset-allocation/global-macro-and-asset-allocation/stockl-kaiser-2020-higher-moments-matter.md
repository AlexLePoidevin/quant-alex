# Higher Moments Matter! Cross-Sectional (Higher) Moments and the Predictability of Stock Returns

| | |
|---|---|
| **Authors** | Sebastian Stöckl, Lars Kaiser (University of Liechtenstein) |
| **Year** | 2020 (*Review of Financial Economics* 39(4), 455–481); working paper November 2016, SSRN 2747627 |
| **Type** | Working-paper version, 31pp. Monthly data on the 100 Fama–French size/book-to-market portfolios, August 1963 – December 2015 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `stockl2020higher` |
| **Status** | Reference: Table 4 (out-of-sample R²), Figure 3 (cumulative performance over time) and Table 5 (market timing) carry the results |

## What it is

A test of whether the *shape* of the cross-section of stock returns in a month predicts
the market's excess return over the following 1–48 months.

- **Predictors.** Each month, across the 100 Fama–French portfolios:
  - cross-sectional volatility (CSV): how dispersed returns are;
  - cross-sectional skewness (CSS);
  - cross-sectional kurtosis (CSK).

  Maio (2016) had shown that high CSV forecasts a lower equity premium. The authors add the
  two higher moments and combine them with CSV by principal components.
- **Statistical results.**
  - At the 1-month horizon nothing, neither these measures nor 14 standard predictors,
    forecasts out of sample.
  - Skewness adds most at horizons up to 12 months. Kurtosis adds most beyond 12 months.
  - At 48 months the out-of-sample R² reaches 15.7% for one principal-component
    combination, against 2.1% for CSV alone.
- **Timing over history.** The cumulative-performance plots in the Welch–Goyal style show
  that none of the cross-sectional measures predicted anything before about 2000. All
  their gains come after the dot-com bust, and CSV's own gains are concentrated around
  2000–03 and 2008. Adding skewness and kurtosis makes the post-2000 record smoother.
- **Economic value.** Market-timing strategies built on the combined forecasts beat CSV
  alone and the historical-mean benchmark on Sharpe ratio and certainty-equivalent gain
  at most horizons. Most of the 14 classical predictors do not.

## Why it's in the library

Return dispersion, how spread out stock returns are within a month, is a cheap, timely
market-state variable. It rises in bubbles and crises, when common factors explain
less of returns. This paper shows that the skew and fat-tailedness of the cross-section
carry information beyond dispersion itself. The market-state reading is the useful part,
whatever one makes of the forecasts.

The forecasting claims need discounting:

- **Many combinations tried.** Three moments, several principal-component mixes and
  horizons from 1 to 48 months are all reported, with no correction for the number tried.
- **Overlapping returns.** Long-horizon forecasts from monthly data overlap heavily, so the
  48-month R² rests on few independent observations.
- **One regime.** The predictive power appears only after 2000. It may be a feature of two
  crashes rather than a stable relation, which is the Welch–Goyal warning the authors
  themselves cite.

## Links

- [[campbell-lettau-malkiel-xu-2001]] — rising idiosyncratic volatility and falling
  correlations, the trend behind higher cross-sectional dispersion
- [[harvey-liu-zhu-2016]] — why many predictors tested on one sample need a higher bar
- [[cochrane-2011]] — return predictability and discount rates, the framework these
  equity-premium forecasts sit in
- [[liu-moench-2016-what-predicts-us-recessions]] — forecasting the macro state rather
  than the equity premium, with the same out-of-sample discipline
