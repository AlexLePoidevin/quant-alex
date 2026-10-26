# A Robust Quantile Huber Loss with Interpretable Parameter Adjustment in Distributional Reinforcement Learning

| | |
|---|---|
| **Authors** | Parvin Malekzadeh, Konstantinos N. Plataniotis (Department of Electrical and Computer Engineering, University of Toronto); Zissis Poulos, Zeyu Wang (Rotman School of Management, University of Toronto) |
| **Year** | 2024 |
| **Type** | Paper — *ICASSP 2024*, IEEE International Conference on Acoustics, Speech and Signal Processing. arXiv:2401.02325v2 [cs.LG], 6pp |
| **PDF** | `malekzadeh-et-al-2024-a-robust-quantile-huber-loss-in-distributional-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `malekzadeh2024robust` |
| **Status** | Reference — a 4-page conference paper; read §3 and §4.2 |

## What it is

QR-DQN, IQN and FQF all train with the quantile Huber loss at a fixed threshold κ = 1. This
paper gives that threshold a meaning. It derives the loss as an asymmetric **1-Wasserstein
distance between two Gaussians** that model noise in the predicted and target quantiles,
which produces a smoother, more outlier-robust generalised loss — and says how to set κ from
the data.

- **Reading the Huber term as a distance (§3).** The usual pairwise term is the 1-Wasserstein
  distance between two Diracs, one at the predicted quantile and one at the target. That
  implicitly assumes both are noise-free.
- **Adding noise (Eq. 6).** Let the target and predicted quantiles carry independent
  zero-mean Gaussian noise with standard deviations σ1 and σ2. The 1-Wasserstein distance
  between the two Gaussians has a closed form in the standard normal CDF and an exponential.
  Shifted to be zero at zero error, this gives the cost C^b_GL(u) with **b = |σ1 − σ2|**, and
  the **generalised quantile Huber loss** L^GL_b (Eq. 7).
- **Properties.** Smoother near zero than Huber, and **less sensitive to outliers**: the
  exponential term fades and the CDF bounds the penalty for large errors.
- **Link to the classical loss (Eq. 8).** A second-order expansion for small errors and a
  large-error approximation give L^GL-A, which is quadratic inside |u| < b and linear outside:
  **the ordinary quantile Huber loss with κ = b**. So κ can be set to the estimated gap in
  noise levels rather than grid-searched.
- **Atari (§4.1, Table 1).** Swapping the loss into QR-DQN and FQF on 55 games, with b
  estimated from batch sample standard deviations: the generalised loss gives small gains
  (QR-DQN median 193% → 209%; FQF 272% → 281%).
- **Option hedging (§4.2, Fig. 1).** In a SABR-simulated gamma–vega hedging task with 0.5%
  transaction costs and a CVaR95 objective, the approximate loss converges faster than the
  D4PG quantile baseline, and the estimated b settles near κ ≈ 2 — the value that a grid
  search finds best, not the default of 1.

## Read with care

- **Short paper, thin evidence.** Atari gains are a few points of median score, with no seeds,
  confidence intervals or significance reported. The hedging result is a single simulated
  market model and a training curve.
- **The Gaussian noise model is an assumption.** It is what makes the closed form possible.
  Real TD-target noise is neither Gaussian nor independent of the prediction. The quantity
  b = |σ1 − σ2| is also odd as a noise scale: it vanishes when both sides are equally noisy.
- **How σ1 and σ2 are estimated is brief.** "Sample standard deviation averaged across
  batches" leaves room for interpretation; the code is the reference.
- **Robustness is argued, not measured.** There is no experiment with injected outliers.

## Why it's in the library

**κ is a noise-scale parameter, so set it from the noise.** Anyone fitting quantiles to
returns with a Huberised pinball loss has this hyperparameter, and its right value scales
with the noise in the target. Tying it to an estimate of that noise, and letting it adapt as
training goes on, is a sensible default — more so when return volatility changes over time
and a fixed threshold means different things in calm and stressed periods.

**A worked finance example.** The hedging experiment is one of the few places in this folder
where distributional RL is applied to a market problem with a CVaR objective and
transaction costs. It is simulated, but it shows the default κ = 1 being wrong for that
problem by a factor of two.

**A bounded-influence quantile loss.** Return data have heavy tails and occasional bad prints.
A loss whose penalty saturates for very large errors limits how much a handful of extreme
days can move a fitted quantile — worth comparing against the plain Huber loss when training
tail-quantile models.

## Links

- [[dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression]] — where
  the quantile Huber loss and the fixed κ = 1 come from
- [[yang-et-al-2019-fully-parameterized-quantile-function-for-distributional-reinforcement-learning]]
  — FQF, one of the two agents the new loss is tested in
- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]] —
  another user of the same loss and default threshold
- [[duan-et-al-2023-distributional-soft-actor-critic-with-three-refinements]] — a different fix
  for scale sensitivity: tie the clipping bound to the learned spread
- [[rockafellar-uryasev-2000]] — the CVaR objective used in the hedging experiment
