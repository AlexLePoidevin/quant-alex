# Asymmetric Linkages among the Fear Index and Emerging Market Volatility Indices

| | |
|---|---|
| **Authors** | Ihsan Badshah, Stelios Bekiros, Brian M. Lucey, Gazi Salah Uddin |
| **Year** | 2018 (*Emerging Markets Review* 37, 17–31) |
| **Type** | Journal article; this copy is the Elsevier accepted manuscript, 37pp, which lists only Lucey as author (a known production error flagged on its cover page). Daily data, 16 March 2011–16 January 2016 |
| **PDF** | Not hosted in this repository (Elsevier accepted manuscript, no open licence stated) |
| **Find it** | [doi.org/10.1016/j.ememar.2018.03.002](https://doi.org/10.1016/j.ememar.2018.03.002) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Asymmetric+Linkages+among+the+Fear+Index+and+Emerging+Market+Volatility+Indices%22+Badshah) |
| **BibTeX** | `badshah2018fear` |
| **Status** | Reference: §4 (quantile regressions, Tables 2–4) and the time-varying copula results (Table 6, Figures 2–4) |

## What it is

A study of how shocks to the US "fear index" (VIX) pass to option-implied volatility in
emerging markets: the Cboe emerging-markets ETF index (VXEEM), China (VXFXI) and Brazil
(VXEWZ), all launched on 16 March 2011 and computed the same way as the VIX from ETF options.

- **Method.** Quantile regressions of daily changes in each emerging-market volatility index
  on the same-day and lagged VIX change and the absolute VIX change, at quantiles from 5% to
  95%, compared with OLS. Then GJR-GARCH-filtered series fed to time-varying copulas
  (Normal, Student-t, Gumbel and rotated Gumbel, and symmetrised Joe–Clayton) to see how the
  dependence, and its tails, change over time.
- **Findings.**
  - The link is mostly same-day: the contemporaneous VIX effect is about three times (up to
    five for Brazil) the one-day-lagged effect.
  - It is strongest in the upper quantiles, when emerging-market volatility is jumping.
  - It is asymmetric: at the 95% quantile a rise in the VIX moves emerging volatility about
    twice as much as a fall (three times for China), and the effect there is about eight
    times what OLS reports.
  - The broad emerging-markets index is most tied to the VIX, then China, then Brazil;
    Chinese implied volatility shows the biggest gap between responses to VIX rises and falls.
  - The copula dependence varies over time, with the rotated Gumbel fitting best.
- **Context in the sample.** The August 2015 Chinese sell-off took VXFXI to 58%, VXEEM to
  55%, VXEWZ to 52% and the VIX to 40% on the same day.

## Why it's in the library

It is a clean measurement of one part of risk-on/risk-off: volatility shocks travel from the
US to emerging markets fast and asymmetrically, and the transmission is strongest exactly when
it matters. The quantile approach is the point, since an average (OLS) relationship understates
the tail response many times over. Limits: under five years of data, one dominant direction
assumed (US to emerging), and Granger tests reported only in robustness; nothing is said about
trading on the link.

## Links

- [[ang-chen-2002]] — asymmetric correlations in down markets, the same pattern in equity
  returns rather than volatility
- [[munnix-schafer-2011-copula-dependencies]] — copulas for dependence that changes with
  market conditions
- [[nelsen-2006-introduction-to-copulas]] — the copula families (Gumbel, Clayton) used here
- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — risk-off episodes
  dated from switches in FX correlation regimes
- [[cboe-2021-vix-index-white-paper]] — how the VIX and its ETF-based relatives are calculated
