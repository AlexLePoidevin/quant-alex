# Determining Optimal Trading Rules without Backtesting

| | |
|---|---|
| **Authors** | Peter P. Carr (Morgan Stanley; Courant Institute, NYU); Marcos López de Prado (Guggenheim Partners; Lawrence Berkeley National Laboratory) |
| **Year** | 2014 (arXiv 1408.1159; first version October 2013, this version August 2014) |
| **Type** | Working paper (arXiv version, 39pp including 25 heat-map figures and Python code). Simulation only, no market data |
| **PDF** | `carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting.pdf` (arXiv version) |
| **BibTeX** | `carr2014optimal` |
| **Status** | Reference: §2 (the overfitting problem), §4 (the five-step procedure) and §5 (the conjecture). Filed here for want of a better fit; it is about trading-rule calibration, not volatility |

## What it is

A procedure for setting profit-taking and stop-loss levels without searching over them in
a backtest.

- **The problem.** A trading rule exits a position when the mark-to-market gain reaches a
  profit-taking level or the loss reaches a stop-loss level. Picking these two numbers by
  trying many pairs in a historical simulation overfits: the chosen pair fits the noise
  in the sample and is expected to do worse than the median pair out of sample. The paper
  is about exiting an existing position, not about when to enter.
- **The alternative.** Fit a model of the price process to the whole history once, then
  find the best rule by simulating that model. The paper uses a discrete
  Ornstein–Uhlenbeck process: each step moves the price part of the way towards a target
  level, plus noise. Three numbers describe it: the target, the speed of convergence
  (expressed as a half-life) and the noise size. These are estimated by one regression.
- **The procedure.** Build a 21×21 grid of profit-taking and stop-loss levels (0 to 10 in
  steps of 0.5, in units of the noise). Simulate 100,000 paths from the fitted process with
  a maximum holding period of 100 steps. Apply every rule to every path and compute its
  Sharpe ratio. Pick the best rule, or the best stop-loss for a given profit target, or
  the best profit target under a given maximum stop-loss.
- **Results with no expected profit (market-making).** With a 5-step half-life the best
  rules take small profits and tolerate losses 5 to 7 times larger, with Sharpe ratios
  around 3.2 per trade. As the half-life lengthens the process approaches a random walk
  and no rule stands out. On a random walk any "best" rule found by backtesting is pure
  overfitting.
- **Results with a positive expected profit (position-taking).** With a target of 10 and a
  half-life of 5, the best profit-taking level is around 6 with stop-losses from 4 to 10,
  and Sharpe ratios around 12. Longer half-lives move the optimum towards smaller profit
  targets and wider stops, and the best Sharpe ratio falls: about 9 at a half-life of 10,
  2.7 at 25, 0.8 at 50 and 0.32 at 100.
- **Negative expected profit** gives the mirror image: the problem is how to unwind a
  losing position at least cost.
- **The conjecture.** For an Ornstein–Uhlenbeck price there is a unique profit-taking and
  stop-loss pair that maximises the Sharpe ratio. The paper does not prove it and gives no
  closed form.

## Why it's in the library

**It is a direct answer to one kind of backtest overfitting.** Exit thresholds are free
parameters that can be tuned to individual trades. Fitting a process once and optimising
on synthetic paths removes the trial-and-error over history, and the heat maps show when
there is nothing to optimise at all.

**It shows how much the answer depends on mean reversion.** The same grid produces a clear
optimum when the half-life is short and nothing usable when it is long. Estimating the
half-life well matters more than the search.

**The model risk moves, it does not vanish.** The result is only as good as the fitted
process. If prices are not Ornstein–Uhlenbeck, or the parameters drift, the "optimal" rule
is optimal for the wrong world. The Sharpe ratios are per trade on simulated paths with no
costs, so they are not comparable with strategy Sharpe ratios.

## Links

- [[harvey-liu-zhu-2016]] — the multiple-testing problem in finance research, the same
  issue at the level of whole strategies
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — another trading rule derived from a model rather than a backtest search
- [[baur-et-al-2020-investing-in-gold-market-timing-or-buy-and-hold]] — what a data-snooping correction does to 4,000 backtested gold-timing rules
- [[lipton-lopez-de-prado-2020-three-quant-lessons-from-covid-19]] — the case against backtest-mined rules and all-weather strategies, after the COVID selloff
- [[van-hemert-et-al-2020-drawdowns]] — how likely a drawdown is, and when drawdown-based stop rules help
