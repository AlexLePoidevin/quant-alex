# Variance Swaps (Bloomberg OVML pricing documentation)

| | |
|---|---|
| **Authors** | Bloomberg L.P., Quantitative Analytics (no individual authors) |
| **Year** | 2018 (dated 1 February 2018) |
| **Type** | Vendor model documentation, 10pp. Describes how Bloomberg's OVML option pricer values variance swaps, mainly FX ones |
| **PDF** | Local copy only (Bloomberg internal documentation, no licence) |
| **BibTeX** | `bloomberg2018variance` |
| **Status** | Reference: §2 (replication with a control variate) and §3 (Greeks) are the useful parts; §5 is about the OVML screen |

## What it is

A short technical note on how a production pricer values a variance swap and its
sensitivities.

- **Payoff and accrual.** The swap pays notional × (annualized sum of squared daily log
  returns − strike²). Once fixing has started, total variance splits into the part already
  realized and the expected future part, weighted by the number of observations in each.
- **Pricing the future part by replication.** Expected future variance is the integral of
  out-of-the-money puts and calls weighted by 1/K², the same result as
  [[bossu-strasser-guichard-2005-just-what-you-need-to-know-about-variance-swaps]]. It
  assumes no jumps and deterministic rates.
- **A numerical detail worth copying.** Rather than integrate option prices directly, it
  integrates the *difference* between smile option prices and flat-volatility prices at the
  forward's ATM vol, and adds back the flat-vol variance analytically. That flat-vol swap
  acts as a control variate. The integral is taken in log-strike over ±10 standard
  deviations around the forward, with 200 trapezoid nodes on each side.
- **FX quirk.** If the swap's notional is in the foreign currency, price it on the inverted
  currency pair. The currency of the notional changes the deal, not just the units.
- **Greeks.** Delta and gamma are zero before the first fixing. After that they come only
  from the partly realized current day's return, so they are small. Vegas (ATM, risk
  reversal, strangle) are computed by bumping the surface and repricing; strangle vega is
  typically about twice ATM vega, because fair variance-swap volatility is roughly ATM plus
  twice the strangle.
- **Models.** The analytic "Black–Scholes" choice is really the smile replication above.
  The pricer also offers Monte Carlo under flat Black–Scholes or under a stochastic local
  volatility model calibrated to the surface. In a scale-invariant model like SLV, a
  sticky-moneyness delta in the domestic currency is exactly zero, since the payoff depends
  only on return ratios.

## Why it's in the library

**It shows how the textbook replication is implemented in practice.** The 1/K² formula is
simple on paper; the control-variate trick, the integration limits and the handling of the
FX notional currency are the details that make it stable and correct in a real pricer.

**It is vendor documentation, not research.** Most of §5 describes screen settings, and
nothing here is tested against market prices.

## Links

- [[bossu-strasser-guichard-2005-just-what-you-need-to-know-about-variance-swaps]] — the
  derivation of the replication this document implements
- [[merton-1976]] — jumps, which the replication here assumes away
- [[ambrus-capital-2022-is-the-vix-becoming-increasingly-leptokurtic]] — the VIX, computed
  from the same option strip for a 30-day horizon
