# The Long-run Relationship of Gold and Silver and the Influence of Bubbles and Financial Crises

| | |
|---|---|
| **Authors** | Dirk G. Baur; Duy T. Tran (University of Technology, Sydney) |
| **Year** | 2014 (this copy: SSRN 2016631, 1 November 2013); published in *Empirical Economics* 47(4), 1525–1541, 2014 |
| **Type** | Empirical time-series paper, 28pp. 499 monthly observations, January 1970 to July 2011 |
| **PDF** | Local copy only (SSRN working paper; journal version is Springer) |
| **BibTeX** | `baur2014goldsilver` |
| **Status** | Reference: §2 (co-integration with and without episode dummies, Tables 2–4), §3 (error-correction models and Granger causality) and §4 (sub-samples) |

## What it is

A replication and extension of Escribano and Granger (1998), asking whether gold and silver
prices are tied together in the long run, and whether bubbles and crises create the tie.

- **The data.** Monthly London gold bullion and silver fix prices from January 1970 to July
  2011. The gold/silver ratio averaged about 55, rising from around 30 in the 1970s to
  around 100 in the early 1990s and then falling. The ratio alone shows the relationship is
  not stable.
- **Episodes.** Four dummy periods: the 1979–80 silver "bubble" (the Hunt brothers' corner,
  September 1979 to March 1980), the 2004–2011 commodity bull run, the 2008–09 crisis
  (August 2008 to February 2009), and 2010–2011.
- **Co-integration.** Regressing the gold price on the silver price gives a stable
  coefficient (0.34 to 0.39) and residuals that look stationary, so prices appear
  co-integrated. But once the episode dummies are allowed to change the slope (interaction
  terms), the evidence for co-integration disappears. In logs there is no co-integration at
  all. The authors' reading: the long-run link is created by the extreme episodes, not by
  normal times.
- **Who leads.** In error-correction models, deviations from the long-run relation are
  corrected mainly through silver, and gold Granger-causes silver but not the reverse. Gold
  drives the relationship despite being less volatile. Nonlinear (cubic) correction terms fit
  better than linear ones, especially in the bubble and bull periods.
- **Sub-samples.** 1970–1990 confirms Escribano and Granger's co-integration; 1990–2011 shows
  weaker evidence, consistent with their prediction that the two markets would separate.

## Why it's in the library

**It is a warning about pairs and ratio trades between related assets.** A co-integration
test on the full sample says gold and silver are tied together; the same test with the
bubble episodes modelled says they are not. A spread trade calibrated on the full sample
would rely on a few extreme periods to supply the mean reversion.

**It shows crises and bubbles changing the dependence between assets.** The link between two
markets is strongest exactly when investors pile into or out of both. That is the same
regime-dependence seen in correlations between stocks in crashes.

**Mostly descriptive, on one pair.** The episode dates are chosen partly by eye from the
price chart, some results are "not reported due to space", and a few error-correction
estimates are only marginally significant. Treat the conclusions as plausible, not settled.

## Links

- [[jarrow-1992-market-manipulation-bubbles-corners-and-short-squeezes]] — how a corner like the Hunt brothers' silver squeeze works and why it distorts prices
- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — the same author on gold's intraday safe-haven behaviour
- [[ang-chen-2002]] — dependence between assets that changes in down markets, the general version of this episode effect
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — calm-period relationships breaking down in stress
