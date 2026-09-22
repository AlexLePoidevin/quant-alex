# The "Rebalance Drag" Myth in Leveraged ETFs: What Advisors Need to Know

| | |
|---|---|
| **Author** | Return Stacked® Portfolio Solutions (no individual byline) |
| **Year** | 2025 (30 January) |
| **Type** | Practitioner note — advisor-facing, not peer reviewed |
| **BibTeX** | `returnstacked2025rebalance` |
| **Link** | https://www.returnstacked.com/the-rebalance-drag-myth-in-leveraged-etfs-what-advisors-need-to-know/ |
| **Status** | Read |

## Key takeaway

The myth is one of **attribution, not arithmetic**. Advisors attribute leveraged-ETF
underperformance to the daily-reset mechanism — the fund supposedly "buys high and sells
low" each afternoon. That mechanism is not the cause. The cause is **variance drain**: the
compounded return of a series sits at or below its arithmetic average, the gap widens with
volatility, and leverage amplifies volatility. It would happen with no rebalancing trade
at all.

The useful consequences they draw:

- Path dependency cuts both ways. Sustained trends with moderate volatility make daily-reset
  leverage *outperform* the naive multiple; chop makes it underperform.
- Concentrated single-asset leveraged ETFs suffer the most drain, because a single asset's
  volatility is what is being amplified.
- **Diversified** leveraged exposure mitigates it, because lowering portfolio `sigma^2` is
  the only lever that touches the drain term.
- Rebalancing itself generates excess return only when there are multiple imperfectly
  correlated assets. On one asset it is a mechanical necessity, not a source of return.

## Why it's here

**The best short statement of the misattribution, from the audience that most often makes
it.** Worth keeping precisely because it is practitioner-facing: it is the version of the
argument a reader is likely to have already encountered, correctly stated.

It also lands the diversification point independently of Booth & Fama — the only way to
reduce the drain is to reduce portfolio variance, which makes the diversification return
and variance drag the same fact read in opposite directions.

⚠️ **One level short of the real correction, and worth noting the gap.** Their framing —
"compounded return is always ≤ simple average return" — is the AM–GM inequality on a
*realised* sample, which is true but weaker than the distributional statement. It still
leaves a reader thinking something is being lost. The stronger version:
`E[S_T] = S_0 * exp(mu*T)` **exactly**, so no expected value is destroyed at all; the
`-sigma^2/2` is a mean-median gap. Use their piece for the attribution fix and the
diversification conclusion; take the framing from `../01-compounding`.

Also note the source: this is a sponsor with leveraged, diversified products to sell, and
the conclusion — *concentrated leverage bad, diversified leverage fine* — is the conclusion
its business favours. The reasoning happens to be sound. Check it anyway rather than
inheriting it.
