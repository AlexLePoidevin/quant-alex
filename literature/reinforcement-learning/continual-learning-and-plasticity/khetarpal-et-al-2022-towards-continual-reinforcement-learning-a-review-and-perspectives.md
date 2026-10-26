# Towards Continual Reinforcement Learning: A Review and Perspectives

| | |
|---|---|
| **Authors** | Khimya Khetarpal (Mila, McGill University), Matthew Riemer (Mila, Université de Montréal, IBM Research), Irina Rish (Mila, Université de Montréal), Doina Precup (Mila, McGill University, DeepMind) |
| **Year** | 2022 |
| **Type** | Survey — *Journal of Artificial Intelligence Research* 75, 1401–1476. arXiv:2012.13490v2 [cs.LG], 11 November 2022, 78pp |
| **PDF** | `khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives.pdf` (in this folder) |
| **BibTeX** | `khetarpal2022towards` |
| **Status** | Reference — read §3 and §4 (the taxonomy), skim §5, read §6.2 and §7.2; use the rest as a bibliography |

## What it is

A long review of reinforcement learning when the world keeps changing — also called
lifelong or non-stationary RL. Its main contribution is **vocabulary**: a way to say exactly
*what* is changing and *why*, so that papers that sound alike can be told apart.

- **Why RL suits the problem (§3).** The **stability–plasticity dilemma** (how much weight to
  give past versus recent experience) has a natural answer in continuing RL: care about the
  past **in proportion to how representative it is of the future**. Naive SGD and episodic
  policy-gradient methods instead make myopic updates focused on the current data.
- **A general problem (§4.1).** Every element — states, actions, rewards, transitions,
  observations — may be a function of time.
- **Two common assumptions about change (§4.2).** **Lipschitz** non-stationarity (things
  drift at a bounded rate) and **piecewise** non-stationarity (stable regimes separated by
  change points). The authors note that **with no assumption at all the problem is vacuous**:
  arbitrary change leaves nothing to learn.
- **Scope and driver (§4.3).** *Scope* is which elements change. *Driver* is what causes the
  change: **stationary** task distribution, **passive** (change independent of the agent's
  actions), **active** (the agent's actions cause it), or **hybrid**.
- **Non-stationary MDPs are POMDPs (§4.4, Prop. 2).** Add the unobserved time-varying
  variable to the state and the problem becomes stationary but partially observed. This is
  the formal link between regime change and hidden state.
- **Other learners cause non-stationarity (Prop. 3).** If other agents are learning, the
  world looks non-stationary to each one, even if the rules never change.
- **Approaches (§5).** Explicit retention (storing parameters, distillation, rehearsal),
  exploiting shared structure (modules, abstractions, skills, goals, auxiliary tasks), and
  learning to learn (context detection, learning to adapt, meta-learning).
- **Evaluation (§6).** Benchmarks and metrics; cumulative reward alone is not enough —
  measure forward and backward transfer, interference and recovery speed.
- **Open problems (§7.2).** Including that **separate train and test phases are unnatural**
  in truly continual settings, and that a purely data-driven agent has no reason to keep
  skills for old tasks it has no evidence will return.

## Read with care

- **Breadth over depth.** It is a map, not a method. Specific claims about each approach
  must be checked in the cited papers.
- **Written before the plasticity results.** Loss of plasticity — networks losing the
  ability to learn at all — is only lightly covered. Read with
  [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]].
- **Neuroscience sections (§7.1) are suggestive.** The analogies to brain systems motivate
  ideas but do not test them.

## Why it's in the library

**Markets are a hybrid non-stationary environment.** In the survey's terms, a trading model
faces changes it does not cause (macro regimes, a passive driver) and changes partly caused
by participants adapting, itself included (an active driver). Naming the driver tells you
what can be learned: passive change can at best be tracked or detected, while active change
also requires thinking about how others respond.

**The regime-as-hidden-state view is directly usable.** Proposition 2 says a non-stationary
problem is a stationary one with a missing state variable. That is the formal reason why
adding regime indicators, or memory, to a model can do the same job as retraining it often.

**It gives the right questions for a rolling retrain.** Is change piecewise (regimes and
breaks) or smooth (drift)? Should the model remember old regimes because they recur, or
forget them because they don't? How fast must it recover after a break? The survey does not
answer these for finance, but it makes them precise.

## Links

- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — the origin
  of the forgetting side of the stability–plasticity dilemma
- [[anand-precup-2023-prediction-and-control-in-continual-reinforcement-learning]] — a
  concrete method by one of the same authors, built on this taxonomy
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the plasticity half
  of the dilemma, which this review underplays
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — learning to adapt
  (§5.3.2) in practice
- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] —
  recurrence as the tool for the POMDP view of non-stationarity
