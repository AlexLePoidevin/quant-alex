# Dead Cat Bounce: Demand Reversal Following the Bursting of a Bubble

| | |
|---|---|
| **Authors** | Kolja Johannsen (Warwick Business School) |
| **Year** | 2016 (dated 27 May 2016) |
| **Type** | Working paper, SSRN 2961304, 39pp. Theory only; no empirical test |
| **PDF** | Local copy only (SSRN download, no licence stated) |
| **BibTeX** | `johannsen2016deadcat` |
| **Status** | Reference: §3 (set-up and assumptions), Propositions 1–2 in §5 (the jump in demand) and Proposition 3 in §6 (when and how big the bounce is) carry the argument |

## What it is

A theory paper on the **dead cat bounce**, the sharp but temporary rally after a bubble bursts,
which the author calls the first theoretical treatment of it. The mechanism is loss-driven
re-entry by investors with cumulative prospect theory (CPT) preferences.

- **Set-up.** An investor buys a binary-outcome bubble asset (a small chance π < 0.5 of a high
  payoff, otherwise a low one) and forms a reference value Y₀, the price they expect it to reach.
  The bubble bursts, they sell at Yᵣ < Y₀ and book a loss relative to their reference. They
  cannot short. As the price falls further they reconsider.
- **Loss recovery drives demand.** Optimal demand splits into a *loss-recovery* part (what the
  investor must buy to have any chance of getting back to Y₀) and an investment part. The
  investor will buy even at a negative expected return, which they would not do without the
  prior loss.
- **Demand jumps (Proposition 1).** As the price falls, desired holdings jump from zero to a
  large position at a threshold price, rather than rising smoothly. In the benchmark numerical
  example the jump is to over 56% of what the investor held when the bubble burst.
- **Investors jump together (Proposition 2).** The price at which an investor re-enters does not
  depend on the size of their loss, their reference value or their wealth (while wealth is
  sufficient); only the amount does. Investors with similar beliefs about the asset therefore
  all re-enter at about the same price, so aggregate demand jumps.
- **The bounce (§6).** Risk-averse investors supply the asset expecting the CPT investors' demand
  to rise smoothly. When the actual demand jumps above what they anticipated, the price has to
  rise to clear the market. That rise is the dead cat bounce. A larger share of risk-averse
  investors shrinks the bounce; more optimism during the bubble (a higher reference value) makes
  a bounce more likely and larger; a larger share held by CPT investors at the peak delays it.

The motivating examples are the NASDAQ in 2000 (down over a third in two months, up 33% in the
next eight weeks, then down to a near-80% total loss) and currency and commodity crashes.

## Why it's in the library

It gives a mechanism for **bear market rallies** that needs no fundamental news and no
short-covering: a crowd of loss-averse investors who sold at a loss all try to win it back at
about the same price. That is a testable story behind the bear-rally state in the Maheu, McCurdy
and Song model, and a reason rallies early in a decline can be sharp and then fail.

It is a stylised model, not evidence. The asset has two outcomes, the timing of each re-entry
decision is exogenous, the paper lists its predictions (about the investor mix and the size of
the bubble) without testing them, and the numbers in the figures come from chosen parameters.
It also only models the bounce itself, not the second leg down.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — the bear-rally state this
  paper tries to explain, measured on 125 years of S&P 500 data
- [[schultz-2002-bear-market-investing-strategies]] — the practitioner account of the same
  rallies: oversold markets, short covering and the hope of getting back to cost
- [[soros-2013]] — boom–bust dynamics driven by participants' beliefs rather than fundamentals
- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — a different, liquidity-based reason
  sell-offs are followed by rebounds
- [[bashchenko-marchal-2020-deep-learning-for-asset-bubbles-detection]] — a statistical test for when a price is in a bubble, from the shape of its volatility
- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — three centuries of evidence on what follows a crash: large falls rebound, moderate ones persist
