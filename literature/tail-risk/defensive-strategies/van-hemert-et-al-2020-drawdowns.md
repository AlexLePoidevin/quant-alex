# Drawdowns

| | |
|---|---|
| **Authors** | Otto Van Hemert, Mark Ganz, Campbell R. Harvey, Sandy Rattray, Eva Sanchez Martin, Darrel Yawitch (Man Group; Harvey also at Duke and NBER) |
| **Year** | 2020 (version dated 4 May 2020) |
| **Type** | Paper. SSRN 3583864, 19pp; published in *Journal of Portfolio Management* 46(8), 34–50 (2020). Simulation study plus bootstrapped market returns |
| **PDF** | Local copy only (SSRN download of a Man Group working paper; no open licence) |
| **BibTeX** | `vanhemert2020drawdowns` |
| **Status** | Reference: §2 ("drawdown Greeks"), §3 (manager replacement rules) and §5 (five takeaways) |

## What it is

A guide for allocators who fire or de-risk managers when a drawdown limit is hit: how
likely a given drawdown is, and when drawdown rules beat total-return rules.

- **How likely is a drawdown?** For a strategy with 10% volatility and a Sharpe ratio of
  0.5 observed over 10 years, the chance of a maximum drawdown of at least 1, 2, 3 and 4
  annual standard deviations (−10%, −20%, −30%, −40%) is 97.1%, 43.0%, 9.9% and 1.5%. So a
  perfectly good manager has close to even odds of a −20% drawdown in a decade.
- **What drives it ("drawdown Greeks").** Probability scales with drawdown measured in
  volatility units, not in percent; it rises with the evaluation horizon, falls with the
  Sharpe ratio, and rises with persistence in risk (autocorrelated returns or
  volatility clustering). Bootstrapping real market returns lifts the 2-sigma probability
  from 43% to about 55%. Occasional gap moves matter only if they are large relative to
  what markets usually show.
- **Firing rules.** With managers of fixed quality (a mix of Sharpe 0.5 and Sharpe 0
  managers), a total-return rule identifies the bad ones best. When good managers can turn
  bad (0.5% a month in the simulation, about 45% over ten years), drawdown rules catch the
  change faster.
- **De-risking rules.** Cutting risk by half after a drawdown can nudge the Sharpe ratio up
  but lowers the return. A stop-loss only adds return if expected returns after losses are
  negative, which requires negative-skill managers or strong autocorrelation.
- **Five takeaways.** Know the statistics before setting a limit; a drawdown limit
  discourages managers from taking risk in bursts and from gambling for resurrection;
  weigh the cost of firing a good manager against keeping a bad one; use total-return and
  drawdown rules together; and let the drawdown limit widen with time, since a constant
  limit is hit eventually even by a manager whose skill hasn't changed.

## Why it's in the library

**It makes drawdown limits quantitative.** Drawdown is the number investors act on, yet it
is path-dependent and noisy. The tables here turn "is a 20% drawdown alarming?" into a
probability that depends on volatility, Sharpe ratio and horizon.

**It frames de-risking as a hypothesis test.** Firing or cutting a manager trades off two
errors, and which rule is better depends on whether skill can decay. That is a useful lens
for any stop rule applied to a strategy, not only to external managers.

**Limits.** Mostly simulated normal returns with stylised manager pools; the conclusions
depend on the assumed migration rate from good to bad, which is not estimated from data.

## Links

- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — choosing stop-loss levels from a model rather than a backtest
- [[harvey-liu-zhu-2016]] — the multiple-testing view of judging strategies by their track record
- [[clare-et-al-2017-reducing-sequence-risk-using-trend-following-and-the-cape-ratio]] — what drawdowns cost a retiree drawing income, and a trend filter that cuts them
- [[dugan-greyserman-2019-the-impact-of-skew-on-performance-and-bias]] — how skew changes drawdown depth and length at the same Sharpe ratio
