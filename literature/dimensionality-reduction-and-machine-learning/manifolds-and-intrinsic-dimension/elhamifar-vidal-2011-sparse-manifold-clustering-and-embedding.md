# Sparse Manifold Clustering and Embedding

| | |
|---|---|
| **Authors** | Ehsan Elhamifar, René Vidal (Center for Imaging Science, Johns Hopkins University) |
| **Year** | 2011 |
| **Type** | Conference paper — *Advances in Neural Information Processing Systems 24* (NIPS 2011) |
| **PDF** | `elhamifar-vidal-2011-sparse-manifold-clustering-and-embedding.pdf` (in this folder; the open-access proceedings version) |
| **BibTeX** | `elhamifar2011sparse` |
| **Status** | Reference — §2 (the sparse neighbour program and the dimension read-out) is the core |

## What it is

Methods like LLE, Laplacian eigenmaps and Isomap start by joining each point to a fixed
number of nearest neighbours. Pick too few and the local shape is lost; pick too many and
the neighbourhood spills across curvature or onto a nearby manifold. **SMCE (Sparse
Manifold Clustering and Embedding) lets each point choose its own neighbours**, and the
same choice serves for clustering, embedding and dimension estimation.

- **The idea.** Near a point on a d-dimensional manifold, d+1 neighbours from the same
  manifold span a flat patch passing close to it (roughly the tangent space). Neighbours
  from a different manifold do not. So look for the *fewest* nearby points whose affine
  span passes close to the point.
- **The program.** For each point, normalise the directions to all other points and solve
  a Lasso-like problem with an affine constraint: minimise
  λ‖Q c‖₁ + ½‖X c‖² subject to the weights summing to one. Q penalises distant points, so
  the solution picks a few close neighbours on the same manifold. The result does not
  change if the data are rotated, shifted or rescaled.
- **Clustering and embedding.** The sparse weights form a similarity graph that ideally
  splits into one connected piece per manifold. Spectral clustering separates the
  pieces, and the eigenvectors of each piece's graph Laplacian give its low-dimensional
  embedding, with no second neighbour search.
- **Dimension for free.** A point on a d-dimensional manifold should get d+1 non-zero
  weights. Sorting each point's weights and taking the median across a cluster gives a
  vector whose number of large entries is roughly the dimension plus one, so each
  cluster gets its own dimension estimate.
- **Results.** Two trefoil knots in R¹⁰⁰, close enough that 9% of points have another
  knot's point among their 3 nearest neighbours: LLE and Laplacian eigenmaps misclassify
  9.5–38.5% for every neighbour count tried; SMCE gets 0% for λ from 10 to 200. Two
  subjects' faces under changing light (Extended Yale B): 2.34% error (3 of 128 images),
  with a 2-dimensional estimate matching the light source's two degrees of freedom. Also
  shown: a punctured sphere, Frey faces and five MNIST digits.

## Read with care

- **One parameter, but still a parameter.** Results are stable for λ from 1 to 200 in the
  examples, but break at λ = 0.1. Each point is also only allowed to choose among its
  N/10 nearest neighbours, which is a hidden neighbourhood size.
- **The key assumption can fail.** It needs each manifold to be locally close to flat at
  the sampling density. Sparse samples, heavy noise or sharp curvature break it, and the
  paper gives no guarantee that each manifold forms one connected piece of the graph.
- **The dimension read-out is informal.** "Number of relatively large entries" is judged
  by eye; there is no threshold or error bar.
- **Cost.** One convex problem per point makes it slower than nearest-neighbour graphs on
  large data sets.
- **Small, clean experiments.** Two or five clusters, at most about 2,000 points, all
  images or synthetic shapes. No finance data.

## Why it's in the library

**It is the algorithm behind the union of manifolds picture.**
[[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
used class labels to stand in for separate manifolds. SMCE finds the separate pieces and
their dimensions without labels, which is what unlabelled data such as returns would need.

**Regimes as separate manifolds.** If calm and stressed markets occupy different
low-dimensional pieces, a fixed nearest-neighbour graph will blur them where they come
close. SMCE's test (do the neighbours span a flat patch through the point?) is a
principled way to keep them apart, and its per-cluster dimension says how many factors
drive each piece.

**A neighbourhood-size check.** Any method built on a k-nearest-neighbour graph
([[coifman-lafon-2006]], the local estimators in [[levina-bickel-2004]] and
[[facco-et-al-2017]]) depends on k. Comparing against SMCE's self-chosen neighbourhoods
shows whether a chosen k is mixing pieces that should stay separate.

## Links

- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
  — the evidence that data are several manifolds of different dimension, which SMCE
  clusters and measures
- [[levina-bickel-2004]] — a nearest-neighbour dimension estimator; SMCE gives a
  per-cluster estimate without fixing k
- [[facco-et-al-2017]] — two-NN, the minimal-neighbourhood dimension estimator
- [[coifman-lafon-2006]] — diffusion maps, the spectral embedding on a fixed kernel graph
  that SMCE replaces with a sparse, self-chosen graph
- [[koulakis-seibold-2026-the-data-manifold-under-the-microscope]] — controlled image
  manifolds of known dimension, on which methods like this can be checked
