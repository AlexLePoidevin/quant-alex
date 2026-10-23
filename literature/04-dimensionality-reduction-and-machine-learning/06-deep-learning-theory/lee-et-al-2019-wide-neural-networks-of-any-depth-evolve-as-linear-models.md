# Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent

| | |
|---|---|
| **Authors** | Jaehoon Lee, Lechao Xiao, Samuel S. Schoenholz, Yasaman Bahri, Roman Novak, Jascha Sohl-Dickstein, Jeffrey Pennington (Google Brain) |
| **Year** | 2019 |
| **Type** | Paper — *Advances in Neural Information Processing Systems* 32 (NeurIPS 2019). arXiv:1902.06720v4, 28pp including supplement |
| **PDF** | `lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models.pdf` (in this folder) |
| **BibTeX** | `lee2019wide` |
| **Status** | Reference — the standard citation for the "lazy" / neural-tangent-kernel regime |

## What it is

A proof and a set of experiments showing that, as hidden layers get wide, training a deep
network by gradient descent is the same as training its **first-order Taylor expansion
around the initial weights**:

f_lin(x; θ) = f(x; θ₀) + ∇θ f(x; θ₀) · (θ − θ₀)

- **The model is linear in its parameters, not in its inputs.** The features are the
  gradients ∇θ f(x; θ₀), fixed at initialisation. Their inner product is the **neural tangent
  kernel** Θ(x, x′) = ∇θ f(x) ∇θ f(x′)ᵀ (Jacot et al. 2018). Training is then kernel
  regression with that fixed kernel.
- **Sufficient conditions (Theorem 2.1).** Below a critical learning rate η_critical,
  gradient-descent trajectories stay within O(n^−1/2) of the linearised trajectory, where *n*
  is the width. Fig. 1: weights and the empirical kernel barely move as width grows.
- **Closed form for squared loss.** The outputs follow linear ODEs with solution
  f_t = (I − e^(−ηΘt)) y on the training set, so training speed along each eigenvector of Θ is
  set by its eigenvalue.
- **Predictions are a Gaussian process (Theorem 2.2).** Over random initialisations, the
  trained network's outputs are a GP at every time *t*, with an explicit mean and covariance.
  It is **not** the Bayesian posterior: gradient descent and exact Bayesian inference (the
  NNGP) give different GPs.
- **Holds for any parameterisation** (standard or NTK); the effect comes from width.
- **Experiments.** Finite networks match their linearisation closely across fully-connected
  and convolutional nets and a wide ResNet, with SGD, momentum and minibatches, and with
  MSE and cross-entropy losses (Figs. 2–4). The authors computed the analytic NTK for ReLU and
  erf networks, and released code (neural-tangents).

## Read with care

- **"Wide enough" and "small learning rate" are doing the work.** The theorem needs a
  learning rate below η_critical and very large width. Practical networks trained with large
  learning rates, normalisation layers and long schedules can leave the linear regime.
- **In this regime the network learns no features.** The kernel is fixed at initialisation,
  so a lazy network is a kernel machine. Later work (Chizat–Oyallon–Bach 2019 on lazy
  training, Yang–Hu 2021 on feature learning) shows that what makes real networks better than
  kernels happens *outside* this regime. The paper itself notes that infinite-width kernels
  beat finite CNNs without pooling in some settings and lose in others (§6).
- **Experiments are on vision benchmarks** (MNIST, CIFAR-10), mostly with small training
  subsets. Nothing on noisy, non-stationary or tabular targets.

## Why it's in the library

**It tells you what a wide network is doing when it is trained conservatively: kernel
regression.** A wide MLP with a small learning rate on a feature panel is close to a kernel
method with a fixed, architecture-determined kernel. A kernel ridge regression or Gaussian
process with that kernel is a cheap, deterministic baseline it should beat before any
claim of learned representation is taken seriously.

**It explains the smoothness bias found in tabular benchmarks.** Training along each NTK
eigenvector runs at a speed set by its eigenvalue, and the large eigenvalues belong to smooth,
low-frequency functions. That is the spectral bias that
[[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
found makes networks miss irregular targets, which trees catch with splits.

**Early stopping is shrinkage.** With f_t = (I − e^(−ηΘt)) y, stopping at time *t* fits the
large-eigenvalue directions and leaves the small ones unfitted, much like ridge regression
on the kernel's eigenbasis. Where returns are mostly noise, the number of training steps is
a regularisation parameter and should be chosen on validation data like any other.

**Ensembles over random seeds have a known spread.** Theorem 2.2 gives the variance of
predictions across initialisations, which is the variance a seed ensemble averages away.

## Links

- [[kernel-pca]] — kernel methods with a fixed feature map, the class a lazy network falls into
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the empirical smoothness bias this paper's dynamics explain
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the other route to understanding architectures: through symmetry, not width
- [[conklin-et-al-2026-learning-is-forgetting]] — the opposite picture, where representations
  change a lot during training
