# FX Options in Target Zone

| | |
|---|---|
| **Authors** | Peter P. Carr (NYU Tandon); Zura Kakushadze (Quantigic Solutions; Free University of Tbilisi) |
| **Year** | 2017 (*Quantitative Finance* 17(10), 1477–1486; arXiv 1512.01527, December 2015, revised June 2016) |
| **Type** | Journal paper, written as a teaching note (arXiv version, 25pp). Theory only, no data |
| **PDF** | `carr-kakushadze-2017-fx-options-in-target-zone.pdf` (arXiv version) |
| **BibTeX** | `carr2017targetzone` |
| **Status** | Reference: §3 (reflecting boundaries and why the rate differential cannot be deterministic) and §3.4–3.5 (the solvable examples) |

## What it is

How to price options on an exchange rate that a central bank keeps inside a band, such as
USD/HKD between 7.75 and 7.85.

- **Two ways to model a band.** Boundaries can be unattainable, with volatility falling to
  zero fast enough that the rate never touches them. Or they can be attainable, with the
  rate touching a boundary and bouncing back. The first is the more studied approach but
  usually needs numerical solutions or awkward special functions. The paper takes the
  second.
- **Boundaries must reflect.** For no arbitrage, the discounted exchange rate must be a
  martingale and total probability must be conserved. That forces reflecting (Neumann)
  boundary conditions on the pricing equation. Absorbing or mixed boundaries would let
  probability "leak" out of the band.
- **The interest-rate differential cannot be fixed.** With reflecting boundaries, a
  positive exchange rate and no arbitrage, the foreign-minus-domestic short-rate cannot
  be constant, or even a deterministic function of time. It has to depend on where the
  rate sits in the band: positive near the lower boundary, negative near the upper one.
  The authors read this as uncovered interest parity at work inside the band.
- **Local volatility vanishes at the edges.** The exchange rate's local volatility goes to
  zero at each boundary. The hedge ratio stays finite, so options can still be hedged
  there. In the paper's example the volatility drops off only near the edges: at a tenth of
  the band's width from a boundary it is still about 31% of its peak.
- **Solving it.** The pricing equation becomes a one-dimensional Schrödinger-type
  eigenvalue problem. Because real bands are narrow, the rate process can be chosen for
  convenience without changing prices much. With good choices, call and put prices come
  out as fast-converging series of sines and cosines. One example has mean reversion that
  is close to Ornstein–Uhlenbeck near the middle of the band but solvable in elementary
  functions.
- **What it leaves out.** Option markets sometimes price a chance that the band breaks.
  Models of band breaks are outside the paper.

## Why it's in the library

**It is a clean example of no-arbitrage constraints doing real work.** Requiring the
discounted rate to be a martingale inside a reflecting band pins down how the interest
differential must behave. That is not a modelling choice.

**It covers a regime the rest of the FX material does not.** Most FX smile models assume a
free-floating rate. Pegs and bands (HKD, historically the EUR/CHF floor and the ERM) have
bounded, mean-reverting rates with very different option prices, and a tail risk that is
not in the model: the band breaking, as the Swiss franc floor did in January 2015.

**It is a teaching note.** There is no calibration to market prices, so it shows how to
build such a model rather than how well one fits.

## Links

- [[merton-1976]] — jumps, the missing ingredient for modelling a band that breaks
- [[carr-fisher-ruf-2014-on-the-hedging-of-options-on-exploding-exchange-rates]] — another case where FX no-arbitrage breaks standard model assumptions
