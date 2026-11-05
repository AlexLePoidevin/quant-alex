# From Local Volatility to Local Lévy Models

| | |
|---|---|
| **Authors** | Peter Carr, Hélyette Geman, Dilip B. Madan, Marc Yor |
| **Year** | 2004 (working paper dated 9 October 2004; published in *Quantitative Finance* 4(5), 2004) |
| **Type** | Paper, 17pp (working-paper version) |
| **PDF** | Local copy only (pre-publication draft, no open licence) |
| **BibTeX** | `carr2004locallevy` |
| **Status** | Reference: §2–3 give the recovery formula, §4 the closed-form double-exponential case, §6 the Fourier method for VG and CGMY |

## What it is

A generalisation of Dupire's local volatility model in which the driving noise is a
jump process instead of Brownian motion, with a recipe for recovering the model from
option prices.

- **Local volatility as Brownian motion at a variable speed.** Dupire (1994) and Derman and
  Kani (1994) let instantaneous volatility be a deterministic function of price and time,
  chosen so that the model reprices every quoted European option. Equivalently, log price
  is Brownian motion run at a speed equal to local variance. Locally, returns are still
  Gaussian, with no skew and no excess kurtosis.
- **The local Lévy model.** Replace the Brownian motion with a fixed Lévy process (such as
  variance gamma or CGMY) and run it at a "local speed" a(S, t), a deterministic function
  of price and time. The model is still one-dimensional and Markov, but local returns can
  be skewed and fat-tailed. A diffusion term can be kept alongside, though the main case
  is pure jump.
- **Recovering the speed from option prices.** In Dupire's formula local variance comes
  from the calendar spread divided by the butterfly. Here the calendar spread is replaced
  by its convolution with the "exponential double tail" of the Lévy measure. That double
  tail is the price of an instantaneous out-of-the-money option, and it spreads the
  calendar spread across jump sizes. Solving the convolution gives a(S, t).
- **Closed forms and numerics.** For a double-exponential (Kou-type) jump density, the
  convolution can be inverted analytically, because it is the resolvent of a Brownian
  motion with drift. The result is a direct analogue of the Dupire formula. An arithmetic
  (Bachelier) version is given for options on a martingale that can go negative. For VG
  and CGMY the convolution is solved with Fourier transforms.

## Why it's in the library

**It shows what local volatility is doing and how to relax it.** Local volatility gets the
whole surface right by loading everything onto one function. Here the Lévy process
supplies the short-dated skew and kurtosis, so the speed function has less to explain.
The authors expect more reasonable forward smiles as a result, but the paper does not test
that.

**It ties model calibration back to traded spreads.** In both local volatility and local
Lévy, the model is read off calendar spreads and butterflies. The jump version shows how
the spread has to be redistributed across jump sizes.

**This is a theory paper.** It contains no calibration to market data and no hedging or
pricing test, so it says nothing about whether local Lévy models price exotics better than
local volatility in practice.

## Links

- [[carr-et-al-2007-time-for-a-change-variance-gamma-model]] — the variance gamma process,
  one of the driving Lévy processes used here
- [[carr-et-al-2003-stochastic-volatility-for-levy-processes]] — the other route to a
  realistic term structure: a random clock instead of a deterministic local speed
- [[merton-1976]] — jumps added to a diffusion; local Lévy lets the jump intensity depend on
  price and time
- [[shreve-2004]] — the continuous-time background (Itô calculus, risk-neutral pricing) the
  paper assumes
