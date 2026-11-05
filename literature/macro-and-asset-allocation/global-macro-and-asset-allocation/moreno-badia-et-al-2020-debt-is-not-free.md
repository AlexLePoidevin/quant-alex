# Debt Is Not Free

| | |
|---|---|
| **Authors** | Marialuz Moreno Badia, Paulo Medas, Pranav Gupta, Yuan Xiang (IMF Fiscal Affairs Department) |
| **Year** | 2020 (January) |
| **Type** | IMF Working Paper WP/20/1, 68pp. Fiscal crises in 188 countries, 1980–2016 |
| **PDF** | Local copy only (© International Monetary Fund, no open licence) |
| **BibTeX** | `morenobadia2020debt` |
| **Status** | Reference: §III (crisis definition and data), §IV–V (feature selection, variable importance, partial dependence) and Appendix 5 (out-of-sample design) carry the results |

## What it is

An early-warning study of fiscal crises that asks whether high public debt actually predicts
them, using random forests instead of the logit models usual in this literature.

- **What counts as a crisis.** A year with at least one of four events: a credit event
  (default or restructuring), exceptionally large IMF financing, an implicit domestic
  default (very high inflation or arrears), or a loss of market confidence (spread
  spikes). Over 1980–2016 there are 418 crisis starts: 25 in advanced economies, 202 in
  emerging markets and 191 in low-income countries. The 1990s had the most; about a third
  overlap with currency crises, few with banking crises.
- **The predictors.** 748 indicators built from debt (public, public external, private,
  total, debt service, creditor structure), growth, inflation, fiscal balances, the
  external accounts, global factors, demographics and institutions, each in several
  forms (levels, lags, 3-, 5- and 10-year changes, cross-country averages). Missing values
  are filled with the training-sample median.
- **The method.** A random forest predicts the chance of a crisis starting in the next two
  years. Four feature-selection algorithms (Boruta, recursive feature elimination, VSURF,
  permutation p-values) cut the 748 variables down. Out-of-sample tests use 15 expanding
  windows starting with a 1980–2000 training sample, rolled forward a year at a time.
  Importance is read from permutation importance and Shapley values; shapes and
  interactions from partial dependence plots and Friedman's H-statistic.
- **How well it predicts.** Out-of-sample AUC is about 0.81 for advanced and emerging
  economies and about 0.71 for low-income countries (0.5 is a coin toss), against 0.69 and
  0.68 for an earlier IMF logit benchmark. Boruta keeps over 300 variables, matches the
  full model's accuracy and selects nearly the same set when 5% of the sample is dropped
  (overlap 0.92); recursive elimination is less stable (0.63).
- **What predicts crises.** Debt, especially public external debt, is the most important
  group. Its effect is strongly non-linear: in advanced economies the crisis probability
  rises sharply around 70% of GDP; in emerging markets it is flat below about 30% and
  steep above. Above about 70% of GDP (80% for low-income countries) the predicted
  probability crosses the crisis threshold whatever else is going on.
- **The interest–growth differential (r − g) barely matters.** Its partial dependence is
  almost flat, and in event studies r − g stays low until the crisis starts, then jumps. So
  it is a coincident indicator, not a leading one, and a negative r − g does not offset
  high debt.
- **Interactions.** Debt matters more alongside other stresses: inflation above about 20%,
  current-account deficits of 3–7% of GDP, and a private credit gap above about 40% all
  raise the crisis probability at moderate debt levels.

## Why it's in the library

**It is a crisis-prediction study with a reasonable out-of-sample design.** Expanding
windows, retuning each year, comparison against a published benchmark and a stability check
on which variables get selected are the habits a forecasting study should have. The AUC of
about 0.8 is a fair measure of how predictable fiscal crises are two years out with annual
macro data.

**Its main result is a warning about a popular argument.** The case that debt is cheap when
interest rates are below growth rests on r − g. Here r − g carries almost no warning,
because it moves only once a crisis has begun. For anyone reading macro risk into asset
prices, the leading signal is the debt stock and its mix, not the current cost of
servicing it.

**It shows the limits of the method as clearly as the results.** The paper says plainly
that the model finds association, not causation. Importance and partial-dependence plots
come from a forest with hundreds of correlated, overlapping predictors (the same variable in
levels, lags and changes), which is exactly where tree importance measures are least
reliable. The thresholds (70% of GDP and so on) are readings off those plots, not estimated
break points with standard errors. The authors are IMF staff, and the paper argues a policy
position.

## Links

- [[klusowski-2019-analyzing-cart]] — what tree feature-importance scores actually measure, and why they mislead when predictors are correlated
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]] — why tree ensembles are the default for tabular data like this panel
- [[chen-roll-ross-1986]] — macro variables (inflation, growth, default spreads) as priced risks in asset returns
- [[harvey-liu-zhu-2016]] — the multiple-testing problem when hundreds of candidate predictors are screened
