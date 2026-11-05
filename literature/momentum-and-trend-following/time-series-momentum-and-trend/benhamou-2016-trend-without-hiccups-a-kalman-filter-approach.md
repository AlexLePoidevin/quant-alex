# Trend Without Hiccups: A Kalman Filter Approach

| | |
|---|---|
| **Authors** | Eric Benhamou (then at Thomson Reuters, Paris) |
| **Year** | 2016 (April 2016; SSRN 2747102; posted to arXiv as 1808.03297 in 2018) |
| **Type** | Practitioner paper, 29pp. Four Kalman-filter models and a one-year E-mini S&P 500 trading backtest |
| **PDF** | `benhamou-2016-trend-without-hiccups-a-kalman-filter-approach.pdf` (the arXiv 1808.03297v1 copy; same text and numbers as the SSRN version) |
| **BibTeX** | `benhamou2016hiccups` |
| **Status** | Read: §3 (the four state-space models) and §5.3 (Tables 1–7) carry the content; the backtest is in-sample |

## What it is

A pitch for replacing moving averages with Kalman filters as a technical indicator.
Moving averages lag; a Kalman filter that models price *dynamics* (level plus speed)
can predict the next price with little lag, and the sign of predicted minus current price
becomes a long/short signal.

- **Moving-average lag, formally.** The lag of a k-times repeated moving average is k
  times the single lag, which recovers Mulloy's zero-lag DEMA (2·MA − MA∘MA) and TEMA.
- **Four state-space models.**
  - Model 1: price with speed and acceleration, like a car tracked by GPS (4 parameters).
  - Model 2: the local linear trend model, level plus random-walk slope (5 parameters).
  - Model 3: a short-term and a long-term price component (10 parameters).
  - Model 4: model 3 plus a drift driven by the 14-day stochastic oscillator, where the
    price sits between its recent high and low (15 parameters).
- **The trading rule.** Go long if the filter's one-step prediction is above yesterday's
  close plus an offset, short if below; one E-mini contract, $4 round-trip commission.
- **The backtest (Table 1).** Daily data, 28 February 2015 to 28 February 2016. Net
  profit: model 1 $18,755, model 2 $22,380, model 3 $29,022, model 4 $39,558, with maximum
  drawdowns of $7,348, $7,348, $3,800 and $2,600. The author concludes that model 4, which
  adds the oscillator, is far better than the rest.

## Why it's in the library

**It is a readable, code-level introduction to Kalman filters as trend signals**, with
pseudo-code for the predict and update steps and a clear statement of the state-space
models, including the local linear trend model that [[bruder-et-al-2011-trend-filtering-methods-for-momentum-strategies]]
shows is equivalent to an exponential moving average.

**The evidence does not support the conclusions, and the note records why.**
- **In-sample.** The Discussion says the parameters "are obtained by a general
  optimization" on the same single year the profits are reported for. Models 3 and 4 have
  10 and 15 fitted parameters for 48–57 trades.
- **One year, one contract, one big trade.** The best model's largest trade, a short from
  30 July to 24 August 2015 into the August selloff, made $11,309, about 29% of its net
  profit.
- **"Best" depends on the metric.** Model 4 has the highest dollar profit, but its Sharpe
  ratio (0.73) is lower than model 3's (1.22) and similar to models 1 and 2 (0.72, 0.76).
- **Small inconsistencies.** Model 3's drawdown is −3,800 in Table 1 and −3,820 in
  Table 4. The update pseudo-code adds `K·Y` (the measurement) rather than `K·I` (the
  innovation), which as written is not a Kalman update.

## Links

- [[bruder-et-al-2011-trend-filtering-methods-for-momentum-strategies]] — the survey this
  paper cites for the Kalman-equals-EMA result, with honest treatment of estimator noise
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a
  principled derivation of the optimal smoothing filter, in contrast to an in-sample search
- [[moskowitz-ooi-pedersen-2012-time-series-momentum]] — the out-of-sample, multi-asset
  evidence that trend signals work, which this one-year test cannot provide
