# Distributional Reinforcement Learning with Quantile Regression

| | |
|---|---|
| **Authors** | Will Dabney (DeepMind), Mark Rowland (University of Cambridge; work done at DeepMind), Marc G. Bellemare (Google Brain), Rémi Munos (DeepMind) |
| **Year** | 2018 |
| **Type** | Paper — *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (AAAI 2018). arXiv:1710.10044v1 [cs.AI], 14pp including appendices |
| **PDF** | `dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression.pdf` (in this folder) |
| **BibTeX** | `dabney2018distributional` |
| **Status** | Reference — short and central; read it all, the appendix proofs are optional |

## What it is

C51 proved its theory in the Wasserstein metric but trained with a projected KL loss. This
paper closes the gap. It **"transposes" the parameterisation**: instead of learning
probabilities on fixed return values, it fixes N equal probabilities and learns their
**locations**, which are quantiles, using quantile regression. The resulting agent is QR-DQN.

- **Quantile distribution (Eq. 7).** Z_θ(x, a) is a uniform mixture of N Diracs at
  θ_1(x, a), …, θ_N(x, a). No bounds on the support, no fixed grid, no projection step.
- **Which quantiles (Lemma 2).** The N locations that minimise 1-Wasserstein distance to a
  target distribution are the quantiles at the **midpoints** τ̂_i = (2i − 1)/2N, not at i/N.
- **How to learn them.** The sample Wasserstein loss has biased gradients, and that stays
  true for the quantile parameterisation (Prop. 1). But **quantile regression** — the pinball
  loss ρ_τ(u) = u(τ − 1{u < 0}) from Koenker's econometrics — gives unbiased sample gradients
  for each quantile. Minimising the sum over midpoints therefore minimises W1 by SGD.
- **Contraction (Prop. 2).** The quantile projection composed with the Bellman operator is a
  γ-contraction in the ∞-Wasserstein metric, so the projected algorithm has a unique fixed
  point. It is not, in general, a contraction in W_p for p < ∞ (App. Lemma 5).
- **Quantile Huber loss (Eqs. 9–10).** The pinball loss has a constant gradient however small
  the error. The authors replace it near zero with a quadratic: an asymmetric Huber loss
  with threshold κ. κ = 1 works best on Atari (QR-DQN-1).
- **QR-DQN (Alg. 1).** DQN with an |A| × N output head, the quantile Huber loss summed over
  all pairs of current and target quantiles, and Adam. The only new hyperparameter is N (200
  in the experiments).
- **Evidence.** On a windy gridworld, QRTD learns the multimodal return distribution of the
  start state and converges in W1 to Monte Carlo ground truth (Fig. 3). On 57 Atari games,
  QR-DQN-1 reaches mean 915% / median 211% of human versus C51's 701% / 178% (Table 1).

## Read with care

- **Still risk-neutral.** Actions are greedy on the mean of the quantiles. The paper names
  risk-sensitive policies as the main future direction.
- **κ is a heuristic.** The quantile Huber loss is no longer an exact quantile loss: inside
  [−κ, κ] it estimates something between a quantile and an expectile. The value of κ was
  chosen by experiment; see the 2024 Huber paper in this folder.
- **Uniform, fixed quantile fractions.** Equal spacing in probability puts few points in the
  tails. Better tail resolution needs larger N or learned fractions (IQN, FQF).
- **Overestimation bias is not addressed.** The authors expect QR-DQN to inherit DQN's
  max-operator bias.
- **Benchmark evidence.** Results are best-agent scores on deterministic Atari games, with
  hyperparameters tuned on five training games and a single seed for the test protocol.

## Why it's in the library

**It is quantile regression, the econometric tool, inside a learning loop.** The pinball loss
and the midpoint result are the parts to keep. They are exactly what you use to forecast
conditional quantiles of returns, to build VaR estimates by regression, or to train a model
on return buckets. The paper is a clear statement of why the pinball loss gives unbiased
gradients for quantiles when the Wasserstein loss itself does not.

**A set of quantiles is a usable risk object.** N equally weighted quantile locations give
direct estimates of VaR at any level and of CVaR as the average of the lower ones. A
forecast in this form plugs straight into tail-risk constraints, unlike a mean and a
variance.

**The Huber trade-off is a noise trade-off.** On heavy-tailed, noisy return data the choice
between pinball, squared and Huber-type losses decides how much a few extreme observations
move the fit. This paper sets κ by hand; it is worth tuning it, or estimating it, rather than
taking the default.

## Links

- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] — the
  theory this paper makes trainable
- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]] —
  replaces the fixed N quantiles with a learned quantile function
- [[yang-et-al-2019-fully-parameterized-quantile-function-for-distributional-reinforcement-learning]]
  — learns where the quantile fractions should sit as well
- [[malekzadeh-et-al-2024-a-robust-quantile-huber-loss-in-distributional-reinforcement-learning]]
  — a principled way to set the κ this paper fixes at 1
- [[rockafellar-uryasev-2000]] — CVaR as an average of lower quantiles, which a quantile
  forecast gives directly
- [[wackerly-2008-mathematical-statistics]] — quantiles, inverse CDFs and order statistics
