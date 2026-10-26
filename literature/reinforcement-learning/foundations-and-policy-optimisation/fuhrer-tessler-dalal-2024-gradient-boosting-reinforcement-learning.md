# Gradient Boosting Reinforcement Learning

| | |
|---|---|
| **Authors** | Benjamin Fuhrer (NVIDIA), Chen Tessler, Gal Dalal (NVIDIA Research) |
| **Year** | 2024 (v1, 11 July) |
| **Type** | Preprint — arXiv:2407.08250v1 [cs.LG], 21pp including supplementary material. Code: github.com/NVlabs/gbrl |
| **PDF** | `fuhrer-tessler-dalal-2024-gradient-boosting-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `fuhrer2024gradient` |
| **Status** | Reference — read §4–5 and the limitations (§7); skip the per-environment tables |

## What it is

Gradient-boosted trees dominate supervised learning on tabular data but are almost absent
from RL, because boosting libraries expect a fixed dataset with known targets. GBRL makes
**gradient-boosted trees the function class for actor-critic RL**: each boosting iteration
fits one new tree to the policy-gradient (and value) gradients from the latest batch.

- **Boosting as functional gradient descent (§3.3).** A GBT model is F₀ + ε Σ hₖ(x); each
  tree hₖ is the projection of the negative functional gradient onto the tree class
  (Eq. 1–2). RL supplies the gradient, ∇θ J, rather than a residual against a label.
- **The method (§4, Algorithm 1).** The ensemble outputs the actor-critic parameters, e.g.
  θ(s) = [µ(s), σ(s), V(s)] for a Gaussian policy. Collect a rollout, compute the
  algorithm's gradients (PPO, A2C or AWR), fit a tree to (state, gradient) pairs, add it.
  So θₖ ≈ θ₀ + ε Σ ∇θ J, a scaled sum of past gradients.
- **Handling non-stationarity.** RL gradients change size and direction as the state
  distribution shifts, and a bad large step risks forgetting. GBRL fits each tree on a
  **random batch sampled with replacement** from the buffer, so useful directions accumulate
  and harmful ones are diluted. Standard GBT features (GOSS, early stopping, pruning,
  categorical encodings) do not fit this setting.
- **Shared actor-critic trees.** Each leaf predicts both policy and value; the split
  structure is shared, with **separate learning rates** for actor and critic outputs. This
  uses less than half the GPU memory and almost triples training speed with no loss of
  reward (Fig. 7).
- **Results (§5).** Classic control: PPO-GBRL is on par with PPO with a network; A2C and AWR
  mixed. **Google Football (hand-built, structured features): PPO-GBRL clearly beats the
  network** on most scenarios. **Atari RAM (unstructured bytes): the network wins** in most
  cases. **MiniGrid (categorical): GBRL wins or ties** in most tasks. CatBoost and XGBoost
  with incremental learning cannot solve even CartPole in a realistic time.
- **Interpretation.** The authors tie the split to the supervised findings: trees win on
  irregular, structured or categorical inputs; networks win where the solution is smooth in
  raw features.

## Read with care

- **Preprint, single version.** Five seeds per environment, hyperparameters from RL Zoo
  where available and tuned otherwise. Plots are normalised GBRL-versus-network
  differences, which hide absolute scale; the raw numbers are in the supplement.
- **The ensemble grows without bound** (§7). Every update adds a tree, so memory and
  inference cost rise over training; off-policy methods make it worse. Runs used up to
  24 GB of GPU memory and up to 5 days, against 3 GB and 3 days for the networks.
- **Only on-policy or advantage-weighted algorithms.** Trees are not differentiable in the
  input, so DDPG and SAC, which need ∇a Q, are not supported.
- **"Structured" is doing the work.** Wins come where features are already meaningful. The
  paper does not test noisy targets, so it says nothing about low signal-to-noise rewards.

## Why it's in the library

**It is the bridge from tree-based ranking to RL.** If a cross-sectional model is already a
gradient-boosted ranker on engineered tabular features, GBRL shows the same function class
can be trained directly on a policy objective. The football result — structured,
hand-built features favour trees — matches what
[[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
and [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] found in
supervised learning, and is the relevant regime for factor-style inputs.

**Boosting on gradients is a general pattern.** Fitting a tree to the gradient of any
differentiable objective is how custom ranking losses work in boosting libraries. GBRL
makes the point that the objective can be a policy gradient, a utility or a Sharpe-style
surrogate, not only a supervised loss.

**The limitations matter for daily retraining.** An ensemble that only grows, with early
trees fitted to a stale distribution, is the tree-model version of loss of plasticity.
Pruning, compression or a rolling window of trees would be needed before a continually
trained GBRL policy is practical.

## Links

- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — why trees beat networks on tabular data, cited by the authors to explain their results
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same
  comparison, with boosting as the strong default
- [[schulman-et-al-2015-trust-region-policy-optimization]] — the trust-region idea behind
  PPO, GBRL's best backbone
- [[rajeswaran-et-al-2017-towards-generalization-and-simplicity-in-continuous-control]] —
  another test of whether neural policies are needed at all
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — plasticity loss
  in continually trained networks, the analogue of an ever-growing stale ensemble
