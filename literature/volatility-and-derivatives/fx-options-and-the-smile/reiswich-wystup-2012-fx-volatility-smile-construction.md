# FX Volatility Smile Construction

| | |
|---|---|
| **Authors** | Dimitri Reiswich, Uwe Wystup (Frankfurt School of Finance & Management; MathFinance AG) |
| **Year** | 2012 (*Wilmott* magazine, July 2012, pp. 58–69). Earlier version: CPQF Working Paper No. 20, Frankfurt School, 2009, revised March 2010 |
| **Type** | Journal article, 12pp (working paper 34pp) |
| **PDF** | Not hosted in this repository (the *Wilmott* article). The working-paper version from EconStor was also supplied: it may be copied only for personal and scholarly use, so it is not kept either |
| **Find it** | [doi.org/10.1002/wilm.10132](https://doi.org/10.1002/wilm.10132) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22FX+Volatility+Smile+Construction%22+Reiswich) |
| **BibTeX** | `reiswich2012smile` |
| **Status** | Reference. Both versions read; the working paper has the proofs and the empirical robustness test |

## What it is

How to turn the three numbers the FX options market quotes for each expiry into a full
implied-volatility smile.

- **The quoting problem.** FX dealers do not quote volatility against strike. For each
  expiry they quote an at-the-money volatility, a risk reversal (the 25-delta call
  volatility minus the 25-delta put volatility) and a strangle (or butterfly) margin over
  ATM. Turning these into strikes needs four choices to be known first: spot or forward
  delta, premium-adjusted or not, and which ATM definition (delta-neutral straddle,
  forward, or spot).
- **Delta and ATM conventions.** The paper sets out the four delta types and their
  formulas. With a premium-adjusted call delta the map from delta to strike is not
  one-to-one, so a given delta can match two strikes; the paper shows how to bound the
  root search. Pairs of OECD currencies use spot delta up to one year and forward delta
  beyond; pairs with an emerging-market currency use forward delta throughout. The
  premium-adjusted delta is the default when the premium is paid in the foreign currency
  (USD/JPY, for example).
- **The quoted strangle is a price, not a volatility.** The market strangle defines one
  volatility, two strikes and hence a strangle price. The smile has to reproduce that
  price at those strikes, not the strangle volatility at the 25-delta points. The
  commonly used shortcut (call vol = ATM + strangle + ½RR, put vol = ATM + strangle −
  ½RR, as in Malz 1997) gets this wrong when the risk reversal is large. With the
  January 2009 USD/JPY data the difference is visible.
- **The "simplified parabolic" formula.** A parabola in delta, with volatility equal to
  ATM plus a linear and a quadratic term in (delta − ATM delta). It matches the ATM and
  risk-reversal quotes automatically; the strangle margin is then a single parameter
  found by a one-dimensional root search so the strangle price matches. It follows the
  sticky-delta rule. The paper proves the strike-to-volatility map exists and gives
  closed-form strike derivatives, which a local-volatility model needs. The smile
  flattens to a constant at extreme strikes.
- **Robustness test (working paper).** Calibrated daily to Bloomberg quotes for EUR/USD,
  GBP/USD, AUD/USD, USD/JPY, USD/CHF and USD/CAD, 1–12 month expiries, October 2003 to
  January 2009, at both the 25-delta and 10-delta quotes. In more than 30,000 calibrations
  the method failed six times, all for 10-delta USD/JPY during the extreme skew after the
  2008 crisis.

## Why it's in the library

**It is the base of FX smile construction.** Every FX option model, from vanna-volga to
stochastic-local volatility, is calibrated to a smile built from these quotes. The paper
is the clearest account of the conventions and of the strangle-price condition that
simpler methods miss.

**It shows that "the data" depends on a convention.** The same three quoted numbers give
visibly different smiles depending on which delta type they are read as. Any analysis
using vendor smile data has to know which convention the vendor assumed.

**Constant wings are a limitation.** Flat extrapolation in the wings is consistent with
Lee's moment formula only if the underlying has finite moments of all orders, which fat
tails rule out. Do not use it to price far out-of-the-money options without checking.

## Links

- [[wystup-2017-fx-options-and-structured-products]] — the book that sets out the same
  quotation and delta conventions for practitioners
- [[merton-1976]] — a jump model, the kind of fat-tailed underlying whose wings a flat
  extrapolation misprices
- [[reiswich-wystup-2010-a-guide-to-fx-options-quoting-conventions]] — the quoting conventions (delta types, ATM definitions) the smile is built from
