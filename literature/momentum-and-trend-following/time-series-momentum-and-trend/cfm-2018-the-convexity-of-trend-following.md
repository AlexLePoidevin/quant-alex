# The Convexity of Trend Following: Protecting your assets but perhaps not as much as you would like!

| | |
|---|---|
| **Authors** | Capital Fund Management (CFM), no individual authors named |
| **Year** | 2018 (February) |
| **Type** | Manager technical note, 8pp. Simulated random walks, S&P 500 E-mini and wheat futures (about 35 years each), and the SG CTA index |
| **PDF** | Not hosted in this repository (CFM marketing note with disclaimers, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Convexity+of+Trend+Following%3A+Protecting+your+assets+but+perhaps+not+as+much+as+you+would+like%21%22+Management) for the title and authors |
| **BibTeX** | `cfm2018convexity` |
| **Status** | Reference: the derivation and Equation 1 (pp. 2–3) and the SG CTA index check (Figure 6) carry the argument |

## What it is

A short note from a large systematic manager showing that a trend-following rule is
mechanically convex in the asset it trades, and that the steps CTAs take to make trend
following a better product weaken that convexity.

- **The identity.** With a position equal to the price change since a start date, the
  total profit over a period equals half of (the squared total move) minus (the sum of
  squared daily moves). So a trend follower makes money when variance measured over the
  trend's timescale exceeds the sum of daily variances, that is when moves persist, and
  loses otherwise. For a pure random walk the two cancel on average.
- **The EMA version.** With an exponential moving average signal of timescale τ, an EMA
  of the trend P&L is proportional to the squared EMA of returns minus the EMA of squared
  daily returns (Equation 1). Plotting smoothed trend P&L against smoothed returns gives a
  U-shaped parabola: convexity. It holds exactly even for a random walk, which has zero
  expected profit; the convexity is a property of the rule, not evidence of predictability.
- **Real data.** The same U-shape appears for trend on the S&P 500 and on wheat, each
  relative to its own market. Volatility scaling keeps the subtracted daily-variance term
  roughly constant, which the note calls essential.
- **What erodes it.** Three standard CTA choices improve risk-adjusted returns but blur
  the convexity to equities:
  - trading many markets, so trend P&L on wheat adds noise to the S&P 500 parabola (the
    parabola survives only as a lower envelope);
  - capping position size, or trading only the sign of the signal, which trims the fat
    right tail;
  - smoothing the signal with a second average to cut trading costs, which delays entry
    after a sudden move.
- **The industry check.** Using a trend timescale of about six months, which a previous
  CFM paper found best reproduces the SG CTA index (about 85% correlation), the
  smoothed SG CTA index against the smoothed S&P 500 fits a parabola with R² of 0.18. The
  usual check, monthly CTA returns against monthly S&P 500 returns, gives R² of 0.02.
- **The conclusion.** Trend following is convex but weakly so once implemented as a
  diversified, risk-controlled product. CFM's view is that it should be held for its
  statistically robust returns, with crisis protection a bonus. Puts, by contrast, are
  described as protection with a systematically negative return.

## Why it's in the library

**It explains where trend following's "crisis alpha" comes from without options.**
Fung and Hsieh model trend followers as owners of lookback straddles; this note derives
the convexity directly from the P&L of a moving-average rule. The two views agree: the
payoff depends on the size of persistent moves, in either direction.

**It is honest about how much protection a CTA gives.** Diversification, position caps and
signal smoothing all trade convexity for Sharpe ratio. The note's own advice is that an investor who
wants trend as an equity hedge should trend-follow equities directly, accepting a lower
Sharpe ratio than a diversified programme. The R² of 0.18 for the industry index is the measured amount of equity
convexity that survives.

**The timescale matters.** The convexity is with respect to moves over the trend's own
horizon. A crash faster than the signal's timescale, or one that reverses quickly, is not
captured; the note's EMA-smoothing point says the same about entry delays.

**It is a manager's note.** The derivation is standard and checkable; the empirical part
uses CFM's own earlier papers and the SG CTA index, without tests of significance, and
the conclusion favours holding trend following, which CFM sells. Note that the printed
summation formula on page 3 has a typo (the position should be the price change since the
start date); the identity it leads to is correct.

## Links

- [[fung-hsieh-2001-the-risk-in-hedge-fund-strategies-trend-followers]] — the option-based view of the same convexity: trend followers as lookback-straddle owners
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the time-series momentum strategy and its smile against the market
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — trend against puts as crisis protection, decade by decade
- [[sepp-2018-trend-following-strategies-for-tail-risk-hedging-and-alpha-generation]] — trend-following rules analysed as tail-risk hedges
- [[mcquinn-thapar-villalon-2021-portfolio-protection-its-a-long-term-story]] — protection over long bad periods rather than single crashes
