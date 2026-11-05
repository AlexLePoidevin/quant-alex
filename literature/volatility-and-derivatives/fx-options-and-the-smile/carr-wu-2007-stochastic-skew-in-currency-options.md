# Stochastic Skew in Currency Options

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg; Courant Institute, NYU), Liuren Wu (Baruch College) |
| **Year** | 2007 (*Journal of Financial Economics* 86(1)) |
| **Type** | Paper, 48pp (accepted-manuscript version) |
| **PDF** | Local copy only (journal article, no open licence) |
| **BibTeX** | `carr2007stochasticskew` |
| **Status** | Reference: §2 (stylised facts of the FX smile), §3 (the model), §5 (in- and out-of-sample results) and §6 (asymmetric and central-tendency extensions) |

## What it is

An empirical study of over-the-counter currency option smiles, and a model built to match
their most awkward feature: a skew that drifts and regularly changes sign.

- **Data.** Over-the-counter quotes on USD/JPY and USD/GBP from January 1996 to January
  2004, sampled weekly. There are eight maturities from one week to 18 months and five
  deltas: the at-the-money straddle, and 10- and 25-delta risk reversals and butterflies.
  That is 16,760 quotes per pair. Quotes are in Garman–Kohlhagen implied volatility at
  fixed delta, the FX market convention.
- **The stylised facts.**
  - **Persistent curvature.** The smile is U-shaped at every maturity and stays curved out
    to a year, so returns stay fat-tailed at long horizons, which i.i.d. returns cannot
    produce.
  - **Moving level.** At-the-money volatility varies a lot over time.
  - **Stable butterflies.** Ten-delta butterflies stay at about 10% of the at-the-money
    volatility.
  - **Volatile risk reversals.** For JPY the ten-delta risk reversal swung from −30% to
    +60% of at-the-money volatility; for GBP from −20% to +20%. The direction of the
    skew switches several times.
  - **Spot moves with the risk reversal.** Currency returns are strongly positively
    correlated with changes in risk reversals, and barely correlated with butterflies.
- **Why standard models fail.** Bates (1996), which adds Merton jumps to Heston stochastic
  volatility, fits the average smile and the moving volatility level. Its skew is set by
  fixed parameters (mean jump size, correlation), so it cannot make the skew wander or flip.
- **The stochastic skew model (SSM).** Write the currency return as the sum of two
  time-changed Lévy processes, one skewed up and one skewed down, each running on its own
  random clock with square-root dynamics. Together the two clocks set the volatility; the
  balance between them sets the skew. The paper links this to buy and sell orders arriving
  separately. Four jump types are tried (from finite-activity Kou-style jumps to
  infinite-activity CGMY-style jumps). Option prices stay in closed form via Fourier
  inversion, and estimation is by maximum likelihood with an unscented Kalman filter.
- **Results.**
  - **In sample.** All four SSMs beat Bates by a wide margin. For JPY the pricing error
    falls from 1.065 to about 0.87 volatility points and the log-likelihood rises by
    2,605–2,685. For GBP the error falls from 0.442 to about 0.39. Vuong tests confirm
    the gap.
  - **Out of sample.** Re-estimated on the first six years and tested on the last two,
    the ranking holds.
  - **Jump type** barely matters, because OTC quotes only span roughly the 10th to 90th
    percentile of the distribution. Higher-frequency jumps help a little for JPY.
- **Extensions.** Letting the two components differ (an asymmetric SSM) cuts the error
  to 0.65 (JPY) and 0.33 (GBP), against 0.89 and 0.42 for the symmetric version on the
  same subsample. The main asymmetry is in how persistent the two clocks are, not how big
  the two sides are. Adding a common, slowly moving long-run level for both clocks (a
  "stochastic central tendency") roughly halves the error again.
- **Caveats in the paper.** Likelihood-ratio tests reject parameter stability between the
  two subperiods for every model, and the inferred market price of volatility risk
  (negative) has large standard errors.

## Why it's in the library

**It is the reference description of what the FX smile does over time.** The facts in §2
(stable curvature, a risk reversal that moves with spot and changes sign) are what any FX
volatility model, or anyone reading risk reversals as a sentiment gauge, has to start
from.

**The model separates three things cleanly.** Volatility (how fast the clocks run), tails
(the Lévy jumps) and skew (the balance between the two clocks) each get their own
component. That makes it a clear template for thinking about skew as a state variable
rather than a fixed parameter.

**The evidence is model-fit evidence.** The comparisons are about pricing quotes within
the sample's range of strikes. They say nothing about hedging performance or tail pricing
beyond the 10-delta wings, and parameter stability is rejected.

## Links

- [[carr-et-al-2003-stochastic-volatility-for-levy-processes]] — the earlier
  time-changed Lévy framework, with a single clock, that this paper extends to two
- [[carr-et-al-2007-time-for-a-change-variance-gamma-model]] — returns as the difference of
  up-jump and down-jump processes, the idea split here onto separate clocks
- [[merton-1976]] — the jump model inside the Bates benchmark
- [[ang-chen-2002]] — asymmetry that changes with the market state, measured in equity
  correlations rather than option skew
- [[brunnermeier-nagel-pedersen-2008-carry-trades-and-currency-crashes]] — the crash risk behind currency skew: carry unwinds when funding tightens
