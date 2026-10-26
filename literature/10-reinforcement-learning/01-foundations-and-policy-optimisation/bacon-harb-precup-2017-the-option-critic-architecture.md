# The Option-Critic Architecture

| | |
|---|---|
| **Authors** | Pierre-Luc Bacon, Jean Harb, Doina Precup (Reasoning and Learning Lab, School of Computer Science, McGill University) |
| **Year** | 2017 |
| **Type** | Paper — *Proceedings of the Thirty-First AAAI Conference on Artificial Intelligence* (AAAI 2017). arXiv:1609.05140v2 [cs.AI], 9pp |
| **PDF** | `bacon-harb-precup-2017-the-option-critic-architecture.pdf` (in this folder) |
| **BibTeX** | `bacon2017option` |
| **Status** | Reference — read the theorems (Thm 1–2) and the ALE section |

## What it is

An **option** is a temporally extended action: a sub-policy plus a rule for when to stop.
Options let an agent act and plan at more than one timescale, but discovering useful ones
usually needs hand-specified subgoals or extra rewards. Option-critic **learns the options
end to end by policy gradient**: the sub-policies, their termination functions and the
policy over options, all from the task reward, given only the number of options.

- **Setup.** A Markov option is (initiation set, intra-option policy πω, termination βω).
  Options are assumed available everywhere. Execution is call-and-return: pick an option,
  follow it until it terminates, pick again.
- **Values.** QΩ(s, ω) is the value of being in option ω at s; QU(s, ω, a) the value of
  taking action a inside it; U(ω, s′) = (1 − β)QΩ(s′, ω) + β VΩ(s′) the value on arrival,
  mixing "continue" and "stop and re-choose" (Eq. 1–3).
- **Intra-option policy gradient (Thm 1).** The gradient for the sub-policies is the usual
  policy gradient with QU in place of Q, weighted by the discounted occupancy of
  state–option pairs. A local change is judged by its effect on the overall return, not on
  an option-specific pseudo-reward.
- **Termination gradient (Thm 2).** The gradient for βω is −∂β/∂ϑ · AΩ(s′, ω), where
  AΩ = QΩ − VΩ is the advantage of the current option. **If the current option is worse than
  average, termination becomes more likely**; it is a gradient version of interrupting an
  option when a better one exists.
- **Algorithm.** Critic learns QU (or QΩ, with QU estimated from it) by intra-option
  Q-learning on a fast timescale; actor updates policies and terminations more slowly
  (two-timescale actor-critic).
- **Experiments.** Four-rooms: after the goal moves, option-critic **recovers faster** than
  flat actor-critic and SARSA, and learned terminations concentrate near doorways. Pinball
  (continuous state): near-optimal options within about 40 episodes. Atari (Asterix, Ms.
  Pac-Man, Seaquest, Zaxxon) with a shared deep network: beats the original DQN on three of
  four; with two options in Seaquest, one specialises in "up", one in "down".

## Read with care

- **Options shrink without help.** Optimising return alone drives options to terminate
  every step, since primitive actions suffice for any MDP. The deep experiments add a
  termination regulariser ξ = 0.01 and an entropy bonus; without such terms, temporal
  extension is not guaranteed.
- **The number of options is fixed in advance**, and options are available everywhere.
  Learning initiation sets is left open.
- **The Atari comparison is to the 2013 DQN** with a matched episode budget, one parameter
  setting for all games. It shows the method works end to end, not that options beat strong
  flat agents.
- **Interpretability is anecdotal.** The doorway terminations and up/down options are
  illustrations from small or chosen cases.

## Why it's in the library

**Strategies have their own timescales.** A book that holds positions for days, re-ranks
daily and changes regime over months is acting at several timescales at once. The options
framework is the formal version of "choose a sub-strategy, run it until it stops being the
right one". Option-critic shows how to learn both the sub-strategies and the switching rule
from the same objective.

**The termination gradient is a switching rule with a clear reading.** Stop when the current
mode's value falls below the average over modes, by a margin. That margin (ξ) is a
hysteresis band: it trades switching cost against staying too long in a stale mode — the
same trade-off as a rebalance threshold or a regime filter with persistence.

**It is a caution as much as a method.** The finding that unregularised options collapse to
one-step actions is a reminder that hierarchical structure must be paid for with explicit
regularisation, or the optimiser will remove it.

## Links

- [[schulman-et-al-2015-trust-region-policy-optimization]] — policy gradients at the
  primitive level, which option-critic generalises to options
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — reusable skills and temporal abstraction as tools for changing environments
- [[anand-precup-2023-prediction-and-control-in-continual-reinforcement-learning]] — the
  Precup's later split of the value function into permanent and transient components
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — adapting
  behaviour online when the task drifts
- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] — the
  other way to carry information across time: memory instead of temporally extended actions
