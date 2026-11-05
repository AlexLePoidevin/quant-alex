# When Diversification Fails

| | |
|---|---|
| **Authors** | Sébastien Page, Robert A. Panariello (T. Rowe Price) |
| **Year** | 2018 |
| **Type** | Journal article, *Financial Analysts Journal* 74(3), 2018, 19–32. Practitioner research |
| **PDF** | `page-panariello-2018-when-diversification-fails.pdf` (open access: the article is distributed under CC BY-NC-ND 4.0, which permits unaltered non-commercial redistribution) |
| **BibTeX** | `page2018diversification` |
| **Status** | Reference: "Measuring Tail Correlations" and Appendix A (the method), Figures 1–5 (risk assets, hedge funds, private assets, risk factors) and Figures 6–7 (stocks vs Treasuries) carry the results |

## What it is

An update of Chua, Kritzman and Page's "The Myth of Diversification" (2009) with post-2008
data, a wider set of assets, and a simple fix for noisy tail correlations.

- **Method.** Monthly data from 1970 (or first availability) to June 2017. Correlations are
  conditioned on *one* asset, US stocks, being in a given percentile of its returns, rather
  than on both assets moving together. Each conditional correlation is compared with what a
  bivariate normal with the same moments would give, because conditioning alone shrinks
  correlations even under normality. To stabilise estimates deep in the tails, the
  subsample is padded with the rest of the data under exponentially decaying weights whose
  half-life is set at the percentile in question (Appendix A).
- **International equities.** The correlation of US with non-US stocks (MSCI EAFE, local
  currency) is +87% in the worst 1% of US months and −17% in the best 1%. Normality would
  give the same value on both sides.
- **Everything risky converges in a selloff.** Credit (excess returns over Treasuries),
  high yield, emerging markets, real estate, MBS (which looked like a diversifier before
  2008) and every hedge fund style, market-neutral included, have much higher left-tail
  than right-tail correlations with US stocks. Private equity and direct real estate look
  diversifying on smoothed quarterly returns but much less so on rolling annual returns.
  The explanations offered: credit is a short put on firm assets (Merton), many hedge fund
  strategies are short volatility or liquidity, and "risk-off" regimes move everything
  together.
- **Risk factors.** Cross-asset and currency momentum have lower left-tail than right-tail
  correlations with stocks, because momentum sells risk assets as they fall. Size and
  currency carry fail in the left tail. Most of the apparent benefit of factors over asset
  classes is the freedom to go short.
- **Stocks and Treasuries.** Conditioned on stock returns, long Treasuries are the one
  desirable profile: they decouple from stocks in selloffs and correlate in rallies.
  Conditioned on *bond* selloffs, though, stocks can fall too, so the hedge is one-way and
  can break when inflation or rate shocks drive markets.
- **Recommendations.** Drop full-sample correlations from risk models (or stress them), use
  downside-aware optimisation and scenario analysis before trading, and look beyond
  diversification: tail hedges, defensive momentum and especially managed volatility,
  which cuts risk when volatility spikes and so offsets correlation spikes.

## Why it's in the library

**It measures the problem every multi-asset portfolio has.** Diversification across risk
assets largely disappears in the worst 1% of equity months and reappears when it is not
needed. The figures make the size of that asymmetry concrete across asset classes,
styles, alternatives and factors.

**Single conditioning shows which asset drives the selloff.** Conditioning on stocks
versus on bonds gives different stock–bond correlation profiles. That one-way nature of the
Treasury hedge is the same warning as the inflation-driven stock–bond papers.

**Caveats.** The results are almost entirely charts; few numbers are given beyond the
international-equity example, and the full profiles are in an online appendix. Tail
estimates at the 1st percentile of monthly data rest on a handful of months, which the
weighting smooths but cannot add to. The authors run multi-asset portfolios, and the
managed-volatility recommendation rests mainly on their colleagues' earlier research
(Dreyer et al. 2016) rather than on tests in this paper.

## Links

- [[kinlaw-et-al-2021-the-myth-of-diversification-reconsidered]] — the same research line
  revisited: downside versus upside correlations and what to do about them
- [[ang-chen-2002]] — the original evidence that equity correlations rise in down markets
- [[hartmann-straetmans-de-vries-2004-asset-market-linkages-in-crisis-periods]] —
  extreme-value estimates of joint crashes, an alternative to conditional correlations
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — when inflation
  news dominates, the stock–bond hedge fails in both directions
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — evidence on the managed
  volatility the paper recommends
- [[kinlaw-turkington-2014-correlation-surprise]] — measuring unusual co-movement as it
  happens rather than after the fact
