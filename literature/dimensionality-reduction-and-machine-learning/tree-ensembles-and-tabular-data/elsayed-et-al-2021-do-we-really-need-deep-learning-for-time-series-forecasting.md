# Do We Really Need Deep Learning Models for Time Series Forecasting?

| | |
|---|---|
| **Authors** | Shereen Elsayed, Daniela Thyssens (equal contribution), Ahmed Rashed, Hadi Samer Jomaa, Lars Schmidt-Thieme (University of Hildesheim) |
| **Year** | 2021 (arXiv v2, 20 October 2021) |
| **Type** | Preprint — arXiv:2101.02118v2 [cs.LG], 16pp. Code: https://github.com/Daniela-Shereen/GBRT-for-TSF |
| **PDF** | `elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting.pdf` (in this folder) |
| **BibTeX** | `elsayed2021gbrt` |
| **Status** | Reference |

## What it is

The time-series companion to
[[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]]. It asks whether
a gradient-boosted tree (XGBoost), set up properly, keeps up with deep forecasting models
from 2016–2020 conference papers.

- **The setup is the whole contribution.** A "naive" GBRT regresses each point on that
  point's covariates and ignores the past. The **window-based** GBRT flattens the last w
  target values into one row, appends the covariates **of the last time step only**, and
  predicts each of the h future steps with a separate model (a multi-output wrapper). That
  turns forecasting into ordinary tabular regression with lagged features.
- **Opponents:** TRMF, LSTNet, DARNN, DeepGlo, DeepAR, DeepState, the Temporal Fusion
  Transformer (TFT) and DAQFF, on electricity, traffic, exchange-rate, solar, air-quality,
  room-temperature and NASDAQ-100 data.
- **Results:**
  - **Univariate, no covariates (Table 2):** the windowed GBRT is best or close on
    Electricity, PeMSD7 and Exchange-Rate. Traffic is the exception, where DARNN and LSTNet
    win. ARIMA and the naive GBRT are far behind everywhere.
  - **Adding simple calendar covariates (Table 3)** moves the GBRT ahead of DeepGlo on all
    four datasets, Traffic included, and ahead of the STGCN traffic model's published RMSE
    on PeMSD7.
  - **Against published numbers:** it beats LSTNet on Solar and Exchange-Rate, DeepAR and
    DeepState on ElectricityV2 and TrafficV2, DARNN on SML 2010, and DAQFF on both air
    quality datasets.
  - **TFT is the one model that beats it consistently** (WAPE 0.055 against 0.067 on
    electricity, 0.095 against 0.148 on traffic).
- **Ablation (Table 8):** appending covariates from every step of the window instead of only
  the last one makes almost no difference.

## Read with care

- **There is no random-walk baseline.** That matters most for the two financial datasets.
  Exchange-Rate and NASDAQ-100 are price **levels**, where "tomorrow equals today" is
  very hard to beat on RMSE and gives a correlation near 1. The GBRT's 0.999 correlation on
  Exchange-Rate is what persistence would give. Nothing here shows a forecast of **returns**.
- **NASDAQ-100 is internally inconsistent.** The GBRT's RMSE (0.078) and MAE (0.063) are
  about a quarter of DARNN's, yet its MAPE (0.0257) is six times worse (0.0043). Those
  can't all be on the same scale, so the comparison is unreliable.
- **Mixed protocols.** Many baselines are numbers copied from the original papers
  (marked * in the tables), others were re-implemented and re-tuned, and Electricity and
  Traffic were sub-sampled. Tuning budgets aren't stated, and each table is a single final
  run with no error bars or significance tests.
- **The GBRT is tuned per dataset** (ElectricityV2 separately), so "a simple baseline" still
  has its window size and hyperparameters chosen on each problem.
- A preprint with no published version found, and the deep models it beats are mostly
  2016–2019. Later work (N-BEATS, PatchTST, and the linear "DLinear" baseline of Zeng et
  al. 2023) reopened the question with stronger baselines on both sides.

## Why it's in the library

**It shows that the framing matters more than the model family.** The same XGBoost goes from
far behind (naive) to competitive (windowed) without changing the learner. The gain comes
from giving it the past as features. That is the usual practice for return prediction too:
lagged returns, volatility and other rolling features on a row per date, fed to a tree
model.

**"Last-step covariates are enough" supports the compact feature set.** If the covariates
are already rolling summaries, repeating their values for every lag adds columns without
adding information. Lags of the target carry the dynamics; the covariates carry the state.

**The missing random walk is the lesson to take.** A forecasting result on prices with no
persistence baseline proves nothing about predictability. Any comparison on financial data
should include the naive forecast and score on returns, not levels.

## Links

- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]] — the i.i.d.
  tabular benchmark, with three reasons trees beat networks there
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same
  question for cross-sectional tabular data, with the same answer
- [[hall-rasheed-2025-survey-of-machine-learning-methods-for-time-series-prediction]] — a
  tally of 79 tree-vs-deep time-series comparisons; roughly a tie on accuracy, trees far cheaper
- [[gu-kelly-xiu-2021]] — deep learning on a return panel, where the benchmark should
  include a well-configured tree model
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — a long flattened window is a
  wide feature vector; trees split one feature at a time and avoid distance concentration
