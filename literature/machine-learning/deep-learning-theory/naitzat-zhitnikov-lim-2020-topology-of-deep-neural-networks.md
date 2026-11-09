# Topology of Deep Neural Networks

| | |
|---|---|
| **Authors** | Gregory Naitzat (Chicago, Statistics), Andrey Zhitnikov (Technion), Lek-Heng Lim (Chicago, CAM) |
| **Year** | 2020 |
| **Type** | Paper — *Journal of Machine Learning Research* 21(184), 1–40 (2020) |
| **PDF** | `naitzat-zhitnikov-lim-2020-topology-of-deep-neural-networks.pdf` (in this folder; the JMLR version, CC BY 4.0) |
| **Link** | [JMLR](https://jmlr.org/papers/v21/20-345.html) |
| **BibTeX** | `naitzat2020topology` |
| **Status** | Reference — read in full (the algebraic-topology background in §3 skimmed) |

## What it is

An experimental study of how the **shape (topology) of a data set changes as it passes
through the layers** of a well-trained classifier. Topology here is measured with
persistent homology, which estimates the **Betti numbers** of a point cloud from Vietoris–Rips
complexes:
- β₀ counts connected pieces.
- β₁ counts loops.
- β₂ counts enclosed voids.

**Set-up.** Binary classification of two disjoint manifolds that are deliberately tangled:
- **D-I:** nine disks sitting inside the holes of a disk with nine holes.
- **D-II:** nine pairs of linked solid tori.
- **D-III:** nine sets of nested spherical shells around balls.

No hyperplane can separate either class from the other in the input space, and any boundary
that does separate them must itself be topologically complex. The networks are trained to
perfect training accuracy, with about 0.01% test error. The authors ran over 10,000
experiments varying activation (ReLU, leaky ReLU, tanh), width and depth, each repeated at
least 30 times. They then checked the findings on four real data sets: MNIST, HTRU2 pulsars,
UCI banknotes and UCI sensorless drive. On those, 95–98% accuracy was the best achievable.

**Findings.**
- **Networks work by simplifying topology.** Layer by layer, the Betti numbers of both classes
  fall towards the simplest possible values: one connected piece, no loops, no voids. The
  tangled classes end as two clusters a hyperplane can split. The profile is consistent
  across training runs.
- **ReLU simplifies faster than tanh.** A tanh layer is a homeomorphism, so it cannot change
  topology; topology changes only through the dimension changes between layers. ReLU is
  many-to-one, so it can fold space and merge or remove holes. On MNIST, tanh networks
  remained stuck at two connected pieces where ReLU reached one.
- **Depth spreads the work.** In deep networks the early layers mostly change geometry and
  topological change is spread across later layers. In shallower networks it is concentrated
  in the final layers, and below a certain depth the networks become hard to train to high
  accuracy.
- **Bottlenecks force abrupt changes.** A narrow layer forces a large topological change at
  that layer.

The closing section speculates on the mechanism. ReLU adds *folding* to the rotate, shift and
stretch moves of an affine map. Width beyond the input dimension gives room to untangle, as
in a kernel embedding. Depth acts like time: more steps for a sequence of folds.

## Why it's in the library

**It gives a topological answer to "why depth and why ReLU".** Universal approximation says
one wide layer is enough. This paper's account is that hard boundaries need many successive
folds. It sits alongside the function-counting argument of
[[eldan-shamir-2016-the-power-of-depth-for-feedforward-neural-networks]] and the
piecewise-linear capacity bounds of [[lei-et-al-2018-geometric-understanding-of-deep-learning]].

**It is the topological counterpart of the geometry papers.**
[[cohen-chung-lee-sompolinsky-2020-separability-and-geometry-of-object-manifolds-in-deep-neural-networks]]
tracks manifold radius and dimension shrinking until classes become linearly separable. This
paper tracks connected pieces, loops and voids disappearing on the way to the same end state.
It deliberately studies a whole class of inputs, not how one example image changes, which is
the same choice Cohen et al. make.

**It warns against finite-width, lazy-regime intuitions.** The networks here are small (15
neurons per hidden layer is typical) and well short of the infinite-width limits in
[[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]]. The topology
changes they measure need nonlinear folding that a near-linearised network would not do.

**Limits.**
- **The evidence is empirical.** The paper does not prove how a ReLU network changes topology.
- **The synthetic data are tiny.** The manifolds are 2- and 3-dimensional, with
  near-perfectly separable classes, built so the true topology is known in advance.
- **Real-data checks are limited.** They use fixed ten-layer, ten-neuron networks, MNIST is
  reduced to 50 input dimensions, and persistent homology is recomputed at every layer. That
  is expensive and needs denoising.
- **The scale choice is a judgement call.** Persistent homology depends on picking a
  neighbourhood scale, and the simulated experiments fix one scale for all layers.

## Links

- [[cohen-chung-lee-sompolinsky-2020-separability-and-geometry-of-object-manifolds-in-deep-neural-networks]]
  — the geometric counterpart: manifold radius, dimension and capacity across layers
- [[eldan-shamir-2016-the-power-of-depth-for-feedforward-neural-networks]] — depth separation:
  functions a deeper network represents with far fewer units
- [[lei-et-al-2018-geometric-understanding-of-deep-learning]] — piecewise-linear limits on
  which manifolds a ReLU network can flatten
- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the
  infinite-width linear limit, where this kind of folding does not happen
- [[khalid-et-al-2026-a-survey-of-theory-grounded-interpretability-for-deep-neural-networks]]
  — survey of geometric and other theory-based explanations of deep networks
- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
  — data as several disconnected manifolds, the β₀ > 1 case this paper starts from
