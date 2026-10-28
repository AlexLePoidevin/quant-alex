# Mixed-Curvature Decision Trees and Random Forests

| | |
|---|---|
| **Authors** | Philippe Chlenski, Quentin Chu, Raiyan R. Khan, Kaizhu Du, Antonio Khalil Moretti, Itsik Pe'er (Columbia, Barnard, Spelman) |
| **Year** | 2025 |
| **Type** | Conference paper — *Proceedings of the 42nd International Conference on Machine Learning* (ICML 2025), PMLR 267; camera-ready = arXiv:2410.13879v3 |
| **PDF** | `chlenski-et-al-2025-mixed-curvature-decision-trees-and-random-forests.pdf` (in this folder) |
| **Code** | [github.com/pchlenski/manify](https://github.com/pchlenski/manify) |
| **BibTeX** | `chlenski2025mixed` |
| **Status** | Reference — §3 (the angular split) is the idea; most of the 30 pages are appendix |

## What it is

A decision tree and random forest for data that lives on curved spaces, not flat ones.
The spaces are **product manifolds**: a hyperbolic part (good for hierarchies and
trees), a spherical part (good for cycles and directions) and a Euclidean part, glued
together. The list of parts and their curvatures is called the **signature**, e.g.
H² × S² × E².

- **The problem with ordinary trees here.** Splitting on raw coordinates ignores the
  geometry: a leaf can be two disconnected pieces, the shortest path between two points
  in a leaf can leave it, and the threshold sits unevenly between its two neighbours.
  The paper lists five properties a good split should keep (connected leaves, convex
  leaves, equidistant thresholds, O(nd) candidates per split, O(1) per decision).
- **The fix: split on angles.** Each point is projected onto two-dimensional slices
  (the ambient "time" coordinate x₀ plus one other coordinate) and summarised as a
  single angle θ = tan⁻¹(x₀/x_d). A split is then a threshold on θ, and the threshold
  is placed at the geometric midpoint for that curvature (formulas for each of the
  three geometries). One tree can split on any component, so it allocates splits to
  whichever geometry matters.
- **Special cases.** With one Euclidean component it reduces exactly to an ordinary
  CART tree; with one hyperbolic component, to the earlier hyperbolic forests; with
  a spherical one it gives the first hyperspherical trees.
- **Results.** 57 benchmarks: synthetic Gaussian mixtures on each geometry, graph
  embeddings (Cora, CiteSeer, PolBlogs), VAE latent spaces (MNIST, CIFAR-100, blood
  cells), and data that is naturally curved (land vs water on the globe, calendar
  time on circles). The product forest is first on 29 and top-two on 41, against
  forests on raw or tangent-plane coordinates, k-nearest neighbours, MLPs and a
  curvature-aware graph network. On link prediction it is level with the others.

## Read with care

- **The margins are small.** Most wins sit inside the overlapping 95% intervals from
  10 seeds with one fixed 80:20 split. "First on 29 of 57" is a count, not a test.
- **It assumes the embedding.** The data must already sit in a product manifold with
  a chosen signature; the paper picks it by embedding distortion. Choosing and fitting
  that embedding is the hard, expensive part, and the authors say so.
- **It loses on the time-series examples.** On the two real cyclic regressions —
  city temperatures by month and road traffic with year/day/hour/minute as circles —
  the plain forest on raw coordinates beats the product forest (RMSE 48 vs 78; 0.22
  vs 0.31). Encoding calendar time as angles did not help a tree.
- **No privileged axes.** A tree's bias towards axis-aligned splits makes sense when
  each column means something. Learned embeddings have no meaningful axes, which the
  authors flag as a weak point of the whole approach.
- **No finance data**, and the benchmarks are small (hundreds to a few thousand points).

## Why it's in the library

**It is the step after a tree-like embedding.**
[[sonthalia-gilbert-2020-tree-i-am-no-tree-i-am-a-low-dimensional-hyperbolic-embedding]]
measures whether distances are tree-like and embeds them in hyperbolic space; this
paper is what you can fit on top. A hierarchy of stocks built from correlations, as in
[[mantegna-1999]], could be embedded in a hyperbolic component and fed to a forest
whose splits respect it.

**It is the curved-space version of the patch idea.**
[[li-et-al-2019-manifold-forests-closing-the-gap-on-neural-networks]] gives a forest
the structure of a grid or a time axis by changing which features a split can use.
This paper gives it the structure of a curved space by changing how a split is
measured. Both keep the tree algorithm and change only the split.

**It is a caution about cyclical features.** Day-of-week, month-of-year and
time-of-day are natural circles, and encoding them as angles is a common trick. Here
the plain forest did better on exactly that kind of data — a tree can already cut a
calendar column into ranges.

## Links

- [[sonthalia-gilbert-2020-tree-i-am-no-tree-i-am-a-low-dimensional-hyperbolic-embedding]]
  — tree-likeness and hyperbolic embeddings, the input this method assumes
- [[li-et-al-2019-manifold-forests-closing-the-gap-on-neural-networks]] — forests that
  respect structure through the choice of split features
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the general case for building a domain's geometry into the model
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — why axis-aligned trees win on tabular data, the inductive bias this paper bends
- [[mantegna-1999]] — the correlation hierarchy that a hyperbolic component could hold
