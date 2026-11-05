# The Vanna-Volga Method for Derivatives Pricing

| | |
|---|---|
| **Authors** | Agnieszka Janek (Wrocław University of Technology; supervisor Rafał Weron) |
| **Year** | 2011 (MPRA Paper No. 36127, posted January 2012) |
| **Type** | Master's thesis, 65pp. Posted on MPRA (Munich Personal RePEc Archive) |
| **PDF** | Local copy only (MPRA hosts it openly, but no redistribution licence is stated) |
| **BibTeX** | `janek2011vannavolga` |
| **Status** | Reference. Ch. 2–3 (derivation and variants) and Ch. 5 (calibration tests) carry the content |

## What it is

A careful, self-contained treatment of vanna-volga pricing, the FX market's rule of thumb
for putting the smile into option prices, tested against market data.

- **The idea.** Start from the Black–Scholes (Garman–Kohlhagen) price at the ATM
  volatility. Build a portfolio of three liquid options (the 25-delta put, the ATM option
  and the 25-delta call) that matches the target option's vega, vanna and volga. Add the
  market cost of that portfolio over its Black–Scholes value. The result is a
  smile-consistent price from only three quotes. The justification (Castagna and Mercurio
  2007) assumes a flat but randomly moving implied volatility.
- **Two versions.** The *exact* method solves for the three option weights. *Wystup's
  simplified* method adds the cost of a risk reversal in proportion to the option's vanna
  and the cost of a butterfly in proportion to its volga, ignoring the small cross terms.
- **Barrier options.** The full correction overprices knock-outs, because the hedge is not
  needed once the option has knocked out. Practice scales it by a "survival probability",
  usually the risk-neutral no-touch probability. The thesis also tests a weighted variant.
  Knock-ins are priced as vanilla minus knock-out to keep the in-out parity.
- **Comparison with Heston.** The stochastic-volatility model is calibrated to the same
  smiles for comparison.
- **Results.** EUR/USD (1 July 2004) and EUR/PLN (12 August 2009, 22 July 2010, 23
  March 2011), tenors 1 week to 2 years.
  - Heston fits the 10-delta wings far better: its sum of squared errors is several orders
    of magnitude smaller.
  - The exact vanna-volga method usually fits better than the simplified one. The
    simplified one does better at the 10-delta wings.
  - Both vanna-volga methods work best for short expiries and ordinary smile shapes, and
    badly when the surface is unusual.
  - For EUR/PLN down-and-out calls the best variant priced about 7% below the quoted
    market prices on average. For some barriers the error reached about 23%.
  - The vanna-volga correction can be negative.

## Why it's in the library

**It is the most readable full derivation of vanna-volga.** The method is everywhere in FX
pricing systems and trader conversations, but the original sources are short and informal.
This thesis sets out the replication argument, both variants and the barrier adjustment
in one place, with worked numbers.

**It shows where the shortcut breaks.** On unusual surfaces and in the wings the method can
be far from market, and its barrier prices depend on an ad hoc survival weight. It is a
pricing heuristic, not a model of the dynamics: the thesis says so in its conclusion.

**Limited evidence.** A master's thesis with hand-collected data on a handful of dates in
two currency pairs. Treat the error figures as illustrations.

## Links

- [[wystup-2017-fx-options-and-structured-products]] — the practitioner's book where the
  simplified vanna-volga rule comes from, with its own critical assessment
- [[reiswich-wystup-2012-fx-volatility-smile-construction]] — how the three quoted volatilities
  that vanna-volga takes as input are turned into strikes
