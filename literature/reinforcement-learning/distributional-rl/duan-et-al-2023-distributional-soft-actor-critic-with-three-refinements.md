# Distributional Soft Actor-Critic with Three Refinements

| | |
|---|---|
| **Authors** | Jingliang Duan (University of Science and Technology Beijing), Wenxuan Wang, Liming Xiao, Jiaxin Gao, Shengbo Eben Li, Chang Liu, Ya-Qin Zhang, Bo Cheng, Keqiang Li (Tsinghua University; Liu at Peking University; Xiao at USTB) |
| **Year** | 2023 (v1); v5 revised 1 February 2025 |
| **Type** | Paper — journal article (IEEE; the arXiv copy does not name the venue). arXiv:2310.05858v5 [cs.LG], 12pp |
| **PDF** | `duan-et-al-2023-distributional-soft-actor-critic-with-three-refinements.pdf` (in this folder) |
| **BibTeX** | `duan2023distributional` |
| **Status** | Reference — read §3.2 and §4 (the three refinements) and §5.3 (ablations); skip §6 |

## What it is

The Atari papers in this folder learn return distributions for discrete actions. DSAC brings
the idea to **continuous control** inside soft actor-critic: the critic learns a
**Gaussian** return distribution N(Q, σ²) rather than a scalar Q. The original version
(DSACv1) reduced Q-value overestimation but trained unstably and needed reward rescaling
per task. This paper adds three fixes (DSAC-T, or DSACv2).

- **The critic gradient splits in two (§3.2, Eq. 11).** The Gaussian log-likelihood gradient
  has a **mean-related** term, the TD error scaled by 1/σ², and a **variance-related** term
  with the squared TD error. Both use a *random* target return y_z drawn from the next-state
  distribution, so both are noisy; the squared term can explode. DSACv1 clipped y_z to
  Q ± b in the variance term only, with a fixed b.
- **Refinement 1 — expected value substituting (§4.1, Eq. 18).** In the mean term, replace
  the random target y_z with its expectation, the ordinary soft Q target y_q. The mean update
  then matches SAC's, up to a 1/σ² factor. The variance term still uses the sampled return.
- **Refinement 2 — twin value distributions (§4.2).** A distributional version of clipped
  double Q-learning: train two critics and use the one with the **smaller mean** for targets
  and for the actor. This trades overestimation for slight underestimation, which the
  authors argue is safer because underestimated actions are avoided and do not propagate.
- **Refinement 3 — variance-based gradient adjustment (§4.3, Eqs. 23–27).** Set the clipping
  bound adaptively, **b = ξ · E[σ]** with ξ = 3 by the three-sigma rule, and multiply the
  critic loss by ω = E[σ²] so the 1/σ² scaling of the mean update cancels on average. Both are
  tracked by moving averages. This removes the dependence on reward scale.
- **Evidence (§5).** Twelve Gym/MuJoCo tasks with five seeds and shared hyperparameters:
  DSAC-T matches or beats SAC, TD3, DDPG, PPO and TRPO on all of them (Table 2) and has the
  smallest or slightly negative value bias on most (Table 3). Ablations: removing either of
  the first two refinements hurts stability on Humanoid (Fig. 4); with a fixed bound, the
  agent fails at reward scales 0.01 and 0.1, while DSAC-T is flat across scales (Fig. 5).
  §6 deploys a sim-trained policy on a wheeled robot.

## Read with care

- **A Gaussian return distribution.** One mean and one standard deviation per state–action:
  no skew, no fat tails, no multimodality. It captures spread, not shape — the opposite
  trade-off to the quantile methods in this folder.
- **The distribution is mainly a tool against overestimation.** The policy maximises the
  (min-of-twins) mean plus entropy. Nothing here uses σ for risk-sensitive decisions.
- **Theory is inherited.** Convergence is the DSPI result from DSACv1 under tabular
  assumptions; the refinements are algorithmic and come with no new guarantee.
- **Benchmark claims.** "Matches or outperforms on all tasks" is on authors' own framework
  (GOPS) with their implementations of the baselines; differences on several tasks are within
  seed noise. Ablations are shown on one or two tasks each.

## Why it's in the library

**Scale-free updates are worth copying.** The third refinement ties the outlier clip and the
step size to the model's own learned spread instead of an absolute constant. For any model
trained on returns whose scale drifts — across assets, across volatility regimes, across
retraining windows — a clip of "three learned sigmas" behaves consistently where a fixed
constant does not. It is the same reasoning as volatility-normalising a target.

**Use the expectation where you can.** Refinement 1 is a variance-reduction idea that
transfers: when a target has a known conditional mean, use it for the mean update and keep
the noisy sample only where you need it (here, to learn the variance). Learning the mean
from a noisy sample when its expectation is available only adds noise.

**Pessimism as a default.** Taking the minimum of two independently trained estimates is a
cheap guard against selection bias: picking the action — or the stock — with the highest
estimated value systematically picks overestimates. The twin-critic minimum is one way to
shrink that winner's curse; the price is a small downward bias.

## Links

- [[haarnoja-et-al-2018-soft-actor-critic]] — the maximum-entropy actor-critic that DSAC makes
  distributional
- [[schulman-et-al-2015-trust-region-policy-optimization]] — one of the on-policy baselines
  compared against
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] — the
  distributional idea, here with a Gaussian rather than a categorical family
- [[dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression]] — the
  quantile alternative, which keeps shape but has its own scale parameter κ
- [[malekzadeh-et-al-2024-a-robust-quantile-huber-loss-in-distributional-reinforcement-learning]]
  — another attempt to set a loss threshold from estimated noise rather than by hand
