# Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges

| | |
|---|---|
| **Authors** | Michael M. Bronstein, Joan Bruna, Taco Cohen, Petar Veličković (Imperial College / USI / Twitter; NYU; Qualcomm AI Research; DeepMind) |
| **Year** | 2021 |
| **Type** | Book-length monograph (proto-book) — arXiv:2104.13478v2, 2 May 2021. 160pp |
| **PDF** | `bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges.pdf` (in this folder) |
| **BibTeX** | `bronstein2021geometric` |
| **Status** | Reference — read §2–3 for the framework; dip into §4–5 for a specific architecture |

## What it is

An attempt to do for deep learning what Klein's Erlangen Programme did for geometry: derive
the main architectures from one principle, **the symmetries of the domain the data live on**.

- **The problem (§2).** Learning a generic function in *d* dimensions needs a number of
  samples exponential in *d*: for Lipschitz functions, and only slightly better under
  Sobolev smoothness. Smoothness alone does not beat the curse of dimensionality.
- **The fix (§3): geometric priors.** If the signal lives on a domain Ω with a symmetry
  group G, the target function should respect G: **invariant** (output unchanged by a
  transformation, e.g. a class label) or **equivariant** (output transforms the same way,
  e.g. a segmentation). Two more priors: **deformation stability** (small distortions
  change the output a little) and **scale separation** (build long-range behaviour by
  composing local operations and coarsening).
- **The blueprint (§3.5).** Stack (i) local equivariant layers, (ii) nonlinearities,
  (iii) coarsening/pooling, and finish with (iv) a global invariant layer. Choosing the
  domain and its group picks the architecture.
- **The "5 Gs" (§4)** are the domains:
  - **Graphs and sets:** permutation symmetry. A function of a set must satisfy
    F(PX) = F(X); node-wise outputs must satisfy F(PX) = P F(X).
  - **Grids:** translation symmetry, which gives convolution.
  - **Groups and homogeneous spaces:** e.g. rotations on a sphere.
  - **Geodesics and manifolds:** isometries, intrinsic (Laplacian, geodesic) operators.
  - **Gauges and bundles:** local frame choices on a manifold.
- **Models (§5)** fall out of the blueprint: CNNs, group-equivariant CNNs, GNNs (convolutional,
  attentional, message-passing), Deep Sets and Transformers (a Transformer is a GNN on a
  complete graph), equivariant message passing, intrinsic mesh CNNs. RNNs, LSTMs and GRUs
  are read as models invariant to **time warping**: gating is what that invariance requires.
- §6 surveys applications (chemistry, drug design, protein biology, recommender systems,
  traffic, physics, computer vision); §7 is a short history.

## Read with care

- **A framework, not an empirical result.** There are no benchmarks. The claim that
  symmetry explains why architectures work is argued by derivation and example, and it is
  strongest for grids and graphs, where the symmetry is exact.
- **It assumes the symmetry is known and exact.** Financial data rarely give you one. The
  ordering of stocks in a cross-section is arbitrary (permutation symmetry is real), but
  time is not translation-invariant under non-stationarity, and feature columns have no
  natural symmetry group at all.
- **No finance in it.** Every application is from science, vision or recommender systems.
- **2021 snapshot.** Written before the large-Transformer era; the Transformer section is
  short, and later work on approximate or learned symmetries is not covered.
- **Long and mathematically uneven.** §2–3 and the blueprint are accessible. Gauges and
  bundles (§4.5) need differential geometry and are optional for most readers.

## Why it's in the library

**It gives the vocabulary for "what should the model be invariant to?"** That is the right
first question for any architecture on market data:
- A **cross-sectional ranking model** should be permutation-equivariant across assets: the
  score of a stock must not depend on its row position. Per-asset shared models (a tree or
  an MLP applied row by row) satisfy this automatically; Deep Sets and attention add
  interactions between assets while keeping it.
- A **correlation or co-movement network** is a graph, and GNNs are the matching architecture.
- **Tabular features have no symmetry group**, which is the geometric version of
  [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]:
  forcing rotation invariance on columns that each mean something throws information away.

**It connects the curse of dimensionality to manifold structure.** Low intrinsic dimension
([[facco-et-al-2017]], [[levina-bickel-2004]]) and known symmetries are the two ways out of
the exponential sample requirement in §2. Diffusion maps ([[coifman-lafon-2006]]) are the
spectral, Laplacian-based tools that §4.4 builds on for manifolds and graphs.

## Links

- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the empirical case that the wrong invariance (rotation) hurts on tabular data
- [[facco-et-al-2017]] — measuring intrinsic dimension, the other escape from §2's curse
- [[coifman-lafon-2006]] — diffusion maps and the graph Laplacian, used throughout §4.4
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the curse of dimensionality
  seen through distance concentration
