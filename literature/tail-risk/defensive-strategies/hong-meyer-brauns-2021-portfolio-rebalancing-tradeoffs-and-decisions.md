# Portfolio Rebalancing: Tradeoffs and Decisions

| | |
|---|---|
| **Authors** | Xing Hong, Philipp Meyer-Brauns (Dimensional Fund Advisors) |
| **Year** | 2021 (June) |
| **Type** | Manager research paper, 21pp (SSRN 3858951). Hypothetical index backtests: US 60/40 1979–2019, global 60/40 1988–2019 |
| **PDF** | Not hosted in this repository (Dimensional paper; "unauthorized copying ... strictly prohibited") |
| **Find it** | [doi.org/10.2139/ssrn.3858951](https://doi.org/10.2139/ssrn.3858951) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Portfolio+Rebalancing%3A+Tradeoffs+and+Decisions%22+Hong) |
| **BibTeX** | `hong2021rebalancing` |
| **Status** | Reference: Exhibits 2–3 (US 60/40), 7–8 (tiered bands) and 10–11 (tracking error, drawdowns) carry the results |

## What it is

A practical comparison of rebalancing rules for a fixed-weight portfolio, arguing that the
choice should be made on cost against tracking error, not on return.

- **The rules tested.** Four calendar rules (monthly, quarterly, annual in December or
  June) and tolerance bands of 1%, 2.5%, 5%, 7.5% and 10%. When a band is breached the
  portfolio goes either all the way back to target or only to the edge of the band
  ("rebalance to bound"). Bands are checked monthly. No costs are deducted; turnover stands
  in for cost.
- **Returns barely differ.** For a US 60/40 (Russell 3000 / US Aggregate), average monthly
  returns across all 14 rules span 0.87% to 0.89%, and annualised returns 10.39% to
  10.64%. What differences exist track the average equity weight: wider bands let equities
  drift up (to 65.2% on average for a 10% band rebalanced to bound), so they earn a little
  more. A footnote shows the same thing as noise: twelve annual rules that differ only in
  the month chosen produced a 0.03% monthly spread with t = 2.99, which the authors
  attribute to chance.
- **Bands beat the calendar on cost per unit of tracking error.** For a given tracking
  error against a monthly-rebalanced portfolio, calendar rules turn over more. Rebalancing
  to the band edge improves the trade-off further. Monthly rebalancing turns over roughly 9–10%
  a year one way; a 10% band rebalanced to bound accepts about 1% tracking error for
  turnover of a percent or two (read from the paper's chart). The pattern holds across 253 rolling 20-year windows.
- **Tiered bands.** For a six-component global 60/40, one band for the stock/bond split and
  a second for components within each sleeve cuts turnover further for the same tracking
  error. Almost all within-sleeve rebalancing happens in equities, the more volatile sleeve.
- **What tracking error costs.** Maximum drawdowns are about the same across rules
  (30–33% for the US 60/40). The visible cost is short-run divergence from target: the
  worst 12-month gap against monthly rebalancing is −0.2%/+0.2% for a 1% band and
  −2.9%/+3.7% for a 10% band. Tracking error grows with the equity share: the gap between
  10% and 1% bands is 1.47 points at 80% equity and 0.64 points at 20%.
- **Fewer components, less turnover.** An eight-index global equity mix rebalanced back to
  market weights turns over 0.6–8.8% a year, against zero for a single all-market index
  with the same exposure. The paper uses this to argue for integrated funds, which is also
  Dimensional's product.

## Why it's in the library

**It separates the return question from the cost question.** Once the target mix is set,
rebalancing rules mostly change how far the portfolio drifts from it, not what it earns.
Return differences between rules are style drift (more equities) or noise, and the paper
shows the noise is large enough to look significant.

**It is the plain-vanilla baseline for the defensive rebalancing papers.** The Man Group
papers here treat rebalancing as an implicit short-volatility trade and try to time it.
This paper is the view that ignores timing and asks only for an efficient band.

**Limits.** A manager's paper with hypothetical index data and no trading costs, taxes or
cash flows. Turnover is a stand-in for cost, so the "efficient" frontier depends on how
costly turnover really is for a given investor. Bands are checked monthly only, which
understates how often a band would trigger with daily monitoring.

## Links

- [[granger-et-al-2014-rebalancing-risk]] — why fixed-weight rebalancing behaves like a short straddle in trending crashes
- [[rattray-et-al-2020-strategic-rebalancing]] — timing rebalancing with trend signals to cut drawdowns
- [[hoffstein-faber-braun-2020-rebalance-timing-luck-of-smart-beta]] — how much the choice of rebalance date alone moves results
- [[booth-fama-1992]] — the diversification return that rebalancing harvests
