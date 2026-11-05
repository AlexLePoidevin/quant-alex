# Static Options Replication

| | |
|---|---|
| **Authors** | Emanuel Derman; Deniz Ergener; Iraj Kani (Goldman Sachs Quantitative Strategies) |
| **Year** | 1995 (*Journal of Derivatives* 2(4), 78–95); the local copy is the May 1994 Goldman Sachs research note |
| **Type** | Bank research note, later a journal paper, 42pp |
| **PDF** | Local copy only (Goldman Sachs research note, "All rights reserved") |
| **BibTeX** | `derman1995static` |
| **Status** | Reference: "The Principle of Static Replication", the up-and-out call example and Appendix A carry the method |

## What it is

The paper that turned static hedging of barrier options into a general recipe: build a
portfolio of ordinary calls and puts, with fixed weights, whose value matches an exotic
option's value on its boundaries. Once the boundaries match, the two have the same value
everywhere inside them, so the hedge needs no rebalancing until a boundary is hit.

- **The problem it solves.** Delta hedging a barrier option is costly and inaccurate near
  the barrier, where gamma is large. A static hedge replaces continuous trading in stock
  with a one-off position in standard options.
- **The principle.** An option's value inside a region is fixed by its payoff at expiry
  and its value on the region's edges. So match the terminal payoff with options expiring
  at maturity, then work backwards in time: at each earlier date, add options struck beyond
  the boundary (calls above an upper barrier, puts below a lower one) so that the
  portfolio's value equals the target's value on the boundary at that date. Each new
  option expires out of the money at the boundary level, so it does not disturb the
  matches already made. The weights come from a simple backward recursion (Appendix B).
- **The worked example.** A one-year up-and-out call, strike 100, barrier 120, 15%
  volatility, worth 1.913. A 100-strike one-year call plus six calls struck at 120 and
  expiring every two months is worth 2.284, 19% too much, and tracks the target within
  about 30% over most prices and times. With 24 options matched every half-month it is
  worth 2.01. The large errors are close to the barrier near expiry, where the
  option's value is small.
- **Exact hedges in special cases (Appendix A).** Some barrier options can be replicated
  exactly with very few instruments. If the forward equals spot (interest rate equals
  dividend yield), a down-and-in call with the barrier below the strike is replicated by
  K/B puts struck at B²/K. This is the put–call symmetry result the authors credit to
  Peter Carr.
- **What it assumes.** Black–Scholes with fixed volatility and rates, and that the
  portfolio can be unwound at model value the moment the barrier is hit. The hedge is only
  as good as those assumptions; a change in implied volatility between setting it up and
  hitting the barrier leaves an unhedged residual. Costs are deferred "to a future paper".

## Why it's in the library

**It is the practical origin of static hedging.** Later work on static and semi-static
replication (Carr's put–call symmetry, robust replication of barriers, frame-based hedging)
builds on this backward-matching idea or measures itself against it.

**It shows the model risk that a static hedge moves rather than removes.** The options
replace gamma risk near the barrier with exposure to how the volatility surface moves before
the barrier is hit. That is the same smile-dynamics question that local-stochastic-volatility
models are built to answer for exotics.

**It is a clear, numerical introduction.** The tables let you check every step on a
spreadsheet, which makes it a good first read before the more abstract papers.

## Links

- [[kirkby-deng-2019-static-hedging-and-pricing-of-exotic-options-with-payoff-frames]] —
  a modern generalisation: approximate any payoff with a basis built from traded strikes,
  and semi-static barrier hedges as one application
- [[monciaud-reghai-2021-singular-exotic-perturbation]] — the smile-dynamics risk that a
  static barrier hedge leaves behind, priced for exotics
- [[carr-chou-1997-breaking-barriers]] — the reflection-based static hedge for barriers
