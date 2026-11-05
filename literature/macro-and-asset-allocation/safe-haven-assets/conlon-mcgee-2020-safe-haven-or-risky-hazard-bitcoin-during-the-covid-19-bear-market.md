# Safe Haven or Risky Hazard? Bitcoin during the Covid-19 Bear Market

| | |
|---|---|
| **Authors** | Thomas Conlon, Richard McGee (Smurfit Graduate School of Business, University College Dublin) |
| **Year** | 2020 |
| **Type** | Journal article, *Finance Research Letters* 35, 101607, 5pp. Data to 20 March 2020 |
| **PDF** | `conlon-mcgee-2020-safe-haven-or-risky-hazard-bitcoin-during-the-covid-19-bear-market.pdf` (open access under CC BY 4.0, as stated on the article) |
| **BibTeX** | `conlon2020bitcoin` |
| **Status** | Reference: Table 1 and Fig. 2 carry the results |

## What it is

A short test of whether Bitcoin protected an S&P 500 investor in the first real crash since
it began trading: the COVID-19 bear market that started after the S&P 500 peaked on
13 February 2020.

- **Data and periods.** Daily S&P 500 prices and CoinMetrics' Bitcoin reference rate, over
  three windows: July 2010 to March 2020, April 2016 to March 2020 (when the Bitcoin market
  is considered more efficient), and the year to 20 March 2020.
- **Method.** Downside risk is measured with four-moment "modified" value at risk and
  conditional value at risk (CVaR, the average loss beyond the VaR). These use the
  Cornish–Fisher expansion to adjust the normal quantile for skewness and kurtosis. The test
  compares a portfolio with some Bitcoin against the S&P 500 alone.
- **What happened.** From the February peak, Bitcoin fell with the S&P 500 and by more.
- **Downside risk.** In the year to March 2020, putting 10% in Bitcoin raised the 1% VaR by
  13.6% (from 10.34% to 11.75%) and the 1% CVaR by 15.3% (from 16.18% to 18.65%). The same
  holds in the longer windows. The increase grows with the Bitcoin weight; above a 28%
  weight, downside risk is at least 50% higher than for the S&P 500 alone. Bitcoin's worst
  day in the sample was −66.5%, against −12.8% for the S&P 500.
- **Conclusion.** Bitcoin was not a safe haven in this crash; any allocation increased the
  downside risk of an equity portfolio.

## Why it's in the library

**It tests "digital gold" in the one setting that matters.** Earlier claims that Bitcoin was a
haven came from periods without a severe equity crash. In the first one it fell with
stocks, and by more.

**It measures a haven by what it does to portfolio tail risk.** CVaR of the combined
portfolio is the right question for a hedge, rather than an average correlation.

**It is one five-week episode.** The data stop on 20 March 2020, before the rebound, and the
conclusion rests on a single crash. The Cornish–Fisher expansion is unreliable at kurtosis as
high as that reported here (about 20 to 38), so the exact VaR figures should not be leaned on. The
"cumulative return" rows appear to be sums of log returns: Bitcoin's 1,124% is described in
the text as wealth rising "over 11 times", but read as a log return it is a far larger
multiple.

## Links

- [[baur-dimpfl-2022-a-safe-haven-index]] — Bitcoin's beta to a basket of established safe
  havens is insignificant, with an R² of zero
- [[baur-trench-2022-not-all-gold-shines-in-crisis-times]] — gold rose in the same crash while
  gold-mining shares fell with the market
- [[rockafellar-uryasev-2000]] — CVaR, the tail-loss measure used here
- [[gormsen-koijen-2020-coronavirus-impact-on-stock-prices-and-growth-expectations]] — what
  the COVID crash priced in, read from dividend futures
- [[maheu-mccurdy-song-2021-bull-and-bear-markets-during-the-covid-19-pandemic]] — the 2020
  bear market and bear rally dated with a regime model
