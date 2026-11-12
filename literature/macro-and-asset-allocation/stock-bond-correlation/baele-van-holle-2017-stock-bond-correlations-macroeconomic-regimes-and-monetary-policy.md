# Stock–Bond Correlations, Macroeconomic Regimes and Monetary Policy: An International Perspective

| | |
|---|---|
| **Authors** | Lieven Baele (Tilburg University), Frederiek Van Holle (Degroof Petercam Asset Management) |
| **Year** | 2017 (October 2017 draft) |
| **Type** | Working paper, SSRN 3075816, 78pp. 10 developed markets, monthly and quarterly, data to December 2013 with an out-of-sample check to March 2017 |
| **PDF** | Not hosted in this repository (SSRN working paper, no licence) |
| **Find it** | [doi.org/10.2139/ssrn.3075816](https://doi.org/10.2139/ssrn.3075816) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Stock%E2%80%93Bond+Correlations%2C+Macroeconomic+Regimes+and+Monetary+Policy%3A+An+International+Perspective%22+Baele) |
| **BibTeX** | `baele2017stockbond` |
| **Status** | Reference: §4 (inflation and output regimes), §5.2 (monetary-policy regimes) and §6.2, Table 10 (interacted regimes) carry the results |

## What it is

A test of what explains the sign of the stock–bond correlation in ten developed markets
(the US, Canada, Japan, the UK, Germany, France, the Netherlands, Belgium, Italy and
Spain). Its answer: inflation and growth regimes on their own explain little; monetary
policy explains much more.

- **The stylised fact.** US stock–bond correlations averaged about +20% in the 1970s and
  +40% in the 1980s and early 1990s, then about −20% from 1998. They ranged from +70% in
  late 1994 to −67% in 2003 and 2012. All ten markets switched to negative around 1998,
  except Japan, which turned negative in 1993. Correlations are estimated with a DCC-MIDAS
  model on daily returns.
- **Method.** Macro regimes are estimated first, separately from the correlations, so they
  can't be fitted to them; correlations are then regressed on regime dummies.
  - **Inflation:** low, intermediate and high regimes.
  - **Output gap:** recessions and expansions.
  - **Monetary policy:** a regime-switching Taylor rule splits "restrictive" policy (reacts
    strongly to inflation) from "accommodating" policy (reacts more to output).
- **Macro regimes alone don't explain it.**
  - **Inflation:** correlations are lower in the low-inflation regime, but almost every
    country entered that regime in the early 1990s, years before correlations turned
    negative.
  - **Output:** recession dummies explain very little.
  - **Procyclical inflation:** no such regime is found anywhere. That contradicts the
    popular explanation that inflation switched from countercyclical to procyclical
    around 2000.
- **Monetary policy does better.** With global policy-regime dummies, the average
  correlation is −11.5% under accommodating policy and +28.1% under restrictive policy.
- **The interaction is the main result.** Large negative correlations appear only when
  inflation is low and policy is accommodating: about −27% to −29%, in expansions and
  recessions alike. With restrictive policy in the same low-inflation state, the correlation
  is +24% to +34%. With high inflation it is +25% to +29% regardless of policy or growth.
  - **Fit:** one set of coefficients for all ten countries more than doubles the R² of an
    inflation-and-output model (59% against 26%), and gets the sign right 89% of the time
    (against 77%).
  - **Global versus local:** global regimes explain more than local ones.
- **The intuition offered.** When inflation is low, the fear is deflation. Credible easing
  makes a deflationary spiral less likely, which pushes bond yields up and lifts growth
  expectations and stocks: a negative correlation. Under restrictive policy, inflation
  news means rate hikes that hurt both, so the correlation is positive.
- **Out-of-sample check.** The model, fitted to December 2013, predicted the average US
  correlation over January 2014 to March 2017 correctly.

## Why it's in the library

**It gives a rule of thumb for when bonds hedge stocks.** Negative stock–bond correlation is
not a permanent feature; it needs both low inflation and a central bank leaning towards
growth. Take away either, as in 2022 with high inflation and a hiking Fed, and bonds stop
diversifying equities. That is the regime question behind every 60/40 and risk-parity
portfolio.

**It argues with the alternatives in the same topic.** The procyclical-inflation story
(Campbell, Pflueger and Viceira; Burkhardt and Hasseltoft) is not supported by this
paper's regime estimates, and the monetary-policy story is. The fiscal-leadership paper
offers a third account. The evidence is regressions on estimated regimes, so it is
association rather than proof of a mechanism. Peripheral Europe during the sovereign-debt
crisis and Japan fit worst.

## Links

- [[campbell-pflueger-viceira-2020-macroeconomic-drivers-of-bond-and-equity-risks]] — the inflation-cyclicality explanation this paper finds weak support for
- [[li-et-al-2022-does-fiscal-policy-matter-for-stock-bond-return-correlation]] — fiscal-led versus monetary-led policy as the driver of the sign flip
- [[brixton-thapar-maloney-2021-when-stock-bond-diversification-fails]] — inflation surprises as the reason stocks and bonds fall together
- [[liu-fan-2016-stock-bond-correlation-and-duration-risk-allocation]] — the week-to-week correlation as a signal for bond returns
- [[bekaert-hoerova-lo-duca-2013-risk-uncertainty-and-monetary-policy]] — how accommodating policy lowers risk aversion, part of this paper's intuition
- [[bekaert-engstrom-2010-inflation-and-the-stock-market-the-fed-model]] — why stock and bond yields moved together in stagflationary periods
