# Barrier Options

| | |
|---|---|
| **Authors** | Sam Howison (University of Oxford). The file carries no author name; it is the `barriers.pdf` hosted on Howison's Oxford page, and the draft refers to a co-author "Jeff" (probably Jeff Dewynne) |
| **Year** | 2006 (PDF built September 2006; the note says it is "several years old" by then) |
| **Type** | Lecture notes / draft book chapter, 44pp |
| **PDF** | Local copy only (freely hosted by the author, but with no licence to redistribute) |
| **Link** | <https://people.maths.ox.ac.uk/howison/barriers.pdf> |
| **BibTeX** | `howison2006barrier` |
| **Status** | Reference: §0.2–0.4 (the down-and-out call and the reflection principle) carry the method; §0.17 is static hedging. The author warns the note is preliminary, has no references and "Do not trust its accuracy!" |

## What it is

A textbook-style treatment of barrier options as boundary-value problems for the
Black–Scholes equation, written in the style of Wilmott, Howison and Dewynne.

- **Barriers are boundary conditions.** A knock-out option satisfies the ordinary
  Black–Scholes equation everywhere the barrier has not been hit; the barrier only adds a
  condition (value zero, or a rebate) on the line S = B. So any contract can have a
  barrier added, and numerical methods handle them directly.
- **The reflection principle.** After a change of variables the Black–Scholes equation
  becomes the heat equation, and a barrier becomes a boundary held at zero. The method of
  images solves this: reflect the payoff through the barrier with the opposite sign. For
  a down-and-out call with barrier below the strike, the value is the vanilla call minus
  a power-of-S factor times the vanilla call evaluated at the reflected price B²/S.
  In–out parity (knock-in plus knock-out equals the vanilla) then gives the knock-in.
- **A catalogue.** American digitals (one-touches), rebates, double knock-outs, perpetual
  barriers, up-down and ladder options, shout and ratchet (cliquet) options, accrual,
  corridor and switch options, Parisian options, and barriers on futures, where the
  formulas simplify because the power term disappears.
- **Hedging.** Barrier options are "a nightmare to hedge" because of large gamma, and
  hence large exposure to the volatility assumption, near the barrier. On a futures
  contract a down-and-in call is exactly equivalent to E/B puts struck at B, so it can be
  hedged statically: buy the puts once, and sell them if the barrier is hit. On the spot
  price the exact static hedge needs a continuum of strikes, so the note sets up an
  approximate one with a few traded options by least squares over time. The note itself
  calls this section "out of date and mathematically rather naive".

## Why it's in the library

It is a clear first pass at barrier options: one idea (barriers are boundary conditions;
reflection gives the formulas) covers a whole family of contracts. The reflection
principle and the futures static hedge are the starting point for the static-replication
papers in this section. Treat the formulas as a guide, as the author asks; the published
literature on static hedging supersedes the last section.

## Links

- [[schmock-et-al-2001-dealing-with-dangerous-digitals]] — pricing the hedging difficulty
  near the barrier that this note describes
- [[chen-et-al-2008-static-super-replicating-strategies-for-exotic-options]] — static
  hedging with vanillas for basket and Asian payoffs
- [[bossens-et-al-2010-vanna-volga-methods-applied-to-fx-derivatives]] — how barrier and
  touch options are priced off the smile in practice
