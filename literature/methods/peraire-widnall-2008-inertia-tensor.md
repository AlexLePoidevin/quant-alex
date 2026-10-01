# 3D Rigid Body Dynamics: The Inertia Tensor

| | |
|---|---|
| **Authors** | Jaime Peraire, Sheila Widnall (MIT, Department of Aeronautics and Astronautics) |
| **Year** | 2008 |
| **Type** | Lecture note — MIT 16.07 *Dynamics*, Lecture L26, version 2.1, 13pp |
| **PDF** | `peraire-widnall-2008-inertia-tensor.pdf` (in this folder) |
| **BibTeX** | `peraire2008inertia` |
| **Status** | Reference — borrowed from mechanics, not finance |

## What it is

The derivation of the inertia tensor from the angular momentum of a rigid body. Starting
from `H_G = Σ mᵢ (r′ᵢ × (ω × r′ᵢ))`, the lecture shows that angular momentum is not
parallel to the angular velocity in general, that the constant of proportionality is a
tensor rather than a scalar, and that this tensor is symmetric and positive semi-definite.
It then covers the parallel axis theorem, the rotation of the tensor under a change of
basis, and the principal axes obtained by diagonalising it.

## Why it's in the library

**Because it is the same mathematics as a covariance matrix, derived by people who had to
make it physical.** A mass distribution and a probability distribution are both measures;
the moment of inertia about an axis and the variance along a direction are both second
moments of a measure about its centre. The correspondence is exact and worth having
explicitly:

| mechanics | statistics |
|---|---|
| centre of mass | mean |
| moment of inertia about an axis | variance along a direction |
| product of inertia | covariance |
| parallel axis theorem | the variance decomposition, `E[(X−a)²] = Var(X) + (μ−a)²` |
| principal axes of inertia | principal components |
| a body spins freely about a principal axis | uncorrelated coordinates in the eigenbasis |

**One detail in the correspondence is worth getting right, because it inverts.** The
inertia tensor is not the second-moment matrix `S = Σ m x xᵀ` but `I = tr(S)·Id − S`. The
two share eigenvectors, so the principal axes of inertia and the principal components of
the mass distribution coincide — but the eigenvalues map as `λ_I = tr(S) − λ_S`, which
reverses the ordering. The axis of **minimum** moment of inertia is the direction of
**maximum** spread. A pencil spins most easily about its length, which is exactly the
direction along which its mass is most dispersed. Anyone importing the physical intuition
into a covariance setting needs that sign, or they will read the principal component
backwards.

**It is also the honest source of an analogy worth using carefully.** Describing a
portfolio's risk as having a "centre of gravity" and "principal axes" is standard
rhetorical furniture; this lecture is where the furniture actually comes from, and reading
it shows where the analogy stops. Mass is non-negative and conserved, so an inertia tensor
is always estimable to arbitrary precision from a known body. A covariance matrix is
estimated from a finite sample of a distribution that may not be stationary, which is the
entire difficulty — see [[marchenko-pastur-1967]] and [[ledoit-wolf-2004]]. The mechanics
has the geometry without the estimation problem.

## Links

- [[markowitz-1952]] — the covariance matrix as the object whose geometry this mirrors
- [[meucci-2009]] — diversification measured in the eigenbasis, the principal-axes idea
  applied to a portfolio
- [[marchenko-pastur-1967]], [[ledoit-wolf-2004]] — what breaks when the tensor must be
  estimated from a sample rather than measured from a body
- [[wackerly-2008-mathematical-statistics]] — moments of a distribution, defined without
  the mechanical analogy
