# The Random Matrix-Based Informative Content of Correlation Matrices in Stock Markets

| | |
|---|---|
| **Authors** | Laura Molero González; Roy Cerqueti; Raffaele Mattera; Juan E. Trinidad Segovia |
| **Year** | 2025 |
| **Type** | Paper — *Chaos* 35, 093111 · [doi:10.1063/5.0289031](https://doi.org/10.1063/5.0289031) · CC BY |
| **BibTeX** | `molero2025informative` |
| **Status** | Read |

## Key takeaway

Peer-reviewed, and it does the thing the Part 2 article most needs: **it doesn't just count
the significant eigenvalues, it identifies what the top ones *are*, empirically.**

Design: 12 markets (8 developed, 4 emerging), constituent stocks of each index, 2015–2024,
**rolling windows** (n = 252 days, step 5; n = 1000 for S&P 500 at p = 500, n = 500 for
Nikkei at p = 225). MP band per window, then interrogate the escapers.

**Three results:**

1. **λ₁ *is* the market portfolio — measured, not asserted.** Treat each leading eigenvector
   as portfolio weights, normalise to sum to one, regress its return on the market return.
   **β₁ = 1 in every one of the twelve markets.** This is the empirical demonstration that
   "the market is an eigenvector."
2. **λ₁ tracks market connectedness.** Its path overlaps the Diebold–Yilmaz Total Spillover
   Index closely enough that the paper proposes λ₁ as a proxy for spillover. **The dominant
   eigenvalue is a time-varying measure of entanglement.**
3. **λ₂ counter-moves.** The second eigenvalue runs *opposite* to spillover and to λ₁ across
   nearly all markets, with mostly negative betas (IBEX35 −11, FTSE100 −8.2, Dow −5.8,
   S&P 500 −2.4). Read as a defensive / safe-haven component. **⚠️ Statistically significant
   in only 2 of 12 markets (Nikkei, Dow Jones)** — the authors say so plainly. Suggestive,
   not established.

## Why it's here

**Result 2 is the one that matters for our framing.** The article's thesis is cross-sectional
*entanglement*, not factor models. This paper gives entanglement a number that moves: λ₁
rises as connectedness rises. That converts "equities are entangled" from a static
observation into a dynamic, measurable quantity — and it is the mechanism behind
dimensionality collapse in crises (entanglement up ⇒ λ₁ up ⇒ effective dimension down).
It is the empirical backbone for the crisis/regime material.

**Result 1 retires an assertion.** We had planned to say "the market mode is delocalised,
therefore it is the market." This paper shows β = 1 directly. Cite it rather than argue it.

Mild caveat on Result 2: λ₁ and a spillover index are both measures of connectedness, so
agreement is reassuring rather than surprising. The practical value is that λ₁ is an
eigendecomposition while Diebold–Yilmaz needs a fitted VAR — same information, far cheaper.

## ⚠️ The tension with Patel (2026) — and what it teaches

The two papers disagree on how much structure there is:

| | Patel (2026) | Molero González et al. (2025) |
|---|---|---|
| Sample | 474 stocks, T = 1258, one window | 12 markets, rolling windows |
| Q | 0.377 → λ₊ = 2.60 | 0.5 for S&P 500 → λ₊ ≈ 2.91 |
| Escapers | **15** | **~3; the 4th is "almost never" above λ₊** |

Both used the S&P 500. The counts differ by 5×. Reasons, and each is a lesson:

- **The band depends on Q = p/n, so the count depends on your window length.** A longer
  sample tightens the band and admits more modes. The number of pipes you measure is partly
  an artifact of how much data you looked at. **Always report Q.**
- **Rolling 252-day windows are noisy.** Estimating a correlation matrix from one year
  detects only the most persistent modes.
- The paper also cites the **Onatski test**: at 99% confidence only **one** factor is
  significant; relax to 95% or 90% and you get **up to three**. So even the "significant"
  count is a function of the threshold you chose.

**This is a genuinely important caveat for the article.** The honest claim is not "the
market has exactly K dimensions." It is that the dimension is *far smaller than N*, with the
precise figure depending on window length, universe, period and confidence level. Reporting
a single number without those four is the mistake both to avoid and to point out.

## Caveats

- Rolling windows of 252 days for most markets — short for correlation estimation.
- The S&P 500 uses Q = 0.5, a wide band and therefore a conservative escaper count.
- λ₂-as-safe-haven is significant in 2 of 12 markets. Do not repeat it as a finding.
- 2015–2024 covers COVID, which is useful for the regime argument.
- Yahoo Finance data.

## Links

- [[patel-2026-sp500-eigenpairs]] — same test, static, 5× the escapers; read together
- [[marchenko-pastur-1967]] · [[laloux-et-al-1999]] · [[plerou-et-al-2002]]
