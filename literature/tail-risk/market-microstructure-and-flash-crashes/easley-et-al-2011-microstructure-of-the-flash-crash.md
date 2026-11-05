# The Microstructure of the "Flash Crash": Flow Toxicity, Liquidity Crashes, and the Probability of Informed Trading

| | |
|---|---|
| **Authors** | David Easley, Marcos López de Prado, Maureen O'Hara |
| **Year** | 2011 |
| **Type** | Journal article, *The Journal of Portfolio Management* 37(2), Winter 2011, pp. 118–128 |
| **PDF** | Local copy only (publisher download, © Pageant Media) |
| **BibTeX** | `easley2011flash` |
| **Status** | Reference: the whole article is short; Exhibits 5–8 carry the evidence |

## What it is

The authors argue that the 6 May 2010 flash crash was a liquidity event that had been building
for hours, and that a measure of order-flow "toxicity" called VPIN gave warning of it.

- **The event.** E-mini S&P 500 futures fell 5% between 2:30 and 2:45 p.m. (EDT), on top of
  a 2.97% drop earlier in the day, and the Dow had its largest one-day point fall (998.5).
  More than 1.1 million June E-mini contracts traded between 2:30 and 3:00 p.m. Volume was
  high but liquidity was not.
- **The market-structure argument.** High-frequency firms had become the main liquidity
  providers. They hold tiny inventories, turn them over several times a day and run on thin
  capital, so they are very sensitive to intraday losses. Three forces make sudden
  illiquidity more likely: liquidity provision concentrated in a few firms, less retail
  flow (so the flow market makers see is more informed), and providers who leave quickly.
- **Toxicity.** Flow is toxic when market makers are trading against better-informed
  counterparties and so lose on average. When toxicity rises, they cut their positions and
  leave. Extreme toxicity turns liquidity providers into liquidity consumers.
- **VPIN.** Measured in volume time (buckets of equal traded volume, here 1/50 of average
  daily volume), VPIN is average order imbalance divided by total volume: an estimate of the
  share of volume coming from informed traders. The authors fit a lognormal to its
  distribution from January 2008 to October 2010 and report CDF(VPIN), how unusual a reading is.
- **The evidence on 6 May.** CDF(VPIN) was unusually high for the week before. On the day
  it passed the 90th percentile by 11:55 a.m. and the 95th by 1:08 p.m. At 2:30 p.m. VPIN
  reached the highest level in the contract's history, and the crash began at 2:32 p.m.
  They estimate nearly 80% of E-mini flow was toxic during the volume burst.
- **VPIN versus VIX.** The VIX rose from 25.92 at the open to 40.69 at 3:28 p.m., far from
  its 89.53 peak of October 2008. It only reached comparable extremes after the low, so it
  responded to the crash rather than anticipating it.
- **VPIN and later volatility.** Over the full sample, high VPIN readings shift probability
  towards larger absolute returns in the next volume bucket. The correlation between VPIN
  and the following absolute price change is 0.1596. Read the other way, VPIN was above 0.41
  before 80% of the moves between 1.75% and 2%.
- **Proposal.** A futures contract on VPIN, so market makers could hedge the risk of being
  adversely selected instead of dumping inventory. Also: use it as a benchmark for brokers
  and as a warning signal for regulators.

## Why it's in the library

**It gives a mechanism for a crash without news.** A crash can come from inside the market:
liquidity providers who are losing money to informed flow withdraw, and their withdrawal
makes the remaining flow even more one-sided. This is the microstructure version of the
feedback loops in [[cole-2017-volatility-and-the-alchemy-of-risk]]. There, leverage sized
by volatility is the amplifier. Here, it is market makers with thin capital.

**It shows that volume is not liquidity.** May 6 was the E-mini's third-highest volume day
and one of its least liquid. Any risk model that treats high volume as a sign of a deep
market needs this counterexample.

**It is a claim by the measure's inventors, and it has been disputed.** VPIN is a Tudor
trademark, and one author worked at Tudor. The evidence is one event plus in-sample
conditional tables, with no out-of-sample test of false alarms. Andersen and Bondarenko
(2014, *Journal of Financial Markets*) argue that VPIN's apparent warning comes mostly from
its link to trading volume and from how trades are classified, and that it did not peak
before the crash under other specifications. Read this paper for the mechanism. Treat the
early-warning claim as unproven.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the macro version of the same loop:
  strategies that are short volatility sell into a falling market and deepen the fall
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — another case where a market's
  plumbing, not news, set the size of the loss
- [[merton-1976]] — prices that jump, the modelling counterpart of a liquidity crash
- [[poitras-2012-what-happened-may-6-2010-anatomy-of-the-flash-crash]] — the futures-arbitrage account of the same day, compared with 1987
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — how the crash spread across the Dow stocks, modelled as self-exciting trades
