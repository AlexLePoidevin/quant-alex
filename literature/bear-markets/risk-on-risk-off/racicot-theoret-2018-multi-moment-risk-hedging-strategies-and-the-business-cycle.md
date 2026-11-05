# Multi-moment Risk, Hedging Strategies, and the Business Cycle

| | |
|---|---|
| **Authors** | François-Éric Racicot (University of Ottawa), Raymond Théoret (UQAM) |
| **Year** | 2018 |
| **Type** | Journal article, *International Review of Economics and Finance* 58, 637–675. Copy is the accepted manuscript (87pp). Monthly hedge fund index returns, January 1997 – June 2016 |
| **PDF** | Local copy only (Elsevier accepted manuscript) |
| **BibTeX** | `racicot2018multimoment` |
| **Status** | Reference: §2 (method), §5 (impulse responses by regime), §6 (systemic risk) and §7 (conclusion) |

## What it is

A study of whether hedge funds actively manage their exposure to market crashes, measured
not just by beta but by co-skewness and co-kurtosis, and whether they do it differently
in expansions and recessions.

- **Measures.** From the four-moment CAPM, each hedge fund strategy's return gets three
  time-varying sensitivities to the market: beta (co-movement with the market return),
  co-skewness (with its square) and co-kurtosis (with its cube). They are estimated each
  month from a BEKK multivariate GARCH.
- **Data.** Ten strategy indices plus a benchmark from two databases (Greenwich
  Alternative Investments and EDHEC), January 1997 – June 2016, 234 monthly observations.
  Shocks come from the VIX (uncertainty), the term spread, the credit spread and
  industrial production growth.
- **Regimes.** A smooth-transition VAR lets the responses differ between expansion and
  recession. The recession probability is a logistic function of a 21-month moving
  average of industrial production growth; the authors chose the parameters "after many
  experiments" to fit their priors. It flags two recessions: August 2001 – September 2002
  and August 2008 – June 2010.
- **Findings.**
  - Beta is the most cyclical: funds raise it in expansions and stabilise it in
    recessions.
  - All three measures react strongly to VIX shocks: after a rise in the VIX, funds cut
    beta and co-kurtosis and raise co-skewness. The higher-moment response is about the
    same in expansion and recession, so it is tied to crises rather than to the cycle.
  - The authors' summary: the typical hedge fund sells insurance in expansions and buys
    it in recessions and crises.
  - Short sellers and managed futures gain at the start of crises (positive co-skewness,
    negative co-kurtosis). Equity market neutral funds struggle to control their
    co-skewness after volatility and credit shocks and are "not so neutral".
  - After a VIX shock the cross-sectional spread of the strategies' risk measures
    narrows: hedge funds behave more alike, which the authors read as higher systemic
    risk.

## Why it's in the library

**Crash risk is co-skewness and co-kurtosis, not volatility.** Measuring how a strategy
co-moves with the market's squared and cubed returns separates "loses when the market
crashes" from "is merely volatile". The finding that funds reshape these exposures
after VIX spikes is evidence that tail exposure is actively managed, and that the
managing is pro-cyclical.

**Market-neutral is not crash-neutral.** The equity-market-neutral result echoes the
2007 and 2020 quant drawdowns: dollar or beta neutrality says nothing about how a book
behaves when correlations break.

**Caveats.** The recession indicator was tuned until it matched the authors' priors;
hedge fund index data have well-known biases (backfill, self-reporting), only partly
treated; the impulse-response results are in-sample and mostly shown as charts. The
conclusion's last sentence appears to drop a "not" ("there should be too much concern
about tail risk").

## Links

- [[kakushadze-2020-quant-bust-2020]] — why dollar-neutral statistical arbitrage behaves
  like a short put in a crash
- [[kinlaw-turkington-2014-correlation-surprise]] — a turbulence measure built from
  unusual co-movement, the market-level counterpart of co-skewness spikes
- [[smales-2016-risk-on-risk-off-financial-market-response-to-investor-fear]] — how
  markets respond to VIX shocks, the shock used here
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the argument that many strategies are
  implicitly short volatility in calm markets
