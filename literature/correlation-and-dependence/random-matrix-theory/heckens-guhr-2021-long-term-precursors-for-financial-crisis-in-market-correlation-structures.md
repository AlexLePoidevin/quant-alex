# A New Attempt to Identify Long-term Precursors for Financial Crisis in the Market Correlation Structures

| | |
|---|---|
| **Authors** | Anton J. Heckens, Thomas Guhr (University of Duisburg–Essen) |
| **Year** | 2021 |
| **Type** | Working paper, arXiv 2107.09048 (q-fin.RM), 22pp. Daily returns on 250 US stocks, 1997–2012 |
| **PDF** | `heckens-guhr-2021-long-term-precursors-for-financial-crisis-in-market-correlation-structures.pdf` (arXiv version) |
| **BibTeX** | `heckens2021precursors` |
| **Status** | Reference: §III (reduced-rank correlation matrices) and §IV (the snapshot analysis around 2000 and 2008) carry the paper |

## What it is

A physicists' search for early-warning signs of crises in how stock correlations are
structured, after removing the market as a whole.

- **Reduced-rank correlations.** In a stock correlation matrix the largest eigenvalue is
  the market moving together. The authors subtract that market component and study what
  is left: correlations within and between industry sectors, measured relative to the
  market. Two versions are built, one from covariances and one from correlations.
- **Market states.** Correlation matrices are computed on non-overlapping two-month
  windows (42 trading days) and grouped with k-means clustering. Each cluster is a
  "market state", a correlation structure the market sits in for a while before moving
  on. With the market removed, the states are more stable, sometimes lasting years.
- **Snapshots using only past data.** To test for precursors, the clustering is rerun
  with windows added one at a time up to a crisis, so no post-crisis data are used.
- **Lehman.** A transition into a new "crisis" state appears around mid-2007, when the
  interbank market froze. That is about three windows (half a trading year) before the
  Lehman collapse.
- **Dot-com.** No transition appears before the bubble burst; the structural change
  shows up two to four windows after it.
- **Mean correlations.** Low points in the mean reduced-rank correlation mark the start
  of both crisis periods. The authors read the build-up afterwards as endogenous risk
  passing between sectors. The IT sector in 2000 and financials in 2007–08 become
  anti-correlated with the rest of the market.

## Why it's in the library

**It shows what is left in a correlation matrix once the market mode is removed.** The
sector structure under the first eigenvector carries information about stress that the
average correlation hides, and it changes more slowly.

**The precursor evidence is thin, and the authors say so.** Two crises, one detected
early and one only after the fact. 250 stocks chosen to survive the whole period, and
no false-alarm rate: there is no test of how often a state transition happens without a
crisis following. Treat it as a candidate indicator to study, not a signal.

## Links

- [[laloux-et-al-1999]] — which eigenvalues of a correlation matrix are signal and which
  are noise
- [[plerou-et-al-2002]] — the market mode and sector modes in US stock correlations
- [[mantegna-1999]] — hierarchical sector structure recovered from correlations
- [[munnix-schafer-2011-copula-dependencies]] — the same group's line of work on
  time-varying dependence between US stocks
