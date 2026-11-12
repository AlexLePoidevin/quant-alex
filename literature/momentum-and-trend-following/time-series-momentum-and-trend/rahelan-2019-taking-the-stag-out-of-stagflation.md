# Taking the Stag out of Stagflation

| | |
|---|---|
| **Authors** | Nader Rahelan |
| **Year** | 2019 (November working paper, SSRN 3479536) |
| **Type** | Working paper, 16pp. AQR's daily equity factor data (market, BAB, SMB, HML, UMD, HML-devil) for 23 developed countries and regional portfolios, 1999–2019 |
| **PDF** | Not hosted in this repository (SSRN working paper, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Taking+the+Stag+out+of+Stagflation%22+Rahelan) for the title and authors |
| **BibTeX** | `rahelan2019stagflation` |
| **Status** | Reference: Exhibits 1–3 (the factor trend strategy), Exhibit 11 (the regression that selects stagflation) and Exhibit 12 (the stagflation-conditioned strategy) carry the claims |

## What it is

A single-author working paper that applies a trend-following rule to equity factors
rather than to assets, finds it does not beat simply holding the factors, and then
claims it does during stagflation.

- **The rule.** For each factor in each country, take the signs of its past 3-, 6- and
  12-month returns (a variant of Hurst, Ooi and Pedersen's trend signal, with 3 months in
  place of 1). Hold the factor if at least two are positive, otherwise hold nothing:
  long or flat, never short. The positions are equally weighted. Each switch costs 20 bp.
- **Unconditional result.** Over 1999–2019 the portfolio earns 11.2% a year gross, 7.2%
  after a hypothetical 2-and-20 fee, and 3.1% after fees and costs, at 6.8% volatility: a
  Sharpe ratio of 0.45. It has a 0.64 correlation with the equally weighted factor
  portfolio and small negative correlations with the S&P 500 and Treasuries. Factor by
  factor, timing has an average information ratio against simply holding the factor of
  −0.01 before costs and −0.02 after. In nine of the ten worst drawdowns of the factor
  portfolio the timed version does worse.
- **Regimes.** Relative to the factor portfolio, the timed version does better in NBER
  recessions (+3% a year) and high-inflation months, and worse in booms (−0.83%).
- **The stagflation step.** Seven regressions of timing-minus-benchmark returns on lagged
  recession, high-inflation and recession×inflation ("stagflation") dummies are compared
  by F-statistic, and stagflation is chosen as the predictor. The final strategy holds the
  equally weighted factor portfolio normally, and after a stagflation month goes long the
  timed factors and short the factor portfolio.
- **The headline.** A Sharpe ratio of 1.03 (4.6% return, 4.5% volatility) net of costs and
  2-and-20 fees, correlation −0.1 with the S&P 500 and −0.06 with 10-year Treasuries, and
  a Sharpe ratio "around 2" in stagflation months.

## Why it's in the library

**As a negative result, it is useful.** Trend-following a factor is a way to time it, and
here that timing adds nothing after costs, which matches the larger studies of factor
timing. Holding the factors beats trading their trends.

**As a positive result, it shows how a backtest gets made.** The stagflation strategy is
built in one sample: the predictor is picked from seven regression specifications on
1999–2019 data, then the strategy using it is evaluated on the same data. NBER recession
dates are announced months after the fact, and the paper's own caveat says the
high/low inflation split is defined ex post, so neither the lagged recession nor the
lagged inflation signal was available in real time. Stagflation months are rare in a
20-year sample, so the Sharpe ratio of about 2 in those months rests on very few
observations, and no significance test is given for the final strategy.

**The text and tables do not always agree.** The paper says the timed strategy has "a
Sharpe ratio of one" net of costs where its own table shows 0.45; Exhibit 2 is labelled
as Sharpe ratios but reports percentages. Treat the numbers as indicative.

## Links

- [[ilmanen-et-al-2021-how-do-factor-premia-vary-over-time]] — a century of evidence that timing factor premia barely pays after costs
- [[arnott-et-al-2019-alices-adventures-in-factorland]] — factor returns, crashes and the pitfalls of factor investing
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — choosing rules from a model rather than by searching a backtest
- [[neville-et-al-2021-the-best-strategies-for-inflationary-times]] — what actually worked in inflationary regimes since 1926, with far more episodes
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the time-series momentum signal applied here to factors
