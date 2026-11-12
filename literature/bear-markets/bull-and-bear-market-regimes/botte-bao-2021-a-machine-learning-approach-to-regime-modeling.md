# A Machine Learning Approach to Regime Modeling

| | |
|---|---|
| **Authors** | Alex Botte, Doris Bao (Two Sigma) |
| **Year** | 2021 (October) |
| **Type** | Manager research note ("Street View"), 9pp. Daily factor returns from the early 1970s to July 2021 |
| **PDF** | Not hosted in this repository (© Two Sigma, all rights reserved) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22A+Machine+Learning+Approach+to+Regime+Modeling%22+Botte) for the title and authors |
| **BibTeX** | `botte2021regime` |
| **Status** | Reference: short and complete; the four regime descriptions and Exhibit 4 are the content |

## What it is

Two Sigma fits a Gaussian mixture model to its own factor returns and reads the clusters
as market regimes.

- **Method.** A Gaussian mixture model (GMM) fits several multivariate normal
  distributions to the joint returns of the 17 factors in the Two Sigma Factor Lens
  (equity, rates, credit, commodities, inflation, currency, emerging markets, and equity
  and macro style factors). Each cluster has its own means, volatilities and
  correlations. The number of clusters, the only hyperparameter, was chosen by
  cross-validated log-likelihood: four.
- **The four regimes, labelled by the authors.**
  - *Crisis*: equity and credit factors negative, rates positive, trend following
    strongly positive, small caps lagging, the highest factor correlations. Shows up in
    1987, 2008 and March 2020.
  - *Steady State*: most factors earn their usual premia. The most common state, and
    dominant in the 2010s.
  - *Inflation*: the inflation factor earns double-digit returns, the dollar weakens,
    stocks and bonds earn little. Found only in the 1970s and 1980s.
  - *Walking on Ice*: equities up but volatile, style-factor volatility roughly double its
    norm (value 18.2% vs 8.9%). Found mostly around the dot-com bubble and in the rebounds
    after 2008 and 2020.
- **2020–21.** Crisis in February–March 2020, then Walking on Ice, then Steady State in
  late 2020, and a drift back toward Walking on Ice in 2021. The Inflation regime's
  probability stayed near zero despite high CPI prints.

## Why it's in the library

**It is a clear, practical example of data-driven regime labelling.** The mixture model
captures both the centre and the tails of factor returns, and the four clusters line up
with recognisable episodes without being told about them.

**It also shows what this kind of regime model cannot do.** Each day is classified on
its own (the model treats periods as independent), so regimes switch abruptly and there
is no persistence or transition model. The fit uses the full sample, so the labels are
in-sample. The authors say plainly that the model is descriptive, not predictive.

**Read it as a manager's illustration.** It uses Two Sigma's proprietary factor lens and
shows charts, not statistics on out-of-sample stability. The Inflation regime missing
2021 suggests the clusters are tied to how past episodes looked.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a Markov-switching
  alternative, with persistent states and transition probabilities
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — two-state
  bull/bear regimes and the trend rule they imply
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — two regimes in the level of the
  VIX
- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — risk-off
  regimes dated from switches in FX correlations
