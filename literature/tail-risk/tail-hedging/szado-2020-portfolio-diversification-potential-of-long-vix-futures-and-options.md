# The Portfolio Diversification Potential of Long VIX Futures and Options Strategies

| | |
|---|---|
| **Authors** | Edward Szado (Providence College; INGARM) |
| **Year** | 2020 (dated 15 June 2020) |
| **Type** | Research paper funded by Cboe Global Markets, 54pp. Data run from February 2006 to December 2017, with the VXTH index followed to mid-2018 |
| **PDF** | Local copy only (Cboe-funded paper with no open licence) |
| **BibTeX** | `szado2020vix` |
| **Status** | Reference: §3 (2008 vs 2016), §4.1 (full period) and §5 (VIX calls vs SPX puts) carry the results |

## What it is

A backtest of what small long-volatility positions do to an ordinary portfolio, in a bad
year, a calm year and over the whole period since VIX options were listed.

- **The setup.** Two base portfolios: a 60/40 stock/bond mix and a hypothetical endowment
  (an actual endowment's published allocations applied to ten asset-class indexes). To
  each is added either 5% in long VIX futures (one-month, or three-month held for a month)
  or 1% in one-month VIX calls (at the money, or 25% out of the money). No transaction
  costs. The 5% futures weight is deliberately oversized to make the effect visible.
- **Why VIX looks like a hedge.** VIX's 90-day rolling correlation with the S&P 500
  stayed below −0.65 through the 2008 crisis, while most other assets' correlations with
  equities rose. It is most negative in the worst months for stocks.
- **Why it costs so much to hold.** VIX futures are usually in contango (the futures
  price sits above spot), so a long position loses as it rolls towards expiry. Over
  2006–2017 a 100% allocation to one-month VIX futures returned −55.8% a year with a
  −100% maximum drawdown; three-month futures returned −28.8% with −99.4%.
- **2008, the good year.** The 60/40 portfolio lost 20.9% (maximum drawdown −30.9%).
  With 5% in one-month futures it lost 13.4%; with 1% in 25%-OTM VIX calls it gained
  12.1%, though its volatility rose from 24.1% to 27.6%. The endowment improved from
  −38.6% to −9.8% with the same 1% of OTM calls.
- **2016, the bad year.** One-month VIX futures alone lost 77.9% (drawdown −87.5%). The
  60/40 portfolio's 8.4% return fell to 2.3% with 5% in futures and to −1.9% with 1% in
  OTM calls. Volatility and drawdowns fell, but the Sharpe ratio dropped in every case.
- **The whole period, 2006–2017.** Every long-VIX addition lowered the 60/40 return
  (7.5% to between 3.9% and 5.9%) and its Sharpe ratio (0.65 to between 0.32 and 0.64),
  while cutting the maximum drawdown from −34.8% to about −26% to −28%. The endowment
  results are similar.
- **VIX calls versus S&P 500 puts.** With the same 1% budget, VIX calls beat SPX puts over
  the full period: 60/40 plus 25%-OTM VIX calls returned 4.1% and plus ATM VIX calls
  3.9%, against −1.3% for 10%-OTM puts and 1.1% for 5%-OTM puts. Both kinds of hedge
  still left the portfolio below the unhedged 7.5%. The paper does not scale the puts and
  calls to equal protection.
- **A dynamic version, VXTH.** Cboe's VIX Tail Hedge index holds the S&P 500 and buys
  30-delta VIX calls each month, sized by the level of one-month VIX futures: nothing at
  15 or below, 1% between 15 and 30, 0.5% between 30 and 50, nothing above 50. From March
  2006 to December 2017 it returned 7.6% a year at 16.8% volatility with a −43.3% maximum
  drawdown, against −55% for the S&P 500. In February 2018, when spot VIX more than
  doubled in one day, VXTH fell 3.9%, the same as the S&P 500: it had no calls on because
  VIX had been low going in.
- **Efficient frontier.** Adding long VIX futures, calls and VIX futures spreads to the ten
  asset classes moves the ex-post efficient frontier up and to the left across its whole
  length. The paper stresses this is hindsight optimisation.

## Why it's in the library

**It puts numbers on the cost of carrying a hedge.** The same 1% of VIX calls that turned
2008 from a 21% loss into a 12% gain cut the 60/40 portfolio's long-run return from 7.5% to 4.1% a year.
Contango means a permanent long-volatility position is a steady drag. The protection is
real, and so is the price: it pays off only in a few crisis years and loses in all the
others.

**It shows that how you buy protection matters as much as whether you do.** Instrument
(VIX futures, VIX calls, index puts), moneyness and tenor change the result by several
percentage points a year on the same 1% budget. In this sample OTM VIX calls gave more
crash payoff per dollar than OTM index puts, because VIX rises more than in proportion
when stocks fall.

**The VXTH episode is a warning about timing rules.** A hedge sized by the current
volatility level is off exactly when calm markets break suddenly. February 2018 is the
case in point, and the paper says so directly.

**It is evidence about one period, sponsored by the exchange that lists the products.**
The results come from one 12-year sample, without trading costs. Almost none of the
alphas it reports are statistically significant. Treat it
as a careful description of what happened rather than a forecast.

## Links

- [[ang-chen-2002]] — correlations between stocks rise in down markets, which is why a
  hedge has to be something whose correlation stays negative in a crash
- [[donnelly-embrechts-2010-devil-is-in-the-tails]] — 2008 as the failure of a model that
  assumed diversification held in the tail
- [[merton-1976]] — jumps in prices, the risk that crash protection is bought against
- [[rockafellar-uryasev-2000]] — CVaR, the tail-loss measure a hedge is trying to reduce
- [[markowitz-1952]] — the efficient frontier that §7 extends with VIX exposure
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — why a crash can be bigger than the history suggests: volatility-sized strategies as one hidden short-volatility trade
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]] — why rule-based tail hedges bleed, and the case for trading them on price
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — how the VIX is computed and why it can stay low in an orderly decline, with a manager's case that its tails are getting fatter
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — the dealers' side of the hedge trade: SPX option spreads widen when market makers are short gamma, and dealers get flat in stressed markets
