# Can Market Regimes Really be Timed with Historical Volatility?

| | |
|---|---|
| **Authors** | Richard McGee (Smurfit School of Business, University College Dublin) |
| **Year** | 2021 |
| **Type** | Working paper, SSRN 3832340 (April 2021) |
| **PDF** | `mcgee-2021-can-market-regimes-really-be-timed-with-historical-volatility.pdf` (kept locally; SSRN download with no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3832340](https://doi.org/10.2139/ssrn.3832340) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Can+Market+Regimes+Really+be+Timed+with+Historical+Volatility%3F%22+McGee) |
| **BibTeX** | `mcgee2021regimes` |
| **Status** | Reference: Section 2 (replication and robustness of Moreira–Muir), Table 5 (out-of-sample comparison) and Figure 4 (rebalancing-day sensitivity) carry the results |

## What it is

A replication and stress test of volatility-managed portfolios (Moreira and Muir, 2017):
scale market exposure down when last month's realised volatility is high and up when it is
low. The paper asks whether recent volatility really tells you which regime you are in.

- **Replication.** On Kenneth French's US market factor, 1926–2015, the volatility-managed
  version has a Sharpe ratio of 0.52 against 0.42 for buy-and-hold, with an annual alpha of
  6.4%, matching the original paper.
- **Leverage.** With leverage capped at 1, the Sharpe advantage shrinks to 0.427 against
  0.416 before costs, and most of it comes from the late 1920s.
- **Twenty-year investors.** Over 70 rolling twenty-year windows the levered strategy has the
  lower Sharpe ratio in 30, the unlevered one in 58. Its Sharpe ratio never beats the 10th
  percentile of bootstrapped buy-and-hold Sharpe ratios, and its alpha is significant only
  in windows containing the 1920s–30s or 2008.
- **Rebalancing day.** Moving the monthly rebalance from the last business day to 9–12 days
  earlier turns the outperformance into underperformance. The difference comes from a
  handful of months around big market events.
- **A regime test.** Each month, using only past data, the paper picks the volatility
  threshold that best separates a "bear" month from a "bull" month for a mean-variance
  investor, and the best portfolio of stocks and Treasuries for each. Out of sample,
  December 1969 to December 2016, the Sharpe ratios are 0.436 for buy-and-hold, 0.46 for a
  rolling mean-variance portfolio, 0.433 for the regime-timed portfolio and 0.277 for
  Moreira–Muir. The chosen bear portfolio is always 100% Treasuries, and returns in the two
  volatility regimes differ little (11.7% against 10.9% a year).

## Why it's in the library

- **A check on volatility targeting.** Scaling exposure by recent volatility is one of the
  most common defensive rules. This paper shows that the headline evidence for it on the
  equity market depends on leverage, the 1920s–30s, and the day of the month the portfolio
  is rebalanced.
- **The rebalancing-day result generalises.** A strategy whose value changes sign when the
  trade date moves by two weeks is relying on the timing of a few events. That is a test
  worth running on any monthly-rebalanced rule.
- **Limits.** This is one market factor and an unpublished paper. It does not cover the
  multi-asset volatility targeting that Man Group and others study, where the evidence is
  different. The regime test assumes a mean-variance investor and a single volatility
  threshold.

## Links

- [[maheu-mccurdy-2000-identifying-bull-and-bear-markets-in-stock-returns]] — the regime
  literature that ties high volatility to bear markets, which volatility timing relies on
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — a model in which volatility
  separates bear rallies from bull markets
- [[harvey-liu-zhu-2016]] — why a rule tuned in-sample overstates its future performance
- [[carr-wu-2017-leverage-effect-volatility-feedback-and-self-exciting-market-disruptions]] — the
  leverage effect, the negative link between volatility and returns that volatility timing
  needs
- [[zegadlo-2022-identifying-bull-and-bear-market-regimes-rule-based]] — another way of
  classifying regimes, from price rules rather than volatility
