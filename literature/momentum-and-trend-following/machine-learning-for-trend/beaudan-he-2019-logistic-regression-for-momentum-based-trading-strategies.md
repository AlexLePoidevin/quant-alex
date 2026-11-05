# Applying Machine Learning to Trading Strategies: Using Logistic Regression to Build Momentum-based Trading Strategies

| | |
|---|---|
| **Authors** | Patrick Beaudan (Belvedere Advisors / Emotomy); Shuoyuan He (Tulane University) |
| **Year** | 2019 (draft dated January 2019) |
| **Type** | Working paper, SSRN 3325656, 78pp. Daily S&P 500 price index 1927–2018, plus seven other equity indices |
| **PDF** | Local copy only (SSRN working paper; no open licence) |
| **BibTeX** | `beaudan2019logistic` |
| **Status** | Reference: §3.2 (design), Table 5 and Figures 3–6 (results by polynomial degree and horizon), §6 (long-short and other indices) |

## What it is

A single-index timing rule: each day, a logistic regression predicts whether the S&P 500's
annualised return over the next few days will exceed 5%. If yes, hold the index; if no, go to
cash (or short, in the long-short version).

- **Inputs.** Momentum over 30 to 360 business days and drawdowns over 15 to 120 days, all
  from the index price alone, plus every polynomial combination of them up to a chosen degree
  (455 features at degree three, 1,820 at degree four), with L2 regularisation (λ = 1).
- **Training.** The first 40% of the data (1927–1964) trains the model. The strategy then walks
  forward from August 1964, and retrains on a sliding window when the cost function on the
  new data stops changing. This gave seven training periods.
- **Headline result.** With cubic features and a three-day horizon, the long-only rule
  returned 8.6% a year from 1964 to 2018 with a Sharpe ratio of 0.54, against 0.35 for the
  price index, a 45% maximum drawdown, and average daily drawdown cut from −11.2% to −7.8%.
  The long-short version returned 10.0% with a similar Sharpe ratio (0.55). A classic 12-1
  dual-momentum rule with the same 5% hurdle did worse than buying and holding.
- **Other indices.** Applied unchanged, it added little to US mid caps, reduced returns
  slightly on the Dow Industrials (6.4% to 6.1%, with much smaller drawdowns), and improved
  the FTSE 100, Topix, FTSEurofirst 300 and Dow Transports.

## Why it's in the library

It shows how much design freedom sits inside a "simple" machine-learning trend rule, and
why the reported numbers are an upper bound.

- **The settings were chosen on the reported period.** The polynomial degree (three beat two
  and four) and the three-day horizon (best of 1 to 21 days) were picked by comparing results
  over the same 1964–2018 walk-forward that is then reported. The authors concede this in
  §6.2. The other-index tests are the closest thing to an out-of-sample check, and there the
  results are mixed.
- **No costs, and frequent trading.** The rule trades daily with average annual turnover of
  19.8 (about ten round trips a year), and slippage, costs and taxes are ignored.
- **Price index only.** The S&P 500 series excludes dividends, and the paper does not say
  what cash earns, so the comparison with buy-and-hold is not a total-return comparison.
- **The overfitting check is weak.** Training and test cost functions being close says the
  classifier is not memorising, not that the trading rule will hold up.

## Links

- [[kim-kim-2021-deep-asset-allocation-for-trend-following-investing]] — deep learning used to weight a stock trend portfolio, with similar caveats
- [[hoffstein-sibears-2018-diversifying-the-what-how-and-when-of-trend-following]] — why picking one signal, lookback or horizon from a backtest is a hidden risk
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — a trend rule derived from a model instead of searched for
- [[carr-lopez-de-prado-2014-determining-optimal-trading-rules-without-backtesting]] — setting trading-rule parameters without searching backtests
