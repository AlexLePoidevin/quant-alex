# VPIN (Volume-Synchronized Probability of Informed Trading)

| | |
|---|---|
| **Authors** | Wikipedia contributors (revision 557342271) |
| **Year** | 2013 |
| **Type** | Encyclopedia article, printed to PDF (10pp) |
| **PDF** | `wikipedia-2013-vpin-flow-toxicity.pdf` (CC BY-SA 3.0, per the licence page in the printout) |
| **BibTeX** | `wikipedia2013vpin` |
| **Status** | Reference: an overview of the PIN/VPIN family; go to the papers for anything quantitative |

## What it is

A Wikipedia printout that surveys the probability-of-informed-trading models, from the 1996
PIN model to the high-frequency VPIN measure, and what VPIN has been proposed for.

- **PIN (1996).** In Easley, Kiefer, O'Hara and Paperman's sequential trade model, informed
  traders arrive at rate μ when there is news and uninformed traders at rate ε. A market
  maker sets the bid and ask so that what it loses to informed traders is paid for by what
  it earns from uninformed ones. The spread is set by the probability that a trade is
  informed. The parameters are fitted by maximum likelihood to a mixture of three Poisson
  distributions of buy and sell volume. A later version (Easley, Engle, O'Hara and Wu,
  2008) lets the arrival rates vary over time.
- **VPIN (2010).** Easley, López de Prado and O'Hara sample in volume time: buckets that
  each contain the same traded volume. They split each bucket's volume into buys and sells
  with Bulk Volume Classification (the share of buys comes from the standardised price
  change, through the normal CDF), not the tick rule. VPIN is the average absolute
  buy–sell imbalance divided by bucket volume. It needs only bars, not tick data.
- **Uses claimed.** Warning of liquidity crashes (the 6 May 2010 flash crash; a Lawrence
  Berkeley National Laboratory study called it "the strongest early warning signal known
  to us at this time"). Forecasting volatility caused by toxic flow, not volatility in
  general. A proposed futures contract on VPIN so market makers can hedge adverse
  selection. A "yellow flag" that slows matching on the side being hit instead of halting
  the market. An optimal-execution-horizon model built on order imbalance.
- **Implementation cautions.** Use bars and bulk classification, not tick data and the tick
  rule. Use a conditional-probability approach, not plain regression, to relate VPIN to
  later volatility. The article says other implementations "will yield results
  inconsistent with this theory".

## Why it's in the library

**It is a compact map of where VPIN comes from.** The flash-crash paper
([[easley-et-al-2011-microstructure-of-the-flash-crash]]) assumes the reader knows PIN and
volume buckets. This article supplies that background in a few pages.

**Volume time and bulk classification are useful ideas on their own.** Sampling by traded
volume rather than by the clock makes returns closer to normal and lines the data up with
activity. Bulk classification works from bars alone. Both carry over to any work on
intraday data.

**It is not a neutral source.** Its contributor list includes accounts named "Berklabsci" and
"Cornellian1", which suggests links to the Berkeley lab and to Cornell, where two of the
authors work. The article reports the case for VPIN and none of the published criticism, notably Andersen and Bondarenko (2014), who found that
VPIN's forecasting power largely reflects trading volume and the trade-classification
choice. The "cautions" section partly reads as a defence against that criticism. Use the
article for definitions, not for evidence.

## Links

- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — the paper that applies VPIN to
  6 May 2010, with the actual numbers
- [[merton-1976]] — jumps in price, what a liquidity crash looks like in a returns model
