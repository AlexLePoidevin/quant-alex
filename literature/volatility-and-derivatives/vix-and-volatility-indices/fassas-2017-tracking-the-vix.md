# Tracking the VIX

| | |
|---|---|
| **Authors** | Athanasios Fassas (University of Sheffield International Faculty, City College, Thessaloniki) |
| **Year** | 2017 |
| **Type** | Journal article, *The Journal of Index Investing* 8(1), 76–91. Data: January 2011 – March 2014 |
| **PDF** | Not hosted in this repository (journal download; publisher copyright) |
| **Find it** | [doi.org/10.3905/jii.2017.2017.1.050](https://doi.org/10.3905/jii.2017.2017.1.050) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Tracking+the+VIX%22+Fassas) |
| **BibTeX** | `fassas2017tracking` |
| **Status** | Reference: the tracking-error and regression exhibits (3 and 4) carry the results |

## What it is

A test of how well the instruments sold as "VIX exposure" actually follow the spot VIX
over one day, one week and one month. It covers front VIX futures and seven exchange-traded
products (VXX, VIXY, VIIX, VXZ, VIXM, CVOL and the long-short XVIX).

- **Why they can't track it.** The VIX is not a traded asset, so there is no
  cost-of-carry link between spot and futures. VIX futures are the market's expectation
  of the VIX at expiry. Because volatility mean-reverts, futures move much less than spot
  and usually sit in contango (above spot). Products that roll futures to keep a constant
  maturity pay that roll every day; the paper cites the short-term VIX futures index
  losing about 94% over six years.
- **Daily tracking is decent.** Front futures returns correlate about 0.90 with daily VIX
  returns (adjusted R² 0.81), and the three short-term ETPs a little less.
- **Weekly and monthly tracking fails.** Average tracking error rises from about 3–4% a
  day to roughly 6.5–13.6% a week and 10.5–23% a month. Futures, the best daily tracker,
  have the worst weekly and monthly tracking: their weekly and monthly returns are
  essentially uncorrelated with the VIX's.
- **Betas well below one.** A 1% daily VIX move goes with about 0.5% in the short-term
  ETPs and 0.2% in the mid-term ones. Mid-term products, which should suffer less roll
  cost, do not track spot any better.

## Why it's in the library

**It makes the "you can't buy the VIX" point with numbers.** Anyone using VIX products as
a hedge or a directional bet is holding a position on the futures curve, not on the index
quoted in the news. Over a week or a month the two can move in unrelated ways.

**It is a short-sample descriptive study.** Three years of data, closing prices rather
than NAVs, and no costs. The conclusion's tracking-error ranges (2.4–6.5% daily) do not
match those in the results section (2.9–4.5%). Use it for the qualitative pattern.

## Links

- [[gehricke-zhang-2018-modeling-vxx]] — why VXX bleeds: roll yield priced by the variance
  risk premium
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  a model of the whole VIX futures curve and the cost of holding the front end
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — the early evidence
  that VIX futures sit in contango and move less than spot
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  long VIX futures actually did inside a portfolio, crisis years and calm years
