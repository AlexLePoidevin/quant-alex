# False Safe Haven Assets: Evidence From the Target Volatility Strategy Based on Recurrent Neural Network

| | |
|---|---|
| **Authors** | Tomasz Kaczmarek, Barbara Będowska-Sójka, Przemysław Grobelny, Katarzyna Perez (Poznań University of Economics and Business) |
| **Year** | 2022 (working paper 2021) |
| **Type** | Paper. SSRN 3780149, 59pp; published in *Research in International Business and Finance* 60, 101610 (2022). Daily data 2000–2020; training 2000–2009, out-of-sample test 2010–2020 |
| **PDF** | Not hosted in this repository (SSRN working-paper version; journal version is Elsevier) |
| **Find it** | [doi.org/10.1016/j.ribaf.2021.101610](https://doi.org/10.1016/j.ribaf.2021.101610) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22False+Safe+Haven+Assets%3A+Evidence+From+the+Target+Volatility+Strategy+Based+on+Recurrent+Neural+Network%22+Kaczmarek) |
| **BibTeX** | `kaczmarek2022safehaven` |
| **Status** | Reference: §3.3–3.5 (forecasting models and the strategy), §4 (results, Table 4), §5 (robustness) and §6 (conclusions) |

## What it is

A test of which supposed safe-haven assets actually help a volatility-targeting equity
portfolio, using volatility forecasts from recurrent neural networks.

- **The strategy.** Hold the S&P 500 and cash, with the equity weight set to target
  volatility divided by forecast volatility (no leverage, so at most 100% equity). On days
  when forecast volatility is in the top 10%, 5% or 1% of its history, part of the cash is
  moved into a candidate safe haven, capped at 10%, 20% or 30% of the portfolio. Results are
  averaged over these nine settings.
- **Forecasts.** Two GRU recurrent networks (one using only past volatility, one with more
  inputs) are compared with ARFIMA, GARCH and GJR-GARCH. The networks are tuned with five-fold
  cross-validation and early stopping on 2000–2009 data and tested on 2010–2020, a period that
  includes the COVID crash.
- **Candidates.** Thirteen assets: gold, silver, platinum, copper, oil, cocoa, wheat, soybeans,
  corn, and 10- and 30-year US Treasuries, 10-year Swiss and 10-year German government bonds.
  An asset counts as a safe haven if it raises both the Sharpe and Calmar ratios by more than
  10%.
- **Results on the S&P 500 (Table 4).**
  - The volatility-targeting strategy with the multivariate GRU forecast has a Sharpe ratio of
    0.97 and a Calmar ratio of 0.75, against 0.80 and 0.41 for the index. The authors report
    this as 21% and 83% better.
  - The ARFIMA version does at least as well (Sharpe 1.00, Calmar 0.80), so the neural
    network is not what makes the strategy work.
  - Long-term US Treasuries are the only asset that helps consistently, adding about 0.01–0.04
    to the Sharpe ratio. The conclusion says they add about 5% to the Sharpe ratio and more
    than 10% to the Calmar ratio when forecast volatility is moderate, and that none of the
    assets help when it is extremely high.
  - Gold changes the Sharpe ratio by 0.00–0.04 and the Calmar ratio by −0.06 to +0.04: no
    reliable effect. Oil is clearly harmful, cutting the Sharpe ratio by 0.47–1.09.
- **Other markets.** The Treasury result holds for the Nikkei 225 and Nifty 50. For the Euro
  Stoxx 50 the basic strategy does not beat the index, so safe havens are not tested there.

## Why it's in the library

**It tests safe havens the way an investor would use them**: as a partial replacement for cash
when risk is high, inside a strategy that is already cutting equity exposure. On that test only
long-term Treasuries earn their place over 2010–2020, and gold does not.

**It is also evidence that volatility targeting itself does the work.** Most of the improvement
over the index comes from scaling equity exposure, and a classical ARFIMA forecast is as good as
the neural networks.

**Limits.**

- One test decade, during which Treasuries rallied in most equity selloffs.
- The improvements from adding any asset are small relative to sampling noise, and no
  significance tests are reported for them.
- Transaction costs are not modelled, although the equity weight changes daily.
- The volatility target is described as a 10% *monthly* standard deviation, which would rarely
  bind. If that is right, the strategy is close to fully invested most of the time.

## Links

- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility targeting across 60+ assets, and why it mainly cuts the left tail
- [[baur-smales-2018-gold-and-geopolitical-risk]] — the case for gold as a hedge against geopolitical risk
- [[capie-mills-wood-2005-gold-as-a-hedge-against-the-dollar]] — gold as a partial dollar hedge, unstable across periods
- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — risk-off regimes, when safe havens are supposed to work
