# Div, Grad, Curl, and All That: An Informal Text on Vector Calculus

| | |
|---|---|
| **Author** | H. M. Schey |
| **Year** | 2005 |
| **Type** | Undergraduate textbook — W. W. Norton & Company, 4th edition, 163pp |
| **Origin** | A short companion to a first course in vector calculus or electromagnetism, built around electrostatics |
| **PDF** | `schey-2005-div-grad-curl-and-all-that.pdf` (in this folder; scanned, no text layer) |
| **BibTeX** | `schey2005divgradcurl` |
| **Status** | Reference — read straight through; the problems at the end of each chapter are the point |

## What it is

Vector calculus taught through one physical question: given the charges, what is the
electric field? Each operator is introduced at the moment the question needs it, so its
meaning comes before its formula.

1. **Vector functions and electrostatics.** Fields as functions from points to vectors,
   and Coulomb's law as the motivating example.
2. **Surface integrals and the divergence.** Unit normals, surface integrals and flux;
   Gauss' law; the divergence as flux per unit volume in the limit; the del notation; the
   **divergence theorem**.
3. **Line integrals and the curl.** Work and line integrals; path independence; the curl
   as circulation per unit area in the limit, and what it means geometrically; **Stokes'
   theorem**; simply connected regions; path independence ⇔ zero curl.
4. **The gradient.** Line integrals of a gradient; finding the field from a potential;
   **Laplace's equation**; directional derivatives; the gradient as the direction of
   steepest ascent, normal to level surfaces.

Cylindrical and spherical forms of each operator are derived, and worked solutions to
selected problems are at the back.

It is informal on purpose: limits are handled by picture and argument, not by ε–δ, and
everything lives in R³. Differential forms are the step up in generality: see
[[bachman-2003-geometric-approach-to-differential-forms]].

## Why it's in the library

**The gradient is the object every optimiser follows.** Chapter 4's "steepest ascent,
orthogonal to level sets" is the picture behind gradient descent, the Lagrange condition
(the gradient of the objective is parallel to the gradient of the constraint on the
efficient frontier) and backpropagation.

**Divergence and the Laplacian are how densities move.** The divergence theorem is the
conservation law under the Fokker–Planck equation for a diffusion's density, and the
Laplacian of chapter 4 is the generator of Brownian motion that appears in Itô's formula
in [[shreve-2004]]. The graph and matrix Laplacians in [[coifman-lafon-2006]] and the
QCML papers are discrete versions of the same operator.

**Curl and Stokes' theorem are the template for curvature.** Path independence fails
exactly when the curl is non-zero, and Stokes' theorem turns a loop integral into a flux
of curl. The Berry connection and its curvature in
[[steinacker-2021-quantum-matrix-geometry-and-quasi-coherent-states]] are this idea with
complex phases in place of work.

## Links

- [[shreve-2004]] — the Laplacian and gradient used inside Itô's formula and the
  Feynman–Kac / heat-equation link
- [[coifman-lafon-2006]] — the Laplacian rebuilt from data as a diffusion operator
- [[steinacker-2021-quantum-matrix-geometry-and-quasi-coherent-states]] — connection and
  curvature on the space of quasi-coherent states, Stokes' theorem in a quantum setting
- [[axler-2024-linear-algebra-done-right]] — the linear algebra the operators act through
- [[nemirovski-2023-linear-optimization]] — the optimisation side, where gradients and
  normals to constraint surfaces become duality
- [[bachman-2003-geometric-approach-to-differential-forms]] — grad, div and curl unified as
  the exterior derivative, and the three theorems as one Stokes' theorem
