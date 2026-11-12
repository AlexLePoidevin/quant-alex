# Static Replication of European Standard Dispersion Options

| | |
|---|---|
| **Authors** | Sébastien Bossu (NYU Courant); Peter Carr (NYU Tandon); Andrew Papanicolaou (North Carolina State University) |
| **Year** | 2022 (*Quantitative Finance* 22(5), 799–811; this preprint dated 1 March 2021) |
| **Type** | Journal paper (preprint version, 21pp). Theory with one numerical example |
| **PDF** | Not hosted in this repository (journal article, no open licence). The download was misnamed "Options on Realized Variance and Convex Orders" |
| **Find it** | [doi.org/10.1080/14697688.2022.2040743](https://doi.org/10.1080/14697688.2022.2040743) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Static+Replication+of+European+Standard+Dispersion+Options%22+Bossu) |
| **BibTeX** | `bossu2022dispersion` |
| **Status** | Reference: §1.2 (main result), Proposition 1 (the dispersion call), §6 (worked example) and §8 (pricing consequences) |

## What it is

A multi-asset version of the classic result that any payoff on one asset can be built from
a continuum of calls and puts on that asset (Breeden–Litzenberger; Carr–Madan).

- **The instrument.** A "standard dispersion" option pays a function of how spread out a
  group of assets' performances are, measured as the Euclidean length of the vector of
  performances. A dispersion call pays the amount by which that length exceeds a strike.
  Industry contracts usually use mean absolute deviation instead; the paper uses the
  Euclidean version because the maths is tractable and leaves the other for later work.
- **The result.** Any such payoff that is smooth enough can be replicated exactly by a
  continuous portfolio of ordinary basket calls, one for every possible set of basket
  weights, including negative weights (long–short baskets). The quantities come from
  solving an integral equation with Radon-transform and fractional-calculus tools.
  Closed forms are given for the dispersion call, the zero-strike dispersion call and the
  dispersion put.
- **A technical fix.** The general solution needs the payoff's slope at zero to be zero.
  The authors isolate the first-order term and show it can be replicated with zero-strike
  basket calls, which removes the restriction.
- **Worked example.** A two-asset "Mexican hat" straddle (payoff one minus a Gaussian bump
  in the dispersion) is replicated numerically, with the weights plotted.
- **The pricing consequence.** If prices of basket calls are known for all weights, a
  dispersion option has a model-free price enforced by arbitrage. The authors argue it
  should therefore be priced with the same model as basket calls, not with a separate
  stochastic-correlation model. They accept that binary basket calls and negative weights
  in the replicating portfolio may still justify practical adjustments.

## Why it's in the library

**It ties dispersion to correlation.** A dispersion call is short correlation: when assets
move together their performances bunch up and dispersion falls. The paper shows that this
exposure is entirely determined by basket option prices, which are themselves prices of
correlation.

**It extends the strip-of-options idea used throughout the section.** The variance swap,
the VIX and many static hedges rest on building a payoff from vanilla options on one
asset. This is the step to many assets.

**It is theory, not a trading recipe.** Basket calls on arbitrary long–short weights do not
trade, so the replication is a statement about consistency of prices, not a hedge anyone
can put on.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — VIX
  products, the best-known instruments built on single-asset option replication
- [[ang-chen-2002]] — stock correlations rise in down markets, the risk a short-correlation
  dispersion position carries
- [[jacquier-slaoui-2010-variance-dispersion-and-correlation-swaps]] — dispersion and correlation swaps priced with volga
- [[avellaneda-2009-dispersion-trading]] — dispersion trading in practice
