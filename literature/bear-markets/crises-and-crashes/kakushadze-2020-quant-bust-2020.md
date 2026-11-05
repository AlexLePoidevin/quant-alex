# Quant Bust 2020

| | |
|---|---|
| **Authors** | Zura Kakushadze (Quantigic Solutions; Free University of Tbilisi) |
| **Year** | 2020 (dated 7 April 2020) |
| **Type** | Essay with backtest appendix, 29pp. arXiv 2006.05632; published in *World Economics* 21(2), 183–217 (2020). Backtests on the 2,000 most liquid US stocks, March 2019 – March 2020 |
| **PDF** | `kakushadze-2020-quant-bust-2020.pdf` (arXiv version) |
| **BibTeX** | `kakushadze2020quantbust` |
| **Status** | Reference: the main text explains the mechanism; Appendix A and Table 1 give the illustrative backtests |

## What it is

A non-technical explanation, by a former statistical-arbitrage trader, of why
dollar-neutral quant equity strategies lost heavily in the COVID-19 selloff of
February–March 2020.

- **Why statistical arbitrage works in normal times.** Long-horizon investors buy and
  sell without caring about pennies, creating small mispricings; shorter-horizon
  strategies arbitrage them away (a "trickle-down" of profits). A mean-reversion
  statistical-arbitrage book buys stocks that have lagged their (sub-)industry and
  shorts the ones that have run ahead, betting the usual correlations will snap back.
- **Why it breaks in a selloff.** Long-only liquidations (index funds, ETFs, futures)
  dwarf the dollar-neutral books (equity market neutral hedge funds held about $76bn
  against roughly $12tn of US market value lost) and do not preserve industry
  correlations. With no snap-back, the strategy keeps adding to losing positions; then
  its own forced unwinding breaks the correlations further. It also loses on execution:
  it is normally a liquidity provider, but in a rout short sales become hard (stocks
  hard to borrow, no liquidity on the offer) while buy orders get run over.
- **When it works best.** A sideways market with moderate volatility. In straight-line
  rallies it lags: in 2019 the S&P 500 returned about 30%, an equity market neutral index
  −0.56%.
- **The analogy.** Mean-reversion statistical arbitrage is like selling deep
  out-of-the-money index puts: it is designed to lose in black-swan events, like August
  2007, and no machine learning model changes that.
- **The backtests (Appendix A).** Intraday-only versions of 1-, 5-, 10- and 20-day
  mean-reversion strategies over the year to 23 March 2020, $10m long and $10m short,
  with a liquidity-based cost model. They were roughly flat before costs in the 2019
  rally and fell about 10% (1-day) to 15% or more (longer horizons) of capital between
  20 February and 23 March 2020; with costs every close-to-close mean-reversion version
  has a negative annual return (about −21% to −28%). A one-day momentum strategy (the
  opposite bet) had P&L spikes during the selloff, even after costs, though it was flat
  to negative over the year. Strategies using fundamental industry classifications did better than ones
  using statistical clusters.

## Why it's in the library

**It explains a crisis mechanism that applies beyond 2020.** Any strategy that profits
from a stable correlation structure is short that structure's breakdown, and crowded
forced selling is what breaks it. The same story explains the August 2007 quant
meltdown.

**"Dollar-neutral" is not "market-neutral", and neither is "crash-neutral".** The paper
is blunt about this, and about the claim that machine learning can rescue a strategy
from its own design.

**Weigh it as an essay.** The backtests are deliberately simplified (intraday only, one
year, free Yahoo data) and illustrative; the author says so. Parts are opinion, including
pointed remarks about data science hype.

## Links

- [[lipton-lopez-de-prado-2020-three-quant-lessons-from-covid-19]] — another short essay on
  what COVID-19 taught quant investors
- [[racicot-theoret-2018-multi-moment-risk-hedging-strategies-and-the-business-cycle]] —
  evidence that equity market neutral hedge funds are not neutral in crises
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — the short-term
  reversal effect that mean-reversion statistical arbitrage harvests
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — strategies that earn steady returns
  by being implicitly short volatility
