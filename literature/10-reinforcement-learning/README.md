# Reinforcement learning

Agents that learn by acting: they choose actions, see rewards, and improve a policy
without being told the right answer. A trading system has the same shape (decide,
observe P&L, adjust), so this section collects the methods. It also covers the problem
that matters most when a model is retrained again and again on a market that keeps
changing: networks that **stop learning** or **forget** what they knew.

Read `01` first. `02` and `04` are the parts that carry over most directly to forecasting
returns and retraining models. `06` is the applied work, read sceptically.

| Folder | What's in it |
|---|---|
| `01-foundations-and-policy-optimisation` | The core policy-optimisation methods: deterministic policy gradients, trust regions (TRPO), maximum-entropy actor-critic (SAC), learned options and Munchausen bootstrapping. Plus two checks on how simple the model can be: linear policies, and gradient-boosted trees in place of a neural network |
| `02-distributional-rl` | Learning the whole distribution of returns rather than its mean: categorical C51, quantile regression (QR-DQN, IQN, FQF), robust quantile losses, and a distributional actor-critic for continuous control. The bridge to quantile and tail-risk (CVaR) forecasting |
| `03-memory-recurrence-and-large-scale-agents` | Recurrent and memory-based agents: DRQN's LSTM for partial observability, R2D2's fixes for stale hidden states, Agent57 and its 200× more data-efficient successor, plus truncated backpropagation through time and episodic memory |
| `04-continual-learning-and-plasticity` | Why networks trained on a changing stream forget what they learned (catastrophic interference) and gradually lose the ability to learn anything new (loss of plasticity, dormant units). Also covers the fixes: selective reinitialisation, layer norm plus weight decay, and splitting values into slow and fast parts |
| `05-meta-learning-and-non-stationarity` | Learning rules that adapt while they learn: meta-gradients that tune an RL objective and its hyperparameters online as the environment changes. Plus two supporting methods: weight uncertainty that scales (radial Bayesian networks) and normalisation from running statistics, with no batches (online normalisation) |
| `06-rl-for-trading` | Two deep RL trading agents, read sceptically: a recurrent Q-network on intraday FX that learns from the reward of every action without exploring, and a PPO system for US stocks with separate buy, sell and stop-loss modules. Kept for their ideas and as worked examples of the cost, survivorship and benchmark problems that inflate RL trading results |

Supervised and end-to-end trading models (DeePM, intraday decision trees) are in
`../04-dimensionality-reduction-and-machine-learning/08-ml-trading-strategies/`.
They are the non-RL route to the same decision, and the baseline any RL trader has to beat.
