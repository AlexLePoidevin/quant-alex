# Switching Risk Off: FX Correlations and Risk Premia

| | |
|---|---|
| **Authors** | Alessandro Beber (Cass Business School); Michael W. Brandt (Duke); Jason Cen (Cass) |
| **Year** | 2013 (November 2013 draft for the Third FX Workshop; posted to SSRN as 2508651) |
| **Type** | Working paper, marked "preliminary and incomplete", 53pp |
| **PDF** | Local copy only (pre-publication draft marked "please do not circulate") |
| **BibTeX** | `beber2013switching` |
| **Status** | Reference: §3 (the correlation regimes), §4.2–4.5 (returns by regime transition) and §4.7 (returns after a transition) carry the results |

## What it is

An attempt to date "risk-off" episodes from the foreign-exchange market itself: days when
currencies suddenly move in lock-step, risky currencies falling together and safe havens
rising.

- **The model.** Daily G10 exchange rates against the dollar, January 1995 to October 2013.
  Each rate's volatility is filtered with a GARCH(1,1). The standardised returns then follow
  a regime-switching correlation model (Pelletier's RSDC) with two correlation matrices and
  a Markov chain that switches between them, estimated by EM.
- **The two regimes.** One has high correlations across most currencies, except the yen
  (and partly the Swiss franc), which move away from the rest. The other has lower
  correlations, with the yen more in line. Expected durations are 33 days for the
  high-correlation regime and 110 for the low. The high regime lasts for long only in
  2007–09 and the 2010–12 euro crisis. The first principal component explains more variance
  in the high regime: about 11 percentage points more on high-regime days.
- **Risk-off days.** A switch from the low to the high regime (transition probability above
  0.2) picks out 39 episodes, matching the Asian crisis, the Russian default, the dot-com
  bust, the subprime crisis and the euro crisis. Many are not tied to any news about
  fundamentals. The regime probabilities barely move with the VIX or FX volatility, so they
  carry different information.
- **Returns at the switch.** On low-to-high days the G10 carry trade loses 49 bps on
  average. The Australian and New Zealand dollars, Canadian dollar and Norwegian krone fall
  sharply, while the yen and franc gain. The paper annualises this to 123% a year, which
  says nothing about holding the trade. On high-to-low days carry gains 34 bps. Momentum
  barely reacts to either switch.
- **Volatility depends on the regime.** The usual finding is that higher volatility means
  carry losses. Here it depends on the switch. A one-standard-deviation rise in the VIX
  with a low-to-high switch goes with a 38 bps carry loss; with a high-to-low switch, with a
  gain of nearly 100 bps. With global FX volatility in place of the VIX the risk-off loss is
  123 bps. Adding the regimes raises the explained share of daily carry returns from 8%
  (VIX alone) to 10%.
- **After the switch.** After a low-to-high switch, carry keeps losing: about 200 bps
  cumulative by day 20 and more than 500 bps by day 60. After a high-to-low switch it gains
  about 2% over the following month.
- **Positioning.** CFTC data on speculators' futures positions agree: after risk-off
  switches, net positions in the Australian dollar fall by about half against their
  pre-event average, while positions in the franc and the dollar rise by 30–40%.

## Why it's in the library

**It measures a crash regime through correlation, not volatility.** Risk-off shows up as a
change in the shape of the correlation matrix (currencies split into risky and safe
groups) before, and sometimes without, a change in volatility. Lehman is the example: the
VIX began falling while FX correlations stayed in the high regime.

**It explains why carry has crash risk.** Carry earns its premium in calm, low-correlation
markets and loses it in sudden risk-off switches. Correlation regimes say when the
negative volatility exposure actually bites.

**Read it as a draft.** It is marked preliminary. The regime dates are estimated on the
full sample, so the "after the switch" returns are not a tradable forecast. The R² gain is
small (8% to 10%).

## Links

- [[ang-chen-2002]] — correlations rise in down markets for stocks; this paper finds the FX
  version, where correlations polarise rather than simply rise
- [[laloux-et-al-1999]] — the largest eigenvalue of a correlation matrix as the market
  mode, which the paper's variance-ratio test measures by regime
- [[munnix-schafer-2011-copula-dependencies]] — equity dependence in the tails exceeds what
  one correlation coefficient implies; the regimes here are another way of saying a single
  correlation matrix is not enough
- [[shevchenko-2006-implied-correlation-for-pricing-multi-fx-options]] — the currency-triangle
  identity the paper uses to turn dollar-based correlations into cross-rate volatilities
- [[doman-doman-2020-daily-fx-volatility-and-the-time-of-day]] — another FX volatility measurement result
- [[badshah-et-al-2018-asymmetric-linkages-fear-index-and-emerging-market-volatility]] — how VIX shocks spread to emerging-market implied volatility, asymmetrically and mostly in the upper tail
- [[baur-smales-2018-gold-and-geopolitical-risk]] — gold as a haven against geopolitical threats, a different kind of risk-off from financial stress
- [[caballero-kamber-2019-global-impact-of-risk-off-shocks-and-policy-puts]] — what a risk-off shock does to stocks, yields and currencies, and how central-bank puts shortened it
- [[smales-2016-risk-on-risk-off-financial-market-response-to-investor-fear]] — risk-on/risk-off measured with the VIX across stocks, bonds and currencies
- [[stavrakeva-tang-2019-the-dollar-during-the-great-recession]] — the dollar's flight-to-safety rally in 2008–2012, traced to the Fed's forward guidance
