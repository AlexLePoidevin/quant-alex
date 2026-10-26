# Loss of Plasticity in Deep Continual Learning

| | |
|---|---|
| **Authors** | Shibhansh Dohare, J. Fernando Hernandez-Garcia, Qingfeng Lan, Parash Rahman, A. Rupam Mahmood, Richard S. Sutton (University of Alberta; Amii) |
| **Year** | 2024 |
| **Type** | Article — *Nature* 632, 768–774 (22 August 2024), doi:10.1038/s41586-024-07711-7. Open access, CC BY 4.0. 26pp including Methods and Extended Data |
| **PDF** | `dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning.pdf` (in this folder) |
| **BibTeX** | `dohare2024loss` |
| **Status** | Reference — the headline paper of this folder; read the main text (7pp) and the Methods section on continual backpropagation |

## What it is

A systematic demonstration that **standard deep learning, trained continually, gradually loses
the ability to learn**, until it learns no better than a shallow or linear network. The
authors call this **loss of plasticity** and separate it from catastrophic forgetting, which
is about losing old knowledge. The fix that works best keeps injecting randomness.

- **Continual ImageNet (Fig. 1).** Thousands of binary tasks, each a new pair of ImageNet
  classes, of constant difficulty. A well-tuned convolutional network reaches about 88% on
  early tasks; **by task 2,000 it has fallen to or below a linear baseline**, for every step
  size tried.
- **Class-incremental CIFAR-100 (Fig. 2).** A ResNet-18 with batch norm, data augmentation,
  L2 and learning-rate schedules — a full modern recipe — is compared with **a network
  retrained from scratch** on the same classes. Incremental training helps at first, but
  after about 40 classes it falls behind, ending **5% below the from-scratch network**.
- **Reinforcement learning (Figs. 3–4).** PPO on the Ant robot with friction changed every
  2M steps degrades badly. **It also collapses with friction held constant**: performance
  rises for about 3M steps then falls, as the agent's own changing behaviour is enough
  non-stationarity.
- **What goes wrong inside (Figs. 2, 4).** Three correlates: the share of **dormant units**
  (active <1% of the time) rises, the **stable rank** of the representation falls (units
  become similar), and **weight magnitudes grow**.
- **What helps (Maintaining plasticity).** **Adam, dropout and normalisation made it worse**
  in their tests (Extended Data Fig. 4). L2 regularisation helps by keeping weights small.
  Shrink and Perturb (L2 plus small noise) helps more. **Continual backpropagation** —
  reinitialise a tiny fraction of the least-used units each step, outgoing weights set to
  zero — maintained plasticity indefinitely in the supervised tests. In RL it was used with a
  little L2.
- **Conclusion (Discussion).** Gradient descent alone is not enough for sustained learning;
  **a random, non-gradient component** is needed to keep variability.

## Read with care

- **"Deep learning does not work" is deliberately strong.** It means: in long continual
  settings, standard methods eventually stop beating shallow ones. Loss of plasticity
  **may not appear at all over a small number of tasks**, as the authors say.
- **Compute limits what was tested.** The networks are classic, not large modern ones; the
  authors note that a systematic study with large language models is not affordable.
- **Head resetting in Continual ImageNet.** Output weights are reset at each task change,
  which gives the learner knowledge of task boundaries (Methods). The other experiments do
  not use it.
- **Best hyperparameters were chosen over the whole run.** Each method's curves are the best
  of a grid search on average accuracy over 5,000 tasks. Fair across methods, but optimistic
  for each one.
- **RL results are noisier.** The authors say themselves that negative RL results are harder
  to make definitive than supervised ones.

## Why it's in the library

**It is direct evidence on warm-start versus retrain-from-scratch.** The CIFAR-100 experiment
is the cleanest statement: carrying weights forward helps for a while, then hurts, compared
with a fresh network trained on the same data. A model refreshed on each rolling window by
continuing from the last window's weights should be checked against a fresh retrain on the
same window, at intervals, to see whether the warm start is still paying.

**Constant data is not enough to be safe.** The constant-friction Ant result shows plasticity
can be lost even when the environment does not change, because the learner's own data
changes. Any model whose training data depends on its own past decisions — for example,
one that learns from the outcomes of its own trades — is in that situation.

**It gives cheap health checks.** Dormant-unit fraction, stable rank of a hidden layer, and
weight norm can be logged at each retrain at almost no cost. Trends in them are an early
warning that a continually updated model is losing the ability to respond to a new regime.

**Remedies are small.** L2, Shrink and Perturb, and selective reinitialisation are each a few
lines of code. They are worth comparing before concluding that a model "has stopped
working".

## Links

- [[dohare-sutton-mahmood-2021-continual-backprop-stochastic-gradient-descent-with-persistent-randomness]]
  — the earlier preprint that introduced continual backprop on smaller problems
- [[lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks]] — takes
  the correlates seen here apart into separate mechanisms with separate fixes
- [[sokar-et-al-2023-the-dormant-neuron-phenomenon-in-deep-reinforcement-learning]] —
  dormant units in value-based RL, and recycling them
- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — forgetting,
  the problem this paper is careful to distinguish from
- [[garrod-keating-2026-unifying-low-dimensional-spectra-in-deep-learning]] — low-rank
  structure in trained networks, the spectral side of falling stable rank
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — a different route
  to adaptivity: learn the hyperparameters online
