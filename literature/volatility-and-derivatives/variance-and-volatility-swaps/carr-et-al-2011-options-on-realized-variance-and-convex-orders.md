# Options on Realized Variance and Convex Orders

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg LP); Hélyette Geman (Birkbeck, University of London; ESCP Europe); Dilip B. Madan (University of Maryland); Marc Yor (Paris VI and VII) |
| **Year** | 2011 (*Quantitative Finance* 11(11), 1685–1694; this working-paper copy dated 8 October 2009) |
| **Type** | Journal paper (working-paper version, 28pp). S&P 500 daily data January 1990 to December 2008, plus a handful of over-the-counter quotes from early 2009 |
| **PDF** | Not hosted in this repository (journal article, no open licence) |
| **Find it** | [doi.org/10.1080/14697680903397675](https://doi.org/10.1080/14697680903397675) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Options+on+Realized+Variance+and+Convex+Orders%22+Carr) |
| **BibTeX** | `carr2011convex` |
| **Status** | Reference: §1 (Lévy processes), §2 (S&P 500 and acceptability pricing) and §4 (models that guarantee an increase) |

## What it is

A paper about a basic property that options on a traded asset always have, and options on
realized variance need not.

- **The property.** For a stock, a call at a fixed moneyness is worth more the longer its
  maturity. Equivalently, the risk-neutral distributions of the forward-scaled price get
  wider with maturity "in the convex order", so every convex payoff is worth more later.
  This follows from no-arbitrage because the stock is traded and its forward-scaled price
  is a martingale.
- **Why it can fail for variance.** Realized variance over different horizons is not one
  traded price evolving over time. The paper scales realized variance to have expectation
  one at each maturity and asks whether calls on it rise or fall with maturity.
- **Lévy models give a decrease.** If the stock follows a pure-jump Lévy process (variance
  gamma, CGMY, normal inverse Gaussian and so on), realized variance per unit time is a
  backward martingale. Averaging independent increments narrows its distribution, so call
  prices on normalised realized variance fall with maturity. For the variance gamma model
  the authors give the prices in closed form. This is a law-of-large-numbers effect, not
  mean reversion.
- **The S&P 500 under the real-world measure.** A long-memory regression for log squared
  daily returns, simulated forward 10,000 times from December 2008, gives distributions
  for normalised realized variance that shrink slowly with maturity.
- **Risk-neutral evidence points the other way.** Pricing the same options so that the
  required margin of safety rises slightly with maturity (the authors' "acceptability"
  pricing) produces distributions that widen with maturity. Three at-the-money straddle
  quotes on SPX realized variance from early 2009 also rise with maturity once scaled
  (0.7113 for June 2009, 0.7397 for December 2009, 0.7430 for December 2010). That is a
  very small sample.
- **Stochastic volatility models are mixed.** Heston and the CGMY stochastic-clock models
  produce increases at some strikes and maturities and decreases at others, and tend to a
  decrease eventually because their variance processes are stationary.
- **A model that guarantees it.** Making instantaneous variance a normalised exponential of
  a Lévy process ensures that normalised realized variance increases in the convex order.
  Simulations suggest other transformations work too.

## Why it's in the library

**It shows what a variance-option model has to get right.** Standard models with
independent increments imply that options on realized variance get cheaper with maturity
at a fixed scaled strike. If market prices show the opposite, the model must keep
volatility persistent enough to stop averaging from narrowing the distribution.

**It separates traded and non-traded underlyings.** Calendar-arbitrage bounds that hold
for options on a stock do not carry over to options on variance or on the VIX. That
matters when building a term structure of volatility options.

**The market evidence is thin.** Three straddle quotes from one crisis period are
suggestive at best. The real-world result rests on one regression model of S&P 500
variance. Read the empirical part as an illustration of the question, not an answer.

## Links

- [[merton-1976]] — the jump models whose averaging effect drives the decrease in §1
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] —
  options on volatility used in practice, the market this paper's question applies to
