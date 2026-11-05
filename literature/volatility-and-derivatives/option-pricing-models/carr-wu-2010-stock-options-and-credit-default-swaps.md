# Stock Options and Credit Default Swaps: A Joint Framework for Valuation and Estimation

| | |
|---|---|
| **Authors** | Peter Carr (Bloomberg; Courant Institute, NYU), Liuren Wu (Baruch College) |
| **Year** | 2010 (published in the Journal of Financial Econometrics 8(4); this copy is the working paper dated 26 September 2006, first draft April 2004) |
| **Type** | Journal article (working-paper version), 43pp |
| **PDF** | Local copy only (working-paper download, no open licence) |
| **BibTeX** | `carr2010stock` |
| **Status** | Reference: §1 (the model and pricing formulas), §2.3 (the stylised link between CDS spreads and implied volatility) and §4 (estimates and factor impacts) carry the results |

## What it is

One model that prices a company's stock options and its credit default swaps (CDS)
together, estimated on both markets at once.

- **The model.** Default arrives as a Poisson event with a random intensity λ. On default
  the stock goes to zero. Before default the stock diffuses with stochastic variance v,
  and its risk-neutral drift is raised by λ to pay for the chance of default. The default
  intensity is λ = βv + z: part of it moves with stock variance (loading β) and part, z,
  is an independent credit factor. Both v and z are square-root processes, and stock
  returns are negatively correlated with v (the leverage effect).
- **Tractable prices.** Option prices come from a Fourier transform that is exponential
  affine in (v, z), inverted by FFT. CDS spreads come from the same affine machinery as a
  ratio of protection-leg to premium-leg values. Both have closed-form coefficients.
- **The stylised facts it is built to match.** For General Motors, Ford, Altria and Duke
  Energy (January 2002 to April 2004), five-year CDS spreads rise with at-the-money
  implied volatility and with a steeper negative skew. Weekly changes in the two are
  correlated 0.52–0.61. A regression of the CDS spread on ATM volatility and skew
  explains 83% of its variation for Ford but only 36% for Altria, so the two markets
  share a factor but also move separately.
- **Estimation.** Weekly data: five CDS maturities (1–10 years) and 39 option series (30,
  60 and 91 days; 13 deltas) per company. The model is estimated by quasi-maximum
  likelihood with an unscented Kalman filter, treating v and z as hidden states.
- **Fit.** Over 90% of the variation in most option series is explained. CDS spreads fit
  less well: over 80% for Ford and Duke, about 50% for GM and about 30% for Altria. GM's
  CDS curve steepened sharply after 2003, which the two-factor model cannot follow.
- **What the estimates say.**
  - The independent credit factor z is far more persistent than stock variance, under
    both the pricing and the real-world measure. Variance shocks fade quickly along the
    maturity curve; credit shocks last.
  - The market price of variance risk comes out positive and the market price of the
    independent credit risk negative for all four firms. In this decomposition the
    negative risk premium in single-stock options comes from default risk, not from
    diffusion variance.
  - Average default intensity is much lower under the real-world measure than under the
    pricing measure, as the corporate-bond literature also finds.
  - Recovery rates are identified separately from default intensity, at 47–81%, which
    pure CDS data cannot do.
- **Where each factor shows up.** Variance shifts the implied-volatility smile roughly
  evenly across strikes. The credit factor mainly lifts low-strike (put) volatilities, and
  its effect grows with maturity: for six-month options it is about as large as the
  variance factor's. In CDS spreads, the credit factor dominates at long maturities, and
  variance matters only at the short end.

## Why it's in the library

**It explains part of the equity skew as default risk.** The steep negative skew in single-stock
options is usually modelled as stock-volatility correlation or as jumps. Here a
measurable part of it is the market pricing a jump to zero. The same risk is traded
separately in the CDS market, so the two markets can be checked against each other.

**It is a clean template for joint estimation across markets.** The approach treats risk
factors as hidden states and fits several markets that load on them differently through
one filter. That is how a recovery rate gets pinned down when one market alone cannot.

**Read the empirical part as illustrative.** It covers four firms over about two years,
with weekly data and a period dominated by the 2002 credit stress. The model fails on
GM's long CDS maturities and fits Altria's CDS poorly.

## Links

- [[merton-1976]] — jumps in the underlying; here the jump is a default, a drop all the
  way to zero, with a random arrival rate
- [[barbon-buraschi-2021-gamma-fragility]] — another source of skew and crash risk in
  option prices, from dealer hedging rather than default
- [[demirovic-guermat-tucker-2017-the-relationship-between-equity-and-bond-returns]] — how a firm's shares and its own bonds co-move as default risk rises
- [[merton-1974-on-the-pricing-of-corporate-debt]] — the original structural model linking a firm's equity, volatility and credit risk
