# The Vanna-Volga Method for Implied Volatilities

| | |
|---|---|
| **Authors** | Antonio Castagna, Fabio Mercurio |
| **Year** | 2007 (*Risk*, January 2007, pp. 106–111) |
| **Type** | Journal article (practitioner), 6pp. A longer preprint, "The Vanna-Volga method for implied volatilities: tractability and robustness", has the same content |
| **PDF** | Local copy only (Risk.net reprint, publisher copyright) |
| **BibTeX** | `castagna2007vanna` |
| **Status** | Reference: §2–4 (the replication argument, the weights, the price formula) and the two approximations for the implied volatility carry the paper |

## What it is

The standard reference for vanna-volga (VV), the rule FX option desks use to turn the
three quoted volatilities for an expiry into a whole smile, and to put a smile-consistent
price on a vanilla at any strike.

- **The market it starts from.** For each expiry an FX market quotes three numbers: the
  at-the-money (delta-neutral straddle) volatility, the 25-delta risk reversal and the
  25-delta butterfly. These pin down three strikes K₁ < K₂ < K₃ (25-delta put, ATM,
  25-delta call) with volatilities σ₁, σ₂, σ₃. Every other strike has to be filled in.
- **The replication argument.** Assume the Black–Scholes (Garman–Kohlhagen) smile is flat
  but its level moves randomly. A call at any strike K can then be hedged locally with the
  underlying plus amounts x₁, x₂, x₃ of the three quoted options, chosen so the portfolio
  matches the call's vega, vanna (vega's sensitivity to spot) and volga (vega's
  sensitivity to volatility). The paper gives these weights in closed form; they depend
  only on the vegas and on log-ratios of the strikes, and the system always has a unique
  solution.
- **The price.** Price the call at K with Black–Scholes at the ATM volatility, then add
  what the hedge really costs at market prices instead of flat-volatility prices:
  C(K) = C_BS(K) + x₁(K)·[market − BS price at K₁] + x₃(K)·[market − BS price at K₃].
  The ATM term drops out because the flat volatility is the ATM one. At the three quoted
  strikes the formula returns the market price exactly.
- **Properties.** The price has the right limits as K goes to zero or infinity and is
  convex in K for typical market inputs, so it is arbitrage-free in practice, but the
  authors note convexity can fail for some parameters. Two consistency results: starting
  from any three other strikes priced by the VV curve gives back the same curve; and
  extending the method to any European payoff gives the same price as integrating that
  payoff against the density implied by the VV call prices (Carr–Madan static
  replication), so a payoff can be priced from the three basic options alone.
- **Approximations.** A first-order expansion makes the implied volatility a weighted sum
  of σ₁, σ₂, σ₃ that is quadratic in log-strike: very accurate between the 25-delta
  strikes but too high in the wings, where it breaks Lee's (2004) moment bound. A
  second-order approximation is accurate in the wings too, but involves a square root
  that can occasionally be undefined.
- **The example.** EUR/USD 3-month data from 1 July 2005: σ₁ = 9.79%, σ₂ = 9.375%,
  σ₃ = 9.29%. The VV curve and a calibrated SABR curve nearly overlap between the
  10-delta strikes and match the 10-delta broker quotes (10.46% put, 9.49% call), while
  Malz's quadratic-in-delta interpolation does not.

## Why it's in the library

**It explains how FX volatility is actually quoted and filled in.** An FX smile is not
observed strike by strike: three quotes per expiry are all there is, and every desk turns
them into a curve with VV or something calibrated to agree with it. Any analysis of FX
option prices across strikes is reading the output of this interpolation.

**The method is a hedge, not just a curve fit.** The price is the Black–Scholes value
plus the cost of neutralising vega, vanna and volga with the three liquid options. That
makes the smile's two shape quotes interpretable: the risk reversal prices vanna (skew)
and the butterfly prices volga (convexity in volatility).

**It says where the method stops.** The replication assumes no jumps and an inconsistent
"flat but stochastic" smile, and it says nothing rigorous about path-dependent options.
For barriers and touches desks reweight the VV correction by survival probabilities, a
rule the authors call harder to justify, and which can even get the sign wrong when the
smile is steep. That gap is what stochastic-volatility and exotic-option methods
elsewhere in this section address.

## Links

- [[garrivier-2020-fx-vanilla-pricing-and-smile-calibration]] — the FX delta conventions
  and market-strangle quotes the three VV inputs come from, and two other ways to build
  the same smile slice (delta interpolation and SVI)
- [[lipton-sepp-2022-hybrid-method-for-pricing-barrier-options-with-stochastic-volatility]]
  — pricing barriers under a full stochastic-volatility model, the problem VV's
  survival-probability adjustment only approximates
- [[merton-1976]] — jumps, which the VV replication argument assumes away
