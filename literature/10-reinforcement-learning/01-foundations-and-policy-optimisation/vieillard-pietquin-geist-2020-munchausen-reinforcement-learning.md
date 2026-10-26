# Munchausen Reinforcement Learning

| | |
|---|---|
| **Authors** | Nino Vieillard (Google Research, Brain Team; Université de Lorraine, CNRS, Inria, IECL), Olivier Pietquin, Matthieu Geist (Google Research, Brain Team) |
| **Year** | 2020 |
| **Type** | Paper — *Advances in Neural Information Processing Systems 33* (NeurIPS 2020). arXiv:2007.14430v3 [cs.LG], 29pp including appendices |
| **PDF** | `vieillard-pietquin-geist-2020-munchausen-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `vieillard2020munchausen` |
| **Status** | Reference — read §1–3 (the idea and the two theorems) and §4's ablation; the appendix is proofs and per-game curves |

## What it is

TD learning bootstraps on the agent's own value estimate. This paper bootstraps on a second
estimate the agent already has: **its own policy**. The change is one term: **add the scaled
log-policy α τ ln π(a|s) to the reward** in the TD target. Named after the Baron who pulls
himself out of a swamp by his own hair.

- **The idea (§2).** If the optimal policy were known, ln π* would be 0 for optimal actions
  and −∞ otherwise: a strong learning signal that does not change the optimal control. The
  current policy is used in its place, kept stochastic for numerical stability. This is
  **not** maximum-entropy RL, which subtracts the log-policy from every future reward.
- **M-DQN (Eq. 1–2).** First make DQN stochastic: Soft-DQN, with a softmax policy at
  temperature τ and an entropy term in the target (a discrete-action SAC). Then add
  α τ ln π(aₜ|sₜ) to rₜ. α = 0 gives Soft-DQN; τ → 0 gives DQN.
- **Implicit KL regularisation (§3, Thm 1).** Munchausen value iteration is equivalent to
  mirror-descent value iteration with **KL(π‖πₖ) scaled by ατ and entropy scaled by (1 − α)τ**.
  Because the KL is implicit, the greedy step is still an exact softmax, so known bounds apply
  to the deep agent. The error term is **the norm of the average of past errors**, not a
  discounted sum of their norms: errors can cancel across iterations instead of
  accumulating, and the horizon dependence improves from (1 − γ)⁻² to (1 − γ)⁻¹.
- **Action gap (Thm 2).** The gap between the best and other actions grows by a factor
  (1 + α)/(1 − α), which makes greedy choices less sensitive to small value errors. Links to
  advantage learning, conservative value iteration and dynamic policy programming.
- **Experiments (§4).** All 60 Atari games, 200M frames, Dopamine's harder protocol (sticky
  actions), three seeds. Working values α = 0.9, τ = 0.03, log-policy clipped at l₀ = −1.
  M-DQN beats DQN on 53/60 games and beats C51 without distributional RL, n-step returns or
  prioritised replay. M-IQN beats IQN on 40/60 games and beats Rainbow on mean and median.
- **Ablation (Fig. 3).** Switching DQN to Adam alone helps a lot. Soft-DQN is no better than
  Adam-DQN; **the Munchausen term is what makes the difference**, over Soft-DQN at either
  temperature and over advantage learning.

## Read with care

- **Three seeds, aggregate scores.** Human-normalised means are dominated by a few games
  with large gains; the authors note the mean–median gap. Per-game improvement counts are the
  more robust summary.
- **Hyperparameters were tuned on a few games** and then fixed. The action-gap figure is a
  single game and is labelled illustrative.
- **Theory is for the abstract scheme.** The bounds hold for M-VI with discrete actions and
  an exact softmax greedy step; the deep agent adds network fitting error, ε-greedy
  behaviour and log-policy clipping.
- **Discrete actions.** The trick needs a computable log-policy; continuous-action versions
  exist elsewhere but are not studied here.

## Why it's in the library

**Errors that average out instead of compounding.** The core theoretical result — successive
estimates regularised towards the previous policy make approximation errors cancel over
iterations — is what one wants from a model retrained every day on overlapping, noisy data.
Anchoring today's policy to yesterday's, by KL, turns retraining noise into something closer
to averaging.

**A cheap way to stabilise a ranking.** Adding the log-probability of the current choice is a
consistency bonus. For a cross-sectional selector that outputs a softmax over names, the
analogue is a penalty on divergence from yesterday's ranking distribution, with α setting how
sticky it is. That is turnover control expressed as regularisation, with a theory behind it.

**The ablation is a lesson in baselines.** Changing only the optimiser moved DQN to roughly
C51's level. Before crediting a new loss, check what a better-tuned baseline does.

## Links

- [[haarnoja-et-al-2018-soft-actor-critic]] — maximum-entropy RL; Soft-DQN is its
  discrete-action form
- [[schulman-et-al-2015-trust-region-policy-optimization]] — explicit KL regularisation
  between successive policies, which M-RL gets implicitly
- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]]
  — IQN, the distributional agent that M-IQN modifies
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] —
  C51, the first agent M-DQN overtakes without a distributional critic
- [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] — the distributed
  large-scale agents the authors explicitly do not compare with
- [[harvey-liu-zhu-2016]] — why aggregate scores across many trials need deflating
