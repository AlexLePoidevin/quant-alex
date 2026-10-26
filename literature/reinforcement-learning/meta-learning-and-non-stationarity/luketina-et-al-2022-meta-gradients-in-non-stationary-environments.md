# Meta-Gradients in Non-Stationary Environments

| | |
|---|---|
| **Authors** | Jelena Luketina (University of Oxford; work done at DeepMind), Sebastian Flennerhag, Yannick Schroecker, David Abel, Tom Zahavy, Satinder Singh (DeepMind) |
| **Year** | 2022 |
| **Type** | Paper — *1st Conference on Lifelong Learning Agents* (CoLLAs 2022), PMLR 199; arXiv:2209.06159v1 [cs.LG], 16pp including appendices |
| **PDF** | `luketina-et-al-2022-meta-gradients-in-non-stationary-environments.pdf` (in this folder) |
| **BibTeX** | `luketina2022meta` |
| **Status** | Reference — short and empirical; read §3 (contextual meta-gradients), §6.2 and §6.4 |

## What it is

Meta-gradients tune hyperparameters during training by following the gradient of future
performance (see [[xu-et-al-2020-meta-gradient-reinforcement-learning-with-an-objective-discovered-online]]).
This paper asks whether that actually helps when the environment keeps changing, and what
information the tuner needs. The answer is: **plain meta-gradients barely help, but
meta-gradients that see a few summary statistics of recent performance help clearly.**

- **White-box only (§1–2).** The study tunes a small number of existing hyperparameters, an
  entropy-loss weight, an L2 weight or the ε of ε-greedy, rather than learning a whole
  update rule. Meta-gradients are truncated to the last K inner updates.
- **Contextual meta-gradients (§3).** Instead of learning a hyperparameter value η, learn a
  small function η = g_ω(c) of **context features** c: histories of mean reward, TD error,
  value, and so on. The idea is that a plain meta-gradient can only track a good value
  slowly, while a function of context can learn "when reward drops, explore more" and apply
  it instantly the next time the same pattern appears. Gradients do not flow through the
  context.
- **Environments (§4).** "Two Colors", where the rewarding object swaps every 100k steps,
  and "Switching MDPs", which resamples a random gridworld every 100k steps from a pool of 4
  (tasks repeat) or 1000 (tasks effectively never repeat).
- **Context is what matters (§6.1, Tables 1–2).** Without context, meta-gradients are close
  to a well-tuned fixed baseline (actor-critic, Two Colors: 1.29–1.32 vs 1.24); with reward or
  richer context they are clearly better (1.58–1.79). On Switching MDPs, only the contextual
  versions beat the baseline, and the gain is larger when tasks do not repeat.
- **Learned schedules make sense (§6.2, Figs. 1–2).** Without context the learned entropy
  weight is almost constant. With reward context it **jumps after each task switch**, and
  probing the learned function shows high exploration for low or falling rewards, low
  exploration for high rewards, and different outputs for inputs with the same mean but
  different trend.
- **More context mostly helps (§6.3, Fig. 3).** Adding value, reward, TD-error, action,
  gradient-similarity and past meta-parameter statistics generally raises performance. The
  exception is high-dimensional state-visitation features, which hurt, probably by
  overfitting.
- **Too fast a change defeats everything (§6.4, Fig. 5).** When the task switches every 25k
  steps, no meta-gradient method beats the fixed baseline; rich context degrades least.

## Read with care

- **Toy gridworlds with regular, discrete switches.** The switches happen on a clock, and in
  Two Colors the same two tasks alternate, which is the best case for learning a
  context-to-hyperparameter map. Real non-stationarity is gradual, irregular and rarely
  repeats exactly.
- **Best configuration per method.** Every row reports the best point of a hyperparameter
  sweep over meta learning rate, meta-rollout length and other settings, ten seeds each.
  Reasonable for a methods comparison, but it means the adaptive method was itself tuned.
- **One or two hyperparameters tuned.** The claims are about exploration-type
  hyperparameters in small agents, not learning rates or architectures at scale.
- **The context features are hand-picked.** The finding is that the right summary
  statistics help, which leaves the choice of statistics to the designer.

## Why it's in the library

**It is the honest test of "make the hyperparameters adapt".** In a changing market the
obvious idea is to let regularisation strength, learning rate or exploration drift over
time. This paper shows that a tuner that only follows the gradient of recent performance is
**too slow to matter** under fast change: it tracks, it does not anticipate. What works is
conditioning the hyperparameter on observable state — recent hit rate, recent error,
recent volatility — so the response to a familiar situation is immediate.

**That is a regime-conditioned hyperparameter.** The quant translation is a small,
explicitly specified map from a few slow-moving diagnostics (rolling error, rolling
dispersion, drawdown) to a hyperparameter, learned on past data and applied causally. The
paper's two warnings carry over directly: high-dimensional context overfits, and when the
regime changes faster than the tuner can see a few examples of it, adaptation stops paying.

**It sets expectations.** The gains are real but moderate, in toy settings built to reward
the method. Any adaptive scheme should be compared against a fixed, well-tuned default
under the same validation protocol, as the paper does.

## Links

- [[xu-et-al-2020-meta-gradient-reinforcement-learning-with-an-objective-discovered-online]]
  — the black-box, single-lifetime meta-gradient method this paper contrasts with
- [[anand-precup-2023-prediction-and-control-in-continual-reinforcement-learning]] — another
  answer to changing environments: split fast and slow value components
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — the taxonomy of non-stationarity this study samples from
- [[lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks]] — why
  the network itself, not only its hyperparameters, can fail to keep adapting
- [[sokar-et-al-2023-the-dormant-neuron-phenomenon-in-deep-reinforcement-learning]] — a
  concrete mechanism behind lost adaptivity in long RL runs
