# A Survey of Machine Learning Methods for Time Series Prediction

| | |
|---|---|
| **Authors** | Timothy Hall, Khaled Rasheed (Institute for Artificial Intelligence, University of Georgia) |
| **Year** | 2025 |
| **Type** | Review — *Applied Sciences* 15(11), 5957 (MDPI, open access, CC BY), doi:10.3390/app15115957. 33pp |
| **PDF** | `hall-rasheed-2025-survey-of-machine-learning-methods-for-time-series-prediction.pdf` (in this folder) |
| **BibTeX** | `hall2025survey` |
| **Status** | Reference — a scoreboard of other people's comparisons, not new evidence |

## What it is

A survey that only counts papers in which **the same authors ran both a tree model and a deep
model on the same data**. That rule is meant to avoid comparing numbers across studies with
different datasets and setups.

- **Sample.** A Web of Science query (gradient boosting AND time series AND a deep-learning
  term) gave 589 papers from 2017–2024. From the 100 most-cited, 65 met the criteria; 4 papers
  from 2023 and the 10 most-cited from 2024 were added, for **79 studies** over 46 tasks in 10
  groups (energy, environment, agriculture, water/air quality, transport, structural health,
  finance and demand, healthcare, anomaly detection, other).
- **Scoring.** *First Place Aggregation* (FPA) is the share of comparisons a model wins or
  ties. *Weighted Rank Aggregation* (WRA) maps each rank to 1 − (rank − 1)/(n − 1) and
  averages. ARIMA, linear regression, single trees, SVMs and AdaBoost are dropped up front
  because they lost in the surveyed papers.
- **Overall it's a tie.** Tree models win 54.6% of comparisons (WRA 0.691) and deep models
  52.7% (WRA 0.649). The strongest subclasses are RNNs (FPA 61.4%, WRA 0.733) and the
  XGBoost/LightGBM/CatBoost family (FPA 50%, WRA 0.633). LSTM (39 comparisons, FPA 59%) and
  LightGBM (17, FPA 59%) are the best-supported single models; CatBoost and Transformers top
  the chart on three and five studies. Plain MLPs never win.
- **Training time.** In the 10 studies that report it, the best tree model trained faster
  than the best deep model in 9. The median gap is about 57× (reported as "5603% faster").
- **Author focus predicts the winner (§5.3.5).** In papers built around a deep model, deep
  models score 34% higher on FPA. In papers built around a tree model, trees score 67%
  higher. In balanced papers, trees lead by 15%.
- **Splits (Table 3):** trees for energy, transport and the largest datasets (>206k samples);
  RNNs for environmental, structural-health and the "stock market, finance and market trends"
  group. Hourly data favour boosted trees; daily data are mixed.
- **M5 and M6 (§6).** LightGBM dominated M5 (Walmart sales): it was the main model of the
  top-50 accuracy entries and in four of the top five uncertainty entries. In M6 (50 stocks and
  50 ETFs, monthly forecasts and portfolios for 12 months) the winners used unrelated methods,
  and the organisers found **no correlation between forecast accuracy and investment
  return**. The investment winner was 92nd in forecasting.
- **Recommendation (§7):** do the data and features first, start with LightGBM (CatBoost for
  many categorical features), tune with Bayesian search or Optuna, try an LSTM/GRU next, and
  ensemble the two.

## Read with care

- **Vote counting, not effect sizes.** FPA and WRA ignore how much a model won by, so a
  0.1% RMSE edge counts the same as a 50% one. There are no confidence intervals. The 2.5%
  overall gap is well inside what a different paper sample would give.
- **The sample is selected on citations**, which favour papers with a striking new model, and
  then topped up with 2023–2024 papers by a different rule. Each study's own tuning effort is
  not recorded, and §5.3.5 shows that effort follows the authors' preferred model.
- **The finance result rests on almost nothing.** Group 7 holds six task instances: three
  stock-price or trend tasks, one hedge-fund return task, and two **retail demand** tasks
  (store items, vegetables). "DL is better for finance" comes from that handful. The paper
  itself says the per-domain cells are too small to be definitive.
- **Splits by dataset size and sampling interval** have similar problems: some cells have three
  to eight comparisons, and the size buckets mix sample counts across very different tasks.
- **The training-time mean (127,000%) is two outliers** (905,140% and 235,559%). Use the
  median. Several of the surveyed papers also time a tuned tree model against an untuned
  network, or the other way round.
- **Careless editing in places.** For the largest datasets the text says trees beat deep
  models "by 15.15 in WRA", impossible on a 0–1 scale. Table 3's dataset-size row reads
  "Medium/Large (35,712)" with no upper bound. Software version numbers ("LightGBM 4.6.0",
  "XGBoost 2.1.4") are attached to the abstract and inclusion criteria, although the surveyed
  papers used many versions. Check the figures before quoting a number from the prose.

## Why it's in the library

**It is the base rate for "trees or nets?" on time series.** Across 79 head-to-head studies
the answer is roughly even on accuracy and decisively in favour of trees on cost. That
supports starting with a boosted tree and treating any deep model as something that has to
beat it, which is the same conclusion as
[[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] and
[[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]], reached by
counting rather than by experiment.

**The author-focus result is the most useful number in the paper.** A 34–67% swing in win
rate depending on which model the authors were promoting is the publication-level version of
tuning to the test set. Any comparison here should give both models the same tuning budget
and the same validation folds, decided in advance.

**M6 is the warning for financial use.** Accuracy on prices and money made from the forecasts
were uncorrelated across teams. Choose models on the portfolio outcome (after costs, on held-out
periods), not on RMSE of the forecast.

## Links

- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] — one
  controlled experiment of the kind this survey tallies, with windowed XGBoost against deep
  forecasters
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same
  question for tabular data, including the same selection-bias finding
- [[gu-kelly-xiu-2021]] — deep models on a return panel, where a tuned tree model belongs in
  the comparison
