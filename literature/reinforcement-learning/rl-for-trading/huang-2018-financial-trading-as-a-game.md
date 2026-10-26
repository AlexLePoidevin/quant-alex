# Financial Trading as a Game: A Deep Reinforcement Learning Approach

| | |
|---|---|
| **Author** | Chien-Yi Huang (Department of Applied Mathematics, National Chiao Tung University, Hsinchu, Taiwan) |
| **Year** | 2018 (v1, 8 July) |
| **Type** | Preprint, written up as a thesis — arXiv:1807.02787v1 [q-fin.TR], 15pp |
| **PDF** | `huang-2018-financial-trading-as-a-game.pdf` (in this folder) |
| **BibTeX** | `huang2018financial` |
| **Status** | Reference — short; read §2 (the MDP and action augmentation) and Tables 1–4, and treat the results as an illustration, not evidence |

## What it is

An early, much-cited attempt to trade real market data with a pure deep RL agent. A deep
recurrent Q-network ([[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]])
trades one FX pair at a time on 15-minute bars, with three changes to the standard recipe.

- **Data (§2.1).** Tick data from TrueFX for 12 major and cross pairs, January 2012 to
  December 2017, resampled to 15-minute OHLC bars plus tick volume.
- **The MDP (§2.2).** State is 198 numbers: sinusoidal minute / hour / weekday features,
  the 8 most recent log returns of price and tick volume for **all 12 pairs** (running
  96-bar z-score, clipped at 10), and a one-hot of the current position. Actions are target
  positions {−1, 0, +1}. Reward is the one-step log return of the account, with cost equal
  to a fixed spread times the change in position.
- **Action augmentation (§2.3).** The key idea. If you assume zero market impact and fills at
  the next open, the reward of every action is known once the bar closes: the P&L of −1 is
  the negative of +1, and 0 earns nothing. So the agent **updates the Q-values of all three
  actions at every step** and acts greedily, with no ε-greedy exploration, which in trading
  would just burn spread.
- **Training changes (§2.5).** A **small replay memory** (480 transitions, about five days)
  because recent data matter more; **long sampled sequences** (T = 96 bars) so the LSTM can
  learn hold-then-exit behaviour; and one update every T steps. The network is small:
  two 256-unit ELU layers, an LSTM and a 3-unit output, about 65k parameters.
- **Purely online learning (§2.5.2).** The author drops walk-forward train / test splits
  because they "overfit", and instead runs the agent once through the data, learning as it
  goes. Results (Table 1) are positive on all 12 pairs, with Sharpe ratios from 1.0 to 5.7
  and roughly 30,000 trades per pair, about one every four or five bars.
- **Cost sensitivity (Table 3).** Returns fall as the fixed spread widens from 0.08 to
  0.2 "basis points" (pips); two pairs turn negative at the widest setting. Action
  augmentation adds about 6 percentage points of annual return over ε-greedy (Table 4).

## Read with care

- **The cost model is far too kind.** A fixed spread of 0.08 pip, no slippage, no impact and
  fills at the next bar's open, applied to ~30,000 round trips per pair. At that turnover the
  result depends almost entirely on the cost assumption, and Table 3 shows the edge
  shrinking quickly as the spread grows. TrueFX quotes are indicative bank prices, not a
  tradeable book.
- **No clean out-of-sample test.** Hyperparameters came from a random search on the same
  2012–2017 data the agent is then evaluated on. Online learning is prequential, but the
  design choices were not.
- **Five seeds, 12 pairs, one period.** No significance tests, no deflation for the
  configurations tried, and no comparison to simple FX baselines such as short-horizon
  momentum or carry.
- **Weak benchmark, chosen after the fact.** Buy-and-hold or "sell-and-hold", whichever did
  better over the test period.
- **Units are mixed.** Net profit for JPY-quoted pairs is in yen, so the Table 1 columns are
  not comparable across pairs; use the percentage returns.
- **Risk-neutral reward.** The agent maximises expected log return; risk enters only through
  the author's suggestion of distributional RL as future work.

## Why it's in the library

**It shows the one trick that genuinely transfers to trading RL.** When your own actions do
not move the price, the counterfactual reward of every action is known. That removes the
exploration problem that makes RL so expensive in markets, and it turns the problem into
something close to supervised learning on per-action returns. Seeing this clearly is a good
reason to ask, for any "RL for trading" paper, what the RL part is adding beyond a
cost-aware classifier.

**Small, recent memory and long sequences** are the paper's answer to non-stationarity.
That is the same trade-off a ranking model faces when choosing training-window length and
retrain cadence: more history is more data but staler data. The continual-learning folder
treats the problem properly.

**A worked example of how cost assumptions make or break a high-turnover result.** The
spread table is the most useful exhibit in the paper: put any high-frequency backtest through
the same sweep before believing it.

## Links

- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] — the DRQN
  algorithm the agent is built on
- [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]]
  — how replay of recurrent sequences, burn-in and stale states should be handled
- [[bellemare-dabney-munos-2017-a-distributional-perspective-on-reinforcement-learning]] — the
  distributional RL the author proposes for risk-aware actions
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]] —
  the general version of the small-replay, non-stationary problem
- [[harvey-liu-zhu-2016]] — why a handful of seeds and pairs on one period is not evidence
- [[jeong-gu-2024-pro-trader-rl]] — a later, equity version of RL trading with similar
  evaluation problems
