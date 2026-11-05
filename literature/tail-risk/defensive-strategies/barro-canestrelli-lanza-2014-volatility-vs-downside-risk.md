# Volatility vs. Downside Risk: Optimally Protecting Against Drawdowns and Maintaining Portfolio Performance

| | |
|---|---|
| **Authors** | Diana Barro, Elio Canestrelli, Fabio Lanza (Ca' Foscari University of Venice) |
| **Year** | 2014 |
| **Type** | Working paper, Department of Economics, Ca' Foscari, No. 18/WP/2014 (SSRN 2521007), 28pp. Weekly S&P 500 and sector index data, 2000–2013 |
| **PDF** | Local copy only (working paper, no open licence) |
| **BibTeX** | `barro2014volatility` |
| **Status** | Reference: §2 (the model), §3.3–3.5 (volatility control, tail control, joint effects) and Table 2 carry the results |

## What it is

A multi-period portfolio optimisation that puts volatility control and tail-loss control
into the same model, compared with a simple rule-based volatility-target strategy.

- **The rule-based benchmark.** A volatility-target strategy holds the S&P 500 at weight
  w = min(target volatility / trailing realised volatility, 1) and the rest in cash, so it
  never levers up. With 5–10 week trailing volatility and targets of 5%, 10% or 15%, it
  cuts risk but still follows the index down. A 25% target is almost always fully
  invested, since the index's own volatility over 2000–2013 was about 19%.
- **The optimised model.** A stochastic programme on a scenario tree (bootstrapped weekly
  returns) tracks the S&P 500 using the sector indexes. On top of the tracking goal it can
  switch on (a) a penalty or a hard limit on the portfolio's variability at each node of
  the tree ("local volatility control") and (b) a penalty on falling below a loss
  threshold (tail-risk control). Each control is a separate layer that can be turned up or
  down.
- **The test.** Out of sample, 50 weeks at a time with weekly rebalancing, in three
  windows: October 2005 – September 2006, September 2007 – August 2008, and August 2009 –
  July 2010.
- **Results.** All the controls cut volatility and the left tail compared with the index,
  at the cost of upside. In the falling 2007–08 window the index lost on average 0.23% a
  week; the tightly controlled optimised portfolios had slightly positive mean returns and
  were the only ones with positive Sharpe ratios. In the two rising windows they gave up
  return but still had higher weekly Sharpe ratios than the index (for example 0.45
  against 0.13 in the first window, for the hard volatility limit). The rule-based target
  improved on the index only modestly. Adding tail control on top of volatility control
  gave the best protection for a given loss of upside, which the authors measure with
  Omega and one-sided performance ratios.

## Why it's in the library

**It frames volatility targeting as a blunt tool for tail risk.** Scaling exposure by
trailing volatility cuts both tails, so it gives up upside to reduce downside. Controlling
losses below a threshold directly lets the portfolio keep more of the right tail.

**It is a useful contrast with the Man Group volatility-targeting evidence.** Those papers
test simple scaling rules across asset classes and decades; this one shows what an
optimiser adds on top, in a few stress windows.

**Limits.** Three 50-week windows are very little evidence, and the Sharpe ratios are
weekly and unannualised. No transaction costs, although the optimised portfolios
rebalance across sectors every week. Table 2 also shows the index with negative excess
kurtosis in the first window and lower kurtosis than the 5% target strategy, which sits
awkwardly with the text's claim that the index has the fattest tails. A later published
paper on the same theme (Barro, Canestrelli and Consigli, Computational Management Science
2019) has a different co-author and is not this paper.

## Links

- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — volatility scaling tested across asset classes since 1926
- [[mcgee-2021-can-market-regimes-really-be-timed-with-historical-volatility]] — a sceptical replication of volatility-managed portfolios
- [[rockafellar-uryasev-2000]] — optimising directly on the tail with CVaR
- [[van-hemert-et-al-2020-drawdowns]] — what drawdowns to expect for a given volatility and Sharpe ratio
