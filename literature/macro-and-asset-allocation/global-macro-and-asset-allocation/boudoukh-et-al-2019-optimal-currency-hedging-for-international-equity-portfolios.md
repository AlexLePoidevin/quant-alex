# Optimal Currency Hedging for International Equity Portfolios

| | |
|---|---|
| **Authors** | Jacob Boudoukh, Matthew Richardson, Ashwin Thapar, Franklin Wang (AQR Capital Management and consultants) |
| **Year** | 2019 |
| **Type** | Journal article, *Financial Analysts Journal* 75(4), 65–83, doi 10.1080/0015198X.2019.1628556 |
| **PDF** | `boudoukh-et-al-2019-optimal-currency-hedging-for-international-equity-portfolios.pdf` (open access under CC BY-NC-ND 4.0, which allows non-commercial redistribution of the unaltered article) |
| **BibTeX** | `boudoukh2019currency` |
| **Status** | Reference: the theory section (the three-part decomposition), Table 2 (hedging volatility) and Table 3 (currency styles) carry the results |

## What it is

A mean–variance treatment of the currency exposure in an international equity portfolio,
split so each part can be estimated in the way that works best for it. G-10 currencies,
weekly data, 1981–2017, returns gross of fees and costs.

- **The split.** The best currency position for a hedged equity portfolio is the sum of two
  pieces: a *hedge* portfolio, −Σ⁻¹·cov(currencies, equity), which minimises the equity
  portfolio's variance, and an *alpha* portfolio, Σ⁻¹·α, chosen for its standalone Sharpe
  ratio, mixed in at a weight set by the minimum-variance portfolio's own mean and variance.
  The minimum-variance portfolio is uncorrelated with any pure currency portfolio, so the
  two pieces can be chosen separately.
- **Hedging wants the full optimiser.** Full hedging cuts average international equity
  volatility from 16.5% to 14.9%. A single time-varying hedge ratio on the whole basket
  gets 14.3%. Estimating the whole covariance matrix (exponentially weighted, 130-day
  centre of mass, 25% correlation shrinkage) gets 12.7%, a 23% cut from unhedged. The
  optimiser shorts currencies that rise with equities (Australian and Canadian dollars) and
  holds ones that fall with them (yen, Swiss franc, US dollar).
- **Alpha wants simple rules.** Rank-weighted carry, momentum, fundamental momentum and
  value combined give Sharpe 0.88; feeding the same signals to the optimiser gives 0.84
  with worse skew (−1.8 vs −0.4), deeper drawdown, and 53% more leverage and 26% more
  turnover.
- **The pure hedge has a cost.** Minimum-variance hedging lowers returns, because it is
  effectively short carry: high-carry currencies are the ones that rise with equities.
  Adding the alpha portfolio undoes that: volatility stays at about 14.6% (against 16.5%
  unhedged and 14.9% fully hedged) and the Sharpe ratio goes from 0.38 to 0.68.
- **One answer for everyone.** Because every country's "international" portfolio is nearly
  the same mix, the optimised hedged volatility is 12.6–13.1% for all ten home countries.
  The different hedge ratios investors use mostly reflect different starting exposures.

## Why it's in the library

It is a clean example of estimation error deciding method. The same paper finds the full
optimiser wins where the inputs are covariances (which are estimated well) and loses where
the inputs are expected returns (which are not). That is the Michaud and Chopra–Ziemba
point, shown on one problem.

It also states plainly that the "free lunch" of hedging is partly a short carry position,
which matters for anyone reading the volatility reduction as costless. The results are a
backtest by managers who sell currency overlays, gross of costs, over one long sample; the
alpha-style returns are the familiar currency factors rather than anything new.

## Links

- [[michaud-1989]] — why optimised portfolios amplify errors in expected returns, the reason the alpha piece uses simple ranks
- [[chopra-ziemba-1993]] — errors in means cost far more than errors in covariances, which is the pattern found here
- [[markowitz-1952]] — the mean–variance problem being decomposed
- [[ledoit-wolf-2004]] — covariance shrinkage, used here in a simple form on the currency correlations
- [[diamonte-liew-stevens-1996-political-risk-in-emerging-and-developed-markets]] — another AQR-lineage study of what drives international equity returns
- [[asness-israelov-liew-2011-international-diversification-works-eventually]] — why an unhedged global equity portfolio still pays off over long horizons
