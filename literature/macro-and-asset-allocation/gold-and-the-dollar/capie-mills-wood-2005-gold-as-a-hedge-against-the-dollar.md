# Gold as a Hedge Against the Dollar

| | |
|---|---|
| **Authors** | Forrest Capie (Cass Business School), Terence C. Mills (Loughborough University), Geoffrey Wood (Cass Business School) |
| **Year** | 2005 (*Journal of International Financial Markets, Institutions and Money* 15(4), 343–352) |
| **Type** | Journal article, 10pp. Weekly data, 8 January 1971 to 20 February 2004 (1,728 weeks) |
| **PDF** | Local copy only (Elsevier journal article) |
| **BibTeX** | `capie2005gold` |
| **Status** | Reference: §3 (the GARCH models and Table 2, sub-periods) |

## What it is

A test of whether gold protects against falls in the dollar's foreign-exchange value,
using the period after the Bretton Woods gold window closed in 1971, when gold stopped
being part of the monetary system.

- **Why start in 1971.** Under the gold standard gold was a hedge by construction, since
  currencies were fixed to it. Once that ended, gold could only be a hedge if people
  switched into it when currencies weakened.
- **The data.** Weekly London gold fix in dollars, and sterling–dollar and yen–dollar rates
  at the same time.
- **The contemporaneous link.** Weekly changes in gold and in the two exchange rates (in
  foreign currency per dollar) have correlations of about −0.2, with almost no lead or
  lag. When the dollar weakens, gold rises in dollars.
- **The model.** Regressions of the weekly gold change on the exchange-rate change with
  EGARCH errors and fat-tailed (Student t, about 4 degrees of freedom) innovations. The
  elasticity is about −0.31 for sterling and −0.21 for the yen, and the long-run effect
  is reached within a week. So gold is an inelastic hedge: a 1% dollar fall goes with
  roughly a 0.2–0.3% gold rise. (The text swaps the long-run figures for the two
  currencies in one sentence; Table 2 gives −0.330 for sterling.)
- **Unstable over time.** Plots of gold against each currency fall into separate strata,
  with breaks in January 1974, October 1976 and September 1979 for sterling, and at the
  Plaza Accord of September 1985 for the yen. In one sub-period (October 1976 to
  September 1979) the sterling elasticity was −1.32.
- **Volatility.** Gold volatility is extremely persistent and rises more after unexpected
  price rises than after falls.

## Why it's in the library

**It is a standard reference for gold as a dollar hedge.** The negative link between gold
and the dollar is real but partial and, by the authors' own conclusion, depends on
"unpredictable political attitudes and events" that change its strength from period to
period.

**It shows why a full-sample coefficient can mislead.** The sub-period elasticities range
from about −0.2 to −1.3, so an investor relying on the average would be wrong in most
sub-periods. The data stop in 2004, before the 2008 crisis and the later period of
negative real yields.

## Links

- [[baur-smales-2018-gold-and-geopolitical-risk]] — a different reason gold rises: geopolitical threats rather than the dollar
- [[jermann-2022-golds-value-as-an-investment]] — gold priced from real interest rates, with the dollar as a secondary factor before 2007
- [[merton-1976]] — jumps and fat tails, which the Student-t errors here account for
- [[baur-2021-is-gold-a-safe-haven-in-all-currencies]] — how gold's currency-hedge property makes it a safe haven for non-dollar investors
