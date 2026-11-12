# The Stock-Bond Correlation

| | |
|---|---|
| **Authors** | Megan Czasonis (State Street Associates), Mark Kritzman (Windham Capital, MIT), David Turkington (State Street Associates) |
| **Year** | 2021 (February) |
| **Type** | Journal article, *The Journal of Portfolio Management* 47(3), 67–76. US data, January 1926 to November 2019 |
| **PDF** | Not hosted in this repository (publisher reprint; "unauthorized copies" prohibited) |
| **Find it** | [doi.org/10.3905/jpm.2020.1.195](https://doi.org/10.3905/jpm.2020.1.195) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Stock-Bond+Correlation%22+Czasonis) |
| **BibTeX** | `czasonis2021stockbond` |
| **Status** | Reference: Exhibits 1, 3 and 4 carry the results; the method (partial sample regression) is from the same authors' 2020 JPM paper |

## What it is

A method for forecasting the stock–bond correlation over the horizon investors care about,
five years, instead of extrapolating the correlation of monthly returns. Stocks are the
S&P 500 (Ibbotson index before 1973), bonds the Bloomberg US Long Treasury index.

- **The horizon problem.** Over 1926–2019 the correlation of monthly returns is 0.07, of
  annual returns 0.11, of three-year returns 0.17 and of five-year returns 0.21. Correlations
  are not invariant to the return interval because returns are autocorrelated and
  cross-autocorrelated at lags, so monthly numbers understate how stocks and bonds drift
  together over a holding period.
- **Single-period correlation.** For each five-year window, the product of the stock and bond
  z-scores divided by the average of their squared z-scores. It is +1 when both deviate from
  their long-run means by the same number of standard deviations, −1 when they deviate
  equally in opposite directions. The ordinary Pearson correlation is exactly the average of
  these single-period values weighted by how unusual each period was ("informativeness").
- **Four predictors.** Year-on-year industrial production growth, CPI inflation, the log
  ratio of the earnings yield (inverse CAPE) to the 10-year Treasury yield, and the log
  ratio of their five-year trailing volatilities.
- **Partial sample regression.** The forecast uses only the 25% most "relevant" past
  observations, where relevance is similarity to today's predictors (negative Mahalanobis
  distance) plus unusualness (Mahalanobis distance from the historical mean). The
  correlation is mapped through a probit transform so forecasts stay inside −1 and 1.
- **Results** (annual forecasts of the next five-year single-period correlation, 1930–2018).
  The correlation between forecasts and outcomes rises from 0.23 for extrapolating the
  trailing monthly correlation, to 0.34 with the four predictors, 0.57 with relevance
  filtering, and 0.63 when growth and inflation enter as five-year paths. A
  Henriksson–Merton test of calling the sign of the next correlation scores 1.06 (p = 0.29)
  for extrapolation and 1.29 (p < 0.01) for the full model, where 1 is no skill and 2 is
  perfect.

## Why it's in the library

- It states plainly why the monthly stock–bond correlation is the wrong input for a
  multi-year allocation, and puts numbers on the gap (0.07 against 0.21 over the same
  century).
- The single-period correlation is a useful way to see which periods drive a full-sample
  correlation: it decomposes Pearson correlation into period-by-period contributions.
- The evidence is weaker than the headline. Only about 90 annual forecasts of overlapping
  five-year windows exist, so observations are far from independent. The paper's own
  shuffling test gives p = 0.06 for the relevance-filtered model and p = 0.37 for the best
  model (0.63), meaning the top result is not distinguishable from chance on that test; the
  authors lean on the Henriksson–Merton scores instead. Predictor choice and the 25% cut-off
  are not tested for sensitivity.
- Relevance filtering is the same Mahalanobis machinery as the authors' business-cycle index
  and correlation-surprise work.

## Links

- [[kinlaw-turkington-2014-correlation-surprise]] — the same group's Mahalanobis split of market turbulence into magnitude and correlation surprise
- [[kinlaw-kritzman-turkington-2021-a-new-index-of-the-business-cycle]] — the same relevance and Mahalanobis-distance idea applied to recession signals
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — why the correlation turns positive: inflation news dominating growth news
- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — a structural model of the same correlation flip around 2000
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — what goes wrong when one correlation number is trusted to describe joint risk
