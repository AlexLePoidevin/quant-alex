# Unifying Low Dimensional Spectra in Deep Learning

| | |
|---|---|
| **Authors** | Connall Garrod, Jonathan P. Keating (Mathematical Institute, University of Oxford) |
| **Year** | 2026 |
| **Type** | Paper — *Proceedings of the 43rd International Conference on Machine Learning* (ICML 2026), PMLR 306. 45pp including appendices |
| **PDF** | `garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning.pdf` (in this folder) |
| **BibTeX** | `garrod2026unifying` |
| **Status** | Reference — theorem-heavy; read §1–3.1, §3.5 and §5, skip the appendix proofs |

## What it is

Matrices from trained classifiers — the Hessian, the gradients, the weights — have a
recognisable spectrum: a **bulk** of eigenvalues near zero and a few **outliers**, with the
count tied to the number of classes K. This paper gives one analytic explanation for all of
it: the outliers are built from the **class means of the features**, so they appear once the
network's representations collapse onto those means.

- **The phenomenon (§1–2).** Empirically the Hessian has K large outliers plus a
  K(K − 1) "mini-bulk" (Papyan, 2020); gradients align with the top-K eigenspace (Gur-Ari et
  al., 2018); weight matrices are low rank. Earlier theories (random matrix theory,
  spin-glass analogies, NTK limits) each reproduced only part of this.
- **The tool.** **Deep neural collapse** (DNC): past the point of fitting the training data,
  each layer's features collapse to their class means, the means form an orthogonal frame,
  and the weights line up with them. The analysis uses the **unconstrained feature model**
  (UFM), which treats the output of a highly expressive feature map as free variables and
  studies the last L layers on top, with MSE loss and weight decay.
- **Layer-wise Hessian (Thm 3.1).** At a global optimum the layer Hessian has rank K², with
  eigenvectors equal to Kronecker products of normalised class means of adjacent layers,
  µ̂c^(l+1) ⊗ µ̂c′^(l), and a closed-form common eigenvalue. Under MSE the outliers and
  mini-bulk sit together; App. B shows cross-entropy separates them, as Papyan observed.
- **Cross-class decomposition (Thm 3.2).** Papyan's split of the Fisher term into class /
  cross-class / within-class pieces is recovered with the right eigenvalue counts, each
  piece explaining one part of the spikes / mini-bulk / bulk picture.
- **Gradients (Thm 3.3).** The gradient lies in the span of only K of the outlier
  eigenvectors, the c = c′ ones, which explains the alignment Gur-Ari et al. reported.
- **Weights (Thm 3.4).** Each weight matrix has rank K, with all K singular values equal and
  singular vectors given by the class means.
- **Full Hessian (Thm 3.5–3.6).** In the deep limit the whole network's Hessian inherits the
  layer-wise K² outlier structure, and the rest of its normalised spectrum goes to zero.
- **ReLU (§4).** DNC is not globally optimal for ReLU, but among DNC solutions the best ones
  have non-negative features, act linearly, and the same theorems hold (Thm 4.3).
- **Experiments (§5).** A ResNet-20 with a fully connected head on MNIST (CIFAR-10 in App. G):
  predicted eigenvectors align with the true ones early in training, and the K² = 100
  outliers emerge from the bulk.

## Read with care

- **A limit, not a training trajectory.** Results hold at global optima of an idealised model:
  infinitely expressive features, interpolation of the training data, and (for the full
  Hessian) a depth limit. The authors use it to describe converged, heavily
  overparameterised networks, not training on the way there.
- **MSE and feature regularisation.** The main results use MSE loss and penalise the features
  directly rather than the parameters. Cross-entropy is handled in App. B; §5 checks that
  standard regularisation shows the same picture.
- **Classification with many samples per class.** The structure exists because there are K
  discrete classes to collapse onto. A regression model on a continuous target has no class
  means, so it is not clear how much carries over (regression variants of collapse exist,
  but are not analysed here).
- **Clean data.** The experiments are MNIST and CIFAR-10, where networks fit the training set
  exactly. Nothing here covers noisy, low-signal labels.

## Why it's in the library

**It is the bulk-plus-outliers story again, inside a network.** A sample correlation matrix
of stock returns is a Marchenko–Pastur bulk of noise plus a few outliers — the market mode
and sectors — that carry the structure
([[laloux-et-al-1999]], [[marchenko-pastur-1967]]). This paper shows a trained classifier's
Hessian has the same shape for an identifiable reason: the outliers come from the class
means, and everything else is near-flat. The same reading applies: count the outliers,
identify what generates them, and treat the bulk as directions the model does not use.

**It makes curvature something you can look at directly.** Flatness of the loss surface is
tied to generalisation and to methods like sharpness-aware minimisation. Here the sharp
directions are written down explicitly in terms of the learned representations, so
checking how far features have collapsed onto class means is a cheaper diagnostic than
computing Hessian eigenvalues. For a ranking or quantile-bucketed model, that check is the
practical takeaway: whether representations collapse onto the label buckets, and how many
effective directions are left.

**It sits beside the kernel papers in this folder.** The NTK picture
([[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]]) describes
networks whose features barely move; neural collapse is what happens when features move a
lot and training runs past interpolation. That is the rich end of
[[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]].

## Links

- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — lazy vs rich; collapse
  is a rich-regime, past-interpolation phenomenon
- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the opposite
  limit, where features stay fixed
- [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]]
  — another physics-style analysis of what feature learning does to network kernels
- [[nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail]] —
  spectra of a different matrix (the NTK), read for what training reaches
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — the
  interpolation regime that this paper's model assumes
- [[laloux-et-al-1999]] — bulk-plus-outliers in financial correlation matrices
- [[marchenko-pastur-1967]] — the noise bulk that the outliers stand out from
- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] — collapse in self-supervised learning, and the
  variance and decorrelation constraints that prevent it
