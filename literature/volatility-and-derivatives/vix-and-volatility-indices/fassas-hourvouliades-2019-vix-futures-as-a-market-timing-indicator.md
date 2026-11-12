# VIX Futures as a Market Timing Indicator

| | |
|---|---|
| **Authors** | Athanasios P. Fassas and Nikolas Hourvouliades (American College of Thessaloniki) |
| **Year** | 2019 (published version); the copy here is the SSRN working paper (3189502) dated 3 June 2018 |
| **Type** | Journal article, *Journal of Risk and Financial Management* 12(3), 113 (2019). Data: January 2010 – December 2017 |
| **PDF** | Not hosted in this repository (SSRN working paper). The published version is open access under CC BY at [mdpi.com/1911-8074/12/3/113](https://www.mdpi.com/1911-8074/12/3/113) |
| **Find it** | [doi.org/10.3390/jrfm12030113](https://doi.org/10.3390/jrfm12030113) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22VIX+Futures+as+a+Market+Timing+Indicator%22+Fassas) |
| **BibTeX** | `fassas2019timing` |
| **Status** | Reference: Exhibits 3 and 4 carry the results |

## What it is

A test of the common trader's rule that an inverted VIX futures curve marks an oversold
stock market.

- **Measuring the curve.** Each day the authors fit a straight line through spot VIX (as
  maturity zero) and the seven nearest VIX futures. The slope is the term-structure
  measure. Over 2010–2017 it averaged +2.3 vol points per year (contango), was inverted
  repeatedly in 2010–2011 and in August 2015, and never inverted in 2017.
- **Regression on future returns.** S&P 500 returns over the next day, week, month and
  quarter are regressed on the slope, split into its positive and negative parts, with
  Newey–West errors for the overlapping windows. The negative part matters: the more
  inverted the curve, the higher the later return (coefficient −0.17 for one day rising to
  −1.18 for one quarter; not significant at one month). The positive part is never
  significant: ordinary contango says nothing. R² is 1% to 3.5%.
- **Percentile buckets.** Ranking each day's slope against its own past into 20
  buckets gives the same picture. The most inverted 5–20% of days are followed by
  significantly higher returns at every horizon.

## Why it's in the library

**It puts a number on a widely used contrarian signal.** Backwardation in VIX futures is
the market paying up for near-term protection. This paper finds that, after the fact,
those were usually good times to own stocks rather than the start of a bigger fall.

**The evidence comes from one bull market.** 2010–2017 had no bear market, so "buy when
the curve inverts" was always rewarded; 2008 or 2022 could look very different. There are
few inversion episodes, the long-horizon windows overlap heavily, and there is no
out-of-sample test or trading rule with costs. Some bucket coefficients are implausibly
large for one day (2.4% after the most inverted days). Treat it as a description of
2010–2017.

## Links

- [[farooqui-2020-a-note-on-trading-the-term-structure-of-vix-futures]] — a term-spread
  switching strategy built on the same curve, with similar caveats
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  a model of the VIX futures curve and how often it inverts
- [[fassas-2017-tracking-the-vix]] — the same author on why VIX futures and ETPs do not
  follow spot VIX
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bull corrections and
  bear rallies, the market states this signal is trying to tell apart
