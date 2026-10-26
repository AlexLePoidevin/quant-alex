# Recurrent Experience Replay in Distributed Reinforcement Learning

| | |
|---|---|
| **Authors** | Steven Kapturowski, Georg Ostrovski, John Quan, Rémi Munos, Will Dabney (DeepMind, London) |
| **Year** | 2019 |
| **Type** | Conference paper — ICLR 2019. 19pp including appendices |
| **PDF** | `kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `kapturowski2019recurrent` |
| **Status** | Reference — read §2.3, §3 and §5 closely; §4 is benchmark results |

## What it is

The R2D2 paper. It asks how to train a recurrent agent from a replay buffer when the stored
data were produced by older versions of the network. The answer is a small set of training
choices, and the agent built on them was the first to beat the human baseline on 52 of the 57
Atari games.

- **The agent (§2.3).** R2D2 is Ape-X (distributed prioritised replay, 5-step double
  Q-learning, dueling heads, about 256 actors and one learner) with an LSTM after the
  convolutional stack. Replay holds fixed-length sequences of 80 steps that overlap by 40
  and never cross episode boundaries. Rewards are not clipped; instead an invertible value
  rescaling h(x) is used. Priorities mix the max and mean TD error over a sequence (η = 0.9),
  because a plain mean washes out large errors.
- **Two problems with replayed recurrence (§3).**
  - **Initial recurrent state mismatch:** starting each replayed sequence from a zero
    hidden state, as in DRQN, puts the network in a state it never sees when acting.
  - **Representational drift and recurrent state staleness:** a hidden state stored at
    acting time came from older parameters, so it may no longer match what the current
    network would produce.
- **The diagnostic (§3, Fig. 1).** ΔQ: the normalised gap between Q-values computed from
  the hidden state the training strategy produces and from the stored true hidden states,
  measured at the first and last step of a sequence.
- **Two fixes, best combined (§3).**
  - **Stored state:** keep the recurrent state in replay and start from it.
  - **Burn-in:** unroll the first part of each sequence (40 steps) only to warm up the
    state, and train on the rest.
  Burn-in mainly helps by **preventing "destructive updates"** from badly wrong early
  outputs. Stored state does more to cut ΔQ. Together they give the smallest discrepancy
  and the most robust gains.
- **Results (§4, Table 1).** One architecture and one hyperparameter set across Atari-57 and
  DMLab-30. Median human-normalised score on Atari is about four times Ape-X's. DMLab-30 is
  matched with a value-based agent, which earlier only actor-critic methods had managed.
- **What the LSTM does (§5).** A feed-forward ablation loses much of the gain, even on
  near-fully-observed Atari. Cutting the agent's memory at test time (Fig. 5) shows that
  agents trained from stored state use memory more, so they degrade faster when it is
  removed. The authors suggest recurrence also helps through **better representation
  learning**, not only memory.
- **Distributed effects (App.).** Fewer actors means older data in replay (mean parameter
  lag rises from about 1,500 to 5,500 updates going from 256 to 64 actors) and larger ΔQ.

## Read with care

- **Benchmarks, not mechanisms.** The Atari gains combine an LSTM, sequence prioritisation,
  value rescaling, a higher discount and other changes. Ablations (Fig. 4, App.) show only
  the LSTM helps consistently; the rest help some games and hurt others.
- **Few seeds, huge compute.** Results average three seeds (one for some variants), and
  agents use billions of frames. App. figures show R2D2 is less sample-efficient than
  single-actor agents early on.
- **ΔQ is an indirect proxy.** It measures sensitivity to the start state, not the quality
  of the learned memory. The causal story for burn-in (destructive updates) is a hypothesis,
  supported by informal experiments the paper does not show.
- **Memory-critical results are on DMLab.** Atari is close to fully observed with 4-frame
  stacks, so the memory-use analysis rests mainly on one DMLab task.

## Why it's in the library

**Stale state is a general problem for any model trained on its own history.** A replay
buffer of hidden states produced by old parameters is the same issue as a sequence model
whose cached state or features were computed by an earlier fit. R2D2's two fixes carry over:
store the state but expect it to be stale, and warm the model up over a burn-in prefix
before scoring the part that counts.

**Burn-in is a disciplined way to use rolling windows.** When a recurrent model is trained
on windows of price history, the first few steps of each window see a cold state and are
mostly noise. Unrolling but not training on a prefix keeps those steps out of the loss. It is
a cheap, testable change.

**It is also a caution about attribution.** R2D2's results came from many changes at once,
and the authors themselves found only one robust across games. When a strategy improves
after a bundle of changes, ablate each one before believing any single story.

## Links

- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] — the
  zero-start-state recurrent agent this paper improves on
- [[bird-2021-backpropagation-through-time-for-networks-with-long-term-dependencies]] — the
  truncation that fixed-length replay sequences impose
- [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] — R2D2 extended with
  exploration and adaptive discounts
- [[kapturowski-et-al-2022-human-level-atari-200x-faster]] — the same lineage made far more
  data-efficient
- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]]
  — the single-actor state of the art R2D2 is compared against
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — another way a
  network trained on a moving stream of its own data degrades
