# Supervised Similarity for High-Yield Bonds

| | |
|---|---|
| **Authors** | Joshua Rosaler (BlackRock), Luca Candelori, Vahagn Kirakosyan, Kharen Musaelian, Ryan Samson (Qognitive), Martin T. Wells (Cornell), Dhagash Mehta, Stefano Pasquali (BlackRock) |
| **Year** | 2025 |
| **Type** | Paper — *Risk.net*, Cutting Edge: Investments, May 2025, 6pp. Preprint arXiv:2502.01495, *Supervised Similarity for High-Yield Corporate Bonds with Quantum Cognition Machine Learning* |
| **Link** | [arxiv.org/abs/2502.01495](https://arxiv.org/abs/2502.01495) (free preprint); [risk.net](https://www.risk.net/cutting-edge/7961606/supervised-similarity-for-high-yield-bonds) (paywalled) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22Supervised+Similarity+for+High-Yield+Bonds%22+Rosaler) for the title and authors |
| **BibTeX** | `rosaler2025bonds` |
| **Status** | Reference — short; the QCML proximity definition (eq. 5), table A and figures 1–2 carry the result |

## What it is

A comparison of three ways to measure how similar two corporate bonds are, judged by how
well each one finds bonds with similar yields or spreads. The use cases are finding a
tradable substitute for an illiquid bond, pricing a bond with no recent trades from its
neighbours, hedging, and spotting outliers.

- **Supervised similarity.** Similarity is defined with respect to a target (yield or
  spread), not raw feature distance. The standard method uses a random forest: two bonds
  are close if they often land in the same leaf. The paper uses the geometry-and-accuracy-
  preserving (GAP) version of Rhodes et al. (2023), whose weights reproduce the forest's
  own prediction exactly.
- **QCML similarity.** A supervised QCML model maps each bond to a quantum state (the
  ground state of an error Hamiltonian built from learned feature matrices) and predicts
  the target as ⟨ψ|B|ψ⟩, trained on mean absolute error. The distance between two bonds is
  1 − |⟨ψ₁|ψ₂⟩|², one minus the overlap of their states (the fidelity). The square root of
  this is a true metric.
- **Data.** The holdings of two iShares ETFs on 18 September 2024: high yield (HYG, target =
  yield) and 1–5 year investment grade (IGSB, target = credit spread). Seven numerical
  features (coupon, frequency, days to maturity, duration, age, amount issued and
  outstanding) and three categorical (rating, country, industry), 99 features after one-hot
  encoding. Hilbert-space dimension chosen by 3-fold cross-validation: 7 for HYG, 12 for
  IGSB. Random forest tuned too (1,000 trees for HYG, 200 for IGSB).
- **Direct prediction (10 random 80/20 splits).** High yield: mean absolute percentage error
  (MAPE) 0.09 for QCML, 0.11 for the forest and 0.13 for linear regression; R² 0.65, 0.62
  and 0.59. Investment grade: the forest is slightly better on MAE (13.74 vs 13.87 bp) and
  R² (0.76 vs 0.74); QCML's MAPE is 0.23 vs 0.25.
- **Similarity test.** Each distance is plugged into a k-nearest-neighbour regressor, for k
  from 1 to 100, plain or weighted by proximity. For high yield, QCML distance gives the
  lowest error in both versions. For investment grade it wins unweighted and roughly ties
  weighted.
- **Why the forest struggles on high yield.** Under the forest's distance almost every bond
  is at the maximum distance (near 1.0) from almost every other, so only a handful of
  neighbours count; QCML distances are mostly below 0.5. The authors attribute this to trees
  growing separate branches for outliers, and high yield has many outliers (bonds near
  default). One example: for a bond yielding about 50%, QCML's ten nearest neighbours
  predict 33.04%, the forest's 18.17%. For a typical investment-grade bond the forest does
  better (11.2 bp error vs 24.3 bp).

## Why it's in the library

**Similarity relative to a target is a useful tool in its own right.** "Which bonds behave
like this one?" comes up in substitution, pricing illiquid securities, building hedges and
peer groups. Learning the distance from a target, then judging it with a k-nearest-neighbour
test, is a clean recipe that works with any model that yields a distance.

**The forest's distance falls apart on sparse, outlier-heavy data.** When nearly every pair
sits at the maximum distance, nearest-neighbour methods have little to work with; this is
the hubness and distance-concentration problem
([[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]],
[[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]])
appearing in a learned metric. Checking the spread of pairwise distances is a cheap
diagnostic for any similarity measure.

**The result is narrow.** One snapshot day, two bond universes (the paper does not give their sizes),
and an advantage concentrated in the high-yield tail. On investment-grade
bonds QCML and the forest are about even. It is a case for trying QCML distance where data
are sparse and full of outliers, not a general win.

## Links

- [[samson-et-al-2025-supervised-similarity-for-firm-linkages]] — the same QCML similarity
  method applied to links between companies
- [[samson-et-al-2024-quantum-cognition-machine-learning-financial-forecasting]] — the
  supervised QCML model (forecast observable B) this paper builds its distance from
- [[candelori-et-al-2025-robust-estimation-of-intrinsic-dimension-with-qcml]] — the
  peer-reviewed QCML method and its Hilbert-space dimension trade-off
- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the
  programme's founding white paper
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the quantum-geometry framework behind the
  error Hamiltonian
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — when distances concentrate,
  nearest neighbours stop being informative
- [[radovanovic-nanopoulos-ivanovic-2010-hubs-in-space-popular-nearest-neighbors-in-high-dimensional-data]]
  — how high dimension distorts neighbour lists
- [[candelori-santhanam-2025-breaking-the-curse-of-dimensionality-qcml-vs-tree-based-models]]
  — the same authors' QCML-versus-trees comparison on synthetic data
