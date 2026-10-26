# Towards Generalization and Simplicity in Continuous Control

| | |
|---|---|
| **Authors** | Aravind Rajeswaran, Kendall Lowrey, Emanuel Todorov, Sham Kakade (University of Washington, Seattle) |
| **Year** | 2017 |
| **Type** | Paper — *Advances in Neural Information Processing Systems 30* (NIPS 2017). arXiv:1703.02660v2 [cs.LG], 12pp including appendix |
| **PDF** | `rajeswaran-et-al-2017-towards-generalization-and-simplicity-in-continuous-control.pdf` (in this folder) |
| **BibTeX** | `rajeswaran2017towards` |
| **Status** | Reference — short and readable; read all of §1–5 |

## What it is

A sanity check on deep RL. The authors ask **what is the simplest set of ingredients** that
solves the standard OpenAI Gym MuJoCo benchmarks, and find that **linear policies and
random-feature (RBF) policies are competitive with neural networks**. They then show that
the benchmarks themselves are too narrow, so policies that score well are brittle.

- **Training (§2.1).** A plain natural policy gradient: likelihood-ratio gradient with GAE
  advantages, Fisher matrix from the score outer products, and a **normalised step** of
  fixed KL-like size δ = 0.05 for every task (Eq. 5). The value function is fitted on the
  previous iteration's trajectories to avoid bias.
- **Policies (§2.2).** Linear: a ~ N(W s + b, σ). RBF: the same on top of random Fourier
  features sin(P s / ν + φ), i.e. a two-layer network whose first layer is frozen random.
- **Benchmark results (§3).** On Swimmer, Hopper, HalfCheetah, Walker, Ant and Humanoid, the
  linear policy is competitive on most tasks and the RBF policy beats the published
  TRPO-plus-network results on five of six. Linear policies train **almost 20× faster** and
  reach a performance threshold sooner on four of six tasks.
- **The benchmarks are the problem (§3).** Narrow initial states and early termination
  produce **trajectory-centric** policies: good only on the states they visited. A small
  push makes the walker fall and it cannot get up; a rotated swimmer cannot turn.
- **Diverse training (§4).** Wider initial-state distributions (start lying down, random
  heading), matching reward shaping, no termination, and weaker or heavier bodies. These
  produce **"global" policies that recover from perturbations** never seen in training
  (Fig. 4). Here RBF with 500 features does best, then the network, then linear.
- **Discussion (§5).** Representation: there is no compelling evidence for multi-layer
  networks on these tasks. Modelling: the initial-state distribution and reward are
  assumptions the researcher chooses, and they decide robustness. Optimisation: plain
  REINFORCE was too sensitive to step size; preconditioning helps (Fig. 3b).

## Read with care

- **Benchmark-specific.** The claim is about the Gym-v1 locomotion tasks of 2017, with
  low-dimensional proprioceptive states. It does not say linear policies suffice for
  pixels, long horizons or partial observability.
- **Comparisons use published network results**, from the Gym leaderboard and prior
  papers, not a matched tuning budget. Three seeds per curve.
- **Robustness is tested by hand-chosen perturbations** (pushes, rotations, video). That is
  a step toward measuring generalisation, as the authors say, not a full test.

## Why it's in the library

**Try the linear model first.** The central lesson — a well-optimised simple model matches an
elaborate one on the accepted benchmark — is common in tabular and financial prediction too
([[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]],
[[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]]). Any
claim that a deep policy adds value should beat a linear or random-feature policy trained
with the same optimiser.

**Narrow training distributions make brittle models.** A policy trained only near its own
limit cycle fails once pushed off it. A strategy trained on one regime, one universe or one
rebalance phase is the market analogue: it scores well on states like the ones it saw and
has no response to a shock. The fix here — deliberately widen the training distribution of
starting states and stress conditions — corresponds to training across regimes and
evaluating under perturbation, not only on the realised path.

**The step size should be dimensionless.** Normalising the update by the Fisher metric made
one δ work across all tasks, while a raw learning rate had to be re-tuned for reward scale.
That is a practical point for any system retrained routinely across universes with
different volatility.

## Links

- [[schulman-et-al-2015-trust-region-policy-optimization]] — the trust-region method this
  paper's normalised natural gradient simplifies
- [[fuhrer-tessler-dalal-2024-gradient-boosting-reinforcement-learning]] — another check of
  whether a network is the right function class for an RL policy
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the supervised version of "simple models are competitive"
- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] — the
  same question asked of time-series forecasting
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — generalisation when the environment itself changes
