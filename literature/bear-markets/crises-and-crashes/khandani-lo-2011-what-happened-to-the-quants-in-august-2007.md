# What Happened to the Quants in August 2007? Evidence from Factors and Transactions Data

| | |
|---|---|
| **Authors** | Amir E. Khandani, Andrew W. Lo (MIT; Lo also AlphaSimplex Group) |
| **Year** | 2011 (journal); this copy is the 23 October 2008 revision |
| **Type** | Journal article, *Journal of Financial Markets* 14(1), 1–46, 2011. Earlier as NBER Working Paper 14465 and SSRN 1288988. US stocks (S&P 1500), daily and 5-minute TAQ data, 2007 |
| **PDF** | Not hosted in this repository (SSRN working-paper version, no open licence) |
| **Find it** | [doi.org/10.1016/j.finmar.2010.07.005](https://doi.org/10.1016/j.finmar.2010.07.005) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22What+Happened+to+the+Quants+in+August+2007%3F+Evidence+from+Factors+and+Transactions+Data%22+Khandani) |
| **BibTeX** | `khandani2011quants` |
| **Status** | Reference: §3–4 (factor simulations), §5 (intraday market-making strategy) and §6 (conclusions, with the authors' caveats) |

## What it is

A forensic reconstruction of the "Quant Meltdown": the week of 6 August 2007 when
quantitative long/short equity hedge funds lost heavily at once (press reports: one large
fund −30% in a week, others −5% to −20% in August) while the stock market barely moved.

- **The unwind hypothesis.** One or more large portfolios were liquidated fast, probably to
  raise cash or cut leverage after losses elsewhere. Because many quant funds held similar
  factor bets, the price impact hit all of them, forcing further deleveraging.
- **Factor simulations.** Long/short decile portfolios on five factors: book-to-market,
  earnings-to-price, cashflow-to-market, price momentum and earnings momentum. Through July
  2007 the value portfolios steadily declined while momentum rose, which the authors read as
  a slow unwind already under way. Daily cross-sectional regressions of returns on the
  factors had R² spiking above 10% in early August.
- **Intraday detail.** Five-minute portfolio returns point to two unwinds: a mini-unwind on
  1 August (10:45–11:30am) and a sustained one from the open on 6 August to about 1pm,
  starting in financials and in long book-to-market, short earnings-momentum positions.
  Value portfolios fell on 2–3 August; earnings momentum was hit on 8–9 August. On Friday
  10 August sharp reversals erased nearly all losses since 6 August.
- **Leverage arithmetic.** At 8:1 leverage, the book-to-market portfolio would have lost 24%
  from the morning of 1 August to the close of 7 August, enough to force cuts that would
  then have missed the rebound.
- **Market-making withdrew.** A 5-minute contrarian strategy (buy recent losers, sell recent
  winners), standing in for liquidity provision, lost significantly in the week of 6 August
  but made money before and after, suggesting market makers pulled risk capital from about
  8 August. Weekly volume hit record levels of 2.9–3.6 billion shares in late July to
  mid-August.

## Why it's in the library

- It is the reference case for crowding as a systemic risk: when many managers hold the same
  factor tilts, one fund's forced selling becomes everyone's loss, regardless of how sound
  each portfolio looked alone.
- It shows the two-stage pattern that recurs in later crises: slow deleveraging of a crowded
  position, then a liquidity air-pocket when market makers step back, then a sharp reversal.
- The evidence is indirect, as the authors stress: simulated strategies stand in for
  unobserved fund holdings, with no access to prime-brokerage or fund data, and US
  long/short simulations proxy for a broader, international industry. The ultimate trigger
  of the unwind is not identified.

## Links

- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — the short-term reversal premium earned by supplying liquidity, the strategy that broke here
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — the 2010 flash crash, another case of liquidity providers withdrawing mid-crisis
- [[arnott-et-al-2019-alices-adventures-in-factorland]] — factor crashes, crowding and why factor returns are fatter-tailed than they look
- [[lipton-lopez-de-prado-2020-three-quant-lessons-from-covid-19]] — lessons drawn from a later quant drawdown
