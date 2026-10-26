# Fully Parameterized Quantile Function for Distributional Reinforcement Learning

| | |
|---|---|
| **Authors** | Derek Yang (UC San Diego; work done at Microsoft Research), Li Zhao, Tao Qin, Jiang Bian, Tie-Yan Liu (Microsoft Research), Zichuan Lin (Tsinghua University) |
| **Year** | 2019 |
| **Type** | Paper — *Advances in Neural Information Processing Systems 32* (NeurIPS 2019). arXiv:1911.02140v3 [cs.LG], 14pp including appendices |
| **PDF** | `yang-et-al-2019-fully-parameterized-quantile-function-for-distributional-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `yang2019fully` |
| **Status** | Reference — read §3 (Prop. 1 is the idea) and §5; §4 is Atari tables |

## What it is

C51 fixes the return values and learns probabilities. QR-DQN fixes the probabilities and
learns values. IQN samples the probabilities at random. FQF **learns both**: a fraction
proposal network chooses N quantile fractions τ for each state–action, and an IQN-style
quantile value network gives the quantile at each.

- **Staircase approximation (§3.1, Eq. 1).** The return distribution is a weighted mixture of
  N Diracs, Σ (τ_{i+1} − τ_i) δ_{θ_i}, a step function approximating the quantile function.
  Error is measured as the 1-Wasserstein area between the true and step quantile functions
  (Eq. 2, Fig. 1).
- **Where the steps should be (Prop. 1, Eq. 5).** With each value at the midpoint quantile
  (Lemma 1, from QR-DQN), the gradient of W1 with respect to a fraction τ_i is
  2F⁻¹(τ_i) − F⁻¹(τ̂_i) − F⁻¹(τ̂_{i−1}). **This gradient can be computed without computing W1
  itself**, which cannot be estimated without bias. The current quantile network stands in
  for the unknown true quantile function.
- **Training (§3.2–3.3, Alg. 1).** The fraction network is updated with that gradient; the
  quantile value network with the quantile Huber loss on the proposed fractions. Fractions
  are kept ordered by a cumulative softmax, with an optional entropy penalty so they do not
  collapse. Q is the fraction-weighted average of the quantiles.
- **Evidence (§4).** On 55 Atari games with 3 seeds, FQF reaches mean 1426% / median 272% of
  human, ahead of IQN (1112% / 218%) and Rainbow (1213% / 227%) (Table 1), and learns faster
  on some games where final scores are similar (Fig. 2).

## Read with care

- **No convergence guarantee.** The authors cannot show that W1 reaches its minimum when the
  quantile function is itself being learned, or that the QR-DQN contraction result holds for
  self-adjusting fractions (§5). The fraction gradient uses the model's own estimate as the
  truth.
- **Cost.** About 20% slower than IQN, and the gap grows with the number of fractions.
- **Implementation-specific baselines.** IQN is the Dopamine re-implementation, which scores
  below the original paper; two games are dropped. The improvement is relative to that.
- **Better distribution, not proven better decisions.** The agent still acts on the mean. The
  paper asks, but does not answer, how much a better-fitted distribution matters for the
  policy.

## Why it's in the library

**Put the resolution where the distribution changes.** With a fixed budget of quantiles,
equally spaced fractions waste points in the flat middle and under-resolve the tails. FQF's
answer — move the fractions to minimise approximation error — is the right idea for return
distributions, whose interest is in the tails. Proposition 1 is a short, reusable result:
for a step approximation to any monotone quantile function, it tells you where each step
edge should go.

**Optimising a loss you cannot evaluate.** The trick of descending a known analytic gradient
of an un-estimable objective (here W1) recurs in practice. It is also a warning: the
fractions chase the model's own beliefs, so errors in the quantile network feed into where
the model looks. On noisy targets that feedback can lock in early mistakes.

## Links

- [[dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning]] —
  the quantile value network FQF reuses, with sampled rather than learned fractions
- [[dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression]] — the
  midpoint lemma and quantile Huber loss that FQF builds on
- [[malekzadeh-et-al-2024-a-robust-quantile-huber-loss-in-distributional-reinforcement-learning]]
  — swaps a generalised loss into FQF and QR-DQN
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] — the
  fixed-value end of the parameterisation spectrum
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why tail resolution is where a
  distribution model earns or loses its keep
