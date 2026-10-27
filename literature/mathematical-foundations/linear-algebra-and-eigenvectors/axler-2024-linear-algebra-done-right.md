# Linear Algebra Done Right

| | |
|---|---|
| **Author** | Sheldon Axler (San Francisco State University) |
| **Year** | 2024 (fourth edition; this PDF is the author's revised printing of 16 August 2026) |
| **Type** | Textbook — Springer, Undergraduate Texts in Mathematics, 404pp. Open access, CC BY-NC 4.0 |
| **PDF** | `axler-2024-linear-algebra-done-right.pdf` (in this folder) |
| **BibTeX** | `axler2024linear` |
| **DOI** | [10.1007/978-3-031-41026-0](https://doi.org/10.1007/978-3-031-41026-0) |
| **Status** | Reference |

## What it is

A second course in linear algebra, written for students who can already compute with
matrices and now need the theory. It is known for one choice: **determinants come last.**
Eigenvalues are shown to exist from the minimal polynomial (chapter 5), not from the roots
of det(A − λI). Determinants appear only in chapter 9, defined through alternating
multilinear forms.

Nine chapters:

1. Vector spaces
2. Finite-dimensional vector spaces — span, independence, bases, dimension
3. Linear maps — null space and range, matrices, invertibility, quotients, duality
4. Polynomials — no linear algebra; can be covered quickly
5. Eigenvalues and eigenvectors — invariant subspaces, the minimal polynomial,
   upper-triangular and diagonalisable operators, commuting operators
6. Inner product spaces — orthonormal bases, Gram–Schmidt, orthogonal projection as
   **least squares**, the **pseudoinverse**
7. Operators on inner product spaces — self-adjoint and normal operators, the
   **spectral theorem**, positive operators, isometries and matrix factorisations, the
   **singular value decomposition** and what follows from it
8. Operators on complex vector spaces — generalised eigenvectors, Jordan form, trace
9. Multilinear algebra — bilinear and quadratic forms, determinants, tensor products

The author's preface flags 5E (commuting operators), the pseudoinverse part of 6C, and
duality (3F) as optional.

## Read with care

- **It is proof-based and abstract.** It works with operators on vector spaces, not
  matrices of numbers, and almost never computes. Pair it with code rather than reading it
  as a numerical-methods text: there is nothing on conditioning, floating point or
  algorithms.
- **No statistics.** Covariance matrices, PCA and estimation error are not in it. It
  supplies the theorems those rely on, not the applications.
- **Postponing determinants is a teaching choice,** not the standard order. Other texts
  find eigenvalues through determinants, so expect the two to look different side by side.

## Why it's in the library

**Chapters 6 and 7 are what the rest of the library uses without proving.** A covariance
matrix is a positive self-adjoint operator. The spectral theorem (7B) is why it has an
orthonormal basis of eigenvectors, which is all PCA is. The SVD (7E–7F) is the same
statement for any data matrix. Orthogonal projection (6C) is least squares, so it is every
linear regression and factor model. The pseudoinverse is the answer when the covariance
matrix is singular, which a sample covariance with more assets than observations always is.

**It supports the folder's existing note.** [[peraire-widnall-2008-inertia-tensor]] gives the
principal-axes picture of a symmetric matrix through a physical object. This book proves
the theorem behind that picture, in general.

**It gives the exact statements the random-matrix and shrinkage notes depend on.** What
[[marchenko-pastur-1967]] and [[ledoit-wolf-2004]] change is the *sample* eigenvalues. To see
what goes wrong, it helps to be exact about what an eigenvalue of a positive operator is and
what the spectral theorem promises.

**Suggested route for this library:** 6A–6C (inner products, projection, pseudoinverse),
then 7A–7C and 7E–7F (spectral theorem, positive operators, SVD). Go back to chapters 2–3
and 5 only where a proof calls on them.

## Links

- [[peraire-widnall-2008-inertia-tensor]] — the principal-axes intuition for a symmetric
  matrix, which chapter 7 proves in general
- [[markowitz-1952]] — the covariance matrix as a quadratic form (9A) and a positive
  operator (7C)
- [[meucci-2009]] — diversification measured in the eigenbasis of the covariance matrix
- [[marchenko-pastur-1967]], [[ledoit-wolf-2004]] — what happens to the spectrum when the
  matrix is estimated from a sample
- [[kernel-pca]] — PCA after a nonlinear feature map, the same spectral theorem in a larger
  inner-product space
- [[le-gall-2022-measure-theory-probability]] — conditional expectation as an orthogonal
  projection in L², chapter 6C in an infinite-dimensional space
