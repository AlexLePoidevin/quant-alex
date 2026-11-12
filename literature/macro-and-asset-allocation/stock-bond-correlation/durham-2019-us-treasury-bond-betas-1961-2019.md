# U.S. Treasury Bond Betas: 1961–2019

| | |
|---|---|
| **Authors** | J. Benson Durham |
| **Year** | 2019 (dated 3 October 2019) |
| **Type** | Working paper, SSRN 3463854, 39pp. Published as "US Treasury Bond Betas: 1961–2019", *Journal of Fixed Income* 29(4), 2020, 20–47 |
| **PDF** | Not hosted in this repository (SSRN working paper with no open licence) |
| **Find it** | [doi.org/10.3905/jfi.2020.1.083](https://doi.org/10.3905/jfi.2020.1.083) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22U.S.+Treasury+Bond+Betas%3A+1961%E2%80%932019%22+Durham) |
| **BibTeX** | `durham2019betas` |
| **Status** | Reference: the A-DCC section (Table 2, Charts 1–4), the spectral section (Tables 3–4, Charts 5–10) and the quantile-regression section (Tables 5–6, Charts 11–18) carry the results |

## What it is

A study of how well US Treasuries have hedged the S&P 500, using daily data from June 1961
to September 2019 and three tools that go beyond the usual rolling correlation.

- **Why it matters for yields.** In 288 alternative regressions of the 10-year zero-coupon
  yield on macro forecasts, deficits and foreign demand (monthly, 1996–2018), the dynamic
  bond–stock correlation is significant in every one: a one-standard-error rise in the
  correlation goes with about 38bp higher yields, comparable to or larger than the
  survey-expectation variables.
- **Asymmetric DCC-GARCH.** The familiar regime change: the average conditional correlation
  between 2-, 5- and 10-year Treasuries and stocks fell from about +0.2 before 1998 to
  about −0.2 after. The new point is that the *variability* of the correlation rose: its
  standard deviation went from 0.04–0.07 before 1998 to 0.18–0.23 after, even as bond
  volatility and "vol of vol" fell. Less covariance risk on average, but more uncertainty
  about it. Splitting yields into expected short rates and term premium (Adrian–Crump–Moench)
  shows the expected-rate component turned positively correlated with stocks in 2012–14
  (the taper tantrum period), while the term premium stayed a hedge.
- **Spectral decomposition.** Using rolling three-year Fourier transforms, cycles of one
  week or shorter account for about half of the bond–stock covariance, and their share has
  risen (for the 10-year from about 44% in the early 1960s to about 60% by 2019). But
  band-specific betas are much the same at every frequency: Treasuries are not a better
  hedge against short-lived shocks than against long ones, which sits awkwardly with the
  view that flights to quality drive the correlation.
- **Convexity.** OLS betas on the most extreme stock days, and quantile regressions of
  Treasury returns on stock returns, ask whether Treasuries pay off most in the worst
  states. Over the full sample they do not: conditioned on a 0.5th-percentile stock day
  (−3.34%), the 2-year return distribution is wider (about 209bp from 5th to 95th
  percentile, against 160bp on an equally large up day) and negatively skewed. After 1998
  the 2-year improves (its bad-day skew is more favourable than its good-day skew), but
  the 10-year's bad-day distribution is wider and more negatively skewed, and over the
  last three years of the sample it is about 64bp wider than on good days.

## Why it's in the library

**It separates "negatively correlated on average" from "pays off in the crash".** The
post-2000 negative stock–bond correlation is real, but this paper finds no consistent
evidence that long Treasuries are a convex hedge: their returns get more uncertain and more
left-skewed exactly when stocks fall hard. That matters for any portfolio that counts on
duration as its crisis asset, and for risk parity.

**The rising variance of the correlation is the practical warning.** A model that plugs
in a single negative correlation understates how quickly the hedge can switch off, as it
did in 2022, after this paper was written.

**Caveats.** Fitted zero-coupon curves rather than traded bonds (which the author notes
may understate the hedge, since on-the-run issues carry crisis liquidity premiums), and a
1998 break date chosen by the author. The 288-regression valuation exercise is presented
as motivation only; its details are "available on request".

## Links

- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the
  macro explanation for the sign flip: inflation went from counter- to pro-cyclical around
  2001
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — when inflation
  news dominates, stocks and bonds fall together
- [[li-et-al-2022-does-fiscal-policy-matter-for-stock-bond-return-correlation]] — a
  monetary-versus-fiscal-regime account of the same flip
- [[soper-2015-vix-and-us-treasuries-during-quantitative-easing]] — Treasury yields and the
  VIX through QE
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — joint
  crash probabilities for stocks and bonds: the tail version of the bond-beta question
