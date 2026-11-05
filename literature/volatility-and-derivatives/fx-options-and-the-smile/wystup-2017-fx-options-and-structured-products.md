# FX Options and Structured Products

| | |
|---|---|
| **Authors** | Uwe Wystup (MathFinance AG; Frankfurt School of Finance & Management) |
| **Year** | 2017 (second edition; the first edition was 2006) |
| **Type** | Book, Wiley Finance. About 530pp in four chapters: FX derivatives, structured products, hedge accounting, FX markets |
| **PDF** | Local copy only: MathFinance's 92-page extract of the second edition (contents, preface and sample sections). A 343-page image-only scan of the first edition was also supplied; it is not kept |
| **BibTeX** | `wystup2017fx` |
| **Status** | Reference. Written from the extract: the contents, preface, Ch. 1.1–1.4 (conventions, quotation, premium-adjusted delta), parts of 1.5–1.7 (smile, call spreads, digitals) and the target-forward case studies in Ch. 2.2. The rest of the book was not read |

## What it is

The standard practitioner's book on currency options, written by a former FX structurer
and quant, and organised by product rather than by model. Wystup says plainly it is "not
on valuation … from a programmer's or quant's point of view": the modelling is in his
companion book, *Foreign Exchange Risk* (with Hakala).

- **Chapter 1, FX derivatives.** Conventions first: which currency is domestic, the six
  ways an option price can be quoted (domestic or foreign cash, percent, pips), and why
  delta depends on which currency the premium is paid in. If the premium is paid in the
  foreign currency the hedge is reduced by the premium received, giving the
  *premium-adjusted delta*. Only EUR/USD, GBP/USD, AUD/USD and NZD/USD are quoted
  without the adjustment by default. Then volatility (historic, the smile, ATM
  interpolation with reduced weights for weekends and holidays, volatility cones),
  vanilla combinations (call spreads, risk reversals, straddles, strangles, butterflies,
  seagulls), first-generation exotics (digitals, barriers, touches, compounds, Asians,
  lookbacks, forward starts, quantos), and second-generation exotics on one or several
  currency pairs (range accruals, faders, variance and volatility swaps, forward
  volatility agreements, baskets, best-of and worst-of, correlation swaps).
- **Chapter 2, structured products.** The products corporate treasurers and private
  clients are actually sold: participating and knock-out forwards, shark forwards,
  accumulators, target forwards (TARFs), dual-currency deposits, cross-currency swaps,
  power reverse dual-currency bonds (PRDCs), and treasury case studies. Each comes
  with a term sheet, the motivation for trading it and a "critical assessment".
- **Chapter 3, hedge accounting** under IAS 39 and IFRS 9, with a worked effectiveness
  test for a shark forward.
- **Chapter 4, the market.** Vanna-volga pricing (the trader's rule for adding the cost
  of hedging smile risk to a Black–Scholes price) and its critique, bid–ask spreads,
  systems, how sales and trading are organised, fixings and cut-offs.
- **Bad trades as case studies.** A Turkish trader's leveraged USD/TRY ratio call spread
  in 2008, set up at zero cost and apparently flat in vega and gamma, which drew margin
  calls until it was closed out; the claimant's expert then computed losses with a
  delta hedge that averaged today's and tomorrow's spot, which Wystup shows removes
  the gamma P&L entirely. A USD/CAD pivot target forward sold to a private client in
  July 2008, and an AUD/JPY knock-in-knock-out TARF sold in June 2008. Both paid a small
  gain with high probability and a large loss with low probability, and both lost
  heavily that October.

## Why it's in the library

**It is the reference for FX option conventions.** Smile quotes in FX come as at-the-money
volatility, risk reversals and butterflies tied to a delta, and the delta itself depends
on spot versus forward hedging and on the premium currency. Getting these wrong gives
the wrong strikes, and every FX smile paper in this topic assumes the reader knows them.

**It explains why products trade, not only how to price them.** The structured-products
chapter shows how a zero-cost product is built by selling optionality the client may not
understand. The TARF and pivot-forward cases are a clear account of how a product sold as
low-risk is really short a crash.

**It is a practitioner's book, not a model.** Numbers in the case studies are single
trades, and the book does not test the methods it recommends. Read the quantitative
claims alongside the smile-construction and vanna-volga papers in this topic.

## Links

- [[shreve-2004]] — the stochastic calculus the book recommends as background for its
  quantitative sections
- [[merton-1976]] — jumps in the underlying, the risk that short-optionality structures
  like TARFs are exposed to
