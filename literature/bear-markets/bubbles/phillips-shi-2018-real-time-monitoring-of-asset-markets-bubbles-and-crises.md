# Real Time Monitoring of Asset Markets: Bubbles and Crises

| | |
|---|---|
| **Authors** | Peter C. B. Phillips (Yale), Shuping Shi (Macquarie University) |
| **Year** | 2018 (Cowles Foundation Discussion Paper 2152, 22 November 2018; SSRN 3299498). Written as a book chapter |
| **Type** | Methods chapter with R code, 25pp |
| **PDF** | Not hosted in this repository (Cowles Foundation / SSRN working paper with no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3299498](https://doi.org/10.2139/ssrn.3299498) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Real+Time+Monitoring+of+Asset+Markets%3A+Bubbles+and+Crises%22+Phillips) |
| **BibTeX** | `phillips2018monitoring` |
| **Status** | Reference: §2 (the PSY recursive test), §5 (the new bootstrap) and §6 (the S&P 500 and euro-area applications) |

## What it is

A practical guide to the most widely used statistical test for bubbles, the
Phillips–Shi–Yu (PSY) procedure, together with an R package (`psymonitor`) and a new
way of setting its critical values.

- **What the test looks for.** In normal times a log price (or price-to-dividend ratio)
  behaves like a random walk with at most a small drift. During a bubble it becomes
  *mildly explosive*: an autoregressive coefficient slightly above one, so each move
  builds on the last. During a crash or credit crisis it instead follows a random walk
  with a large negative drift (or, for bond yields, a large positive drift).
- **How it does it.** For each date, PSY runs augmented Dickey–Fuller regressions on every
  window that *ends* on that date, from a minimum window up to the whole history, and
  takes the largest t-statistic. This "backward sup ADF" uses only past data, so it can
  be run in real time. A bubble or crisis is dated from the first day the statistic
  crosses its critical value until the day it falls back below.
- **One statistic, two kinds of episode.** The same statistic rises in a bubble
  (explosive growth) and in a crash (a negative random drift). The test does not by
  itself say which, so the user reads the episode from the direction of the price move.
- **A new bootstrap.** Two problems inflate false alarms. Volatility changes over time
  (heteroskedasticity), and the test is repeated every day, so some crossings happen by
  chance. The paper combines a wild bootstrap (to handle changing volatility) with
  taking the maximum statistic over a chosen window (to control the false-alarm rate
  over, say, two years rather than per day). It uses 999 replications and the 95th
  percentile.
- **Application 1: the S&P 500 price-to-dividend ratio, 1973–2018 (monthly).** With size
  controlled over two-year windows it flags:
  - a short episode in mid-1986 and July–August 1987, before Black Monday;
  - the dot-com bubble, from January 1996 to October 2000 with gaps, which starts
    before Greenspan's "irrational exuberance" speech in December 1996;
  - the financial crisis, from October 2008 (a month after Lehman) to February 2009.
- **Application 2: euro-area sovereign credit risk, 1997–2016.** The test is applied to
  the spread between a GDP-weighted 10-year yield of Greece, Ireland, Italy, Portugal and
  Spain and the German 10-year yield. It flags March 2008, October 2008 to March 2009,
  and May 2010 to August 2012.

## Why it's in the library

**It is the standard tool, written as a recipe.** Central banks use PSY for housing and
asset markets; the Dallas Fed publishes a housing exuberance indicator built on it. The
chapter gives the regression, the window rule (minimum window r0 = 0.01 + 1.8/√T), the
dating rule and the code, which makes it the quickest way to apply the method.

**The bootstrap matters more than it looks.** Running a test every month for decades
will flag something by chance. Controlling the false-alarm rate over a window is the
difference between an alarm that means something and one that rings in every sample.
This is the same multiple-testing problem that inflates backtests.

**Know what "bubble" means here.** PSY detects explosive *price behaviour*, not
mispricing. A price that grows explosively because fundamentals are growing explosively
would also be flagged, which is why the S&P 500 example is run on the price-to-dividend
ratio rather than on the price. The examples are in-sample illustrations ("pseudo
real-time"), not a record of alarms issued at the time, and the chapter reports no
false-alarm or missed-episode rates.

## Links

- [[gurkaynak-2008-econometric-tests-of-asset-price-bubbles]] — the survey of earlier bubble tests and the joint-hypothesis problem that this approach sidesteps by testing price behaviour alone
- [[bashchenko-marchal-2020-deep-learning-for-asset-bubbles-detection]] — a different definition (strict local martingales) and a machine-learning detector
- [[west-1988-bubbles-fads-and-stock-price-volatility-tests]] — the older volatility-bound tests for bubbles
- [[harvey-liu-zhu-2016]] — the same multiple-testing problem in the factor zoo
- [[fusari-jarrow-lamichhane-2025-testing-for-asset-price-bubbles-using-options-data]] — an alternative that detects bubbles from a single day's option prices rather than a price history
- [[tarlie-sakoulis-henriksson-2022-stock-market-bubbles-and-anti-bubbles]] — explosive valuation recast as a temporarily negative mean-reversion speed, which also finds anti-bubbles
