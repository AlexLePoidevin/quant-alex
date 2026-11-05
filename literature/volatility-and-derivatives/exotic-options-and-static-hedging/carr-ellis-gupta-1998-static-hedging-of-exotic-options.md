# Static Hedging of Exotic Options

| | |
|---|---|
| **Authors** | Peter Carr (Morgan Stanley), Katrina Ellis, Vishal Gupta (Cornell) |
| **Year** | 1998 (*Journal of Finance* 53(3), 1165–1190) |
| **Type** | Journal article, 26pp |
| **PDF** | Local copy only (journal version, publisher copyright) |
| **BibTeX** | `carr1998static` |
| **Status** | Reference: §I (put-call symmetry), §II (single barriers), §III (double barriers, roll-downs, ratchets, lookbacks), §IV (bounds with carry) |

## What it is

How to hedge barrier-type exotic options with a fixed portfolio of ordinary puts and
calls that is set up once and unwound at most once, instead of being rebalanced
continuously.

- **Put-call symmetry (PCS).** The key result. If the forward price has zero risk-neutral
  drift, no jumps, and a volatility that is symmetric in log(F/F₀) (the same at any two
  levels whose geometric mean is today's forward), then a call struck at K is worth
  √(K/H) puts struck at H whenever √(KH) equals the forward. Example: with the forward at
  $12, one call struck at $16 is worth √(16/9) = 4/3 puts struck at $9 (the scanned text
  reads "4 puts", but equation (4) gives 4/3). The call is arithmetically further out of
  the money yet worth more, because absolute volatility is higher at higher prices. A
  call struck at twice the forward is worth two puts struck at half of it. PCS generalises a result of Bates (1988) and holds under Black's model
  and under smiles that are symmetric in log-moneyness.
- **Down-and-out call.** Buy a call struck at K and sell K/H puts struck at H²/K. If the
  barrier H is touched, PCS says the call and the puts have equal value, so the position
  is closed at zero cost; if not, the puts expire worthless and the call pays off.
  Example: K = 100, H = 95 means selling 1.0526 puts struck at 90.25.
- **Up-and-out call.** A call, minus up-and-in puts and bonds, which in turn are built from
  calls and binary calls. Binary calls are approximated by call spreads, and a
  three-point Richardson extrapolation gets five-decimal accuracy from a few spreads
  (exact Black value $0.292384 in the paper's example).
- **Multiple barriers.** A binary version of PCS handles double knock-outs as an infinite
  but fast-converging series of out-of-the-money options, where each layer cancels the
  previous layer's value at the other barrier. The options needed shrink exponentially
  in number and moneyness, so a few layers give a good approximation (checked against
  the Kunitomo–Ikeda closed form). Roll-down calls, ratchets and lookbacks follow, with lookbacks approximated
  by ratchets with many rungs.
- **When carry is not zero.** With a non-zero rate differential (FX) or dividend yield,
  PCS no longer holds exactly. The paper gives a pair of static hedges that bracket the
  true value, tight for small carry.

## Why it's in the library

**It is the founding paper of static replication for exotics.** The hedge does not need a
volatility estimate, rate forecasts or continuous trading: the holdings are fixed at the
start and liquidated only if a barrier is hit. Since barrier options have large gammas
near the barrier, a static hedge is far cheaper and more robust in practice than a
dynamic one.

**It turns a barrier price into a statement about the smile.** Because the hedge is made
of vanillas, the barrier is worth what those vanillas cost, so its value follows from
today's smile rather than from a model of future volatility, as far as the symmetry
assumption holds.

**Its assumptions are the weak point, and it says so.** PCS needs zero drift, no jumps,
and a symmetric smile. Equity smiles are skewed, so the exact hedges become
approximations; with carry the paper only gives bounds. Later work by Carr and others
relaxes these conditions.

## Links

- [[lipton-sepp-2022-hybrid-method-for-pricing-barrier-options-with-stochastic-volatility]]
  — the model-based alternative: price barriers under stochastic volatility numerically
- [[merton-1976]] — jumps, which break put-call symmetry and with it the exact hedge
- [[derman-et-al-1995-static-options-replication]] — the calendar-spread alternative for static barrier hedges
