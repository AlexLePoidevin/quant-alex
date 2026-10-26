# On the Surprising Behavior of Distance Metrics in High Dimensional Space

| | |
|---|---|
| **Authors** | Charu C. Aggarwal (IBM T. J. Watson), Alexander Hinneburg, Daniel A. Keim (University of Halle) |
| **Year** | 2001 |
| **Type** | Conference paper — *Database Theory — ICDT 2001*, LNCS 1973, pp. 420–434, doi:10.1007/3-540-44503-X_27. Author copy, 15pp |
| **PDF** | `aggarwal-hinneburg-keim-2001-surprising-behavior-of-distance-metrics.pdf` (in this folder) |
| **BibTeX** | `aggarwal2001surprising` |
| **Status** | Reference |

## What it is

The follow-up to [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]]. Beyer et al. showed
that nearest and farthest neighbours become equally far away as dimension grows. This paper
asks whether the **choice of distance** changes how fast that happens, and finds that it does.

- **The gap between farthest and nearest depends on the norm.** For the L_k distance
  (Σ|xᵢ − yᵢ|^k)^{1/k} with independent coordinates, E[Dmax − Dmin] grows like
  **d^{1/k − 1/2}** (Lemma 2, any distribution; Lemma 1 gives the constant for uniform data).
  - **L₁ (Manhattan):** the gap grows like √d.
  - **L₂ (Euclidean):** the gap tends to a constant.
  - **L₃ and above:** the gap shrinks to zero.
- **The relative contrast** (Dmax − Dmin)/Dmin falls like 1/√d for every k, but the constant
  is larger for smaller k. In simulations with 10 uniform points, L₁ has the higher relative
  contrast than L₂ with high probability from about 20 dimensions on (Table 2). Their ranking
  is L₁ first, then L₂, L₃ and so on, with L_∞ (the maximum coordinate difference) worst.
- **Fractional "metrics", k < 1.** Taking k = f in (0, 1) increases the contrast further
  (Theorem 3, proved for f = 1/l). Small coordinate differences count for relatively more
  and a single large, possibly noisy, difference counts for less.
- **Empirical results:**
  - **k-means** on 6 well-separated Gaussian clusters in 20 dimensions: about 99% correct at
    f = 0.3 against 89% for Euclidean (Fig. 4).
  - **Nearest-neighbour class matching** on four UCI datasets (Machine, Musk, Breast Cancer,
    Segmentation): accuracy falls almost monotonically as k rises from 0.1 to 10 to ∞
    (Table 3). On Musk, L₀.₁ matches 998 against 405 for L₂. L_∞ is often no better than
    random.
  - **Noise masking:** L₁₀ falls to random at 40% of entries replaced by noise, L₁ at 60%,
    and L₀.₁ degrades slowest (Fig. 6).

## Read with care

- **k < 1 is not a metric.** The "fractional distance metric" breaks the triangle inequality,
  so tree indexes, metric-space algorithms, and anything relying on that property lose their
  guarantees. Ranking neighbours is fine; geometry is not.
- **The theory assumes IID coordinates** (uniform for the explicit constants). Correlated or
  factor-driven features are not covered, and Beyer et al.'s result covers a much broader
  class.
- **Every k still concentrates.** The relative contrast still falls like 1/√d, so the norm
  changes the constant, not the rate. A smaller k delays the problem but doesn't remove it.
- **The real-data evidence is thin:** four small datasets, one neighbourhood size, no error
  bars. The k-means test uses synthetic clusters that are easy by construction.
- **Scale matters before the norm does.** None of this helps if features are on different
  scales; standardise first.

## Why it's in the library

**It turns Beyer et al.'s warning into a setting you can change.** If a method on a wide
feature set depends on distances (kNN analogue forecasting, clustering of days or assets,
an RBF kernel), Euclidean distance is not the neutral default it looks like. L₁, or even
k < 1 for ranking, keeps more contrast and is less dominated by the one feature that
happens to be far off.

**The mechanism is about outlier coordinates.** A large k lets the coordinate with the
biggest difference dominate the distance. With fat-tailed financial features, one extreme
value can set the whole distance at k = 2 or higher. A small k spreads the weight across
coordinates, which is a robustness argument as much as a dimensionality one.

**It is cheap to test.** Running the same kNN or clustering with k ∈ {0.5, 1, 2} and
comparing the farthest-to-nearest ratio is a one-line check before trusting a neighbour
method.

## Links

- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the distance-concentration
  theorem this paper refines (their reference [6])
- [[levina-bickel-2004]], [[facco-et-al-2017]] — intrinsic-dimension estimators built on
  Euclidean nearest-neighbour distances, so they inherit the choice of norm
- [[kernel-pca]] — RBF kernels use squared Euclidean distance, the k = 2 case
- [[coifman-lafon-2006]] — diffusion maps, also built on a Euclidean kernel
