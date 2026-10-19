# High-dimensional portfolio optimization using GARCH-EVT, R-vine Copula, and SCAD penalty with weight constraints

| | |
|---|---|
| **Authors** | Jian Lv, Chenxu Wang, Wenyong Yuan (School of Finance, Zhejiang University of Finance and Economics) |
| **Year** | 2026 (PDF dated 23 February 2026) |
| **Type** | Working paper — SSRN 6292962, 50pp |
| **Link** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6292962 |
| **PDF** | `lv-wang-yuan-2026-garch-evt-rvine-scad-portfolio.pdf` (in this folder) |
| **BibTeX** | `lv2026highdimensional` |
| **Status** | Reference — a worked pipeline, not evidence |

## What it is

The full copula-to-portfolio pipeline in one paper, run daily on Chinese equities:

1. **Margins:** ARMA(1,1)-GARCH(1,1) with t innovations on each asset, then EVT on the
   standardised residuals. A generalised Pareto distribution fits each tail and a Gaussian
   kernel fits the centre (the semi-parametric margin of McNeil & Frey).
2. **Dependence:** an R-vine copula on the probability-integral-transformed residuals. The
   structure comes from `RVineStructureSelect` (Dißmann's algorithm): each tree is the
   maximum spanning tree on |Kendall's τ|, pair families are chosen by AIC, and
   insignificant edges are pruned to independence.
3. **Scenarios:** 1,000 draws from the vine, pushed back through the inverse margins and the
   GARCH recursion to give one-day-ahead return scenarios.
4. **Optimisation:** minimise CVaR_τ plus a **SCAD** penalty subject to fully-invested
   weights. The CVaR objective is rewritten as a quantile regression (Bassett, Koenker &
   Kordas 2004: CVaR_τ(Y) = (1/τ)·E[ρ_τ(Y − ξ_τ)] − μ, with the budget constraint absorbed by
   regressing on rᵢ − r₁). The non-convex SCAD problem is solved as adaptive-LASSO
   penalised quantile regression.

The data are ten SSE sector indices (to show the vine) and 131 CSI 300 stocks (for the
portfolio), 2010–2016 in-sample and 2017–2020 out-of-sample, with a 500-day rolling window.

**Headline (Table 2, 2017–2020):** SCAD at τ = 0.05 returns 21.4% a year with Sharpe 0.91 and
max drawdown 26.8%. The CSI 300 gives 12.5% and Sharpe 0.55; equal weight 0.41; minimum
variance and mean-variance are both negative (−0.47, −0.36). The τ = 0.01 version, the most
tail-averse, is the weakest of the three (Sharpe 0.59). Including the vine lowers forecast
VaR and CVaR against an independence copula (Fig. 4).

## Read with care

- **Survivorship and selection on the full sample.** 131 of the 300 CSI 300 names survive a
  filter that drops "abnormal returns, missing data, or [failure] to converge". The filter
  is not described as point-in-time, and current constituents are used throughout. Both
  favour the strategy.
- **No transaction costs.** The weights are re-solved every day from a fresh vine fit, and
  turnover is not reported.
- **The significance is thin.** Four years of daily data give a Sharpe standard error of about
  ±0.5, so 0.91 against the index's 0.55 is inside the noise. The excess-return t-test is
  one-sided at p = 0.044 with three τ values tried. The Scheffé tests and the 60/90-day
  RAROC and Sharpe tables use windows advanced one day at a time, so the observations
  overlap by 59/60 or 89/90 and are far from independent. Tests that treat them as
  independent overstate significance.
- **The vine is not isolated in the return comparison.** EWP, MVP and MVO "all employ the
  R-vine copula" too, so Table 2 compares objectives (CVaR + SCAD against variance), not
  copulas. The only with/without-vine comparison is on forecast risk (Fig. 4), not realised
  returns.
- **Fixed tuning.** λ = 1 and α = 3.7 (the Fan & Li default) are fixed, on the grounds that
  sparsity is "insensitive" to them. Why τ = 0.05 beats τ = 0.01 by 0.3 of Sharpe is not
  examined.
- Eq. (24) defines the reported portfolio return with the **mean simulated forecast** r̂,
  which reads as a forecast rather than a realised return. Table 2 presumably uses realised
  returns, but the text doesn't say so. The log-return formula is also printed upside down,
  ln(p_{t−1}/p_t).

## Why it's in the library

**It is the reference implementation of "copula-based scenarios into a CVaR optimiser".**
Each stage has its own note here: GARCH filtering before fitting a copula
([[wikipedia-copula-statistics]] on stationarity), the vine
([[czado-2019-analyzing-dependent-data-with-vine-copulas]]), and scenario CVaR
([[rockafellar-uryasev-2000]]). This paper wires them together and gives the ordering, so it
is a template to copy, not a result to cite.

**The CVaR-as-quantile-regression identity is the reusable piece.** Once CVaR minimisation
is a quantile regression, any penalised quantile-regression solver (LASSO, adaptive LASSO,
SCAD) gives sparse tail-risk portfolios, and the penalty does what a cardinality constraint
would do without the integer programme.

**Its results show the usual pattern.** Minimum variance and mean-variance lose money over
the test period while an equal-weight-like sparse portfolio wins. That matches
[[chopra-ziemba-1993]] and [[michaud-1989]] on estimation error more than it shows the vine
adds return.

## Links

- [[rockafellar-uryasev-2000]] — CVaR optimisation over scenarios, which Step 7 is a
  penalised version of
- [[czado-2019-analyzing-dependent-data-with-vine-copulas]] — R-vines, pair-copula families
  and Dißmann's selection algorithm used in Step 3
- [[wikipedia-tree-graph-theory]] — the spanning-tree construction behind each vine level
- [[artzner-delbaen-eber-heath-1999]] — why CVaR (coherent) rather than VaR
- [[pekar-pcolar-2022]] — fat-tailed margins and CVaR, without the dependence model
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — why the copula, not the correlation,
  sets the joint tail
- [[michaud-1989]], [[chopra-ziemba-1993]] — why the mean-variance benchmarks lose
