# Gamma Fragility

| | |
|---|---|
| **Authors** | Andrea Barbon (University of St. Gallen), Andrea Buraschi (Imperial College) |
| **Year** | 2021 (this version March 2021; first version January 2019) |
| **Type** | Working paper, SSRN 3725454, 48pp |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `barbon2021gamma` |
| **Status** | Reference: §II.B (the gamma-imbalance measure), §III (volatility, illiquidity, autocorrelation) and §IV (flash crashes) carry the results |

## What it is

An empirical paper on how option dealers' hedging feeds back into the stocks underneath.
When dealers are net short options (short gamma), delta-hedging makes them sell as prices
fall and buy as they rise, which amplifies moves. When they are net long (long gamma), the
hedging leans against moves.

- **The measure.** From Nasdaq ISE, GEMX and PHLX open/close volume by trader type
  (January 2010–May 2020, 10–20% of US equity option dollar volume), they rebuild
  broker-dealer inventories (following Ni, Pearson, Poteshman and White, 2018), weight
  each option by its gamma from OptionMetrics, and express the result as the dollar
  hedging trade a 1% move would force, divided by average daily volume. The panel covers
  about 2,700 stocks plus four indices. For indices, which the Nasdaq data do not cover,
  they assume dealers are long calls and short puts (customers run collars) and use call
  gamma minus put gamma.
- **A motivating fact.** Five-minute intraday return autocorrelation averages zero, but
  22% of stock-days have |ρ| > 0.2, and ρ is persistent. Something other than a random
  walk is going on within the day.
- **Volatility.** In panel regressions of absolute daily return on the previous day's gamma
  imbalance, controlling for implied volatility and fixed effects, the coefficient is
  negative with t-statistics between −5.07 and −12.08. One standard deviation of gamma
  imbalance moves the absolute daily return by 5–25bp, against an average of 180bp. For
  the four indices the effect is larger, over 20bp per standard deviation (about 20% of a
  standard deviation of the absolute return), with t-statistics of −3.3 to −4.4.
- **Illiquidity.** The effect is stronger for the less liquid half of stocks (Amihud
  measure): the interaction term has t = −7.61, about 9bp more volatility per standard
  deviation for illiquid names. This is what you would expect if the channel is dealers'
  trades moving prices.
- **Momentum and reversal.** The autocorrelation of 5- to 60-minute returns falls as gamma
  imbalance rises (negative imbalance, positive autocorrelation), by 1.5–2 percentage
  points per standard deviation. The effect is largest at 5 and 60 minutes, which the
  authors read as two hedging frequencies.
- **Flash crashes.** Using the drift-burst test of Christensen, Oomen and Renò (2018) on
  minute data, 1997–2015, they find 10,572 crashes (a drop of at least 1% within about 30
  minutes) across 1,849 stocks, roughly one per stock every three years. A one standard
  deviation lower gamma imbalance raises the chance of a crash by only about 5% relative
  to the base rate, but makes the drop 20–200bp deeper once one happens.
- **6 May 2010.** Market-wide gamma imbalance fell from about +$383m a week earlier to
  about −$431m on the day, −1.7 standard deviations. The authors say this does not show
  causation.
- **Not leveraged ETFs.** Leveraged-ETF rebalancing always pushes in the direction of the
  day's move and cannot produce reversals. Its aggregate size does not explain the days of
  high or low autocorrelation, while gamma imbalance does explain the cross-section.

## Why it's in the library

**It tests the "dealers are short gamma" story that runs through practitioner writing.**
Manager letters such as [[cole-2017-volatility-and-the-alchemy-of-risk]] argue that hedging
flows can turn a decline into a crash. This paper measures dealer positioning stock by
stock and finds the predicted signs: more volatility, more intraday momentum and deeper
flash crashes when dealers are short gamma, and stronger effects in illiquid names.

**It separates the size of the effect from its significance.** The t-statistics are large,
but the economic effects are modest: a few basis points of daily volatility per standard
deviation, and a 5% change in crash probability. Gamma positioning shapes how moves unfold
more than whether crashes happen. The deeper-drop result is the strongest for tail risk.

**The measure is a proxy, and the authors say so.** The Nasdaq exchanges cover only 10–20%
of volume, and the index measure rests on an assumption about who holds what. It is a
working paper, and the results are associations, not causal estimates.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the narrative version: hedging and
  volatility-targeting flows as a hidden short-volatility position
- [[avellaneda-zhang-2010]] — leveraged-ETF rebalancing, the competing flow explanation the
  paper rules out for intraday reversals
- [[merton-1976]] — jumps in price, what a flash crash looks like in a returns model
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — the index version: SPX dealer gamma inventory and option liquidity, 2004–2020
- [[squeezemetrics-2020-the-implied-order-book]] — the practitioner version: dealer gamma (GEX) read as a hidden order book
- [[tee-ting-2019-cross-section-of-mini-flash-crashes]] — another detector and cross-section of single-stock flash crashes
- [[carr-wu-2010-stock-options-and-credit-default-swaps]] — a different source of single-stock skew: the market pricing a jump to zero on default
- [[wystup-2008-vanna-volga-pricing-pros-and-cons]] — the FX version: a bank delta-hedging a large reverse barrier holds spot away from the barrier, then dumps the hedge once it breaks
