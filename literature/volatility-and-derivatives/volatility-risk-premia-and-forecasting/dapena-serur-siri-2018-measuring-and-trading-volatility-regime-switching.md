# Measuring and Trading Volatility on the US Stock Market: A Regime Switching Approach

| | |
|---|---|
| **Authors** | José P. Dapena, Juan A. Serur, Julián R. Siri (Universidad del CEMA) |
| **Year** | 2018 (November 2018) |
| **Type** | Working paper, UCEMA Documentos de Trabajo 659, SSRN 3257073, 27pp |
| **PDF** | Local copy only (working paper, no open licence) |
| **BibTeX** | `dapena2018volatility` |
| **Status** | Read in full |

## What it is

A hidden Markov model of the volatility risk premium, used to switch between selling
volatility and holding Treasuries.

- **The signal.** The spread between last month's VIX and the 30-day close-to-close
  realised volatility of the S&P 500, a rough measure of the volatility premium. It is
  usually positive.
- **The regimes.** A two-state model fitted to the whole sample finds a calm state (mean
  spread 5.1 vol points, low variance, expected duration about 49 days, about 75% of the
  time) and a turbulent state (mean 1.9, much higher variance, about 18 days). A
  three-state version adds a state with a negative mean spread (−7.0) that is active about
  40% of the time.
- **The strategy.** Re-estimate the model every day on two years of data, decode the most
  likely current state (Viterbi), and hold an inverse-VIX product (ZIV or SVXY) in the calm
  state and the 7–10 year Treasury ETF (IEF) otherwise. Trades are entered the day after
  the signal, at 10bp cost. Before ZIV and SVXY existed, the products are replicated with
  VIX futures. Sample April 2004 to October 2018.
- **Reported results.** Buy-and-hold: S&P 500 8.5% a year (Sharpe 0.46), ZIV 10.1% (0.34),
  SVXY 14.6% (0.24, maximum drawdown −93%). Switching: 17.2% (ZIV, Sharpe 0.80), 45.1%
  (SVXY, 1.03) and 28.8% (three states, 0.86), with drawdowns of −36% to −53%. Daily
  Carhart alphas are positive and significant, but the strategies also load heavily on the
  market (betas 0.5–1.1).
- **February 2018.** The model switched out during the volatility spike that ended XIV.
  The authors relate the event to realised volatility jumping far above what the VIX had
  implied.

## Why it's in the library

**It shows the volatility premium as a regime, not a constant.** The gap between implied
and realised volatility is wide and stable in calm markets and collapses or turns negative
in stress. A seller of volatility earns the first and must avoid the second.

**It is a simple, reproducible template for regime-filtered short volatility.** One
observable spread, a two- or three-state HMM, daily re-estimation and a switch into
bonds.

**The backtest should not be taken at face value.** The early half uses replicated
products, SVXY's leverage was cut after February 2018, and the switch into IEF benefits
from a falling-yield era. The equity betas show much of the return is ordinary market
risk, and there is no out-of-sample period after the design was fixed. The first
sub-period (2004–2010) is weak for the ZIV version (3.1% a year).

## Links

- [[carr-wu-2009-variance-risk-premia]] — the variance risk premium measured properly from option prices
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — a Markov-switching model of VIX levels themselves
- [[dapena-serur-siri-2019-risk-on-risk-off-regime-switching-model]] — the same authors' regime model applied to stock–bond allocation
- [[malkiel-et-al-2018-option-writing-using-vix-to-improve-returns]] — another rule for when to sell index options based on the VIX
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] — why short-VIX products earn the roll yield, and how risky that is
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the case that short volatility was a crowded trade before February 2018
