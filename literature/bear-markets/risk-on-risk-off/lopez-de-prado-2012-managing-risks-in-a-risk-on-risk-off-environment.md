# Managing Risks in a Risk-On/Risk-Off Environment

| | |
|---|---|
| **Authors** | Marcos López de Prado (Lawrence Berkeley National Laboratory) |
| **Year** | 2012 |
| **Type** | Slides, 50pp. SSRN 2150877, doi:10.2139/ssrn.2150877 |
| **PDF** | Not hosted in this repository (SSRN download, no licence) |
| **Find it** | [doi.org/10.2139/ssrn.2150877](https://doi.org/10.2139/ssrn.2150877) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Managing+Risks+in+a+Risk-On%2FRisk-Off+Environment%22+Prado) |
| **BibTeX** | `lopezdeprado2012roro` |
| **Status** | Reference: Sections IV (eigenvectors and risk-on/risk-off), V (portfolio entropy) and VI (worked examples) carry the argument |

## What it is

A slide deck arguing that in a risk-on/risk-off market, the danger is not only how much
risk a portfolio carries but how concentrated it is along a single direction of the
covariance matrix.

- **Correlation as geometry.** Correlation is the cosine of the angle between two return
  vectors. Pairwise correlations, average correlations and regressions can measure the
  level of risk but not its concentration in a portfolio of more than two assets.
- **Pure bets.** The eigenvectors of the covariance matrix are uncorrelated portfolios that
  between them explain all the variance. Any portfolio can be written as loadings on these
  "pure bets", and its risk can be split exactly among them.
- **Why concentration is dangerous.** Among portfolios of a given size, the eigenvectors
  are where risk peaks (the critical points of the Rayleigh quotient). A portfolio lined
  up with an eigenvector takes the whole of any shock in that direction. In the deck's
  example, doubling the first eigenvalue (the risk-on/risk-off move) doubles the risk of a
  portfolio aligned with it, while a balanced portfolio absorbs much of the shock. The
  analogy is the Tacoma Narrows Bridge failing when wind hit one of its natural vibration
  modes.
- **Portfolio entropy.** Concentration is measured by the entropy of the risk
  contributions across eigenvectors (Meucci's effective number of bets, rescaled from 0,
  fully concentrated, to 1, risk spread evenly). Two worked futures examples make the
  point:
  - stocks, Italian bonds and copper: implied correlation 0, but entropy 0.05, with 98% of
    the risk in one eigenvector;
  - four Treasury futures: implied correlation 0.98, but entropy 1.
- **Balanced baskets.** The deck surveys risk parity (equal risk contribution), maximum
  diversification, diversified risk parity (equal risk on every eigenvector, entropy 1) and
  the author's mini-max subset correlation basket. It argues risk parity can still hide a
  large eigenvector concentration.

## Why it's in the library

- **Concentration, not just level.** In a risk-on/risk-off regime one eigenvector, the
  risk-on/off factor, dominates. A portfolio can sit inside its risk limits and still be
  maximally exposed to that single direction. Entropy over eigenvectors is a direct check.
- **It is a deck, not a paper.** There is no out-of-sample test, and the examples are
  constructed to make the point. The eigenvectors themselves are estimated with noise and
  can change across regimes, which the slides do not address.

## Links

- [[meucci-2009]] — the effective number of bets that the deck's entropy measure rescales
- [[laloux-et-al-1999]] — how much of an estimated covariance matrix's eigen-structure is
  noise
- [[mantegna-1999]] — another way to read structure out of a correlation matrix
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] —
  another paper by the same author
