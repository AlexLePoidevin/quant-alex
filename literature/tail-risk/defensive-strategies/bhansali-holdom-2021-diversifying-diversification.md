# Diversifying Diversification: Downside Risk Management with Portfolios of Insurance Securities

| | |
|---|---|
| **Authors** | Vineer Bhansali (founder and CIO), Jeremie Holdom (LongTail Alpha) |
| **Year** | 2021. The copy is the version dated 25 November 2020, submitted to the journal; published in *The Journal of Portfolio Management* 47(6), 101–113 |
| **Type** | Manager research paper, 19pp. Data January 1971 to September 2020 |
| **PDF** | Not hosted in this repository (manager working version, no open licence) |
| **Find it** | [doi.org/10.3905/jpm.2021.1.229](https://doi.org/10.3905/jpm.2021.1.229) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Diversifying+Diversification%3A+Downside+Risk+Management+with+Portfolios+of+Insurance+Securities%22+Bhansali) |
| **BibTeX** | `bhansali2021diversifying` |
| **Status** | Reference: Exhibit 1 (each hedge on its own), Exhibits 4–12 (in-sample and out-of-sample drawdown periods) and Exhibits 13 and 16 (full sample and weight stability) carry the results |

## What it is

A test of whether crash protection should itself be a diversified portfolio rather than one
favourite hedge. Written by a manager that runs tail-hedging strategies.

- **Six "insurance securities".** The Swiss franc and the yen (spot), spot gold, US long bond
  futures (modelled from yields before 1977), a simple trend programme, and a put ladder on
  the S&P 500. The trend programme is long anything above its 252-day moving average and
  short anything below, across the S&P 500, the two currencies, gold, wheat, soy, sugar and
  bonds, weighted by inverse volatility. The put ladder buys a one-year put struck 20% out of
  the money every month on 1/12 of the notional. Before 1996 option prices are modelled from
  realised volatility plus an average premium.
- **On their own, 1971–2020.** Annual growth was 7.4% for the S&P 500 (worst drawdown
  −56.8%), 3.2% for the franc, 2.5% for the yen, 8.2% for gold (worst drawdown −70.3%), 3.3%
  for bond futures and 9.5% for trend (worst drawdown −35.0%, Sharpe 0.80). The put ladder
  lost 1.4% a year, with a correlation of −0.80 to the S&P 500 and the most convex payoff in a
  sell-off.
- **The test.** S&P 500 drawdowns of more than 15% are split at random into six in-sample
  episodes (1980, 1981–82, 1987–89, 2000–06, 2008–12, 2012) and five out-of-sample ones
  (1973–79, 1990, 1998, 2018, 2020). Two insurance baskets are fitted in-sample: equal risk
  contributions (assuming zero correlations), and the risk contributions that maximise the
  Sharpe ratio of stocks plus the basket. Everything is scaled to 15% volatility, so the
  baskets use leverage.
- **What the optimiser picked.** Mostly bonds (weight 0.91) and trend (0.62), some gold
  (0.14), and no puts at all, because mean-variance ignores the skew the puts are bought
  for. The equal-risk basket held 0.80 notional in puts.
- **Out of sample.** Over the five out-of-sample drawdowns the S&P 500 returned −0.2% a year
  (Sharpe −0.01). The equal-risk basket earned a Sharpe ratio of 1.19 and the optimised one
  1.01. Combined with stocks, the average drawdown fell from −16.0% to −7.3% (equal-risk) and
  −9.0% (optimised). Bond futures earned about nothing out of sample; trend, gold, the yen
  and the franc did the work.
- **Full sample.** Stocks alone had a Sharpe ratio of 0.55; stocks with the equal-risk basket
  0.93, and with the optimised basket 0.97. The optimised weights swing between samples:
  bonds 0.73 in-sample and 0.00 out-of-sample, puts 0.00 and 1.01. The equal-risk weights
  barely move.
- **Conclusion.** Equal-risk weighting of several hedges does about as well as optimising
  them, and is more reliable, because it needs no forecast of which hedge will work next
  time.

## Why it's in the library

**It argues that crash protection should be diversified too.** The hedge the optimiser
liked best, long bonds, earned nothing out of sample, and the put ladder cost money every
year. A basket of hedges with different reasons for working was more reliable than betting
on whichever one worked last time.

**It shows how the optimiser shapes the hedge.** Mean-variance discards the put because it
only sees mean and variance, not the convex payoff. Whatever objective is used to size
hedges decides which hedges survive.

**Several choices flatter the results.** The paper comes from a manager that sells tail
hedging. Currencies are spot prices only, so holding the low-yielding franc and yen ignores
their interest-rate cost. There are no transaction costs, the baskets are levered with no
stated funding cost, and pre-1996 option prices are modelled. "Out of sample" means five
drawdown episodes, and the full-sample figures reuse the in-sample periods. Exhibit 13's
S&P 500 figures (6.3% growth, 12.6% volatility) do not match Exhibit 1 (7.4%, 15–18%), and
the difference is not explained.

## Links

- [[harvey-et-al-2019-the-best-of-strategies-for-the-worst-of-times]] — the same set of crash
  hedges (puts, bonds, gold, trend) scored over the drawdowns of 1985–2018
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — puts against
  trend as crash protection, decade by decade
- [[mcquinn-thapar-villalon-2021-portfolio-protection-its-a-long-term-story]] — why puts help
  in fast crashes but not in long bad periods
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — evidence that trend
  following does best in the worst equity and bond markets
- [[chang-holdom-bhansali-2021-tail-risk-hedging-performance-measuring-what-counts]] — the
  same firm on how to measure whether a tail hedge is working
- [[bhansali-2018-right-tail-hedging-managing-risk-when-markets-melt-up]] — the same author on
  the opposite risk: being under-invested in a rally
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — another
  crash hedge, long VIX, and its carrying cost
