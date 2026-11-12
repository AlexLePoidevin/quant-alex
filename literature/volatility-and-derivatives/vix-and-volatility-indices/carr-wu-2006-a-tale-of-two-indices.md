# A Tale of Two Indices

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg; NYU Courant), Liuren Wu (Baruch College, CUNY) |
| **Year** | 2006 (this version dated 22 December 2005) |
| **Type** | Journal article, *Journal of Derivatives* 13(3), Spring 2006, 13–29; 38pp working-paper version |
| **PDF** | Not hosted in this repository (author version of a journal article) |
| **Find it** | [doi.org/10.3905/jod.2006.616865](https://doi.org/10.3905/jod.2006.616865) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22A+Tale+of+Two+Indices%22+Carr) |
| **BibTeX** | `carr2006tale` |
| **Status** | Reference: §I–II (the old and new VIX and what each one measures) and §III.D (variance risk premium) are the core; §IV covers bounds for VIX futures |

## What it is

The standard explanation of what the VIX actually is, written when the CBOE switched
from the old index (now VXO) to the current one in 2003 and launched VIX futures in
2004. It adds a study of the new index from January 1990 to October 2005.

- **The old index (VXO).** An average of eight near-the-money Black–Scholes implied
  volatilities on S&P 100 options, interpolated to 22 trading days. It applied a
  "trading-day conversion" that inflates the number by about √(30/22), so it was not
  comparable with realised volatility. At best it approximates a one-month
  **volatility swap** rate (expected realised volatility).
- **The new index (VIX).** VIX² is a weighted sum of S&P 500 out-of-the-money put and
  call *prices* across all strikes, at the two nearest expiries, interpolated to 30
  days. That sum is the cost of the option strip that replicates a **variance swap**. So
  VIX² ≈ the risk-neutral expectation of realised variance over the next 30 days. The
  approximation is exact for continuous prices; jumps add a third-order error term.
- **Why the switch mattered.** VIX is the price of a linear portfolio of options, so it
  can be replicated and has a concrete meaning. That made futures and options on it
  possible, which never happened for VXO.
- **Empirical results, 1990–2005.**
  - VIX averaged about 5 volatility points above subsequent 30-day realised S&P 500
    volatility (t = 14.1).
  - Daily changes in VIX had a −0.78 correlation with same-day index returns. Past
    returns weakly predict VIX moves; VIX moves do not predict returns.
  - VIX rose into scheduled FOMC meetings and fell after them: 0.6 points on average
    from the day before to the day after (t = 4.1).
- **Variance risk premium.** The average of realised variance minus VIX² was −158.67 basis points of annualised variance (standard error 17.2), strongly
    significant.
  - In return terms, a long 30-day variance swap returned −40% on average, so a short
    position earned the reverse.
  - Shorting paid off in 89% of the 5,769 daily start dates. The best outcome was
    +89.5%; the worst was a loss of 242.4%, so the distribution is heavily negatively
    skewed, like selling insurance.
  - The CAPM gets only the sign right: the long-variance beta is strongly negative, but
    the intercept stays at about −36%. Variance risk is priced as a separate risk.
- **Predictability.** VIX predicts realised variance better than a GARCH(1,1) forecast,
  and GARCH adds nothing once VIX is included. Excess returns on variance swaps are
  not predictable from VIX, their own lags or index returns. The predictable part of
  volatility is already in the price.
- **VIX futures.** VIX futures must lie between two bounds that come from S&P options:
  - the forward volatility-swap rate (lower bound);
  - the forward variance-swap rate quoted in volatility points (upper bound).

  The gap between the bounds is the risk-neutral variance of future volatility.
  Together with the futures price, it gives the variance of future VIX, which is the
  input needed to price VIX options.

## Why it's in the library

**It is the reference for what the VIX measures.** VIX is a variance-swap rate quoted in
volatility points, not an average implied volatility and not a forecast of volatility.
It sits above realised volatility on average because of the variance risk premium and
because of convexity (Jensen's inequality between variance and volatility). Almost every
other VIX paper takes this as its starting point.

**It puts numbers on the premium for selling volatility.** A 40% average monthly excess
return and a 3.5 information ratio, alongside occasional losses of more than twice the
notional, make the volatility-selling trade concrete. These are the payoffs that tail
hedgers buy and that the short-volatility strategies in the tail-risk section collect.

**The bounds on VIX futures are worth knowing.** They explain why VIX futures sit below
the forward variance-swap level, and by how much: the gap is the variance of future
volatility.

**Mind the sample.** The data end in 2005, before VIX futures and options became heavily
traded, before 2008, and before the volatility ETN era. The sign of the premium has
held up since, but its size and the tails have changed.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the buyer's side of the same premium: what holding VIX futures and calls cost a 60/40 portfolio after 2006
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the short-volatility trade this paper measures, argued to have grown into a systemic risk
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — a later look at how the VIX calculation behaves, and whether its tails have fattened
- [[carr-lee-2007-realized-volatility-and-variance-options-via-swaps]] — pricing options on realised variance and on the VIX from variance and volatility swaps
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the replication formula behind the new VIX
- [[cboe-2021-vix-index-white-paper]] — the official VIX methodology, including weeklys, filtering and settlement
- [[chen-liu-li-2018-the-predictive-content-of-cboe-crude-oil-volatility-index]] — the VIX method applied to oil options, and whether it forecasts oil volatility
- [[doran-2020-volatility-as-an-asset-class-holding-vix-in-a-portfolio]] — which SPX options drive daily VIX changes, and using them to hedge
