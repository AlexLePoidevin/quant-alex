# Prediction and Control in Continual Reinforcement Learning

| | |
|---|---|
| **Authors** | Nishanth Anand (McGill University, Mila), Doina Precup (McGill University, Mila, DeepMind) |
| **Year** | 2023 |
| **Type** | Conference paper — *Advances in Neural Information Processing Systems 36* (NeurIPS 2023). arXiv:2312.11669v1 [cs.LG], 18 December 2023, 39pp including appendices |
| **PDF** | `anand-precup-2023-prediction-and-control-in-continual-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `anand2023prediction` |
| **Status** | Reference — read §1, §3 and §6; §4 is tabular theory, the appendix holds most experimental detail |

## What it is

A simple idea for learning values in a changing world: **split the value function into a
slow part and a fast part**. The slow, *permanent* part learns what is common across all the
situations seen. The fast, *transient* part learns a correction for the current situation
and is then decayed or reset. The idea comes from the complementary learning systems theory
of the brain (a slow neocortex and a fast hippocampus).

- **The dilemma, even in a table (§1).** The stability–plasticity problem is not just about
  small networks. With a lookup table, a convergent TD learner averages over all tasks and
  is imprecise for the current one; a tracking TD learner overwrites the past and relearns
  from scratch; one estimator per task needs to know which task is active.
- **Permanent + transient (§3).** V = V_permanent + V_transient. The transient part is
  trained by TD on the **combined** estimate, so it only learns the residual the permanent
  part misses. At a task change, the transient part's knowledge is folded into the
  permanent part by a small step, and the transient part is reset.
- **Theory (§4, tabular, prediction only).** With the right initialisation the method is
  exactly TD learning (Thm. 1), so it **strictly generalises TD**. The transient fixed point
  is the true value minus the permanent part (Thm. 3). **The permanent part converges to the
  average value function across tasks (Thm. 5), which is the best zero-shot starting point
  for a new task (Thm. 6).** It retains past knowledge where TD forgets (Thm. 7) and has a
  tighter early error bound on a new task (Thm. 8).
- **Known task boundaries (§5).** Gridworlds, Minigrid, with tabular, linear and deep value
  functions: lower error on the current task and on old tasks than TD or Q-learning, with
  or without resets.
- **Unknown boundaries (§6, Alg. 2).** The permanent part is updated every k steps from a
  buffer; the transient part is decayed by λ each time rather than reset. **k and λ set the
  stability–plasticity trade-off.** For every k tried there was a λ that beat Q-learning.
- **Deep RL (§6, Fig. 5).** On JellyBeanWorld (rewards flipped every 150k steps) and a
  MinAtar sequence (game switched every 500k steps), PT-DQN with half-size networks beats
  DQN, DQN with a large replay buffer, and a multi-head DQN that is told the task identity.
  **A large replay buffer hurt**, because old samples are stale.

## Read with care

- **Theory assumes piecewise change and i.i.d. tasks** (Assumption 1), tabular prediction
  only. Smooth drift is listed as future work (§7.1).
- **Two new hyperparameters.** k and λ interact; the authors suspect they could be merged
  but do not show how.
- **Small domains.** JellyBeanWorld and MinAtar were chosen to afford 30 seeds; scale-up is
  untested.
- **Value-based only.** Policy-gradient and actor-critic versions are proposed, not tested.

## Why it's in the library

**It is the cleanest form of "slow model plus fast correction".** In a rolling-window setting,
the analogue is a model trained on long history (the permanent part) plus a short-memory
adjustment trained on recent data (the transient part), added together. Theorem 6 gives
the reason this is sensible: the long-history model is the best starting point for an
unseen regime.

**It frames warm-start versus fresh retrain as two knobs.** How often to consolidate (k) and
how quickly to forget the recent correction (λ) replace the binary choice between
continuing from the last weights and starting again.

**The stale-replay result applies to any long training buffer.** Using a large store of old
data helped forgetting but hurt tracking, because old samples describe a world that has
moved on. The same tension appears when choosing the length of a training window.

**The baseline matters.** The method beat a multi-head model that knew the task identity,
because shared features drift under the stale heads. Regime-specific heads on a shared,
continually trained trunk carry the same risk.

## Links

- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — the taxonomy this paper works within (Precup co-authored both)
- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — the
  forgetting problem that complementary learning systems were proposed to solve
- [[wallace-bluff-2002-episodic-memory-a-connectionist-interpretation]] — connectionist
  accounts of fast episodic memory, the "hippocampus" side of the analogy
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — the authors
  suggest learning k and λ with meta objectives
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the network-level
  failure that a fast, resettable component also sidesteps
