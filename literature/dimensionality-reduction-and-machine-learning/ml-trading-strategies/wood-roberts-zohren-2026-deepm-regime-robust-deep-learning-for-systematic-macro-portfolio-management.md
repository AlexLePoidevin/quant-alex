# DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management

| | |
|---|---|
| **Authors** | Kieran Wood (Oxford-Man Institute and Machine Learning Research Group, University of Oxford); Stephen J. Roberts, Stefan Zohren (Machine Learning Research Group, University of Oxford) |
| **Year** | 2026 (v1, 9 January) |
| **Type** | Preprint — arXiv:2601.05975v1 [q-fin.TR], 35pp including appendices |
| **PDF** | `wood-roberts-zohren-2026-deepm-regime-robust-deep-learning-for-systematic-macro-portfolio-management.pdf` (in this folder) |
| **BibTeX** | `wood2026deepm` |
| **Status** | Reference — read §1.1, §3, §5 and §6.1.4–7; the appendices hold the cost table and the EVaR derivation |

## What it is

An end-to-end deep portfolio model for 50 futures and FX contracts. Instead of forecasting
returns and then optimising, the network outputs positions and is trained directly on the
**net-of-cost, risk-adjusted P&L** of the portfolio. Most of the paper is about the
inductive biases and the loss that make this stable.

- **Three practical problems (§1.1).** Asynchronous market closes (using same-day data from
  a market that has not closed yet is a quiet look-ahead); costs that depend on the path of
  positions; and objectives that look good on average while hiding a few disastrous windows.
- **Architecture (§4, Fig. 1).** A per-asset temporal encoder (variable selection network,
  LSTM, temporal attention, as in the Momentum Transformer), then **cross-asset attention on
  data lagged one day** (the "Directed Delay"), then a graph network over a **fixed,
  hand-built macro graph** (asset-class cliques, supply-chain links, carry and inflation
  channels, regional equity / bond / currency triangles). Outputs go through tanh to risk
  weights, then volatility targeting.
- **Inputs (§3.3).** Daily closes only: volatility-normalised returns over 1, 21, 63 and
  252 days, multi-scale MACD, price z-scores, with a rolling median ± 5 MAD clip. No carry
  or macro data.
- **Costs (§3.5, App. A.3).** Per-asset linear costs from a tick-size floor times a
  liquidity multiplier, from 0.25 bp (equity index futures) to 15 bp (orange juice).
- **Objective (§5.1).** Minus the pooled Sharpe ratio of net returns, minus λ times a
  **SoftMin of per-window Sharpe ratios** over quarterly blocks. The SoftMin is shown to be
  the dual form of **entropic value-at-risk**: training against an adversary that reweights
  history towards the worst windows.
- **Cost scaling and ensembling (§5.2, App. B).** Turnover cost is convex in positions, so
  averaging K models trades less than the average model (Jensen). The paper argues that the
  best training cost multiplier γ is therefore below 1 for an ensemble, and uses γ = 0.5.
- **Protocol (§6.1.4).** Expanding-window walk-forward from 1990: retrain every 5 years,
  90/10 chronological train / validation split, test on the next 5 years. 50 seeds per
  model; the final signal averages the top 25 by validation Sharpe. Out-of-sample 2010–2025.
- **Results (§7, Tables 1–2), rescaled to 10% volatility.** **Net Sharpe 0.93** (gross
  1.29), HAC t-statistic 3.69, average holding period 7.1 days. Passive equal-risk long 0.50,
  12-month time-series momentum 0.45, Momentum Transformer with the same cost training 0.66.
  Information ratio against passive 0.44 with t = 1.85. 2020–2025 net Sharpe 0.79 (0.97 with
  MACD features).
- **Ablations (§7.2).** Pooled Sharpe without SoftMin: 0.68. Cross-attention without the
  graph: 0.79. Graph without cross-attention: 0.84. Same-day "cascading" data instead of the
  one-day lag: 0.84. Zero-cost training: 0.56; full-cost training: 0.70. Best single seed
  0.72 against 0.93 for the top-10 or larger ensembles.

## Read with care

- **Design choices are judged on the test period.** All ablations, the SoftMin temperature
  comparison and the ensemble sizes are reported on 2010–2025. The baseline configuration is
  "the best-performing" one, so the 0.93 is partly selected on the data it is reported on.
  A deflated Sharpe or a final untouched period would be needed to quote it cleanly.
- **The edge over passive is marginal.** IR 0.44 with t = 1.85 (1.93 for the 100-seed
  ensemble). The strong t of 3.69 is for the strategy's own return, which includes the risk
  premia the passive book also earns.
- **Hyperparameters are reported inconsistently.** §6.1.4 gives τ = 1/5, λ = 0.1; §7.1
  gives τ = 0.5, λ = 1/5. The temperature discussion implies τ = 0.2.
- **The macro graph is hand-built by people who know the history.** It is fixed ex ante,
  but which links to include is itself a modelling choice made with hindsight.
- **Costs are linear and capacity is not modelled.** The cost table is reasonable for
  liquid futures, but there is no impact term, so results say nothing about size.
- **Ex-post volatility rescaling** to 10% puts strategies on one scale but uses the
  realised volatility of the test period.
- **Continuous futures from a commercial vendor;** the roll and back-adjustment method is
  not described.

## Why it's in the library

**It is the strongest argument in this folder for aligning the loss with the portfolio.**
A ranking loss is still a proxy; here the network is trained on the thing the investor gets.
The paper shows the costs of doing so naively (Sharpe ratios that collapse into
low-volatility "inertia") and two fixes worth borrowing for any ranker: a worst-window
penalty across time blocks, and evaluating on several regimes at once.

**Three transferable findings for a daily long/short ranker.** (1) Training with a reduced
cost penalty and then ensembling seeds beat training with the full cost, because averaging
cancels idiosyncratic trades; this is a cheap experiment to run on any model that is
retrained in windows. (2) **Seed ensembles mattered more than many architecture choices**
(0.72 to 0.93). (3) Strictly lagged cross-asset information beat fresher same-day data, a
reminder that intraday or asynchronous inputs need to show they help before they are used.

**The "ragged filtration" point applies beyond futures.** Any feature built from markets or
data feeds that close at different times can leak in a backtest. The paper's fix, lag every
cross-asset input by one decision step, is crude but safe.

## Links

- [[rockafellar-uryasev-2000]] — CVaR optimisation, the classical relative of the EVaR penalty
- [[michaud-1989]] — the error-maximisation problem that motivates end-to-end learning
- [[ledoit-wolf-2004]] — the shrinkage covariance used by the two-stage baselines
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — another approach to
  learning under regime change
- [[harvey-liu-zhu-2016]] — the multiple-testing bar for a strategy chosen among many variants
