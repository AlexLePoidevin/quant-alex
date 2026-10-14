# Introduction about Copulas (seminar slides)

| | |
|---|---|
| **Author** | Duc T. Nguyen (Ulm University) |
| **Year** | 2020 (29 November) |
| **Type** | Seminar talk 1, Beamer slides, 37pp |
| **Based on** | Nelsen (2006), *An Introduction to Copulas*; Hofert, Kojadinovic, Mächler & Yan (2018), *Elements of Copula Modeling with R* |
| **PDF** | `nguyen-2020-introduction-to-copulas-slides.pdf` (in this folder) |
| **BibTeX** | `nguyen2020copulaslides` |
| **Status** | Explainer — cite [[nelsen-2006-introduction-to-copulas]] instead |

## What it is

A short walk through Nelsen chapter 2 in four parts:

1. **Motivating example.** Two samples of 1000 points look different: one has normal
   margins, the other exponential. After the probability-integral transform F(X) ~ U(0,1)
   their scatter plots are indistinguishable. The dependence is the same and only the
   margins differ.
2. **The analytic route to copulas.** H-volume, 2-increasing and grounded functions,
   subcopulas, the Lipschitz bound, and the Fréchet–Hoeffding bounds
   max(u+v−1, 0) ≤ C(u,v) ≤ min(u,v). The Frank copula is the worked example.
3. **Copulas and random variables.** Sklar's theorem stated and used, and the
   Fréchet–Hoeffding bounds W, Π and M read as countermonotone, independent and comonotone.
4. **Survival and symmetric copulas.**

## Why it's in the library

**The motivating example is the whole idea in one picture.** Transforming each margin to
uniform removes everything except the dependence. That is the operation behind the
empirical copula in [[munnix-schafer-2011-copula-dependencies]], and behind any
rank-based measure of co-movement.

**It is a quick way into Nelsen chapter 2.** Read the slides first for the definitions and
the order of the argument, then the book for the proofs, the exercises and chapter 5 on
dependence. The slides stop before tail dependence, which is the part that matters most for
returns. The material in the slides is all in Nelsen, so cite the book.

## Links

- [[finance-tutoring-2024-sklar-theorem]] — the plain-language version, to read first
- [[nelsen-2006-introduction-to-copulas]] — the source; chapter 2 in full, chapter 5 for
  tail dependence
- [[munnix-schafer-2011-copula-dependencies]] — the transform-to-uniform step applied to
  S&P 500 returns
