# Separability and Geometry of Object Manifolds in Deep Neural Networks

| | |
|---|---|
| **Authors** | Uri Cohen, SueYeon Chung (equal contribution), Daniel D. Lee, Haim Sompolinsky (Hebrew University, Harvard, MIT, Columbia, Cornell Tech) |
| **Year** | 2020 |
| **Type** | Paper — *Nature Communications* 11, 746 (2020), doi:10.1038/s41467-020-14578-5 |
| **PDF** | `cohen-chung-lee-sompolinsky-2020-separability-and-geometry-of-object-manifolds-in-deep-neural-networks.pdf` (in this folder; the published version, open access under CC BY 4.0) |
| **Link** | [Nature Communications (open access)](https://doi.org/10.1038/s41467-020-14578-5) |
| **BibTeX** | `cohen2020separability` |
| **Status** | Reference — read in full (main text; supplementary not included) |

## What it is

A measurement of how deep networks "untangle" objects, using a statistical-physics theory of
when collections of points can be split by a hyperplane.

**Object manifolds and capacity.** All the responses a layer gives to one object, across
poses, crops or warps, form that object's *manifold*. The **classification capacity** α_c is
the most manifolds per neuron (P/N) that a linear readout can still separate under random
binary labels. Above it, separation fails with high probability. Two reference points:
- **α_c = 2** when each manifold collapses to a single point (a fully invariant representation).
- **α_c = 2/M** when each manifold is just M unstructured random points.

**Capacity is set by two geometric numbers.** The theory generalises support vectors to
*anchor points*: each manifold contributes one point that pins the separating hyperplane, and
which point it is depends on the other manifolds and the labels. The spread of a manifold's
anchor points defines its effective **radius R_M** and **dimension D_M**. For
high-dimensional manifolds, capacity is close to that of balls with that radius and
dimension. This paper extends the theory to manifolds whose centres are correlated, as real
ones are.

**Findings on ImageNet networks** (AlexNet and VGG-16, with ResNet-50 in the supplement):
- **Pixels look like noise.** At the input layer, object manifolds are as hard to separate as
  randomly shuffled ones.
- **Capacity rises through the network, mostly in the last layers.** By the final layers it is
  about an order of magnitude above the shuffled baseline. VGG-16 ends higher than AlexNet.
- **Training does the work.** An untrained network with the same architecture improves very
  little, so the gain comes from the learned weights, not the architecture.
- **Dimension falls most.** In AlexNet, manifold dimension drops from over 80 in early layers
  to about 20, and radius from about 1.4 to 0.8. Correlations between manifold centres also
  fall.
- **The geometry is causal.** Scaling a manifold up lowers capacity. Replacing each manifold
  with a ball of the same R_M and D_M reproduces the measured capacity. Reducing dimension
  alone accounts for about 90% of the gain in early layers and 55% in late ones; reducing
  radius alone does much less. Randomising manifold centres shows correlations matter too.
- **No single block explains it.** Convolution, ReLU, pooling and fully connected stages each
  change the geometry differently, and the improvement only appears across the whole
  hierarchy.
- **Capacity is extensive.** The number of separable manifolds grows in proportion to the
  number of neurons, so capacity can be estimated from a random subset of neurons.

## Why it's in the library

**It turns "a good representation" into numbers.** "Untangling factors of variation", the
goal in [[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]],
becomes three measurable quantities: manifold radius, dimension and centre correlation. Each
is linked to how many classes a linear readout can separate.
[[khalid-et-al-2026-a-survey-of-theory-grounded-interpretability-for-deep-neural-networks]]
treats it as the foundational paper connecting manifold geometry to classification.

**It fits the library's dimension theme.** It is a layer-by-layer version of
[[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]],
where classes with higher intrinsic dimension are harder to classify. It is also a
representation-side counterpart to [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]],
where training drives low-dimensional structure in weights and gradients.

**The diagnostic transfers.** Capacity, R_M and D_M can be computed for any labelled
representation, whether network embeddings or engineered features. They give a
readout-independent check of whether a transformation makes groups more linearly separable,
and a "same architecture, random weights" control for separating learned structure from
architecture.

**Limits.**
- Capacity uses random binary labels over many objects (about 50 per run), which is not the
  same as accuracy on a real task.
- The mean-field theory is exact only for large N and P.
- The point-cloud manifolds use the top 10% highest-scoring images per class or about 1,000
  images, so absolute capacities depend on sampling. The authors report it relative to
  shuffled manifolds for that reason.
- Everything is measured on ImageNet vision networks.

## Links

- [[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]] —
  the untangling goal this paper makes measurable
- [[khalid-et-al-2026-a-survey-of-theory-grounded-interpretability-for-deep-neural-networks]]
  — survey that places this paper at the base of manifold-based interpretability
- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
  — per-class intrinsic dimension predicts classification difficulty
- [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]] — low-dimensional
  structure in the weights and gradients of trained networks
- [[lei-et-al-2020-a-geometric-understanding-of-deep-learning]] — the manifold picture applied
  to generative models
- [[conklin-et-al-2026-learning-is-forgetting]] — compression of representations during
  training, measured with the Information Bottleneck
