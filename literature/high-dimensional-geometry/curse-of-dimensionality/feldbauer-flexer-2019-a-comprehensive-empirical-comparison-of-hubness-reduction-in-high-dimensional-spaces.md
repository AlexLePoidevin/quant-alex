# A Comprehensive Empirical Comparison of Hubness Reduction in High-Dimensional Spaces

| | |
|---|---|
| **Authors** | Roman Feldbauer; Arthur Flexer (Austrian Research Institute for Artificial Intelligence, Vienna) |
| **Year** | 2019 (online May 2018) |
| **Type** | Paper — *Knowledge and Information Systems* 59, 137–166, doi:10.1007/s10115-018-1205-y. Open access, CC BY 4.0. 30pp |
| **PDF** | `feldbauer-flexer-2019-a-comprehensive-empirical-comparison-of-hubness-reduction-in-high-dimensional-spaces.pdf` (in this folder) |
| **BibTeX** | `feldbauer2019comprehensive` |
| **Status** | Reference |

## What it is

The practical follow-up to [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]].
Hubness is known to damage nearest-neighbour methods; this paper tests every unsupervised
fix that existed and says which ones work.

- **What is measured.** Hubness is the skewness of the 10-occurrence distribution (how
  often each point is among others' 10 nearest neighbours). Whether a fix keeps the
  meaning of the data is measured by k-NN classification accuracy, on the view that
  same-class points should stay closest.
- **Twelve methods in four families**, each producing a "secondary distance" from the
  original one:
  - **Repair asymmetric neighbour relations** (in high dimension, x is often y's neighbour
    but not the reverse):
    - *local scaling (LS)*: divide each distance by the distance to each point's k-th
      neighbour;
    - *NICDM*: the same, using the mean distance to the k nearest neighbours;
    - *mutual proximity (MP)*: the probability that x and y are both closer to each other
      than to the rest of the data, computed from each point's full distance distribution
      (exactly, or with a Gaussian approximation, MP-GaussI);
    - *shared nearest neighbours (SNN, simhub)*: similarity from overlapping neighbour lists.
  - **Remove spatial centrality:** centering the data on its mean (CENT) and localized
    centering (LCENT), for inner-product similarities.
  - **Flatten the density gradient:** DisSim global and local (DSG, DSL), which subtract
    each point's squared distance to the global or local centroid from the squared
    Euclidean distance.
  - **Different distance measures:** L_p norms from p = 0.25 to 5, and the data-dependent
    m_p-dissimilarity.
- **Protocol.** 50 public datasets (UCI, LibSVM, OpenML; text, genomics, images, audio),
  ten-by-ten nested cross-validation, hyperparameters tuned to minimise hubness on the
  inner folds, Friedman test and Nemenyi post-hoc ranks across datasets.
- **Results:**
  - **LS, NICDM, MP and DSL are the winners.** All four cut hubness and keep or improve
    accuracy; LS is the only method significantly better than both Euclidean and cosine
    baselines on accuracy. DSL reduces hubness most but occasionally hurts accuracy.
  - **Fixes only matter when hubness is high.** Clear gains start above a 10-occurrence
    skewness of roughly 1.2–1.4. On low-hubness data the good methods do no harm.
  - **Shared-neighbour methods reduce hubness but damage accuracy**: they keep only rank
    information and lose the semantics.
  - **Centering helps mainly on text** and fails on clustered data, because hubs sit near
    the cluster centres, not the global mean.
  - **Changing the L_p norm and DSG do almost nothing.** LCENT increases hubness on average.
  - **Symmetry is what matters.** Across methods, how much a fix makes neighbour relations
    mutual correlates 0.72 (Spearman, on ranks) with accuracy; how much it reduces
    centrality doesn't correlate with accuracy at all (−0.05).
- **Cost.** MP with the empirical distances is O(n³); LS, NICDM, DSL and MP-GaussI are
  O(n²). The methods are implemented in the authors' Python Hub-Toolbox, and the paper
  ends with a decision chart (measure hubness → check data size and domain → pick a method).

## Why it's in the library

**It turns hubness from a warning into a fix you can apply.** If a k-NN, clustering or
analogue method runs on many features, the recipe is short: measure the skewness of
k-occurrence; if it is above about 1.2, rescale distances with local scaling or mutual
proximity before searching for neighbours. Both are a few lines on top of a distance
matrix, and the paper shows they rarely hurt.

**It closes off two tempting shortcuts.** Switching to a fractional or other L_p norm
([[aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics]]) did not reduce
hubness in practice, and centering the data on its mean fails when the data is clustered,
as market data usually is (regimes, sectors).

**Mutual proximity has a natural reading for time series.** It asks whether two days are
each other's unusual neighbours, relative to how far each typically is from everything.
That discounts the "average" days that would otherwise be everyone's closest analogue.

## Links

- [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]]
  — the paper that defined hubness and explained where hubs come from
- [[aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics]] — fractional
  norms, one of the remedies this benchmark finds ineffective against hubness
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — distance concentration, the
  related curse
- [[coifman-lafon-2006]] — diffusion maps, another way of replacing raw distances with
  ones that respect the data's local structure
