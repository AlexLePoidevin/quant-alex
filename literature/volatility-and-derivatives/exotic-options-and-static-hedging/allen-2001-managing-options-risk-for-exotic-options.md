# Managing Options Risk for Exotic Options

| | |
|---|---|
| **Authors** | Unsigned. Attributed to Steve Allen (NYU Courant risk-management course): the text and the named Excel workbooks match the "Managing Exotic Options Risk" chapter of his *Financial Risk Management* (Wiley) |
| **Year** | 2001 (Word file dated January 2001) |
| **Type** | Course notes, 21pp |
| **PDF** | Local copy only (course handout with no licence) |
| **BibTeX** | `allen2001exotic` |
| **Status** | Reference: the binary-option reserve example, the barrier comparison table and the Carr static hedge carry the content |

## What it is

Risk-manager's notes on how to mark and control an exotic option, meaning one with no
liquid market price. The method is to price it at the cost of a hedge built from more
liquid instruments, then measure what that hedge leaves uncovered.

- **The trade-off running through it.** A hedge made of liquid instruments leaves *basis
  risk* (the hedge does not match the exotic exactly). A hedge that matches closely needs
  illiquid instruments or huge sizes and so carries *liquidity risk*. Each step builds on
  the last: forwards hedge forwards, vanillas hedge vanillas, vanillas hedge barriers,
  barriers hedge lookbacks.
- **European payoffs are vanilla portfolios.** Any payoff that depends only on the price at
  one date can be replicated as closely as you like with calls and puts at many strikes
  (Carr–Madan). Worked examples: a gold-in-gold option (101% of an at-the-money call plus
  2% calls at every 1% strike step), the log contract that hedges a variance swap, CMS
  convexity, and compound options. Marking the exotic at its hedge-package cost picks up
  the volatility skew without assuming a model.
- **Binary options and pin risk.** A $10MM one-year S&P binary at the forward is worth
  $4,601,700 at a flat 20% volatility. The same value comes from a call spread $100bn wide
  at 0.01% strike spacing (tiny basis risk, impossible size) or $500MM at 2% spacing
  (tradable, but a near-the-strike finish can leave a $4.5MM gap). Near expiry, delta
  hedging a binary close to its strike becomes a forced bet either way.
- **The reserve method.** Book the binary internally as a one-sided call-spread overhedge
  that always pays at least as much as the binary, and hold the value difference in a
  reserve. In the example $200k of a $400k sale profit is reserved; the firm can see
  windfall gains but never windfall losses. With skew (20.25% vol at 99%, 20% at 101%) the
  binary's value moves from $4.60MM to $5.10MM, showing how skew-sensitive binaries are.
- **Barriers depend on the whole surface.** An up-and-out call (spot 100, strike 100,
  barrier 120, 3 months) never exceeds 2.81 under the flat-volatility formula at any
  volatility, but prices at about 3.09–3.10 with 20% volatility at 100 and 18% at 120,
  using either a local-volatility (Derman–Kani) tree or Carr's static hedge. No single
  flat volatility gives the right price.
- **Three static hedges compared.** Derman–Ergener–Kani ("Forever Hedged") uses vanillas
  of many expiries and inherits the volatility model's errors: a down-and-out hedge set at
  20% volatility misses by up to 0.57 if realised volatility is 30%. Carr–Ellis–Gupta uses
  put–call symmetry to hedge a down-and-out call with K/H puts struck at H²/K, immune to
  the volatility level and to symmetric smiles but not to skew or drift. Optimisation-based
  hedges (Dembo) fit vanillas to the barrier's unwind value across scenarios and give a
  distribution of hedge errors to reserve against.
- **Combinations.** A contingent-premium option is a vanilla plus a forward plus a binary.
  A ratchet (and so, in the limit, a lookback) is a sum of knock-in calls.

## Why it's in the library

**It treats pricing as a hedging and reserving problem.** For an instrument with no
market, the price is the cost of the hedge you could actually run, and the risk is what
that hedge misses. This is a more useful frame than picking a model.

**The binary example makes pin risk concrete.** The same price can be hedged with a
position that is too large to trade or one that leaves a $4.5MM hole. The reserve method
shows how a desk can sell such risk without counting profit it may not keep.

**The barrier table explains why exotics need the full volatility surface.** Under a
skew, the flat-volatility formula cannot reach the correct price at any volatility. This
is the problem the FX smile and vanna-volga material elsewhere in this section is solving.

**The sources are dated.** The notes are from 2001 and lean on Taleb's *Dynamic Hedging*
and Hull. The methods (static replication, local volatility trees) are still standard,
but the market details are not current.

## Links

- [[baldacci-et-al-2020-options-market-making-in-high-dimension]] — a market maker's view
  of the same problem: carrying option inventory across many strikes at a cost
- [[barbon-buraschi-2021-gamma-fragility]] — what dealers' delta hedging of option books
  does to the underlying, the market-wide version of the pin-risk problem
- [[squeezemetrics-2020-the-implied-order-book]] — dealer gamma positioning read as hidden
  buy and sell orders
- [[merton-1976]] — jumps, which break the static barrier hedges' assumption that the spot
  is exactly at the barrier when the hedge is unwound
- [[derman-et-al-1995-static-options-replication]] — one of the static hedges compared
- [[carr-ellis-gupta-1998-static-hedging-of-exotic-options]] — another of the static hedges compared
