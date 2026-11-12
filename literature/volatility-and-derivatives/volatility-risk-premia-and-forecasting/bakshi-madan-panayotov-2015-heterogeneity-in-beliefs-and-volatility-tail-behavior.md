# Heterogeneity in Beliefs and Volatility Tail Behavior

| | |
|---|---|
| **Authors** | Gurdip Bakshi, Dilip Madan, George Panayotov |
| **Year** | 2015 (*Journal of Financial and Quantitative Analysis* 50(6), 1389–1414, December 2015; earlier SSRN 2024592). The source file is labelled 2016 |
| **Type** | Journal article, 26pp. Theory plus VIX option returns, March 2006 – December 2013 (93 months) |
| **PDF** | Not hosted in this repository (journal version) |
| **Find it** | [doi.org/10.1017/S0022109015000642](https://doi.org/10.1017/S0022109015000642) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Heterogeneity+in+Beliefs+and+Volatility+Tail+Behavior%22+Bakshi) |
| **BibTeX** | `bakshi2015heterogeneity` |
| **Status** | Reference: §II (model and Theorem 1) and Table 2 (VIX option returns by moneyness) carry the argument |

## What it is

A model of the market for volatility itself, and a test of it on VIX options.

- **The usual view.** Investors dislike high volatility, so the pricing kernel rises with
  volatility. Under that view, puts on volatility (bets that volatility falls) should have
  positive expected returns that *fall* as the strike rises, and deep out-of-the-money
  volatility puts should be the best-performing.
- **The model.** Two groups of investors disagree about volatility: one expects it to rise,
  the other to fall. Volatility claims are in zero net supply, so every long is someone
  else's short. With this disagreement the pricing kernel is U-shaped in volatility:
  investors pay up for protection in both tails, low volatility as well as high. Then
  expected returns on volatility calls fall with strike, and expected returns on volatility
  puts *rise* with strike, so deep OTM volatility puts are the worst.
- **The test.** One non-overlapping 28-day return per month for VIX calls and puts at about
  5%, 15% and 25% out of the money, bought at the ask, March 2006 – December 2013.
  - **Puts:** average returns are +10.2% (5% OTM), +4.5% (15%) and −32.7% (25%), so they
    rise with strike, as the model predicts. Bootstrap tests reject "25% OTM ≥ 15% OTM" at
    0.8% and the Patton–Timmermann monotonicity test gives p = 0.049.
  - **Calls:** −27.4%, −31.3% and −34.8%, consistent with both views.
- **Verdict.** The left tail of volatility (puts) favours the heterogeneous-beliefs model
  over the standard one.

## Why it's in the library

Most work on the volatility risk premium looks at one number, the gap between implied
and realised variance. This paper looks at the *shape* of the premium across strikes and
argues that the left tail of volatility is priced too: deep OTM VIX puts are expensive,
not just VIX calls. That is relevant to anyone selling or buying volatility outright.

The evidence is thin, and the paper says so in part:

- **Ninety-three monthly returns per option**, and none of the six average returns is
  significantly different from zero (all the 90% bootstrap intervals include zero). Only
  the *differences* across strikes are significant.
- **Ask prices** make every option return look worse, more so for cheap deep OTM options,
  where the spread is a larger share of the price. That alone pushes the 25% OTM put return
  down.
- **The sample** contains one dominant volatility episode (2008).

## Links

- [[carr-wu-2009-variance-risk-premia]] — the variance risk premium as a single number,
  which this paper breaks down by tail
- [[carr-madan-2014-joint-modeling-of-vix-and-spx-options]] — pricing VIX options jointly
  with SPX options, the instruments tested here
- [[dupire-2006-model-free-results-on-volatility-derivatives]] — model-free bounds on VIX
  derivatives
- [[carr-lee-2007-realized-volatility-and-variance-options-via-swaps]] — pricing options on
  volatility from swap prices
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  buying VIX calls cost and paid in a portfolio, 2006–2017
