# Market Manipulation, Bubbles, Corners, and Short Squeezes

| | |
|---|---|
| **Authors** | Robert A. Jarrow (Cornell University) |
| **Year** | 1992 |
| **Type** | Journal article, *Journal of Financial and Quantitative Analysis* 27(3), 311–336. Theory only; no data |
| **PDF** | Local copy only (ResearchGate scan of the JFQA article; publisher copyright) |
| **BibTeX** | `jarrow1992manipulation` |
| **Status** | Reference: §III (assumptions A1–A4), §IV (paper vs real wealth), Examples 2–3 in §V and Proposition 4 in §VI carry the argument |

## What it is

A model of when a trader big enough to move prices can make riskless profits from that
power alone, with no private information. Jarrow calls this a *market manipulation trading
strategy*: the large-trader version of an arbitrage.

- **The setup.** A discrete-time market with one stock and a money market fund. A single
  large trader (or a coalition acting together) has no information advantage, but the stock
  price is some function of the date, the state of the world and the whole history of the
  large trader's holdings. Prices rise when the large trader buys and fall when he sells
  (assumption A3), and, holding his position fixed, the market has no arbitrage for anyone
  (A4).
- **Paper wealth versus real wealth.** *Paper wealth* values the large trader's position at
  the prices his own holdings support. *Real wealth* values it at the price he would get
  after selling out. For a price taker the two are equal; for the large trader real wealth
  is strictly lower whenever he holds a position. A manipulation strategy is defined on
  real wealth: start from zero, end with non-negative real wealth for sure and positive
  real wealth with positive probability.
- **Price takers cannot manipulate, and neither can anyone in two periods.** With prices
  independent of the trader's holdings, the standard no-arbitrage result applies
  (Proposition 1). With only one trading round, any purchase is at too high a price and any
  sale at too low a price, so no manipulation strategy exists, not even a corner
  (Proposition 2).
- **Corner and squeeze.** With three periods, buying more than the total shares outstanding
  (a corner) and then calling in the shorts (a squeeze) lets the trader set the price the
  shorts must pay, because the normal price response no longer applies. Any price above a
  bound gives riskless profit (Example 2). The paper links this to the NYSE rule that lets
  its Board set a "fair price" in a squeeze, and gives the price that removes the profit.
- **Trend-and-sell.** Without a corner, a trader can still profit by buying to push the
  price up and then selling into the move, if prices respond less to his later trades than
  to his earlier ones. In a worked deterministic example the price goes from e (2.72) to
  e³ (20.09) and back down to about 18.17, and the trader makes money (Example 3). This is a
  finite-horizon bubble and crash created by one trader.
- **When manipulation is impossible.** If the price depends only on the trader's *current*
  holdings, not the path that got him there (A5), and he never holds more than the shares
  outstanding, there is no manipulation strategy (Proposition 4). Corners and squeezes
  remain possible regardless, which justifies position limits.
- **Bubbles without arbitrage.** Even when manipulation is ruled out, the trader can push
  *paper* wealth as high as he likes and generate a bubble and crash in observed prices
  (Example 4). So an econometrician who finds "arbitrage" in observed prices may be seeing
  paper wealth that could never be realised. With infinite horizons and a lower bound on
  wealth, nothing new appears (Proposition 5).

## Why it's in the library

It gives a clean definition of what a squeeze is and why it pays: once a position exceeds
the floating supply, the price stops being set by the market and starts being set by the
holder. The famous episodes it opens with (the 1869 gold corner, Northern Pacific in 1901,
Stutz Motor, the Hunt silver squeeze, soybeans, tin, Treasuries in 1986) all had the same
shape of a sharp rise and a collapse, and the model reproduces that shape from trading
alone.

The paper-versus-real-wealth distinction is the more general lesson. Marking a large
position at the last price overstates what it is worth, and backtests or empirical tests
that find "arbitrage" in prices moved by large trades may be finding nothing that could be
captured. It is pure theory with no data, and the price process is taken as given rather
than derived from an equilibrium.

## Links

- [[soros-2013]] — boom–bust dynamics where participants' actions move the prices they are
  reacting to
- [[sarkissian-2019-statistical-mechanics-of-price-stabilization-and-destabilization]] —
  large one-sided order imbalances turning ordinary repricing into a crash
- [[filippou-et-al-2022-no-max-pain-no-max-gain]] — evidence that positioning in listed
  options pulls stock prices towards particular strikes before expiry
- [[poitras-2012-what-happened-may-6-2010-anatomy-of-the-flash-crash]] — a crash in which
  selling pressure, not news, drove prices, compared with 1987
- [[fusari-jarrow-lamichhane-2025-testing-for-asset-price-bubbles-using-options-data]] — Jarrow's later work: testing for bubbles from the gap between call and put prices
