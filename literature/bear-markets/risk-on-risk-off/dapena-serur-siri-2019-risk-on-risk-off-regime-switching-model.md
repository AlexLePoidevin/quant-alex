# Risk On-Risk Off: A Regime Switching Model for Active Portfolio Management

| | |
|---|---|
| **Authors** | José P. Dapena, Juan A. Serur and Julián R. Siri (Universidad del CEMA, Buenos Aires) |
| **Year** | 2019 |
| **Type** | Working paper. UCEMA Documentos de Trabajo 706 (December 2019); SSRN 3509895 (doi 10.2139/ssrn.3509895), 13pp |
| **PDF** | Local copy only (working paper; no open licence) |
| **BibTeX** | `dapena2019riskon` |
| **Status** | Reference: short paper; §2 (signal and trading rule), Table 1 (strategy statistics, April 2004 to October 2018) and Table 2 (factor regressions) carry the results |

## What it is

A two-fund switching strategy between the S&P 500 (SPY) and Treasuries. A hidden Markov model
(HMM) chooses between them.

- **The signal.** The volatility spread: the previous month's VIX minus 30-day realised
  volatility. The HMM is estimated with Baum–Welch and the most likely state is read with the
  Viterbi algorithm. The method is taken from the authors' 2018 paper on trading volatility
  regimes.
- **The rule.** When the most likely state is calm (a high spread, implied volatility well above
  realised), hold SPY. When it is turbulent (realised volatility catching up with implied),
  hold Treasuries. Trades are made the day after the signal. The two-state version switches about
  16 times a year; a three-state version switches about 55 times.
- **Results, April 2004 to October 2018.**

  | | S&P 500 | Switching strategy |
  |---|---|---|
  | Annual return | 8.48% | 11.36% |
  | Volatility | 18.3% | 12.7% |
  | Sharpe ratio | 0.46 | 0.89 |
  | Max drawdown | −55.2% | −26.0% |

  Regressed on the Fama–French and Carhart factors, the strategy has a daily alpha of 0.03%
  (t ≈ 3.1, about 7.5% a year) and a market beta of about 0.33.
- **The proposal.** Since the switch is simple, the authors suggest adding it to the
  Fama–French and Carhart models as an "active premium" factor.

## Why it's in the library

It is a compact example of the most common risk-on/risk-off rule: hold equities when implied
volatility sits comfortably above realised volatility, and step aside when realised volatility
catches up.

The evidence is weaker than the table suggests:
- **Possible look-ahead.** As described, the HMM is fitted with Baum–Welch and decoded with
  Viterbi. Viterbi picks the most likely path of states using the whole sample, including later
  data. Unless the model was re-estimated and decoded only on past data at each date (the paper
  doesn't say), each state call uses information from after the trade. Trading one day later
  doesn't remove that.
- **No trading costs.** The two-state rule switches about 16 times a year, and the paper
  charges no costs.
- **The risk-off asset is unclear.** The text describes it in three ways: short-term Treasury
  bills, 7–10 year Treasuries, and in one place a short position in SPY.
- **One sample, no robustness checks.** There is a single 14-year sample and no tests of
  sensitivity to the method or the period.

The alpha is the return from sitting out the volatile periods, mostly 2008. It is not a
separate premium.

## Links

- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching applied to the VIX
  itself
- [[ang-timmermann-2012-regime-changes-and-financial-markets]] — why two-state models of returns
  mostly separate calm from turbulent periods, which is what this signal trades on
- [[haase-neuenkirch-2023-predictability-of-bull-and-bear-markets]] — a stock-or-bonds switching
  strategy built from real-time regime forecasts, with publication lags and costs handled
- [[smales-2016-risk-on-risk-off-financial-market-response-to-investor-fear]] — how markets
  respond when the VIX jumps
- [[keller-keuning-2016-paa]] — a rule-based allocation that also moves to bonds when the
  market weakens
- [[dapena-serur-siri-2018-measuring-and-trading-volatility-regime-switching]] — the authors' earlier regime model, applied to short volatility
