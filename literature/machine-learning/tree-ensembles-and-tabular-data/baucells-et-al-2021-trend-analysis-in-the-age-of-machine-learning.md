# Trend Analysis in the Age of Machine Learning

| | |
|---|---|
| **Authors** | Manel Baucells (Darden), Emanuele Borgonovo (Bocconi), Elmar Plischke (Clausthal), John Barr and Herschel Rabitz (Princeton) |
| **Year** | 2021 (working paper, version of 21 May 2021, SSRN 3867894) |
| **Type** | Working paper, 24pp. Theory with worked examples and a COVID-19 SEIR simulator case study |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `baucells2021trend` |
| **Status** | Reference: §3 (the consistency results and Table 1) and §5 (the two indices) carry the content |

## What it is

Despite the title, this is not about price trends. "Trend" here means the shape of a
model's input–output relationship: does the output rise or fall, bend up or down, as one
input changes? The paper asks which of the common plots and statistics used to read a
black-box model (a trained machine-learning model or a simulator) report that shape
correctly.

- **The property tested.** An indicator is *monotonicity-consistent* if, whenever the
  model output is increasing in an input, the indicator says so; *convexity-consistent*
  is the same for convexity.
- **The verdicts (Table 1).**
  - One-way sensitivity functions (vary one input, hold the rest at a baseline), and
    therefore ICE plots (many of these at different baselines), are always consistent.
    So are gradients and Hessians where they exist.
  - Partial dependence functions (average the model over the other inputs' *marginal*
    distribution) stay consistent even when inputs are correlated, provided the inputs'
    joint support is a product of their individual ranges.
  - Correlation coefficients, regression curves (conditional expectations) and ALE plots
    are only guaranteed consistent when inputs are independent. With dependence they can
    report the wrong sign. Example 4: output x₁·x₂, increasing in x₁, yet the correlation
    with x₁ is −0.083 and the regression curve slopes down.
- **Intervention versus forecasting.** If output depends only on x₁ and x₂ merely
  correlates with x₁, the regression curve on x₂ slopes, but acting on x₂ changes
  nothing. Partial dependence and ICE plots show it flat. For "what if we change this
  input?" questions, only the consistent indicators answer correctly.
- **Two new indices.** A *discrepancy index* (how often the local ICE slopes disagree in
  sign with the partial dependence slope, 0 to 1) and a *flatness index* (how much of the
  partial dependence curve is flat). Together they flag non-monotonic models and the case
  where ICE lines go both ways and average to a flat, uninformative partial dependence.
- **Recommendation.** Plot ICE and partial dependence together and report the two indices.
  Partial dependence problems in practice come from the ML model extrapolating into
  regions without data, not from the definition itself.

## Why it's in the library

**It is a careful guide to reading fitted models.** When a tree ensemble or network is
used to forecast returns, partial dependence and ICE plots are the standard way to check
what it learned from each feature. This paper says which of those diagnostics can be
trusted when features are correlated, as financial features almost always are. It pairs
with the tree theory notes on what feature importance measures.

**Caveat on fit.** It was filed from a folder of trend-following papers, but it has
nothing to do with market trends; the title is the only connection. It sits here, next to
the tree-model interpretability material.

## Links

- [[klusowski-2019-analyzing-cart]] — what MDI feature importance in trees actually
  measures; a companion question to which effect plots can be trusted
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the tree models whose fitted shapes these plots are usually used to read
