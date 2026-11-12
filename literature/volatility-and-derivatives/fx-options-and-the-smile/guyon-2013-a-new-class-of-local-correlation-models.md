# A New Class of Local Correlation Models

| | |
|---|---|
| **Authors** | Julien Guyon (Quantitative Research, Bloomberg LP) |
| **Year** | 2013 (first version February 2013; this version 21 June 2013) |
| **Type** | Working paper (SSRN), 36pp |
| **PDF** | Not hosted in this repository (working paper with no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22A+New+Class+of+Local+Correlation+Models%22+Guyon) for the title and authors |
| **BibTeX** | `guyon2013local` |
| **Status** | Reference: §2–§5 (the representation and the particle method) and §10 (the FX numerics) carry the content |

## What it is

A way to build multi-asset models whose correlation depends on where the prices are, while
still matching the option smile of a basket exactly. The worked case is the FX triangle:
EUR/USD and GBP/USD each have a smile, and so does the cross EUR/GBP, so the correlation
between the two USD rates is pinned down by three markets at once.

- **The problem.** Banks price multi-asset products with a local volatility for each asset
  and a correlation matrix. A constant correlation fitted at the money gives an index skew
  roughly half the market's. The basket smile carries information that correlation is
  higher in sell-offs, which only a state-dependent ("local") correlation can reproduce.
- **Admissible correlations.** A local correlation is admissible if the model reprices the
  basket's (here, the cross rate's) whole smile. The paper gives the exact condition: a
  conditional expectation of the model's cross variance, given the cross rate, must equal
  the market's local variance of the cross.
- **The new family.** Pick two functions a and b of time and prices, and require that
  a + bρ depend only on the cross rate. Every admissible correlation can be written this
  way. The two models already in the literature are special cases: correlation itself
  local in the cross (a = 0, b = 1; Reghai, Guyon–Henry-Labordère), and cross variance
  local in the cross (Langnau). A third natural case makes the covariance local in the
  cross.
- **Calibration by particle method.** Simulate many paths forward. At each time step,
  estimate the needed conditional expectations with kernel regression across the
  particles, and set the correlation from them. If a candidate leaves [−1, 1], cap it and
  check how much of the smile is lost.
- **Numerics, FX triangle, March 2012 data.** USD is the domestic currency and rates are
  set to zero. Choosing b = (S¹S²)^α produces a negative correlation skew. A larger α
  gives a steeper skew, until correlations must be capped: 0.3% of simulated spots in one
  case, 0.5% for the local-covariance model, and 22% and 16% for two badly chosen (a, b)
  pairs, which then misfit the cross smile.
- **Prices are far from pinned down.** With all three smiles fitted exactly, a min-of-calls
  option ranges from 2.37 to 2.91 across admissible correlations. The highest and lowest
  prices come from the local-covariance model and a deliberately extreme correlation. The
  paper reads this as a partial answer to the bounds on multi-asset prices given the
  three smiles.
- **Extensions.** The same construction works with local stochastic volatility,
  stochastic rates and dividends. Applied to a single asset, it builds path-dependent
  volatility models that still fit the smile.

## Why it's in the library

**It shows how much a fitted smile leaves undetermined.** Three exactly calibrated smiles
still leave a range of more than 20% in the price of a simple two-asset option. Correlation is the
free parameter, and the choice of model decides the price.

**It ties correlation to the price level.** The paper's motivation is that correlation is
higher when markets fall. Building that into the model also builds it into the delta
hedge, so a desk short correlation is not caught by a correlation jump in a crisis.

**The FX triangle is the clean test case.** In FX, the cross-rate smile is a traded
market, so the implied correlation between two rates is observable. That is rarely true
in equities or rates.

**It is a method paper, not an empirical one.** The numerics illustrate one day of data
and a handful of choices of (a, b). Whether a solution exists in general is left open.

## Links

- [[ang-chen-2002]] — correlations between US stocks rise in down markets, the empirical
  pattern a local correlation is built to capture
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — a correlation assumption that held
  in calm markets and failed in the tail
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — a single correlation number
  used as the market's price for dependence
