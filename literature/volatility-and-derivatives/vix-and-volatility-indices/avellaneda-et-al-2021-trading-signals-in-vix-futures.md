# Trading Signals in VIX Futures

| | |
|---|---|
| **Authors** | Marco Avellaneda (NYU), Thomas N. Li (NYU), Andrew Papanicolaou (NC State), Gaozhan Wang (Columbia) |
| **Year** | 2021 (arXiv 2103.02016v2, 9 March 2021) |
| **Type** | Preprint, 20pp |
| **PDF** | `avellaneda-et-al-2021-trading-signals-in-vix-futures.pdf` (arXiv copy) |
| **BibTeX** | `avellaneda2021trading` |
| **Status** | Reference: §2 (the VIX futures curve model and roll yield), §3 (the network and the cross-validation tables 3.2–3.5) carry the results |

## What it is

A method for trading VIX futures from the shape of their curve. It rests on the curve's
strong tendency to snap back to contango.

- **The curve as a state.** VIX futures are turned into constant-maturity futures (CMFs) at
  one to five months by interpolating adjacent contracts. Rolling one of these is what VIX
  ETNs such as VXX (one month) and VXZ (five months) do. Each rolling portfolio's return
  is the cash rate plus a *roll yield* plus the change in the CMF. The roll yield is
  usually negative because the curve is usually in contango, which is why these products
  decay. The state is spot VIX, the five log CMFs and the five roll yields: 11 numbers in
  all.
- **A model of how the curve moves.** A vector autoregression for that state, centred on
  the most likely (modal) curve rather than the mean, because the state has heavy tails.
  In its modal state spot VIX is about 12–14 and the long end 17–20, in contango.
- **Choosing a trade.** Each day pick one of five positions in the one-month (I¹) and
  five-month (I⁵) rolling portfolios:
  - flat;
  - short I¹ and long I⁵;
  - short I¹ and 2× long I⁵;
  - long I¹ and short I⁵;
  - long I¹ and 2× short I⁵.
  The choice maximises the next day's expected utility, either piece-wise linear (losses
  weighted 1.3×) or exponential. A five-layer feed-forward network (550 units per layer)
  learns each position's expected utility as a function of the curve. It is trained on
  paths simulated from the fitted VAR, not directly on history.
- **What it does.** In contango the typical signal is long the short end and short the
  long end. In backwardation it is short one-month and 2× long five-month. The authors
  say simpler static versions (a regression hedge ratio, or volatility-matched 1:2
  short/long) had large drawdowns at the worst times.
- **Results.**
  - Data: end-of-day curves from April 2008 to November 2020, split into ten
    cross-validation folds.
  - **Without costs (Tables 3.2–3.3):** fold Sharpe ratios run from about 1 to 11, with
    maximum drawdowns of 12–29%.
  - **With costs (Tables 3.4–3.5):** half the spread (at least 5 cents) or 20–40 bp. Here
    several folds lose money. At 40 bp most folds are negative, and drawdowns reach
    50–90%.
  - The authors' own summary: profits fall to "more pedestrian levels" with costs, and the
    drawdowns "would be difficult to manage in practice".
  - A live run from 28 December 2020 to 19 February 2021, retrained weekly, ended up about
    18%. It lost about 12% on 27 January 2021, the GameStop volatility spike.

## Why it's in the library

**It is a clear model of the VIX futures curve and of why long-volatility products bleed.**
The split of a rolling futures return into roll yield and the change in the
constant-maturity price explains the contango drag that makes holding long volatility so
costly. It also explains why curve shape, not the level of VIX, is where any short-term
predictability lies.

**It is a cautionary example of evaluating a trading model.**
- Its k-fold cross-validation trains on folds *after* the test fold, so the test is not
  truly out of sample. The authors acknowledge this.
- The network is trained on paths from a VAR estimated on the same history.
- The zero-cost rows of Tables 3.4–3.5 do not match Tables 3.2–3.3, and several folds turn
  from strongly positive to negative.
- Results are highly sensitive to costs that are realistic for VIX futures when the curve
  is in backwardation.

Read it for the curve model and the decision framing, not the performance numbers.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  same contango drag, measured as the cost of holding long VIX futures in a portfolio
- [[avellaneda-zhang-2010]] — the same first author on why leveraged and rolling ETFs
  drift away from their index, the mechanism behind VIX ETN decay
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — how VIX is built
  and how fat its tails have become, the distribution this strategy trades
