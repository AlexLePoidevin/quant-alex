# Deep Asset Allocation for Trend Following Investing

| | |
|---|---|
| **Authors** | Saejoon Kim, Hyuksoo Kim (Sogang University) |
| **Year** | 2021 (published online 5 April 2021; issue 2022) |
| **Type** | Journal article, *Journal of Experimental & Theoretical Artificial Intelligence* 34(4), 599–619. Doi 10.1080/0952813X.2021.1908429. Stocks in the S&P 500 (1997–2018), FTSE 100 (2001–2018) and KOSPI 200 (2000–2019), monthly rebalancing |
| **PDF** | Local copy only (Taylor & Francis; publisher copyright) |
| **BibTeX** | `kim2022deepallocation` |
| **Status** | Reference: Tables 1–3 (weighting schemes) and Tables 4–9 (machine-learning weights) |

## What it is

A long-only stock trend strategy (hold every stock with a positive past-year return, rebalance
monthly) where the question is only how to weight the stocks held.

- **Weighting by past return beats equal weighting.** Weighting each held stock by its
  past-year return (RW) gave a higher annual return than equal weight (EW), inverse
  volatility (EVW) or risk parity (RP) in all three markets, net of an assumed 0.1% one-way
  cost at 75% turnover. On the S&P 500, RW returned 11.8% a year against 9.7% for EW and 3.5%
  for the index, but its Sharpe ratio was 0.66 against 0.68 for EW and 0.73 for RP, because
  its volatility was higher. In the FTSE 100 and KOSPI 200 it also had the best Sharpe ratio.
- **The motivating thought experiment.** Weighting by each stock's actual next-month return
  (not knowable in advance) produces enormous returns. The authors use this to argue that
  better return forecasts should improve the weights.
- **Forecasting the weights with machine learning.** Each stock's next-month return is
  predicted from 63 lagged monthly returns covering the past year, using support vector
  regression on the raw inputs, on features from a stacked autoencoder, or on features from a
  marginalised denoising stacked autoencoder (mdSAE). On the S&P 500, the mdSAE-weighted
  portfolio returned 13.9% a year with a Sharpe ratio of 0.83, against 11.8% and 0.66 for
  past-return weights. Its maximum drawdown was 37% against 45% for equal weight.

## Why it's in the library

It is a useful example of how a modest result (weight held stocks by their trend strength)
gets presented as a deep-learning result, and of the checks such a paper needs.

- **Possible look-ahead in the training set.** As written, the training pairs for the
  prediction made at day i\* use inputs at i\* − 21j with targets 21 days later, for
  j = 0 to 99. At j = 0 the target is the very return being predicted. If this is not a
  typo, every forecast was trained on its own answer, and the mdSAE gains are not credible.
- **The universe.** "Securities in the S&P 500" is not said to be point-in-time, so the
  sample is probably today's survivors, which flatters any long-only stock strategy.
- **Model selection.** Network shapes, activation functions and noise levels were chosen per
  market, and the gains over the simple past-return weighting are small (1.4–2.1 points a
  year), well within what such choices can produce.

The part worth keeping is the first: within a trend-following stock book, tilting towards the
strongest trends raised returns before any machine learning.

## Links

- [[beaudan-he-2019-logistic-regression-for-momentum-based-trading-strategies]] — another machine-learning layer on a momentum rule, for a single index
- [[asness-et-al-2014-fact-fiction-and-momentum-investing]] — the evidence on stock momentum that this builds on
- [[gu-kelly-xiu-2021]] — machine learning for stock returns with a careful out-of-sample design
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — why choices fitted on the same backtest overstate results
