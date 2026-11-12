# Automation, Intermediation and the Flash Crash

| | |
|---|---|
| **Authors** | Andrei Kirilenko, Albert S. Kyle, Mehrdad Samadi, Tugkan Tuzun |
| **Year** | 2018 (SSRN 3119363) |
| **Type** | Short companion piece, 22pp, summarising the authors' *Journal of Finance* article (Kirilenko et al. 2017, "The Flash Crash: High-Frequency Trading in an Electronic Market", 72(3), 967–998) and discussing market design. CFTC account-level E-mini data, 3–6 May 2010 |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3119363](https://doi.org/10.2139/ssrn.3119363) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Automation%2C+Intermediation+and+the+Flash+Crash%22+Kirilenko) |
| **BibTeX** | `kirilenko2018automation` |
| **Status** | Reference: Figure 2 (intermediary inventories), Table 1 (aggressive/passive volume around price changes) and the section on pit versus electronic trading |

## What it is

The regulator-data account of who did what in the E-mini S&P 500 futures on 6 May 2010.

- **Data and classification.** Every E-mini transaction from 3–6 May 2010 with buyer and
  seller account IDs and an aggressor flag. Of more than 15,000 accounts, 204 that kept
  small, mean-reverting net positions on 3–5 May are classed as intraday intermediaries; the
  16 most active are high-frequency traders (HFTs), the rest market makers. HFTs did 34% of
  volume, about half of it with marketable orders.
- **Intermediaries could not absorb the sale.** The crash was triggered by a 75,000-contract
  (about $4.1bn) sell program. HFTs never held more than about 4,000 contracts net on any of
  the four days, and market makers no more than 1,500; together under 6,000. Both groups
  built net long positions as prices fell, but their risk capacity was tiny next to the order.
- **HFTs trade like quote snipers, not market makers.** HFTs' share of aggressive volume at
  the best ask rises from 34% unconditionally to 58% just before a price rise, and falls to
  15% at the new level, where their passive share rises. Prices stay about 15% of a tick
  higher 20 seconds after HFTs buy. Traditional market makers trade much more passively.
- **Market design.** A comparison of pit trading (no time priority, partial anonymity,
  scalpers, out-trades) with Globex (strict price-time priority, anonymity, speed), arguing
  that speed is the remaining advantage, and that automated intermediaries' small capital and
  short holding periods can make liquidity gaps more likely in a large imbalance.

## Why it's in the library

It is the most authoritative data on 6 May 2010, because it uses account identities that
no outside researcher has. It answers a narrower question than the toxicity account: not
whether order flow was informed, but whether the intermediaries were big enough to take the
other side, and they were not. It says intermediaries are unlikely to cause a crash but can
amplify one. For the full evidence, read the 2017 *Journal of Finance* paper; this piece adds
the market-design discussion.

## Links

- [[easley-et-al-2011-microstructure-of-the-flash-crash]] — the order-flow-toxicity (VPIN)
  account of the same day
- [[poitras-2012-what-happened-may-6-2010-anatomy-of-the-flash-crash]] — the official reports
  read against the 1987 crash
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — how
  the selling spread across the Dow stocks
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — dealer inventory limits in
  options, the same constraint on a different set of intermediaries
- [[cole-2018-what-is-water-in-markets]] — February 2018 read as a liquidity event, with
  E-mini depth down 95%
