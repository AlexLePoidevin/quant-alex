# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

| | |
|---|---|
| **Authors** | Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, Sergey Levine (Berkeley Artificial Intelligence Research, UC Berkeley) |
| **Year** | 2018 |
| **Type** | Paper — *Proceedings of the 35th International Conference on Machine Learning* (ICML 2018), PMLR 80. arXiv:1801.01290v2 [cs.LG], 14pp including appendices |
| **PDF** | `haarnoja-et-al-2018-soft-actor-critic.pdf` (in this folder) |
| **BibTeX** | `haarnoja2018soft` |
| **Status** | Reference — read §3–4 for the objective and updates, §5.2 for the ablations |

## What it is

Deep RL in 2017 had two practical problems: on-policy methods (TRPO, PPO, A3C) needed fresh
samples for every update, and the efficient off-policy method (DDPG) was brittle to
hyperparameters and seeds. SAC is an **off-policy actor-critic with a stochastic actor**,
trained on the **maximum entropy** objective: maximise reward plus the policy's entropy,
"succeed at the task while acting as randomly as possible".

- **Objective (§3.2, Eq. 1).** J(π) = Σ E[r(s, a) + α H(π(·|s))]. The **temperature α** trades
  reward against entropy; α → 0 recovers ordinary RL. Benefits claimed: wider exploration,
  giving up early on clearly bad actions, and spreading probability over several
  near-optimal actions instead of committing to one.
- **Soft policy iteration (§4.1).** Policy evaluation uses a soft Bellman backup whose state
  value is E[Q − log π] (Eq. 2–3). Policy improvement projects exp(Q)/Z onto the policy
  class by minimising KL (Eq. 4). In the tabular case this **provably converges** to the
  best policy in the class (Lemmas 1–2, Thm 1).
- **The practical algorithm (§4.2).** Neural networks for a soft value V, a soft Q and a
  Gaussian policy, updated by SGD from a **replay buffer**, so old data is reused. The policy
  loss is the KL to the Boltzmann distribution of Q, minimised with the
  **reparameterisation trick** (Eq. 11–13), which gives lower-variance gradients than the
  likelihood-ratio estimator. A slow-moving target value network stabilises training.
- **Two Q-functions (§4.2).** Train two critics and use **the minimum** of the two in the
  value and policy updates (following TD3) to curb overestimation; this speeds learning
  markedly on harder tasks.
- **Results (§5.1).** On MuJoCo Hopper, Walker2d, HalfCheetah, Ant and two Humanoid tasks,
  SAC matches the baselines on the easy tasks and clearly beats DDPG, PPO and soft
  Q-learning on the hard ones, in both speed and final return. DDPG makes no progress on Ant
  and the Humanoids.
- **Ablations (§5.2).** A deterministic variant (no entropy, closer to DDPG) has **far higher
  variance across seeds** (Fig. 2). Evaluating with the policy mean beats sampling. **Reward
  scale is the one hyperparameter that needs tuning** because it acts as the inverse
  temperature. The target smoothing τ has a wide workable range.

## Read with care

- **Temperature is tuned by hand here.** In this version α is fixed (folded into the reward
  scale), and the paper shows performance is sensitive to it and that the best value varies
  by task. Automatic temperature tuning came in the follow-up (Haarnoja et al. 2018b).
- **"Stable across seeds" is measured on five seeds**, with min–max bands on simulated
  locomotion tasks that have dense, informative rewards. That says little about domains
  where the reward is mostly noise.
- **Entropy is not risk control.** The policy is random in action space, which helps
  exploration; it does not penalise variance of returns. Return risk needs a separate
  mechanism, such as a distributional critic.
- **Off-policy data has limits.** The replay buffer assumes old transitions are still
  informative about current dynamics. Under drift, old data can mislead the critic.

## Why it's in the library

**It is the default continuous-action RL baseline.** Any RL position-sizing or allocation
study since 2018 compares against SAC or a close relative. Knowing what it actually does —
two clipped critics, a Gaussian actor, entropy bonus, replay — is needed to judge whether a
reported edge comes from the method or from tuning.

**Entropy as a regulariser has a portfolio reading.** A maximum-entropy policy spreads weight
across near-equivalent actions instead of committing to the argmax. For a ranking model on
low-signal data that is the same instinct as preferring diffuse selections over concentrated
picks: when expected values are barely distinguishable, the soft choice is more robust to
estimation error. The temperature is then a concentration knob, and it should be chosen out
of sample, not left at a default.

**The clipped double critic is a general idea.** Taking the minimum of two independently
trained value estimates is a cheap, pessimistic correction for the upward bias that
maximising over a noisy estimate creates — the same winner's-curse problem that inflates
backtest selection.

## Links

- [[silver-et-al-2014-deterministic-policy-gradient-algorithms]] — the deterministic
  actor-critic that SAC's stochastic actor replaces
- [[schulman-et-al-2015-trust-region-policy-optimization]] — the on-policy approach whose
  sample cost motivates SAC
- [[duan-et-al-2023-distributional-soft-actor-critic-with-three-refinements]] — SAC with a
  distributional critic to reduce overestimation further
- [[vieillard-pietquin-geist-2020-munchausen-reinforcement-learning]] — the discrete-action
  analogue (Soft-DQN) plus a log-policy bonus that turns entropy into KL regularisation
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — why long-running
  off-policy agents can stop learning
- [[harvey-liu-zhu-2016]] — the selection-bias problem that pessimistic estimates address
