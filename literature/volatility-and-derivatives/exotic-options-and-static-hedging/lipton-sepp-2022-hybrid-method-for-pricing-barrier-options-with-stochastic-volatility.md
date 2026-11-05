# Toward an Efficient Hybrid Method for Pricing Barrier Options on Assets with Stochastic Volatility

| | |
|---|---|
| **Authors** | Alexander Lipton (Abu Dhabi Investment Authority), Artur Sepp (Sygnum Bank) |
| **Year** | 2022 |
| **Type** | Paper, 32pp. arXiv 2202.07849 (q-fin.CP), CC BY 4.0 |
| **PDF** | `lipton-sepp-2022-hybrid-method-for-pricing-barrier-options-with-stochastic-volatility.pdf` |
| **BibTeX** | `lipton2022hybrid` |
| **Status** | Reference: §2.3 (conditional Willard formula), §3–4 (the barrier formula and the two loops) and §6 (conclusions); §5 is a mathematical aside |

## What it is

A numerical method for a classic hard problem: the price of a barrier option (one that
knocks out if the price touches a level) when volatility is itself random.

- **The difficulty.** Under a stochastic-volatility model such as Heston, a barrier price
  solves a PDE in time, price and variance. Two-dimensional Monte Carlo and finite
  differences both work but are slow. The only known closed form (Lipton 1997, the method
  of images) needs zero rates and zero spot–volatility correlation.
- **The idea: condition on the volatility path.** Split the price shock into a part
  correlated with variance and an independent part. Given one variance path, the
  log-price is a Brownian motion with a deterministic, time-dependent drift and variance.
  For vanilla options this conditional price is just Black–Scholes, averaged over variance
  paths (Willard's 1997 formula). The paper extends the same conditioning to barrier
  options.
- **Two loops.** The outer loop simulates variance paths by Monte Carlo. The inner loop
  solves, for each path, a one-dimensional barrier problem with time-dependent
  coefficients. The authors solve that inner problem two ways: Crank–Nicolson finite
  differences, and the method of heat potentials, which reduces it to a linear Volterra
  integral equation of the second kind.
- **Results.** In a Heston example (S₀ = 1, V₀ = 0.25, T = 1, r = 3%, log-barrier −0.5)
  the two inner methods agree to within 10⁻³ (Green's function, no-touch prices) and
  10⁻⁴ (barrier calls), and match a 100,000-path plain Monte Carlo using 10,000 outer
  paths. The heat-potential version is "an order of magnitude faster" than other hybrid
  methods at the same or better accuracy; the abstract says orders of magnitude faster
  than existing methods.
- **A by-product.** A new expression for the joint density of a Brownian motion with
  time-dependent drift and its running minimum, a problem the authors say earlier
  published attempts got wrong.
- **Scope.** The method works for any one-factor stochastic-volatility model (the authors
  prefer Stein–Stein to Heston for ease of simulation) and, they say, can be extended to
  rough volatility and double-no-touch options in later work.

## Why it's in the library

**It shows the standard trick for path-dependent options under stochastic volatility.**
Conditioning on the volatility path turns a two-factor problem into an average of
one-factor problems with known structure. The same idea underlies mixing (Hull–White,
Romano–Touzi) approaches to vanillas, and here it is pushed to barriers.

**Barriers are where smile models disagree.** Vanilla prices only pin down each expiry's
distribution; barrier and touch prices depend on the path, so different models fitted to
the same smile price them differently. A fast, accurate barrier pricer is what makes it
practical to compare models on those products rather than on vanillas.

**It is a methods paper, not an empirical one.** Timings are reported qualitatively, the
test case is one parameter set, and there is no calibration to market data. Its value is
the decomposition and the numerical technique.

## Links

- [[carr-ellis-gupta-1998-static-hedging-of-exotic-options]] — the opposite approach to
  barriers: replicate them with vanilla options instead of solving a model
- [[castagna-mercurio-2007-the-vanna-volga-method-for-implied-volatilities]] — the FX
  desk's model-free smile rule, whose extension to barriers is only heuristic
- [[merton-1976]] — jump-diffusion, the other main family of models for the smile
- [[carr-itkin-muravey-2022-barrier-options-in-the-time-dependent-heston-model]] — a semi-analytical alternative in time-dependent Heston
