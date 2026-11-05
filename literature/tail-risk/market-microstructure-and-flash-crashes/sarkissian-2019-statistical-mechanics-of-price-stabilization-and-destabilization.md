# Statistical Mechanics of Price Stabilization and Destabilization in Financial Markets

| | |
|---|---|
| **Authors** | Jack Sarkissian (Algostox Trading) |
| **Year** | 2019 (SSRN 3514329; its examples use S&P 500 data from July–August 2019) |
| **Type** | Working paper, 17pp, single author, not peer reviewed |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `sarkissian2019statistical` |
| **Status** | Reference: §1 (imbalance and crashes), §3 (the tanh solution), §4–5 (price dynamics and impact) |

## What it is

A physics-style model of how a price settles around fair value, and why a large enough
repricing turns into a crash rather than a quiet random walk. It borrows the Landau theory
of phase transitions.

- **Order and execution imbalance.** Order imbalance is J = (N_b − N_a)/(N_b + N_a), from
  +1 (no sellers) to −1 (no buyers). Execution imbalance I = p_a − p_b is the difference
  in the probability of executing at the ask and the bid, and is taken as roughly linear
  in J. I(s) is the imbalance that would be seen if the security traded at price s; fair
  value s₀ is where I(s₀) = 0.
- **Crashes as a phase transition.** Building on the author's earlier empirical papers,
  one-minute ensemble correlation across S&P 500 stocks and ensemble volatility both spike
  during intraday sell-offs, but only when the drawdown exceeds a critical size D_c.
  Smaller repricings are absorbed as a random walk. Since ensemble correlation is roughly
  I², a large drawdown forces imbalance to one of two branches, near −1 in the sell-off
  and near +1 in the rebound, flipping without passing through balance (the S&P 500 on
  31 July 2019 is the example).
- **Free energy.** The market's free energy is written as a Landau expansion in I and
  dI/ds: (a₂/2)I² + (a₄/4)I⁴ plus gradient terms. With a₂ > 0 near fair value and
  negative far from it, the only physically valid solution is a "dark soliton",
  I(s) = −I₀ tanh((s − s₀)/Δs): a smooth step from buying to selling pressure whose width
  is the bid–ask spread, ε = 2Δs = √(8b₂/a₄).
- **Dynamics after a fair-value jump.** If fair value moves by much more than the spread,
  price converges linearly, moving about half a spread per trade. If it moves by much less,
  it converges exponentially and slowly.
- **Price impact.** Inverting the tanh gives impact δs = Δs·T·atanh(n/(NT)) for an order of
  size n against top-of-book size N executed over T: roughly linear for small orders,
  blowing up as the order approaches the available liquidity. In the discussion the
  author estimates that SPY needs a move of about 25bp, 6–8 times its 3–4bp spread, to set
  off a critical event.

## Why it's in the library

**It describes crashes as a change of regime, not a large draw from the same
distribution.** Below a threshold the market absorbs a repricing as noise; above it,
correlation and volatility jump together and order flow becomes one-sided. That matches
how flash crashes and liquidity events look in the data, and it is why correlation and
volatility estimated in calm periods say little about the crash state.

**The impact formula has the right shape.** Impact that is close to linear for small
orders and explodes as an order consumes the book is the practical reason large orders
are split up, and the mechanism behind sell programmes overwhelming liquidity.

**Treat it as a phenomenological sketch.** The free-energy expansion is assumed, not
derived. The empirical support is the author's own earlier working papers and a few
intraday charts. The author says it does not model the crash itself (overshoot,
oscillation, the sign flip). The "quantum" framing it builds on is the author's own and
not widely used.

## Links

- [[ang-chen-2002]] — correlations rise in down markets, measured at monthly frequency
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why calm-period dependence says
  nothing about joint crashes
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the market-wide version: a shock large
  enough to flip volatility-sized strategies from buyers to sellers
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — correlation rising sharply in a real crash, measured
