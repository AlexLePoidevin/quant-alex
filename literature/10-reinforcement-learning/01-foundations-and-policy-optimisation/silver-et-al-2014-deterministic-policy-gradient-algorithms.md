# Deterministic Policy Gradient Algorithms

| | |
|---|---|
| **Authors** | David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, Martin Riedmiller (DeepMind; Guy Lever at University College London) |
| **Year** | 2014 |
| **Type** | Paper — *Proceedings of the 31st International Conference on Machine Learning* (ICML 2014), JMLR W&CP 32. 9pp (main text; the proofs are in a separate supplement not included here) |
| **PDF** | `silver-et-al-2014-deterministic-policy-gradient-algorithms.pdf` (in this folder) |
| **BibTeX** | `silver2014deterministic` |
| **Status** | Reference — read §2–4 for the theorem and the actor-critic algorithms; §5 is small-scale |

## What it is

Policy gradient methods were built for stochastic policies: sample an action, see what return
it earns, nudge the action probabilities. This paper shows that **a deterministic policy
a = µθ(s) also has a policy gradient**, and that it has a simpler form: follow the gradient of
the action-value function with respect to the action. It is the theoretical basis of DDPG and
of most later continuous-action actor-critic methods.

- **Background (§2).** The stochastic policy gradient theorem (Eq. 2) is an expectation over
  both states and actions of ∇θ log πθ(a|s) · Q(s, a). Actor-critic methods replace Q with a
  learned critic; "compatible" critics (linear in the policy's score features) leave the
  gradient unbiased. The off-policy version (OffPAC) needs importance weights π/β.
- **The intuition (§3.1).** In continuous action spaces, greedy policy improvement
  (argmax over a of Q) needs a global optimisation at every state. Instead, move the policy a
  little in the direction that increases Q: by the chain rule,
  ∇θ µθ(s) · ∇a Q(s, a) evaluated at a = µθ(s) (Eq. 7).
- **Deterministic policy gradient theorem (Thm 1, Eq. 9).** That intuitive update is the exact
  gradient of the performance objective. As in the stochastic case, **no gradient of the
  state distribution is needed**. The expectation is over states only, not actions.
- **A limit of the stochastic case (Thm 2).** For a policy family with a variance parameter σ,
  the stochastic policy gradient tends to the deterministic one as σ → 0. So natural
  gradients, compatible critics and the rest of the machinery carry over.
- **Algorithms (§4).** On-policy deterministic actor-critic with a Sarsa critic (didactic);
  **off-policy deterministic actor-critic** with a Q-learning critic, where actions come from
  a noisy behaviour policy but the deterministic target policy is learned. Because the
  action integral disappears, **no importance sampling is needed** in the actor, and
  Q-learning avoids it in the critic.
- **Compatible function approximation (Thm 3).** A critic whose action-gradient is linear in
  ∇θ µθ(s) and fitted by least squares gives an unbiased gradient. With gradient-TD learning
  in the critic (COPDAC-GQ) the critic provably converges. The natural deterministic policy
  gradient reduces to θ ← θ + α w.
- **Experiments (§5).** A quadratic continuous bandit in 10, 25 and 50 action dimensions: the
  deterministic update beats the stochastic one by a margin that **grows with action
  dimension**. Mountain car, pendulum and puddle world: a slight edge. A 6-segment octopus arm
  with 20 action and 50 state dimensions is learned directly.

## Read with care

- **Exploration is outsourced.** A deterministic policy does not explore. The method relies on
  an off-policy behaviour policy (here fixed-width Gaussian noise) and on a critic that
  extrapolates well to actions near the policy. When the critic is wrong, the actor follows
  the wrong gradient confidently.
- **Off-policy gradient is approximate.** Eq. 15 drops a term involving ∇θ Q, as OffPAC did.
  The justification is that local optima are preserved, not that the gradient is exact.
- **Small-scale evidence.** Linear tile-coded critics, simple tasks, best-of-sweep step sizes.
  The deep version (DDPG, Lillicrap et al. 2015) came later and is known to be brittle to
  hyperparameters; this paper does not address that.
- **The variance argument.** The stochastic gradient's variance grows like 1/σ² as the policy
  becomes deterministic (§6). That is the core practical case for DPG, but it is argued, not
  measured here beyond the bandit.

## Why it's in the library

**It is the template for "differentiate the critic, not the reward".** A trading policy that
outputs continuous weights is a deterministic map from features to positions. DPG says the
gradient of performance is the critic's sensitivity to those weights, pushed back through
the policy. If a differentiable model of next-period P&L is available, this is the same as
maximising a learned utility of portfolio weights by backpropagation, which is how many
end-to-end portfolio networks are trained in practice.

**It shows where the weak point moves to.** Once the gradient comes from ∇a Q, everything
depends on the critic's action-gradient being right. On noisy, low-signal returns a learned
Q will be flat or wrong in most directions, and the actor will chase its errors. That is the
argument for heavy critic regularisation, clipped double critics (as in
[[haarnoja-et-al-2018-soft-actor-critic]]) and conservative updates.

**High-dimensional actions favour it.** A cross-sectional book with hundreds of names is a
high-dimensional action. The bandit result — the stochastic gradient degrades with action
dimension, the deterministic one does not — is the relevant one for that setting.

## Links

- [[schulman-et-al-2015-trust-region-policy-optimization]] — the stochastic, on-policy
  alternative: constrain the step size instead of removing the action integral
- [[haarnoja-et-al-2018-soft-actor-critic]] — off-policy actor-critic with a stochastic,
  entropy-regularised actor; fixes DDPG's brittleness
- [[duan-et-al-2023-distributional-soft-actor-critic-with-three-refinements]] — a modern
  continuous-action actor-critic that learns a return distribution, not just its mean
- [[rajeswaran-et-al-2017-towards-generalization-and-simplicity-in-continuous-control]] —
  how far linear policies and a natural gradient get on the same kind of tasks
- [[jeong-gu-2024-pro-trader-rl]] — an actor-critic applied to trading decisions
