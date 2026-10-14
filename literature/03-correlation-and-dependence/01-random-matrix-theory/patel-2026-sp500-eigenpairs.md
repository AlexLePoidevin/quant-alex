# Economic Interpretation of Eigenvalues and Eigenvectors in S&P 500 Correlation Matrix via Marchenko-Pastur Law

| | |
|---|---|
| **Author** | Zubin Patel (project advisor: Tina Lal) |
| **Year** | 2026 |
| **Type** | Unpublished manuscript — student research project |
| **BibTeX** | `patel2026sp500` |
| **Status** | Read |
| **Code** | [github.com/zubinpatel07-lang/sp500-eigenvalue-analysis-via-marchenko-pastur-law](https://github.com/zubinpatel07-lang/sp500-eigenvalue-analysis-via-marchenko-pastur-law) |

## Key takeaway

Applies Marchenko–Pastur to the Pearson correlation matrix of daily log returns,
**N = 474 S&P 500 stocks, T = 1,258 days (2013–2018), Q = N/T ≈ 0.377**, giving a noise band
of **[0.15, 2.60]**. Then interprets every eigenvalue above the bound as an *eigenportfolio*
and names it economically.

**The headline numbers:**

| Region | Count | % of eigenvalues | % of eigenvalue sum |
|---|---|---|---|
| Below λ₋ = 0.15 | 103 | 21.7% | 2% |
| Inside [0.15, 2.60] | 356 | 75.1% | 48% |
| **Above λ₊ = 2.60** | **15** | **3.2%** | **50%** |

**λ₀ = 141.07 — 29.8% of the trace on its own, ~54× the MP upper bound.** Its eigenvector
has all components the same sign in a tight range (−0.068 to −0.012, σ ≈ 0.010) versus an
average range of 0.324 across the other 473 — i.e. **delocalised**, exactly the predicted
signature of a market-wide mode.

**The named modes (1–14):** utilities · energy · regional banks · physical retail · real
estate · healthcare · **low volatility** · defense · event-driven · managed healthcare ·
airlines · entertainment · event-driven · event-driven.

## Why it's here

This is the closest published execution of the measurement the Part 2 article is built
around, and it supplies **reference values for every blank in `draft.md`**. Treat our own
run as a replication on a different sample, not a novel result.

Three details that are directly usable:

1. **λ₀'s top loadings are BLK, BRK.B, PFG, IVZ** — asset managers and diversified holding
   companies. The most market-like stocks are the ones that literally own a slice of
   everything. That is a far better illustration of "delocalised eigenvector = the market"
   than any abstract description.
2. **Eigenvalue 7 is a *style*, not an industry** — top loadings mix utilities (EIX, AEE,
   PEG, XEL) with consumer staples (PG, CLX, CL, PEP). The paper reads it as a low-volatility
   / defensive factor driven by stable demand and rate sensitivity. **This is the single most
   useful finding for our framing:** the modes are not merely sector labels, they are shared
   *exposures*. A rate-sensitive defensive channel cuts across industry classification
   exactly as the pipes argument predicts.
3. **Eigenvalues 9, 10, 14 are event-driven** and sit just above the bound — transient
   co-movement rather than persistent structure, with weaker eigenportfolio variance. A
   useful honesty note: not every escaper is a durable factor.

## ⚠️ Methodological gap we can improve on

**The band is fitted with σ² = 1 on the raw spectrum, with no correction for the dominant
mode.** This is the standard naive application, and the paper's own numbers show why it
undercounts:

- Trace = N = 474. The market mode takes 141.07, leaving **332.9 of variance spread across
  473 modes** — an average of ≈ **0.70**, not 1.0.
- Refitting the band to that residual variance gives λ₊ ≈ 0.70 × 2.60 ≈ **1.83**, not 2.60.
- More eigenvalues clear a bound of 1.83 than clear 2.60, so **15 is a lower bound on the
  number of significant modes.**

Corroborating evidence for the same point: **103 eigenvalues (21.7%) fall *below* λ₋**.
Under a genuine MP null with Q < 1 essentially nothing should. That mass below the lower
edge is precisely what you expect when one mode has absorbed ~30% of the variance and the
σ² = 1 assumption is therefore wrong for the bulk. The excess-below-λ₋ and the undercount-
above-λ₊ are the same artifact.

*(The 0.70 arithmetic is ours, derived from the paper's reported trace and λ₀ — the paper
does not compute it.)*

## Caveats on using it

- **Not peer-reviewed.** A supervised student research project. The underlying result is
  not novel — it replicates Laloux et al. (1999) and Plerou et al. (2002), both of which are
  peer-reviewed and should carry the citation weight. Use this for its *economic
  interpretation table*, which is more granular than either.
- **2013–2018 only** — a low-volatility bull regime with no COVID and no 2022 rate shock.
  Structure is regime-dependent; this sample says nothing about how the census behaves in a
  crisis.
- **Survivorship.** 474 of 505 retained by requiring fewer than 10 missing days over the
  window, i.e. names that survived the whole period. Distorts realised returns far more
  than correlation structure, but it is there.
- Source data is a Kaggle mirror rather than a primary vendor feed.
- The paper is candid that the MP bound is "a general guideline rather than a strict binary
  classifier" — the right posture, and one we should keep.

## Links

- [[marchenko-pastur-1967]] — the theorem it applies
- [[laloux-et-al-1999]], [[plerou-et-al-2002]] — the peer-reviewed results it replicates
