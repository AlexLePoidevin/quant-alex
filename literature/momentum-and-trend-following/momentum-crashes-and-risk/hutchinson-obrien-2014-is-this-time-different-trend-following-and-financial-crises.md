# Is This Time Different? Trend Following and Financial Crises

| | |
|---|---|
| **Authors** | Mark C. Hutchinson and John O'Brien (University College Cork, Centre for Investment Research) |
| **Year** | 2014 (Journal of Alternative Investments 17(2), 82–102); this copy is the February 2014 working-paper version (SSRN 2375733) |
| **Type** | Journal article (working-paper version), 43pp. A time-series momentum portfolio on commodity, bond, equity-index and currency futures and forwards, 1921–2013, split into crisis and no-crisis periods |
| **PDF** | Local copy only (working paper of a journal article, no open licence) |
| **BibTeX** | `hutchinson2014crises` |
| **Status** | Reference: Exhibit 7 (crisis versus no-crisis performance), Exhibits 9–11 (autocorrelation by period) and Exhibit 13 (individual crises) carry the results |

## What it is

A test of whether trend following does badly after financial crises, prompted by weak
CTA returns after 2008 (the Newedge Trend Index returned −0.8% a year from January 2009
to June 2013, against +8.0% in the prior five years).

- **The portfolio.** Twenty-one commodities, 13 government bonds, 21 equity indices and
  currency crosses from nine exchange rates, January 1921 to June 2013 (1940–49 excluded).
  Futures where they exist, synthetic forwards from spot, yield and cash rate before
  that. The signal averages the signs of 1- to 12-month past returns, each position is
  scaled to 40% volatility, risk is split equally across the four asset classes, and
  transaction costs (Hurst–Ooi–Pedersen estimates) are always charged; 2/20 fees where
  stated.
- **Long-run performance.** Net of fees, 12.1% a year at 11% volatility (Sharpe ratio
  1.10) from 1925 to 2013. Correlation with the Newedge Trend Index over 2000–2013 is 0.76.
- **The crises.** Six global crises from Kindleberger–Aliber and Reinhart–Rogoff: 1929,
  1973, 1981, 1987, 2000 and 2007, each dated from the prior equity peak. "Crisis" means
  the 24 or 48 months after that peak.
- **Main result (Exhibit 7, net of fees, 1925–2013).**
  - First 24 months of a crisis: 4.0% a year (Sharpe 0.36), against 13.6% (Sharpe 1.24)
    otherwise.
  - First 48 months: 6.0% (Sharpe 0.55) against 14.9% (Sharpe 1.35).
  - The same pattern holds for equity indices, bonds and currencies. Commodities are the
    exception: they do slightly *better* in crises.
  - The 1980–2013 subsample, all exchange-traded, gives similar ratios (2.6% versus 7.8%
    over 24 months).
- **Why: autocorrelation breaks down.** Pooled regressions of volatility-scaled monthly
  returns on their own lags show strong continuation out to 12 months in normal periods.
  In crisis periods the continuation weakens and reverses at lags 5, 6 and 8. After 12
  months the cumulative coefficient is significantly lower in crises for the full set,
  equities and currencies.
- **Shape of the weakness.** It is a long sideways period rather than a deep drawdown: the
  longest stretch with no cumulative excess return ranges from 18 months (2000) to 54
  months (1987), about three years on average. Fast crises (1929, 1987, 2000) start with
  losses as equity trends reverse sharply; slower ones (1973, 1981, 2007) give the signal
  time to turn and make early profits.
- **Regional crises.** Eight local crises (Spain 1977, Norway 1987, Nordic 1989, Japan
  1990, Mexico 1994, Asia 1997, Colombia 1997, Argentina 2000) show near-zero returns for
  two years, then recovery, with wide dispersion between crises.

## Why it's in the library

**It is the counterweight to "crisis alpha".** The usual case for trend following is
that it pays in the crash itself (2008 is the standard example). This paper shows the
other half of the cycle: in the years *after* the crash, trends stop persisting and the
strategy goes sideways for years. Anyone holding trend as a hedge needs both facts. The
proposed mechanisms (less overconfidence, policy interventions that cause reversals,
changing hedging pressure) are offered as hypotheses, and the authors say they do not test
them.

**Caveats.**
- Six global crises is a small sample, and the crisis windows are fixed at 24 or 48 months
  rather than measured.
- The study was funded by Aspect Capital, a trend-following manager.
- The commodity rows are identical in the full-sample and 1980–2013 panels, consistent
  with commodity data starting only with exchange-traded futures.

## Links

- [[hamill-et-al-2016-trend-following-equity-and-bond-crisis-alpha]] — the "crisis alpha"
  case for trend over the same kind of century-long sample
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the autocorrelation regressions
  and strategy construction this paper reuses
- [[harvey-et-al-2019-the-best-of-strategies-for-the-worst-of-times]] — trend as one of
  several crisis hedges, scored over drawdowns
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — why
  trend tends to be positioned correctly in the worst months but not the first ones
- [[butt-virk-2020-momentum-crashes-and-variations-to-market-liquidity]] — the
  cross-sectional version: momentum's worst periods follow market stress
