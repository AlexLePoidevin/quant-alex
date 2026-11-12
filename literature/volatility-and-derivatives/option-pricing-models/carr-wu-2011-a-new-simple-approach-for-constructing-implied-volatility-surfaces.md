# A New Simple Approach for Constructing Implied Volatility Surfaces

| | |
|---|---|
| **Authors** | Peter Carr, Liuren Wu (NYU and Baruch College) |
| **Year** | 2011 (talk at Columbia University, 28 February 2011) |
| **Type** | Slides, 23pp. The theory was later published as Carr and Wu, "Analyzing volatility risk and risk premium in option contracts: A new theory", *Journal of Financial Economics* (2016) |
| **PDF** | Not hosted in this repository (seminar slides with no licence) |
| **Find it** | [search Google Scholar](https://scholar.google.com/scholar?q=%22A+New+Simple+Approach+for+Constructing+Implied+Volatility+Surfaces%22+Carr) for the title and authors |
| **BibTeX** | `carr2011surfaces` |
| **Status** | Reference: slides 6–11 (the PDE, the quadratic equation, the two dynamics) and 18–20 (fit against Heston) |

## What it is

A seminar deck that models the implied volatility of each option directly, rather than the
instantaneous volatility of the stock. It derives the whole implied volatility surface as
the solution of a quadratic equation.

- **Where it sits.** There are two existing approaches.
  - Stochastic-volatility models (Heston, SABR) assume dynamics for the unobservable
    instantaneous vol. They are slow to calibrate.
  - "Market models" of implied vol take today's surface as given and model how it moves.
    They are constrained in ways that are often unknown: for example, a downward-sloping
    smile rules out positive spot–vol correlation.

  This deck assumes dynamics for the implied vols themselves and derives today's surface.
- **The no-dynamic-arbitrage PDE.** Each option's implied vol follows a diffusion with a
  drift and a vol of vol, all driven by one Brownian motion correlated with the stock.
  No arbitrage between an option, a basis option and the stock gives one linear relation:
  theta equals vega × drift, plus gamma × spot variance, plus vanna × covariance, plus
  volga × vol-of-vol variance. The authors call it the Vega–Gamma–Vanna–Volga (VGVV)
  model.
- **From PDE to algebra.** Substitute the BMS Greeks, which are all multiples of dollar
  gamma. The relation becomes an algebraic equation in the implied vol. If the drift and
  vol of vol do not depend on the implied vol itself, each point on the surface is the
  root of a quadratic.
- **Two tractable dynamics.** Each has six coefficients: mean-reversion speed, long-run
  level, vol of vol, its decay with maturity, correlation and current instantaneous vol.
  - Square-root implied variance (SRV) gives a quadratic in standardised moneyness.
  - Log-normal implied variance (LNV) gives a quadratic in log relative strike.

  At zero maturity the smile is the spot variance plus terms in correlation and vol of
  vol. At infinite maturity it flattens to the long-run level.
- **Fast calibration.** The coefficients are treated as a random-walk state and the
  quotes as noisy observations, then fitted with an unscented Kalman filter. Fitting 573
  weeks of surfaces takes about half a second, against about a minute for Heston.
- **Results.**
  - FX (JPYUSD and GBPUSD, 1997–2007, 31,515 options): RMSE of 0.36–0.40 vol points
    for JPYUSD and 0.12–0.14 for GBPUSD. All three models fit with R² of 0.98–0.99, and
    LNV is best.
  - SPX (30,120 options, one month to five years): LNV's RMSE is 0.67 vol points against
    1.12 for Heston, with R² of 0.99 against 0.95 and less autocorrelated errors.

## Why it's in the library

**It is the surface-building version of the P&L-attribution idea.** The same four Greeks
that explain an option's daily P&L, once their expected gains must balance theta, pin
down the shape of the smile. Building a surface needs only solving quadratics, with no
characteristic functions and no Fourier inversion.

**It is honest about what is open.**
- The construction guarantees no dynamic arbitrage between each option and the basis
  option. It does not guarantee static no-arbitrage (no negative butterflies or calendar
  spreads) across the whole surface.
- It is single-factor and continuous, with no jumps.

These are the gaps to check before using the method for quoting.

**It documents two stylised facts worth remembering.**
- SPX skew, measured against standardised moneyness, does not flatten as maturity
  rises out to five years.
- Long-dated FX smiles barely smiled before 2001, but since then they "smile, smirk, and
  are constantly switching into different faces".

## Links

- [[bakshi-et-al-2008-stochastic-risk-premiums-and-skewness-in-currency-options]] — the
  same authors' structural model of the FX smile, estimated with the same unscented Kalman
  filter
- [[carr-wu-2020-option-profit-and-loss-attribution-and-pricing]] — the published,
  general version of the pricing relation these slides start from
- [[gayda-et-al-2022-option-liquidity-and-gamma-imbalances]] — what market makers'
  gamma and vega inventories do to SPX option prices in practice
- [[carr-wu-2016-analyzing-volatility-risk-and-risk-premium-in-option-contracts]] — the published paper behind these slides
- [[bloch-2016-a-practical-guide-to-quantitative-volatility-trading]] — another parametric, arbitrage-free surface model (MixVol: a mixture of shifted lognormals), with variance-swap and dispersion applications
- [[horvath-muguruza-tomas-2021-deep-learning-volatility]] — another route to fast surface calibration: a neural network trained to reproduce a slow (rough) volatility model's surface
