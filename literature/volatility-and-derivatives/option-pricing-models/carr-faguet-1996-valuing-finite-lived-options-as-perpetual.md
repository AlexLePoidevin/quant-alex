# Valuing Finite-Lived Options as Perpetual

| | |
|---|---|
| **Authors** | Peter Carr, Dmitri Faguet (Cornell University) |
| **Year** | 1996 (working paper, version of 21 June 1996; SSRN 706; formerly titled "Fast Accurate Valuation of American Options") |
| **Type** | Working paper, 35pp. Numerical tests in the Black–Scholes model |
| **PDF** | Not hosted in this repository (SSRN working paper; no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.706](https://doi.org/10.2139/ssrn.706) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Valuing+Finite-Lived+Options+as+Perpetual%22+Carr) |
| **BibTeX** | `carr1996perpetual` |
| **Status** | Reference: §III (time decay as credit downgrades) is the idea; §IV (Richardson extrapolation and Table 1) is the practical result |

## What it is

A closed-form approximation for American options, which have no exact formula. The paper
replaces the passage of time with a sequence of random "credit downgrades" of a perpetual
option.

- **The problem.** An American put's value and its early-exercise boundary jointly solve
  a free-boundary PDE with no closed form. A perpetual (infinite-maturity) American put
  does have one, from Samuelson and McKean, because time drops out.
- **The annuity analogy.** A finite annuity is worth a perpetuity minus a deferred
  perpetuity, but the same subtraction undervalues an American put. It fixes the exercise
  boundary at the perpetual level, which is suboptimal.
- **Time decay as downgrades.** Instead, split the option's life into n equal steps. Treat
  the option as a perpetual claim that is downgraded one credit class at each jump of a
  Poisson process with intensity n/T. In the last class it is worth its payoff.
  - Each class's value solves an ordinary differential equation in the stock price with
    a closed-form solution. There is no time variable, and space is not discretised.
  - For an annuity this gives the exact value of the discretised problem, which
    converges to the true value as n grows.
  - Numerically this is the method of lines (Rothe's method): time is discretised while
    space stays continuous. The result is an explicit formula for the put value and the
    exercise boundary at each step.
- **Richardson extrapolation.** The raw n-step values converge slowly from below,
  because freezing the boundary over each step restricts the exercise choice. Combining
  the 1-, 2- and 3-step values with alternating weights removes most of the error.
  - Test case: S = K = 100, T = 1, r = 10%, σ = 30%. The "true" value is 8.3378 from a
    2,000-step binomial tree.
  - Raw values are 7.04, 7.62 and 7.84 for n = 1, 2, 3.
  - Extrapolated values reach 8.3311 at 5 points and 8.3371 at 15.
  - A hand-tuned three-point scheme gives 8.3332, accurate to the penny in three steps.
- **Extensions.** The paper adds a constant dividend yield and American calls. It also
  gives an explicit approximation for the critical stock price near expiry.

## Why it's in the library

**It is a trick that recurs.** Replacing a fixed horizon with a random, exponentially
distributed one turns a time-dependent problem into a stationary one. This is the idea
later published by Carr as "Randomization and the American put" (1998). It became known
in the industry as "Canadization", and it is used again for barrier, lookback and other
path-dependent claims. This working paper is its first statement.

**It shows the cost of an approximation in one table.** Table 1 shows slow one-sided
convergence, and extrapolation then fixes most of it. The authors report that Broadie and
Detemple's comparison put the three-point scheme on the speed–accuracy frontier, between
the Barone-Adesi–Whaley quadratic formula and capped-option approximations.

**Limits.** Convergence of the scheme is conjectured, not proved. The fine-tuned weights
in equation (35) were chosen by numerical experiment on test cases. Everything is in the
constant-volatility Black–Scholes model.

## Links

- [[shreve-2004]] — optimal stopping and the American put free-boundary problem
- [[carr-wu-2020-option-profit-and-loss-attribution-and-pricing]] — the same author's much
  later idea of pricing an option from its local theta–gamma balance rather than from its
  terminal payoff
