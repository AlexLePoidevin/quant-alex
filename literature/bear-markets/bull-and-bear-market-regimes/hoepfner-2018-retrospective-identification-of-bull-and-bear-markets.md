# Retrospective Identification of Bull and Bear Markets: A New, But Simple Algorithm

| | |
|---|---|
| **Authors** | Marcel Hoepfner (Bielefeld University) |
| **Year** | 2018 |
| **Type** | Working paper. Bielefeld Working Papers in Economics and Management 01-2018; SSRN 3105209 (doi 10.2139/ssrn.3105209), 21pp |
| **PDF** | Local copy only (working paper; no open licence) |
| **BibTeX** | `hoepfner2018retrospective` |
| **Status** | Reference: §2 (the IBB algorithm), Table 1 (most robust window sizes) and Tables 2–4 (dated bull and bear markets for six indices) |

## What it is

An algorithm for dating bull and bear markets **after the fact**. The author calls it the IBB
algorithm (identification of bull and bear markets).

Most dating rules need two or more parameters chosen by the analyst: a minimum fall (often 20%),
a minimum rise, and a minimum duration. Pagan and Sossounov (2003), for example, use four months
per phase and 16 months per cycle. IBB keeps only one parameter, a window size, and chooses it
by a robustness criterion:

1. **Find turning points.** Set a window of f points either side of each date. A date is a peak
   (trough) if it is the highest (lowest) point in the window centred on it, and the same
   maximum is found by F = 2f + 1 consecutive windows.
2. **Keep the phases alternating.** If two peaks occur without a trough in between, keep the
   higher one; the same for troughs.
3. **Choose f by robustness.** Run the algorithm for many values of f, find the longest range of
   f that gives the same bull and bear markets, and take the middle of that range.

Applied to the Dow Jones, S&P 500, Nikkei, DAX, FTSE and SMI from July 1992 to September 2016,
the chosen windows span at least a year either side of each date. The resulting phases don't
change when the window is varied by roughly 27% to 68%. Each index splits into five or six
phases. For the S&P 500 these are:
- bull to March 2000;
- bear to October 2002;
- bull to October 2007;
- bear to March 2009;
- bull to the end of the sample.

The bear phases show the expected negative returns and higher volatility. The returns are
summed log returns, so the S&P 500's −83.9% for 2007–09 is about a −57% price fall.

## Why it's in the library

It is a clean, reproducible way to label the large bull and bear markets in a price series. It
is useful as an ex-post reference when testing anything that claims to forecast regimes.

Its limits:
- **It cannot be used in real time.** Every turning point needs about a year of future data,
  which is why the paper says "retrospective".
- **"No arbitrary parameters" is overstated.** The rule for choosing f (the longest stable range,
  then its midpoint) is itself a choice. So is the author's stated aim to find long phases
  rather than short ones.
- **It only finds the largest cycles.** With windows of a year or more either side, smaller bear
  markets such as 2011 and 2015–16 in the US are not separate phases.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a model-based alternative
  that also separates bear rallies and bull corrections
- [[ang-timmermann-2012-regime-changes-and-financial-markets]] — the Markov-switching approach,
  which Kole and van Dijk find better for forecasting while rule-based dating like this is better
  for labelling the past
- [[yang-wagner-2014-optimal-probabilistic-market-timing-using-bull-bear-cycle-statistics]] — a
  threshold-based dating rule (gain, loss and duration) of the kind IBB tries to replace
- [[haase-neuenkirch-2023-predictability-of-bull-and-bear-markets]] — uses the Lunde–Timmermann
  dating rule as the ex-post benchmark for real-time forecasts
