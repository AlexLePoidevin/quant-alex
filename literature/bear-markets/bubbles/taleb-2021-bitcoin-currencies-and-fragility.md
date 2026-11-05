# Bitcoin, Currencies, and Fragility

| | |
|---|---|
| **Authors** | Nassim Nicholas Taleb (Universa Investments; NYU Tandon) |
| **Year** | 2021 (Quantitative Finance 21(8), 1249–1255) |
| **Type** | Essay with light formal arguments, 6pp. arXiv:2106.14204v2 |
| **PDF** | `taleb-2021-bitcoin-currencies-and-fragility.pdf` (the arXiv version, 2106.14204v2) |
| **BibTeX** | `taleb2021bitcoin` |
| **Status** | Reference: "Vulnerability of revenue-free bubbles" (Principle 1) and the safe-haven fallacies carry the argument |

## What it is

Taleb's case that bitcoin is a fragile, revenue-free bubble that fails as a currency, a store
of value, an inflation hedge and a safe haven.

- **The valuation argument ("cumulative ruin").** An asset that pays nothing and has no
  residual value is worth only what someone later pays for it. If there is any per-period
  probability that it hits an absorbing barrier (miners leave, the technology is replaced,
  interest fades), backward induction gives a present value of zero. To escape, the price
  would have to grow at the discount rate plus the hazard rate forever, with certainty.
  Gold differs because it needs no maintenance and has industrial and jewellery demand.
- **Not a currency.** Pricing in bitcoin would need incomes, costs and balance sheets fixed
  in bitcoin, which needs low volatility against goods. Twelve years in, almost nothing is
  priced in it, and transactions are slow and costly. A good numeraire is the one with the
  lowest variance against a basket of goods; the paper uses the Hunt brothers' silver
  squeeze (1979–80) to show that even gold and silver failed that test.
- **Not a safe haven.** In March 2020 bitcoin fell further than equities and then recovered
  with them on central-bank liquidity. A public ledger is a poor place to hide wealth from a
  government.
- **Concentration.** Holdings follow a power law (tail index about 5/4, the paper says) and
  early holders gain from the price, which the author calls a worse agency problem than
  the one bitcoin was meant to fix.

## Why it's in the library

**The cumulative-ruin argument is the useful part.** It is a general statement about any
asset with no cash flows: a small hazard of permanent abandonment matters more than any
upside story. It applies to speculative assets well beyond crypto.

**Read it as advocacy.** The piece is polemical, has no empirical tests beyond charts of
volatility, and the author is a principal of a tail-hedging firm. Its safe-haven claim rests
mainly on one episode (March 2020).

## Links

- [[jarrow-1992-market-manipulation-bubbles-corners-and-short-squeezes]] — the theory of corners and squeezes, which the Hunt silver episode illustrates
- [[erb-harvey-2013-the-golden-dilemma]] — a systematic test of the claims made for gold, the asset bitcoin is usually compared with
- [[baur-2021-is-gold-a-safe-haven-in-all-currencies]] — what a safe haven has to do in a crisis
- [[gurkaynak-2008-econometric-tests-of-asset-price-bubbles]] — rational bubble models, which the paper's footnote on growth and absorption draws on
