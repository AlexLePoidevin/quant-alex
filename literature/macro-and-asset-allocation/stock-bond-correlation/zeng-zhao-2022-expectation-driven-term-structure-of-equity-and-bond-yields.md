# Expectation-Driven Term Structure of Equity and Bond Yields

| | |
|---|---|
| **Authors** | Ming Zeng (University of Gothenburg, Swedish House of Finance), Guihai Zhao (Bank of Canada) |
| **Year** | 2022 (last updated 11 May 2022) |
| **Type** | Bank of Canada Staff Working Paper 2022-21, 59pp. Equilibrium model with subjective expectations, US data from the late 1980s to 2019. Earlier title: "Term Structure of Equity and Bond Yields over Business Cycles". DOI 10.34989/swp-2022-21 |
| **PDF** | Local copy only (© 2022 Bank of Canada, no open licence) |
| **BibTeX** | `zeng2022expectation` |
| **Status** | Reference: §1 (summary of results), §2 (belief formation), §4 (equity yields, bond–stock comovement, strip-return predictability) carry the content |

## What it is

An asset-pricing model in which stock and bond prices move because investors' expectations
of growth move, not because their required returns move, fitted to survey forecasts.

- **The puzzles it addresses.** Recent evidence that standard models struggle with:
  survey expectations of returns barely vary; stock prices move mostly with expected cash
  flows; yields on short-dated dividend claims are more volatile than long-dated ones; the
  slope of equity yields (long minus short) falls in recessions; returns on dividend strips
  are predictable, less so at longer maturities; and the stock–bond correlation turned from
  positive to negative after the late 1990s.
- **How investors form beliefs.** They extrapolate from recent data (the "belief in the
  law of small numbers"), updating forecasts of latent states in dividend growth, GDP
  growth and inflation with learning gains estimated from survey consensus forecasts. The
  estimated gains imply under-reaction to news about GDP and inflation and over-reaction to
  news about dividends. Model dividend-growth expectations track survey forecasts with a
  correlation of about 0.80 (2003–2019).
- **Pricing.** Constant relative risk aversion makes the subjective risk premium constant,
  so equity yields move with expected dividend growth and bond yields with expected GDP
  growth and inflation. Short-horizon dividend expectations are volatile and revert towards
  a steadier long-run level, which makes short equity yields more volatile. In recessions
  short-run expectations collapse more than long-run ones, so the equity yield curve
  inverts: the model gives an average slope of 3.96% in expansions and −3.77% in
  recessions, against −5.50% in recession data.
- **The stock–bond correlation flip.** After 2000, expectations of real GDP growth and real
  dividend growth move together more closely, so real bonds hedge dividend risk better.
  That accounts for about 90% of the change in the bond–stock covariance; inflation
  becoming procyclical accounts for about 30% (the channels overlap).
- **Predictability.** With a constant premium, predictable strip returns come from
  predictable forecast errors and revisions: investors over-react to dividend news, and
  dividends mean-revert. The effect weakens with maturity because news moves long-run
  expectations less.
- **Fit.** Model 1- and 10-year bond yields correlate 0.92 and 0.95 with the data; model
  2- and 10-year dividend-strip returns correlate 0.63 and 0.52 with realised ones.

## Why it's in the library

**It is the expectations-based explanation of the stock–bond correlation flip.** Set next to
the policy-regime explanation, it says the flip is mostly about real growth and dividends
becoming more tightly linked, with inflation a smaller part. The two papers cannot both be
the whole story; together they show how much the hedging value of bonds depends on which
macro force dominates.

**It shows how far survey-based subjective expectations can go.** A model with a constant
risk premium and extrapolating beliefs matches a long list of facts that rational-expectations
models explain with time-varying risk premiums. That matters for anyone reading the equity
yield curve or valuation ratios as signals about future returns.

**It is a calibrated and estimated model, from a central-bank working paper.** The learning
gains are fitted to surveys and the fit is judged by correlations with the data, not by
out-of-sample tests. It is a coherent account, not proof.

## Links

- [[li-et-al-2022-does-fiscal-policy-matter-for-stock-bond-return-correlation]] — the competing explanation: a switch from monetary-led to fiscal-led policy around 2001
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — balanced and risk-parity portfolios rely on the negative stock–bond correlation this paper explains
- [[barberis-shleifer-2003]] — investors who extrapolate and move money between styles
- [[chen-roll-ross-1986]] — expected growth and inflation as macro risks in stock returns
