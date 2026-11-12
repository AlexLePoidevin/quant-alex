# Tail Risk Hedging Performance: Measuring What Counts

| | |
|---|---|
| **Authors** | Linda Chang, Jeremie Holdom, Vineer Bhansali (LongTail Alpha) |
| **Year** | 2021 (revised November 2021) |
| **Type** | Working paper, SSRN 3962552, 25pp, with the firm's disclosures |
| **PDF** | Not hosted in this repository (SSRN download marked confidential, no licence) |
| **Find it** | [doi.org/10.2139/ssrn.3962552](https://doi.org/10.2139/ssrn.3962552) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Tail+Risk+Hedging+Performance%3A+Measuring+What+Counts%22+Chang) |
| **BibTeX** | `chang2021tailhedging` |
| **Status** | Reference: the hypothetical cash-flow exhibits (1–7) make the main point; the 2017–21 and 1996–2021 backtests (Exhibits 8–11) illustrate it |

## What it is

A paper by a tail-hedging manager on how the performance of an option-based hedge should be
reported. Its claim is that the usual fund statistic, the compounded return of the net asset
value (NAV), misstates the value of a strategy whose payoffs are multiples of the money put in
and are taken out when they happen.

- **The arithmetic.** Compounded returns assume money stays in. When a hedge pays several
  times its premium and the gain is withdrawn, compounded and dollar returns diverge:
  - a 5× gain withdrawn, then a 90% loss, shows −50% compounded while the investor made
    $31 on $10;
  - a hedge that first decays to zero shows −100% compounded forever after, even if it
    later returns 500% on fresh premium.
- **The example hedge.** Buy 20% out-of-the-money one-year S&P 500 puts each quarter, and sell
  any position once it is worth 8× its cost, with spending normalised to 2% of the portfolio
  a year.
  - **2017–21:** it gained about 80% in December 2018 and 203% in March 2020. Its compounded
    NAV return is −99.99%, but in dollars it spent $10 and got back $5.10, a 49% loss.
  - **1996–2021, as an overlay on the S&P 500:** with payouts reinvested in the index, the
    hedged portfolio's annual return was about 0.57 points lower (7.49% against 8.06%). Its
    maximum drawdown was smaller (−45% against −57%), and so was its volatility (12.7%
    against 15.2%). Scaled to the same 15% volatility, it comes out about 0.8 points a year
    ahead.
- **Beyond the numbers.** It argues, by analogy with home insurance, that reliability, ease of
  monetisation and fit with the portfolio being hedged also belong in the evaluation.

## Why it's in the library

The measurement point is correct and general: for any strategy with convex payoffs and
withdrawals, report NAV, cash flows and dollar returns together, and judge the hedge on the
combined portfolio, not on its own return stream. That applies to every tail-hedge note in this
folder and to the put and VIX results in
[[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]].

Read the evidence as a manager's illustration. The backtest is the firm's own rule, chosen
after the fact ("a conservative representative backtest"), and the 2017–21 window contains two
favourable shocks. The overlay result depends on the 8× monetisation rule and on reinvesting
in the index at the low. The volatility-scaled gain of 0.8 points assumes the hedged portfolio
can be levered, and the statistics are unaudited.

## Links

- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] —
  long-VIX and put hedges judged on portfolio returns
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — a competing manager's view that rule-based hedges bleed and should be traded on price
- [[bhansali-2018-right-tail-hedging-managing-risk-when-markets-melt-up]] — the same author's
  case for upside (call) hedges, to which the measurement argument also applies
- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — puts against
  trend as crisis hedges, the alternative this paper mentions but does not test
- [[van-hemert-et-al-2020-drawdowns]] — drawdown statistics, the portfolio-level measure used
  here
- [[bhansali-holdom-2021-diversifying-diversification]] — the same firm on combining several crash hedges into one equal-risk basket
