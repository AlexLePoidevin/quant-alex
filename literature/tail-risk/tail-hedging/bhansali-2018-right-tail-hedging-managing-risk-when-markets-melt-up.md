# Right Tail Hedging: Managing Risk When Markets Melt Up

| | |
|---|---|
| **Authors** | Vineer Bhansali (LongTail Alpha) |
| **Year** | 2018 |
| **Type** | Journal article, *The Journal of Portfolio Management* 44(7), Summer 2018, 55–62, 8pp. doi:10.3905/jpm.2018.44.7.055 |
| **PDF** | Local copy only (Institutional Investor journal download, all rights reserved) |
| **BibTeX** | `bhansali2018right` |
| **Status** | Reference: the jump-diffusion pricing example and the one-jump skew formula carry the argument; the rest is market commentary from early 2018 |

## What it is

A tail-hedging manager's case for buying **call** options as a hedge against a market that
rallies hard, the mirror image of buying puts against a crash. It was written in early 2018,
after the post-election rally, and argues that conditions then made upside convexity cheap.

- **Draw-ups are as real as drawdowns.** Since 1950 the S&P 500's worst drawdown was about
  50%, while its draw-ups were several times larger; from 2015 to early 2018 the worst
  drawdown was about 12% inside a 50% draw-up. Studies that "prove" buying options loses
  money mostly use samples without melt-ups.
- **A worked example.** On 1 September 2017 a one-year 5% out-of-the-money S&P call cost
  2.67% (implied vol 12.14%, delta 0.33). By 2 January 2018 it was worth 6.45% while the index
  rose 8.91%; on an equal-delta basis the call returned 10.88%. The author calls the example
  "cherry-picked" himself.
- **Why calls looked cheap.** Low call implied volatility (volatility sellers write calls and
  puts symmetrically, and need more calls than puts for the same premium), a steep put–call
  skew driven by collars, passive inflows, cheap capital and buybacks, and credit and
  long–short managers who can only keep up with an equity rally through synthetic upside.
- **Jumps make calls dearer than Black–Scholes says.** With Merton's jump diffusion, 12%
  diffusion volatility and one certain 10% up-jump, a one-year 5% out-of-the-money call is
  worth 4.23% instead of about 2.9%, roughly 50% more; for a one-month option the gap is
  close to fourfold.
- **A one-jump skew formula.** With a small probability p of an up-jump of size J, the
  implied volatility needed in Black–Scholes rises by roughly pJ divided by S√t, plus a
  strike-dependent term. Three consequences follow: implied vol can rise as the market rises
  ("spot up, vol up"), the effect is largest for short-dated options, and it is largest when
  volatility starts low. The extra gamma from an unpriced up-jump is what can force dealers
  who hedge with Black–Scholes to chase a rally.
- **Behavioural side.** A call fixes the maximum loss at the premium, so it works as a
  pre-commitment device against the disposition effect (taking gains too early, holding
  losses too long). It also fits a log-periodic "bubble" curve (Sornette) to the S&P 500 from
  2015 to January 2018.

## Why it's in the library

It is the upside half of the tail-hedging argument: the same convexity logic as put
protection, applied to the risk of being under-invested in a melt-up, and a short, clear
example of how a single jump changes option prices, skew and dealer gamma. It sits with
[[merton-1976]] (the jump-diffusion model it uses) and with the dealer-gamma notes in
`../volatility-and-market-structure/`.

It is a manager's argument rather than a test. There is no backtest of a call-buying
programme, the headline trade is one hand-picked option over four months, the jump
probability and size are assumed, and the log-periodic fit is illustrative. Its timing was
also unlucky in the short run: the article went to press around the February 2018 volatility
spike, which the author himself anticipated might turn the right tail into a left one.

## Links

- [[merton-1976]] — the jump-diffusion option model behind the pricing example
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  left-tail counterpart: what long volatility and puts did for a portfolio
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — another option-hedging manager on why hedges should be bought on price, not on a schedule
- [[squeezemetrics-2020-the-implied-order-book]] — dealer gamma and how hedging flows can push
  the index, the mechanism behind the melt-up feedback loop here
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the short-volatility build-up of the same
  period, seen from the downside
