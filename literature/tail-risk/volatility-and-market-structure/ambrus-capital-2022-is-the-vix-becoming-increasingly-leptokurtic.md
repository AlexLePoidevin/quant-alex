# Is the VIX Becoming Increasingly Leptokurtic Due to the Changing Derivatives Market?

| | |
|---|---|
| **Authors** | The Ambrus Group (Ambrus Capital); no individual author named |
| **Year** | 2022 (undated; written during 2022, after the S&P 500 had fallen more than 20% that year) |
| **Type** | Manager white paper, 6pp |
| **PDF** | Local copy only (manager material marked confidential, no licence) |
| **BibTeX** | `ambrus2022leptokurtic` |
| **Status** | Reference: short; the spot-vol beta section is the only part with data |

## What it is

A short note asking why the VIX stayed between about 20 and 33 in 2022 even though the
S&P 500 fell more than 20%. It argues that the VIX's distribution is becoming more
**fat-tailed** (leptokurtic): quiet most of the time, but liable to jump further in a
crash than it has before.

- **What VIX measures.** VIX is the 30-day implied volatility from SPX options with 23 to
  37 days to expiry, priced at the midpoint of the bid and ask. It can be read as the strike
  of a one-month variance swap. A VIX of 20 implies an expected move of about 4.6% over a
  month or 0.84% over a day, as mean absolute deviations.
- **Why 2022 was quiet.** Realised 30-day volatility of the S&P 500 peaked at 36 and stayed
  under 30 for most of the year. The decline was orderly, so a low VIX was the index
  working as designed, not a sign it was broken.
- **Why the tails may be getting fatter.** The paper gives three reasons:
  1. Short-dated SPX options, with expiries now every weekday, have grown sharply. The
     options VIX is computed from have also seen much more activity.
  2. Few option market makers absorb this flow. The paper says five main ones remain;
     its earlier paper said four. In a stampede for protection they widen spreads or step
     away, and the VIX's mid-price calculation then jumps. The analogy is a heavier
     bowling ball hitting fewer pins.
  3. Spot-vol beta, the expected change in implied volatility for a given move in the index, has been
     making higher highs and lower lows. A rolling 200-day estimate within VIX regimes
     has trended up. November–December 2021 saw one of the largest readings: the S&P 500
     fell less than 5% and volatility soared.
- **The forecast.** Using the old VXO, a 1987-style one-day drop has been estimated to put
  the VIX above 150, and the paper expects a repeat today could go higher still.
- **The pitch.** Deep out-of-the-money VIX-complex options are cheap relative to the
  middle of the volatility surface, so they make good tail hedges.

## Why it's in the library

**It explains what the VIX is, and why a low VIX in a falling market is not a puzzle.**
VIX prices expected short-term variance, not direction. A slow 20% decline with modest
daily moves should leave it subdued. That is a useful correction to the common reading of
VIX as a "fear gauge" that must rise whenever stocks fall.

**The fat-tail thesis is plausible but not tested here.** The paper notes that the
non-Friday options driving the growth are not in the VIX calculation. Its causal chain
(more short-dated activity → concentrated dealers → wider spreads in a panic → a bigger VIX
jump) is reasoned, not measured. The one data series, rolling spot-vol beta, is shown
without its construction or any test. No kurtosis of VIX is actually computed, despite the
title.

**The conclusion is the product.** "Tail options are underpriced relative to the belly"
is the claim a long-volatility manager needs, and no pricing evidence is given for it.

## Links

- [[cole-2017-volatility-and-the-alchemy-of-risk]] — why volatility can stay suppressed
  and then reprice violently, the same convexity argument at the level of the whole market
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] —
  what VIX futures and calls actually did as hedges, including the cost of carrying them
- [[merton-1976]] — jumps in the underlying, the formal reason implied volatility in the
  tails can be worth more than a smooth model says
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — the same firm on why fixed-rule VIX and put hedges bleed
- [[ambrus-capital-2023-dispelling-false-narratives-about-0dte-options]] — the same firm on short-dated options and intraday volatility
- [[avellaneda-et-al-2021-trading-signals-in-vix-futures]] — the VIX futures curve as a mean-reverting state: roll yield, contango drag and calendar trades
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the variance-swap replication the VIX formula is built on
- [[rolloos-arslan-2015-taylor-made-volatility-swaps]] — pricing a swap on volatility rather than variance: the strike sits at the zero-vanna point of the smile
