# What Predicts US Recessions?

| | |
|---|---|
| **Authors** | Weiling Liu (Harvard Business School), Emanuel Moench (Deutsche Bundesbank) |
| **Year** | 2016 |
| **Type** | Journal article, *International Journal of Forecasting* 32(4), 1138–1150. Monthly US data, January 1959 – December 2011 |
| **PDF** | Local copy only (Elsevier) |
| **BibTeX** | `liu2016recessions` |
| **Status** | Reference: §2.2 (the ROC method) and §4 (in- and out-of-sample results) carry the paper |

## What it is

A horse race between the Treasury term spread and a long list of leading indicators, at
predicting NBER recessions 3 to 24 months ahead.

- **Setup.** Probit models map indicators to a recession probability. The benchmark is
  the 10-year minus 3-month Treasury spread, alone and with its six-month lag. About 35
  candidates are then added one at a time: stock returns, interest-rate spreads over fed
  funds, the Conference Board leading-index components, credit spreads, building permits,
  new orders, payrolls and broker-dealer margin debt.
- **Scoring.** Each model is scored by the area under the ROC curve (AUROC), which counts
  true against false positives across every probability cutoff, so no single recession
  threshold has to be chosen. 0.5 is a coin toss, 1 is perfect. Confidence bands come from
  a block bootstrap with eight-year blocks.
- **The spread on its own** is a mediocre short-horizon predictor (AUROC 0.67 at three
  months) and peaks at one year ahead (0.87).
- **Short horizons.** Adding the lagged spread lifts three-month AUROC to 0.86. Adding the
  S&P 500's one-year return on top lifts it to a near-perfect 0.96 in sample. Margin debt
  and payrolls give about 0.94.
- **One year ahead,** the spread is hard to beat. Shorter rate spreads over fed funds help
  a little, but not significantly.
- **Longer horizons.** At 18 and 24 months, broker-dealer margin debt and new orders of
  non-defence capital goods add significant information. Margin debt lifts 18-month AUROC
  from 0.81 to 0.88.
- **Out of sample** (fit on 1959–1985, tested on 1985–2011, three recessions), the
  short-horizon gains hold: S&P returns, initial jobless claims and payrolls again help at
  three months. The best extra variables at six months change, which the authors read as
  possible drift in what drives the cycle.

## Why it's in the library

**It is the reference test of the yield curve as a recession signal.** The term spread's
reputation holds best around a one-year horizon. Nearer in, recent equity returns and
labour data do much more. Further out, leverage in the financial system (margin debt)
matters.

**AUROC is the right yardstick for a regime signal.** Recessions are rare, so accuracy at
one cutoff is misleading. The ROC approach shows the whole trade-off between missed
recessions and false alarms, and the bootstrap shows how wide the uncertainty is.

**Small samples.** Seven recessions in sample and three out of sample is very little
data. Near-perfect AUROCs at three months partly reflect that the S&P 500 is itself
falling as a recession starts. Treat the variable rankings as suggestive.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bull and bear states
  in stock returns, the market-side counterpart of the business-cycle dating used here
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — trend
  rules derived from a two-state bull/bear model
- [[azqueta-gavaldon-et-al-2020-nowcasting-business-cycle-turning-points]] — recessions nowcast from stock-return networks, with a sobering out-of-sample test
