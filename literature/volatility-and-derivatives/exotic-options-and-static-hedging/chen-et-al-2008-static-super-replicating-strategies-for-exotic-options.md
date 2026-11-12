# Static Super-Replicating Strategies for a Class of Exotic Options

| | |
|---|---|
| **Authors** | Xinliang Chen, Griselda Deelstra, Jan Dhaene, Michèle Vanmaele (K.U. Leuven, Université Libre de Bruxelles, Ghent University) |
| **Year** | 2008 (this version 25 March 2008; published in *Insurance: Mathematics and Economics* 42(3), 2008) |
| **Type** | Journal article (working-paper version), 41pp |
| **PDF** | Not hosted in this repository (no open licence; the journal version is Elsevier copyright) |
| **Find it** | [doi.org/10.1016/j.insmatheco.2008.01.002](https://doi.org/10.1016/j.insmatheco.2008.01.002) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Static+Super-Replicating+Strategies+for+a+Class+of+Exotic+Options%22+Chen) |
| **BibTeX** | `chen2008superreplicating` |
| **Status** | Reference: §1 (the problem and applications), §2 (comonotonicity) and Theorems 1–3 carry the idea; §4 is the finite-strike case and the appendix an algorithm |

## What it is

A model-free upper bound on the price of a basket or Asian option, built only from the
prices of vanilla options on each component.

- **The problem.** The payoff is a call on a weighted sum of prices,
  (w₁X₁ + … + wₙXₙ − K)⁺. For a basket option the Xᵢ are different assets at one date; for
  an Asian option they are one asset at different dates. Vanilla calls on each Xᵢ are
  traded, so each marginal distribution is known, but nothing pins down how the Xᵢ move
  together. What is the most a rational buyer should pay?
- **The answer: assume the worst dependence.** Replace the true joint distribution with
  the *comonotonic* one, in which every Xᵢ is an increasing function of a single uniform
  random variable (perfect positive dependence, the Fréchet–Hoeffding upper bound). The
  sum of comonotonic variables is the largest in convex order among all vectors with the
  same marginals, so the call on it is the most expensive possible. That price is an
  upper bound for any fair price.
- **The bound is a portfolio.** The comonotonic call price splits exactly into a weighted
  sum of vanilla calls, one on each Xᵢ, at strikes Kᵢ chosen so that every Kᵢ sits at the
  same quantile of its own distribution and ΣwᵢKᵢ = K. Buying those calls super-replicates
  the exotic in every state, and it is the cheapest such static strategy, both among
  portfolios of this form and among a much wider class. The bound is also the worst-case
  expectation over all joint distributions with the given marginals.
- **Finite strikes.** In practice only a few strikes trade. The paper replaces each call
  price curve by its linear interpolation (a discrete distribution on the traded
  strikes), shows the bound is then a combination of traded calls with a common
  interpolation weight across assets, proves it is still the cheapest super-replication,
  and proves convergence to the continuous case as strikes become dense. An appendix gives
  an algorithm that avoids evaluating every strike.
- **Uses.** A seller can quote this price and hold no risk; a buyer should never pay more.
  If the exotic trades, comparing its price with the bound detects arbitrage or model
  error. It also bounds unit-linked insurance guarantees. The proofs use actuarial
  stop-loss order and comonotonicity rather than the Lagrange multipliers of Hobson et al.
  (2005), and handle dividends and non-continuous marginals in one framework.

## Why it's in the library

It shows exactly what the option market tells you about dependence: nothing beyond the
marginals, so the only model-free statement about a basket is a bound, reached when
everything moves together. The comonotonic upper bound is the same object as the upper
Fréchet copula in the dependence notes, here turned into a tradeable hedge. It is also a
clean example of static replication: a portfolio of vanillas set up once and never
rebalanced.

## Links

- [[nelsen-2006-introduction-to-copulas]] — the Fréchet–Hoeffding upper bound, the
  comonotonic copula that gives the bound here
- [[finance-tutoring-2024-sklar-theorem]] — marginals plus a copula give the joint
  distribution; here only the marginals are known
- [[howison-2006-barrier-options]] — static hedging of barrier options with vanillas, the
  same once-and-for-all idea for a path-dependent payoff
- [[austing-2011-repricing-the-cross-smile]] — the FX case where a third market (the
  cross) does pin down the dependence between two assets
