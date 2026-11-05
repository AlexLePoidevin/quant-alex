# Financial Turmoil and Safe Haven Assets

| | |
|---|---|
| **Authors** | Dirk G. Baur (University of Technology Sydney), Thomas K. J. McDermott (Grantham Research Institute, LSE) |
| **Year** | 2013 (version dated May 2013; first posted 2012). The authors' later paper "Why is gold a safe haven?", *Journal of Behavioral and Experimental Finance* 10 (2016), 63–71, returns to the same question |
| **Type** | Working paper, SSRN 2004796, 34pp. Daily data, 1980–2010 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `baur2013turmoil` |
| **Status** | Reference: Tables I–III (crisis episodes and returns on the worst stock days), Tables V–VI (the VAR models) and §III (the behavioural interpretation) carry the argument |

## What it is

A joint study of the two best-known safe havens, US Treasuries and gold, and of how each
responds to large falls in world stock markets.

- **Data.** Daily returns, 1980–2010, for the MSCI World index in dollars, US Treasuries (2,
  10 and 30 years), gold bullion and COMEX gold, plus a trade-weighted dollar index from the
  Bank of England.
- **On average there is no haven.** The correlation of stocks with 10-year Treasuries is
  −0.02 and with gold +0.07. Gold is the most volatile of the three (daily standard deviation
  1.28%, against 0.89% for stocks and 0.52% for 10-year bonds).
- **On the worst days, bonds move first.** On the worst 1% of stock days (81 days, average
  −3.8%), 10-year Treasuries returned +0.51% and 30-year +0.89% on the same day, while gold
  bullion returned −0.04%.
- **Gold moves the day after.** In a vector autoregression run only on days of large stock
  falls, the lagged stock return in the gold equation gets steadily more negative as the
  falls get bigger: −0.08, −0.13 and −0.39 at the 10%, 5% and 1% thresholds. So gold rises
  the day after an extreme fall, while bonds' lagged response stays weak and insignificant.
  Lagged bond losses are also followed by gold gains, which the authors read as gold being a
  haven from bonds too. Gold rallies tend to be followed by higher stocks; bond rallies by
  lower stocks two days later.
- **The episodes.** In October–November 1987 stocks fell 20.7% while 30-year bonds rose 7.0%
  and gold 8.2%. Gold rose 6.3% in September 2001 and 6.8% in September 2008, then fell 15.4%
  in October 2008 as stocks fell another 23.6%. In the 1997 Asian crisis gold fell 12%.
- **A behavioural explanation.** The authors argue that gold's role cannot be explained by
  mean and variance, since it is riskier and less liquid than bonds. They use Ellsberg's
  ambiguity aversion: when investors lose confidence in their estimates, they weight the
  worst case more heavily. With assumed worst cases (stocks worst, bonds next, gold least
  bad), the preferred asset shifts from stocks to bonds to gold as ambiguity rises. They also
  point to "local thinking": in a panic, gold is the asset whose image comes to mind as a
  store of value.

## Why it's in the library

**It separates two havens by timing.** Treasuries are the same-day refuge in a stock crash;
gold responds with a lag and more strongly in the most extreme, unfamiliar shocks. That is a
useful prior for anyone choosing what to hold for a crash, and it explains why the two can
look so different in correlation tables.

**Gold is not a reliable short-term hedge.** Its October 2008 fall and its 1997 fall are in
the paper's own tables: a haven can be sold when investors need cash.

**The evidence is thinner than the story.** The VAR is estimated only on days selected by
extreme stock returns, which is non-standard, and the paper does not spell out exactly how
the days are chosen. The behavioural model is an illustration with payoffs the authors
assume, not a test. The data stop in 2010. The text also cites Table III for the summary
statistics that appear in Table II.

## Links

- [[baur-dimpfl-2022-a-safe-haven-index]] — a benchmark index of safe havens, including gold
  and Treasuries, and their behaviour in four crises
- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — intraday evidence on when gold starts
  to rise in a crash
- [[baur-2021-is-gold-a-safe-haven-in-all-currencies]] — why gold's safe-haven role depends
  on the investor's currency
- [[erb-harvey-2013-the-golden-dilemma]] — the usual arguments for holding gold, tested one
  by one
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — how often
  bonds rally when stocks crash, measured with extreme-value methods
- [[ang-chen-2002]] — correlations rise in down markets, which is why a haven has to be
  judged on the bad days
- [[stavrakeva-tang-2019-the-dollar-during-the-great-recession]] — the flight to the dollar
  in the 2008 crisis
