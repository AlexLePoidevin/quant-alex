# Investigation of Flash Crash via Topological Data Analysis

| | |
|---|---|
| **Authors** | Wonse Kim; Younng-Jin Kim; Gihyun Lee; Woong Kook (Seoul National University) |
| **Year** | 2021 (arXiv preprint August 2020) |
| **Type** | Paper — *Topology and its Applications* 301, 107523 (2021). Preprint arXiv:2008.11558 [q-fin.ST], 11pp |
| **DOI** | [10.1016/j.topol.2020.107523](https://doi.org/10.1016/j.topol.2020.107523) |
| **PDF** | `kim-et-al-2021-investigation-of-flash-crash-via-topological-data-analysis.pdf` (in this folder; arXiv v1) |
| **BibTeX** | `kim2021flashtda` |
| **Status** | Reference — short paper; §3 (method) and §4 (one figure of results) are the content |

## What it is

A short application of topological data analysis (TDA) to the 6 May 2010 flash crash,
following Gidea and Katz's use of persistence landscapes on daily index data.

- **Data.** One-minute prices of S&P 500, Dow Jones and Nasdaq futures, 1 April to 28 May
  2010 (42 trading days). Each minute gives a point in 3D: the three one-minute log
  returns.
- **Persistence landscape.** For a sliding window of 50 minutes (50 points in 3D) they
  build the Vietoris–Rips filtration, record when loops and other homology classes are
  born and die as the distance scale grows, and summarise that as a persistence
  landscape. Its L1 norm gives one number per minute: roughly, how much persistent
  "shape" the recent cloud of joint returns has.
- **Anomaly score.** They track that number with an exponential moving average and
  variance and define Zₜ as the current value minus the previous EMA, divided by the
  square root of the previous EMVar.
- **Result.** Just before the crash's steep fall on 6 May, Zₜ reaches 28,034.92, far above
  its values at other times that day and on eight randomly chosen days before and after.
  The authors conclude the method can characterise and predict an intraday crash.

## Why it's in the library

**It is an example of the geometric tools elsewhere in the library pointed at a tail
event.** Persistence landscapes summarise the shape of a point cloud. Here the point
cloud is joint returns across three futures, and the idea is that the shape changes
before prices break.

**The evidence is thin, and it is worth saying why.** There is one event. The smoothing
parameter α for the EMA is not reported. A z-score of 28,000 means the trailing variance
was near zero, so the score is very sensitive to that denominator. There is no false-
alarm rate, no comparison with simpler measures (realised volatility, return dispersion
across the three contracts), and no lead time is measured: the "prediction" is a spike
just before the steepest part of a fall the paper dates from 2:32 p.m. Treat it as a
demonstration of the method, not as a tested crash signal.

**The three inputs are nearly the same asset.** S&P, Dow and Nasdaq futures move almost
together. Any change in their joint shape mostly reflects one contract briefly
decoupling from the others, which is what happened when liquidity broke. A wider and
more diverse set of assets would be a fairer test.

## Links

- [[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] — measuring the
  geometry of a point cloud, the general idea behind summarising returns by their shape
- [[flora-reno-2020-v-shapes]] — a statistical test for the same event (minimum
  V-statistic −24.6 on 6 May 2010), with bootstrap p-values and many more days tested
