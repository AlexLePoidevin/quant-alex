# On the Hedging of Options on Exploding Exchange Rates

| | |
|---|---|
| **Authors** | Peter Carr (Courant Institute, NYU), Travis Fisher, Johannes Ruf (Oxford-Man Institute) |
| **Year** | 2014 (published in Finance and Stochastics; this copy is arXiv 1202.6188v3, 24 November 2013) |
| **Type** | Journal article (arXiv version), 30pp |
| **PDF** | `carr-fisher-ruf-2014-on-the-hedging-of-options-on-exploding-exchange-rates.pdf` (arXiv copy) |
| **BibTeX** | `carr2014exploding` |
| **Status** | Reference: §3 (Theorem 3.4 and the corollaries on put-call parity) and §4 (the hyperinflation interpretation) carry the results; §2 and the appendix are the measure theory |

## What it is

A fix for a pricing problem that appears when an exchange rate is modelled as a *strict
local martingale*. That is a process with no expected drift locally, but whose expected
future value is below today's value. Several FX smile models, including the "quadratic
normal volatility" family and some SABR parameterisations, have this property.

- **The problem.** If the exchange rate X (dollars per euro) is a strict local martingale
  under the dollar pricing measure, then pricing claims as expected payoffs breaks things:
  - put-call parity fails for model prices;
  - one euro delivered at T is "worth" less than one euro today;
  - the dollar and euro views of the same option disagree.
- **The proposal.** Price a claim at the cheapest cost of a strategy that replicates it
  almost surely under *both* the dollar measure and the euro measure at once. When X is a
  strict local martingale the two measures are not equivalent: each assigns probability
  to events the other treats as impossible. Replicating under both is therefore dearer
  than replicating under one.
- **The main result (Theorem 3.4).** The joint replication price in dollars is the
  dollar-measure expectation of the payoff, plus today's rate times the euro-measure
  value of the payoff on the event that X explodes (the dollar becomes worthless against
  the euro) before maturity.
- **What it restores.**
  - The price of one euro is exactly today's exchange rate, replicated by buy-and-hold.
  - Put-call parity holds.
  - International put-call equivalence holds: a dollar call on euros matches a euro put
    on dollars.
  - Calls get a correction term, equal to today's rate times the euro-measure probability
    of an explosion. This matches Lewis's earlier pricing formula for stochastic-volatility
    models, which had been justified only by postulating parity. Here it is a hedging cost.
- **The interpretation (§4).** Under a real-world measure that allows either currency to
  hyperinflate (the dollar–mark rate moved by a factor of about 10¹⁰ in 1922–23), the
  exchange rate is a strict local martingale under a pricing measure exactly when that
  currency's hyperinflation has positive probability. So the "bubble" in the model is the
  priced chance of a currency collapse. The result needs a no-obvious-hyperinflation
  condition, and the paper shows a counterexample without it.

## Why it's in the library

**It matters for anyone fitting an FX smile with a convenient model.** Models that fit the
smile well can quietly be strict local martingales. Their naive prices then break parity
and give different answers depending on which currency you price in. This paper gives the
price that is consistent from both sides of the currency pair, and the hedge behind it.

**It turns a technical defect into an economic statement.** The correction term is the
value of the chance that one currency becomes worthless. That is a tail event, which an
expected-value pricer leaves out.

**It is mathematical, not empirical.** There is no data and no calibration. Its value is in
saying which prices are internally consistent, not in saying what the market charges.

## Links

- [[merton-1976]] — the classic way to add extreme moves to an option model; here the
  extreme event is a currency's complete collapse
- [[carr-kakushadze-2017-fx-options-in-target-zone]] — FX options when the rate is held inside a band
- [[carr-wu-2007-stochastic-skew-in-currency-options]] — how currency risk reversals swing and change sign in the data
