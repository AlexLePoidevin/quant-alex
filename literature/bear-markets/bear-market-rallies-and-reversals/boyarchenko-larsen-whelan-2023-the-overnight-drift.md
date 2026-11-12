# The Overnight Drift

| | |
|---|---|
| **Authors** | Nina Boyarchenko (Federal Reserve Bank of New York), Lars C. Larsen and Paul Whelan (Copenhagen Business School) |
| **Year** | 2023 (published); first circulated February 2020 |
| **Type** | Paper. *Review of Financial Studies* 36(9), 3502–3547 (doi 10.1093/rfs/hhad020). The copy is Federal Reserve Bank of New York Staff Report no. 917, revised April 2022, 98pp with appendix |
| **PDF** | Not hosted in this repository (copyright). The Federal Reserve Banks are not federal agencies, so their staff reports are not US-government works in the public domain; the report carries no open licence, and the journal version is Oxford University Press |
| **Find it** | [doi.org/10.1093/rfs/hhad020](https://doi.org/10.1093/rfs/hhad020) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22The+Overnight+Drift%22+Boyarchenko) |
| **BibTeX** | `boyarchenko2023overnight` |
| **Status** | Reference: the introduction, §II–III (where the drift sits and the order-imbalance sorts), §IV (predictive regressions and the daylight-saving experiment) and §V (trading strategies with and without costs) carry the results |

## What it is

A study of S&P 500 E-mini futures returns around the clock, January 1998 to December 2020,
from tick data. US equity futures returns do not accrue evenly over 24 hours. The single
largest positive hour is **2:00–3:00 a.m. New York time, the opening of European markets**,
averaging about 3.6% a year on its own. The authors call this the **overnight drift**.

- **It is robust.** It survives a bootstrap over all hours and Bonferroni-adjusted p-values (the
  only window consistently significant). It is positive in 20 of 23 years (significant in 17),
  on every weekday and in 9 of 12 months.
- **It follows the previous day's selling.** The authors measure end-of-day order imbalance as
  signed over gross volume in the last hour of US trading. Large net selling at the US close is
  followed by large price reversals overnight, as dealers who bought it sell to traders arriving
  in Asia and Europe. Large net buying is followed by much smaller reversals. When the closing
  imbalance is near zero, there is no reversal. This **asymmetry** is what makes the average
  overnight return positive.
- **It is bigger when volatility is high.** In a regression with an interaction, a
  one-standard-deviation more negative closing imbalance predicts about 2.6 bp in the 2:00–3:00
  hour with the VIX at 20, about 6.1 bp with the VIX at 30, and roughly nothing with the VIX at
  12.
- **It moves with the arrival of traders.** Japan has no daylight saving time, so Tokyo's open
  shifts by an hour in New York time between winter and summer, and the predictability around
  the Tokyo open shifts with it. The same happens around the London and Frankfurt open in the
  weeks when US and European clocks change on different dates. This is the paper's natural
  experiment for an inventory-risk explanation.
- **Explanation.** A Grossman–Miller inventory model, in which dealers are paid for absorbing
  order imbalances until new traders arrive. The asymmetry is attributed to dealers' risk
  capacity: selling pushes volatility up (the leverage effect), dealers' value-at-risk limits
  tighten, and they demand more to hold the inventory.
- **Trading it.** Over 2007–2020, holding the futures only from 2:00 to 3:00 has a Sharpe ratio
  of about 1 before costs and is unprofitable after paying the bid-ask spread. A "buy the dip"
  version that holds 1:30–3:30 only after days with net selling at the close has a Sharpe ratio
  of about 1.8 before costs and is the only one still profitable after costs, because it trades
  on about half the days. It does not beat simply holding the index in total return.

## Why it's in the library

It shows, at hourly frequency, the same **asymmetric rebound after sell-offs** that this section
studies at the scale of bear markets. Selling pressure is absorbed by intermediaries whose
willingness to take risk shrinks when volatility rises, and the price recovers when new buyers
arrive. Reversals after selling are larger than after buying, and larger when the VIX is high.
It is also a reminder that "markets bounce after a bad day" is mostly compensation for liquidity
provision, and largely disappears once you pay the spread.

The pre-cost Sharpe ratios are reported inconsistently: the introduction gives about 1.0 for the
2:00–3:00 strategy and 1.2 for 1:30–3:30, while §V gives 1.2 and 1.3. The after-cost conclusion
is the same either way. The strategies are on one contract, and the profitable one relies on
the closing order-imbalance signal, which needs signed tick data to compute. A later New York
Fed *Liberty Street Economics* post is titled "The Disappearing Overnight Drift" (2026); it was
not read for this note.

## Links

- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — dealers' risk-bearing capacity in
  options, the same intermediary-constraint story in a different market
- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — order-flow imbalance and volume time
  in the same E-mini contract
- [[barbon-buraschi-2021-gamma-fragility]] — dealer positioning that amplifies moves instead of
  absorbing them
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — rebounds inside a bear
  regime, at weekly rather than hourly frequency
- [[johannsen-2016-dead-cat-bounce]] — a behavioural rather than liquidity explanation for
  rebounds after a fall
- [[barth-mitchell-sun-2020-runs-to-banks-cash-sweeps-during-market-downturns]] — where retail selling goes in a downturn: brokerage cash swept into bank deposits
- [[baur-kuck-2020-the-timing-of-the-flight-to-gold]] — intraday gold on crash days: the flight to gold keeps building after the US close
- [[collin-dufresne-daniel-2015-liquidity-and-return-reversals]] — the single-stock version: how much of a non-news price shock reverses, and how fast
