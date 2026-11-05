# Tail risk

Crashes: what protecting a portfolio against them costs and pays, why markets can be calm
for years and then fall faster than the calm-period data suggest, and what actually
happens inside a crash.

| Folder | What's in it |
|---|---|
| `tail-hedging` | Long VIX futures and options as a diversifier, and why rule-based tail hedges bleed |
| `volatility-and-market-structure` | Volatility-sized strategies as one hidden short-volatility trade, option dealers' gamma hedging as an amplifier, 0DTE options, and what the VIX does and does not measure |
| `market-microstructure-and-flash-crashes` | The 6 May 2010 flash crash and single-stock mini flash crashes: order-flow toxicity (VPIN), self-exciting trades, tests for crash-and-rebound shapes, microstructure noise, and dealer quoting |

Several sources here are written by managers or vendors who sell volatility or tail-hedging
products. Their notes say where the argument runs ahead of the evidence. The measurement side
of tail risk (fat tails, jumps, coherent risk measures, CVaR optimisation) is in
`../portfolio-construction-and-risk/tail-risk-and-risk-measures/`, and tail dependence
between assets is in `../correlation-and-dependence/copulas-and-tail-dependence/`.

## Tail hedging

- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]: A volatility manager's case that calendar-rolled tail hedges bleed (equity and volatility risk premia, compounding of the bleed, paying wide spreads, fitting exits to a handful of crashes) and that hedges should be traded on price instead; the diagnosis is checkable, the cure is asserted without a track record.
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]]: Small long-VIX futures and call positions added to a 60/40 and an endowment portfolio, 2006–2017: big gains in 2008, a steady drag from contango otherwise, VIX calls compared with S&P 500 puts, and the VXTH dynamic tail-hedge index.

## Volatility and market structure

- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]]: What the VIX actually measures, why it stayed subdued during 2022's orderly 20% decline, and Ambrus's untested argument that short-dated options and dealer concentration are fattening its tails.
- [[ambrus-capital-2022-volatility-and-the-changing-market-structure]]: Ambrus's list of structural reasons US equities have become calm-then-crash fragile (dealer gamma hedging, few option market makers, Dodd–Frank risk limits, structured products, passive and leveraged ETFs, common VaR triggers), and its case for a small managed volatility allocation.
- [[ambrus-capital-2023-dispelling-false-narratives-about-0dte-options]]: Who trades zero-day SPX options and in which direction: mostly institutions selling volatility at the open, which damps markets day to day, with the risk that one-sided put buying amplifies a shock (classification method proprietary).
- [[barbon-buraschi-2021-gamma-fragility]]: Barbon and Buraschi measure option dealers' gamma imbalance stock by stock (2010–2020): when dealers are short gamma, volatility and intraday momentum rise, more so in illiquid stocks, and flash crashes are somewhat more likely and markedly deeper.
- [[cole-2017-volatility-and-the-alchemy-of-risk]]: Christopher Cole's essay arguing that roughly $1.5tn of strategies that size risk by volatility (risk parity, volatility control, risk premia, short-VIX products, and buybacks) form one giant short-volatility trade that can turn a shock into a crash, with Black Monday 1987 as the template.
- [[cole-2018-what-is-water-in-markets]]: Cole's follow-up to the 2017 essay: February 2018 as a liquidity crisis rather than a volatility event (E-mini depth down 95%, tail puts driving the VIX), a toy simulation of passive investing crowding out active price discovery, and a macro forecast that half came true.
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]]: SPX option market makers' aggregate gamma inventory built from Cboe open-close data, 2004–2020: spreads widen when dealers are short gamma, and dealers flatten their gamma when markets are illiquid, volatile and intermediaries are constrained.
- [[squeezemetrics-2020-the-implied-order-book]]: SqueezeMetrics on dealer gamma (GEX) and vanna (VEX) exposure as a hidden S&P 500 order book, and why customer-sold puts that go in the money can turn dealer hedging into a crash feedback loop; vendor argument from scatterplots.

## Market microstructure and flash crashes

- [[baldacci-et-al-2020-options-market-making-in-high-dimension]]: A stochastic-control method for a dealer quoting many options on many underlyings: a value function quadratic in inventories cuts the problem to a few PDEs, with greeks updated continuously; tested only in simulation.
- [[demos-et-al-2015-some-statistical-properties-of-the-mini-flash-crashes]]: Return statistics around 14 single-stock mini flash crashes (2011–2012) and the 2010 Dow: non-normal, power-law tails, chaos and log-periodic fits tried and then doubted, threshold GARCH fits but misses the tails.
- [[easley-et-al-2011-microstructure-of-the-flash-crash]]: Easley, López de Prado and O'Hara on 6 May 2010 as a liquidity crash: order-flow toxicity (VPIN) in E-mini futures rose for hours before the fall as high-frequency market makers withdrew; the early-warning claim is the inventors' own and has been disputed.
- [[filippou-et-al-2022-no-max-pain-no-max-gain]]: Tests the options-folklore 'max pain' effect on US stocks, 1996–2021: in the week before expiry, prices drift towards the strike where listed options pay out least (about 0.4% a week on a decile spread), with no effect in matched stocks that have no options.
- [[flora-reno-2020-v-shapes]]: A test (the V-statistic) for prices that overshoot and reverse, separating market failure from fast but efficient repricing; applied to the 2010 flash crash, SPY through Covid, and a €434m loss on Italian bond auctions in May 2018.
- [[kim-et-al-2021-investigation-of-flash-crash-via-topological-data-analysis]]: Persistence landscapes of one-minute joint returns on S&P, Dow and Nasdaq futures, turned into an anomaly score that spikes on 6 May 2010; one event, no false-alarm rate.
- [[poitras-2012-what-happened-may-6-2010-anatomy-of-the-flash-crash]]: A market historian's reading of the SEC–CFTC reports on the 6 May 2010 flash crash next to the 1987 crash, arguing that futures selling passed to stocks by index arbitrage, outside the collateral limits on short selling, drove both.
- [[romero-2016-microstructure-noise-two-scales-realized-volatility]]: A thesis walk-through of the two-scales realized volatility estimator (Zhang, Mykland and Aït-Sahalia): why summing squared tick returns measures bid-ask noise rather than volatility, how TSRV removes it, and a small inconclusive test of whether wider-spread Dow stocks carry more noise.
- [[sarkissian-2019-statistical-mechanics-of-price-stabilization-and-destabilization]]: A Landau-style free-energy model of order imbalance in which small repricings are absorbed as a random walk but large ones trigger a phase transition (correlation and volatility spike, order flow goes one-sided), with a tanh price-impact formula; a phenomenological sketch rather than a tested model.
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]]: A multivariate Hawkes model of the 30 Dow stocks through the 6 May 2010 Flash Crash: fewer but much stronger cross-stock links, cross-excitation catching up with self-excitation, and clusters that cut across sectors.
- [[tee-ting-2019-cross-section-of-mini-flash-crashes]]: A Kalman-filter detector for mini flash crashes in S&P 500 trade data, 2010–2013: 7,492 crashes at z = 6, clustered on news and event days, with smaller, more volatile, thinner and lower-priced stocks moving furthest.
- [[wikipedia-2013-vpin-flow-toxicity]]: A Wikipedia overview of the probability-of-informed-trading models, from the 1996 PIN model to volume-clock VPIN with bulk classification, and the uses claimed for it; good for definitions, one-sided on evidence.
- [[zakamulin-giner-2022-optimal-trend-following-in-a-markov-switching-model]]: Proves that in a two-state bull/bear Markov switching model the exponential moving average is the optimal trend-following rule, gives its window in closed form, and estimates a 9-month EMA for the S&P 500 from 1926–2020 data.
