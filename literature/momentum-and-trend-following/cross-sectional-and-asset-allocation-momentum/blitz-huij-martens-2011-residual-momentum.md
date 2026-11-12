# Residual Momentum

| | |
|---|---|
| **Authors** | David Blitz, Joop Huij, Martin Martens (Robeco; Erasmus University Rotterdam) |
| **Year** | 2011 (Journal of Empirical Finance 18(3), 506–521) |
| **Type** | Journal article; copy is the SSRN author version (2319861), 60pp. CRSP US stocks, January 1926 – December 2009 |
| **PDF** | Not hosted in this repository (SSRN author copy of an Elsevier article) |
| **Find it** | [doi.org/10.1016/j.jempfin.2011.01.003](https://doi.org/10.1016/j.jempfin.2011.01.003) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Residual+Momentum%22+Blitz) |
| **BibTeX** | `blitz2011residual` |
| **Status** | Reference: §4.1 (factor exposures and Table 2), §4.2–4.3 (decades and the business cycle) and §5 (robustness) carry the results |

## What it is

A momentum signal built from each stock's own news rather than its total return, which
roughly halves the strategy's risk while keeping its profit.

- **The problem with ordinary momentum.** A 12-1 month momentum portfolio buys whatever
  went up. After a rising market it is long high-beta stocks and short low-beta ones;
  after a falling market the reverse. The same happens with size and value. So the
  strategy carries large exposures to the Fama–French factors that flip sign with recent
  factor returns, and it loses heavily when those factors reverse.
- **The residual signal.** Each month, regress every stock's last 36 months of returns on
  the Fama–French three factors. Sum the residuals over months t−12 to t−2, divide by
  their standard deviation, and form the long–short decile portfolio on that score. The
  regression alpha is left out so that returns from three years ago, which belong to the
  long-term reversal effect, don't leak into the signal.
- **Main result (one-month holding period, 1930–2009).** Total-return momentum: 10.26% a
  year, volatility 22.70%, conditional alpha 7.98%. Residual momentum: about 11.2% a year
  with volatility 12.49%, and an alpha about 2.9 points higher. With similar returns and
  roughly 45% less volatility, the Sharpe ratio about doubles, to between 0.4 and 0.9
  depending on the holding period. Residual momentum's dynamic factor betas are three to
  five times smaller; factor exposures explain 34–48% of total-return momentum's variance
  but only up to 17% of residual momentum's.
- **Fewer disasters.** Total-return momentum's worst drawdown was 85% in the early 1930s,
  taking over 19 years to recover; residual momentum's was less than half that. In
  2000–2009 total-return momentum returned −8.5% a year with a drawdown above 80%, while
  residual momentum made 4.7% a year with a drawdown of about 40%. The 2009 rebound, when
  ordinary momentum was short high-beta stocks into a rally, is the textbook case.
- **The business cycle and January.** In NBER recessions total-return momentum loses
  8.73% a year (versus +14.70% in expansions), mostly in the second half of recessions
  when markets turn. Residual momentum still earns about 5.6% a year in recessions.
  Because it is nearly size-neutral, it also avoids most of momentum's January losses
  from tax-loss rebounds in small losers (an average January return of −0.32% versus −2.60%).
- **Robustness.** The result survives other formation and holding periods, a large-cap
  only sample, other factor models and beta windows, and the post-1960 period.

## Why it's in the library

**It shows that much of momentum's risk is accidental factor timing.** About half of
ordinary momentum's variance comes from dynamic factor bets that add only about a quarter
of its return. Taking them out is a cheap improvement that uses only data available at
the time.

**It explains momentum's worst episodes.** The 1932 and 2009 crashes come from the
strategy being short the market just before a rebound. That links to the momentum-crash
literature and to why a residual or factor-neutral signal behaves differently in bear
market rallies.

**Limits.** Returns are gross of costs, though the authors argue residual momentum's
smaller small-cap tilt should make it cheaper to trade. The 36-month regression requires
three years of history, which drops young stocks. Results are for US stocks to 2009 only.

## Links

- [[kelly-moskowitz-pruitt-2021-understanding-momentum-and-reversal]] — momentum and reversal explained by stocks' time-varying factor betas
- [[carhart-1997]] — the four-factor model that made 12-1 momentum a standard factor
- [[fama-french-1993]] — the three factors whose exposures residual momentum strips out
- [[hoffstein-faber-braun-2020-rebalance-timing-luck-of-smart-beta]] — how much a momentum portfolio's result depends on its rebalance dates
