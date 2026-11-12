# Understanding Asset Correlations

| | |
|---|---|
| **Authors** | Dominic Burkhardt, Henrik Hasseltoft (University of Zurich and Swiss Finance Institute) |
| **Year** | 2012 (September draft; first draft January 2009) |
| **Type** | Working paper, Swiss Finance Institute Research Paper No. 12-38 (SSRN 1879855), 64pp. US quarterly data, 1965–2011 (some series from the 1930s) |
| **PDF** | Not hosted in this repository (SSRN working paper, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.1879855](https://doi.org/10.2139/ssrn.1879855) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Understanding+Asset+Correlations%22+Burkhardt) |
| **BibTeX** | `burkhardt2012correlations` |
| **Status** | Reference: §2–3 (empirics and regime-switching estimates), §6 (VAR) and the conclusion; the long-run-risk model in §4–5 skimmed |

## What it is

An explanation of why the US stock–Treasury correlation changes sign, built on one
macro quantity: whether inflation is bad news for growth (countercyclical) or comes with
growth (procyclical).

- **The empirical pattern.** Stock–bond correlations move inversely with the correlation of
  consumption growth and inflation. Positive stock–bond correlation goes with stagflation;
  negative goes with procyclical inflation. Ten-year growth–inflation correlations
  were about 0.8 in the 1930s, about −0.8 in the 1970s and close to 0.6 in the 2000s.
- **Regime switching.** A two-state Markov-switching VAR on consumption growth, inflation,
  stock and bond excess returns (1965–2011). The countercyclical-inflation state is
  persistent (stay probability 0.977, expected duration 43 quarters, unconditional
  probability 0.73); the procyclical state lasts about 16 quarters. The smoothed
  probability of the procyclical state passes 0.5 in 2001Q2, which the authors treat as the
  break. In that state the stock–bond shock covariance flips from positive to negative.
- **Inflation uncertainty cuts both ways.** It always lowers stock prices. It lowers nominal
  bond prices when inflation is countercyclical (bonds are risky) but raises them when
  inflation is procyclical (bonds hedge bad times). So inflation risk predicted stock–bond
  covariance positively before 2000 and negatively after.
- **The Fed model.** The correlation of dividend yields with nominal yields was 0.64 over
  1965–2001Q2 and −0.57 over 2001Q3–2011. Inflation illusion explains the first but not the
  second; the regime story explains both.
- **A long-run-risk model.** A Bansal–Yaron economy with non-neutral inflation shocks and
  regime switches reproduces the sign changes and, unusually, an upward-sloping real yield
  curve after 2000.
- **What drove each regime.** In a VAR, inflation and monetary-policy shocks explain 6% and
  18% of stock–bond covariance variance at 20 quarters in 1965–1999 (output 2%); in
  2000–2011 output shocks explain 25% at one quarter and 56% at 20 quarters.

## Why it's in the library

- It is the cleanest statement of the mechanism several other notes here rely on: bonds
  hedge equities when inflation moves with growth, and fail to when inflation moves against
  it. That is the variable to watch for a return to positive correlation.
- It joins the stock–bond correlation and Fed-model questions under one explanation,
  without needing irrational investors.
- Caveats: the procyclical regime is essentially one episode (2000–2011) plus a brief
  late-1980s visit, so its parameters have large standard errors, as the authors say; the
  VAR identification is a simple Cholesky ordering; and the sample stops before the
  2021–22 inflation, which is the natural out-of-sample test.

## Links

- [[bekaert-engstrom-2010-inflation-and-the-stock-market-the-fed-model]] — the Fed model explained through inflation and risk aversion rather than regimes
- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the same sign change built on the inflation–output-gap correlation in a habit model
- [[ang-bekaert-2002-regime-switches-in-interest-rates]] — Markov regime switching applied to the short rate
- [[aqr-2020-fire-and-ice-inflation-and-deflation]] — how assets behave in inflationary and deflationary surprises
