# Continual Backprop: Stochastic Gradient Descent with Persistent Randomness

| | |
|---|---|
| **Authors** | Shibhansh Dohare (University of Alberta), Richard S. Sutton (University of Alberta, Amii, DeepMind Edmonton), A. Rupam Mahmood (University of Alberta, Amii) |
| **Year** | 2021 (v3, 5 May 2022) |
| **Type** | Preprint — arXiv:2108.06325v3 [cs.LG], 18pp including appendices |
| **PDF** | `dohare-sutton-mahmood-2021-continual-backprop-stochastic-gradient-descent-with-persistent-randomness.pdf` (in this folder) |
| **BibTeX** | `dohare2021continual` |
| **Status** | Reference — short; read §1, §3 and §4. Superseded as evidence by the 2024 Nature paper, but clearer on the algorithm |

## What it is

The first statement of "loss of plasticity". Backpropagation has two parts: **gradient
descent**, and **initialisation with small random weights**. The second only happens once.
The paper shows that on long streams of changing data, plain backprop **learns well at first
and then gets steadily worse at adapting**, and proposes a fix that keeps the random part
going.

- **Problems with thousands of changes (§2).** *Bit-Flipping*: a regression target fixed but
  the input distribution shifts every 10,000 steps, with a learner smaller than the target so
  the best approximation keeps moving. *Online Permuted MNIST*: pixels re-permuted after each
  pass. *Slippery Ant*: a PyBullet robot whose ground friction is resampled every 10M steps.
- **Backprop degrades (§3).** Across six activations, SGD and Adam and a range of step sizes,
  online error first falls then rises. **With ReLU it ends worse than a linear learner.**
  Smaller step sizes only slow the decline. On Permuted MNIST the average weight magnitude
  in the last layer keeps growing.
- **Why (§3).** The only thing that differs between early and late learning is the starting
  weights. So the initial random weights must have special properties — **diverse,
  unsaturated features and small magnitudes** — that training slowly destroys.
- **Continual Backprop (§4, Alg. 1).** Add a **generate-and-test** step to every update. A
  *tester* scores each hidden unit by a running average of its contribution (|activation −
  its mean| × the size of its outgoing weights) times its adaptability (1 / size of its
  incoming weights). Each step, a tiny fraction ρ of mature units with the lowest scores are
  **reinitialised from the original distribution, with outgoing weights set to zero** so the
  network's output is unchanged. New units are protected for m updates.
- **Results.** CBP holds performance level for thousands of changes on all three problems.
  L2 regularisation helps but is fragile (it works for tanh, not ReLU, in Bit-Flipping);
  Online Normalisation helps at first then degrades. CBP is much less sensitive to its
  hyperparameter than L2 is to weight decay. Same computational cost as backprop.

## Read with care

- **The tester is a heuristic.** The authors say so (§6). The utility measure is plausible but
  not derived; an appendix ablation supports each component.
- **Small, idealised problems.** Bit-Flipping uses a 5-unit network. The 2024 Nature paper
  carries the claim to ImageNet, ResNets and longer RL runs.
- **Plasticity, not forgetting.** The paper deliberately does not measure performance on old
  data. A method that keeps learning may still forget.
- **Online, one example at a time.** Most experiments use no mini-batches. How the effects
  scale to large-batch, many-epoch training is left to later work.

## Why it's in the library

**It names a failure that warm-started models can have.** A model that is updated
incrementally on new data, rather than retrained from scratch, may slowly become *worse at
learning*, even if each update looks fine. The symptom is that the model stops responding
to new regimes, not that it forgets old ones.

**It gives a cheap diagnostic and a cheap remedy.** Track weight-magnitude growth and the
fraction of hidden units doing nothing. If they drift upward over successive retrains, the
model is losing plasticity. Selective reinitialisation of unused units is a small change to
any training loop.

**It sharpens the case for periodic fresh retrains.** Retraining from a fresh random
initialisation on each rolling window is, in this view, the crudest way to restore
plasticity: it resets everything. The paper's point is that one can keep what works and
refresh only what has died.

## Links

- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the full, larger
  version of this study, with the same algorithm
- [[sokar-et-al-2023-the-dormant-neuron-phenomenon-in-deep-reinforcement-learning]] — the
  same reset idea in deep RL, selecting units by low activation
- [[lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks]] — why
  the weights grow and units die, and which fixes combine
- [[chiley-et-al-2019-online-normalization-for-training-neural-networks]] — the online
  normalisation baseline used here
- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — the
  forgetting problem this paper sets aside
