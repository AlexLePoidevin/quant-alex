# Implicit Quantile Networks for Distributional Reinforcement Learning

| | |
|---|---|
| **Authors** | Will Dabney, Georg Ostrovski, David Silver, Rémi Munos (DeepMind) |
| **Year** | 2018 |
| **Type** | Paper — *Proceedings of the 35th International Conference on Machine Learning* (ICML 2018), PMLR 80. arXiv:1806.06923v1 [cs.LG], 14pp including appendices |
| **PDF** | `dabney-et-al-2018-implicit-quantile-networks-for-distributional-reinforcement-learning.pdf` (in this folder) |
| **BibTeX** | `dabney2018implicit` |
| **Status** | Reference — read §2.4, §3 and §4; §5 is benchmark tables |

## What it is

QR-DQN learns a fixed set of N quantiles. IQN learns the **whole quantile function**: the
network takes a probability level τ as an extra input and returns the τ-quantile of the
return, Z_τ(x, a) = F⁻¹(τ). Feeding it τ ~ U[0, 1] samples from the return distribution;
feeding it a distorted τ gives a **risk-sensitive** agent.

- **Architecture (§3.1, Eq. 4).** τ is embedded with a cosine basis,
  φ_j(τ) = ReLU(Σ_i cos(πiτ) w_ij + b_j), and multiplied element-wise into the state
  features before the final layers. Approximation error is now set by network size and
  training, not by the number of output quantiles.
- **Loss (Eqs. 2–3).** Draw N values of τ for the current state and N′ values of τ′ for the
  target, and average the quantile Huber loss over all N × N′ pairwise TD errors. Fresh
  samples each step decorrelate the errors.
- **Sample counts (§3.1, Fig. 2).** More τ samples speed early learning; N = N′ = 8 gets most
  of the long-run benefit, and even N = N′ = 1 is about three times DQN.
- **Risk as a sampling distribution (§2.4, §3).** Following Yaari's dual theory of choice, a
  **distortion risk measure** β reweights cumulative probabilities instead of applying a
  utility to outcomes. The distorted value is Q_β = ∫ F⁻¹(τ) dβ(τ), which IQN computes simply
  by sampling τ through β. **CVaR at level η is just τ ~ U[0, η].**
- **Risk-sensitive experiments (§4, Fig. 3).** Four families on six games: cumulative
  probability weighting from prospect theory, Wang's transform, a power law, and CVaR.
  **The risk-averse Wang and power distortions beat risk-neutral**, by a wide margin on two
  games; risk-seeking Wang(1.5) is as good or worse, and underperforms on three of six;
  strong CVaR(0.1) hurts on two games. The authors
  do not know why; one guess is that risk aversion keeps the agent alive longer.
- **Atari-57 (§5).** Risk-neutral IQN reaches mean 1019% / median 218% of human versus
  QR-DQN's 864% / 193%, close to Rainbow, which combines many other improvements, and
  ahead of it on human starts and on the hardest games.

## Read with care

- **No new theory.** Contraction results for fixed quantiles do not automatically extend to a
  learned quantile function; convergence of risk-sensitive control is open. §6 lists both.
- **The network need not output a monotone function.** Nothing forces Z_τ to increase in τ,
  so quantile crossing can occur. The paper does not address it.
- **The risk-sensitive results are small and unexplained.** Six games, a few distortion
  settings, and evaluation by the risk-neutral score. They show the policy class is usable,
  not that any distortion is generally better.
- **Distortion is applied to the policy only.** The learned distribution is the risk-neutral
  one; β changes how actions are chosen, which mixes "what the distribution is" with "which
  action is best under a risk measure" in the bootstrapped target.

## Why it's in the library

**It puts a risk measure into the policy with one line of code.** Choosing actions by CVaR,
Wang's transform or a prospect-theory weighting is a choice of how to sample τ. The same
construction works for any model that outputs a conditional quantile function: rank or size
positions by a distorted expectation of the forecast return rather than its mean, and the
risk preference becomes an explicit, testable parameter.

**Utility versus distortion is a real modelling choice.** Expected utility applies a concave
function to outcomes; Yaari's approach reweights probabilities. They are dual but not the
same, and they behave differently when combining positions. §2.4 is a compact account, worth
reading next to the coherent risk measure literature.

**One network for all quantiles.** A single conditional quantile model that takes τ as input
avoids training separate models per quantile and shares statistical strength across levels.
For a cross-sectional return model this is a cheap way to get a full predictive distribution
per stock and day — with the caveat that monotonicity in τ must be checked.

## Links

- [[dabney-et-al-2018-distributional-reinforcement-learning-with-quantile-regression]] — the
  fixed-quantile predecessor and the quantile Huber loss used here
- [[yang-et-al-2019-fully-parameterized-quantile-function-for-distributional-reinforcement-learning]]
  — keeps the τ embedding but learns which τ to use instead of sampling them
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] — the
  distributional framework and its control-setting caveats
- [[rockafellar-uryasev-2000]] — CVaR, which IQN implements as τ ~ U[0, η]
- [[artzner-delbaen-eber-heath-1999]] — coherent risk measures; which distortions qualify
- [[bernoulli-1738]] — the expected-utility route to risk aversion that distortion measures
  offer an alternative to
