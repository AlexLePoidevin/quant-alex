# Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem

| | |
|---|---|
| **Authors** | Michael McCloskey, Neal J. Cohen (Johns Hopkins University) |
| **Year** | 1989 |
| **Type** | Book chapter — *Psychology of Learning and Motivation*, vol. 24, pp. 109–165 (Academic Press). 57pp |
| **Link** | https://doi.org/10.1016/S0079-7421(08)60536-8 |
| **BibTeX** | `mccloskey1989catastrophic` |
| **Status** | To read — written from the publisher summary and its reputation; check against the chapter before citing |

## What it is

The chapter that named the problem. It asks what happens when a connectionist network (a
neural network trained by small weight adjustments) learns items **one batch after another**
rather than all mixed together. The answer: **new learning can wipe out old learning**, and
not gradually but catastrophically.

- **The setting.** Networks whose knowledge lives in connection weights, learned by repeated
  small updates, and stored in a **distributed** way: each item uses many weights, and each
  weight serves many items. The publisher summary lists the attractions of this — content-
  addressable memory and "automatic generalisation" to untrained items in the same domain.
- **The problem.** When the network is trained **sequentially**, the weight changes that
  encode the new items overwrite the weights that encoded the old ones. The summary calls
  this catastrophic interference.
- **The diagnosis.** The analysis implies that **some interference is unavoidable whenever
  new learning can change weights that also represent old learning** — that is, whenever
  representations overlap. Distributed representation, the property that gives
  generalisation, is the same property that causes the interference.
- **The scope of the evidence.** The authors are careful: the simulations show that
  interference is catastrophic **in specific networks**, not that it must be catastrophic in
  every possible network. The chapter is best known for simple arithmetic-fact and
  list-learning simulations with backpropagation networks.

## Read with care

- **Written without the full text.** This note is based on the publisher summary and on how
  the chapter is cited. The details of the simulations, and how strong the general claims
  are, should be checked in the chapter itself.
- **1989 networks.** Small, shallow, trained by plain backpropagation on toy tasks. Modern
  networks still forget, but the size and mechanism differ, and later work separates
  forgetting from a second problem, loss of plasticity.
- **Forgetting is not the only failure.** The chapter concerns losing old knowledge. A
  network retrained over and over can also lose the ability to learn new things at all —
  see [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]]. The two are
  different and need different fixes.

## Why it's in the library

**It is the origin of the stability–plasticity problem in neural networks.** Every later
paper in this folder cites it. The question it raises — how to learn the new without
destroying the old — is the central trade-off for any model trained on data that keeps
arriving.

**It explains why "just keep training on the latest window" is not free.** A model updated
in place on a rolling window of recent market data will, by this mechanism, overwrite what
it learned from older regimes. Sometimes that is exactly what is wanted (old regimes are
stale). Sometimes it throws away structure that will matter again when an old regime
returns. The chapter makes the cost visible; it does not say which choice is right.

**It frames the retrain-from-scratch versus warm-start choice.** Retraining from scratch on
the full window sidesteps sequential interference, because all items are mixed together.
Warm-starting on only new data invites it. Knowing the mechanism makes the trade-off a
decision rather than an accident.

## Links

- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — the modern review; places catastrophic forgetting inside the stability–plasticity
  dilemma for RL
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the other half of the
  problem: networks that stop learning, not just forget
- [[anand-precup-2023-prediction-and-control-in-continual-reinforcement-learning]] — a
  slow-plus-fast value function, explicitly inspired by complementary learning systems
- [[wallace-bluff-2002-episodic-memory-a-connectionist-interpretation]] — connectionist
  memory models from the same cognitive-science tradition
- [[conklin-et-al-2026-learning-is-forgetting]] — forgetting as compression inside a
  single training run, a different sense of the same word
