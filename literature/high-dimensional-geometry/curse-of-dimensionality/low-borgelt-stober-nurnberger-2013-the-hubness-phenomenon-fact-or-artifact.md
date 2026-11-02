# The Hubness Phenomenon: Fact or Artifact?

| | |
|---|---|
| **Authors** | Thomas Low; Christian Borgelt; Sebastian Stober; Andreas Nürnberger (Magdeburg; European Centre for Soft Computing) |
| **Year** | 2013 |
| **Type** | Book chapter — in Borgelt et al. (eds.), *Towards Advanced Data Analysis by Combining Soft Computing and Statistics*, Studies in Fuzziness and Soft Computing 285, Springer, pp. 267–278. 12pp |
| **PDF** | Not redistributable (© Springer-Verlag) |
| **BibTeX** | `low2013hubness` |
| **Status** | Reference |

## What it is

A direct challenge to [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]].
Radovanović et al. say hubs are an inherent effect of high dimension. This chapter argues
they are an effect of a **density gradient**, most often the boundary of the region the
data comes from, and that dimension only matters because it makes boundaries bigger.

- **Hubness measures.** Besides the usual skewness of the k-occurrence distribution, it
  proposes two that focus on the hubs themselves: the average k-occurrence of the top q%
  of points, divided by k (h₁), and the share of points that appear in at least βk
  neighbour lists (h₂).
- **Experiment 1: dimension alone isn't enough.** Points sampled from four shapes, up to
  high dimension, averaged over 200 runs:
  - **normal distribution:** strongest hubness (a density gradient everywhere);
  - **cube:** strong hubness from about 15–20 dimensions (gradients at its faces and
    corners);
  - **ball:** much weaker, and it *falls again* beyond about 30–40 dimensions, because
    almost all of a high-dimensional ball's points lie near its surface, i.e. on a sphere;
  - **sphere surface:** no hubness at any dimension. A sphere is a finite space with no
    boundary, so there is no density gradient. This is the paper's key evidence.
- **Experiment 2: where hubs form in 2D.** Collecting the biggest hubs from 250 samples of
  a square shows them concentrated near the corners and edges. Points by a boundary have
  fewer directions to find neighbours in, so the points just inside them get chosen more.
  More boundary per unit of volume, as in a high-dimensional cube, means more hubs.
- **Experiment 3: hubness made in 3D.** Sampling from a grid of separated small cubes
  (lots of boundary) produces measurable hubness in three dimensions. It is weak: in 3D a
  point can be the nearest neighbour of at most 12 others (the kissing number). It vanishes
  when the gaps are too small for the cubes to count as separate, or when each cube holds
  so few points that they are all each other's neighbours.
- **Experiment 4.** Squashing a cube's points into a ball cuts hubness to the level of a
  uniform ball, because it pulls points away from the surface even though it creates
  density gradients inside.

## Why it's in the library

**It changes what to look for.** If hubs come from density gradients rather than from
dimension as such, then hubness is a property of how the data is distributed, which can be
checked and changed, not a fixed price of having many features. Fat-tailed, clustered or
bounded features (ranks, percentiles, clipped z-scores) all create gradients.

**It explains which fixes work.** [[feldbauer-flexer-2019-a-comprehensive-empirical-comparison-of-hubness-reduction-in-high-dimensional-spaces]]
found that centering on the mean helps little, while local scaling and local density
flattening work. That is what this chapter predicts: the cause is local density gradients,
not distance from one global centre. Feldbauer & Flexer cite it for exactly that point.

**Read the two hubness papers together.** Radovanović et al. show that hubs appear and
where (near the centre); this chapter argues why (density falling away from them). On
normal data the two views coincide: the centre is the densest point, density falls away
from it in every direction, and the points there end up closest to everything.

## Links

- [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]]
  — the claim this chapter disputes: hubness as an inherent effect of dimension
- [[feldbauer-flexer-2019-a-comprehensive-empirical-comparison-of-hubness-reduction-in-high-dimensional-spaces]]
  — the benchmark of fixes, whose results fit the density-gradient explanation
- [[salih-2023-the-surprising-behavior-of-data-in-higher-dimensions]] — why a
  high-dimensional cube's volume sits near its boundary and corners
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — distance concentration, the
  other nearest-neighbour curse
