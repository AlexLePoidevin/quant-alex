# A Safe Haven Index

| | |
|---|---|
| **Authors** | Dirk G. Baur (University of Western Australia), Thomas Dimpfl (University of Hohenheim) |
| **Year** | 2022 (version dated 27 January 2022). A later version, with a third author (Pena), was published in *Finance Research Letters* 85 (2025), 107922 |
| **Type** | Working paper, SSRN 3641589, 37pp. Daily data, January 1985 to May 2020 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `baur2022safehaven` |
| **Status** | Reference: §2 (the index), Tables 2–4 (crisis returns, risk-adjusted returns, betas to the index) and §4 (volatility) carry the results |

## What it is

A benchmark for safe-haven assets, built the way a stock index is built, and used to state
some stylised facts about them.

- **The index.** An equal-weighted average of the daily log returns of seven assets the
  literature calls safe havens: gold, the Swiss franc, the yen, US 2-, 10- and 30-year
  Treasuries, and the German 10-year Bund. Equal weights avoid choosing a "market cap" for
  currencies and bullion. The index is published by the University of Hohenheim.
- **Calm but not safe.** The index's daily standard deviation is 0.33%, against 0.96% for
  gold and 1.14% for the S&P 500. Its volatility rises in every crisis, as does that of
  every constituent: a haven's price has to jump in the crisis and fall back afterwards.
- **Crisis returns.** Crises are 20 trading days from 15 October 1987, 11 September 2001,
  15 September 2008 and 24 February 2020. The index earns more than its normal daily return
  in all four. Gold fell in the COVID window. Over the four crisis windows the return per
  unit of risk is 0.17 for the index, against 0.06 for gold, 0.18 for 10-year Treasuries,
  0.30 for 2-year Treasuries and −0.21 for the S&P 500.
- **Betas to the index in crises.** Gold 1.49, 30-year Treasuries 2.25, 2-year Treasuries
  0.24, the US dollar −0.37 and the VIX 7.1. The S&P 500's beta is −2.26, and the
  FANG tech stocks (Facebook, Amazon, Netflix, Google) are between −1.4 and −2.4, so they
  are not havens despite being called so in 2020. Bitcoin's crisis beta is −0.19 and insignificant, with an R² of
  zero: it does not move with the other havens at all.
- **Inverted volatility asymmetry.** For stocks, falls raise volatility more than rises. For
  the safe-haven index it is the other way round (a GJR-GARCH asymmetry term of −0.025,
  against +0.14 for the S&P 500). The effect disappears once the four crisis windows are
  dummied out, so it comes from the crises themselves.
- **COVID was different.** In March 2020 the index briefly fell with stocks, unlike in any
  of the earlier crises. The authors suggest havens were sold to raise cash, which is what
  insurance is for.
- **Diversifying the havens.** The index has a better crisis return-to-risk than most of its
  constituents, so diversification among havens works even in crises. The single best
  haven on both raw and risk-adjusted returns was the 2-year Treasury, helped by central
  bank buying. Dropping gold from the index leaves the main findings intact. The haven
  effect is strongest over 5–10 days and fades after about 20.

## Why it's in the library

**It gives "safe haven" a benchmark.** Without one, any asset that happened to rise in the
last crisis gets the label. Measuring betas to a basket of established havens shows which
assets actually behave like them: gold and long Treasuries do; Bitcoin and big tech stocks
do not.

**Safe havens are risky assets.** Their volatility jumps in exactly the periods they are
held for. That matters for anyone sizing a defensive sleeve on calm-period volatility.

**Read the numbers as four episodes.** Every crisis result rests on four hand-picked 20-day
windows, and the view is that of a US-dollar investor. The equal weights put three of the
seven slots in US Treasuries, so the index leans towards US duration. The text gives the
9/11 start as "September 11, 2011", a typo; Table 4's crisis standard errors repeat the
full-sample ones; and the Table 5 note says monthly data although the analysis is daily.

## Links

- [[baur-2021-is-gold-a-safe-haven-in-all-currencies]] — the same author on why gold's
  safe-haven role depends on the investor's currency
- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — when, within the day, gold starts to
  rise in a crash
- [[baur-trench-2022-not-all-gold-shines-in-crisis-times]] — gold rose in the COVID crash
  while gold-mining shares fell with the market
- [[erb-harvey-2013-the-golden-dilemma]] — the usual arguments for holding gold, tested one
  by one
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] — how often
  stocks and bonds crash together, and how often bonds rally instead
- [[stavrakeva-tang-2019-the-dollar-during-the-great-recession]] — why the dollar
  strengthened in the 2008 crisis
