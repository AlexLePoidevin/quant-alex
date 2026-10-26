# Radial Bayesian Neural Networks: Beyond Discrete Support In Large-Scale Bayesian Deep Learning

| | |
|---|---|
| **Authors** | Sebastian Farquhar (OATML, University of Oxford), Michael A. Osborne (MLRG, University of Oxford), Yarin Gal (OATML, University of Oxford) |
| **Year** | 2020 |
| **Type** | Paper — *Proceedings of the 23rd International Conference on Artificial Intelligence and Statistics* (AISTATS 2020), PMLR 108; arXiv:1907.00865v4 [stat.ML], 18pp including appendices |
| **PDF** | `farquhar-osborne-gal-2020-radial-bayesian-neural-networks.pdf` (in this folder) |
| **BibTeX** | `farquhar2020radial` |
| **Status** | Reference — read §1, §3.1 and §5 for the soap-bubble argument; §4.2 carries an erratum |

## What it is

Bayesian neural networks put a distribution over the weights instead of a point estimate,
so a prediction comes with an uncertainty. The cheap, standard way to fit one, mean-field
variational inference (MFVI, an independent Gaussian per weight), tends to fail on large
models and to be fragile to hyperparameters. This paper identifies a sampling reason and
fixes it with a one-line change to how weights are sampled.

- **The soap bubble (§3, Fig. 1, App. A).** In D dimensions almost all the mass of a
  Gaussian sits in a thin shell at radius about σ√D from the mean, not near the mean. For
  a layer with many weights, **every weight sample is far from the mean and far from every
  other sample**, so the gradient of the data-fit term has very high variance.
- **The radial posterior (§3.1, Eq. 3).** Sample a direction uniformly on the sphere and a
  radius from |N(0, 1)|, independent of dimension:
  w = µ + σ ⊙ (ε/‖ε‖) · r. This costs one normalisation and one scalar draw more than MFVI.
  The entropy term is the same as MFVI up to a constant (§3.2), so the loss is as easy to
  compute.
- **Full support (§1–2).** MC dropout, deep ensembles and SG-MCMC samples all describe the
  posterior with a finite set of points, assigning zero probability almost everywhere. The
  authors argue this is overconfident and makes them **unusable as a prior for further
  updating**. A radial posterior is a proper density and can be.
- **Retinopathy screening (§4.1, Table 1, Fig. 3).** A ~15M-parameter VGG-style model on
  512×512 eye images. Uncertainty is judged by referring the least-confident 10–30% of cases
  to an expert and scoring the rest. The radial BNN beats MC dropout and MFVI (MFVI without
  tweaks barely learns), is **better calibrated**, and an ensemble of three radial BNNs beats
  a three-member deep ensemble.
- **Robustness to hyperparameters (§4.1.3, Fig. 4).** Over 86 random configurations on a
  smaller version, 82% of MFVI runs learned almost nothing versus 39% for radial; 44% of
  radial runs reached good AUC versus 11% for MFVI.
- **Why the MFVI tweaks work (§5, Figs. 6–7).** Gradient variance under MFVI explodes once
  weight standard deviations pass about 0.3, while the KL term pulls them towards 1. Training
  then trades away data fit to lower the prior term. The usual fixes — tiny initial
  variances, pre-training the means, down-weighting the KL, early stopping — all keep
  variances small, which amounts to fitting a nearly deterministic network.

## Read with care

- **The continual-learning result has a known error.** The authors' notes in §4.2 and App. C
  say the cross-entropy term for a radial *prior* is missing a Jacobian term, and the
  experiments used the flawed derivation. Treat the "posterior as prior prevents forgetting"
  result (Fig. 5) as unconfirmed.
- **Built for large models, not small tabular ones.** Footnote 3 and App. E say radial BNNs,
  like MFVI, do not match more expensive methods on the small UCI regression benchmarks. The
  soap-bubble problem is a high-dimension problem.
- **Still mean-field.** The posterior ignores correlations between weights; the change is to
  the shape of the noise, not its dependence structure.
- **One main real task.** The evidence is a single medical-imaging classification problem,
  with hyperparameters chosen by Bayesian optimisation.

## Why it's in the library

**It is about trusting a model's uncertainty, not only its point forecast.** A model whose
predictions come with a calibrated spread can be used to size positions, skip low-confidence
calls, or flag inputs unlike the training data. The paper's evaluation is exactly that
use: hand off the least-confident cases and check that accuracy on the rest improves. The
same check — does performance rise as low-confidence predictions are dropped? — is a
cheap test of any uncertainty estimate on a forecasting model.

**It explains a high-dimensional trap worth recognising.** "Most of a Gaussian is far from
its mean" is the same concentration-of-measure fact behind distance metrics losing meaning
in high dimensions. Noise injected as independent Gaussians across many weights or many
features does not behave like small perturbations around the centre.

**It connects uncertainty to continual updating.** Re-using yesterday's posterior as today's
prior is the Bayesian answer to learning on a stream without forgetting. Methods with
discrete support (dropout, ensembles) cannot do this directly. The experiment that tests it
here is flagged as flawed, so the point stands as an argument rather than a result.

## Links

- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — the
  forgetting problem that posterior-as-prior updating is meant to address
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — where prior-based continual-learning methods sit among the alternatives
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — the same concentration of
  measure in high dimensions, seen through distances
- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]]
  — a different kind of uncertainty: spread of outcomes rather than spread of weights
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — why
  large networks fitting their training data says little about their confidence elsewhere
