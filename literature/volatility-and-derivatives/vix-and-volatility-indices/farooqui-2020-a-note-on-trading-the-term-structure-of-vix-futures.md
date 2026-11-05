# A Note on Trading the Term Structure of VIX Futures

| | |
|---|---|
| **Authors** | Anusar Farooqui (independent) |
| **Year** | 2020 (dated 18 March 2020; SSRN 3556779) |
| **Type** | Short note, 11pp, mostly figures. Data January 2013 – 16 March 2020 |
| **PDF** | Local copy only (SSRN download with no open licence) |
| **BibTeX** | `farooqui2020vixterm` |
| **Status** | Reference: read in full; Table 1 holds all the numbers |

## What it is

A short note claiming that a signal built from the VIX futures curve predicts "risk-off"
days, and that switching between selling and buying the volatility term spread on that
signal earns about twice the risk-adjusted return of simple benchmarks.

- **The economic idea.** In intermediary asset pricing, the risk appetite of broker-dealers
  sets risk premia across asset classes, but the balance-sheet measures of that appetite
  are quarterly. Dealers size positions by value-at-risk, which scales with volatility, so
  the price of volatility should track their risk appetite at any frequency. The term
  structure of VIX futures is the proposed real-time proxy.
- **The signal is not disclosed.** The author says only that it is computed from VIX
  futures, and withholds it "due to the commercial possibilities". It feeds a model of the
  probability of a risk-off day tomorrow, with one hyperparameter chosen by 5-fold
  cross-validation on log loss.
- **The strategies.** When the predicted probability is below a cut-off (tuned by
  cross-validation for the highest Sharpe ratio; the optimum is 0.439 for both versions),
  the strategy sells short-term volatility and hedges with medium-term volatility; above
  it, it reverses. A "wholesale" version uses VIX futures sorted into maturity buckets
  (long minus short); a "retail" version uses the VIXY and VIXM ETFs.
- **The reported results (2014 – March 2020).** Annualised Sharpe ratios of 1.16
  (wholesale) and 1.19 (retail), against 0.26 for the S&P 500, 0.56 for unhedged short
  short-term volatility and 0.63 for short volatility hedged with medium-term volatility.
  The two strategies have positive skew (0.29 and 2.12) where the benchmarks have strongly
  negative skew. The note was written in the middle of the March 2020 sell-off, and the
  author says the positive skew is probably driven by that month.

## Why it's in the library

**The idea is worth having; the evidence is not.** Linking the VIX term structure to
dealer balance sheets is a sensible reading of why the curve inverts in a stress (when
dealers cut risk, near-dated volatility is bid). That connects it to the market-structure
pieces in `tail-risk/`.

**But the paper cannot be checked.** The predictive feature is secret, the "out-of-sample"
figures come from cross-validation on the same seven years used to choose both
hyperparameters, there are no trading costs, and the headline is dominated by a few weeks
of March 2020. It is listed as an example of a claimed edge that a reader has no way to
test, next to the transparent model of the same curve by Avellaneda and Papanicolaou.

## Links

- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  a fully specified statistical model of the same futures curve and of the ETNs that roll it
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  long VIX futures cost to hold when the curve is in contango
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — volatility-targeting leverage as the
  mechanism that ties the price of volatility to how much risk the market carries
- [[fassas-hourvouliades-2019-vix-futures-as-a-market-timing-indicator]] — the VIX futures slope as a contrarian signal for the S&P 500 rather than for VIX futures themselves
