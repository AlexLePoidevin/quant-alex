# An Approximate Solution for Options Market-Making in High Dimension

| | |
|---|---|
| **Authors** | Bastien Baldacci, Joffrey Derchu, Iuliia Manziuk (École Polytechnique, CMAP) |
| **Year** | 2020 |
| **Type** | Preprint, arXiv:2009.00907v1 [q-fin.TR], 17pp |
| **PDF** | `baldacci-et-al-2020-options-market-making-in-high-dimension.pdf` (arXiv version) |
| **BibTeX** | `baldacci2020options` |
| **Status** | Reference: §2 (the problem), §3 (the quadratic approximation) and §4 (numerics) |

## What it is

A stochastic-control method for a dealer quoting a book of options, written to cope with
many options on many underlyings, where the exact problem is far too high-dimensional to
solve.

- **The problem.** A market maker quotes bid and ask prices on request (as on OTC and RFQ
  markets) for many European options on several stocks. Each stock follows a one-factor
  stochastic volatility model with jumps, with correlations across stocks and across
  volatilities. Order arrival rates depend on the quoted spread and can depend on the
  underlying price and volatility. The dealer is assumed perfectly delta-hedged and
  maximises expected mark-to-market P&L minus a quadratic penalty on the portfolio's total
  vega risk.
- **Why it is hard.** The exact value function lives in a space with one dimension per
  option inventory plus the prices and volatilities, so standard numerical schemes fail.
  Short-dated options make it worse: their greeks change quickly, so they cannot be lumped
  into an aggregate inventory, which rules out factor-style dimension reduction.
- **The approximation.** Expand the Hamiltonian around zero and guess a value function
  that is quadratic in the inventory vector. The HJB equation then becomes a small system
  of non-linear PDEs in time, price and volatility only, solvable by finite differences
  for one or two underlyings. For more underlyings the authors add a non-local term so the
  system can be solved by the Deep Galerkin method. Vega, vanna and vomma are updated
  continuously, and the method works the same with multi-factor volatility models such as
  Bergomi's.
- **The numerical test.** One underlying under Heston (spot–variance correlation −0.7, vol
  of vol 0.7), 20 calls with strikes 97–100 and maturities 0.3–0.7 years. Over 1,000
  simulated days, the P&L per request is about the same as the constant-greeks benchmark
  (Baldacci, Bergault and Guéant) early in the day and stays flat. The benchmark's P&L
  falls after about a tenth of the day as its frozen vegas go stale. The benchmark is
  slightly ahead at the start, because the new method allows for the risk of the
  underlying moving. The P&L distribution of the new method has a better tail.

## Why it's in the library

**It is the dealer's side of the gamma story.** Work on gamma imbalance and flash
crashes, such as [[barbon-buraschi-2021-gamma-fragility]], treats dealer
hedging as a flow that hits the underlying. This paper shows how a dealer actually sets
quotes against a book whose greeks drift intraday. Wider quotes and pulled liquidity when
risk builds are the micro-level behaviour behind those flows.

**It shows why short-dated options are different.** Their greeks change too fast to be
netted into a single exposure. The same property makes short-dated option books
destabilising when one-sided.

**The evidence is a simulation.** The test uses one underlying, 20 options and a model
chosen by the authors, with no real data and no cost of hedging. It shows the method is
tractable and beats a frozen-greeks benchmark. It says nothing about live dealer
behaviour.

## Links

- [[barbon-buraschi-2021-gamma-fragility]] — what dealers' aggregate hedging does to the
  underlying stocks
- [[merton-1976]] — the jump-diffusion setting the dealer's model extends
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — what dealer inventories look like in the data
