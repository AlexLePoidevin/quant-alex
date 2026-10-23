# Understanding Deep Learning Requires Rethinking Generalization

| | |
|---|---|
| **Authors** | Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals (MIT, Google Brain, Google DeepMind, UC Berkeley) |
| **Year** | 2017 |
| **Type** | Paper — ICLR 2017 (best paper award). arXiv:1611.03530v2, 15pp |
| **PDF** | `zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization.pdf` (in this folder) |
| **BibTeX** | `zhang2017rethinking` |
| **Status** | Reference — the random-labels experiment; read §2 and §5 |

## What it is

A set of **randomization tests** (§2): train standard image classifiers on data where the
link between input and label has been destroyed, and see what they fit.

- **Networks fit random labels perfectly.** Inception, AlexNet and MLPs on CIFAR-10 reach
  **100% training accuracy** on randomly assigned labels, with test accuracy at chance (~10%).
  On ImageNet, Inception reaches 95.2% top-1 training accuracy on a million random labels
  without retuning. Training takes only a small constant factor longer than on true labels.
- **They fit random inputs too.** Shuffled pixels, independently permuted pixels, and pure
  Gaussian noise images are all memorised.
- **Partial corruption.** As the fraction of random labels rises from 0 to 1, the networks
  still reach zero training error. Test error rises smoothly toward chance, so the
  generalisation gap is set entirely by the labels: same model, same optimiser, same
  hyperparameters.
- **Explicit regularisation is not the explanation (§3, Table 1).** Weight decay, data
  augmentation and dropout help test accuracy by a few points, but turning them off still
  leaves networks that generalise well, and turning them on does not stop them fitting random
  labels. Early stopping and batch normalisation (implicit regularisers) help modestly.
- **Finite-sample expressivity (Theorem 1).** A two-layer ReLU network with 2n + d weights can
  represent any labelling of n points in d dimensions. Once parameters exceed data points,
  capacity is not the constraint.
- **Linear models have the same puzzle (§5).** With d ≥ n, a linear model can fit any labels.
  SGD from zero converges to the **minimum-norm** interpolant (it stays in the span of the
  data), and Gaussian-kernel interpolation with no regularisation still generalises well on
  MNIST and CIFAR-10. But minimum norm does not predict generalisation either: on MNIST,
  wavelet preprocessing raises the norm (≈220 → 390) and halves test error.
- **Conclusion.** Rademacher complexity, VC dimension and uniform stability cannot explain
  why these models generalise, because the same model class and algorithm generalise on
  real labels and fail on random ones. Optimisation is easy whether or not the result
  generalises, so ease of optimisation is not the cause either.

## Read with care

- **Image classification with clean, learnable labels.** The puzzle is why networks that
  *can* memorise choose not to when real structure exists. Financial targets are mostly
  noise, closer to the paper's partially-corrupted case, where memorising is what happens.
- **A negative result, not a theory.** It shows what does not explain generalisation. Later
  work filled some of the gap: implicit bias of gradient descent, the NTK and kernel view
  ([[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]]), benign
  overfitting and double descent (Belkin et al. 2019; Bartlett et al. 2020).
- **"Regularisation doesn't matter" is overstated as a slogan.** Table 1 shows regularisers
  are worth a few points of test accuracy; the claim is only that they are not *necessary*
  for good generalisation on these benchmarks.

## Why it's in the library

**Training fit says nothing.** A model that can fit random labels will fit noise in returns
just as easily. In-sample IC, Sharpe or accuracy of a high-capacity model is not evidence of
anything until it is compared with what the same model achieves when the signal is removed.

**The randomization test is a practical tool.** Shuffle the labels (within each date, to keep
the cross-sectional structure), retrain with the same pipeline, and record the in-sample and
validation metrics. That gives the null distribution for your real result:
- if the shuffled-label model reaches a similar in-sample score, the model has the capacity
  to memorise and the in-sample number means nothing;
- the real model's out-of-sample score should sit clearly outside the shuffled-label
  distribution, a permutation test for the whole pipeline, including feature selection and
  tuning.

**Partial label noise is the financial regime.** The corrupted-label experiment shows test
error climbing as signal is replaced by noise while training error stays at zero. With noisy
targets, what matters is stopping before the model reaches the noise: early stopping, strong
shrinkage, and models (like shallow boosted trees) whose capacity is controlled directly.

## Links

- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — one later
  answer: wide networks trained by gradient descent behave like minimum-norm kernel regression
- [[wikipedia-neural-tangent-kernel]] — the kernel view, including interpolation and implicit
  regularisation
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — what happens to these models on tabular data
- [[conklin-et-al-2026-learning-is-forgetting]] — compression during training as another
  account of why networks generalise
