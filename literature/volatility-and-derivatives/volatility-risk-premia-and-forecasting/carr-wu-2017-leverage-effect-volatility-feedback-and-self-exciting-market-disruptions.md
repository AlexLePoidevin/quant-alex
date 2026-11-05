# Leverage Effect, Volatility Feedback, and Self-Exciting Market Disruptions

| | |
|---|---|
| **Authors** | Peter Carr (NYU Courant), Liuren Wu (Baruch College, CUNY) |
| **Year** | 2017 (first draft 2007; SSRN 1306495) |
| **Type** | Paper, *Journal of Financial and Quantitative Analysis* 52(5), 2119–2156. The local copy is the 73-page February 2016 author version. An earlier September 2011 draft is also in the source folder |
| **PDF** | Local copy only (author version of a journal article, no open licence) |
| **BibTeX** | `carr2017leveragefeedback` |
| **Status** | Reference: §II is the model, §IV.A the index results (parameters, crisis history, variance-risk-premium decomposition), §IV.B the five single stocks |

## What it is

A structural option-pricing model that splits the familiar negative correlation between
equity returns and volatility into three separate economic channels, and uses the
cross-section of S&P 500 options to measure each one.

- **The three channels.**
  - **Financial leverage.** Volatility rises when equity falls relative to assets: Black's
    (1976) leverage effect. Here leverage can also be managed actively, so the leverage
    ratio has its own target-seeking dynamics.
  - **Volatility feedback.** A rise in business risk raises the cost of capital and lowers
    asset value. This gives a negative return–volatility correlation even for a firm with
    no debt, consistent with Hasanhodzic and Lo's finding that all-equity firms show the
    same "leverage effect".
  - **Self-exciting disruptions.** Downward jumps whose intensity jumps up after each one,
    so one crash makes the next more likely.
- **The model.** Index forward = risky asset value × equity-to-asset ratio.
  - The asset has a diffusive variance with negative correlation to returns (feedback).
  - It also has downward jumps whose arrival rate jumps up after each jump (self-excitement).
  - The equity-to-asset ratio X raises return variance by a power p as it falls, and
    targets a level that responds to both kinds of business risk.
  - Option pricing uses time-changed Lévy machinery and the FFT. Estimation uses an
    unscented Kalman filter.
- **Data.** Over-the-counter SPX implied-volatility quotes, January 1997–October 2014,
  sampled weekly. Eight maturities from one month to five years, at strikes 80–120% of spot:
  40 series in all. The long maturities are what let the three channels be separated.
- **Index results.**
  - Average variance contributions are 10.7% vol from leverage, 16.0% from diffusion and
    13.0% from jumps, so all three matter.
  - Leverage power p = 3.49. Feedback correlation ρ = −0.89. The risk-neutral jump size
    is about 19.5%, and its intensity barely mean-reverts (κ ≈ 0.001), so crash risk is
    persistent.
  - The three channels act on different parts of the surface. Feedback acts on short-dated
    options and high strikes. Jump intensity acts on low strikes, peaking at three to six
    months. Leverage moves the at-the-money level and lasts out to long maturities.
- **Where the variance risk premium comes from.** The negative index variance risk
  premium comes from the diffusive-volatility and jump channels. The leverage channel
  contributes a slightly positive premium. Short-dated variance swaps therefore load on the
  transient diffusion premium and long-dated ones on persistent jump and leverage risk.
  This is consistent with short-term variance swaps carrying larger negative premia.
- **Leverage choices.** The aggregate market does not deleverage when ordinary diffusive
  risk rises. Leverage actually increases. It deleverages only when crash (jump) risk
  rises.
  - The filtered paths show this around 1997, 1998 (LTCM: the second-largest jump-intensity
    spike after 2008), the 2000 Nasdaq peak, and 2008, when leverage stayed high despite
    deleveraging because equity values fell so far.
- **Five single stocks.** GE, WMT, JPM, DUK and XOM represent industrials, staples, banks,
  utilities and energy.
  - The leverage effect is strongest for GE (p = 3.82), whose debt is held fixed, and weak
    for JPM (p = 1.64), which manages leverage actively and is the only one of the five
    with strong mean reversion in leverage.
  - Volatility feedback is strongest for XOM (ρ = −0.96).
  - Every stock's feedback is weaker than the index's, as expected if feedback comes from
    systematic shocks.

## Why it's in the library

- **"Leverage effect" names three different mechanisms.** A model that fits one negative
  correlation cannot tell whether volatility rises because balance sheets are levered,
  because risk is repriced, or because a crash is feeding on itself. Each has different
  maturity and strike signatures, and different implications for hedging.
- **Self-exciting crash risk, measured.** Its intensity is persistent and jumps after
  each downward move. This is the option-implied counterpart of contagion and clustering
  in crashes, and it explains why long-dated puts stay expensive after a shock.
- **The variance risk premium has components.** Shorting short-dated variance mainly
  earns the diffusive premium; longer-dated variance carries crash and leverage risk. That
  matters for anyone holding or selling variance at different tenors.
- **Limits.** The model is heavily parameterised and fit to one bank's OTC quotes. The
  single-stock section is described by the authors as preliminary: five names, one per
  sector.

## Links

- [[merton-1976]] — jumps of random size in prices, which this model makes self-exciting
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — a practitioner's version of the same
  feedback loop: leverage set by volatility, stable until a shock reverses it
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] —
  self-exciting (Hawkes) jumps at intraday scale, the microstructure analogue of the
  crash-intensity process here
- [[carr-wu-2009-variance-risk-premia]] — measuring the variance risk premium
- [[harvey-et-al-2018-the-impact-of-volatility-targeting]] — why the leverage effect makes volatility targeting raise Sharpe ratios for equities and credit only
