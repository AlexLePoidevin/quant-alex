# Volatility Regimes for the VIX Index

| | |
|---|---|
| **Authors** | Jacinto Marabel (BBVA; University of Alcalá) |
| **Year** | 2011 (*Revista de Economía Aplicada*) |
| **Type** | Journal article, 36pp in this copy. Monthly VIX, January 1990 – September 2010 |
| **PDF** | Local copy only (author's upload to ResearchGate; no open licence) |
| **BibTeX** | `marabel2011vixregimes` |
| **Status** | Reference: §3 (the model specifications) and §4 (estimates, out-of-sample errors, regime probabilities and durations). The coefficient tables did not survive text extraction, so only figures quoted in the text are used here |

## What it is

A two-regime Markov-switching model for the level of the VIX: the index is either in a
low-volatility or a high-volatility state, and moves between them by an unobserved Markov
chain.

- **Why regimes.** The VIX mean-reverts, but it also sits at a high level for years and
  then at a low level for years, and it is far more volatile when high. The squared VIX
  shows an AR(1) pattern. The paper also derives the VIX from the variance-swap
  replication formula, including dividends.
- **The models.** The VIX follows an AR(1) whose mean depends on the regime, with
  Student-t errors so a single outlier in a calm period does not flip the regime. Three
  versions differ in the variance: regime-dependent (MSMV), ARCH(1) (MSM-ARCHV) and
  GARCH(1,1) (MSM-GARCHV). A plain AR(1) with ARCH errors is the benchmark. All are fitted
  by maximum likelihood with Hamilton's filter and Kim's smoother.
- **The results.** Fitted on January 1990 – October 2009 and forecast one month ahead
  over November 2009 – September 2010 (re-estimated each month), the three switching
  models fit about equally in sample; the MSM-ARCHV model has the lowest out-of-sample
  errors. Allowing for regimes lowers the estimated persistence of the AR term, as
  structural breaks in the mean would predict. The Student-t, regime-switching models
  describe the distribution better than the Gaussian benchmark.
- **The regimes it finds.** Low volatility until July 1996; high volatility through the
  Asian and Russian crises and the dot-com bust until October 2003; low until July–August
  2007; high after that. The ARCH and GARCH versions almost never give a regime
  probability between 0.3 and 0.7. For MSM-ARCHV the average duration is 66 months for the
  low regime and 91 months for the high one.

## Why it's in the library

**It gives the "volatility has regimes" intuition a simple, standard form.** Two states,
regime-dependent means, fat-tailed errors and a filter that says how likely each state is
today. That is the template behind regime filters for volatility-selling and hedging
decisions.

**Its limits are clear.** Monthly data over 20 years contains only a handful of regime
switches, so the durations rest on very few events. The model is for the level of VIX
with normal or t errors, so it can in principle produce negative values (the author notes
a log specification would avoid this). The out-of-sample test is eleven months.

## Links

- [[avellaneda-papanicolaou-2018-statistics-of-vix-futures-and-applications-to-trading]] —
  a two-factor mean-reverting model of VIX and its futures, whose fast factor plays the role
  of the high-volatility regime
- [[merton-1976]] — jumps, the other standard way to model sudden moves into high volatility
- [[lv-wang-yuan-2026-garch-evt-rvine-scad-portfolio]] — GARCH volatility filtering used
  inside a tail-risk portfolio model
- [[ang-timmermann-2012-regime-changes-and-financial-markets]] — the standard survey of regime-switching models across equities, rates and currencies
- [[bilokon-et-al-2021-market-regime-classification-with-signatures]] — regimes found by clustering path signatures rather than fitting a fixed number of states
- [[botte-bao-2021-a-machine-learning-approach-to-regime-modeling]] — market regimes from a Gaussian mixture fitted to multi-asset factor returns
- [[caporale-et-al-2018-is-market-fear-persistent]] — long-memory tests showing the VIX is anti-persistent in calm periods and near a unit root in 2007–09
- [[cloutier-djatej-kiefer-2017-tactical-asset-allocation-that-exploits-variations-in-vix]] — using VIX regimes (above 30, below 20) to tilt a diversified portfolio
- [[dapena-serur-siri-2018-measuring-and-trading-volatility-regime-switching]] — regimes in the VIX-minus-realised spread used to time short volatility
- [[maheu-mccurdy-song-2012-components-of-bull-and-bear-markets]] — regime switching in stock returns, where volatility separates a bear rally from a new bull market
