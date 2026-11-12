# Handling Risk-On/Risk-Off Dynamics with Correlation Regimes and Correlation Networks

| | |
|---|---|
| **Authors** | Jochen Papenbrock (PPI AG / Firamis), Peter Schwendner (Zurich University of Applied Sciences) |
| **Year** | 2015 |
| **Type** | Journal article, *Financial Markets and Portfolio Management* 29(2), 125–147. doi:10.1007/s11408-015-0248-2 |
| **PDF** | Not hosted in this repository (Springer journal version, © Swiss Society for Financial Market Research) |
| **Find it** | [doi.org/10.1007/s11408-015-0248-2](https://doi.org/10.1007/s11408-015-0248-2) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Handling+Risk-On%2FRisk-Off+Dynamics+with+Correlation+Regimes+and+Correlation+Networks%22+Papenbrock) |
| **BibTeX** | `papenbrock2015roro` |
| **Status** | Reference: §3–4 (the six-step regime procedure), Table 2 (regime statistics) and §8 (the MST break-up of the crisis regime) carry the results |

## What it is

A way to find correlation regimes in a multi-asset futures book, and to sort assets into
"risk on" and "risk off" without assuming which is which.

- **Data.** Daily returns on 25 rolled futures from July 1998 to January 2013: six
  government bond futures, seven equity index futures, six commodities and six currency
  futures.
- **The procedure.** Cut the sample into 175 calendar months and compute a 25 × 25
  correlation matrix for each. Turn each into a distance matrix (d = √(2(1 − ρ))). De-noise
  it with average-linkage hierarchical clustering. Compare months by the cophenetic
  correlation between their dendrograms. Then group the 175 months into k = 5 regimes with
  k-means. The choice of five is a judgement call; the authors say two would capture the
  main pattern.
- **What the regimes show.** Regimes 1–4 dominate from 1998 until the run on Northern
  Rock in September 2007, and each asset class mostly forms its own correlated block.
  Regime 5 first appears in mid-2007 and dominates after Lehman. In it the heat map
  collapses to two blocks: bonds and the yen against everything else. This is the
  risk-on/risk-off regime.
- **The numbers.** Mean absolute correlation across the 25 markets is 0.32 in Regime 5,
  against 0.11–0.17 in the others. Mean absolute daily return and realised volatility are
  also highest there (0.51% and 21%). Mean daily returns do not differ significantly across
  regimes (ANOVA p = 0.24). The mean absolute Sharpe ratio is lowest in Regime 5 (0.43):
  assets move a lot but hedge each other, with no steady trend.
- **Risk-on and risk-off assets.** A minimum spanning tree built from Regime 5's average
  correlations breaks into two branches once links with absolute correlation below 0.24
  are cut. The risk-on branch is centred on the Australian dollar and the risk-off branch
  on the US 10-year note future. Natural gas sits on its own, unrelated to the risk-on/off
  split.

## Why it's in the library

- **A data-driven definition of risk-on/risk-off.** Rather than labelling assets by
  intuition, the regime is identified from the shape of the correlation matrix. The
  approach of comparing whole correlation structures across time slices is close to the
  correlation-state work of Münnix et al.
- **Crisis correlation as an input.** The authors suggest parameterising risk models and
  stress tests with the crisis regime's correlation matrix, or with the most similar past
  regime, instead of the most recent window. This is the "correlations go to one when it
  matters" problem made measurable.
- **Limits.** Regimes are found in-sample, with monthly windows of about 21 daily returns
  each, and k is chosen by hand. The paper shows regimes exist after the fact. It does not
  test whether the regime can be identified in real time, or whether acting on it pays.

## Links

- [[munnix-schafer-2011-copula-dependencies]] — dependence structures that change with
  the market state
- [[mantegna-1999]] — the correlation distance and minimum spanning tree used here
- [[laloux-et-al-1999]] — why one-month correlation matrices are mostly noise, the reason
  the authors filter them first
- [[ang-chen-2002]] — correlations that rise in down markets
- [[meucci-2009]] — counting effective independent bets, which collapse towards one in a
  risk-on/risk-off regime
- [[kinlaw-turkington-2014-correlation-surprise]] — a single-number measure of unusual co-movement that flags correlation breakdowns as they start
