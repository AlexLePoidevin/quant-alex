# Momentum Turning Points

| | |
|---|---|
| **Authors** | Ashish Garg, Christian L. Goulding, Campbell R. Harvey, Michele G. Mazzoleni |
| **Year** | 2021 (slides dated January 2021) |
| **Type** | Slides, 33pp, for the paper SSRN 3489539 (2019). The paper was published as Goulding, Harvey and Mazzoleni, "Momentum turning points", *Journal of Financial Economics* 149(3), 378–406 (2023), without Garg. Monthly US value-weighted market excess returns 1969–2018, plus 11 equity markets 1980–2018 |
| **PDF** | Not hosted in this repository (presentation deck, no open licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Momentum+Turning+Points%22+Garg) for the title and authors |
| **BibTeX** | `garg2021turning` |
| **Status** | Reference: slides 4–9 (the four market phases and the speed blends), 12–16 (dynamic speed) and A19/A30 (phase transition probabilities) carry the argument |

## What it is

A talk on why time-series momentum on the stock market goes wrong around turning points,
and what to do about it. It times a single asset, the US market, going long or short on the
sign of its own past return.

- **Two speeds, four phases.** SLOW is the sign of the trailing 12-month return and FAST
  the sign of the trailing 1-month return. Crossing them gives four observable phases:
  - **Bull:** both up.
  - **Bear:** both down.
  - **Correction:** 12-month up, 1-month down.
  - **Rebound:** 12-month down, 1-month up.

  Over 1969–2018 the market spent 48% of months in Bull, 24% in Correction, 17% in Bear and
  11% in Rebound. Corrections and Rebounds, the turning points, make up 35% of months.
- **What follows each phase.** Bulls are followed by high average returns and low
  volatility, Bears by negative average returns and high volatility. Corrections are
  followed by mostly positive but very dispersed returns: 5 of the 10 worst and 4 of the 10
  best months of the 50 years came right after a Correction (October 1987 at −23% among
  them). Rebounds look like Bulls but with more volatility.
- **Blending speeds helps.** Positions that average SLOW and FAST, so that they go to zero
  when the two disagree, beat either pure speed. Sharpe ratios, 1969–2018:

  | Market | SLOW | ¼ fast | MED (½) | ¾ fast | FAST |
  |---|---|---|---|---|---|
  | 0.38 | 0.41 | 0.48 | 0.51 | 0.44 | 0.34 |

  The maximum drawdown goes from −54% for the market to −34% for MED. The authors derive a
  "disagreement multiplier", greater than one, that explains why a blend's Sharpe ratio
  beats the weighted average of its parts.
- **Volatility timing.** Beta and alpha split into a static part, a market-timing part and
  a volatility-timing part. The momentum position is a strong negative predictor of next
  month's volatility. That makes the strategy's beta lower than its average position would
  suggest, and the volatility-timing term contributes about a third of the alpha over
  1969–2018.
- **Dynamic speed.** Choose the speed separately after each phase. Speed only matters after
  Corrections and Rebounds, since in Bull and Bear the two signals agree. The fitted rule is
  to be slow after Corrections, which usually revert to Bull (61% of the time next month),
  and fast after Rebounds.
  - **Estimation:** speeds are estimated on data from 1926 up to the start of each
    evaluation window.
  - **50-year window:** the dynamic strategy's Sharpe ratio is 0.52, against 0.51 for the
    best static blend. It captures 92% of an ex-post "oracle" choice of speeds.
  - **Last 15 years (2004–2018):** 0.61 against 0.57 for the best static blend.
  - **International:** across 11 equity markets it beats every static speed in most of
    them.

## Why it's in the library

**It names the failure mode of trend rules.** A trend signal reads a mix of trend and noise,
so it places its worst bets just after the trend breaks. Splitting the cycle into four
phases makes that visible. It also gives a simple, testable prescription: slow down after
Corrections, speed up after Rebounds.

**It explains why blended look-backs work.** Averaging fast and slow signals is common
practice. The disagreement multiplier gives a reason: the blend steps out of the market
exactly in the phases where returns are most dispersed.

**It links momentum to volatility timing.** Part of the alpha of time-series momentum here
is the position shrinking before volatile months. That ties the trend literature to
volatility targeting.

**Limits.** This is one asset traded once a month. No trading costs are applied. The gains
of the dynamic rule over the best static blend are small: 0.52 against 0.51 over 50 years.
Over the last 15 years the alpha t-statistics are below 2 for every strategy (1.65 for the
dynamic one). These are slides, so the full robustness work is in the published paper.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a four-state statistical model with bear rallies and bull corrections, the model-based counterpart of these four observable phases
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the time-series momentum strategy whose turning-point problem this addresses
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — the optimal moving-average window in a bull/bear switching model, another answer to how fast a trend rule should be
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility targeting, which supplies part of the alpha found here
- [[butt-virk-2020-momentum-crashes-and-variations-to-market-liquidity]] — momentum's losses after down markets, the cross-sectional side of the same rebound problem
