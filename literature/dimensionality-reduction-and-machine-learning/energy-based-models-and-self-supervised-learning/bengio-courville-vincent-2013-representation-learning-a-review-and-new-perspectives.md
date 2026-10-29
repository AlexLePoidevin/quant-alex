# Representation Learning: A Review and New Perspectives

| | |
|---|---|
| **Authors** | Yoshua Bengio, Aaron Courville, Pascal Vincent (Université de Montréal; CIFAR) |
| **Year** | 2013 |
| **Type** | Journal review — *IEEE Transactions on Pattern Analysis and Machine Intelligence* 35(8), 1798–1828. This copy is arXiv:1206.5538v3 (April 2014), 30pp |
| **PDF** | `bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives.pdf` (in this folder) |
| **BibTeX** | `bengio2013representation` |
| **Status** | Foundational — §3 (what makes a representation good) is the part that has aged best; §6–10 are a 2012 snapshot |

## What it is

The standard pre-2014 survey of learning features from data instead of designing them by
hand. Its thesis: models work well when the input is expressed in terms of the
**underlying explanatory factors** of the data, and the job of unsupervised learning is to
find and separate (**disentangle**) those factors.

- **A list of priors (§3.1).** What a good representation should assume about the world:
  smoothness; several explanatory factors; factors arranged in a hierarchy; factors useful
  for P(X) also useful for P(Y|X); factors shared across tasks; data concentrated near a
  low-dimensional **manifold**; classes on separate manifolds; **temporal coherence**
  (relevant factors change slowly); sparsity; and simple, often linear, relations between
  factors.
- **Why depth and distributed codes (§3.2–3.4).** Local methods like kernels and
  nearest neighbours need examples for every region of the input, which fails in high
  dimensions. Distributed features, where many features combine, and deep stacks of them
  can represent exponentially many regions with few parameters.
- **Three families of methods**, with PCA used to show all three views:
  - *Probabilistic models* — sparse coding, ICA, restricted Boltzmann machines (energy-based
    models) and deep belief networks.
  - *Auto-encoders* — sparse, denoising and contractive variants, and how they relate to
    score matching and density estimation.
  - *Manifold learning* — learning tangent planes of the data and exploiting them
    (the manifold tangent classifier).
- **Building in invariance (§11).** Augmentation, convolution and pooling, slow features
  from temporal coherence, and early algorithms for disentangling factors.

## Read with care

- **A 2012 snapshot.** It predates VAEs (2013–14), GANs, batch norm, residual networks,
  attention and contrastive/self-supervised learning. Greedy layer-wise pre-training with
  RBMs and auto-encoders, a large part of the review, has since been dropped in practice.
- **Disentangling is a hope here, not a result.** Later work (Locatello et al., 2019)
  showed that fully unsupervised disentangling is impossible without inductive biases or
  some supervision. The priors in §3.1 are those biases, but which ones hold for a given
  data set is not shown.
- **A review by protagonists.** The authors built many of the methods covered, and the
  emphasis follows their own research.
- **No finance data**; the examples are vision, speech and language.

## Why it's in the library

**It is the vocabulary of the modern ML toolkit.** Autoencoders, energy-based models,
manifolds, disentangled factors and invariance all come from here. Later notes in this
folder ([[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]]) and in
[[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] build on it.

**The priors double as a checklist for financial features.** Several translate directly:
- *multiple explanatory factors* is the factor-model view of returns;
- *simple, linear dependencies between factors* is what a linear risk model assumes;
- *temporal coherence* separates slow factors (sector, style, regime) from fast noise;
- *shared factors across tasks* is why one representation can serve several horizons or
  universes.

Asking which of these hold in market data says whether learning a representation is
likely to beat hand-made features at all.

**It joins PCA, ICA and autoencoders in one picture.** PCA is shown as a probabilistic
model, an auto-encoder and a manifold learner at once, with ICA as the step to
independent factors. That is the bridge between [[ica]] / [[hyvarinen-oja-2000]] and
autoencoder factor models like [[gu-kelly-xiu-2021]].

**It argues against the trees-win result.** The review's premise is that learned
representations beat hand engineering.
[[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
is the counterpoint for tabular data, where hand-made features and trees still usually win.

## Links

- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] — energy-based
  models a decade on, the line that runs from RBMs to JEPA
- [[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] — tests the manifold
  prior and asks whether autoencoders really fit the manifold
- [[ica]], [[hyvarinen-oja-2000]] — independent component analysis, one of the
  probabilistic models reviewed
- [[kernel-pca]] — the fixed-kernel route to non-linear features the review contrasts
  with learned ones
- [[gu-kelly-xiu-2021]] — autoencoders as asset-pricing factor models
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — where learned representations still lose
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — invariance and structure built into the architecture, §11 generalised
