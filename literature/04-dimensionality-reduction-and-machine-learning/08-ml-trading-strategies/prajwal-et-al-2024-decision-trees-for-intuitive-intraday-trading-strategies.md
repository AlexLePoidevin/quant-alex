# Decision Trees for Intuitive Intraday Trading Strategies

| | |
|---|---|
| **Authors** | Naga Prajwal (arXiv lists the name as Prajwal Naga), Dinesh Balivada, Sharath Chandra Nirmala, Tiruveedi Poornoday — undergraduate students, Department of CSE, The National Institute of Engineering, Mysuru, India |
| **Year** | 2024 (v1, 22 May) |
| **Type** | Preprint — arXiv:2405.13959v1 [q-fin.ST], 6pp, CC BY 4.0 |
| **PDF** | `prajwal-et-al-2024-decision-trees-for-intuitive-intraday-trading-strategies.pdf` (in this folder) |
| **BibTeX** | `prajwal2024decision` |
| **Status** | Reference — a short student paper; kept as a baseline and a checklist example, not as evidence |

## What it is

A per-stock, one-minute trading rule learned by a shallow decision tree. Each of the NIFTY 50
stocks gets its own tree, trained on nine technical inputs to predict whether the next
one-minute return is positive.

- **Data (§II).** One-minute bars from the ICICI Breeze API for 2022–2024, adjusted for
  corporate actions with daily adjustment factors from Yahoo Finance.
- **Inputs (§III.A).** One-bar and 15-bar returns, 14-period RSI and ADX, the SMA-to-close
  ratio, the SMA–close correlation, 14-bar and 210-bar rolling volatility, and the
  VWAP-to-close ratio. No scaling, since trees do not need it.
- **Model (§III.B, §IV.B).** scikit-learn `DecisionTreeClassifier`, Gini criterion,
  **max depth 4**, label = sign of the next one-minute close-to-close return. Depths 3 to 6
  were compared (Figs. 1–3); trees use about five to seven of the nine inputs, and the
  inputs used differ by stock (Figs. 4–5).
- **Backtest (§IV.C).** vectorbt, signals shifted one bar, returns on close prices, **no
  commissions or slippage**. Training 2022–2023, testing 2023–2024. Annualisation uses
  252 × 375 one-minute bars and a 7.2% risk-free rate.
- **Results (Table 1, test period, average across stocks).** Sharpe 5.81 for the strategy
  against 2.36 for buy-and-hold; total return 28.6% against 34.2%; max drawdown −2.6%
  against −7.0%; win rate 48%. The strategy beat buy-and-hold on Sharpe for 60% of stocks
  and on total return for 46%, both down from the training period.

## Read with care

- **No trading costs at one-minute frequency.** The model can change position every minute.
  Even a fraction of a basis point per trade would dominate a 48% win-rate strategy at this
  turnover. The results are best read as gross signal, not as a strategy.
- **Look-ahead in data cleaning.** Missing minutes are filled by **linear interpolation**,
  which uses the next observed price. On one-minute bars this can leak the future into both
  features and labels.
- **Model selection on the test set.** The depth sweep in Figs. 1–3 is plotted on the
  testing dataset, and depth 4 was chosen from it. The proposed next step, pruning stocks
  that underperformed, is also selection on outcomes.
- **One year out of sample, one market, one split.** No walk-forward retraining, no seeds,
  no significance tests.
- **Sharpe from tiny volatility.** Annualising one-minute returns with 94,500 periods a year
  and subtracting a 7.2% risk-free rate gives large Sharpe ratios from small, autocorrelated
  P&L. Lower total return than buy-and-hold with a higher Sharpe mainly reflects time out of
  the market.
- **Benchmark.** Buy-and-hold per stock, not a cost-matched or timing-neutral comparison.

## Why it's in the library

**As a contrast case for per-asset against pooled models.** One tree per stock on two years
of data is the opposite design to a cross-sectional ranker that pools all stocks and learns
relative order. The paper shows the appeal (interpretable, stock-specific rules) and the
cost (each model sees little data and selection is easy to overfit).

**As a compact checklist exercise.** Interpolated gaps, test-set tuning, zero costs at high
frequency and Sharpe ratios inflated by annualising minute bars are four of the most common
ways an intraday backtest goes wrong. All four appear here in six pages.

**Depth-limited trees as a sanity baseline.** A depth-4 tree on a handful of technical
features is a reasonable floor for any intraday model; a more complex model that cannot beat
it after costs is not adding much.

## Links

- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — why trees are the default on tabular features
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same case,
  with gradient-boosted ensembles
- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] — simple
  tree baselines for time series
- [[harvey-liu-zhu-2016]] — testing many stocks and depths raises the bar for significance
