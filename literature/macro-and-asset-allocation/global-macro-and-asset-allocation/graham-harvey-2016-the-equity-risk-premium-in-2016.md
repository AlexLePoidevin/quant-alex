# The Equity Risk Premium in 2016

| | |
|---|---|
| **Authors** | John R. Graham and Campbell R. Harvey (Duke University, Fuqua; NBER) |
| **Year** | 2016 (version of 2 August 2016) |
| **Type** | Working paper, SSRN 2816603, 20pp. One of the authors' annual updates of the Duke/CFO Magazine survey |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.2816603](https://doi.org/10.2139/ssrn.2816603) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Equity+Risk+Premium+in+2016%22+Graham) |
| **BibTeX** | `graham2016erp` |
| **Status** | Reference: §2.4 (the 2016 numbers), §2.5 (WACC and hurdle rates) and §2.7 (what the premium moves with) carry the content |

## What it is

The 2016 edition of a survey-based estimate of the US equity risk premium. Each quarter
since June 2000, US chief financial officers have been asked for their expected 10-year
annual S&P 500 return and a 10th–90th percentile range. The premium is that expectation
minus the 10-year Treasury yield.

- **Data.** 65 surveys from June 2000 to June 2016, over 23,000 responses after filters
  (for example, dropping unannualised or "lazy" ±1% ranges). Response rates are 5–8%; the
  authors give six reasons non-response bias is small.
- **The 2016 numbers.** The average premium in June 2016 was 4.02%, against a 3.58% average
  over the 16 years. The expected 10-year S&P 500 return was 5.83%, below the 7.19%
  long-run average, because the 10-year yield was only 1.81%.
- **Stable over time.** The quarterly average premium has a standard deviation of only
  0.58%, against 2.91% across individual responses.
- **Disagreement and uncertainty.** Dispersion across CFOs peaked in February 2009 at 4.13%
  (3.24% in 2016). Individual forecasts are negatively skewed in every survey.
- **WACC and hurdle rates.** In 2016 the premium implies a cost of equity of 6.63% for a
  beta-1 firm and a WACC of about 5.67%. When CFOs were asked directly, they reported far
  higher WACCs (10% in March 2011, 9.3% in June 2012, against implied values of under 6.45%
  and 5.37%). The hurdle rates they actually use (13.5% on average in 2012) are about 400bp
  above their stated WACCs. There is no sign of a small-firm premium in either.
- **What the premium moves with.** It is weakly higher after poor past-year returns
  (R² 0.05), correlated 0.35 with the VIX and 0.49 with the Baa–Treasury credit spread, and
  negatively with TIPS real yields (−0.52), driven by the negative-real-yield period.

## Why it's in the library

- **A direct read of expected returns.** It is one of the few long time series of what
  practitioners actually expect, rather than a model estimate, so it is a reference point
  for capital market assumptions.
- **It shows the premium barely moves.** Despite crises, the survey premium stays near 3–4%,
  while the risk measures it correlates with swing widely.

The overlapping 10-year horizons mean the forecasts cannot yet be checked against outcomes,
and the time-series analysis is descriptive, without formal tests.

## Links

- [[graham-harvey-2018-the-equity-risk-premium-in-2018]] — the 2018 edition of the same survey
- [[aqr-2022-capital-market-assumptions-for-major-asset-classes]] — yield-based expected returns as an alternative to surveys
- [[asness-israelov-liew-2011-international-diversification-works-eventually]] — long-horizon equity outcomes, where the premium assumption matters most
