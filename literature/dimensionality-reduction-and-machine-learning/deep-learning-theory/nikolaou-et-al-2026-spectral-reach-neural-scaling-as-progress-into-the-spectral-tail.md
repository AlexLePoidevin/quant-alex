# Spectral Reach: Understanding Neural Scaling as Progress into the Spectral Tail

| | |
|---|---|
| **Authors** | Konstantin Nikolaou, Jonas Scheunemann, Sven Krippendorf, Samuel Tovey, Christian Holm (Institute for Computational Physics, University of Stuttgart; DAMTP and Physics, University of Cambridge) |
| **Year** | 2026 (v1 29 May; v2 3 August) |
| **Type** | Preprint — arXiv:2605.31244v2 [cs.LG, physics.comp-ph], CC BY 4.0. 30pp including appendices |
| **PDF** | `nikolaou-et-al-2026-spectral-reach-neural-scaling-as-progress-into-the-spectral-tail.pdf` (in this folder) |
| **Link** | https://arxiv.org/abs/2605.31244 (HTML: https://ar5iv.labs.arxiv.org/html/2605.31244) |
| **BibTeX** | `nikolaou2026spectral` |
| **Status** | Reference — recent, not yet peer-reviewed; read §3–5 |

## What it is

A cheap way to measure **which part of the neural tangent kernel's eigenspectrum a network
is learning from at each training step**, and what that shows about why bigger models reach
lower loss.

- **The LNP decomposition (§3).** For a gradient step, the linearised loss decrease is
  δL = ‖∇θ L‖². Writing ∇θ L = (∇θ f)ᵀ ∇f L and the empirical NTK as Θ = ∇θ f (∇θ f)ᵀ, it
  factors into three parts:

  δL = χ_loss · χ_net · χ_pos

  - **χ_net = Tr(Θ)**: how sensitive the outputs are to the parameters (network scale);
  - **χ_loss = ‖∇f L‖²**: how far predictions are from the targets (loss scale);
  - **χ_pos = Σₖ γₖ² pₖ ∈ [0, 1]**, the **spectral position**: γₖ² is the share of the loss
    gradient along the k-th eNTK eigenvector and pₖ is that eigenvalue as a share of the
    trace. Near 1, learning is driven by the dominant modes; near 0, by the weak tail.
- **No kernel needed.** δL, χ_net and χ_loss come from per-sample gradients, so
  χ_pos = δL / (χ_net χ_loss) exactly, at under 2× training cost. Explicit eNTKs are
  infeasible at this scale. χ_pos is closely related to kernel-target alignment (Cristianini
  et al. 2001). Code is in the open-source `perspic` package.
- **Validation.** On random-feature models with power-law data spectra (eigenvalues ∝ k^−β),
  the measured components match theory: χ_net and χ_loss constant, χ_pos following the
  predicted scaling in β (Fig. 3).
- **Findings (§4, Fig. 1).** Llama 2 models (100K–134M parameters) on SimpleStories, and on
  next-pixel prediction on CIFAR-5M, follow clean compute scaling laws. Along the way:
  1. **χ_pos falls by orders of magnitude during training.** Strong modes converge first and
     stop contributing gradient, and learning moves into the tail: the spectral bias of
     the NTK picture, measured in real transformers.
  2. **Larger models reach lower χ_pos.** Small models plateau; large ones keep going. The
     authors call this **spectral reach**: the capacity to learn from weak eigenmodes,
     which they propose as the reason bigger models get lower loss. The ordering survives
     μP parameterisation, which holds feature-learning strength fixed across widths.
- **Feature learning enables it (§5).** Linear probes on pre-trained backbones reach lower
  χ_pos than probes on random backbones (Fig. 4). In fully trained models χ_net = Tr(Θ) rises
  during training, offsetting about one order of magnitude of the χ_pos fall. In frozen
  models it stays constant (Fig. 5), and learning stalls as χ_pos drops.
- **Outlook (§7).** Increase spectral reach either by pushing optimisation into the tail
  faster (learning-rate schedules, gradient scaling) or by reshaping the spectrum so the
  tail is easier to reach (architecture, μP or other initialisation).

## Read with care

- **A preprint, with small models.** At most 134M parameters, two datasets (plus vision
  transformers in an appendix), well-tuned settings per size. The authors ask for broader
  validation.
- **Correlation with scale, not a proven mechanism.** The paper argues the direction
  (spectral bias drives the χ_pos fall) but says that a mechanism would need interventions
  such as clamping χ_pos, which it does not run.
- **Single-pass training on large data.** Every example is seen once, so learning the tail
  improves test loss as well. With repeated epochs on a small dataset, the smallest
  eigenmodes are where label noise sits, and "reaching" them is memorisation
  ([[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]]).
  The paper notes χ_pos can turn negative from stochasticity and overfitting.
- **First-order only.** The non-linear correction to each step's loss change is not analysed.

## Why it's in the library

**It measures spectral bias in real networks.** [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]]
predicts that networks learn the large-eigenvalue (smooth) directions first, and
[[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
found that bias hurting them on tabular data. χ_pos tracks it as training runs.

**On noisy targets, the spectral tail is double-edged.** In returns data, a large part of
the weak eigenmodes is noise. Falling χ_pos on the *training* set while validation loss stops
improving is a direct signal that the model has moved from structure to noise, an
alternative early-stopping signal to the validation curve alone. Tracking χ_pos on train
and validation batches together would show where that happens.

**Feature learning versus frozen features.** The finding that only feature-learning models
keep making progress is the counterpoint to the lazy (NTK) regime: if a network's χ_net stays
flat during training, it is behaving like a kernel model, and a kernel regression baseline
should match it ([[wikipedia-neural-tangent-kernel]]).

## Links

- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — what µP and the
  lazy/rich distinction mean
- [[bordelon-pehlevan-2023-dynamics-of-finite-width-kernel-and-prediction-fluctuations-in-mean-field-neural-networks]]
  — feature learning also pulls finite networks toward their infinite-width limit
- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the
  linearised (NTK) dynamics the LNP decomposition is built on
- [[wikipedia-neural-tangent-kernel]] — definitions, lazy vs feature-learning regimes
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — what
  reaching the tail means when the tail is label noise
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — spectral bias as a weakness on irregular tabular targets
- [[conklin-et-al-2026-learning-is-forgetting]] — another measurement of how representations
  change during training
- [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]] — outlier structure in the Hessian, gradient and
  weight spectra of trained classifiers
