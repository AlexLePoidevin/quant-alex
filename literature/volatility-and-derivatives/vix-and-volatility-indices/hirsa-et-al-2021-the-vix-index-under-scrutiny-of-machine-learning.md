# The VIX Index Under Scrutiny of Machine Learning Techniques and Neural Networks

| | |
|---|---|
| **Authors** | Ali Hirsa, Joerg Osterrieder, Branka Hadji Misheva, Wenxin Cao, Yiwen Fu, Hanze Sun, Kin Wai Wong (Columbia University; Zurich University of Applied Sciences) |
| **Year** | 2021 (arXiv 2102.02119v1, 3 February 2021) |
| **Type** | Working paper, 19pp. Data: end-of-day SPX option quotes January 2017 – March 2018, minute-by-minute quotes January – February 2018 |
| **PDF** | `hirsa-et-al-2021-the-vix-index-under-scrutiny-of-machine-learning.pdf` (arXiv version) |
| **BibTeX** | `hirsa2021vix` |
| **Status** | Reference: §3 (replication and subset selection) and §4 and §7 (neural networks for the VIX and VIX futures) carry the results |

## What it is

A follow-up to the same group's earlier VIX papers. It asks how few S&P 500 options are
needed to reproduce the VIX. The motivation is the manipulation debate: if a handful of
options drive the index, it is easier to move, and easier to trade against.

- **Replicating the official number.** Following the Cboe white paper (with a constant
  interest rate and no filtering algorithm), the authors rebuild the VIX from end-of-day
  quotes with a mean absolute error of 0.024 vol points (0.18%), and from minute data with
  0.064 (0.34%). Correlation with the published index is 0.999. The leftover error is
  mostly mismatched timestamps. On average the formula uses 258 puts and 109 calls each
  minute, because more out-of-the-money puts have a non-zero bid.
- **Using only the options nearest the money.** Keeping just the n options closest to
  the at-the-money strike (for n from 1 to 200), and rescaling the result to match the
  index's mean, still tracks the VIX closely; more options help. Re-picking the subset
  every minute works better than fixing it each morning.
- **A feed-forward network.** With 52 options per minute (every third strike) as inputs,
  two months of minute data, and a random 70/30 train/test split, a two-layer network
  reaches a test MSE of 0.095 (0.090 when theta and vega are added). Decision trees,
  random forests and support vector regression score 0.34 to 1.19.
- **LSTMs for the VIX and VIX futures.** Recurrent networks fitted on the same inputs get
  MSEs of 3.0 to 17.9 for the VIX and 4.4 to 28.9 for the front VIX future, with the best
  architecture changing between the two targets.

## Why it's in the library

**It quantifies how concentrated the VIX is.** Several hundred options enter the formula,
but a small near-the-money subset reproduces most of its movement. That is the mechanism
behind both the manipulation worries and the "replicate the VIX cheaply" trade, and it
connects to the settlement and bias problems in the Osterrieder et al. note.

**The machine-learning results are weak evidence.** The neural-network test uses a random
split of consecutive minutes, so neighbouring, nearly identical observations sit in both
the training and test sets. The networks are mostly learning a known, nearly linear
formula. The LSTM errors are large next to the simple subset method, and no costs or
trading test back the arbitrage claim. Read §3 for the useful part.

## Links

- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — the earlier
  paper from the same group on how the VIX is computed, where it is biased and how it
  settles
- [[kucharczyk-et-al-2018-neural-networks-and-arbitrage-in-the-vix]] — the first version of
  the neural-network idea, predicting minute-ahead VIX moves from ten options
- [[carr-wu-2006-a-tale-of-two-indices]] — why the VIX is a variance-swap rate built from an
  option strip
- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  1/K² replication formula that the VIX implements
