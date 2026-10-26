# Introduction to Latent Variable Energy-Based Models: A Path Towards Autonomous Machine Intelligence

| | |
|---|---|
| **Authors** | Anna Dawid (ICFO Barcelona; University of Warsaw), Yann LeCun (NYU Courant; Meta FAIR) |
| **Year** | 2023 (v1, 5 June) |
| **Type** | Lecture notes — Les Houches Summer School on Statistical Physics and Machine Learning, July 2022. arXiv:2306.02572v1 [cs.LG], 28pp |
| **PDF** | `dawid-lecun-2023-introduction-to-latent-variable-energy-based-models.pdf` (in this folder) |
| **BibTeX** | `dawid2023introduction` |
| **Status** | Reference — an accessible tutorial; §3–4 and §6 are the core |

## What it is

A written-up version of LeCun's 2022 Les Houches lectures. It explains the ideas behind his
proposal for "autonomous machine intelligence" (LeCun, 2022, *A Path Towards Autonomous
Machine Intelligence*) by building up its main component, the **joint embedding predictive
architecture** (JEPA), from energy-based models.

- **The motivation (§2).** Supervised learning needs many labels and reinforcement learning
  many trials. Self-supervised learning — predicting hidden parts of the input from the
  visible parts — supplies far more information per sample. But a model trained to make a
  single prediction of something uncertain predicts the average (blurry images). Normalised
  probability distributions over high-dimensional continuous outputs are intractable, so the
  notes propose giving them up.
- **Energy-based models (§3).** Instead of a probability, the model assigns a scalar
  **energy** F(x, y): low for compatible pairs, high otherwise. Inference is finding the y
  with the lowest energy. Probabilities are recoverable through the Gibbs–Boltzmann
  distribution, but the partition function is what makes them intractable. Only the
  ordering of energies matters for a decision — the notes use chess move scoring as the
  example.
- **Latent variables (§3.2).** A hidden variable z carries what is in y but not in x (pose,
  lighting, the behaviour of other drivers), so one x can have several valid predictions.
  Its **information capacity must be limited**, or the model puts everything in z.
- **Training without collapse (§4).** A model that can give several answers can also
  **collapse**: a flat energy surface that gives every y the same low energy (two encoders
  outputting a constant, an autoencoder learning the identity). Two remedies:
  - **contrastive** methods push down the energy of data and push up the energy of generated
    negatives (hinge loss, InfoNCE, GANs; maximum likelihood is a special case). They need
    negatives everywhere, which scales badly with dimension;
  - **regularised / architectural** methods limit the volume of space that can have low
    energy. **PCA, k-means, Gaussian mixtures, sparse coding and bottleneck or variational
    autoencoders** are all instances, each limiting capacity a different way.
- **Historical examples (§5).** Hopfield networks (Hebbian training, spurious memories),
  Boltzmann and restricted Boltzmann machines (contrastive training by MCMC sampling),
  denoising and masked autoencoders (very successful for text, less for images).
- **JEPA (§6).** Encode x and y separately and predict the **representation** of y from the
  representation of x, with a latent z for what is missing. Predicting in representation
  space lets the encoders drop details that cannot be predicted. Training minimises
  prediction error while keeping the representations informative and z small. The example
  regulariser is **VICReg**: keep each component's batch variance above a threshold, and
  push the covariances between components to zero. Related methods: BYOL, SimSiam, Barlow
  Twins. **Hierarchical JEPA** stacks them, with detailed short-horizon predictions at low
  levels and coarser long-horizon ones above.

## Read with care

- **A research programme, not results.** The notes present LeCun's proposed architecture and
  argue for it; there are no experiments or benchmarks. The claim that regularised methods
  will beat contrastive ones and probabilistic models in high dimensions is a position, not
  something shown here.
- **An introduction, not a survey.** Each method gets a paragraph and the citations are
  pointers. VICReg, Barlow Twins and the JEPA papers themselves are where the details are.
- **Written in 2022–23.** Image and video JEPAs (I-JEPA, V-JEPA) have since been published
  and are not covered.

## Why it's in the library

**It puts PCA and a modern representation learner on one axis.** Every method in this
section is a way of limiting how much of the space a model can call "normal": PCA by rank,
k-means by a discrete set, autoencoders by a bottleneck, VICReg by variance and
decorrelation constraints. Reading [[ica]], [[kernel-pca]] or the autoencoder factor model
[[gu-kelly-xiu-2021]] through this lens makes clear what each one is assuming.

**Collapse is a failure to check for.** A model that learns embeddings without labels can make
its loss small by producing the same output for everything. VICReg's fix — keep each
dimension's variance up and the dimensions decorrelated — is a correlation-matrix condition,
the same object as in the random-matrix notes. If returns or characteristics are ever
embedded without labels, measure the variance and effective rank of the embeddings, not
just the training loss.

**Predict what is predictable.** JEPA's argument is that predicting raw outputs forces a
model to average over noise it cannot forecast, while predicting a learned representation
lets it ignore that noise. That is the same tension as forecasting noisy returns directly
versus ranking them, or predicting a coarser target. It is the same trade-off as the
Information Bottleneck in [[conklin-et-al-2026-learning-is-forgetting]]: keep what predicts,
drop the rest.

## Links

- [[conklin-et-al-2026-learning-is-forgetting]] — compression of representations measured
  information-theoretically; JEPA's regularisers are a version of the same trade-off
- [[ica]], [[kernel-pca]] — classical unsupervised representations; PCA is the notes' first
  example of a regularised energy-based model
- [[gu-kelly-xiu-2021]] — an autoencoder applied to asset pricing; a bottleneck limits what
  it can reconstruct
- [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]] — a different
  kind of collapse: supervised features collapsing onto class means
- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — how far a network
  learns features at all, which representation learning depends on
- [[choi-2022-the-curious-case-of-commonsense-intelligence]] — the language-model route to common sense: generative, defeasible
  inference through text rather than world models
