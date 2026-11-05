# The Best of Strategies for the Worst of Times: Can Portfolios be Crisis Proofed?

| | |
|---|---|
| **Authors** | Campbell R. Harvey, Edward Hoyle, Sandy Rattray, Matthew Sargaison, Dan Taylor, Otto Van Hemert (Man Group; Harvey also at Duke) |
| **Year** | 2019 (version dated 17 May 2019) |
| **Type** | Paper. SSRN 3383173, 26pp; published in *Journal of Portfolio Management* 45(5), 7–28 (2019). Data 1985–2018 |
| **PDF** | Local copy only (SSRN download of a Man Group working paper; no open licence) |
| **BibTeX** | `harvey2019worst` |
| **Status** | Reference: Tables 1–2 (each hedge in the eight drawdowns and three recessions), §3–4 (trend and quality) and Table 10 (portfolio simulation) carry the results |

## What it is

A side-by-side test of the usual ways to protect an equity portfolio, scored on the eight
S&P 500 drawdowns of more than 15% and the three NBER recessions between 1985 and 2018.
Drawdown days are 14% of the sample; the S&P 500 returned −44.3% a year annualised on those
days and +24.4% on the rest.

- **Long puts (rolled one-month at-the-money S&P 500 puts).** Made money in all eight
  drawdowns, mostly in short bursts such as October 2008. They are the most reliable hedge
  and also the most expensive: −7.4% a year excess return over the whole sample, before
  option trading costs. Half equities, half puts lost money in every crisis and overall.
  Out-of-the-money puts are cheaper per unit but pay little in slow, grinding declines.
- **Short credit risk (long Treasuries against investment-grade corporates).** Also
  positive in drawdowns, unevenly: +128% in 2007–09, a credit crisis, then an equally
  large fall. Small negative return overall.
- **Long 10-year Treasuries.** +10.6% a year in drawdowns against +3.1% in normal times,
  but only because of the post-2000 drawdowns. Bonds lost 8.3% around Black Monday. The
  rolling five-year stock–bond correlation since 1900 was positive for most of the century
  before 2000, so the negative correlation investors now rely on is historically unusual.
- **Long gold.** Positive in seven of eight drawdowns (+9.0% a year in drawdowns), negative
  on average otherwise, close to zero overall, with a lot of risk unrelated to equities.
- **Time-series momentum (trend) on 50 futures.** 1- and 3-month trend made money in the
  drawdowns and in all three recessions; 12-month trend lost in the three most recent
  drawdowns, including 2018Q4. Barring long equity positions improves crisis returns but
  costs about 1% a year overall. Estimated costs: 0.6–0.8% a year.
- **Quality long–short stocks.** Profitability, payout and safety composites did best in
  the worst equity quintiles. The paper insists on beta-neutral construction: the usual
  dollar-neutral quality-minus-junk factor has −0.48 correlation to the S&P 500, so its
  crisis returns are partly just a short market position. Growth measures did not help.
  Estimated costs: 1–2% a year.
- **Combining them.** Trend and quality are nearly uncorrelated. After costs, putting 10%
  of the portfolio into a combined trend-plus-quality sleeve improved every one of the eight
  drawdowns and lifted the drawdown-period return from −44.3% to −36.8% a year; it took a
  50% allocation to make drawdown periods positive.

## Why it's in the library

**It prices the main defensive options on one common yardstick.** Puts, bonds, gold, credit
protection, trend and quality are scored on the same crises with the same volatility
scaling. That makes the trade-off between reliability and cost explicit: puts are the
surest and the dearest, bonds are cheap but depend on a correlation regime that may not
last.

**It explains why dynamic hedges can be cheaper than insurance.** Trend behaves like a
synthetic long straddle and quality benefits from flight to quality, and both have earned a
positive return over the full sample, unlike puts. The defensive property comes with an
expected return instead of an insurance premium.

**Read the numbers for what they are.** One 34-year sample, eight episodes, returns gross
of costs in most tables and scaled to 10% volatility after the fact. Only 2018Q4 is out of
sample relative to the authors' earlier version. The authors run trend and quality
strategies commercially, and the paper's own conclusion is that every crisis is different,
so diversify across defensive strategies.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the cost of carrying long-VIX protection, measured on a 60/40 portfolio
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]] — why calendar-rolled option hedges bleed
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — why a trend rule pays off when bull and bear regimes persist
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — how bear markets and bear rallies are structured
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the argument that many popular strategies are implicitly short volatility
- [[cfm-2018-the-convexity-of-trend-following]] — why trend following pays in sustained crashes, derived from the P&L of a moving-average rule
- [[garcia-feijoo-jensen-johnson-2012-the-effectiveness-of-asset-classes-in-hedging-risk]] — an earlier 1970–2010 scorecard of which asset classes co-crash with equities
