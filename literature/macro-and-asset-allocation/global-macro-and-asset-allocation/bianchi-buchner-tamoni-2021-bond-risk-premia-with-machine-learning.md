# Bond Risk Premia with Machine Learning

| | |
|---|---|
| **Authors** | Daniele Bianchi (Queen Mary University of London); Matthias Büchner (Warwick Business School); Andrea Tamoni (Rutgers) |
| **Year** | 2021 (published as "Bond Risk Premiums with Machine Learning", *Review of Financial Studies* 34(2), 1046–1089, doi 10.1093/rfs/hhaa062); this copy is the working-paper draft of 6 April 2020 |
| **Type** | Paper, 86pp including appendices. US Treasury data August 1971 to December 2018; out-of-sample forecasts from January 1990 |
| **PDF** | Local copy only (working paper of a journal article, no open licence) |
| **BibTeX** | `bianchi2021bond` |
| **Status** | Reference: Tables 1–2 (out-of-sample R²), Table 5 (certainty-equivalent gains) and §7 (what the forecasts correlate with) carry the results |

## What it is

A horse race of machine-learning methods for forecasting one-year excess returns on US
Treasury bonds of 2 to 10 years' maturity, run in the two standard settings of the bond
predictability literature.

- **Two settings.** *Yields only*, as in Cochrane and Piazzesi (2005): forward rates from
  the Liu–Wu zero-coupon curve predict next year's excess return. *Yields plus macro*, as
  in Ludvigson and Ng (2009): 128 monthly macroeconomic and financial series (the FRED-MD
  panel) are added.
- **Methods compared.** Principal components and partial least squares; ridge, lasso and
  elastic net; gradient-boosted trees, random forests and extremely randomised trees;
  feed-forward neural networks of one to three hidden layers. Forecasts are made each
  month on an expanding window, with the last 15% of the in-sample data used to tune
  hyperparameters, and are scored by out-of-sample R² against the historical-mean
  forecast (the expectations-hypothesis benchmark).
- **Yields only (Table 1).** Linear compression does badly out of sample: five principal
  components give R² from −55% (2-year bond) to −3% (10-year). Trees and small networks
  do well: a one-layer, three-node network reaches 12.7% (2-year) to 26.4% (10-year), and
  extremely randomised trees 3.9% to 24.6%. That non-linear methods help even with only
  a handful of yield inputs is one of the paper's points: the gain is not just a
  big-data effect.
- **Yields plus macro (Table 2).** The best model is a "group-ensembled" network: one
  small network per economic category of macro variables (output, labour, housing,
  orders and inventories, money and credit, financial, prices, stock market), combined
  at the output with a separate small network on forward rates. Its R² runs from 20.0%
  (2-year) to 36.3% (10-year), about 10 percentage points above the best yields-only
  network. Because this design switches off interactions *across* categories and still
  matches deep unrestricted networks (a three-layer network reaches 24.8% to 33.7%), the
  authors conclude that the useful non-linearity is *within* a category of macro data.
  Trees also improve with macro data (random forest 20.0% to 26.7%).
- **Which macro data matter.** Stock-market and labour-market variables matter most for
  short maturities; output, income, orders and inventories for long maturities.
- **Economic value (Table 5).** A mean-variance or power-utility investor (risk aversion
  5) who allocates between the bond and cash using the forecasts earns certainty-
  equivalent gains over the expectations-hypothesis investor that are significantly
  positive for trees and networks in almost every case. With macro data, networks beat
  trees by about 0.5 to 1 percentage point a year.
- **What the forecasts track (§7).** The network's expected bond return is
  countercyclical: its correlation with industrial production is −12.4% with yields only
  and −24.6% with macro data. It loads on habit-style risk aversion and on uncertainty
  about GDP growth (not inflation uncertainty), with an R² of about 25%, and only weakly
  on bond volatility.

## Why it's in the library

**It is the bond-market counterpart of Gu, Kelly and Xiu's equity work.** The same
research design (train, validate, test on a rolling clock, compare many learners) applied
to Treasury returns. The answer is the same in outline: non-linear methods find
predictability that linear compression misses, and the gain survives a portfolio test.

**It also shows how fragile the evidence is to set up.** The forecast target is a
one-year return sampled monthly, so consecutive observations overlap by eleven months
and out-of-sample R² values are noisy. Many architectures are reported side by side
(Tables 1–2 list over 20 networks), and the headline group-ensembled network is the best
of that set. The authors partly address this: in their model-averaging check, a network
chosen each month by validation error performs about as well as the best fixed one, and
the chosen design is selected about half the time. The out-of-sample period is
"pseudo" out-of-sample, as the authors say, because the whole sample was available when
the designs were chosen.

**The architecture result is useful in its own right.** Building the network around
economic groups of inputs, rather than letting one large network see everything, did as
well as the deepest network and is easier to interpret. That is a transferable design
idea for any forecasting problem with many correlated macro inputs.

## Links

- [[gu-kelly-xiu-2021]] — the same machine-learning research design applied to equity factor models
- [[kelly-pruitt-su-2019]] — another way to let a model learn the mapping from characteristics to expected returns
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]] — why trees are a strong baseline on tabular inputs like these
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same comparison of trees and networks on general tabular data
