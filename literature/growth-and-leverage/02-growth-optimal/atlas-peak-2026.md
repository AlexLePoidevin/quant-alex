# The Kelly Criterion in Financial Markets: Optimal Position Sizing, Portfolio Construction, and Risk Management

| | |
|---|---|
| **Author** | Atlas Peak Research (no named author) |
| **Year** | 2026 (25 April) |
| **Type** | Commercial research note — 23 sections; §12 is *Portfolio-Level Kelly for Equity Books* |
| **Link** | https://www.atlaspeakresearch.com/report/07bf72#12-portfolio-level-kelly-for-equity-books |
| **BibTeX** | `atlaspeak2026kelly` |
| **Status** | To read — body not retrievable |

## Key takeaway

Filed for **§12, portfolio-level Kelly for a book of correlated equity positions** — the
multivariate case, which nothing else in this folder covers. The scalar result
`f* = (μ−r)/σ²` generalises to

```
f* = Sigma^{-1} (mu - r*1)
```

and that inverse is where the whole thing falls apart in practice, because `Σ` for an
equity book is estimated, near-singular, and non-stationary. Everything
`../03-estimation-error/` says about errors in a scalar mean applies here with a matrix
inverse amplifying it.

What is visible of the framing is sound and unusually candid for a sell-side note: Kelly is
presented as a *theoretical upper bound* rather than a target, with the conditions spelled
out — full Kelly is optimal only when "distributions are known, edge is stable, costs are
absent, rebalancing is continuous, margin is frictionless, and there are no career-risk,
redemption, liquidity, tax, or governance constraints." That list is correct and is the
right way to introduce the result.

## Why it's here

**It marks a gap rather than filling one.** This folder currently has only scalar Kelly —
Kelly, Breiman, Merton, Thorp all treat one risky asset or an aggregate. The portfolio
form, where positions are correlated and `Σ⁻¹` does the work, is the case that actually
arises in an equity book, and it is missing. Use this as a pointer to go find that
treatment properly; do not use it as the treatment.
