# Identifying the Factor Structure of Equity Returns

| | |
|---|---|
| **Authors** | Larry J. Merville; Suzanne Hayes-Yelken; Yexiao Xu (all Univ. of Texas at Dallas) |
| **Year** | 2001 |
| **Type** | Paper — *Journal of Portfolio Management*, Summer 2001, pp. 51–61 |
| **BibTeX** | `merville2001identifying` |
| **Status** | Read |

*Strapline: "Returns can be better understood using several dimensions."*

## Key takeaway

Does both halves of the job in one paper: **how many factors**, and — unusually —
**what they are**, by a formal identification procedure rather than by eyeballing loadings.

**Data.** 100 portfolios from CRSP (NYSE/AMEX/Nasdaq), sorted into market-cap deciles then
beta deciles. Whole period July 1963 – June 1999, split at 1981. Equity mutual-fund returns
1989–1995 (640→1,970 funds) as an independent corroboration.

**How many.** Scree eigenvalues for the whole period: **75.74, 5.27, 3.17, 0.93, 0.77,
0.50, 0.40, …** — the first eigenvalue takes roughly three-quarters of the variance of 100
portfolios. Kaiser rule gives K = 3 (K = 4 post-1981). The Connor–Korajczyk mispricing test
agrees: average mispricing is 7.66 under CAPM (p = 0.002), still 7.00 with two factors, and
collapses to **0.87 at three factors (p = 0.31)** — insignificant. Adjusted R² runs 0.678
(CAPM) → 0.751 (1) → 0.804 (2) → **0.838 (3)** → 0.847 (4); gains past three are marginal.

**What they are.** The paper's distinctive contribution is a **factor identification
matrix**: run PCA on a combined matrix of the unrotated factor scores *plus* observable
proxies — financial (NYSE index, SMB, HML, an idiosyncratic-risk proxy, Fed funds) and
macroeconomic (industrial production, unexpected inflation, change in expected inflation,
risk premium, term structure, housing starts, producer prices) — then VARIMAX-rotate.
Whatever loads on the same column identifies that factor.

| Factor | Identification |
|---|---|
| 1 | **Market return** — *and idiosyncratic risk* |
| 2 | **Market capitalisation** (SMB / size) |
| 3 | **Investment opportunity set** (HML, interest rates) |
| Higher-order | **The economy** — industrial production (4), producer prices (5), inflation (6), housing starts (8) |

## Why it's here

This is the closest thing to the post-2 thesis stated academically: *a stock is not just a
bet on the company.* The paper's practical warning is the sentence to remember —
regressing an individual stock on a market proxy alone "can yield many cases of significant
abnormal returns because two to three priced factors are omitted from the regression," so
**a three-factor model should be the minimum for individual stock returns in practice.**

It also supplies, in 2001, the formal version of the macro-coupling idea: don't interpret
eigenvectors by inspection, *rotate them jointly with observable proxies and read which
load together.*

## ⚠️ The finding that complicates our framing — and should change it

**Macroeconomic variables identify the *higher-order* factors, not the dominant ones.**

The pipes intuition says that being long Pepsi is substantially a position in rates, energy
and inflation. This paper says those macro exposures are real and *uniquely identifiable* —
but they are factors 4 through 8, with eigenvalues below 1. The top three are the market, a
size effect, and a value/rates composite: **characteristics, not macro variables.**

The authors say so directly: their results "provide a clear picture as to why macroeconomic
variables do not explain variations in asset returns very well."

So the honest version of the claim is layered: *most* of what you own is market; then size
and value/duration; and the macro forces are present, identifiable, and small. That is a
more defensible and more interesting statement than "you're really long rates" — and it
raises the question the series should ask: **why do the forces with obvious economic
meaning explain the least variance?**

## Two other details worth using

**Factor 1 is not purely the market.** It loads 0.94 on the NYSE index but also **0.86 on
the idiosyncratic-risk proxy**. The authors are explicit that "factor 1 is not just
representing the market factor." The dominant mode blends market exposure with a
compensation-for-idiosyncratic-risk component — which is a caution against reading PC1 as
cleanly synonymous with "the market."

**The identification drifts across periods.** In 1981–1999 factor 3 associates with HML
*and* with Fed funds and the default premium, where earlier it was mainly HML. "The
identification structure may change over different sample periods." That is the
tug-of-war / sloshing idea, documented in a table.

## Caveats

- **Sample ends 1999.** No momentum factor, no 2008, no COVID, no 2022 rate shock.
- **Built on 100 sorted portfolios, not individual stocks.** Portfolio construction imposes
  structure before the PCA sees it; the authors acknowledge the Ferson–Sarkissian–Simin
  critique that such sorts may be arbitrary, and use mutual-fund data to corroborate.
- **Kaiser's eigenvalue ≥ 1.0 rule** is a heuristic, weaker than a Marchenko–Pastur band or
  the Onatski test.
- **VARIMAX rotation is a choice**, and the identification depends on it.
- *JPM* is a practitioner journal — peer-reviewed, but less demanding than *JF* / *JFE*.

## Links

- [[ross-1976]] — APT, the theory this tests
- [[patel-2026-sp500-eigenpairs]] — same identification question, sectors instead of macro
- [[molero-gonzalez-et-al-2025]] — β₁ = 1; compare with this paper's "factor 1 is not
  purely the market"
