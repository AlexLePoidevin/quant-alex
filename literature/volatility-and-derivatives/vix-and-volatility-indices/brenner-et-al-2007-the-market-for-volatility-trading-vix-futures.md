# The Market for Volatility Trading; VIX Futures

| | |
|---|---|
| **Authors** | Menachem Brenner (NYU Stern), Jinghong Shu (UIBE Beijing), Jin E. Zhang (University of Hong Kong) |
| **Year** | 2007 (working paper, May 2007; first version August 2006). Published as Zhang, Shu and Brenner, "The New Market for Volatility Trading", *Journal of Futures Markets* 30(9), 2010 |
| **Type** | Working paper, 31pp. Data: daily VIX and VIX futures, March 2004 to November 2006 |
| **PDF** | Local copy only (author upload to ResearchGate, no open licence) |
| **BibTeX** | `brenner2007vixfutures` |
| **Status** | Reference: §3 (three stylised facts) and §4 (the model and its calibration) |

## What it is

An early study of VIX futures, which started trading on 26 March 2004, written when the
market was two and a half years old.

- **Why there is no cost-of-carry formula.** The VIX is not a traded asset, so a VIX future
  cannot be replicated with the index and cash. Its price has to come from a model or
  from the market.
- **Three stylised facts (2004–2006).**
  1. The VIX and the 30-, 60- and 90-day futures are almost perfectly correlated with each
     other and negatively correlated with the S&P 500.
  2. The futures term structure slopes up on average: VIX (×10) averaged 135.5 against
     144.8, 152.8 and 157.8 for 30-, 60- and 90-day futures, meaning volatility was below
     its long-run level for most of the sample.
  3. The futures' own volatility falls with maturity: 84.4% for the VIX index against
     35.7%, 30.0% and 25.8% for the 30-, 60- and 90-day futures. Mean reversion means
     long-dated futures move less.
- **The model.** Instantaneous variance follows a square-root mean-reverting (Heston/CIR)
  process. VIX² is then a weighted average of the long-run variance and today's variance.
  The futures price is the expected square root of that quantity, which has a closed form
  and a fast Taylor approximation. Spot–volatility correlation does not enter the VIX
  formula, so the VIX says nothing about skewness.
- **Fit.** Parameters estimated from the VIX history alone price futures with a root mean
  squared error of 10–15%. Calibrating each day to the futures term structure brings
  next-day pricing error to about $2.3, under 2% of an average futures price near 150.
  The estimated market price of variance risk is negative, consistent with a variance
  risk premium.
- **Volatility term structure explained.** The model's hedge ratio of futures to spot VIX
  falls with maturity, which reproduces the downward-sloping volatility of futures prices.

## Why it's in the library

**It explains why VIX futures do not track the VIX.** A VIX future is the expected VIX at
expiry, pulled towards the long-run mean. Long-dated futures react much less than spot to
a volatility spike. Anyone holding VIX futures as a hedge gets far less than the headline
moves in the index.

**The upward-sloping curve is the cost of carry for long volatility.** The contango
documented here is what makes a rolling long VIX futures position lose money in calm
markets, the drag measured in the tail-hedging notes.

**It is an early, short sample.** Two and a half years of a thin, new market (average open
interest about 2,800 contracts per expiry), with no crisis in the sample. The term
structure inverts in stress, which this data never shows.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  long-run cost of the contango described here, for a portfolio holding VIX futures
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the index
  underneath the futures is computed and settled
- [[dupire-2006-model-free-results-on-volatility-derivatives]] — a model-free upper bound on
  VIX futures prices, where this paper uses an explicit model
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — why
  VIX² is a variance swap rate
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] — a two-factor model of the whole VIX futures curve
- [[karagiannis-2014-lead-lag-relationship-between-the-vix-and-vix-futures]] — whether VIX futures or the spot index move first (futures lead, on daily data)
