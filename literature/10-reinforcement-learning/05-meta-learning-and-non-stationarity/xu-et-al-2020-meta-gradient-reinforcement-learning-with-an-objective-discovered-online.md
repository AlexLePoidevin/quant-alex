# Meta-Gradient Reinforcement Learning with an Objective Discovered Online

| | |
|---|---|
| **Authors** | Zhongwen Xu, Hado van Hasselt, Matteo Hessel, Junhyuk Oh, Satinder Singh, David Silver (DeepMind) |
| **Year** | 2020 |
| **Type** | Paper — *Advances in Neural Information Processing Systems 33* (NeurIPS 2020); arXiv:2007.08433v1 [cs.LG], 18pp including appendices |
| **PDF** | `xu-et-al-2020-meta-gradient-reinforcement-learning-with-an-objective-discovered-online.pdf` (in this folder) |
| **BibTeX** | `xu2020meta` |
| **Status** | Reference — read §1–3 for the meta-gradient set-up, §4 for the non-stationarity toy, §5.4 for the ablations |

## What it is

Every deep RL algorithm is defined by its update target: the one-step TD target, the n-step
return, the Q-learning max, V-trace. This paper replaces the hand-designed target with a
neural network and learns that network **online, during a single training run on a single
task**, by differentiating through the agent's own updates. The algorithm is called FRODO
(Flexible Reinforcement Objective Discovered Online).

- **Meta-gradients (§3.3).** Two levels. The agent parameters θ take M ordinary gradient
  steps on an inner loss whose target is produced by a meta-network g_η. An outer loss, a
  plain canonical RL loss on a fresh trajectory, is then evaluated at the updated θ′, and its
  gradient with respect to η is back-propagated through the M inner updates. In words:
  **adjust the learning rule so that the next few updates make the agent better on data it
  has not trained on yet.**
- **Single lifetime, not multi-task (§1–2).** Unlike MAML or learned-optimiser work, there is
  no distribution of tasks and no resets. The table in §2 places it among white-box methods
  (tuning γ, λ, learning rates) and black-box methods (learning the whole update rule); this
  is the first black-box, single-lifetime one.
- **Learn a target, not a loss (§3.2, Fig. 3b).** The meta-network outputs the target G, and
  the agent regresses towards it. The authors argue this is more stable than learning the
  loss directly, because the update always moves towards something rather than possibly
  away from it. The ablation agrees: a learned loss performs poorly on all eight test games.
- **Toy evidence (§4).** On "Catch", trained with only 3-step trajectories, FRODO discovers
  bootstrapping and beats the best possible 3-step look-ahead agent. On a 5-state random walk
  whose left-hand reward **switches sign every 960 steps**, the learned target gives lower
  prediction error than TD(λ) for every λ, with **smaller error spikes at the change points**.
- **Atari (§5).** An LSTM meta-network reads rewards, discounts, future values and the
  behaviour and target policy probabilities, so it can in principle learn an off-policy
  correction. With a small **self-consistency penalty** pushing the learned target towards
  the form G_t = R_{t+1} + γG_{t+1} (§5.2), FRODO starts slower than IMPALA but overtakes it
  on median human-normalised score over 57 games.
- **What gets learned (§5.4, Fig. 3d).** The discovered target drifts over training and
  differs from V-trace in a game-specific way; only in Pong does it stay close to V-trace.

## Read with care

- **Expensive and slow to start.** Meta-gradients through M inner steps multiply compute,
  and Fig. 3a shows FRODO behind the baseline for much of training before overtaking it.
- **Needs a hand-built prior to work at scale.** Without the consistency loss performance
  drops and becomes unstable; too much (c = 1) also hurts. "Discovered online" still leans
  on a classical RL structure and on another hyperparameter.
- **The outer loss is still hand-designed.** The meta-network learns a target that serves a
  canonical RL objective (V-trace, TD(1)). It discovers how to optimise that objective
  faster, not what to want.
- **Small number of seeds and a median.** Atari results are one run per game for the main
  curve; ablations use three seeds on eight games. The non-stationarity evidence is a single
  five-state toy with a regular, periodic switch.

## Why it's in the library

**It is the cleanest statement of "let the learning rule adapt online".** Market models are
trained on a stream whose statistics change. Discount factors, learning rates, look-back
lengths and target definitions are usually fixed by a backtest sweep, which picks the
value that was best on average over the whole history. The meta-gradient idea is the
alternative: treat those choices as parameters and update them with the gradient of
**next-period, out-of-sample** performance. The inner/outer split, train on one batch and
score the update on the next, is the same discipline as a walk-forward test, applied at the
level of each update.

**The random-walk toy is a regime-switch experiment.** A reward that flips sign on a fixed
clock is a caricature of a signal that changes sign between regimes. The result worth
remembering is not the lower average error but the smaller error spikes after a switch:
a learning rule that adapts its own target can recover faster than any fixed λ.

**It also shows the cost.** The outer loss must be evaluated on fresh data, which in a
backtest means one more layer of nested validation, and every learned meta-parameter is a
new way to overfit the history. Treat it as a design pattern to borrow carefully, not a
recipe.

## Links

- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — the follow-up that
  tests white-box meta-gradients systematically under controlled non-stationarity
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — the wider continual-RL framing that single-lifetime meta-learning belongs to
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — why a network that
  keeps learning on a changing stream can stop adapting at all
- [[schulman-et-al-2015-trust-region-policy-optimization]] — the policy-gradient family whose
  hand-designed objectives FRODO tries to learn
- [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]]
  — distributed actor-learner RL, where the off-policy lag FRODO corrects comes from
