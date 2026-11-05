# Neural Networks and Arbitrage in the VIX: A Deep Learning Approach for the VIX

| | |
|---|---|
| **Authors** | Daniel Kucharczyk, Joerg Osterrieder, Silas Rudolf, Daniel Wittwer (ZHAW Winterthur) |
| **Year** | 2018 (SSRN 3305686) |
| **Type** | Paper, 22pp. Intraday SPX option quotes and VIX, January–February 2018 |
| **PDF** | Local copy only (SSRN download with no open licence) |
| **BibTeX** | `kucharczyk2018vixnn` |
| **Status** | Reference: §2.1 (how the VIX is computed and settled), §5 (how many options a replication needs) and §6 (the LSTM results) |

## What it is

An attempt to track and predict the VIX minute by minute from a handful of liquid S&P 500
options, instead of the several hundred the official formula uses.

- **The motivation.** The VIX is a weighted sum of out-of-the-money SPX put and call
  quotes with 23–37 days to expiry. It cannot be traded; VIX futures and options settle on
  a special opening quotation computed from an opening auction in SPX options. That
  structure (an illiquid option market feeding a large, liquid VIX derivatives market)
  is why manipulation has been alleged (Griffin and Shams). On 5 February 2018 the
  VIX rose 115% in a day (to 37.32) and spot and futures diverged sharply.
- **Why replication is hard.** The authors re-run the official calculation for 2015–2018:
  it needs between 200 and 450 options at any time (about 350 on a normal day), and the
  set changes as the index moves. The forward-price term in the formula is negligible and
  they drop it.
- **The model.** One LSTM layer of 50 units, fed log-returns of the mid-quotes of a fixed
  set of 10, 100 or 200 OTM options chosen at the start of each day. It is trained on
  January 2018 and validated on February 2018 (1.68 and 1.52 million observations with
  100 options). It is never given the VIX formula.
- **The results.** Using only ten options (five puts, five calls), the network predicts
  the next minute's VIX return with a mean squared error of 4.08e-5, against 5.43e-5 for
  a no-change forecast. Trained instead to predict the sign of the next move, it is right
  61.3% of the time out of sample; a random forest on the same ten options gets 59.9%.
  More options help only slightly.

## Why it's in the library

**It explains the VIX's plumbing.** The most useful part is the description of how the
VIX is built and settled: many illiquid strike quotes, a 30-day interpolation between two
expiries, and a settlement auction. Those details are why the VIX can jump on thin
trading and why VIX futures and spot can come apart intraday.

**It is a small result, and should be read as one.** The sample is two months, the
validation month contains the February 2018 shock, and the gains over the naive forecast
are modest. A 61% hit rate on minute-ahead direction says nothing about profit once option
spreads are paid, which the authors acknowledge. The confusion matrix shows the model
mostly predicts up-moves: it catches only 36% of the down-moves. Some figures disagree with each
other (for example the split between puts and calls in a typical replication, and the
mean squared errors in Table 1 versus the text).

**It is a worked example of the trees-versus-networks question on a financial series.**
The random forest is almost as good as the LSTM, which matches the tabular and
time-series benchmarks elsewhere in the library.

## Links

- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  what VIX futures and the ETNs built on them do over longer horizons
- [[hall-rasheed-2025-survey-of-machine-learning-methods-for-time-series-prediction]] —
  how often deep sequence models beat simpler ones on time series
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — why a random forest is usually a hard baseline to beat
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the short-volatility build-up that
  ended in the 5 February 2018 spike this paper studies
- [[hirsa-et-al-2021-the-vix-index-under-scrutiny-of-machine-learning]] — the extended version: subset replication of the VIX and LSTMs for VIX futures
