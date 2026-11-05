# Multiasset Financial Bubbles in an Agent-Based Model with Noise Traders' Herding Described by an n-Vector Ising Model

| | |
|---|---|
| **Authors** | Davide Cividino (Politecnico di Torino), Rebecca Westphal (ETH Zürich), Didier Sornette (ETH Zürich, SUSTech, Swiss Finance Institute) |
| **Year** | 2023 (Physical Review Research 5, 013009, published 10 January 2023); first circulated as Swiss Finance Institute Research Paper 21-76, November 2021 |
| **Type** | Journal article (agent-based simulation model), 19pp |
| **PDF** | `cividino-westphal-sornette-2023-multiasset-financial-bubbles-in-an-agent-based-model.pdf` (the published version, open access under CC BY 4.0) |
| **BibTeX** | `cividino2023bubbles` |
| **Status** | Reference: §II (the model), §IV (the three herding regimes) and §IV.C.2 (the cascade mechanism) carry the results |

## What it is

A simulated market with one risk-free asset and several risky stocks, built to show how
bubbles can start in one asset and then spread to the others. It extends the
single-stock agent-based model of Kaizoji, Leiss, Saichev and Sornette to many stocks.

- **Two kinds of trader.** *Fundamentalists* hold a mean-variance portfolio (a quadratic
  approximation to constant relative risk aversion) based on dividend yields, so they buy
  more of a stock when it is cheap relative to its dividend and less as it gets
  expensive. *Noise traders* follow price momentum (an exponential moving average of
  past returns) and imitate each other.
- **Imitation as magnetism.** Each noise trader's portfolio is a unit vector on a sphere
  (positive components are holdings of risky stocks, negative components the risk-free
  asset). Their interactions are an O(n) or "n-vector" model from physics, the
  multi-dimensional version of the Ising model. Momentum acts like an external magnetic
  field pulling the vectors towards rising assets. A single parameter κ, the propensity
  to herd, plays the role of inverse temperature.
- **Realistic trading rules.** The paper derives transition probabilities so that each
  trader's choice is a logit (random-utility) decision, and adds a probability of simply
  holding the portfolio for the day (an average holding time of ten days absent herding),
  which captures inertia.
- **Prices from market clearing.** Each simulated day, prices solve the n
  market-clearing equations numerically. The simulations use four risky assets, 1,000
  noise traders and 5,000 trading days, with dividends that are uncorrelated across
  stocks.
- **Stylized facts reproduced.** Returns have power-law tails with exponents of about
  3.0 to 3.3, inside the empirical range of 2 to 4, and absolute returns stay
  autocorrelated beyond 250 days (volatility clustering), while signed returns show
  almost no autocorrelation.
- **Three regimes, set by herding.** The critical value of κ equals the number of risky
  assets (κc = n, here 4).
  - **Below the critical value**, opinions stay idiosyncratic and prices grow steadily
    with dividends: no bubbles.
  - **Near it**, with κ wandering around κc as a mean-reverting process, bubbles appear
    whenever κ crosses κc, at different times in different stocks, and also as
    "negative bubbles".
  - **Well above it**, noise traders are always polarised and momentum steers them.
    Bubbles then appear in cascades: one stock bubbles first and the others follow.
- **The cascade mechanism.** The first bubble makes everyone richer. Fundamentalists,
  whose portfolios are now overweight the bubbling stock, rebalance by selling it and
  buying the others, which pushes those prices up. The rising prices create momentum
  that noise traders then chase, starting new bubbles. So the cautious, contrarian
  rebalancing of fundamentalists is what carries the bubble across the market. Over long
  runs fundamentalists end up richer than noise traders, because noise traders give back
  their gains in the crashes.

## Why it's in the library

**It gives a concrete mechanism for bubbles spreading across assets.** The dividends of
the four stocks are uncorrelated by construction and fundamentalists expect no
correlation, yet bubbles still synchronise. The link runs through wealth and portfolio
rebalancing, not through shared fundamentals. That is a useful counterpoint to treating
asset correlations as stable parameters: in this model, co-movement in a mania is
created by the traders.

**Rebalancing is not automatically stabilising.** The usual intuition is that
fundamentalists who sell what has risen dampen bubbles. Here their rebalancing into the
*other* assets is the channel that spreads the bubble. Whether this matters in real
markets depends on how large the momentum-chasing population is, which the model sets
rather than measures.

**It is a simulation, not evidence.** The parameters are chosen so that one step looks
like a trading day with 1–2% volatility, and the model is validated only against two
stylized facts (fat tails and volatility clustering). The supercritical regime, where
the cascades are clearest, is one the authors themselves say is unlike what is observed
in real markets. Read it as a mechanism to look for, not as a description of how often
it happens.

## Links

- [[schatz-sornette-2020-inefficient-bubbles-and-efficient-drawdowns]] — the same research group's no-arbitrage model of bubbles and crashes
- [[chiarella-he-zwinkels-2014-heterogeneous-expectations-in-asset-pricing]] — an estimated fundamentalist-versus-trend-follower model of the S&P 500, the empirical cousin of this simulation
- [[soros-2013]] — reflexivity: traders' beliefs changing the prices they are trying to forecast
- [[gurkaynak-2008-econometric-tests-of-asset-price-bubbles]] — why bubbles are hard to identify from price data alone
- [[sarkissian-2019-statistical-mechanics-of-price-stabilization-and-destabilization]] — another physics-style model in which collective behaviour tips a market from calm to crash
