# The Equity Risk Premium in 2018

| | |
|---|---|
| **Authors** | John R. Graham and Campbell R. Harvey (Duke University, Fuqua; NBER) |
| **Year** | 2018 (version of 28 March 2018) |
| **Type** | Working paper, SSRN 3151162, 22pp. One of the authors' annual updates of the Duke/CFO Magazine survey |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3151162](https://doi.org/10.2139/ssrn.3151162) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Equity+Risk+Premium+in+2018%22+Graham) |
| **BibTeX** | `graham2018erp` |
| **Status** | Reference: read in full; §2.4 (the 2018 numbers), §2.5 (WACC and hurdle rates) and §2.7 (what the premium moves with) carry the content |

## What it is

A survey-based estimate of the equity risk premium. Every quarter since June 2000, US
chief financial officers have been asked for their expected 10-year annual S&P 500 return;
subtracting the 10-year Treasury yield gives an ex ante risk premium. This edition covers
71 surveys to the one that closed on 7 December 2017 (Table 1's caption says September
2017), about 24,800 responses, roughly 350 a quarter.

- **The level.** The average premium over 2000–2017 is 3.64% (3.62% pooling all
  individual responses), with a standard deviation of only 0.58% across quarters. The
  December 2017 survey gives 4.42%: an expected S&P 500 return of 6.79% on a 2.37%
  10-year yield. It moved little through two recessions (3.52% in recessions, 3.68%
  outside them; 60 observations).
- **Disagreement and tails.** Respondents also give 10th and 90th percentiles, so the
  paper recovers each CFO's own uncertainty (Davidson–Cooper approximation, spread of the
  tails divided by 2.65) and skewness. Disagreement peaked at 4.13% in February 2009
  (3.49% now); individual volatility also peaked then (4.29%). Every quarter shows
  negative average skewness in individual forecasts.
- **What the premium moves with.** Weakly higher after poor past returns and at low
  forward P/E (non-linear); correlation −0.52 with the 10-year TIPS yield (driven by the
  negative-real-yield period); +0.26 with the VIX and +0.42 with the Baa–Treasury credit
  spread, with a marked divergence from both at the end of the sample.
- **WACC and hurdle rates.** The premium implies a weighted average cost of capital of
  about 5.9% for an average firm, but CFOs report WACCs near 9–10% and investment hurdle
  rates of 13.5% (June 2012), with no size premium in either. The gap is roughly what you
  get by plugging in 1926-onwards historical averages (an imputed 9.7%), which suggests
  firms use long-run historical inputs rather than current expectations.

## Why it's in the library

It is a direct, forward-looking measure of the equity premium that is not backed out of
prices or fitted to past returns, and it sits well below the 5–6% long-history numbers
that most capital market assumptions start from. It also shows how stable such survey
expectations are: they barely react to recessions, which is either evidence that the
premium is close to constant or that CFOs anchor. The authors are clear about the limits:
response rates are 5–8%, the 10-year forecasts overlap so successive quarters are not
independent, and there is no way yet to test the forecasts against outcomes. Read it as
a level for long-run assumptions next to AQR's and others' capital market assumptions in
this folder, not as a timing signal.

## Links

- [[asness-israelov-liew-2011-international-diversification-works-eventually]] — long-horizon equity outcomes, where the premium assumption matters most
- [[kinlaw-kritzman-turkington-2021-a-new-index-of-the-business-cycle]] — another attempt to read the macro state, against which this premium barely moves
- [[fama-french-1993]] — the factor-model view of expected returns that survey premia sit outside
- [[blitz-2021-the-quant-cycle]] — the same finding for factor premia: macro and business-cycle states explain little of their variation
- [[graham-harvey-2016-the-equity-risk-premium-in-2016]] — the 2016 edition of the same survey
