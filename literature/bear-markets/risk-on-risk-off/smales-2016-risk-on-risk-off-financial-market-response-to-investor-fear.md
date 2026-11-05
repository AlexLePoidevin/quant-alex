# Risk-On / Risk-Off: Financial Market Response to Investor Fear

| | |
|---|---|
| **Authors** | Lee A. Smales (Curtin University) |
| **Year** | 2016 |
| **Type** | Journal article, *Finance Research Letters* 17, 125–134 (doi 10.1016/j.frl.2016.03.010). The copy is the SSRN version (2717330), 17pp. Daily data, January 2001 to June 2015 |
| **PDF** | Local copy only (SSRN download of an Elsevier article, no open licence) |
| **BibTeX** | `smales2016riskon` |
| **Status** | Reference: Table 2 (full sample), Table 3 (2008–09) and Table 5 (returns after high and low VIX) carry the results |

## What it is

A short empirical test of what market commentators mean by "risk-on" and "risk-off". Smales
takes the VIX (and its Australian equivalent, the A-VIX) as a gauge of investor fear and asks
how stocks, 10-year government bond yields and trade-weighted currencies in the US, Australia
and New Zealand move with it.

- **Same-day moves.** Daily percentage changes in each market are regressed on the daily
  percentage change in the VIX (lagged one day for the Australian and New Zealand markets,
  which close before New York opens). When the VIX rises, stocks fall, bond yields fall and
  the high-yielding Australian and New Zealand dollars weaken, while the US dollar
  strengthens: a flight to quality across asset classes. The fit is strongest for the S&P 500
  (coefficient −0.145, adjusted R² 0.56) and much weaker elsewhere (R² of 0.05–0.19 for the
  other stock, bond and currency series; 0.005 for the US dollar).
- **Stronger in the crisis.** Re-run on January 2008 to June 2009 alone, every sign is
  unchanged but the sensitivities are larger: the S&P 500 coefficient roughly doubles to
  −0.282 (R² 0.70), and stock-market coefficients are on average 85% larger than over the
  full sample. Currency sensitivities rise most and bond sensitivities least.
- **A VAR.** A ten-variable vector autoregression with one lag gives the same picture and
  shows US stock and bond moves feeding into the next day's Australian and New Zealand
  markets.
- **What happens after extreme fear.** Returns are tabulated over the 5, 20, 60 and 120
  trading days after the VIX closes in its top quintile (above 25.66) or bottom quintile
  (below 13.42). After high fear, S&P 500 returns are higher on average (for example +5.7%
  versus +4.2% over 120 days), the US dollar weakens and the Australian and New Zealand
  dollars strengthen. Bond yields go the "wrong" way: they keep falling after high fear (US
  10-year yields down about 18% in relative terms over 120 days) and rise after low fear,
  which Smales attributes to central banks cutting rates in the high-VIX years of 2008–09 and
  2012.

From Table 5 he suggests a strategy of buying risky assets when the VIX is high and selling
them when it is low. That is a suggestion, not a test: no strategy is backtested, the stock
return differences between high- and low-fear periods are not shown to be significant, the
windows overlap heavily, and there are no trading costs.

## Why it's in the library

It puts numbers on the risk-on/risk-off vocabulary. A rising VIX lines up, on the same day,
with falling stocks, falling bond yields, a stronger US dollar and weaker commodity
currencies, and these links tighten in a crisis, which is exactly when diversification is
wanted most. The same-day regressions are descriptive and say nothing about which way
causation runs; VIX changes and S&P 500 returns are two readings of the same market.

The forward-return table is the part to treat sceptically. Fifteen years, one crisis, two
quintile cut-offs chosen in-sample and overlapping holding periods leave little independent
evidence, and the bond result shows that what follows a fear spike depends on the policy
response rather than on fear alone.

## Links

- [[beber-et-al-2013-switching-risk-off-fx-correlations-and-risk-premia]] — dates risk-off
  episodes from regime switches in FX correlations rather than from the VIX
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — what the VIX does
  and does not measure, and why it stayed low in 2022's orderly fall
- [[carr-wu-2006-a-tale-of-two-indices]] — how the VIX is built and what its level means
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bull and bear states
  dated from returns rather than from implied volatility
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — owning
  the fear gauge directly as a hedge
- [[huang-et-al-2018-sentiment-across-asset-markets]] — sentiment measured from news text across five US markets, and how it spills between them
