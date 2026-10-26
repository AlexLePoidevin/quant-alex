# Agent57: Outperforming the Atari Human Benchmark

| | |
|---|---|
| **Authors** | Adrià Puigdomènech Badia, Bilal Piot, Steven Kapturowski, Pablo Sprechmann, Alex Vitvitskyi, Daniel Guo, Charles Blundell (DeepMind) |
| **Year** | 2020 |
| **Type** | Conference paper — ICML 2020 (PMLR 119). arXiv:2003.13350v1 [cs.LG], 30pp including appendices |
| **PDF** | `badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark.pdf` (in this folder) |
| **BibTeX** | `badia2020agent57` |
| **Status** | Reference — read §1, §3 and §4.4 (the bandit meta-controller); skim the rest |

## What it is

Strong Atari agents scored very high on most games and near zero on a few. Agent57 targets
that tail: it is the first agent above the human baseline on **all 57 games**, measured with
a capped score that rewards coverage of the hard cases rather than blow-out scores on easy
ones.

- **Starting point (§2).** Never Give Up (NGU) is built on R2D2 and adds an intrinsic reward
  for novelty: per-episode novelty from an episodic memory of embeddings, scaled by
  life-long novelty from Random Network Distillation. It trains a **family of N = 32
  policies** in one network, each with its own exploration weight βj and discount γj, from
  very exploratory and short-sighted to purely exploitative and long-sighted.
- **Split value function (§3.1).** Q = Q_extrinsic + βj · Q_intrinsic, with two separate
  networks trained on their own rewards but sharing the target policy. App. B shows the
  objective is equivalent to the combined one. The gain is that **each network handles its
  own reward scale and noise**. On a toy "random coin" grid (§4.2, Fig. 5), the original
  shared network fails as the intrinsic reward grows; the split one does not.
- **Meta-controller (§3.2).** NGU sampled policies uniformly. Agent57 picks the (βj, γj)
  arm per episode with a **sliding-window UCB bandit** run separately on each actor, using
  the episode's extrinsic return as the bandit reward. A sliding window is needed because
  the arm rewards are non-stationary as the agent learns. The same bandit picks the
  evaluation policy, so the discount is in effect chosen per game.
- **Longer credit assignment (§4.3).** Discounts go up to 0.9999 and the BPTT window doubles
  from 80 to 160. The longer window learns more slowly at first but is more stable, with the
  largest gain on Solaris.
- **Results (§4.1, Table 1, Fig. 3).** Capped human-normalised score of 100%, and the best
  low-percentile scores. MuZero has higher mean and median but fails completely on games
  like Venture. **The last game to fall, Skiing, needed about 78 billion frames.**
- **Behaviour of the bandit (Fig. 8).** Some games settle on one arm (high discount for
  Skiing). Others start exploratory and short-sighted and move towards exploitative,
  long-horizon arms as training goes on — a learned curriculum.
- **Transfers to R2D2 (§4.4).** Adding the bandit over discounts alone to R2D2 lifts its
  capped score by nearly 20 points.

## Read with care

- **Enormous data and compute.** Tens of billions of frames per game. The authors say so in
  the conclusion, and the follow-up
  [[kapturowski-et-al-2022-human-level-atari-200x-faster]] exists because of it.
- **Max over training.** The reported score is the maximum of a smoothed evaluation curve
  during training, averaged over seeds. That flatters any method and makes small gaps
  unreliable.
- **Benchmark-specific goal.** "Above human on all 57" is a coverage target on a fixed suite
  of deterministic games. The human baselines themselves are weak on some games.
- **Ablations on a chosen subset.** Component studies use a 10-game "challenging set"
  selected for exploration and credit-assignment difficulty, with three seeds.

## Why it's in the library

**A bandit over hyperparameters is a practical answer to non-stationarity.** Agent57 does
not fix the exploration rate or the horizon; it lets a sliding-window bandit choose among a
family, using realised outcomes. For a strategy run as a family of variants (lookbacks,
horizons, risk aversion), a windowed bandit is a simple, auditable way to shift allocation
as conditions change. Note the cost: the selection signal is noisy, so the window and the
exploration rate matter, and a bandit can chase noise as easily as regime.

**Separate models for separately scaled signals.** Splitting the value into parts learned
by separate networks, each on its own scale, is the same instinct as modelling components of
return (market, sector, residual) separately rather than in one target. The toy example
shows why: one network forced to fit targets of very different size fits neither well.

**Judge on the tail, not the average.** The capped score and low-percentile view reward a
method that never fails badly. That is the right lens for comparing models across many
assets or periods, where a high mean can hide a few disasters.

## Links

- [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]]
  — the recurrent replay agent underneath NGU and Agent57
- [[kapturowski-et-al-2022-human-level-atari-200x-faster]] — the same result with about 200×
  less data
- [[bird-2021-backpropagation-through-time-for-networks-with-long-term-dependencies]] — why a
  longer BPTT window helps long-horizon credit assignment
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — adapting
  hyperparameters online by gradient rather than by bandit
- [[xu-et-al-2020-meta-gradient-reinforcement-learning-with-an-objective-discovered-online]]
  — meta-learning the objective itself, the gradient-based alternative
- [[wallace-bluff-2002-episodic-memory-a-connectionist-interpretation]] — episodic memory and
  novelty detection from the cognitive-science side
