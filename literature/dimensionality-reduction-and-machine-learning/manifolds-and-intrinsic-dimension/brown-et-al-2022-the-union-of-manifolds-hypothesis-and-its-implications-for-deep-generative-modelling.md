# The Union of Manifolds Hypothesis and its Implications for Deep Generative Modelling

| | |
|---|---|
| **Authors** | Bradley C.A. Brown (University of Waterloo & Layer 6 AI), Brendan Leigh Ross, Jesse C. Cresswell, Anthony L. Caterini, Gabriel Loaiza-Ganem (Layer 6 AI) |
| **Year** | 2022 |
| **Type** | Preprint — arXiv:2207.02862v1 [stat.ML], July 2022, CC BY 4.0. Later versions were retitled *Verifying the Union of Manifolds Hypothesis for Image Data* and published at ICLR 2023 (v3, March 2023) |
| **PDF** | `brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling.pdf` (in this folder; the v1 preprint) |
| **Code** | [github.com/layer6ai-labs/UoMH](https://github.com/layer6ai-labs/UoMH) |
| **BibTeX** | `brown2022union` |
| **Status** | Reference — §3 (the hypothesis and the per-class dimension estimates) is the core; §4–5 are about generative models |

## What it is

The manifold hypothesis says data lie near one low-dimensional surface. That implies the
same intrinsic dimension everywhere. This paper argues data are better described as a
**union of separate manifolds, each with its own dimension**: an MNIST "1" needs fewer
factors of variation than an "8".

- **Checking the hypothesis.** Using class labels as stand-ins for the separate pieces,
  the authors estimate the intrinsic dimension of each class with the
  [[levina-bickel-2004]] maximum-likelihood estimator. On MNIST, Fashion-MNIST,
  CIFAR-10, CIFAR-100 and ImageNet the estimates vary widely across classes, and the
  pattern holds across choices of the neighbour count k. SVHN is the exception, with
  little variation.
- **Higher dimension, harder to classify.** On CIFAR-100, per-class accuracy falls as
  per-class intrinsic dimension rises (correlation about −0.25 for VGG-19, ResNet-18
  and ResNet-34, significant). Weighting the loss towards high-dimension classes lifts
  ResNet-18 accuracy from 61.38% to 61.77%.
- **Why generative models struggle.** VAEs, GANs, normalising flows and Wasserstein
  autoencoders all push connected noise through a continuous network. The authors prove
  the output must then have one connected support, so these models cannot produce cleanly
  separated groups. Using a Gaussian mixture as the noise does not fix this in practice.
- **The fix: cluster first.** Split the data (by labels or by agglomerative clustering),
  fit a separate generative model to each cluster with its own latent dimension, and mix
  them. These clustered models match or beat the single models on image quality (FID) in
  most cases, despite each seeing less data.
- **When the dimension per cluster matters.** On real images, giving each cluster its own
  latent dimension did not beat one shared dimension. On a synthetic set mixing a
  22-dimensional and a 3-dimensional class it helped a lot. It matters only when the
  dimensions differ widely.

## Read with care

- **Labels stand in for manifolds.** That each class is one connected manifold is an
  assumption, not a finding. The varying estimates could also come from classes having
  different curvature or sample sizes, which bias the estimator.
- **The estimator is noisy.** MLE dimension estimates are biased downwards with few
  points per class (the authors flag ImageNet), and the paper uses a slightly different
  version from earlier work.
- **Small effects.** The loss-reweighting gain is 0.4 percentage points, and the
  per-dimension latent sizes did not help on real data.
- **Images only.** The authors say verifying it on other kinds of data remains to be
  done. No finance data.
- **This is the first version.** The ICLR 2023 paper is retitled and revised; check it
  for the final results.

## Why it's in the library

**Market data plausibly have varying dimension too.** In a sell-off most assets move on
one factor, so the cross-section is close to one-dimensional. In calm markets many
smaller factors matter. Sectors may also differ in how many factors drive them. A
single dimension estimate for "the market" may average over pieces of quite different
complexity, so [[levina-bickel-2004]] and [[facco-et-al-2017]] are better applied by
regime or by group.

**It argues for fitting separate models per group.** Splitting the data into clusters and
fitting each one separately beat one global model here, even with less data per model.
The same reasoning backs per-sector or per-regime models over one model for everything,
provided each group still has enough data.

**It is a warning for generative scenario models.** A VAE or GAN trained to simulate
returns cannot produce cleanly separated regimes (calm vs crisis) from one connected
noise source; it will fill in the gap between them. A mixture of models, one per regime,
does not have that problem.

**Harder groups have higher dimension.** Groups with more intrinsic dimension were
harder to predict. Estimating dimension per group is a cheap way to see where a model
will struggle.

## Links

- [[levina-bickel-2004]] — the dimension estimator used for every result here
- [[facco-et-al-2017]] — two-NN, another estimator, also usable locally per region
- [[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] — measuring manifold
  geometry exactly, on controlled images instead of labelled ones
- [[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]]
  — the manifold and "natural clustering" priors this paper refines
- [[sonthalia-gilbert-2020-tree-i-am-no-tree-i-am-a-low-dimensional-hyperbolic-embedding]]
  — another test of what shape the data has before fitting a model
- [[coifman-lafon-2006]] — diffusion maps, which also separate clusters before
  embedding them
