# Nowcasting Business Cycle Turning Points with Stock Networks and Machine Learning

| | |
|---|---|
| **Authors** | Andres Azqueta-Gavaldon, Dominik Hirschbühl, Luca Onorante, Lorena Saiz (European Central Bank) |
| **Year** | 2020 (November) |
| **Type** | Working paper, ECB Working Paper Series No. 2494, 54pp. Daily returns of S&P 500 stocks 1980–2019, quarterly US GDP regimes 1982–2019 |
| **PDF** | Local copy only (© European Central Bank, all rights reserved) |
| **BibTeX** | `azqueta2020nowcasting` |
| **Status** | Reference: §3 (network construction and feature selection), §4.2 (out-of-sample exercise) and Table 2 (scores) carry the result |

## What it is

An attempt to read the state of the US economy from how shocks spread between stocks.
The idea is that in expansions shocks to firms are mostly idiosyncratic. In contractions
they spread, so the network of stocks becomes more connected.

- **Building the network.** Every quarter, for each pair of S&P 500 stocks, the authors
  test whether one stock's daily returns over the past 12 months Granger-cause the other's
  (HAC errors, 1% level). Significant pairs become directed links. Centrality measures
  (degree, PageRank and others) for each firm and for the whole network give a "fat" data
  set of about 5,000 quarterly series.
- **Choosing features.** Recursive feature elimination keeps the few series that best
  track GDP regimes. Three classifiers then compete: support vector machines, naive Bayes
  and logistic regression. Two targets are used:
  - **two states:** negative growth versus not;
  - **three states:** negative, low and high growth (above 3% annualised).
- **In-sample, it looks excellent.** With features chosen on the whole 1982–2019 sample,
  the network features of manufacturing, transport and financial firms, insurers above all,
  pick out negative-growth quarters almost perfectly. The SVM scores an AUROC of 1.00.
- **Out of sample, much less so.** With features chosen only on data up to 2006 and
  forecasts made from 2007 to 2019:
  - **Two states:** AUROC is 0.62–0.76 and accuracy 0.74–0.81 across the classifiers. The
    binary model misses the start of the Great Recession.
  - **Three states:** the model catches the 2008 turning point. It also gives many false
    negative-growth signals in quarters of weak but positive growth.
  - **Which classifier wins:** logistic regression and naive Bayes beat the SVM, which
    overfits in sample.

## Why it's in the library

**It is a granular alternative to aggregate indicators.** Most recession models use
spreads, surveys or macro aggregates, which average away which firms get hit first. Here
the signal is which firms become central in the network of return spillovers. That also
tells a story about where a downturn starts.

**It shows the in-sample/out-of-sample gap plainly.** Once feature selection is restricted
to the data available at the time, near-perfect fits become moderate ones. That makes the
paper a clean example of how much feature selection on the full sample flatters a
nowcasting model.

**Limits.**
- **Accuracy needs a baseline.** Only about 7 of the 49 out-of-sample quarters had
  negative growth. A constant "no recession" call would score an accuracy of about 0.86,
  better than any of the models. The AUROC of 0.62–0.76 is the fairer measure, and it is
  modest.
- **Look-ahead in the universe.** The universe is the S&P 500 as of the third quarter of
  2018, applied back to 1980.
- **One recession.** The out-of-sample period contains a single recession.

## Links

- [[liu-moench-2016-what-predicts-us-recessions]] — the standard benchmark: the term spread and other leading indicators scored by ROC curves
- [[kinlaw-kritzman-turkington-2021-a-new-index-of-the-business-cycle]] — a recession index built from how unusual current conditions look
- [[heckens-guhr-2021-long-term-precursors-for-financial-crisis-in-market-correlation-structures]] — crisis precursors read from the structure of stock correlations
- [[mantegna-1999]] — the original network view of stock returns, from correlations
