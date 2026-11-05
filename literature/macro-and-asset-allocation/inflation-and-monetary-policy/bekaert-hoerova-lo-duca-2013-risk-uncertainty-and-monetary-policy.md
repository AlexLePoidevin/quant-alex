# Risk, Uncertainty and Monetary Policy

| | |
|---|---|
| **Authors** | Geert Bekaert (Columbia and NBER), Marie Hoerova, Marco Lo Duca (European Central Bank) |
| **Year** | 2013 (the copy is NBER Working Paper 16397, September 2010) |
| **Type** | Journal article, *Journal of Monetary Economics* 60(7), 771–788. doi:10.1016/j.jmoneco.2013.06.003. 51pp working paper |
| **PDF** | Local copy only (NBER working paper, © the authors, all rights reserved) |
| **BibTeX** | `bekaert2013risk` |
| **Status** | Reference: §2.1 (splitting the VIX), §3.1 (benchmark VAR) and §4 (identification from Fed funds futures) carry the results. The published version may differ in detail from this 2010 draft |

## What it is

An empirical paper on whether loose monetary policy makes investors less risk averse,
using the VIX as the window. It splits the VIX into two parts and traces how each responds
to the Fed, and vice versa, from January 1990 to July 2007 (pre-crisis) and to August 2010.

- **Splitting the VIX.** The squared VIX is the option market's expected variance under
  risk-neutral pricing. The authors forecast actual next-month realised variance (from
  5-minute returns) with the squared VIX and past realised variance. The fitted value is
  "uncertainty" (physical expected variance). What is left, squared VIX minus that forecast,
  is the variance premium, labelled "risk aversion". The fitted rule is
  RVAR = −0.00002 + 0.299·VIX² + 0.442·RVAR (lagged one month); it was chosen from eight
  candidate forecasting models.
- **Monetary policy stance.** The real rate (Fed funds target minus CPI inflation). From
  December 2008 the zero-bound rate is replaced by the lower of 0.125% and a Taylor-rule
  rate. Robustness checks use the Taylor-rule residual, the nominal rate and M1 growth.
- **The VAR.** Four variables: industrial production growth, the real rate, risk aversion
  and uncertainty, with 3 lags. Identification is either a recursive ordering or adds a
  long-run restriction that money has no permanent effect on output.
- **Main result.** A one-standard-deviation cut in the real rate (about 34 basis points)
  lowers risk aversion from about 9 months later. The peak effect comes at about 20 months,
  and the effect stays significant to about 40 months. Monetary policy shocks explain over
  20% of the variance of risk aversion at horizons beyond about 30–37 months. Uncertainty
  responds the same way but slightly more weakly.
- **The other direction is weak.** Higher risk aversion or uncertainty is followed by
  looser policy, but this is mostly not statistically significant.
- **Business cycle.** Uncertainty shocks, not risk-aversion shocks, lower industrial
  production, consistent with Bloom (2009).
- **Alternative identification.** The same signs appear when policy shocks are measured
  from Fed funds futures moves in a 30-minute window around FOMC announcements. They also
  appear with monthly futures-based surprises cleaned of economic news (Bernanke and
  Kuttner). In the high-frequency regressions, risk aversion reacts to policy surprises
  (significant at 5%) more strongly than uncertainty (significant only at 16%).
- **The crisis sample is weaker.** Adding 2007–2010 keeps the signs but most effects are
  significant only at 68% confidence. The VIX spike and the zero bound make that period
  hard to measure.

## Why it's in the library

**It is the evidence behind the "Fed put" as a risk-appetite channel.** The finding is
that easier policy compresses the variance premium, the part of the VIX that is pure price
of risk, with a lag of about nine months and an effect lasting two years. That connects the
policy cycle to risk premia across the library: the volatility risk premium, the stock–bond
correlation regimes, and the risk-on/risk-off papers.

**The VIX decomposition is reusable.** Squared VIX minus a forecast of realised variance is
a simple, standard way to separate fear (price of risk) from expected turbulence. It is the
same object as the variance risk premium in the volatility section, with the sign flipped.

**The strong results are pre-crisis.** The results are strongest pre-crisis and lean on VAR
identification. The full-sample effects mostly clear only 68% bands. The "risk aversion"
label is a residual, so it also absorbs forecasting error and any other non-linear pricing
effects.

## Links

- [[carr-wu-2009-variance-risk-premia]] — the variance risk premium this paper uses as its risk-aversion measure
- [[caballero-kamber-2019-global-impact-of-risk-off-shocks-and-policy-puts]] — how risk-off shocks spread and how the policy put responded after 2008
- [[keerati-2020-the-impact-of-monetary-policy-on-the-specialness-of-us-treasuries]] — another channel from Fed surprises to asset prices
- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — monetary policy regimes and the sign of the bond–stock correlation
- [[baele-van-holle-2017-stock-bond-correlations-macroeconomic-regimes-and-monetary-policy]] — accommodating policy and negative stock–bond correlations across 10 countries
- [[smales-2016-risk-on-risk-off-financial-market-response-to-investor-fear]] — how markets respond to VIX shocks day to day
