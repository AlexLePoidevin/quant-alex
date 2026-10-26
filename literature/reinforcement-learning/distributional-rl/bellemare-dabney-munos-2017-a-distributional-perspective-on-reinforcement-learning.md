# A Distributional Perspective on Reinforcement Learning

| | |
|---|---|
| **Authors** | Marc G. Bellemare, Will Dabney, Rémi Munos (DeepMind) |
| **Year** | 2017 |
| **Type** | Paper — *Proceedings of the 34th International Conference on Machine Learning* (ICML 2017), PMLR 70. arXiv:1707.06887v1 [cs.LG], 19pp including appendices |
| **PDF** | `bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `bellemare2017distributional` |
| **Status** | Reference — the founding paper of this folder; read §1–4 and §6, skim the Atari results in §5 |

## What it is

Standard reinforcement learning learns the **expected** return Q(x, a). This paper argues that
the object to learn is the whole **distribution** of the random return Z(x, a), the "value
distribution", and gives both the theory for it and a practical algorithm (C51).

- **Distributional Bellman equation (§1, §3.3).** Z(x, a) has the same law as
  R(x, a) + γ Z(X′, A′). Three sources of randomness enter: the reward, the transition, and
  the next-state return. The value function is just the mean of this distribution.
- **Policy evaluation is well behaved (Lemma 3).** For a fixed policy, the distributional
  Bellman operator is a γ-contraction in a maximal form of the **Wasserstein metric**, so
  iterating it converges to the true return distribution and all its moments. **The choice of
  metric matters**: the same operator is not a contraction in total variation, KL divergence
  or Kolmogorov distance.
- **Control is not (§3.4).** The distributional optimality operator still makes the *mean*
  converge to Q* exponentially fast (Lemma 4), but it is **not a contraction in any metric
  over distributions** (Prop. 1), need not have a fixed point (Prop. 2), and in general only
  converges to a set of "nonstationary" optimal distributions (Thm 1). Several return
  distributions share the same optimal mean, and greedy tie-breaking moves between them.
- **The algorithm (§4, Alg. 1).** Represent each return distribution as probabilities on a
  fixed comb of N atoms between V_MIN and V_MAX (N = 51 gives "C51"). Apply the sampled
  Bellman update to each atom, **project** the shifted atoms back onto the comb by splitting
  mass between neighbours, and minimise the cross-entropy to that projected target. This turns
  the Bellman update into multiclass classification.
- **Why not minimise Wasserstein directly (§4.2, Prop. 5).** The sample Wasserstein loss
  gives **biased gradients**, so it cannot be minimised by SGD from single transitions. The
  projection plus KL is a workaround that leaves a gap between theory and algorithm.
- **Evidence (§5).** On 57 Atari games, a DQN that outputs atom probabilities but still acts
  greedily on the mean beats DQN and its common improvements; more atoms helps
  monotonically (Fig. 3). The learned distributions are often multimodal, separating a
  "losing" outcome from a "surviving" one instead of averaging them (Fig. 4).
- **Why it helps (§6.1).** The authors' candidate reasons: less policy "chattering" under
  approximation, better handling of state aliasing, a rich set of auxiliary predictions, and
  an easier optimisation target.

## Read with care

- **The agent is still risk-neutral.** It acts on the mean. The gains come from learning a
  better representation, not from using the tails. Risk-sensitive control is left as future
  work, and the control theory (Thm 1) is discouraging.
- **The support is a hyperparameter.** V_MIN and V_MAX must be set in advance (±10 here), with
  a uniform grid. Returns outside the range are clipped onto the end atoms. Returns with a
  wide or shifting scale need rescaling.
- **Theory and algorithm do not match.** The contraction is in Wasserstein, but the algorithm
  minimises a projected KL. The quantile papers in this folder were written to close that gap.
- **The explanations in §6.1 are hypotheses.** The experiments show that it works, not why.
- **An erratum** corrects the headline mean score from 1010% to 701% of human because one game
  ran past the usual 30-minute cap. Mean scores across games are driven by outliers; the
  median (178%) is the more honest summary.

## Why it's in the library

**It separates the distribution of an outcome from uncertainty about its mean.** The paper is
explicit that Z describes *intrinsic* randomness, not parameter uncertainty. Return
forecasting has the same split: the dispersion of next-period returns is mostly irreducible
noise, and a model's estimation error is a separate problem. Keeping the two apart is the
first step to handling either.

**The mean can converge while the distribution does not.** Lemma 4 against Theorem 1 is a
clean example of a model that looks stable on its first moment while its tails wander. For
any model whose risk numbers matter, check convergence of the quantities you will actually
use, not only of the point forecast.

**Learning the distribution can improve the mean forecast.** C51 still acts on the mean, yet
trains better. The same idea applies to cross-sectional models on noisy returns: predicting
the conditional distribution (bins or quantiles of forward return) is a richer, better-posed
training target than a single squared-error regression, even if the final ranking uses the
mean.

**It is the vocabulary for the rest of the folder.** Wasserstein contraction, projection onto
a parametric family, and the bias of sample Wasserstein gradients reappear in every later
paper here.

## Links

- [[dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression]] — closes
  the theory–algorithm gap by learning quantiles with quantile regression
- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]] —
  the full quantile function, and the first real use of the tails for risk-sensitive policies
- [[duan-et-al-2023-distributional-soft-actor-critic-with-three-refinements]] — the
  distributional idea carried to continuous control
- [[rockafellar-uryasev-2000]] — CVaR, the tail functional that a learned return distribution
  makes available
- [[wackerly-2008-mathematical-statistics]] — distribution functions, quantiles and moments
  used throughout
