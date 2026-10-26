# The Minimum Correlation Algorithm: A Practical Diversification Tool

| | |
|---|---|
| **Authors** | David Varadi (Flexible Plan Investments); Michael Kapler, MMF, CFA; Henry Bee; Corey Rittenhouse |
| **Year** | September 2012 |
| **Type** | Working paper, 91pp — CSS Analytics |
| **PDF** | `varadi-et-al-2012.pdf` (in this folder) |
| **BibTeX** | `varadi2012mincorr` |
| **Status** | Read in part |

## What it is

A heuristic portfolio construction method that sizes positions by how much each asset
diversifies the rest, without solving an optimisation. Two variants, `Mincorr` and
`Mincorr2`. The procedure normalises the correlation matrix, computes a **rank-weighted
average normalised correlation** for each asset, and then weights proportionally to the
*lowest* average correlations, re-levered to 1. A risk-parity multiplier follows, sizing
each asset by the inverse of its volatility.

The authors' claim is that this is "an excellent alternative to Risk Parity, Minimum
Variance and Maximum Diversification," on three grounds: speed of computation, robustness
to estimation error, and superior risk dispersion.

The rank-weighting is the part that matters. Raw average correlation is unstable and can
be negative; ranking before averaging makes the input ordinal, which is what buys the
robustness. This is the same reasoning that makes inverse volatility survive a finite
sample while full risk parity does not — the method is chosen for the stability of its
inputs, not for optimality.

## Why it's in the library

**It is the documented ancestor of Optimum3's second stage.** Allocate Smartly describes
that strategy's selection step as "akin to Varadi's Minimum Correlation algorithm," and
this is the paper. Optimum3's own rules are not public; this one is.

**But the two differ in a way worth being precise about.** Varadi's algorithm is a
*weighting* scheme: every asset stays in the portfolio and receives a weight inversely
related to its average correlation. Optimum3 applies the same objective at the *selection*
stage instead — it takes the three lowest-average-correlation assets and equal-weights
them, never touching the weights at all. Same objective function, different decision
variable. The distinction is the whole reason Optimum3 behaves differently from an
ordinary minimum-correlation portfolio.

**The inverse-volatility multiplier is the bridge to the rest of this folder.** Mincorr
ends by sizing on 1/σ, which is the same risk-contribution argument that makes inverse
volatility work at all.

## Links

- [[optimum3]] — the strategy that applies this objective as a selection rule
- [[ledoit-wolf-2004]] — the other response to unstable correlation estimates: shrink the
  matrix rather than replace it with ranks
- [[meucci-2009]] — diversification measured in the eigenbasis, the optimisation-based
  alternative this paper positions itself against
