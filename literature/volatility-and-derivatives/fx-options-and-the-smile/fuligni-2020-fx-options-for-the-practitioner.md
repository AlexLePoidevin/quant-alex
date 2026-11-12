# FX Options for the Practitioner

| | |
|---|---|
| **Authors** | Chris Fuligni (Credit Suisse International, FX sales and structuring) |
| **Year** | 2020 (dated 23 January 2020) |
| **Type** | Slides, 101pp. A bank presentation built around the author's career in FX options |
| **PDF** | Not hosted in this repository (Credit Suisse material with bank disclosures, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22FX+Options+for+the+Practitioner%22+Fuligni) for the title and authors |
| **BibTeX** | `fuligni2020fx` |
| **Status** | Reference. Read in full. Rules of thumb and anecdotes rather than tested results |

## What it is

A long practitioner's deck on FX options. The author has been a market maker, prop
trader, structurer and hedge-fund PM. It is ordered by period, from exchange-traded
vanillas in the early 1990s to correlation products after 2006, which mirrors how the
FX options market itself developed.

- **Who uses FX options.** Corporates hedge cash flows; private clients buy notes that sell
  volatility for yield; speculators trade vanillas, barriers, pure volatility products,
  multi-currency correlation products and hybrids. The author's rough split is that
  90–95% of funds are directional premium traders who "often think they are trading
  volatility"; the rest trade volatility and correlation.
- **Greeks and higher-order greeks.** Delta, gamma, theta and vega, then vanna (change in
  vega with spot, which the market prices through risk reversals) and volga (change in
  vega with volatility, priced through butterflies). Sega and rega are the P&L sensitivity
  to butterfly and risk-reversal quotes.
- **Fat tails.** A table of USD/JPY daily moves, 1995–2005: 29 moves of 4–5 standard
  deviations where a normal model expects none, and one move of over 9.
- **Vol-trading rules of thumb.** ATM premium is roughly proportional to volatility times
  √time, vega to √time and gamma to 1/(vol × √time). Calendar spreads use flat and forward
  volatility, and the smile is quoted as ATM + butterfly ± ½ risk reversal.
- **Barriers and touches.** Pricing by replication: a knock-out behaves like a risk
  reversal, a reverse knock-out like a butterfly. Arbitrage identities: knock-in plus
  knock-out equals the vanilla, and one-touch plus no-touch equals the discount factor.
  Rules of thumb for what discount to the vanilla makes each barrier type worth buying.
- **Why FX skew exists.** Interest-rate differentials and carry, spot momentum,
  devaluation risk in emerging markets (USD/ZAR risk reversals always favour ZAR
  puts), and supply and demand at particular strikes. The risk reversal reflects the
  correlation between spot and implied volatility.
- **Pure volatility products.** Forward volatility agreements, volatility swaps, variance
  swaps and options on volatility swaps. A variance swap has constant vega that decays
  linearly, carries more smile value because of its square payoff, and can be closed out
  exactly; a volatility swap cannot. There is a worked 2007 USD/JPY trade, long a
  volatility swap against short a variance swap at equal vega.
- **Correlation products.** Correlation swaps priced off the triangle of three implied
  volatilities (the cosine rule), covariance swaps as three variance swaps, dual
  digitals, worst-of options, external-barrier options and baskets, each with pricing by
  replication and the conditions that make them attractive.

## Why it's in the library

**It is the trader's view of the vol surface.** Most of the topic is models and
calibration. This deck shows how the same objects (risk reversal, butterfly, vanna,
volga) are used to make prices and hedge books, and which simple replications traders
actually rely on.

**It connects FX options to the volatility and correlation products elsewhere in this
section.** The variance-swap and correlation-swap slides are the FX version of the
equity variance-swap literature.

**It is a sales and training deck.** The rules of thumb, the "Sharpe > 2" remark about
volatility traders and the trading stories are not backed by data. The barrier-discount
rules in particular depend on the market and period. Use it for intuition and
vocabulary, not as evidence.

## Links

- [[merton-1976]] — jumps, the formal version of the deck's fat-tailed USD/JPY table and the
  reason the smile exists
- [[bossu-strasser-guichard-2005-just-what-you-need-to-know-about-variance-swaps]] — the
  equity-side primer on the variance swaps the deck covers for FX
- [[barbon-buraschi-2021-gamma-fragility]] — what happens when option dealers are short
  gamma in aggregate, the risk the deck's vol traders manage desk by desk
