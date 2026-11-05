# Using Machine Learning to Predict Realized Variance

| | |
|---|---|
| **Authors** | Peter Carr (NYU Tandon), Liuren Wu (Baruch College, CUNY), Zhibai Zhang (NYU Tandon) |
| **Year** | 2019 |
| **Type** | Paper, arXiv 1909.10035 (q-fin.MF), 15pp |
| **PDF** | `carr-wu-zhang-2019-using-machine-learning-to-predict-realized-variance.pdf` (arXiv version) |
| **BibTeX** | `carr2019mlvariance` |
| **Status** | Reference: §3 sets up the two regressions and the tradability constraint, §4 has the out-of-sample R² tables |

## What it is

A test of whether regression on SPX option prices can forecast realized variance better
than the VIX formula does, while still producing an index that a portfolio of options could
replicate.

- **The problem with VIX as a forecast.** VIX² weights out-of-the-money options by
  2ΔK/K², the variance-swap replication weights. Those weights are chosen to replicate
  variance under the risk-neutral measure, not to forecast realized variance. They also use
  many illiquid deep out-of-the-money options: the CBOE white-paper example has 149.
- **Setup.**
  - Data: daily SPX options from OptionMetrics, 1996–2016.
  - Features: 2k+1 consecutive strikes around the money (k ∈ {10, 20, 30, 40}). Each is
    interpolated to a fixed 30- or 60-day horizon VIX-style and divided by K² so it
    stays stationary.
  - Validation: an initial 1,000-day training set, retrained every 30 days on all
    available data, with the overlap between training and test observations purged.
  - Each model tunes one hyperparameter only, to limit overfitting.
- **Two regressions.**
  - Regression I predicts realized variance directly from the options.
  - Regression II predicts the gap between realized variance and a synthetic VIX*², which
    amounts to forecasting the variance risk premium, then adds VIX*² back.
- **The tradability constraint.** For the forecast to be an index that an option portfolio
  can replicate, it must be a piecewise-linear function of option prices.
  - Linear regression, ridge and a one-hidden-layer ReLU network satisfy this.
  - A random forest does not, because its prediction is an average of past realized
    variances. It is kept only for comparison.
- **Results (out-of-sample R², 30 days).**
  - The synthetic VIX*² alone scores 0.169 with 21 options, rising to 0.389 with 81.
  - With few options, linear regression helps most: 0.313 with 21 options against 0.169.
  - With 81 options, the best model, the ReLU network on Regression II, reaches 0.394
    against VIX*²'s 0.389. Ridge reaches 0.392.
  - Regression II beats Regression I for every non-linear model. In Regression I the
    random forest is negative.
- **Results (60 days).**
  - VIX*² gets worse as more options are added, falling from 0.300 to −0.155.
  - The best model, the network on Regression II with 41 options, reaches 0.342.
- **Robustness checks.**
  - Adding past returns and realized variance as features (not tradable) adds at most
    about 0.006 of R².
  - Doubling the strike spacing to $10 keeps 21-option performance but lowers it with 41
    options.

## Why it's in the library

- **Model the residual.** The paper's main finding is that it is better to predict the
  deviation from an economically motivated benchmark than the target itself. Regression II
  is a residual model on top of VIX, the same "benchmark plus correction" pattern that works
  elsewhere in forecasting.
- **Fewer options, similar forecast.** The real gain is in liquidity. A short strip of
  near-the-money options, weighted by regression, forecasts about as well as VIX's full
  strip. Where many strikes are available, the improvement over VIX*² is marginal.
- **Tradability limits the model class.** If a forecast has to be a payoff, the model must
  be piecewise linear in prices. This is a constraint on model choice that has nothing to do
  with accuracy, and it rules out tree ensembles for this use.
- **Modest R².** The best out-of-sample R² is about 0.39 at 30 days. Realized variance is
  only partly predictable from options, and the paper reports that honestly rather than
  claiming a large gain.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  VIX as a traded instrument, whose formula this paper tries to improve as a forecast
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]] —
  trees usually win on tabular data. Here they are excluded for a structural reason: their
  output cannot be replicated by a portfolio
