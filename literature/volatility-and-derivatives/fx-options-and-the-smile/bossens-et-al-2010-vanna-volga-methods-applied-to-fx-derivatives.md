# Vanna-Volga Methods Applied to FX Derivatives: From Theory to Market Practice

| | |
|---|---|
| **Authors** | Frédéric Bossens, Grégory Rayée, Nikos S. Skantzos, Griselda Deelstra (Université Libre de Bruxelles and practitioners) |
| **Year** | 2010 (*International Journal of Theoretical and Applied Finance* 13(8), 1293–1324) |
| **Type** | Journal article; this copy is the arXiv preprint, arXiv:0904.1074v3 [q-fin.PR], May 2010, 28pp |
| **PDF** | `bossens-et-al-2010-vanna-volga-methods-applied-to-fx-derivatives.pdf` (in this folder; arXiv version) |
| **BibTeX** | `bossens2010vannavolga` |
| **Status** | Reference: §3 (FX quote conventions), §4 (the Vanna-Volga method) and §6 (comparison with market prices) carry it |

## What it is

The standard practitioner shortcut for pricing first-generation FX exotics (barriers and
touches) off the volatility smile, explained, justified for vanillas and tested against
dealer quotes.

- **FX quote conventions first.** FX smiles are quoted in delta, not strike, with at least
  four definitions of at-the-money and two delta conventions (with or without the
  premium, spot or forward). Brokers quote an ATM volatility, a 25-delta risk reversal
  (call vol minus put vol, the skew) and a 25-delta butterfly. The quoted butterfly is
  usually the "1-vol" broker strangle, which is not the same as the "2-vol" butterfly
  that describes the smile's curvature. Treating them as equal is harmless when the risk
  reversal is under about 1 vol but wrong for steeply skewed pairs such as USD/JPY.
- **The method.** Price the exotic in Black–Scholes at the ATM volatility, then add the
  cost, at market prices, of the portfolio of three liquid instruments (ATM straddle, risk
  reversal, butterfly) that cancels its vega, vanna (sensitivity of vega to spot) and
  volga (sensitivity of vega to volatility). The risk reversal mainly carries vanna, the
  butterfly volga.
- **Why it works for vanillas.** With a smile quadratic in a moneyness variable, the
  Vanna-Volga price of a vanilla is a first-order Taylor expansion of Black–Scholes around
  the ATM vol: the risk-reversal term prices the smile's slope, the butterfly term its
  curvature. Castagna and Mercurio's exact version is a smile interpolator.
- **Why it needs fixing for exotics.** Near a barrier the correction is too big, and the
  knock-out price can even rise as the barrier approaches spot. Market practice scales the
  vanna and volga terms by a factor built from either the survival probability (chance of
  not touching the barrier) or the expected first exit time. Being a rule of thumb, the
  method also needs explicit no-arbitrage checks (a knock-out never above its vanilla, and
  so on).
- **Sensitivity to inputs.** For a one-year USD/CHF one-touch worth about 4%, an error of
  0.5 vol in the 2-vol butterfly moves the price by 3 points: getting the conventions
  right can matter as much as the model.
- **The test.** Indicative quotes from three major FX dealers for one-touch, double
  one-touch, reverse knock-out and double knock-out options, 3-month and 1-year, in
  USD/CHF (mild skew, January 2009) and USD/JPY (strong skew, November 2008). Neither
  Dupire local volatility nor Heston stochastic volatility, calibrated to vanillas, prices
  the exotics well; Heston does better in the mild-skew pair and local vol in the
  steep-skew pair. Calibrating the Vanna-Volga scaling on one-touch prices alone, with
  a single free parameter (first-exit-time scaling), gives prices close to the dealers'
  range across all four products.

## Why it's in the library

It is the reference for how FX desks price the most traded exotics, and a reminder that
calibrating a model to vanillas says nothing about its dynamics, which is what exotics
depend on. The convention section is useful on its own: anyone building an FX smile from
broker quotes needs it. The test data are indicative prices that dealers probably compute
with a similar Vanna-Volga recipe, so agreement with them shows consistency with market
practice rather than correctness.

## Links

- [[austing-2011-repricing-the-cross-smile]] — making two FX smiles consistent with the
  third (cross) smile when pricing multi-currency products
- [[howison-2006-barrier-options]] — the Black–Scholes barrier and touch formulas that the
  method starts from
- [[schmock-et-al-2001-dealing-with-dangerous-digitals]] — why reverse knock-outs trade
  above their Black–Scholes value, priced as a hedging constraint instead of a smile
  correction
