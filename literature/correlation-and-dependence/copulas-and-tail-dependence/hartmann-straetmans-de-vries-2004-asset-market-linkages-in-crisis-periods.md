# Asset Market Linkages in Crisis Periods

| | |
|---|---|
| **Authors** | Philipp Hartmann (ECB), Stefan Straetmans (Maastricht), Casper G. de Vries (Erasmus Rotterdam) |
| **Year** | 2004 |
| **Type** | Journal article, *Review of Economics and Statistics* 86(1), 313–326. Weekly G-5 stock and government bond index returns, 1987–1999. An earlier version circulated as an ECB working paper (2001) |
| **PDF** | Local copy only (published version, © President and Fellows of Harvard College and MIT) |
| **BibTeX** | `hartmann2004linkages` |
| **Status** | Reference: §II (the linkage measure), Tables 1–3 and §VI carry the argument; the copy is an image scan |

## What it is

A measure of how likely markets are to crash together, built from extreme-value theory
rather than from correlations.

- **The question.** If one market crashes, how many others crash with it? The paper's
  measure is the expected number of markets in extreme loss given that at least one is,
  E[κ | κ ≥ 1]. With two markets this is 1 plus the probability that both crash given
  that one does.
- **Why not correlations.** Correlations computed on calm data, or on data conditioned on
  a selloff, are biased and tied to the normal distribution. Under a bivariate normal,
  extreme events become independent in the limit, so correlation-based estimates
  understate joint crashes badly.
- **The method.** The linkage is estimated nonparametrically from the tail dependence
  function of multivariate extreme-value theory, so no distribution for returns has to be
  assumed. Crash thresholds are set near the worst weekly moves in the sample: −15% and
  −20% for stocks, −6% and −8% for government bonds.
- **Single-market tails.** A 20% weekly fall in US stocks is estimated to happen about
  once every 39 years; a normal distribution would put it at once in 31.5 × 10²⁰ years.
  A weekly 8% fall in US Treasuries is put at about once in 30 years.
- **Stock–stock linkages are stronger than bond–bond ones.** For Germany and the US, about
  1 in 6 stock crashes of 20% is expected to be a joint crash, but only 1 in 13 bond
  crashes of 6%. Germany–France is the most tightly linked pair.
- **Crashes together versus flight to quality.** A stock crash coinciding with a bond
  crash is about as likely as a stock crash coinciding with a bond rally. In 23 of 25
  tests the two are statistically indistinguishable, even though full-sample stock–bond
  correlations are mostly positive.
- **Borders don't matter much.** Cross-border stock–bond linkages are about as strong as
  domestic ones. US Treasuries act as a safe haven for European stock crashes more than
  the reverse: a French stock crash coincides with a US bond rally 7.7% of the time,
  against 3.0% the other way round.

## Why it's in the library

**It measures the thing a crisis question actually asks.** The quantity is the chance
that a second market crashes once one has, in units an investor can use. That is a
different object from a correlation coefficient, and the paper shows the two can point in
opposite directions for stock–bond pairs.

**The normal distribution is not a rough approximation in the tails; it is wrong by
orders of magnitude.** The 39-year versus 10²⁰-year comparison is a vivid reminder of why
tail dependence needs its own tools.

**It tempers contagion stories.** Joint crashes are far more likely than a normal model
says, but conditional probabilities rarely exceed about 20%. Flight to quality is as
common as joint crashes, which limits how far a crisis spreads across asset classes.

**Limits.** Weekly data over 1987–1999 contain few genuine crashes, so the tail estimates
rest on a handful of events. The authors note a small-sample upward bias in the linkage
estimator. The sample ends before 2000, 2008 and 2020, when stock–bond behaviour changed.

## Links

- [[ang-chen-2002]] — correlations rise in down markets: the correlation-based view of the
  same asymmetry this paper measures with tail dependence
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — what goes wrong when a model assumes
  away tail dependence
- [[munnix-schafer-2011-copula-dependencies]] — time-varying dependence between US stocks
  measured with copulas
- [[nelsen-2006-introduction-to-copulas]] — the copula and tail-dependence background
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — the Gaussian copula, a
  dependence model with no tail dependence, in practice
- [[baur-mcdermott-2013-financial-turmoil-and-safe-haven-assets]] — Treasuries and gold compared as havens on the worst stock market days
- [[deng-bao-gong-2018-increased-tail-dependence-in-global-public-real-estate-markets]] — the same crash co-movement question for listed real estate, before and after 2008
- [[garcia-feijoo-jensen-johnson-2012-the-effectiveness-of-asset-classes-in-hedging-risk]] — joint extreme months across stocks, bonds, gold, commodities and REITs, 1970–2010
- [[kinlaw-et-al-2021-the-myth-of-diversification-reconsidered]] — how to measure downside correlation without discarding the months diversification worked
- [[page-panariello-2018-when-diversification-fails]] — conditional (tail) correlations with US stocks for a wide set of risk assets: a practitioner view of crisis linkages
- [[smales-2022-spreading-the-fear-the-central-role-of-vix-in-global-uncertainty]] — the same crisis co-movement in implied-volatility indices, with the US VIX leading
- [[soper-2015-vix-and-us-treasuries-during-quantitative-easing]] — a simple monthly regression of Treasury yields on the VIX, 2005–2015: the flight-to-quality co-movement over the QE years
- [[van-oordt-zhou-2014-systemic-risk-and-bank-business-models]] — the same extreme-value machinery applied bank by bank: tail beta to the financial sector
