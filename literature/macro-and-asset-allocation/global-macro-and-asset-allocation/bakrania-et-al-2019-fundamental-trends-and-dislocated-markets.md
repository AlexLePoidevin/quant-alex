# Fundamental Trends and Dislocated Markets: An Integrated Approach to Global Macro Investing

| | |
|---|---|
| **Authors** | Paras Bakrania, Chris Doheny, Jonathan Fader, Caroline Heinrichs (AQR Capital Management) |
| **Year** | 2019 (AQR white paper, April 2019; data January 1993 – December 2018) |
| **Type** | Manager white paper, 28pp |
| **PDF** | Local copy only (AQR publication, no open licence) |
| **BibTeX** | `bakrania2019macro` |
| **Status** | Reference: the integrated backtest (Exhibit 7), the factor regressions against the Credit Suisse macro index (Exhibit 9) and the appendix backtest rules |

## What it is

A proposal to combine two global macro approaches that bet in opposite directions:

- **Systematic macro ("macro momentum").** Markets underreact to economic news, so buy
  assets whose fundamentals are improving and sell those deteriorating. Signals are
  grouped into four themes: business cycle (growth and inflation surprises, forecast
  revisions), monetary policy (short-rate changes, Taylor rules), international trade
  (terms of trade, exchange rates) and macro sentiment (options sentiment, equity
  performance). Earlier AQR work found Sharpe ratios of 0.5–0.7 per theme over 1990–2013.
- **Opportunistic macro ("deep value").** Occasionally prices overshoot far from fair
  value. Screen many valuation metrics across equity indices, sectors, bonds, rates,
  currencies and commodities; enter when a value spread exceeds two standard deviations
  and exit below one, plus a short-term reversal signal on two-standard-deviation monthly
  moves. In the real strategy a discretionary check removes false positives; the backtest
  approximates it by skipping trades where other value metrics disagree.

The two are designed for different points in a market cycle (underreaction first,
overreaction later), and the backtests have low or negative rolling correlation. Each
sleeve runs at about 8% volatility; combined, the integrated strategy runs at 10.5%.
Over 1993–2018 the hypothetical integrated strategy earned about 12% a year over cash, a
gross Sharpe ratio of about 1.2, with correlations of 0.03 to equities and 0.00 to bonds,
and Sharpe ratios that held up across growth/inflation regimes.

Regressions show the Credit Suisse Global Macro hedge fund index loads on equities,
bonds and the systematic sleeve, slightly negatively on the opportunistic sleeve, and has
no significant alpha. The integrated strategy, regressed the other way, shows an alpha
of about 11% a year with an R² of 3%. Against a five-style multi-asset portfolio (value,
momentum, carry, defensive, trend) the correlation is 0.3 and a 50/50 mix has a Sharpe
ratio above 1.4.

## Why it's in the library

It sets out cleanly the behavioural case for two macro signals that coexist: trends in
fundamentals (underreaction) and extreme dislocations (overreaction), and why combining a
steady trend sleeve with a lumpy contrarian one smooths risk. The chart of how few
deep-value opportunities exist in calm years (2004–2006) is a useful reminder that value
strategies cannot be run at constant risk.

It is a marketing white paper for an AQR strategy. All results are gross-of-fee
hypothetical backtests, discounted by AQR for data mining in an unstated way; the
discretionary step of the live strategy cannot be backtested; and the 11% alpha is
against a hedge fund index, not against an investable alternative. The design logic is
the useful part, not the performance numbers.

## Links

- [[soros-2013]] — the paper opens with Soros on catching trends early and reversals
  late, the same two-sided view of markets
- [[aqr-2020-fire-and-ice-inflation-and-deflation]] — the same firm on why trend and
  macro momentum strategies help when inflation surprises in either direction
- [[keller-keuning-2023-haa]] — a much simpler rules-based tactical allocation driven by
  trends
