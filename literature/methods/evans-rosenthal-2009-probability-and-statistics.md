# Probability and Statistics: The Science of Uncertainty

| | |
|---|---|
| **Authors** | Michael J. Evans, Jeffrey S. Rosenthal (University of Toronto) |
| **Year** | 2009 |
| **Type** | Undergraduate/early-graduate textbook — W. H. Freeman, 2nd edition, 774pp |
| **Origin** | The Toronto probability-and-statistics sequence; released free by the authors |
| **PDF** | `evans-rosenthal-2009-probability-and-statistics.pdf` (in this folder) |
| **BibTeX** | `evansrosenthal2009prob` |
| **Status** | Reference |

## What it is

Eleven chapters, probability-first and noticeably more measure-theory-adjacent than the
standard applied text:

1–3. Probability models; random variables and distributions; expectation
4. **Sampling distributions and limits**
5–6. Statistical inference; likelihood inference
7. Bayesian inference
8. Optimal inferences
9. Model checking
10. Relationships among variables
11. **Stochastic processes** — random walk, Markov chains, MCMC, martingales, Brownian motion

Most chapters close with a **"Further Proofs (Advanced)"** section, which is the book's
distinguishing habit: the main text states a result and uses it, and the proof is available
without interrupting the argument. Rosenthal is a probabilist — *A First Look at Rigorous
Probability Theory* is his — and the book is written by someone who knows exactly which
steps are being waved through and says so.

## Why it's in the library

**Chapter 4 is the cleanest short treatment of the convergence modes.** §4.2 does
convergence in probability and the weak law, §4.3 convergence with probability 1 and the
strong law, §4.4 convergence in distribution and the central limit theorem. Having the
three laid out in that order, in one chapter, is what makes the CLT legible: the laws of
large numbers say the sample mean collapses onto μ, and the CLT is the separate statement
that if you magnify that collapse at rate √n a non-degenerate limit appears. Conflating the
two is the most common error in applied work, and this chapter is the reason not to.

**§4.4.2 is titled "The Central Limit Theorem and Assessing Error."** That is the whole
justification for quoting a standard error on anything estimated from a sample — which in
this research means every Sharpe ratio. `SE(SR) ≈ √((1 + SR²/2)/T)` is a sampling
distribution and nothing more; the discipline of writing the ± before deciding whether a
backtest is good rests on this section.

**§4.6 supplies the normal-theory distributions.** Chi-squared, t and F are derived as
functions of normal samples rather than asserted, which is what makes degrees of freedom an
object rather than a convention.

**Chapter 11 is the reason to keep this one alongside the others.** Random walk, Markov
chains and their limit theorem, Metropolis–Hastings and Gibbs, martingales and stopping
times, and Brownian motion built as a limit of "faster and faster random walks." That last
construction is the functional version of the same √n rescaling that drives the CLT, and it
is the bridge to continuous-time finance — the discrete-to-continuous step that
[[shreve-2004]] assumes you have already seen. The martingale and stopping-time material is
also the honest framing for why a strategy stopped at a favourable moment is not evidence
of anything.

**Chapter 7 gives Bayesian inference a full chapter rather than an appendix**, which is the
formal statement of what every shrinkage estimator is doing — see [[ledoit-wolf-2004]].

## How it differs from the other statistics text here

[[wackerly-2008-mathematical-statistics]] and this one overlap on the core sequence and
then diverge, which is why both are kept.

- **Wackerly** is the applied inference toolkit: more estimation methods, hypothesis-testing
  practice, ANOVA, experimental design, categorical data and nonparametrics. Deeper on
  *procedures*.
- **Evans & Rosenthal** is probability-first: modes of convergence treated separately and
  carefully, optimal inference and model checking as their own chapters, proofs available,
  and a stochastic-processes chapter Wackerly has no equivalent of. Deeper on *foundations*.

Read Evans & Rosenthal chapter 4 for why an estimator has a distribution at all; read
Wackerly chapters 8–10 for what to do with it.

## Links

- [[wackerly-2008-mathematical-statistics]] — the applied counterpart; overlapping core,
  different emphasis
- [[chopra-ziemba-1993]] — estimation error in optimiser inputs, the applied payoff of
  treating estimators as random variables
- [[ledoit-wolf-2004]] — shrinkage as the Bayesian posterior of chapter 7, used as a
  covariance estimator
- [[harvey-liu-zhu-2016]] — what multiple testing does to the inference of chapters 5–6
- [[shreve-2004]] — continuous-time finance, which begins where chapter 11's Brownian
  motion construction ends
- [[marchenko-pastur-1967]] — the limiting spectral distribution, chapter 4's logic applied
  to an entire covariance matrix
