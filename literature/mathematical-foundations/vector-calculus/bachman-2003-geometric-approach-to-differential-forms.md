# A Geometric Approach to Differential Forms

| | |
|---|---|
| **Author** | David Bachman (California Polytechnic State University) |
| **Year** | 2003 |
| **Type** | Lecture notes — arXiv:math/0306194v1 [math.GT], June 2003, 106pp. Later expanded into a book (Birkhäuser, 2006; 2nd ed. 2012) |
| **Link** | [arxiv.org/abs/math/0306194](https://arxiv.org/abs/math/0306194) |
| **PDF** | `bachman-2003-geometric-approach-to-differential-forms.pdf` (in this folder; arXiv version) |
| **BibTeX** | `bachman2003forms` |
| **Status** | Reference — chapters 2–5 are the core; chapter 7 (manifolds, de Rham cohomology) is the graduate-level extension |

## What it is

Differential forms for a student who has finished multivariable calculus, taught by
picture. The opening claim is that a differential form is simply *an integrand*: the thing
you integrate over a curve, surface or higher-dimensional region.

1. **Introduction.** Why "dx" needs a meaning, and what goes wrong when the usual
   integral is generalised to curves and surfaces. Motivation only.
2. **Forms.** A 1-form as a linear function on vectors at a point; the wedge product of
   1-forms; n-forms as signed volumes of parallelepipeds (through the determinant).
3. **Differential forms and integration.** Forms that vary from point to point;
   orientation; integrating n-forms over parameterised regions, summarised as one recipe.
4. **Differentiation.** The exterior derivative d, defined geometrically and then
   computed algebraically; 0-forms are functions.
5. **Stokes' theorem.** Cells and chains, pull-backs, then ∫_∂C ω = ∫_C dω. Section 4
   shows that the gradient theorem, Green's theorem, Stokes' theorem and the divergence
   theorem are all this one statement.
6. **Applications.** Maxwell's equations in forms; foliations and contact structures.
7. **Manifolds.** Forms on manifolds, and de Rham cohomology: closed forms modulo exact
   ones, measuring the holes that stop a curl-free field from being a gradient.

Linear algebra is kept to determinants until the pull-back in chapter 5.

## Why it's in the library

It is the step up from [[schey-2005-div-grad-curl-and-all-that]]. Schey gives grad, div
and curl as three operators in R³ with three theorems; here they are one operator d in any
dimension with one theorem. That generality matters in the quantum-geometry notes: the
Berry connection in [[steinacker-2021-quantum-matrix-geometry-and-quasi-coherent-states]]
is a 1-form, its curvature ω is the 2-form dA, and the "would-be symplectic form" is a
closed 2-form. Those statements are written in this book's language, and the notion of a
form on a manifold in chapter 7 is what [[steinacker-2024-quantum-geometry-matrix-theory-and-gravity]]
assumes.

Chapter 7's de Rham cohomology is the precise version of Schey's "path independence holds
on simply connected regions".

## Links

- [[schey-2005-div-grad-curl-and-all-that]] — the R³ vector-calculus version, which
  chapter 5 §4 recovers as special cases
- [[steinacker-2021-quantum-matrix-geometry-and-quasi-coherent-states]] — connection
  1-form, curvature 2-form and symplectic form on the space of quasi-coherent states
- [[steinacker-2024-quantum-geometry-matrix-theory-and-gravity]] — the textbook that uses
  forms on manifolds throughout
- [[axler-2024-linear-algebra-done-right]] — alternating multilinear forms and the
  determinant (ch. 9), the algebra behind chapter 2
