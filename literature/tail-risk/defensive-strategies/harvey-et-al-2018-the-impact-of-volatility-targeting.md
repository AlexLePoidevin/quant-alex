# The Impact of Volatility Targeting

| | |
|---|---|
| **Authors** | Campbell R. Harvey, Edward Hoyle, Russell Korgaonkar, Sandy Rattray, Matthew Sargaison, Otto Van Hemert (Man Group; Harvey also at Duke) |
| **Year** | 2018 (version dated 25 June 2018) |
| **Type** | Paper. SSRN 3175538, 28pp; published in *Journal of Portfolio Management* 45(1), 14–33 (2018). Daily data from 1926 for US equities and bonds, 1988–2017 for 50+ futures |
| **PDF** | Local copy only (SSRN download of a Man Group working paper; no open licence) |
| **BibTeX** | `harvey2018voltarget` |
| **Status** | Reference: §2 (US equities since 1926), §4 (60+ assets), §5 (balanced and risk parity) and §6 (the leverage-effect explanation) |

## What it is

A test, across more than 60 assets, of what happens when you hold a constant level of
volatility instead of a constant notional position, scaling up in calm markets and down in
turbulent ones.

- **Sharpe ratios improve only for risk assets.** For US equities 1926–2017 the Sharpe
  ratio rises from 0.40 to 0.48–0.51 with volatility scaling, fairly insensitive to the
  volatility estimator. The same holds for credit. For bonds, currencies and commodities the
  effect on the Sharpe ratio is negligible.
- **Tails improve everywhere.** Across all assets, volatility targeting lowers the
  volatility of volatility and makes extreme months, especially the left tail, less
  severe, because big losses tend to happen when volatility is already high and the
  scaled position is small.
- **Portfolios.** For a 60-40 equity-bond portfolio (1988–2017), scaling at both the asset
  and portfolio level lifts the Sharpe ratio from 0.80 to 0.91 and improves the worst 1% of
  monthly returns from −9.7% to −7.3%. A 25-25-25-25 equity-bond-credit-commodity "risk
  parity" portfolio improves from 0.80 to 0.91, with the worst 1% going from −12.8% to
  −8.2%. Maximum drawdowns fall too. Costs are small: Sharpe ratios net of estimated costs
  are within 0.02 of gross.
- **Why risk assets.** Only equities and credit show a leverage effect (falling prices
  come with rising volatility). Volatility scaling therefore cuts exposure after losses,
  which is a form of momentum, and momentum has paid. That explains most of the
  cross-asset differences in the Sharpe ratio gain.
- **Intraday data help a little.** Using five-minute S&P 500 futures data for the
  volatility estimate slightly improves the Sharpe ratio, vol of vol and left tail.

## Why it's in the library

**It separates two claims that often get mixed up.** "Volatility targeting raises the
Sharpe ratio" is true only for assets with a leverage effect. "Volatility targeting cuts
the left tail" holds across asset classes. The second is the more robust reason to do it.

**It ties volatility targeting to trend following.** The Sharpe gain comes from an
implicit momentum position, which links this paper to the crisis-alpha and rebalancing
papers from the same group.

**Limits and the other side of the argument.** Volatility targeting buys after calm and
sells after shocks, so at the market level it can amplify selloffs. Cole (2017) makes
exactly that case. The paper studies the investor's own portfolio and does not address
that feedback.

## Links

- [[carr-wu-2017-leverage-effect-volatility-feedback-and-self-exciting-market-disruptions]] — the leverage effect and volatility feedback in index options
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — the case that volatility-targeting strategies collectively form a hidden short-volatility trade
- [[booth-fama-1992]] — fixed-weight portfolios, the baseline this paper scales
- [[baltas-kosowski-2017-demystifying-time-series-momentum-strategies]] — better volatility estimates and a correlation adjustment inside a trend portfolio
- [[barro-canestrelli-lanza-2014-volatility-vs-downside-risk]] — an optimised alternative that controls tail losses directly, not just volatility
- [[fan-et-al-2022-momentum-and-the-cross-section-of-stock-volatility]] — a cross-sectional volatility adjustment to momentum, alongside whole-portfolio scaling
- [[kaczmarek-et-al-2022-false-safe-haven-assets]] — which safe-haven assets help a volatility-targeting equity portfolio (only long Treasuries, 2010–2020)
