# Option Pricing using Integral Transforms

| | |
|---|---|
| **Authors** | Peter Carr (NYU Courant), presenting joint work with H. Géman, D. Madan, L. Wu and M. Yor |
| **Year** | 2003 (file dated March 2003; talk at an NYU Stern conference) |
| **Type** | Slides, 45pp, with a bibliography of 76 papers on transform methods in option pricing |
| **PDF** | Local copy only (lecture slides, no licence) |
| **BibTeX** | `carr2003transforms` |
| **Status** | Reference: the Carr–Madan FFT pages, the table of Lévy measures and characteristic exponents, and the time-change pages carry the content |

## What it is

A one-hour survey, as slides, of how Fourier transforms price European options on a single
asset. It runs from the definition of a Fourier transform to stochastic-volatility Lévy
models.

- **From payoffs to transforms.** A payoff can be decomposed into Arrow–Debreu claims
  (Breeden–Litzenberger), and each of those into sine and cosine claims. Pricing then
  becomes an inner product of the payoff with the risk-neutral density. Parseval's relation
  moves that inner product into Fourier space, where the density's transform is the
  characteristic function times a discount factor.
- **The Carr–Madan FFT formula.** Write the call price as a function of log-moneyness.
  - Its generalized Fourier transform is the characteristic function of the log price
    shifted by −i, scaled by the forward and the discount factor.
  - Inverting with the FFT gives prices at n strikes in O(n log n) rather than O(n²).
  - The transform exists only off the real line, because a call is not integrable.
  - Calibration can also be done directly in Fourier space.
- **Why Lévy processes.** They are specified directly by their characteristic function
  (Lévy–Khintchine): a drift, a diffusion and a Lévy measure for the arrival rate of jumps
  of each size. That makes closed-form pricing routine. The slides tabulate the Lévy
  measure and characteristic exponent for Black–Scholes, Merton, Kou, variance gamma, NIG,
  CGMY and finite-moment log-stable.
  - Every Lévy process is a limit of compound Poisson processes, including drift and
    diffusion.
  - The "convexity correction" that makes e^X a martingale is the characteristic exponent
    evaluated at −i.
- **Adding stochastic volatility by time change.** Lévy increments are independent, so
  volatility does not cluster. Running the process on a random business clock fixes this.
  - The characteristic function of the time-changed process is the Laplace transform of
    the clock, evaluated at the Lévy process's characteristic exponent.
  - If the clock is an integrated activity rate, that Laplace transform is a bond price
    in which the activity rate plays the interest rate. The affine and quadratic term-structure
    literature then supplies closed forms.
  - Correlation between clock and price (the leverage effect) is handled by Carr and Wu's
    change to a complex-valued measure.

## Why it's in the library

- **The toolkit behind most modern smile models.** Variance gamma, CGMY, Heston-type
  stochastic volatility and the time-changed Lévy models elsewhere in this section are all
  priced this way. The slides show in one place why those models share a pricing method.
- **The bond-pricing analogy.** Turning a stochastic-volatility pricing problem into a
  bond-pricing problem is what makes these models tractable. It is easy to miss in the
  papers, where it is assumed rather than explained.
- **A reading list.** The 76-paper bibliography covers transform methods up to 2003.
- **It is slides.** The arguments are sketched, sometimes informally ("engineering style
  proofs"). Use them for orientation and go to the papers for the details.

## Links

- [[merton-1976]] — the jump-diffusion whose characteristic function is the first non-trivial
  entry in the slides' table of Lévy models
- [[carr-et-al-2007-time-for-a-change-variance-gamma-model]] — the variance gamma model, one of the Lévy models priced this way
- [[carr-et-al-2003-stochastic-volatility-for-levy-processes]] — stochastic volatility for Lévy models by time change, in full
