# Identifying Bull and Bear Market Regimes with a Robust Rule-Based Method

| | |
|---|---|
| **Authors** | Piotr Zegadło (Kozminski University) |
| **Year** | 2022 (online December 2021; the source file was labelled 2019) |
| **Type** | Journal article, *Research in International Business and Finance* 60, 101603. doi:10.1016/j.ribaf.2021.101603 |
| **PDF** | Local copy only (Elsevier journal version, all rights reserved) |
| **BibTeX** | `zegadlo2022bullbear` |
| **Status** | Reference: §2 (the algorithm), Tables 4–5 (agreement with older rules) and §4 (out-of-sample trading test) carry the results |

## What it is

A one-parameter rule for dating bull and bear markets, compared with the two standard
rule-based methods and a Markov-switching model.

- **The rule (called PZ).** Take daily closes. Mark each local maximum (higher than the
  day before and after) as a peak and each local minimum as a trough. Then repeat the same
  filter on the peaks alone and on the troughs alone, keeping only peaks higher than their
  neighbouring peaks and troughs lower than their neighbouring troughs. If two peaks end up
  next to each other with no trough between them, keep the higher one, and likewise for
  troughs. Four passes suit daily data and leave primary peaks and troughs; a bull market
  runs from a primary trough to the next primary peak. Implicitly, a bull market lasts as
  long as prices keep making new highs. There is no minimum duration or size.
- **The competitors.** Pagan–Sossounov (PS), a Bry–Boschan-style rule with minimum phase
  and cycle lengths (80 and 320 days). Lunde–Timmermann (LT), which switches regime after a
  +20% or −15% move. Both were designed for US stocks.
- **Data.** Twelve daily series from Datastream to end-2020: the Dow, DAX and NIFTY;
  GBP/USD, CHF/JPY and EUR/PLN; and copper, corn, gold, palladium, sugar and oil.
- **Agreement.** PZ and PS give the same classification on 91% of days on average, PZ and
  LT on 86%, and PS and LT on 85%. On sugar and CHF/JPY agreement falls to 70–82%. PZ
  regimes are usually shorter (median 130–340 days). Across almost all series bull phases
  last longer and rise further than bear phases fall, while bear phases are more volatile.
- **Out-of-sample test.** Each rule becomes a long-or-flat trading signal, with
  identification delays respected, 0.1% round-trip costs and no interest on cash. Sharpe
  ratios are compared with a bootstrap reality check at the 10% level. PZ significantly
  beats at least one rival on 8 of the 12 series and is never significantly beaten. On the
  Dow it is middle of the pack (Sharpe ratio 0.41 against 0.48 for PS and 0.45 for buy and
  hold). The Markov-switching rule trades hundreds of times and is hurt by costs.

## Why it's in the library

- **A parameter-light bear-market definition.** The usual "−20% from the peak" rule and its
  academic versions (PS, LT) hard-code amplitudes and durations that suit US equities. This
  rule needs only the data frequency, so the same definition works across asset classes.
  That matters if you want to compare bear markets in stocks, currencies and commodities.
- **Honest about trading value.** The author says plainly that none of the rules
  consistently and significantly beats buy and hold. The trading test is used as a measure
  of fit, not as a strategy.
- **The delay.** Identifying a peak needs the next peak or trough, so the regime is always
  confirmed late. The paper's out-of-sample test accounts for this, but the paper does not
  report the typical delay.

## Links

- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — the Markov-switching
  alternative, with bull corrections and bear rallies as extra states; Zegadło's
  regime-within-regime idea is the rule-based counterpart
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]] — trend rules
  derived from a two-state bull/bear model
- [[marabel-2011-volatility-regimes-for-the-vix-index]] — regime switching applied to
  volatility
- [[gonzalez-et-al-2006-defining-and-dating-bull-and-bear-markets]] — an earlier rule-based dating of two centuries of US bull and bear markets
