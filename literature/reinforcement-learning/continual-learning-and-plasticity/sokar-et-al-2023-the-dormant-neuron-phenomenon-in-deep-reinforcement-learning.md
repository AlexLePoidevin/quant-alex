# The Dormant Neuron Phenomenon in Deep Reinforcement Learning

| | |
|---|---|
| **Authors** | Ghada Sokar (Eindhoven University of Technology; work done at Google DeepMind), Rishabh Agarwal (Google DeepMind, Mila), Pablo Samuel Castro (Google DeepMind), Utku Evci (Google DeepMind) |
| **Year** | 2023 (v2, 13 June) |
| **Type** | Conference paper — *Proceedings of the 40th International Conference on Machine Learning* (ICML 2023), PMLR 202. arXiv:2302.12902v2 [cs.LG], 24pp including appendices |
| **PDF** | `sokar-et-al-2023-the-dormant-neuron-phenomenon-in-deep-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `sokar2023dormant` |
| **Status** | Reference — read §3 (the phenomenon and its causes) and §4 (ReDo, one page); §5 is the evidence |

## What it is

Deep RL networks gradually stop using much of their capacity: **more and more units go
nearly silent and stay that way**. The paper measures this, traces it mainly to the
**moving targets** of RL, and fixes it by periodically **recycling** the silent units.

- **Definition (§3, Def. 3.1–3.2).** A unit's score is its mean absolute activation over a
  batch, divided by the layer's average. It is **τ-dormant** if the score is ≤ τ. An agent
  shows the phenomenon if the count of dormant units **rises steadily** during training.
- **It is widespread (§3, Fig. 2).** Seen in DQN, DrQ(ε) on Atari, and SAC on MuJoCo.
- **Moving targets drive it (Figs. 3–4).** On CIFAR-10, dormant units *fall* with fixed
  labels but **jump each time labels are reshuffled**. In offline RL (fixed data) it still
  happens, but with fixed random targets it does not — so **target non-stationarity, not
  input non-stationarity, is the main cause**.
- **Dormant units stay dormant (Figs. 5–6).** Once silent, a unit almost never wakes up.
  Pruning them during training does not change performance — they really contribute
  nothing.
- **It hurts learning new things (Fig. 8).** A network with many dormant units, fine-tuned
  to a new target, does worse than a random initialisation.
- **More updates per sample, more dormancy (Fig. 7).** A higher replay ratio (gradient
  steps per environment step) produces more dormant units, matching the known performance
  collapse at high replay ratios.
- **ReDo (§4, Alg. 1).** Every so often, find τ-dormant units; **reinitialise their incoming
  weights from the initial distribution and set their outgoing weights to zero.** With small
  τ the network's output barely changes. τ = 0.1 is used in most experiments.
- **Results (§5).** ReDo lets DQN and DrQ(ε) benefit from higher replay ratios instead of
  collapsing; **beats full-layer resets and weight decay** on Atari and SAC; lowering the
  learning rate helps but does not solve it; **doubling or quadrupling width barely helps**;
  recycling random or *most*-active units instead hurts.

## Read with care

- **Correlation in places.** The link between dormant units and the high-replay-ratio
  collapse is a correlation; the authors say it is "difficult to assert conclusively".
- **ReDo does not remove dormancy entirely**, and τ needs tuning (§7, limitations).
- **Atari subsets and short runs.** DQN is evaluated on 17 games for 10M frames rather than
  the usual 200M, to afford many replay ratios. Results are reported as interquartile mean
  with bootstrap intervals, which is good practice.
- **One mechanism among several.** Units can lose usefulness without going silent — for
  example by becoming linear. See
  [[lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks]].

## Why it's in the library

**Any model fitted to targets that move is exposed.** In RL the targets move because they are
bootstrapped from the model's own estimates. In finance, targets move because each rolling
window has a different relation between features and returns. The paper's supervised
reshuffled-labels test is a crude model of a regime change, and dormancy spikes at each one.

**Dormant fraction is a cheap health metric.** Log the share of hidden units with near-zero
activation at each retrain. A steady rise in a model that is warm-started window after
window is a sign it is losing capacity to fit the next regime.

**More training steps on the same data is not free.** The replay-ratio result says that
squeezing more gradient updates out of a limited history increases dormancy. That is
relevant when the history is short — as it is for any rolling window of daily data.

**Recycling is a middle path.** Full retraining from scratch resets everything; pure
warm-starting keeps everything. Recycling only the units that are doing nothing keeps
learned structure while restoring some ability to learn.

## Links

- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the same symptom
  (dormant units, falling rank) shown in supervised continual learning
- [[dohare-sutton-mahmood-2021-continual-backprop-stochastic-gradient-descent-with-persistent-randomness]]
  — the closest relative: reset units by a utility score rather than by activation alone
- [[lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks]] —
  evaluates ReDo against normalisation and finds LN + L2 stronger overall
- [[haarnoja-et-al-2018-soft-actor-critic]] — SAC, one of the agents studied here
- [[kapturowski-et-al-2022-human-level-atari-200x-faster]] — sample-efficient Atari agents,
  where high replay ratios make this problem acute
