# Determinants of Price Discovery in the VIX Futures Market

| | |
|---|---|
| **Authors** | Yu-Lun Chen (Chung Yuan Christian University), Wei-Che Tsai (National Sun Yat-sen University) |
| **Year** | 2017 (*Journal of Empirical Finance* 43, 59–73) |
| **Type** | Journal article, 15pp. Five-minute VIX and VIX futures data, 3 May 2004 – 30 August 2011 |
| **PDF** | Local copy only (Elsevier journal version) |
| **BibTeX** | `chen2017vixdiscovery` |
| **Status** | Reference: Tables 5–6 (information shares) and the futures-basis and announcement regressions carry the results |

## What it is

An intraday study of whether new information about expected volatility shows up first in
the spot VIX or in VIX futures, and what makes the futures' share larger or smaller.

- **Method.** Five-minute prices of the spot VIX and the nearest VIX future. The two are
  cointegrated, so the authors use the two standard price-discovery measures for
  cointegrated prices: Hasbrouck's information share and Gonzalo–Granger's common-factor
  weight, computed for the full sample and day by day.
- **Futures lead.** In the full sample the futures' information share is 0.73 and its
  common-factor weight 0.78, against 0.27 and 0.22 for the spot index. Averaged day by day,
  the futures contribute 71.9% and the index 28.1%.
- **The futures basis matters.** When the basis (spot VIX minus futures) is positive, which
  means an inverted, crisis-shaped term structure, the futures' share of price discovery is
  higher. The authors read this as the spot VIX spiking on short-term fear while the
  futures price in mean reversion.
- **Macro news.** On US macro announcement days, especially CPI, the futures' share rises
  further.
- **Robustness.**
  - Results hold with corridor implied volatility in place of the VIX.
  - The futures' share falls for longer-dated contracts.
  - The futures also lead VIX ETPs and a non-US volatility index (VXEFA).

## Why it's in the library

It is the careful answer to "where is the VIX really priced?": in the futures, by about
three to one. That matters for anyone using the spot VIX as a signal, since the index is
a calculated number that lags the traded futures, especially in stressed, inverted markets.

One structural point helps read it. The spot VIX cannot be traded or arbitraged directly,
and its one-minute returns have an autocorrelation of about 0.48 (the paper's Table 1),
a sign of a smoothed, partly stale series. A share of the futures' "leadership" is
therefore mechanical, not informational. The paper acknowledges that the VIX is hard to
replicate but does not separate the two effects.

## Links

- [[karagiannis-2014-lead-lag-relationship-between-the-vix-and-vix-futures]] — the same
  question on daily data with Granger causality, reaching the same answer more crudely
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — how the spot
  index is computed from option quotes, and its biases
- [[brenner-et-al-2007-the-market-for-volatility-trading-vix-futures]] — the early VIX
  futures market and its term structure
- [[gehricke-zhang-2018-modeling-vxx]] — the ETN built from the futures whose price
  discovery is measured here
- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  mean reversion along the futures curve, the mechanism behind the basis effect
