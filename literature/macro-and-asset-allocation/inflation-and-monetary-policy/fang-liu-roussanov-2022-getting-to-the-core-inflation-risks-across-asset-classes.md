# Getting to the Core: Inflation Risks Within and Across Asset Classes

| | |
|---|---|
| **Authors** | Xiang Fang (HKU), Yang Liu (HKU), Nikolai Roussanov (Wharton, NBER) |
| **Year** | 2022 (the copy is the January 2022 SSRN draft; first version August 2020) |
| **Type** | Working paper, 91pp; later published in *The Review of Financial Studies* 39(3), 702–743 (online July 2025), doi:10.1093/rfs/hhaf050. Also NBER WP 30169 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `fang2025core` |
| **Status** | Reference: §2.2 (betas), §2.3 and Tables 4–5 (prices of risk), §2.4 (1963–99 vs 2000–19) and the conclusion carry the results; the New Keynesian model (§3) was skimmed |

## What it is

A study of which assets actually protect against inflation once headline CPI is split into
core (CPI less food and energy) and energy. Quarterly data, 1963Q2–2019Q4, eight asset
classes: US stocks, Treasuries, agency bonds, corporate bonds, currency portfolios,
commodity futures, REITs and international stocks (38 test portfolios in all).

- **Two different inflations.** Both average about 4% a year, but core is smooth and
  persistent (standard deviation 2.66% a year, autocorrelation 0.79) while energy is
  volatile and barely persistent (standard deviation 19.5%). Their correlation with each
  other is low.
- **"Real" assets hedge energy, not core.** Stocks and REITs have negative core betas and
  positive energy betas. Currencies and commodity futures load positively on energy and
  slightly negatively (insignificantly) on core. Treasuries and agency bonds lose on both.
  The usual near-zero headline beta of stocks is an average of a reliably negative core
  beta and an energy beta that has turned positive.
- **Only core inflation carries a risk premium.** In Fama–MacBeth tests the headline
  inflation factor is not priced. Split into components, core has a price of risk of about
  −1.03 to −1.07 (t ≈ −2.9 to −3.7): an asset with one more unit of negative core exposure
  earns about 1.07% a year more. Energy's price is positive but insignificant. The core
  price comes out at a similar size within each asset class taken separately (−0.68 to
  −1.26), though several of those single-class estimates are weakly identified.
- **Why the stock–bond correlation flipped.** Before 2000 core inflation dominated, both
  stocks and bonds lost when it rose, and their correlation was positive. After 2000 energy
  inflation dominated and was driven mostly by demand, so stocks gained with it while
  bonds lost, and the correlation turned negative.
- **Not just the Fed.** Around CPI releases (1997–2019), fed funds futures do react to
  core surprises, but stocks' negative response to core inflation survives controlling for
  that change in expected policy.
- **A model to explain it.** A two-sector New Keynesian model in which core inflation comes
  from markup shocks (bad for output, so priced negatively) and energy inflation from
  supply and demand shocks that partly cancel in the risk price.

## Why it's in the library

**It replaces "is X an inflation hedge?" with "a hedge against which inflation?"** The
assets usually sold as inflation protection (commodities, REITs, currencies, equities)
hedge the volatile energy component, not the persistent core component that drives bond
yields and policy. A portfolio "protected" against headline inflation can still be fully
exposed to a core-inflation regime.

**It gives a mechanism for the stock–bond correlation regime.** The positive correlation
of the 1970s–90s and the negative one since 2000 fall out of which inflation component
dominates. That is the same question the stock–bond-correlation folder asks from the
monetary-policy side.

**The cross-sectional fit should be read with its sample in mind.** The R² of 0.98 is on
eight average portfolios and two factors, and the weak-identification tests reject only for
some asset classes. The sign and rough size of the core premium are the robust part.

## Links

- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the monetary-policy account of the same post-2000 sign change in the stock–bond correlation
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — the stock–bond correlation was positive in high-inflation eras, the pattern this paper traces to core inflation
- [[aqr-2021-inflation-outlook-the-macro-the-micro-the-transitory]] — core versus transitory inflation from a practitioner's side
- [[aqr-2020-fire-and-ice-inflation-and-deflation]] — how asset classes behave in inflationary and deflationary regimes
- [[erb-harvey-2013-the-golden-dilemma]] — gold's record as an inflation hedge, another "real" asset tested against inflation
- [[bekaert-engstrom-2010-inflation-and-the-stock-market-the-fed-model]] — why equity yields rise with expected inflation: stagflation raises risk premiums
