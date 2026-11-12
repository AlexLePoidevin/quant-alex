# An Investigation of the Lead-Lag Relationship between the VIX Index and the VIX Futures on the S&P 500

| | |
|---|---|
| **Authors** | Sotirios Karagiannis (University of Peloponnese) |
| **Year** | 2014 (*Journal of Science, Innovation and New Technology* 1(11), November 2014, pp. 42–52; earlier SSRN 2498081). The source file is labelled 2019 |
| **Type** | Journal article, 11pp. Daily data, 26 March 2004 – 16 April 2012 (2,029 days) |
| **PDF** | Not hosted in this repository (journal copy, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22An+Investigation+of+the+Lead-Lag+Relationship+between+the+VIX+Index+and+the+VIX+Futures+on+the+S%26P+500%22+Karagiannis) for the title and authors |
| **BibTeX** | `karagiannis2014vix` |
| **Status** | Reference: §4 (Johansen test, VECM, Granger causality) carries the result |

## What it is

A textbook time-series exercise on whether the front-month VIX future or the spot VIX index
moves first.

- **Setup.** Daily closes of the spot VIX and the front-month VIX future. Both are I(1) by
  ADF tests, so the author fits a VAR (3 lags by the Schwarz criterion), tests for
  cointegration, and estimates a vector error-correction model.
- **Cointegration.** One cointegrating relation: futures ≈ 0.936 × spot + 1.65.
- **Error correction.** The futures equation's error-correction coefficient is −0.097
  (t ≈ −4.9); the spot equation's is 0.061 (t ≈ 2.2). Both adjust, the futures more
  strongly.
- **Granger causality.** Lagged futures changes help predict spot changes; lagged spot
  changes do not help predict futures changes. The author concludes that VIX futures lead
  the index and dominate price discovery, in line with Shu and Zhang (2012).

## Why it's in the library

It is a clean worked example of the standard lead–lag toolkit (unit roots, Johansen,
VECM, Granger) applied to the VIX, and its answer agrees with the stronger intraday study
filed next to it.

Its limits are worth knowing:

- **Spot VIX is not tradable**, and its daily close is computed from option quotes rather
  than trades. A smoothed or stale index will "lag" a liquid future mechanically, so
  Granger causality here says little about where information arrives.
- **The model fails its own diagnostics.** The author reports that the VAR residuals are
  serially correlated and non-normal and that the relation seems to change after 2008, but
  keeps the specification.
- **Daily data** cannot resolve a lead that, in liquid markets, plays out over minutes.

## Links

- [[chen-tsai-2017-determinants-of-price-discovery-in-the-vix-futures-market]] — the same
  question with five-minute data and information shares: futures account for about 70–75%
  of price discovery
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — the early VIX
  futures market and how futures relate to spot
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the spot
  index is computed from option quotes, the reason it is not a traded price
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] — a
  model of the whole futures curve rather than just the front month
