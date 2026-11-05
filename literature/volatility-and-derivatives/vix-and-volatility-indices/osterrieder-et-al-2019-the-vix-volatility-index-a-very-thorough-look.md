# The VIX Volatility Index: A Very Thorough Look at It

| | |
|---|---|
| **Authors** | Jörg Osterrieder, Kevin Röschli, Lars Vetter (Zurich University of Applied Sciences) |
| **Year** | 2019 (7 January 2019) |
| **Type** | Working paper, SSRN 3311727, 47pp. Data: CBOE SPX option quotes, end of day 2015 to March 2018 and one-minute January–March 2018 |
| **PDF** | Local copy only (SSRN download, no open licence) |
| **BibTeX** | `osterrieder2019vix` |
| **Status** | Reference: §3.3 (the formula), §6.3 (size of CBOE's approximations), §7 (which options drive the index) and §8 (settlement) are the results |

## What it is

The authors replicate the VIX from raw CBOE option quotes, then use the replication to
test which criticisms of the index hold up.

- **How the VIX is built.** It is a weighted sum of mid-quotes of out-of-the-money S&P 500
  puts and calls, weighted by 1/K², for a near-term (23–30 days) and a next-term (31–37
  days) expiry, interpolated to 30 days. It is updated every 15 seconds. Their
  replication matches CBOE's white-paper example exactly, but daily closes differ by up to
  about 6%, mostly because the last VIX print and the 3:15 pm option snapshot are not
  simultaneous.
- **What drives the number.** The weighted option sum is at least 99.4% of the value; the
  forward-correction term is at most 0.6%. The five puts and five calls nearest the
  forward explain about 50–70% of the VIX. The number of options included changes sharply
  on volatile days, and the deep out-of-the-money puts carry the largest weights.
- **CBOE's approximations make it too low.** A Taylor approximation in the correction term
  costs up to 0.3%. Dropping every strike beyond two consecutive zero bids has changed the
  VIX by more than 7.5% on some days, mostly before 2016. Both errors bias the index
  downwards.
- **Can it be moved deliberately?** Of eight possible levers, two matter in practice. One
  is changing the quotes of included options. The other is changing which strikes are
  included, by posting a bid on a zero-bid strike to extend the tail. Posting quotes costs
  nothing unless they trade.
- **Settlement is a different calculation.** VIX futures and options settle on a Special
  Opening Quotation. It uses opening auction prices rather than mid-quotes, and a single
  expiry exactly 30 days out rather than two interpolated expiries. Large gaps between the
  settlement value and the previous close are therefore expected. The authors argue these
  gaps have been misread in the literature as evidence of manipulation.
- **The structural problem.** Liquid, cash-settled VIX derivatives worth billions are
  priced off thin quotes in illiquid out-of-the-money SPX options.

## Why it's in the library

**Anyone using the VIX as data should know what it is.** It is a model-free variance swap
rate computed from a truncated, discretely sampled strip of quotes. It is not a forecast
of realized volatility, and it is biased low by construction.

**The tail weights matter in a crash.** The deep out-of-the-money puts carry the largest
weights and are the least liquid. In stress the set of strikes changes from minute to
minute, so the index is least reliable exactly when it is watched most closely.

**Settlement mechanics are part of the instrument.** Anyone holding VIX futures or options
into expiry is exposed to the opening auction, not to the index they watched the night
before. February 2018 (VIX up 115% in a day, the end of the inverse-VIX note XIV) is the
paper's motivating case.

**It is one replication study.** The sample is short (2015–2018), and the manipulation
analysis shows what is possible, not what happened.

## Links

- [[demeterfi-et-al-1999-more-than-you-ever-wanted-to-know-about-volatility-swaps]] — the
  variance-swap replication the VIX formula discretises
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — a manager's view of
  the same formula and why the index can stay low in an orderly sell-off
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — the early VIX
  futures market and a model for pricing it
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — what
  VIX futures and options did as portfolio hedges, including February 2018
- [[cole-2018-what-is-water-in-markets]] — the February 2018 short-volatility unwind from a
  manager's side
- [[carr-wu-2006-a-tale-of-two-indices]] — why the VIX moved from VXO to a variance-swap rate
- [[cboe-2021-vix-index-white-paper]] — the exchange's own description of the calculation replicated here
- [[chen-tsai-2017-determinants-of-price-discovery-in-the-vix-futures-market]] — where volatility is really priced: VIX futures lead the computed spot index about three to one
- [[griffin-shams-2018-manipulation-in-the-vix]] — how the separate settlement auction can be pushed by trades in thin out-of-the-money SPX options
- [[hirsa-et-al-2021-the-vix-index-under-scrutiny-of-machine-learning]] — the follow-up: how few options are needed to reproduce the VIX, and neural networks fitted to it
