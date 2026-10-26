# Online Normalization for Training Neural Networks

| | |
|---|---|
| **Authors** | Vitaliy Chiley, Ilya Sharapov, Atli Kosson, Urs Koster, Ryan Reece, Sofía Samaniego de la Fuente, Vishal Subbiah, Michael James (Cerebras Systems) |
| **Year** | 2019 |
| **Type** | Paper — *Advances in Neural Information Processing Systems 32* (NeurIPS 2019); arXiv:1905.05894v3 [cs.LG], 26pp including appendices |
| **PDF** | `chiley-et-al-2019-online-normalization-for-training-neural-networks.pdf` (in this folder) |
| **BibTeX** | `chiley2019online` |
| **Status** | Reference — read §3.2–3.4 and §4 (Eqs. 8–12); skip the appendix proofs |

## What it is

Batch Normalization rescales each hidden unit using the mean and variance of the current
minibatch. That ties the method to batches, biases the gradient, and breaks for batch size
one, recurrent networks and memory-hungry models. Online Normalization instead keeps
**exponentially decaying running estimates** of each unit's mean and variance, normalises
each new sample with the estimates from before it arrived, and adds a matching correction
in the backward pass so the gradient stays close to the true one.

- **Geometry of normalisation (§3.1, Fig. 1).** Normalised outputs lie on a sphere inside
  the zero-mean subspace. The exact gradient through normalisation is therefore just a
  projection and a scaling (Eq. 5): remove the components along the ones vector and along
  the output itself, then divide by σ.
- **Batch gradients are biased (§3.2, Figs. 2–3).** Normalising a batch of two maps every
  pair to (−1, +1) or (+1, −1), so the gradient is zero almost everywhere. On CIFAR-10,
  moderate batch sizes still give gradients more than 10° off the full-data gradient, and
  **no amount of averaging small batches removes this bias**.
- **Errors in statistics compound with depth (§3.3, Fig. 4).** With ReLU, small errors in
  the estimated variance grow exponentially through a 100-layer network, worst when the
  variance is underestimated. Batch methods avoid this because a batch is exactly
  normalised. An online method needs **layer scaling** (Eq. 9), which rescales all features
  of a layer by their root-mean-square, or a bounded activation.
- **Weight decay sets the effective learning rate (§3.4, Eqs. 6–7).** A normalised layer is
  invariant to the scale of its weights, so L2 decay does not regularise; it balances the
  growth of the weights from SGD steps, and at equilibrium the effective learning rate is
  √(2ηλ).
- **The algorithm (§4, Fig. 6).** Forward: y_t = (x_t − µ_{t−1}) / σ_{t−1}, then update µ and
  σ² with decay α_f (Eqs. 8a–c). Backward: two running error accumulators remove the
  gradient components that should be zero, with decay α_b (Eqs. 11–12). The two decay rates
  are the only new hyperparameters.
- **Results (§5, Table 2).** Matches or slightly beats Batch Normalization on CIFAR-10,
  CIFAR-100 and ImageNet ResNet-50, beats group, layer and instance normalisation, and works
  where batch methods cannot: fully connected nets at batch size one, an RNN and LSTM
  language model, and U-Net segmentation, with **over an order of magnitude less activation
  memory** (Table 1).

## Read with care

- **It normalises hidden activations, not input features.** The paper is about a layer
  inside the network. Using its running-statistics idea on inputs is a natural step but is
  not what is tested here.
- **Stationarity is assumed in spirit.** The theory treats drift in the statistics as coming
  from the weights changing slowly under a small learning rate. Drift in the data itself,
  which is the usual problem with market data, is not studied.
- **Modest gains on standard benchmarks.** On image classification the improvement over
  Batch Normalization is within noise (ImageNet top-1 76.3% vs 76.4%), and the ImageNet
  result is a single run with decay rates carried over from CIFAR.
- **It does not keep a network adaptable on a long changing stream.** Dohare et al. (2024)
  used this method on Online Permuted MNIST: it helped on early tasks, but later the network
  had more dead units, lower effective rank and lower accuracy than plain backpropagation.
  Good streaming statistics are not a cure for loss of plasticity.
- **Two more hyperparameters.** α_f and α_b were chosen by a log-grid sweep; the paper does
  not show how sensitive results are to them across tasks.

## Why it's in the library

**It is normalisation without look-ahead.** Each sample is scaled using only statistics of
samples that came before it, which is exactly the constraint on any feature or activation
computed in a backtest. Batch or full-sample normalisation leaks information across a
batch, or from the future; an exponentially weighted running mean and variance does not.
Eqs. 8a–c are a clean, well-justified form of the streaming z-score, including the cross
term that keeps the variance estimate correct when samples carry several values.

**It works at batch size one and on sequences.** Live inference on a single new day, and
recurrent models over a time series, are both cases where batch statistics are unavailable
or meaningless. A normaliser that behaves the same in training and in single-sample
inference removes a train–live mismatch.

**Two side lessons transfer to small networks.** Estimation errors in normalisation
statistics can blow up with depth unless something bounds the scale. And with
normalisation in place, weight decay acts as a learning-rate control, not a regulariser,
so tuning it is really tuning the step size.

## Links

- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — tests this exact
  method on a long non-stationary stream and finds it worsens plasticity loss over time
- [[lyle-et-al-2024-disentangling-the-causes-of-plasticity-loss-in-neural-networks]] — finds
  layer normalisation and weight decay among the most effective protections against
  plasticity loss
- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] —
  recurrent agents, one of the cases batch normalisation handles badly
- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — how initial scales
  and learning rates, which normalisation interacts with, set the training regime
- [[eldan-shamir-2016-the-power-of-depth-for-feedforward-neural-networks]] — the depth that
  makes stable activation scales necessary in the first place
