# A TIPS Scorecard: Are TIPS Accomplishing What They Were Supposed to Accomplish? Can They Be Improved?

| | |
|---|---|
| **Authors** | Michelle L. Barnes, Robert K. Triest, J. Christina Wang (Federal Reserve Bank of Boston), Zvi Bodie (Boston University) |
| **Year** | 2009 (version of September 2009) |
| **Type** | Federal Reserve Bank of Boston Public Policy Discussion Paper No. 09-8 (SSRN 1520569), 55pp. A shorter version was published as "A TIPS Scorecard: Are They Accomplishing Their Objectives?", *Financial Analysts Journal* 66(5), 2010, 68–84 |
| **PDF** | Not hosted in this repository (discussion paper with no open licence; the Boston Fed is not a federal agency, so its papers are not US-government works) |
| **Find it** | [doi.org/10.2139/ssrn.1520569](https://doi.org/10.2139/ssrn.1520569) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22A+TIPS+Scorecard%3A+Are+TIPS+Accomplishing+What+They+Were+Supposed+to+Accomplish%3F+Can+They+Be+Improved%3F%22+Barnes) |
| **BibTeX** | `barnes2009tips` |
| **Status** | Reference: §III.B (CPI bias as basis risk, Table 1), §III.C (alternative price indexes, Tables 2–3) and §IV (long vs short holding periods, Figures 9–15) carry the argument |

## What it is

A policy review of US Treasury Inflation-Protected Securities (TIPS) twelve years after
launch, asking whether they deliver what the Treasury designed them for: a real-return
hedge, a hedge for nominal contracts, and a market reading of expected inflation.

- **CPI bias matters only if it moves.** The 2008 popular critique was that the CPI
  understates "true" inflation (substitution adjustments, hedonic quality adjustment,
  owners' equivalent rent), so TIPS under-protect. The paper's point: a constant bias can
  be offset by holding a little more or less TIPS; what creates basis risk is *time
  variation* in the bias, and it needs a premium only if that variation co-moves with priced
  risk factors.
- **It doesn't, measurably.** The gap between CPI-U and chained CPI (a proxy for the
  remaining substitution bias, about 0.38 points a year on average) has an insignificant
  market beta (0.0013, s.e. 0.0016). A longer PCE-based proxy has a significant but
  economically tiny market loading that disappears once SMB and HML are added.
- **Other price indexes barely differ.** Over 1983–2009 (chained CPI from 2000), CPI-W
  (wage earners), CPI-E (the elderly), chained CPI and the PCE deflator have 12-month
  inflation correlations of 0.89–0.99 with CPI-U; the GDP deflator is lower at 0.74. CPI-E
  ran about 0.3 points a year higher over 1982–2007 (medical care and shelter). The inflation gaps between CPI-U and CPI-W or CPI-E carry no
  significant loading on the market, size or value factors. So retirees indexed to CPI-U
  bear little systematic risk, and issuing TIPS on narrower indexes (by region or
  demographic) would fragment liquidity for little gain.
- **Held to maturity, TIPS remove a large risk.** Ex post real yields on 10-year Treasuries
  bought in the early 1970s were negative, and above 10% for notes bought in the early
  1980s, because 10-year inflation forecasts missed by more than 5 points a year at the
  peak. Ex ante real yields stayed in a narrow band. A TIPS bought at issue and held to
  maturity locks in the ex ante real yield.
- **Held for a year, TIPS are a poor inflation hedge.** The one-year real return on a TIPS
  bought six years before maturity is almost as volatile as a nominal Treasury's, because
  the same shocks that move inflation move real yields.
- **Breakevens are not inflation forecasts.** The nominal–TIPS yield gap also contains an
  inflation risk premium and liquidity, convexity and tax differences, so it should not be
  read as expected inflation.
- **Recommendations.** Keep indexing to CPI-U, extend TIPS maturities (useful for
  inflation-indexed annuities and retirement ladders), and leave house-price risk to
  separate instruments such as Case–Shiller futures.

## Why it's in the library

**It defines what an inflation hedge is, precisely.** The useful distinction is between
level bias (harmless) and time-varying basis risk correlated with priced factors (costly),
and between horizon-matched holding (a near-perfect real hedge) and short holding (mostly
real-rate risk). Both carry over to any "inflation-protected" asset or strategy.

**It is the reference point for TIPS as a safe asset.** TIPS protect a buy-and-hold real
liability; they are not a short-run hedge against an inflation surprise in a portfolio
marked to market. That is the gap the inflation-regime papers in this library try to fill
with commodities and trend.

**Caveats.** The factor tests use short series (chained CPI only from 2000) and monthly
data assuming monthly inflation accrual; the paper itself says the bias estimates are
uncertain. It predates the post-2021 inflation, the real test of the TIPS market.

## Links

- [[aqr-2020-fire-and-ice-inflation-and-deflation]] — how stocks, bonds and other assets
  behave in inflation and deflation surprises, and why nominal bonds hedge only one of the
  two
- [[neville-et-al-2021-the-best-strategies-for-inflationary-times]] — what actually held up
  in high-inflation regimes since 1926 (commodities and trend; nominal bonds and equities
  lost in real terms)
- [[feldstein-1978-the-effect-of-inflation-on-the-prices-of-land-and-gold]] — unindexed
  taxation as the channel through which inflation reprices real assets against bonds
- [[keerati-2020-the-impact-of-monetary-policy-on-the-specialness-of-us-treasuries]] — the
  convenience premium on Treasuries, one of the non-inflation terms inside breakevens
