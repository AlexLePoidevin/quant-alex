# Volatility and the Alchemy of Risk: Reflexivity in the Shadows of Black Monday 1987

| | |
|---|---|
| **Authors** | Christopher Cole (Artemis Capital Management) |
| **Year** | 2017 |
| **Type** | Investor letter / research essay — excerpt from Artemis Capital's 2017 Letter to Investors, October 2017, 19pp |
| **PDF** | `cole-2017-volatility-and-the-alchemy-of-risk.pdf` (kept locally; "All rights reserved", reproduction needs Artemis's permission) |
| **BibTeX** | `cole2017alchemy` |
| **Status** | Reference — the opening pages (the definition and size estimates), the coin game and the 1987 section carry the argument; the footnotes give the sources for the asset estimates |

## What it is

A widely read essay by the manager of a long-volatility fund, written thirty years after
Black Monday. Its claim is that when volatility is used as an input for how much risk to
take, it stops being a measurement of risk and becomes a cause of it.

- **The "short volatility trade", broadly defined.** Any strategy that earns small steady
  gains from stability and takes a large loss on change, and that sizes its risk using
  volatility. Cole splits it into:
  - **Explicit** short volatility, about $60bn: pension put and call writing (~$45bn),
    option-overwriting funds (~$8bn), short-VIX exchange-traded products and speculative
    VIX shorts (~$5bn).
  - **Implicit** short volatility, about $1.1–1.4tn: volatility-control funds (~$400bn),
    risk parity ($400–600bn), risk premia (~$250bn) and the equity side of trend following
    ($70–175bn). These never sell an option but, Cole argues, carry the same exposures: to
    variance, to gamma (having to sell more as prices fall), to interest rates and to
    correlations.
  - **Share buybacks**, $3.8tn since 2009, which he treats as a giant short-volatility
    position because buying every dip is mathematically like selling volatility. He
    attributes about 40% of S&P 500 earnings-per-share growth since 2009, and about 30% of
    the price gains, to buybacks.
  The asset figures are a compilation of bank research notes, press reports and one
  interview, which the footnotes acknowledge are "extremely difficult to discern".
- **The feedback loop.** Low volatility lets volatility-targeting strategies lever up,
  their buying and dip-buying suppress volatility further, and the cycle reverses
  violently on a shock. He reports that in 2017 realised and implied volatility were at or
  near record lows and mean-reverting unusually fast after spikes (Brexit, the 2016
  election), with the VIX 3–4 times more sensitive to market moves than in earlier
  low-volatility regimes.
- **Risk parity as a short-correlation trade.** Decomposed, it is a levered bet that
  stocks and bonds stay negatively correlated, layered on ordinary beta. Cole computes
  that repeating the 2008 bond hedge from 2017's starting yields would need the 10-year
  Treasury yield to fall from 2.32% to −0.91%.
- **The coin game.** A coin pays +1% with probability 99% and −50% with probability 1%:
  positive expected return. At 98% it loses money. Small changes in the probability of the
  rare loss decide the sign of any strategy with small frequent gains and large rare losses,
  and in reflexive markets the losses cluster, so the odds worsen after each one.
- **1987 as the template.** Rising inflation and rates (inflation up about 3 points between
  January and October 1987, short-term rates up over 200bp) were the fire;
  portfolio insurance (about $60bn, selling more futures as prices fell, i.e. synthetic short
  gamma) was the explosive. The essay argues the same mix could recur if inflation stops
  central banks from easing into a crisis.
- **Conclusion and recommendation.** Markets underprice both new volatility lows in the
  short term and new highs (VIX above 80) over 2018–2020. If you short volatility, do it
  with limited loss; otherwise pair equities with active long volatility. He cites a 50/50
  mix of the CBOE Long Volatility Hedge Fund Index and the S&P 500 beating the average hedge
  fund since 2005.

The piece is an argument, not a study. The buyback attribution, the AUM estimates and the
"hyper-crash" scenario are not tested here, and the author runs a long-volatility fund, so
the recommendation is also his product. The forecast had a partial check within months: in
February 2018 the short-VIX products it warns about lost most of their value in a single
day, as it says was "a very real possibility". The broader prediction (VIX above 80 by 2020)
came true in March 2020, though from a pandemic rather than the inflation-and-credit
trigger it describes.

## Why it's in the library

**It defines the thing tail-risk hedging hedges.** The section's other sources ask how to
pay for protection against crashes; this one explains why crashes can be made worse by
the strategies that feel safest in calm markets. Its useful idea is that many portfolios
are short volatility without ever trading an option: anything that sizes positions by
recent volatility, rebalances against moves, or relies on a stable stock–bond correlation
has a short-option payoff hidden in it.

**It makes reflexivity concrete.** [[soros-2013]] argues that market participants change
the quantities they estimate. Here the quantity is volatility itself: when leverage is set
from volatility, low volatility produces more leverage, which produces lower volatility,
until it doesn't. The same failure in correlation is
[[mackenzie-spears-2014-formula-that-killed-wall-street]].

**The coin game is the clearest statement of why sign matters more than average.** Small
frequent gains against rare large losses look profitable in any short sample and turn on a
one-point change in the probability of the loss. That is the ergodicity point of
[[peters-2011]] in a different form: what matters is growth along one path, not the
average over many.

## Links

- [[soros-2013]] — reflexivity in general; this essay applies it to volatility-driven
  leverage
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — the same story for a
  correlation model: a calm-period parameter becomes the market's price, then breaks
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why correlation estimated in normal
  times says nothing about joint crashes, the mathematics behind the risk-parity critique
- [[avellaneda-zhang-2010]] — how daily-rebalanced leveraged ETFs, including the short-VIX
  products discussed here, have path-dependent returns
- [[peters-2011]] — time-average growth and optimal leverage, the formal version of the
  coin game
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the evidence on what long-VIX hedges did for a 60/40 portfolio, 2006–2017: big help in 2008, a steady drag otherwise
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]] — why rule-based tail hedges bleed, and the case for trading them on price
