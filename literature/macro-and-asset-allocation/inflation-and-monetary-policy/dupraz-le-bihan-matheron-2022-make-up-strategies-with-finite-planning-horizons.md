# Make-up Strategies with Finite Planning Horizons but Forward-Looking Asset Prices

| | |
|---|---|
| **Authors** | Stéphane Dupraz (Banque de France), Hervé Le Bihan (Banque de France, Banco de España), Julien Matheron (Banque de France) |
| **Year** | 2022 (Banque de France Working Paper 862, January 2022) |
| **Type** | Central-bank working paper, 50pp. Published as "Make-up strategies with finite planning horizons but infinitely forward-looking asset prices", *Journal of Monetary Economics* 143, 103542 (2024), doi:10.1016/j.jmoneco.2023.11.006 |
| **PDF** | Not hosted in this repository (working paper download, no open licence) |
| **Find it** | [doi.org/10.1016/j.jmoneco.2023.11.006](https://doi.org/10.1016/j.jmoneco.2023.11.006) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Make-up+Strategies+with+Finite+Planning+Horizons+but+Forward-Looking+Asset+Prices%22+Dupraz) |
| **BibTeX** | `dupraz2024makeup` |
| **Status** | Reference: the non-technical summary, §1, §5.3–5.4 (calibration and forward-guidance responses), §6.3–6.4 with Table 2 and §7 carry the results; the derivations in §3–4 were skimmed |

## What it is

A monetary-policy model that asks whether "make-up" strategies work: promising to keep
rates lower for longer after a spell at the lower bound, or targeting average inflation so
that past undershoots are made up. The Fed adopted flexible average inflation targeting in
August 2020, and the ECB's 2021 strategy points the same way.

- **The tension.** In the standard New Keynesian model, agents are fully forward-looking,
  so promises about far-future rates have implausibly large effects today: the
  "forward-guidance puzzle". Survey evidence says households barely react to such
  announcements. Asset prices, though, react strongly and fast.
- **The model.** Households and firms have finite planning horizons (Woodford, 2019), an
  average of one quarter in the main calibration. Financial markets are fully rational
  about the path of policy rates and build it into the long-term rates everyone faces. The
  authors call this forward-looking asset prices.
- **Forward guidance still works, without the puzzle.** Because long rates carry the
  promise to short-sighted households and firms, lower-for-longer policy remains effective.
  Because those agents still can't foresee its full consequences, the effect doesn't
  explode with the horizon of the promise.
- **Make-up strategies help, but less than in textbook models.** In 500 simulations of 300
  quarters, inflation targeting spends about 12% of the time at the lower bound, with
  inflation 9bp and output 26bp below target on average. A lower-for-longer rule cuts the
  volatility of inflation and output by about 7%. Eight-year average inflation targeting
  cuts output-gap volatility from 3.43 to 2.76 and inflation's from 1.36 to 1.12. Price-level
  targeting does best (2.64 and 1.08).
- **The lower bound weakens, not strengthens, the case for average targeting.** With fully
  rational agents the lower bound causes deep deflation spirals that average targeting
  prevents. In this model those spirals are mild, and the lower bound mainly stops average
  targeting from delivering lower rates in the near future.

## Why it's in the library

**It is about how policy promises reach asset prices.** The model's key assumption, that
markets price the full expected path of policy into long rates even when households and
firms don't look ahead, is the channel through which guidance and make-up strategies act.
It explains why long yields move on central-bank communication even when surveys show the
public isn't listening.

**It is background for the post-2020 policy regime.** Average inflation targeting is
designed to let inflation run above target after a shortfall, which matters for how long
rates stay low and for inflation risk in bond and equity portfolios.

**It is a calibrated model, not an empirical test.** The planning horizon, the shocks
(estimated from US data) and the 0% lower bound drive the numbers. The conclusions are
about relative performance across policy rules within that model.

## Links

- [[menand-2021-the-federal-reserve-and-the-2020-economic-and-financial-crisis]] — what the Fed actually did in 2020, the year it adopted average inflation targeting
- [[caballero-kamber-2019-global-impact-of-risk-off-shocks-and-policy-puts]] — how central-bank responses to risk-off shocks feed through to markets
- [[aqr-2021-inflation-outlook-the-macro-the-micro-the-transitory]] — the inflation debate the new strategies were tested against in 2021
- [[aqr-2020-fire-and-ice-inflation-and-deflation]] — asset behaviour under the deflation and inflation risks these strategies try to manage
