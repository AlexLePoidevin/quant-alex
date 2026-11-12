# Portfolio Protection? It's a Long (Term) Story…

| | |
|---|---|
| **Authors** | Nicholas McQuinn, Ashwin Thapar, Dan Villalon (AQR Capital Management) |
| **Year** | 2021 |
| **Type** | Journal article, *The Journal of Portfolio Management* 47(3), February 2021 (Portfolio Construction special issue), 18pp |
| **PDF** | Not hosted in this repository (JPM reprint; "illegal to make unauthorized copies") |
| **Find it** | [doi.org/10.3905/jpm.2020.1.203](https://doi.org/10.3905/jpm.2020.1.203) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Portfolio+Protection%3F+It%27s+a+Long+%28Term%29+Story%E2%80%A6%22+McQuinn) |
| **BibTeX** | `mcquinn2021protection` |
| **Status** | Reference: Exhibit 2 (why long bad outcomes matter), Exhibit 3 (puts) and Exhibits 7–8 (all strategies compared) carry the argument |

## What it is

An argument, with backtests, that investors should hedge against *long* bad periods rather
than sharp crashes, and that put buying does the opposite.

- **Length matters, not only depth.** Two 20% losses in a portfolio otherwise earning 6% a
  year: spread over a year, the loss also wipes out a year of returns; over a month, only a
  month's worth. For a US 60/40 portfolio (August 1971–March 2020), the worst quarters
  barely dent the chance of beating cash + 5% over the next ten years, while a bad
  three-year stretch can mean no wealth growth for a decade. Tech Bust (−22% over 24
  months) versus GFC (−30% over 16 months) is the worked anecdote.
- **Puts protect fast, not slow.** Quarterly 10% and 20% out-of-the-money S&P 500 puts
  (1996–2020) beat 60/40 in its bad outcomes up to about three years; at ten years they
  lose even in 60/40's worst decades, because the volatility risk premium accumulates.
  Their unconditional hit rates against 60/40 are 15% and 12%.
- **What holds up.** Defensive equities (low beta plus quality), a three-asset risk-parity
  portfolio, a market-neutral "styles" portfolio (value, momentum, carry, defensive) and
  multi-asset trend following all beat 60/40 in its bad outcomes, with the margin growing
  with horizon. Trend leads for bad outcomes up to a year, styles for longer ones. An
  equal-weight mix of the four does best overall.
- **COVID-19.** A short crash: puts did well, trend did well, styles were mixed (value and
  currency carry lost), and the combined portfolio beat 60/40 by about its usual margin.

## Why it's in the library

It reframes tail hedging around the investor's horizon, and the "fast versus slow"
distinction is useful whatever one concludes. It pairs naturally with the Ambrus and Szado
notes, which make the case for options-based protection.

It is also a manager's case for the strategies it sells, and some of the result is built in.
The styles and trend backtests are *scaled down* to Sharpe ratios of 0.8 and 0.6, and the
paper notes that their outperformance in 60/40's bad periods is then "by construction",
because a strategy with no market exposure and a positive average return beats a falling
60/40 almost automatically. Overlapping long-horizon windows mean a handful of episodes
drive the long-horizon results, and all returns are gross of fees.

## Links

- [[ilmanen-et-al-2021-tail-risk-hedging-contrasting-put-and-trend-strategies]] — the companion AQR paper comparing puts and trend directly in the worst S&P 500 months
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]] — the long-volatility side of the argument: why rule-based puts bleed and how a manager says to fix it
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — small long-VIX positions in a 60/40: big help in 2008, steady drag otherwise
- [[carr-wu-2009-variance-risk-premia]] — the variance risk premium that makes holding puts a long-run cost
- [[hood-et-al-2019-risk-parity-is-not-short-volatility]] — AQR's answer to the claim that risk parity is a hidden short-volatility trade
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — why trend rules work when bull and bear markets persist
- [[bessembinder-2020-extreme-stock-market-performers-expect-some-drawdowns]] — single-stock drawdowns of 30–50% even among the biggest long-run winners
- [[cfm-2018-the-convexity-of-trend-following]] — how much equity convexity a diversified trend programme actually keeps
