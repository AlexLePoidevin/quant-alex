# Analyzing CART

| | |
|---|---|
| **Authors** | Jason M. Klusowski (Rutgers University) |
| **Year** | 2019 |
| **Type** | Preprint — arXiv:1906.10086 [stat.ML], first posted June 2019; this copy is v7, August 2020, 58pp |
| **PDF** | `klusowski-2019-analyzing-cart.pdf` (in this folder) |
| **BibTeX** | `klusowski2019analyzing` |
| **Status** | Reference — §4–6 (the setup, Theorems 1–2 and Fig. 1) carry the result; §7–11 are assumptions and proofs |

## What it is

A theory paper on why regression trees grown with CART (the standard greedy
split-by-variance algorithm behind random forests and gradient boosting) have small bias
and adapt to which features matter, and how both connect to the mean decrease in impurity
(MDI), the default feature importance in most tree libraries.

- **The setting.** Regression Y = f(X) + noise on [0, 1]^d, where f depends on a small
  unknown subset of "strong" features. To make the analysis possible, splits are chosen
  using the population version of CART's criterion rather than the sample version;
  everything else (leaf averages, depth, which variables are tried) uses the data. The
  paper cites results showing sample split points converge to population ones at rate
  n^(1/3).
- **CART in one line.** At each node CART picks the split giving the largest drop in
  within-node variance. Equivalently, it picks the one-split step function most correlated
  with the response inside that node.
- **Theorem 1: importance controls leaf width.** For any leaf, the probability mass of its
  side along feature j is at most exp(−MDI_j), where MDI_j is a weighted sum of the
  impurity reductions from splits on j above that leaf. Features that have earned a lot of
  importance get narrow leaves; features that have not get wide ones. Narrow leaves along
  the features that matter is what small bias means for a tree.
- **Local adaptivity.** The bound holds leaf by leaf, so a tree splits finely where the
  function changes fast and stays coarse where it is flat. On four UCI datasets
  (rpart, 1,000 bootstrap trees) the median leaf width along each feature falls as its MDI
  rises, as the theorem predicts.
- **Theorem 2: importance grows with how often a feature is used.** If f is not too flat
  along feature j (some derivative is non-zero everywhere) and the features are
  independent, MDI_j is at least a constant Λ_j times the number of times j was split on
  above the leaf. So leaves shrink exponentially in the number of splits on each strong
  feature.
- **What Λ_j depends on.** Λ_j measures how balanced the splits are. It falls as the
  function gets more wiggly: at least (1/(k(k+1)))^(2/3), about k^(−4/3), for a degree-k
  polynomial term, and on the order of m^(−4/3) for a sine of frequency m. Wiggly functions push CART's splits towards the edges of a node
  ("end-cut preference"), so it needs more depth. A penalty (4·P_left·P_right)^α on the
  split criterion pulls splits back towards the middle.
- **Where CART fails.** For f(x) = x₁ + x₂ − 2x₁x₂ with uniform inputs, every possible
  split reduces impurity by zero, so CART cannot see that f depends on both features.
  The paper's assumptions rule this case out, and the theory needs them.
- **Random forests.** Combining these bias bounds with existing variance results, the
  paper proves Breiman's random forest is consistent (its error goes to zero with more
  data) for a general class of continuous f, under its population-split setting and
  assumptions. Earlier consistency proofs for CART-based forests needed f to be additive.
- **Splits keep enough data.** It also shows CART's own splits leave each child with a
  fixed fraction of the parent's data, a condition earlier theory had to impose by hand.

## Why it's in the library

**It is the positive side of the theory of trees.**
[[bengio-delalleau-simard-2010-decision-trees-do-not-generalize-to-new-variations]] shows
what a tree cannot learn: variations where it has no data. This paper shows what CART does
well: it spends its splits on the features and regions where the target actually moves,
and ignores the rest. Together they explain both the strength on sparse tabular problems
and the weakness on targets made of many interacting variations.

**It gives MDI feature importance a meaning.** MDI was introduced as a heuristic. Here it
directly bounds how finely the tree has resolved each feature, so a high MDI means the
model has narrow leaves in that direction. The paper also notes the known weakness: a
weak feature correlated with a strong one can pick up importance, so MDI is unreliable for
deciding which correlated features matter.

**It explains why trees ignore noise features.** A feature that never reduces impurity
never gets split on and keeps one wide leaf, which is the mechanism behind the noise
robustness measured in
[[freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features]]
and [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]].

**The blind spot is worth remembering.** A target driven purely by an interaction, with no
marginal effect of either feature on its own, gives CART nothing to split on at the top of
the tree. If an interaction is suspected, adding it as an explicit feature helps.

## Links

- [[bengio-delalleau-simard-2010-decision-trees-do-not-generalize-to-new-variations]] — the
  negative counterpart: what a single tree cannot generalise to
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the empirical case for trees on tabular data, including robustness to uninformative
  features
- [[freytsis-perelstein-san-2024-anomaly-detection-in-the-presence-of-irrelevant-features]]
  — trees ignoring pure-noise features in practice, with feature importance showing why
- [[candelori-santhanam-2025-breaking-the-curse-of-dimensionality-qcml-vs-tree-based-models]]
  — a benchmark where every feature matters equally and trees struggle
- [[li-et-al-2019-manifold-forests-closing-the-gap-on-neural-networks]] — forests that
  change how splits are chosen, for inputs where single-feature splits are a poor fit
- [[baucells-et-al-2021-trend-analysis-in-the-age-of-machine-learning]] — which partial dependence and ICE plots can be trusted to show a fitted model's shape when features are correlated
