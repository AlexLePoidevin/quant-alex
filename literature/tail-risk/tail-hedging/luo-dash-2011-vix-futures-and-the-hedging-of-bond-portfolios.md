# VIX Futures and the Hedging of Bond Portfolios

| | |
|---|---|
| **Authors** | Frank Luo and Srikant Dash (S&P Indices, Index Research & Design) |
| **Year** | 2011 (December 2011) |
| **Type** | Index provider research paper, 20pp. Data: December 2005 – August 2011 (municipal bonds from August 2007) |
| **PDF** | Local copy only (S&P copyright; redistribution prohibited) |
| **BibTeX** | `luo2011vixbonds` |
| **Status** | Reference: Exhibit 1 (co-movement), Exhibits 12–14 (worst days) and Exhibits 17, 19 and 21 (allocations) carry the results |

## What it is

S&P's study of whether its own S&P 500 VIX Short-Term Futures Index, a rolling position
in the first two VIX futures, is useful for hedging bond portfolios rather than equities.

- **It depends on the kind of bond.** Treasuries rise with equity volatility (a flight to
  quality): the VIX futures index rose 74% of the time when Treasuries were up at least one
  standard deviation. Municipal and investment-grade bonds show little relation.
  High-yield and especially emerging-market bonds move like equities: the index rose 81%
  of the time when EM bonds fell at least one standard deviation.
- **The worst 25 days.** On emerging-market bonds' 25 worst days (average −1.97%) the
  VIX futures index gained 6.6% on average and fell on only four of them. For high yield
  (−1.81%) it gained 2.3%, and for investment grade (−1.38%) only about 0.6%.
- **A static 5% allocation** lowered volatility and drawdowns for corporate and EM bond
  portfolios but also lowered returns, because of the roll cost.
- **A dynamic rule** — hold 5% in VIX futures for a month only when month-end spot VIX
  is at least 25, otherwise nothing — raised returns and lowered volatility and drawdowns
  in all three. EM bonds: 8.98% a year at 8.3% volatility and a 15.8% drawdown, against
  8.60% at 10.4% and 21.9% for the bonds alone. High yield: 6.43% against 5.93%, drawdown
  25.2% against 31.7%.

## Why it's in the library

**It extends the volatility-hedge idea beyond equities.** Credit and EM debt fail in the
same episodes as stocks, so equity volatility is a natural hedge for them; Treasuries are
already a volatility hedge and gain nothing.

**It is the index owner selling its index, on a short sample.** The VIX futures index was
launched in 2009, so its earlier history is back-filled. The sample is one crisis plus
2011. The VIX-above-25 rule and the 5% weight look chosen with hindsight, and costs are
ignored. The text and tables also disagree in places (the investment-grade worst-day
average is 0.66% in the text and 0.55% in the table).

## Links

- [[szado-2009-vix-futures-and-options-portfolio-diversification-during-the-2008-crisis]]
  — the same idea for equity and multi-asset portfolios in 2008
- [[fassas-2017-tracking-the-vix]] — how loosely VIX futures indices follow the spot VIX
- [[ang-chen-2002]] — why correlations jump in down markets, the reason risky bonds need a
  hedge at the same moment as stocks
- [[gehricke-zhang-2018-modeling-vxx]] — the roll cost that makes a permanent 5%
  allocation expensive
