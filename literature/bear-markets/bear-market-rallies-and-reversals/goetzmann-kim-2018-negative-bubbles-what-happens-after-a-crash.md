# Negative Bubbles: What Happens After a Crash

| | |
|---|---|
| **Authors** | William N. Goetzmann (Yale School of Management), Dasol Kim (Office of Financial Research, US Treasury) |
| **Year** | 2018 (*European Financial Management* 24(2), 171–191); this copy is NBER Working Paper 23830, September 2017, revised January 2018 |
| **Type** | Empirical paper, 33pp. 101 national stock markets, monthly real price returns, 1692–2015 |
| **PDF** | Not hosted in this repository (NBER working paper, © the authors, all rights reserved) |
| **Find it** | [doi.org/10.1111/eufm.12164](https://doi.org/10.1111/eufm.12164) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Negative+Bubbles%3A+What+Happens+After+a+Crash%22+Goetzmann) |
| **BibTeX** | `goetzmann2018negative` |
| **Status** | Reference: §4 (Tables 2–4, the conditional distributions) carries the result; §5 tests explanations |

## What it is

Three centuries of crashes across 101 markets, asking one question: after a market falls
hard, does it keep falling or bounce?

- **The data.** Monthly real capital-appreciation returns for 101 markets from Global
  Financial Data, the earliest crash being the year after the South Sea Bubble. A crash is
  a fall over the previous 12 months, graded from any loss to a fall of 50% or more. There
  are 1,032 cases of a 50%+ fall, 1.8% of all observations.
- **Big crashes bounce, small ones persist.** After an ordinary down year the next year is
  more often negative. After a fall of 50% or more, the next 12 months are positive about
  60% of the time, and a gain of more than 25% is roughly twice as likely as a further fall
  of 25%.
- **In regressions** with volatility, three years of past returns, and country and date
  fixed effects (Driscoll–Kraay standard errors for the overlapping data):
  - a 50%+ fall raises the probability of a following gain of 50% or more by 10.5
    percentage points (17.8 without controls);
  - returns in the year after a 50%+ fall are 14.0% to 18.4% higher than after an up year,
    with some reversal in the year after that;
  - falls of up to 10% are followed by returns 5.6% to 6.2% lower, and falls of up to 40%
    by a further decline of roughly 6% to 9%.
- **Explanations tested.**
  - Institutional constraints: rebounds should be bigger when the crash is global (fire
    sales, constrained arbitrageurs). They are not significantly different.
  - Macroeconomic conditions: depressions, GDP, inflation, credit growth, financial crises
    and dividend yields, for 14 markets 1870–2008. They predict returns but do not remove
    the rebound.
  - Political conflicts, 1918–2013: they do not explain it either.
  - Survivorship: a follow-forward sample of markets known to exist at the time, including
    pre-revolutionary Russia and China. The year after a 50%+ fall is positive 71.6% of the
    time, against 58.7% after any down year, so the pattern is not a survivorship artefact.
- **What is left.** Behavioural stories (panic, a "negative bubble" of pessimism, Shiller's
  term) fit the facts but are not tested.

## Why it's in the library

It is the long-run base rate for what follows a crash. Severe falls tend to be followed by
large rebounds, while moderate declines tend to continue: that non-linearity is the case
for not selling after a collapse and for respecting a drawdown that is still moderate. It
puts the bear-rally and dead-cat-bounce material on a very large sample.

Mind the limits. The returns are price-only, real, annual-horizon and overlapping. Many
50%+ crashes are in small, volatile or newly opened markets, the persistence after small
falls does not hold in a subsample of 41 major markets, and the distribution after a crash
is very wide: a bounce is more likely, not assured. The paper does not test whether the
rebound can be captured with a tradable rule.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bear rallies and the
  bear-to-bull transition in a regime model of the US market
- [[johannsen-2016-dead-cat-bounce]] — a behavioural model of a bounce after a bubble bursts
- [[flora-reno-2020-v-shapes]] — a statistical test for crash-and-rebound shapes on much
  shorter horizons
- [[soros-2013]] — boom–bust dynamics driven by beliefs, the kind of explanation the paper
  leaves open
- [[brown-dewey-2021-toil-and-trouble-dont-get-burned-shorting-bubbles]] — a practitioner case that buying after the subprime crash was a better trade than shorting the bubble
- [[quinn-turner-2025-who-wins-and-loses-in-a-bubble-british-bicycle-mania]] — which investors were left holding through a 73% crash, from named shareholder records
- [[schatz-sornette-2020-inefficient-bubbles-and-efficient-drawdowns]] — a framework for the run-up and crash that precede the rebounds studied here
- [[tarlie-sakoulis-henriksson-2022-stock-market-bubbles-and-anti-bubbles]] — anti-bubbles defined as periods when cheap markets keep getting cheaper, from a model of time-varying mean reversion in US valuation
