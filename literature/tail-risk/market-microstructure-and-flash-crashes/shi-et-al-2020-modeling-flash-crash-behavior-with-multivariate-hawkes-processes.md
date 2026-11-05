# Modeling Flash Crash Behavior in a Stock Market using Multivariate Hawkes Processes

| | |
|---|---|
| **Authors** | Feng Shi (Amazon; UNC Chapel Hill), John Paul Broussard (Estonia Business School; Rutgers), G. Geoffrey Booth (The Citadel; Michigan State) |
| **Year** | 2020 (dated 26 June 2020) |
| **Type** | Working paper, SSRN 3425664. Millisecond trades in the 30 Dow stocks on 6 May 2010, from Nanex |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `shi2020flash` |
| **Status** | Reference: the method section (the excitation matrix and the rolling fit) and the results on network density, cross-reflexivity and modularity carry the paper |

## What it is

A description of how trading activity in the 30 Dow stocks fed on itself and on each other
before, during and after the 6 May 2010 Flash Crash.

- **The crash.** The official crash window runs 14:32 to 15:08. Every Dow stock hit its
  low between 14:45 and 14:48, Walmart first and Kraft last. Most fell about 10%, 3M about
  20%, and Procter & Gamble more than 35%.
- **The model.**
  - An event is a trade at a different price from the stock's previous trade.
  - Each stock's event rate is a baseline plus a sum over all 30 stocks' recent events,
    weighted by a 30 × 30 **excitation matrix**. Entry `a(s, s′)` is the expected number of
    stock-s events triggered by one event in stock s′.
  - The diagonal of the matrix is self-excitation; the off-diagonal entries are
    cross-excitation between stocks.
  - The model is fitted with Linderman and Adams's Bayesian network Hawkes model
    (`pyhawkes`). It uses a logistic-normal decay kernel, and a sparsity prior on which
    links exist.
  - It is fitted on 5-minute windows rolled every 5 seconds from 13:00 to 16:00, 2,161 fits
    in all.
- **Why not a covariance matrix.** The excitation matrix is directed, needs no synchronised
  sampling, and avoids the Epps effect: measured correlations shrink towards zero at very
  high sampling frequencies.
- **Results.**
  - *Activity.* About one million price-changing trades across the period. The average gap
    between trades fell from 22.1 ms before the crash to 2.8 ms at the bottom.
  - *Network.* The number of links fell with the market and recovered with it; the two
    series almost overlap. The strength of the remaining cross-links jumped at 14:32 and
    peaked a few minutes after prices bottomed. Activity was more intense but concentrated
    in fewer connections.
  - *Self vs cross.* Self-excitation normally dominates. During the crash it fell and
    cross-excitation rose until the two were close, then both returned to roughly
    pre-crash levels. The baseline (exogenous) rate was under 1% of the total throughout.
  - *Who drives whom.* Bank of America, ExxonMobil and JPMorgan had the largest influence
    on the other stocks. 3M, Alcoa and American Express were the most influenced. ExxonMobil
    was among the most influential on others and the least influenced by them. Across
    stocks, influence on others and influence received were negatively correlated.
  - *Clusters.* Modularity rose during the crash and peaked at the bottom, meaning the
    network split into tighter groups. Those groups did not match industry sectors:
    normalised mutual information was about 0.3 throughout. The authors read this as the
    crash spreading across sectors rather than within them.
  - *Direction.* Price rises made up 48.3% of price changes in the crash phase and 49.6%
    over the whole official window. The authors argue the difference from 50% is
    statistically significant only because the sample is huge, and is not economically
    meaningful.

## Why it's in the library

**It measures contagion directly, at the speed the crash happened.** Correlation breaks
down at millisecond horizons. A directed excitation matrix shows which names transmit
stress and which absorb it, and how that network rewires within minutes. The pattern is
fewer links that become much stronger, clustering that ignores sectors, and self-driven
activity giving way to cross-driven activity. It is a concrete picture of the
diversification that disappears in a crash.

**The Hawkes framing generalises.** Self- and cross-excitation is the standard way to
separate endogenous feedback from news, building on Filimonov and Sornette's
"reflexivity" index. The same model applies to order flow, volatility jumps or default
events.

**It is descriptive, and the authors say so.** It covers one afternoon in 30 stocks and
leaves out the E-mini future, where the crash is usually said to have started. The fitted
interactions are statistical associations, not causes. The suggestions for trading and
risk management in the conclusion are not tested.

## Links

- [[tee-ting-2019-cross-section-of-mini-flash-crashes]] — the many smaller crashes, one
  stock at a time, detected from trade data
- [[ang-chen-2002]] — correlations rising in down markets, the daily-frequency version of
  the same loss of diversification
- [[soros-2013]] — reflexivity, the idea the self- and cross-excitation terms quantify
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — feedback loops as the source of crash
  risk, argued at the level of strategies rather than trades
- [[merton-1976]] — the Poisson jump model that Hawkes processes extend by letting events
  trigger further events
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — the order-flow-toxicity account of 6 May 2010
