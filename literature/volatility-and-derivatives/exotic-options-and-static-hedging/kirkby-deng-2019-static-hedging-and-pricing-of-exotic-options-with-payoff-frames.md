# Static Hedging and Pricing of Exotic Options With Payoff Frames

| | |
|---|---|
| **Authors** | J. Lars Kirkby; Shijie Deng (Georgia Institute of Technology) |
| **Year** | 2019 (*Mathematical Finance* 29(2), 612–658; doi:10.1111/mafi.12184; SSRN 2501812, 2014) |
| **Type** | Journal paper; the local copy is the authors' 2017 accepted version from ResearchGate, 45pp |
| **PDF** | Not hosted in this repository (Wiley journal; author-uploaded copy with no open licence) |
| **Find it** | [doi.org/10.1111/mafi.12184](https://doi.org/10.1111/mafi.12184) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Static+Hedging+and+Pricing+of+Exotic+Options+With+Payoff+Frames%22+Kirkby) |
| **BibTeX** | `kirkby2019payoff` |
| **Status** | Reference: §4 (the butterfly basis), §5.2 (the ABS method) and §6 (the hedging experiments) carry the results |

## What it is

A method for hedging an option with an unusual payoff using only the strikes that actually
trade. Static replication with vanillas has rested on Carr and Madan's integral formula:
any smooth payoff equals a bond, a forward and a continuum of calls and puts weighted by the
payoff's second derivative. In practice there is a finite set of strikes, and the
discretised formula handles kinks and jumps in the payoff badly. Kirkby and Deng recast the
problem as projecting the payoff onto a space spanned by traded payoffs.

- **The butterfly basis.** Three calls at neighbouring strikes make a butterfly, a small
  tent-shaped payoff. Tents centred on each listed strike form a basis, and any payoff can be
  approximated as a weighted sum of them. The weights convert back into ordinary call
  positions, so the hedge can be traded.
- **Frames.** Using frame and Riesz-basis theory from signal processing, the paper gives the
  dual basis in closed form, so the best approximation (in squared error) has explicit
  weights. A faster variant (alternative biorthogonal sequences, "ABS") gives weights almost
  as good at the cost of simple interpolation. The approximation becomes exact as the strike
  spacing shrinks.
- **Exotic European payoffs.** For capped power straddles on the Russell 2000 and for
  payoffs on an S&P 500 strike grid, the projected hedge has about 2.6 times lower error
  than linear interpolation between strikes at every strike spacing tested. The Carr–Madan
  discretisation is reported as orders of magnitude worse.
- **Variance swaps.** A variance swap is hedged with dynamic futures trading plus a static
  log contract. The log contract is not traded, so it has to be built from vanillas. On a
  Henry Hub natural gas example, simulated under Heston and SABR, the ABS hedge's mean
  absolute error is less than half of interpolation's and beats Carr–Madan.
- **Barrier options.** Semi-static barrier hedges need a European payoff that is not
  traded. Built with the butterfly basis, they do much better than delta hedging for
  down-and-out puts, the case where delta hedging fails worst. Under Heston with traders
  using Black–Scholes at the prevailing volatility, errors remain however often the barrier
  is monitored.
- **Tails.** Strikes run out at both ends. Beyond the last listed strike the hedge is
  extended linearly, and what remains is model-dependent tail risk. The paper says so
  rather than hiding it.
- **Pricing.** Once the weights are known, any model only needs to price the basis
  vanillas. That makes it cheap to price many exotics at once, or to compare one payoff's
  value across several models.

## Why it's in the library

**It is the tool for building payoffs that don't trade.** Variance swaps, log contracts,
power payoffs and semi-static barrier hedges all reduce to "build this European payoff from
the listed strikes". This paper gives the most accurate general way to do it, and states
the error that is left.

**It makes the strike grid part of the hedge.** The available strikes, not the model, decide
how good a static hedge can be. Where strikes stop, the hedge stops, and the remaining risk
depends on the model.

**It connects option replication to function approximation.** The basis idea is the same one
used in signal processing and numerical analysis, and the error bounds come from there.

## Links

- [[derman-et-al-1995-static-options-replication]] — the original backward-matching static
  hedge for barrier options, which this paper generalises
- [[monciaud-reghai-2021-singular-exotic-perturbation]] — the smile dynamics that any
  semi-static hedge is exposed to between set-up and the barrier
