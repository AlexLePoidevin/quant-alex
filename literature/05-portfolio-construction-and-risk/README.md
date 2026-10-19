# Portfolio construction and risk

How to turn estimates of return and covariance into a portfolio, and how to measure what
can go wrong with it.

| Folder | Question |
|---|---|
| `01-mean-variance-and-estimation-error` | Markowitz, and why optimised portfolios mostly amplify estimation error |
| `02-diversification-and-effective-bets` | How many independent bets a portfolio really holds: effective number of bets, minimum torsion, eigenvalue stability, minimum-correlation weighting |
| `03-tail-risk-and-risk-measures` | When returns are not normal: fat tails, jumps, coherent risk measures, CVaR optimisation |

**Suggested path:** [[markowitz-1952]] → [[michaud-1989]] → [[chopra-ziemba-1993]] →
[[meucci-2009]] → [[artzner-delbaen-eber-heath-1999]] → [[rockafellar-uryasev-2000]]
→ [[lv-wang-yuan-2026-garch-evt-rvine-scad-portfolio]] (copula scenarios into a sparse CVaR optimiser).

Related: improving the covariance input itself is
`../03-correlation-and-dependence/02-covariance-estimation/`. Sizing the whole book for
compound growth is `../06-compounding-leverage-and-position-sizing/`.
