# Liquidity and Return Reversals

| | |
|---|---|
| **Authors** | Pierre Collin-Dufresne (EPFL), Kent Daniel (Columbia Business School) |
| **Year** | 2015 (draft dated 28 May 2015; first draft October 2013) |
| **Type** | Working paper, 42pp. Not found as a published article |
| **PDF** | Not hosted in this repository (working paper, no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22Liquidity+and+Return+Reversals%22+Collin-Dufresne) for the title and authors |
| **BibTeX** | `collindufresne2015reversals` |
| **Status** | Reference: §2 (Fama–MacBeth reversal pattern), §3.2 (model estimates, Table 2) and §5 (VIX versus cross-sectional volatility) carry the results |

## What it is

A model of how quickly the largest US stocks recover from price shocks that are not news,
and a test of whether that recovery is faster when markets are in turmoil.

- **Sample.** The 100 largest US stocks by market value, reselected each year, daily
  returns 1972–2014. Restricting to the largest stocks means almost every name trades
  every day, so the result is not a stale-price artefact.
- **The pattern.** Each stock's residual return (its return minus its shrunk market beta
  times the market return) is regressed on its own lagged residual returns, lags 1 to 30
  days. Returns within a day of an earnings announcement are set to zero, because
  news-driven moves should not reverse (and in the data they do not). Even for these
  stocks the two-day-lag coefficient has a t-statistic above 17. Lags from 2 to 12 days are
  all significant, and the coefficients decay exponentially.
- **The size of the effect.** About 90% of an idiosyncratic price shock is permanent. The
  remaining 10% is temporary and decays with a half-life of about 2.4 days. The decay rate
  is stable over time; the size of the temporary part varies a lot, with a half-life of
  about a year.
- **The strategy.** A portfolio weighted by an exponentially weighted sum of each stock's
  lagged residual returns, skipping a day before trading, has an annualised Sharpe ratio
  of 3.08 over 1972–2013. The paper reports no transaction costs. That matters for a
  strategy that trades daily.
- **The VIX does not explain it.** Nagel (2012) found reversal profits are higher when the
  VIX is high, and read this as liquidity providers withdrawing in turmoil. Here, once the
  strategy's own (cross-sectional) volatility is controlled for, the VIX has no power to
  forecast the strategy's Sharpe ratio. The VIX and cross-sectional volatility are about
  60% correlated but diverge, for example after 2002–03 and after 2008.

## Why it's in the library

- **Reversal after selloffs, measured.** This is the stock-level version of a bounce: part
  of a non-news price drop is a temporary liquidity effect that reverts within days. The
  paper puts numbers on how big that part is (about 10%) and how fast it goes (half-life
  around two and a half days).
- **Slow-moving capital.** The authors read the results as limited arbitrage capital that
  does not flow freely between markets. Market-wide fear (the VIX) is not the right gauge
  of how profitable liquidity provision is; the strategy's own volatility is.
- **Read the Sharpe ratio as gross.** A 3.08 Sharpe ratio before costs on a daily-turnover
  strategy says the effect is statistically strong, not that it is tradable at that level.

## Links

- [[boyarchenko-larsen-whelan-2023-the-overnight-drift]] — reversal of end-of-day selling
  pressure at the index level, overnight
- [[johannsen-2016-dead-cat-bounce]] — a behavioural model of a bounce after a crash
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — bear rallies at the
  market level
- [[chernenko-sunderam-2020-measuring-the-perceived-liquidity-of-the-corporate-bond-market]] — a liquidity measure built from holdings rather than trades, which picks up perceived risk that transaction measures miss
- [[khandani-lo-2011-what-happened-to-the-quants-in-august-2007]] — the week in August 2007 when the short-term reversal (liquidity-provision) strategy broke
- [[medhat-schmeling-2022-short-term-momentum]] — one-month reversal splits by turnover: thinly traded stocks reverse, heavily traded ones continue
