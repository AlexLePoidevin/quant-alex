# Reducing Sequence Risk Using Trend Following and the CAPE Ratio

| | |
|---|---|
| **Authors** | Andrew Clare, James Seaton, Stephen Thomas (Cass Business School); Peter N. Smith (University of York) |
| **Year** | 2017 (the copy is the May 2017 version, SSRN 2764933; published in *Financial Analysts Journal* 73(4), 91–103, 2017) |
| **Type** | Paper, 34pp. Real S&P 500 returns 1872–2014 from Shiller's data; Monte Carlo and two historical 20-year retirement windows |
| **PDF** | Not hosted in this repository (SSRN preprint of an FAJ article, © CFA Institute) |
| **Find it** | [doi.org/10.2469/faj.v73.n4.5](https://doi.org/10.2469/faj.v73.n4.5) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Reducing+Sequence+Risk+Using+Trend+Following+and+the+CAPE+Ratio%22+Clare) |
| **BibTeX** | `clare2017sequence` |
| **Status** | Reference: the PWR algebra (equations 3–6), Table 2 (PWR distributions with and without trend), the transaction-cost section and Tables 3–6 (1995 and 1973 retirements) carry the result |

## What it is

A study of retirement withdrawals that asks which investment strategy best protects them
from the order in which returns arrive.

- **Perfect withdrawal rate (PWR).** For a given sequence of returns there is one constant
  withdrawal that exhausts the pot exactly at the horizon. It equals the cumulative return
  times a sequence factor S, minus a term for any bequest. S is larger when good returns
  come early, so the same returns in a different order support a different income. That is
  sequence risk.
- **Buy and hold.** With perfect foresight over 20 years, the real PWR on US equities
  ranged from about 4% (starting 1930) to 15% (1949).
  - **Monte Carlo:** drawing 20 annual real returns at random, 20,000 times, gives a 10%
    chance of a PWR of 5.0% or less and a median of 8.6%.
- **Add a trend filter.** Hold the S&P 500 when it is above its 10-month moving average and
  cash otherwise, checked monthly. Over 1872–2014 this:
  - raises the real return from 6.8% to 8.8% a year;
  - cuts volatility from 14.3% to 9.9%;
  - roughly halves the maximum drawdown, from 77% to 35%.
- **What that does to withdrawals.** The trend filter lifts PWRs in every part of the
  distribution up to about the 80th percentile, and the gain is largest in bad cases:
  - **1st percentile:** 5.6% against 3.0%.
  - **10th percentile:** 7.2% against 5.0%.
  - **Median:** 9.8% against 8.6%.

  On the 1,500 overlapping historical 20-year windows the average PWR is 9.6% against
  8.8%.
- **Trading costs.** The filter switches just under 7 times a decade and is invested about
  two-thirds of the time. The break-even one-way cost that would erase its advantage is
  1.35%. At 0.36% one-way, Hurst et al.'s estimate for the early 20th century, the average
  PWR is 9.68% against 8.8%.
- **CAPE.** A low CAPE at the start of retirement goes with a higher later PWR. Setting each
  year's withdrawal from a CAPE regression raised later withdrawals for a 1995 retiree. It
  did not help a 1973 retiree, where the trend filter alone did best: its perfect-foresight
  PWR was 6.1% against 4.6% for buy and hold.

## Why it's in the library

**It measures drawdown risk in the unit retirees care about.** Sharpe ratios ignore the
order of returns. The PWR, written as cumulative return times a sequence factor, turns
"avoid big early losses" into a precise number. It shows why a lower-drawdown strategy can
support more income even when average returns are similar.

**It is a clean case for trend filters as drawdown control.** A rule with one parameter,
applied monthly to one index, does most of the protective work. The paper spells out the
holding-cost and switching-cost arithmetic.

**Limits.**
- **The resampling discards the timing.** The Monte Carlo draws returns independently,
  with replacement. The text says annual returns and the Table 2 note says monthly ones.
  Either way it ignores the serial dependence that sequence risk is about, so the trend
  filter's gain there comes from a better distribution of returns, not from timing.
- **Overlapping windows.** The historical-window test uses heavily overlapping 20-year
  periods.
- **The CAPE regression is never specified.** The text calls it "described above", but it
  isn't. A regression on 20-year forward PWRs can only use windows that have finished,
  which the paper doesn't explain.
- **Narrow scope.** Everything is on US equities alone.

## Links

- [[van-hemert-et-al-2020-drawdowns]] — how likely drawdowns of a given size are, and the rules investors use to act on them
- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — trend following as crisis protection across futures markets
- [[mcquinn-thapar-villalon-2021-portfolio-protection-its-a-long-term-story]] — protection against long bad periods rather than fast crashes
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the empirical case for trend rules across asset classes
- [[keller-keuning-2016-paa]] — a moving-average-style allocation rule that also moves to cash or bonds in bad markets
