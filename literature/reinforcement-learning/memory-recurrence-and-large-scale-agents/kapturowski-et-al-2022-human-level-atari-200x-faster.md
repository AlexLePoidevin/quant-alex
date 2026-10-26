# Human-level Atari 200x faster

| | |
|---|---|
| **Authors** | Steven Kapturowski, Víctor Campos, Ray Jiang, Nemanja Rakićević, Hado van Hasselt, Charles Blundell, Adrià Puigdomènech Badia (DeepMind) |
| **Year** | 2022 (v1, 15 September) |
| **Type** | Paper — arXiv:2209.07550v1 [cs.LG], 35pp including appendices |
| **PDF** | `kapturowski-et-al-2022-human-level-atari-200x-faster.pdf` (in this folder) |
| **BibTeX** | `kapturowski2022human` |
| **Status** | Reference — read §4 (the four fixes) and §5.2 (ablations); the appendices hold the useful detail |

## What it is

Agent57 beat the human baseline on all 57 Atari games but needed about 78 billion frames.
This paper keeps the same goal and cuts the data needed to **390 million frames**, about
200× fewer. The agent is called MEME. The interest is less the headline than the **list of
instabilities that appear when you try to learn faster, and the fix for each**.

- **Starting point (§3).** Agent57: R2D2-style distributed recurrent replay, a family of
  policies with different exploration weights and discounts, and a bandit meta-controller.
- **A — faster signal propagation (§4).**
  - **A1, online bootstrapping with a trust region.** Bootstrap from the online network
    rather than a slow target network. To keep it stable, mask out the loss at any step
    where the online value has moved more than α·σ from the target network's value *and*
    the TD error points further away (Eqns 1–2, Fig. 3). It is like PPO's value clipping
    but scaled by the TD-error spread, so it adapts to value scale.
  - **A2, Soft Watkins Q(λ).** Retrace cuts traces too aggressively under ε-greedy
    policies; Peng's Q(λ) has no off-policy correction. The new estimator cuts a trace only
    when the taken action is worse than the best by more than a tolerance κ (Eqn 4).
- **B — differing value scales (§4).**
  - **B1, TD-error normalisation.** Divide TD errors by a running (or batch) standard
    deviation, floored at 0.01, in both the loss and the replay priorities.
  - **B2, cross-mixture training.** Train every policy in the family on every trajectory,
    mixing the behaviour policy's loss with the mean over all (η = 0.5).
- **C — architecture (§4).** A normaliser-free NFNet torso, since common normalisation
  layers hurt in this non-stationary setting, with stochastic depth whose mask is held
  fixed along each trajectory. A shared torso for the intrinsic and extrinsic value heads,
  trained on the combined loss.
- **D — policy distillation (§4).** A policy head learns to match the ε-greedy policy from
  the Q-values, with a KL trust region. It smooths **policy churn** — the greedy action
  flipping between consecutive updates — and is used as the target policy for returns.
- **Results (§5.1, Fig. 1, Table 1).** Above human on all 57 games by 390M frames. Per game,
  the frames needed fall by 9× to 721×, 63× on average. Hard-exploration games are still
  the last to be solved.
- **Ablations (§5.2, Fig. 4).** On eight tuning games, **removing the trust region with
  online bootstrapping costs the most**. The trust region helps even with a target network.
  Normalisation gives the smallest single gain, plausibly because it overlaps with the other
  regularisers.

## Read with care

- **Tuned on the ablation games.** Hyperparameters were tuned on the same eight games used
  for the ablations. Ablations use three seeds; the main result uses six.
- **Each game trained separately.** One hyperparameter set, but separate weights per game,
  as the authors note.
- **"200×" is the extreme ratio.** It compares the frames needed for the last game. The
  average per-game improvement is 63× and the median 35×.
- **Still very large compute.** 1B-frame runs on TPUv4 with distributed actors. "Data
  efficient" is relative to Agent57, not to the small-data regime of benchmarks like
  Atari 100k.
- **Many interacting parts.** Several components overlap in what they stabilise. Their
  individual value outside this agent is untested.

## Why it's in the library

**Stability tricks for learning fast on non-stationary targets.** Bootstrapping from a
model that is still changing, training on targets with very different scales, and acting on
a decision that flips between updates are all problems for a model refitted often on
streaming market data. The fixes are general: bound how far one update can move a
prediction, relative to its usual error size; normalise errors by a running scale before
they drive the loss or the sampling; and smooth the decision rule with a distilled policy.

**Policy churn has a direct trading cost.** When a ranking model's top picks change because
of small parameter updates rather than new information, the result is turnover without
alpha. Measuring churn between consecutive refits, and smoothing the decision (distillation,
averaged models), is the trading version of section D.

**Normalisation layers can hurt under non-stationarity.** The finding that common
normalisation layers were harmful here is worth testing for any network trained on drifting
inputs, alongside the online alternatives in this library.

## Links

- [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] — the agent made 200×
  more data-efficient here
- [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]]
  — the recurrent replay foundation, including burn-in and sequence priorities
- [[schulman-et-al-2015-trust-region-policy-optimization]] — the trust-region idea, here
  applied to value updates
- [[chiley-et-al-2019-online-normalization-for-training-neural-networks]] — normalisation
  designed for streaming, non-stationary training
- [[vieillard-pietquin-geist-2020-munchausen-reinforcement-learning]] — another change to
  the bootstrap target that makes value learning more stable
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — what goes wrong when a
  network keeps learning on a moving target for long
