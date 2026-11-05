# Variance Dispersion and Correlation Swaps

| | |
|---|---|
| **Authors** | Antoine Jacquier (Imperial College London and Zeliade Systems), Saad Slaoui |
| **Year** | 2010 (arXiv 1004.0125, q-fin.PR) |
| **Type** | Paper, 14pp |
| **PDF** | `jacquier-slaoui-2010-variance-dispersion-and-correlation-swaps.pdf` (arXiv version) |
| **BibTeX** | `jacquier2010dispersion` |
| **Status** | Reference: §3 (implied correlation), §5.2–5.3 (the P&L decomposition) and §5.4 (weighting schemes) carry the result |

## What it is

An explanation of why two ways of trading correlation give slightly different prices.

- **The background.** Banks that sell multi-asset structured products (worst-of options,
  Everest, Himalaya) end up short correlation and want to buy it back. They can buy a
  correlation swap, which pays realised average correlation minus a strike. Or they can
  run a dispersion trade: short options or variance swaps on an index, long the same on
  its components. A dispersion trade's implied correlation is not the same as the
  correlation-swap strike; the paper cites an empirical spread of about ten basis points.
- **Implied correlation.** Following Bossu, the average correlation implied by the index
  and component volatilities is roughly the index variance divided by the square of the
  weighted average component volatility.
- **The decomposition.** For a delta-hedged dispersion trade built from variance swaps, the
  P&L splits into:
  - a gamma part, equal to the spread between implied and realised correlation times a
    weighted average of component variances (exact when each component's notional is its
    squared index weight); and
  - a volatility part, from vega, volga and vanna. For variance swaps vanna is zero.
- **The result.** With practical weightings (vega-hedged or vega-weighted flat) the
  correlation part is almost exact, so the gap between dispersion-implied correlation and
  the correlation-swap strike is explained by the volga term, that is, by the volatility
  of volatility. Read the other way, the observed spread gives an estimate of vol of vol.
- **Other results.** The same analysis for gamma swaps, which weight squared returns by
  price level and so need no cap against jumps. The vega-weighted flat strategy is shown
  to be the boundary for arbitrage.

## Why it's in the library

- Dispersion trading is the main way correlation is traded, and this shows exactly what
  its P&L is made of: a correlation bet plus a second-order bet on volatility of volatility.
- Index options are usually expensive relative to their components because correlation
  rises in sell-offs. This paper separates that correlation premium from the vol-of-vol
  effect.

## Links

- [[ang-chen-2002]] — correlations rise in down markets, the risk a short-correlation
  position is exposed to
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — how correlation assumptions in
  multi-asset products failed in 2008
- [[carr-laurence-2011-multi-asset-stochastic-local-variance-contracts]] — pricing variance
  of a basket from basket options, the model-free side of the same multi-asset problem
