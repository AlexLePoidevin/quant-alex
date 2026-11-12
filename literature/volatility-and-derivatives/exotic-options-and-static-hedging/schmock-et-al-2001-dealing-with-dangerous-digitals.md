# Dealing with Dangerous Digitals

| | |
|---|---|
| **Authors** | Uwe Schmock (ETH Zürich), Steven E. Shreve (Carnegie Mellon), Uwe Wystup (Commerzbank) |
| **Year** | 2001 (dated 25 October 2001; first appeared in *Foreign Exchange Risk*, Risk Publications, London) |
| **Type** | Book chapter / practitioner paper, 25pp |
| **PDF** | Not hosted in this repository (first published by Risk Publications; no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Dealing+with+Dangerous+Digitals%22+Schmock) for the title and authors |
| **BibTeX** | `schmock2001dangerous` |
| **Status** | Reference: §2 (the up-and-out call problem), §3 (super-replication under a leverage constraint) and §4 (closed forms) carry it; §5 is a finite-difference recipe |

## What it is

A practitioner's guide to pricing options whose payoffs jump, such as digitals and barriers
that knock out in the money, by charging for the cost of hedging them under a limit on
position size.

- **The problem.** An up-and-out call with the barrier above the strike pays a large
  amount just below the barrier and nothing at it. Near expiry and near the barrier its
  delta and gamma become huge, so a delta-hedger must hold and repeatedly resize a very
  large short position. Such options trade above their Black–Scholes value. A common
  desk fix is to price as if the barrier were further away, with no rule for how far.
- **The idea.** Cap the hedge's leverage: the short position in the currency may not
  exceed α times the option's value. The price is then the smallest initial capital that
  super-replicates the payoff (covers it in every state) under that cap, the *upper
  hedging price*. The difference from the Black–Scholes value is a "danger supplement".
- **How it is computed.** For a payoff depending only on the final price, Broadie,
  Cvitanić and Soner showed the answer is the ordinary risk-neutral price of a
  "face-lifted" payoff: the smallest payoff above the original that satisfies the
  leverage constraint. For path-dependent options the authors (in earlier work) turn the
  problem into a singular stochastic control problem that can often be solved by
  inspection. For the up-and-out call the result is a Black–Scholes problem with a new
  boundary condition at the barrier: the option no longer drops to zero there but to a
  level set by the constraint, which acts like a rebate.
- **Results.** Closed forms for digital calls and puts, all four reverse knock-outs and
  one-touch options, with their Greeks, plus a Crank–Nicolson scheme for range binaries
  with two barriers. Two readings of α: 1/α is the proportional cost of unwinding the
  hedge at knock-out, and pricing with the barrier moved to (1 + 1/α)B gives a price
  close to the constrained one. That turns the desk practice of shifting the barrier
  into a parameter with a meaning.

## Why it's in the library

It explains why some options cost more than any risk-neutral model says, without invoking
a different model: the extra price is the cost of the hedge you are allowed to run. The
same logic (super-replication under constraints, bid–ask bounds instead of one price) is
the theory behind static hedging and model-free bounds elsewhere in this section. The
examples are FX, but the method applies to any payoff with a discontinuity.

## Links

- [[howison-2006-barrier-options]] — the unconstrained barrier option formulas and why
  their gamma makes them hard to hedge
- [[chen-et-al-2008-static-super-replicating-strategies-for-exotic-options]] — another
  super-replication price, with vanillas instead of a constrained dynamic hedge
- [[bossens-et-al-2010-vanna-volga-methods-applied-to-fx-derivatives]] — how the FX market
  actually prices first-generation barriers and touches off the smile
