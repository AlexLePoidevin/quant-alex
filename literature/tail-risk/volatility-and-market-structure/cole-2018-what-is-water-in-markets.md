# What is Water in Markets? Volatility and the Fragility of the Medium

| | |
|---|---|
| **Authors** | Christopher Cole (Artemis Capital Management) |
| **Year** | 2018 (Letter to Investors, July 2018) |
| **Type** | Investor letter / research essay, 11pp |
| **PDF** | Not hosted in this repository (marked "Confidential to Artemis investors" and not for public distribution) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22What+is+Water+in+Markets%3F+Volatility+and+the+Fragility+of+the+Medium%22+Cole) for the title and authors |
| **BibTeX** | `cole2018water` |
| **Status** | Reference: the passive-investing simulation (p. 3) and the February 2018 liquidity section (pp. 4–5) carry the content; the rest is macro forecasting |

## What it is

Cole's follow-up to "Volatility and the Alchemy of Risk", written after the February 2018
volatility spike. It takes its title from David Foster Wallace's fish who don't know what
water is. In markets the "water" is **liquidity**: the bids and offers everyone takes for
granted. True volatility, Cole argues, is the moment that medium fails.

- **Passive investing as a liquidity-momentum trade.** Cole contrasts two views of value:
  value intrinsic to the asset (Graham and Dodd), and value as whatever the market will
  pay. He says the second now dominates, through passive and factor investing. He builds
  a toy simulation, crediting the idea to Michael Green:
  - 25,000 days of geometric Brownian motion with a drift from constant passive inflows.
  - Active traders push the price back towards equilibrium when it strays too far.
  - As the passive share rises, the excess return available to active traders peaks at
    42% passive, then collapses.
  - Above about 60% passive the simulated market becomes unstable, with wild trends and
    high volatility.
- **February 2018 was a liquidity crisis, not a volatility event.**
  - A routine fall in stocks forced short-VIX exchange-traded products to buy back vega,
    more than the market could supply. VIX had its second-largest rise (+177%) and largest
    five-day fall (−43%) in its 28 years, and the "XIV" product was wiped out.
  - At-the-money implied volatility rose more in January (+3.5%) than in February (+3%).
    The VIX spike came from demand for far out-of-the-money puts, which rose from about
    10% of the VIX's value to about 35%.
  - Top-of-book depth in S&P 500 E-mini futures fell about 95% from late 2017 to
    February–March 2018 (NANEX data). SPY's average spread widened from 1 cent to over
    2 cents. Some SPX option spreads went from 5 cents to over $3.
  - Cole's conclusion: the short-VIX products were the smallest part of a roughly $2tn
    short-volatility trade, and the systemic risk is the larger implicit trade's effect on
    market liquidity.
- **Flows over fundamentals.**
  - Record buybacks after the 2017 tax reform act as a price-insensitive buyer that
    suppresses volatility. The collapses in volatility after the spikes of
    August–September 2015, June 2016 and February 2018 each coincided with buybacks
    resuming.
  - Quantitative tightening, a wave of debt refinancing and baby-boomer retirement
    withdrawals will drain liquidity. Cole forecasts a crisis between 2019 and 2022.

## Why it's in the library

**Its account of February 2018 is the most useful part.** It separates a rise in implied
volatility across the board from a scramble for crash protection when liquidity is gone.
VIX can spike on the second even when at-the-money volatility barely moves, because VIX
weights far out-of-the-money puts. The order-book and spread figures show that liquidity
can vanish in a selloff that is not a fundamental crash.

**The passive-investing simulation is a toy.** It has one mechanism, constant proportions
and no calibration, so the 42% and 60% thresholds are features of the model, not estimates
for real markets. The idea that passive flows can crowd out price discovery is a serious
one, but this simulation does not test it.

**The macro forecast half came true.** A crash did come in March 2020, inside the
2019–2022 window, but its cause was a pandemic, not the debt-refinancing and quantitative
tightening "drought" the letter describes. 2022's bear market followed tightening, but
was an orderly decline rather than a liquidity crisis. Judge the letter on its
mechanisms, not its timing.

**It is a letter from a long-volatility fund to its own investors.** It argues the case
for holding tail exposure, so read its framing as the manager's view.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the essay this letter follows up:
  the hidden short-volatility trade and the 1987 template
- [[soros-2013]] — reflexivity: prices shaping the fundamentals and flows they are meant
  to reflect
- [[huang-rise-of-passive]] — the rise of passive investing and what it does to active
  managers' opportunity
- [[avellaneda-zhang-2010]] — leveraged ETF rebalancing, the mechanism behind the
  short-VIX product squeeze
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] —
  the VXTH tail-hedge index, which had no protection on going into February 2018
- [[ambrus-capital-2022-volatility-and-the-changing-market-structure]] — the structural fragility argument updated for 2022: dealers, 0DTE, passive flows
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — the mechanics of the VIX and its settlement, with February 2018 as the motivating case
