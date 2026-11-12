# Pricing of First Generation Exotics with the Vanna-Volga Method: Pros and Cons

| | |
|---|---|
| **Authors** | Uwe Wystup (MathFinance AG; Frankfurt School of Finance & Management) |
| **Year** | 2008 (version 12 July 2008) |
| **Type** | Slides, 70pp |
| **PDF** | Not hosted in this repository (author's slides with no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Pricing+of+First+Generation+Exotics+with+the+Vanna-Volga+Method%3A+Pros+and+Cons%22+Wystup) for the title and authors |
| **BibTeX** | `wystup2008vanna` |
| **Status** | Reference: the vanna-volga recipe and its one-touch example, the barrier hedging slides and the FX correlation triangle are the content; the exercises and accumulator example are supporting |

## What it is

A practitioner course on pricing FX exotics from the vanilla smile, built around the
vanna-volga method.

- **The FX smile.** Volatility is quoted against delta. The butterfly (average OTM vol
  minus ATM vol) measures the smile's curvature; the risk reversal (OTM call vol minus OTM
  put vol) measures its skew. The deck shows EUR/USD and USD/JPY smiles and a month of
  BBA EUR/GBP quotes.
- **Barriers are where the smile matters.** Regular knock-outs have well-behaved deltas.
  Reverse knock-outs (barrier in the money) have deltas that can grow without bound near
  the barrier. A bank hedging a large reverse down-and-out EUR put must keep buying EUR as
  spot falls towards the barrier, which can slow or stop spot reaching it; once the
  barrier breaks, it must sell the hedge back at once. The price of a barrier is not
  monotone in volatility, so there is no single "barrier volatility".
- **Pricing by hedge cost.** Take the Black–Scholes theoretical value, add the cost of
  managing its volatility risk (the overhedge), then add a supplement for delta-hedging
  difficulty, roughly the same as moving the barrier by 0.5–1%.
- **The vanna-volga recipe.** Market price = theoretical value + p × (vanna of the
  exotic ÷ vanna of a risk reversal × the risk reversal's overhedge) + p × (volga of the
  exotic ÷ volga of a butterfly × the butterfly's overhedge). The weight p is the
  probability that the hedge is still needed, usually the no-touch probability. Worked
  example, a one-year USD/JPY one-touch at 127.00 with spot 117.00: theoretical value
  38.2%, overhedge −4.6%, market price 33.6%, hedged by selling 2 risk reversals and 28
  butterflies.
- **Is it consistent?** The deck compares vanna-volga and Heston prices for 6-month
  USD/JPY one-touches against the market, and lists the open choices: which weight p for
  which product, and whether the rule is consistent with the smile. It cites the
  SuperDerivatives patent and Castagna–Mercurio's three-vanilla version.
- **Correlation from the FX triangle.** Because EUR/USD, USD/JPY and EUR/JPY all have
  quoted volatilities, the correlation between any two is implied by the law of cosines.
  With four currencies (a tetrahedron) every pairwise correlation is implied, so
  correlation risk in a multi-currency option becomes vega risk hedgeable with vanillas.
  The method does not carry over to equities, where the cross does not trade.
- **Baskets and structuring.** A basket put on USD, JPY and GBP against EUR (2 July 2004)
  costs 140,000 EUR against 178,000 EUR for three separate vanilla puts. Exercises cover
  replicating double-no-touches, digitals, KIKOs and reverse knock-outs from simpler
  options, and an accumulator's overhedge is priced from its parts.

## Why it's in the library

**It is the market's own pricing rule, written down by someone who used it.** Vanna-volga
is not a model of prices; it is a recipe for what the hedge costs, scaled by how likely
the hedge is needed. That makes clear why FX exotics trade away from any single model's
value.

**The barrier-hedging slide is a market-impact story.** Hedging a large reverse barrier
pushes against spot until the barrier breaks, then reverses violently. This is the same
mechanism as dealer gamma effects in equity index options.

**The FX correlation triangle is a useful fact.** Implied correlation between currency
pairs is observable from three traded smiles, unlike in most markets.

**Read it alongside the 2020 SLV deck in this folder.** That deck, by the same author,
calls vanna-volga outdated and shows where it gives arbitrage prices. These 2008 slides
present the method at its peak, with its consistency problems raised but not resolved.

## Links

- [[barbon-buraschi-2021-gamma-fragility]] — dealers' hedging of option books pushing the
  underlying, measured in equities
- [[squeezemetrics-2020-the-implied-order-book]] — dealer gamma read as resting buy and
  sell orders, the equity analogue of the reverse-barrier hedge
- [[ang-chen-2002]] — correlation that changes with the market, the risk the triangle
  turns into vega
