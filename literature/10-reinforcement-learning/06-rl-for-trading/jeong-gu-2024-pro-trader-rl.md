# Pro Trader RL: Reinforcement learning framework for generating trading knowledge by mimicking the decision-making patterns of professional traders

| | |
|---|---|
| **Authors** | Da Woon Jeong (Department of Computer Engineering, Sejong University, Seoul); Yeong Hyeon Gu (Department of Artificial Intelligence and Data Science, Sejong University) |
| **Year** | 2024 |
| **Type** | Paper — *Expert Systems with Applications* 254, 124465 (doi:10.1016/j.eswa.2024.124465). Open access, CC BY-NC-ND 4.0. 18pp |
| **PDF** | `jeong-gu-2024-pro-trader-rl.pdf` (in this folder) |
| **BibTeX** | `jeong2024pro` |
| **Status** | Reference — read §3 for the module design and §4.2–4.3 for the backtest; read the results as a case study in what to check |

## What it is

A modular stock-trading system that splits a trader's job into separate parts: a rule
generates candidate entries, one PPO agent decides which candidates to buy, a second decides
when to sell, and fixed stop-loss rules override both. It reports very large out-of-sample
returns on US stocks.

- **Universe and data (§3.1.1).** Daily Yahoo Finance data for the stocks in the S&P 500,
  MidCap 400 and SmallCap 600, keeping those with at least two years of history: **1,465
  stocks**. Training runs from 25 February 2005 to 15 October 2017; testing from 16 October
  2017 to 15 October 2023 (§4.3).
- **Candidate generator (§3.1.2).** A 20-day **Donchian channel breakout**: a buy signal
  when the high exceeds the prior 20-day high. Only buy-signal days enter the RL problems.
- **Features (§3.1.3–3.1.4).** 69 variables: OHLC and Heikin-Ashi candles, ATR, SuperTrend,
  MFI, RSI, Donchian bands, Dow Jones ATR ratios, relative-strength measures against the
  index, and breadth counts (how many stocks rose or fell). Price variables are normalised by
  the Donchian upper band; others by ratios or min-max across their own lags.
- **Buy Knowledge RL (§3.2).** A PPO agent on each buy signal outputs two probabilities:
  "the trade will return at least 10%" or not. Reward is +1 for a correct call, 0 otherwise,
  with classes balanced in training. In test mode, **at most 10 stocks a day** are bought, in
  order of predicted probability. In effect this is a **binary classifier trained with a
  policy-gradient method**.
- **Sell Knowledge RL (§3.3).** A second PPO agent sees each of the 120 days after a
  purchase and outputs sell / hold probabilities. Training uses only trades that reached
  +10%; the reward ranks the days by return, so selling near the peak earns up to +2. In test
  mode the agent sells when sell minus hold probability exceeds 0.85.
- **Stop-loss rules (§3.4).** Exit at the next open if the return "falls below 10%" (read
  as a 10% loss; the text is ambiguous), or at the open of day 21 if 20 days pass with the
  return at or below 10%.
- **Backtest (§4.2–4.3).** $10,000 start, at most 10 positions at 10% each, 0.1% fee per
  transaction, default Stable-Baselines3 PPO settings. Reported test results: **65.3% a
  year, Sharpe 4.58, maximum drawdown 8.4%**, against 6.7% a year for the Dow Jones index and
  negative returns for plain PPO, DQN and A2C agents trading buy / hold / sell.

## Read with care

- **Survivorship bias is built in.** The universe is today's S&P 1500 from Yahoo Finance,
  filtered for two years of history, then traded back to 2005. Stocks that were delisted,
  went bankrupt or fell out of the indices are mostly missing. For a long-only breakout
  strategy concentrated in 10 names, mostly mid and small caps, this alone can produce large
  excess returns.
- **The breadth features inherit the same bias.** "Up Stock" and "Down Stock" counts are
  computed over the survivor universe.
- **The comparison is not like for like.** The benchmark is the Dow Jones price index (30
  large caps, no dividends) against a 10-stock small- and mid-cap book. There is no
  equal-weight or size-matched benchmark and no factor regression, so beta to small caps and
  momentum is not separated from skill.
- **Costs and capacity.** 0.1% per side, no slippage, opening-price fills in small caps,
  and a $10k book. No turnover is reported.
- **One test period, sliced afterwards.** The sideways / bear / bull sub-periods of
  Experiment 2 are chosen inside the same 2017–2023 window. Experiment 3 compares against
  numbers quoted from other papers on different data and periods.
- **The baselines are weak.** The generic RL agents lose money, and supervised baselines
  are paired with the plain Donchian sell rule rather than the paper's own exit logic.
  The gain could come from the exit rules as much as from RL.
- **Sharpe 4.6 on a long-only 10-stock daily book over six years is implausible** for a
  price-only signal. Treat it as a prompt to look for the cause, starting with the universe.

## Why it's in the library

**A clear example of a common pattern: RL that is really classification.** The buy agent
predicts a binary label one step ahead; PPO adds nothing a gradient-boosted classifier or a
ranker could not do, and costs much more to train (about 122 and 195 hours here). When a
paper calls its model RL, check whether the actions change the future state. Here they do
not.

**The decomposition itself is worth keeping.** Candidate generation, entry scoring, exit
timing and risk overrides as separate modules is how many practical systems are built. For a
cross-sectional ranker, the entry-scoring piece maps onto ranking the candidate list and
taking the top K, and the exit question maps onto holding period and rebalance rules.

**It is a useful audit exercise.** Nearly every item on a backtest checklist applies:
survivorship, benchmark choice, costs, sub-period selection, cross-paper comparisons. Reading
it with that list in hand is good practice.

## Links

- [[schulman-et-al-2015-trust-region-policy-optimization]] — the trust-region idea that PPO
  simplifies
- [[huang-2018-financial-trading-as-a-game]] — an earlier RL trading agent with similar
  evaluation gaps
- [[carhart-1997]] — momentum as a factor; a breakout strategy needs to be measured against it
- [[harvey-liu-zhu-2016]] — the bar a new trading rule has to clear
- [[mclean-pontiff-2016]] — why published anomaly returns shrink out of sample
