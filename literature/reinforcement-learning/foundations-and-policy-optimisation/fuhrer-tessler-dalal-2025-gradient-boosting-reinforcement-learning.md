# Gradient Boosting Reinforcement Learning

| | |
|---|---|
| **Authors** | Benjamin Fuhrer (NVIDIA), Chen Tessler, Gal Dalal (NVIDIA Research) |
| **Year** | 2025 (first posted July 2024) |
| **Type** | Paper — *Proceedings of the 42nd International Conference on Machine Learning* (ICML 2025), PMLR 267. This PDF is arXiv:2407.08250v3 (18 Oct 2026), 26pp with appendices. Code: github.com/NVlabs/gbrl |
| **PDF** | `fuhrer-tessler-dalal-2025-gradient-boosting-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `fuhrer2025gradient` |
| **Status** | Reference — read §4 and §5.2 (the robustness tests) and the limitations (§7); skip the per-environment tables |

## What it is

Gradient-boosted trees dominate supervised learning on tabular data but are almost absent
from RL, because boosting libraries expect a fixed dataset with known targets. GBRL makes
**gradient-boosted trees the function class for actor-critic RL**: each boosting iteration
fits one new tree to the policy-gradient and value gradients from the latest batch.

- **Boosting as functional gradient descent (§4.1).** A GBT model is F₀ + ε Σ hₖ(x); each
  tree is fitted to the negative functional gradient. RL supplies that gradient, ∇θ J,
  instead of a residual against a label.
- **The framework (§4.2).** The ensemble outputs the actor-critic parameters, e.g. the
  policy's mean and scale and the value V(s). Collect a rollout, compute the algorithm's
  gradients (PPO, A2C or AWR), fit a tree to (state, gradient) pairs, add it. Each leaf
  predicts both actor and critic outputs; the trees are **shared**, with separate learning
  rates. Sharing halves memory and doubles throughput with no loss of reward (Fig. 3).
- **Splitting on two objectives at once (App. A).** Actor and critic gradients differ in
  size, so a plain split score favours one of them. Normalising per output or scoring by
  cosine similarity fixes it; cosine is slightly better.
- **Standard libraries don't work (§4.3).** CatBoost and XGBoost with incremental
  learning are far slower, and slow down further as the ensemble grows.
- **Standard benchmarks (§5.1, PPO, five seeds).** GBRL clearly wins on **MiniGrid**
  (categorical grid worlds) and on **Football** with hand-built structured features. It
  matches the network on classic control and **loses on Atari RAM**, where the inputs are
  raw memory bytes with no meaning per feature.
- **Challenge environments (§5.2), new in the published version:**
  - **Sparse rewards.** On a task that rewards solving a linear equation only at the end,
    networks manage the one-variable case and fail on two variables. GBRL learns all three
    and keeps the optimal policy.
  - **Spurious correlations.** In MiniGrid with a misleading object next to the target,
    GBRL ignores it and networks lean on it. SHAP values show the network ignoring the
    mission feature.
  - **Out-of-distribution states.** Trees can only output values seen in training, while
    networks extrapolate. GBRL degrades less with added Gaussian noise on classic control,
    with irrelevant objects added in MiniGrid, and when Football opponents are added or
    removed. It solves 11-vs-11 after training against 10.
- **Ablations (§6).** Too high a learning rate destabilises training, too low is slow;
  deeper trees give more accurate gradients at higher cost; small batches learn fast but
  are unstable.

## Read with care

- **The robustness tests are the authors' own designs,** built to show where trees should
  win. They support the claim that trees' inductive bias helps on structured inputs; they
  are not a neutral benchmark.
- **Training budgets differ.** In the challenge tasks GBRL ran 15M steps against the
  network's 30M, and 5M against 20M. That makes GBRL's wins stronger, but the two are not
  compute-matched.
- **Five seeds, partly tuned.** Hyperparameters come from RL Zoo where available and were
  tuned otherwise. The main plots normalise GBRL against the network, which hides absolute
  scale; raw numbers are in the appendix.
- **The ensemble grows without bound** (§7). Every update adds a tree, so memory and
  inference cost rise through training. The authors suggest pruning or compression as
  future work.
- **Only on-policy or advantage-weighted algorithms.** Trees are not differentiable in the
  input, so DDPG and SAC, which need ∇a Q, are not supported.
- **"Structured" is doing the work.** Wins come where each feature already means
  something. Nothing here tests very low signal-to-noise rewards like daily returns.
- **The earlier version (v1, 2024) differed.** It had no challenge environments and
  reported compute costs (up to 24 GB GPU memory and 5 days per run) that this version no
  longer gives.

## Why it's in the library

**It is the bridge from tree-based ranking to RL.** If a cross-sectional model is already a
gradient-boosted ranker on engineered tabular features, GBRL shows the same function class
can be trained directly on a policy objective. The results — structured, hand-built
features favour trees; raw unstructured inputs favour networks — match what
[[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
and [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] found in
supervised learning, and factor-style inputs are the structured case.

**The out-of-distribution result is the one that matters for markets.** A tree can only
return values it saw in training, so in a regime it has never seen it falls back to
something it knows rather than extrapolating. That is a real safety property for a policy
facing a new regime — and also a limit, since it can't respond to anything genuinely new.

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
