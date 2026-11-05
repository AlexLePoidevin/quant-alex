# Dynamic Correlations at Different Time-Scales with Empirical Mode Decomposition

| | |
|---|---|
| **Authors** | Noemi Nava, Tiziana Di Matteo, Tomaso Aste (UCL; Systemic Risk Centre, LSE; King's College London) |
| **Year** | 2018 (arXiv preprint August 2017; published in *Physica A* 502, 2018, pp. 534–544) |
| **Type** | Paper, 19pp. 30-second data on the S&P 500, Mexico's IPC and the VIX, September 2013 – July 2014 (184 days) |
| **PDF** | `nava-et-al-2018-dynamic-correlations-at-different-time-scales-with-emd.pdf` (arXiv 1708.06586v1) |
| **BibTeX** | `nava2018emd` |
| **Status** | Reference: §2–3 (method) and §4.2 (full-sample results) carry the content |

## What it is

A way to measure how correlated two price series are at different time scales, and how that
changes during the day, using empirical mode decomposition (EMD).

- **The decomposition.** EMD splits a series into a few oscillating components (intrinsic
  mode functions, IMFs), each at its own time scale, plus a slow residual trend. The
  components are found from the data's own local maxima and minima by repeated
  "sifting", so no filter has to be chosen in advance, unlike wavelets. Each trading day
  of 780 thirty-second prices gives five IMFs, with periods of roughly 2, 4, 10, 20 and 44
  minutes.
- **Two correlation measures.** First, the Pearson correlation between every pair of
  components of the two series, giving a matrix of correlations across time scales.
  Second, lagged correlations between same-scale components over rolling windows, giving
  correlations that vary through the day and with the lead or lag.
- **Results.** Whole-sample return correlations are 0.21 (S&P 500 and IPC), −0.26
  (S&P 500 and VIX) and about −0.02 (IPC and VIX). Within the day, same-scale components
  carry most of the correlation, and it grows with the time scale: slow components are
  more strongly related than fast ones. The S&P 500 and VIX are negatively correlated at
  every scale and throughout the day. The one stable lead-lag pattern is that S&P 500
  moves are followed, about one minute later, by opposite moves in the VIX, at the three
  fastest scales.
- **The residual caution.** Correlations between the residual trends are high but
  meaningless, since two trending series always look correlated; the authors say not to
  read them.

## Why it's in the library

**It makes the point that a correlation has a time scale.** The same pair of assets can be
weakly related at minute scales and strongly related at hour scales. A risk model or a hedge
estimated on one horizon can be wrong on another, and EMD is a simple, data-driven way to
look.

**The empirical content is small.** One year of data, three indices, and the main finding (the
S&P 500 leads the VIX by about a minute) is unsurprising, since the VIX is computed from
S&P 500 option quotes that respond to index moves. There are no significance tests on the
lagged correlations, and the authors note that their averaging probably understates
correlations at the fastest scales. Read it as a method paper.

## Links

- [[mantegna-1999]] — correlation structure of stock returns and how it depends on the sampling interval
- [[laloux-et-al-1999]] — how much of an estimated correlation matrix is noise
- [[munnix-schafer-2011-copula-dependencies]] — dependence that changes with market conditions
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — another high-frequency view of how markets move together, during the 2010 flash crash
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the VIX is computed from S&P 500 option quotes, which explains why it lags the index
