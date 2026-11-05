# A Practical Guide to Quantitative Volatility Trading

| | |
|---|---|
| **Authors** | Daniel Bloch (Quant Finance Ltd) |
| **Year** | 2016 (version 1.2.0, 15 January 2016) |
| **Type** | Book-length working paper, 327pp, SSRN 2715517 |
| **PDF** | Local copy only ("Copyright © 2016 Quant Finance Ltd"; may be copied only with the company's consent) |
| **BibTeX** | `bloch2016voltrading` |
| **Status** | Reference, written from the abstract, the introduction, the table of contents and a skim of chapters 5–7 |

## What it is

A long monograph, part textbook and part research report, on pricing and trading
volatility. It runs from Black–Scholes to the author's own model of the implied-volatility
surface.

- **Part I: "quantitative trading in classical economics".**
  - Option pricing and risk management: replication, binomial trees, implied volatility,
    no-arbitrage conditions on the call-price surface, and the Greeks and simple hedges.
  - The statistics of asset returns: fat tails, volatility clustering, long memory.
  - Models that generate the smile (local and stochastic volatility, jumps) and why the
    smile's *dynamics*, not just its shape, matter for hedging.
- **Part II: "quantitative trading in inefficient markets".**
  - **The case against the textbook.** Returns are multifractal, with long-range
    dependence and abrupt changes in their scaling. That contradicts the efficient-markets
    assumptions behind Black–Scholes, and the author argues it reflects economic cycles,
    crises and large fluctuations.
  - **Market anomalies.** Discrete dividends and repo, handled by rewriting the stock as a
    "pure" process without dividends.
  - **MixVol.** The author's parametric, arbitrage-free model of the implied-volatility
    surface: option prices written as a weighted sum of Black–Scholes prices with shifted
    strikes (a mixture of shifted lognormals), a term structure for each component, and
    calibration by differential evolution. It is pitched as robust and fast enough for
    systematic volatility trading, with risk management built on it.
  - **Applications.** Variance swaps and their replication, Asian options, and dispersion
    trading. Dispersion covers implied correlation, delta-hedged and intrinsic-value hedges,
    the risks in the trade, and replicating basket options with MixVol.

## Why it's in the library

It collects the practitioner volatility toolkit (surface building, smile dynamics,
variance swaps, dispersion) in one place, with a working parametric surface model. It also
makes the argument that fractal, regime-switching returns break the assumptions under
standard option pricing.

Limits:
- It is a long working paper by one author, promoting his own model; there is no
  out-of-sample test of MixVol against rival surface models.
- The multifractal critique is a survey of others' findings, not a new result.
- It reads more like lecture notes than a paper: long derivations and few empirical
  results.

## Links

- [[carr-wu-2011-a-new-simple-approach-for-constructing-implied-volatility-surfaces]] — another fast, direct way to build the implied-volatility surface
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the standard derivation of variance-swap replication covered in chapter 7
- [[avellaneda-2009-dispersion-trading]] — dispersion trading, implied correlation and the intrinsic-value hedge, as taught at NYU
- [[jacquier-slaoui-2010-variance-dispersion-and-correlation-swaps]] — dispersion and correlation swaps priced with volatility of volatility
- [[reiswich-wystup-2012-fx-volatility-smile-construction]] — building a smile from a few market quotes, the FX-market version of the same problem
