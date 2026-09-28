# Measure Theory, Probability, and Stochastic Processes

| | |
|---|---|
| **Author** | Jean-François Le Gall (Université Paris-Saclay) |
| **Year** | 2022 |
| **Type** | Graduate text — Springer, Graduate Texts in Mathematics **295**, ~403pp |
| **PDF** | `le-gall-2022-measure-theory-probability.pdf` (in this folder), 409pp |
| **BibTeX** | `legall2022measure` |
| **DOI** | [10.1007/978-3-031-14205-5](https://doi.org/10.1007/978-3-031-14205-5) |
| **Status** | Reference |

## What it is

Fourteen chapters in three parts, which is the reason to want this one specifically: it
carries measure theory through to Brownian motion **in a single volume and a single
notation**, rather than assuming the measure theory and starting at martingales.

**Part I — Measure theory** (ch. 1–7)
Measurable spaces · integration of measurable functions · construction of measures
(outer measures, Lebesgue, a non-measurable set, Riesz–Markov–Kakutani) · Lᵖ spaces
(Hölder, completeness, Radon–Nikodym) · product measures and Fubini · signed measures and
Jordan decomposition · change of variables

**Part II — Probability theory** (ch. 8–11)
Foundations (probability spaces, random variables, expectation) · **independence**
(σ-fields, Borel–Cantelli, sums of independent variables) · **convergence of random
variables** · **conditioning**

**Part III — Stochastic processes** (ch. 12–14)
**Theory of martingales** · Markov chains · **Brownian motion** (construction, Wiener
measure, strong Markov property, harmonic functions and the Dirichlet problem)

Le Gall is a probabilist of the first rank — Wolf Prize 2019, and the author of the
standard modern work on Brownian motion and random trees. This is a text by someone who
does research in the subject it ends on.

## Why it's in the library

**Chapters 10–12 are the formal answer to the look-ahead problem.** Convergence of random
variables, conditioning, and martingale theory in that order is exactly the machinery that
makes "what did you know at time *t*" into an object rather than an intention. Conditional
expectation is the projection onto the σ-field of what is observable; a filtration is the
growing family of those σ-fields; a strategy is a process required to be predictable with
respect to it. A backtest that forms an `F_t` decision from `F_{t+h}`-measurable
information is not a strategy in this language — it is not even well-formed.

That is not an abstract concern here. The forward-label boundary leak recorded in this
research was **~83% of reported Sharpe on XLK**, and purge-and-embargo is a statement about
filtrations whether or not it was written that way. This book supplies the vocabulary that
names the bug before it is written.

**It closes the gap the other texts leave open.**
[[evans-rosenthal-2009-probability-and-statistics]] chapter 11 reaches martingales,
stopping times and Brownian motion, but at an undergraduate level and without the measure
theory underneath. [[shreve-2004]] starts *after* that measure theory and assumes it. Le
Gall is the volume that runs from σ-fields to the Dirichlet problem without a change of
book, which is why it is worth acquiring rather than assembling the same material from
three sources.

**Part I is also the general-purpose piece.** Lᵖ spaces, Radon–Nikodym and the duality
results are the ambient language for a great deal else — Radon–Nikodym derivatives are
change of measure, which is where any pricing argument eventually goes.

## Where it sits in the plan

Block III of the foundations roadmap (`substack_posts/foundations/ROADMAP.md`). The roadmap
records an argument that **chapters 10–12 want to be pulled forward to the end of Block I**
rather than waiting for Block III, because filtrations are load-bearing for backtest
methodology long before the rest of measure theory is needed. Chapters 1–7 can wait; ch. 11
and 12 cannot.

**Reading order for that pull-forward**, which is not the book's own order: §8.1 for the
probability-space definitions, then ch. 11 (conditioning) for conditional expectation as an
Lᵖ projection, then ch. 12 §§1–2 for filtrations, adapted and predictable processes, and
optional stopping. That is roughly sixty pages and it does not require Part I beyond the
definition of a σ-field — Radon–Nikodym (§4.4) is the one back-reference, since it is what
makes conditional expectation exist.

## Links

- [[evans-rosenthal-2009-probability-and-statistics]] — reaches the same endpoint without
  the measure theory; the bridge into this book
- [[shreve-2004]] — assumes this book's Part I and most of Part III
- [[wackerly-2008-mathematical-statistics]] — the applied inference counterpart, no overlap
