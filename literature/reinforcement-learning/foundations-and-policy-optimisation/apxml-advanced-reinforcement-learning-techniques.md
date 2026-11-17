# Advanced Reinforcement Learning Techniques

| | |
|---|---|
| **Author** | ApX Machine Learning (apxml.com) |
| **Year** | Online course, accessed November 2026 |
| **Type** | Online course — 8 chapters, about 80 lessons with hands-on practicals; level "Specialist", prerequisites Python plus ML and RL fundamentals |
| **Link** | [apxml.com/courses/advanced-reinforcement-learning](https://apxml.com/courses/advanced-reinforcement-learning) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22Advanced+Reinforcement+Learning%22+ApX) / the web for "ApX Machine Learning Advanced Reinforcement Learning" |
| **BibTeX** | `apxml_advanced_rl` |
| **Status** | Reference — a course syllabus, not a paper |

## What it is

A structured course on deep RL that runs from the MDP basics to the methods used in
practice. The eight chapters:

1. **Foundations and function approximation** — MDPs, Bellman equations, value and policy
   iteration, temporal-difference learning, a first look at policy gradients, and the
   *deadly triad* (function approximation + bootstrapping + off-policy data).
2. **Deep Q-Networks and enhancements** — DQN with experience replay and target networks,
   Double DQN, dueling networks, prioritised replay, distributional RL and Rainbow.
3. **Policy gradients and actor-critic** — baselines, A2C/A3C, generalised advantage
   estimation (GAE), DDPG, TRPO, PPO and SAC.
4. **Exploration** — UCB, Thompson sampling, parameter-space noise, pseudo-counts,
   curiosity from prediction error, random network distillation, information gain.
5. **Model-based RL** — learned dynamics models, Dyna, trajectory sampling, MCTS with
   learned models, and the link to model predictive control.
6. **Multi-agent RL** — stochastic games, non-stationarity, independent learners,
   centralised training with decentralised execution, VDN/QMIX, MADDPG, communication.
7. **Offline (batch) RL** — distributional shift, off-policy evaluation and importance
   sampling, fitted Q-iteration, BCQ, conservative Q-learning (CQL).
8. **Implementation** — network architectures, hyperparameter tuning, action and
   observation spaces, frameworks, distributed RL, reproducibility and debugging.

## Why it's in the library

The rest of this section is individual papers; this is the map that puts them in order.
Chapter 3 is where [[schulman-et-al-2015-trust-region-policy-optimization]],
[[haarnoja-et-al-2018-soft-actor-critic]] and [[silver-et-al-2014-deterministic-policy-gradient-algorithms]]
sit, and chapter 2's distributional lesson is the doorway to the `distributional-rl` folder.

Chapter 7 matters most for trading. A trading agent learns from a fixed history of prices
it cannot act on, so it is an offline-RL problem: the policy is judged on states the data
never visited (distributional shift), and the fixes — staying close to the logged behaviour
(BCQ) or pessimistic value estimates (CQL) — are the RL version of not trusting a backtest
outside the regime it was fitted on. Chapter 8's reproducibility and tuning lessons point
the same way.

## Links

- [[schulman-et-al-2015-trust-region-policy-optimization]], [[haarnoja-et-al-2018-soft-actor-critic]],
  [[silver-et-al-2014-deterministic-policy-gradient-algorithms]] — the chapter 3 methods in their original papers
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]],
  [[dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression]] — the
  distributional RL behind chapter 2's Rainbow lesson
- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] — DQN with
  memory, beyond the course's chapter 2
- [[rajeswaran-et-al-2017-towards-generalization-and-simplicity-in-continuous-control]] — a check
  on how much of chapter 3's machinery is needed
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]] — the
  non-stationary setting the course does not cover
