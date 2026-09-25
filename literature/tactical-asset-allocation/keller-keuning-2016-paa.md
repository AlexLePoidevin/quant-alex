# Protective Asset Allocation (PAA): A Simple Momentum-Based Alternative for Term Deposits

| | |
|---|---|
| **Authors** | Wouter J. Keller; Jan Willem Keuning |
| **Year** | 2016 |
| **Type** | Working paper — SSRN 2759734 |
| **Link** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2759734 |
| **BibTeX** | `keller2016paa` |
| **Status** | Rules verified |

## The rule that matters

PAA sets the defensive allocation from **breadth** — how many assets in the universe have
positive momentum — rather than from any single asset's trend. The bond fraction is

```
BF = (N − n) / (N − n₁),        n₁ = a·N/4
```

where `N` is the universe size, `n` the count of assets with positive momentum, and `a` the
protection factor (0, 1 or 2 for low, medium, high). At `N = 12` with high protection,
`n₁ = 6` and `BF = (12 − n)/6`. The portfolio holds `BF` in the safe asset and splits
`1 − BF` across the top-ranked risky assets.

**BF is bounded in [0, 1] by construction.** The numerator cannot go negative because `n`
counts a subset of `N`, and `BF ≥ 1` is capped at 100% safe. PAA therefore never levers and
never shorts. This is worth stating explicitly because implementations that hardcode the
constants while changing the universe size break that bound — see [[gpm]].

## Why it's in the library

Breadth is a different class of risk signal from everything else in this folder. A trend
rule, a volatility target and a drawdown trigger all read a price series and ask what that
asset is doing. Breadth asks how many assets are participating, which is a statement about
the cross-section. It also degrades continuously — the safe fraction moves in steps of
`1/(N − n₁)` as participation falls, rather than flipping between risk-on and risk-off.

## Links

- [[gpm]] — the strategy that adds correlation hedging to this breadth rule
- [[keller-keuning-2017-vaa]] — breadth momentum with a harsher response function
- [[keller-keuning-2018-daa]] — breadth measured on a separate "canary" universe
