# FX Vanilla Pricing and Smile Calibration

| | |
|---|---|
| **Authors** | A. Garrivier |
| **Year** | 2020 (dated January 2020) |
| **Type** | Working paper, 16pp |
| **PDF** | Local copy only (working paper with no licence) |
| **BibTeX** | `garrivier2020fx` |
| **Status** | Reference: §2 (delta conventions) and §3–4 (market strangle, the two calibrations, the USD/JPY example) |

## What it is

A practitioner's working paper in two halves: the formulas and conventions for pricing
FX vanilla options, and two ways of turning the market's five smile quotes for one expiry
into a volatility for every strike.

- **Pricing and Greeks.** Calls and puts on an exchange rate under Garman–Kohlhagen,
  written undiscounted (discounting depends on the collateral agreement). Theta, vega,
  gamma, vanna and volga in closed form, with remarks on which matter on a desk and why
  textbook theta and delta decay are not what is used in practice.
- **Four kinds of delta.** FX delta depends on whether it is taken against spot or the
  forward, and whether the premium is paid in the risky currency (then the delta is
  "premium adjusted"). G10 pairs use spot delta below one year and forward delta beyond;
  emerging-market pairs use forward delta throughout. Each choice gives a different
  at-the-money (delta-neutral straddle) strike and a different put–call delta parity, and
  premium adjustment also changes gamma.
- **How the smile is quoted.** Five numbers per expiry: ATM volatility, the 25- and
  10-delta risk reversals, and the 25- and 10-delta *market* strangles. A market
  strangle's single volatility fixes both the strikes of its legs and its price; it is not
  the same as the "smile strangle" priced off the true smile, and recovering the smile
  means matching market-strangle prices, not volatilities.
- **Calibration 1: volatility as a function of delta.** Following Reiswich and Wystup, an
  interpolator through five (put delta, volatility) points. The two smile-strangle spreads
  are the unknowns; risk reversals hold by construction, and the spreads are solved so the
  market strangles reprice. Needs a non-oscillating interpolator and an extrapolation rule
  beyond 10 delta.
- **Calibration 2: SVI.** Gatheral's five-parameter "stochastic volatility inspired"
  hyperbola for implied variance against log-moneyness, fitted to reprice ATM, both risk
  reversals and both market strangles. The parameters overlap in effect (shifting m,
  changing b and changing ρ all move the risk reversal), so the fit is not unique and
  depends on the starting guess.
- **Example.** A six-month USD/JPY slice (forward 106.70). SVI is harder to calibrate but
  then easier to use, since volatility is an explicit function of strike, and it has
  sensible wings; the delta method needs a root search for every strike and flattens
  unrealistically for low-delta puts.

## Why it's in the library

**It is the clearest short account of FX smile conventions.** Delta types, premium
adjustment and the market-strangle quote are the details that make FX smiles harder to
build than equity ones, and they are where implementations usually go wrong. Anyone
reading FX volatility data needs to know which delta and which strangle the numbers mean.

**It compares two standard smile builders on real quotes.** The trade-off it reports
(SVI: awkward fit, good wings and direct strike access; delta interpolation: easy fit, poor
extrapolation) is the practical choice behind every FX volatility surface.

**It is an unrefereed working paper.** The derivations are standard, the example is a
single date and pair, and the comparison is visual rather than measured. Use it for the
conventions and the procedure, not as evidence about which method fits better.

## Links

- [[castagna-mercurio-2007-the-vanna-volga-method-for-implied-volatilities]] — the
  vanna-volga method, the other standard way to fill in an FX smile from its quotes
- [[reiswich-wystup-2012-fx-volatility-smile-construction]] — another way to build an FX smile slice from ATM, risk-reversal and strangle quotes
