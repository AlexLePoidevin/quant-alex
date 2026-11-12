# Forecasting Inflation like a Data Scientist

| | |
|---|---|
| **Authors** | Gerardo Manzo, Jeffrey N. Saret (Two Sigma) |
| **Year** | 2017 (November) |
| **Type** | Manager commentary (Two Sigma *Street View*), 5pp, of which about 1.5 are on inflation; the rest is a list of technology articles and disclaimers |
| **PDF** | Not hosted in this repository (© Two Sigma, marked confidential and not for distribution) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Forecasting+Inflation+like+a+Data+Scientist%22+Manzo) for the title and authors |
| **BibTeX** | `manzo2017inflation` |
| **Status** | Reference: short; Figure 1 and the text beside it are the whole argument |

## What it is

A short note arguing that allocators should forecast inflation by pooling many different
forecasts, as a data scientist would, rather than relying on a single measure or model.

- **Why inflation is hard to pin down.** There are many definitions (CPI, PPI, core,
  goods versus services, the PCE index the Fed targets); there is a flood of data, such as
  online prices, that changes faster than shop prices and whose products change
  specification; and market-implied forecasts from TIPS and inflation swaps vary in
  liquidity across maturities.
- **The approach.** Collect publicly available forecasts of US inflation (survey and
  market-based, across horizons and definitions), convert each to a z-score against its
  own history, and look at the whole distribution each month instead of a point estimate.
- **What the chart showed for 2017.** Most forecasts sit within two standard deviations of
  their norms. The median hovered around its long-run level but dipped noticeably in
  October 2017, even as the labour market tightened, which the authors call inconsistent
  with the Phillips curve. The distribution was negatively skewed, which they read as more
  forecasters thinking the Fed too hawkish than too dovish, and so a risk of Fed actions
  surprising markets.

## Why it's in the library

**The idea is sound and general.** Inflation has no single correct measure, so a normalised
cross-section of forecasts gives a better picture of expectations, and of disagreement about
them, than any one series. The same logic applies to any macro input to an allocation.

**There is almost no evidence.** It is a marketing commentary from a quantitative manager.
It does not list the forecasts it pools, show how they were weighted, or test whether the
pooled view forecasts better than its parts. The October 2017 dip is one month, and the
authors themselves call it premature to extrapolate. Keep it as a statement of method, not a
result.

## Links

- [[chen-roll-ross-1986]] — unexpected inflation and changes in expected inflation as priced macro risks
- [[keller-keuning-2023-haa]] — a tactical allocation rule that reacts to rising yields and inflation
- [[li-et-al-2022-does-fiscal-policy-matter-for-stock-bond-return-correlation]] — why the link between inflation and the economy changed sign around 2001
