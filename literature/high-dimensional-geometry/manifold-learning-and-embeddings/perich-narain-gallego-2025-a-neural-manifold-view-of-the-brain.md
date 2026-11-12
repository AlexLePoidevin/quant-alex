# A Neural Manifold View of the Brain

| | |
|---|---|
| **Authors** | Matthew G. Perich (Université de Montréal, Mila), Devika Narain (Erasmus MC), Juan A. Gallego (Imperial College London) |
| **Year** | 2025 |
| **Type** | Review article — *Nature Neuroscience* 28(8):1582–1597 |
| **Link** | [doi.org/10.1038/s41593-025-02031-z](https://doi.org/10.1038/s41593-025-02031-z) |
| **PDF** | Not hosted in this repository (publisher copy, not open access) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22A+Neural+Manifold+View+of+the+Brain%22+Perich) for the title and authors |
| **BibTeX** | `perich2025neural` |
| **Status** | Reference — read in full |

## What it is

A review arguing that the low-dimensional structure seen in recordings of neural
populations is not just a convenient summary but a real object, a *neural manifold*: the
set of collective states a population of neurons can reach, given the constraints of its
wiring and of the behaviour it serves.

- **Definitions (Box 1).** The authors separate three meanings of "manifold" in the
  literature: the output of a dimensionality-reduction method, the geometric shape of
  population activity, and the low-dimensional dynamics during a task. They also separate
  three dimensions: intrinsic (the number of variables that parameterise the manifold),
  embedding (the number of linear directions needed to contain it) and ambient (the number
  of recorded neurons). A curved manifold of low intrinsic dimension can need many linear
  directions, so PCA overstates its dimension.
- **Estimating one (Box 2).** Each neuron is an axis; activity at each moment is a point;
  behaviour traces a path. Linear methods (PCA, factor analysis) fit a flat manifold.
  Nonlinear and manifold-learning methods (Isomap, LLE, diffusion maps, Laplacian
  eigenmaps, t-SNE, UMAP, LTSA, CEBRA, LFADS) can recover curved ones. On a Swiss roll with
  a hole, the methods give visibly different embeddings, and adding noise breaks several of
  them. Each recorded neuron is only one projection of the manifold, so too few neurons or
  too few behaviours can mislead any method.
- **The evidence.** Low-dimensional dynamics appear in worms, fish, mice, monkeys and
  humans, across sensory, cognitive and motor areas. The clearest cases have a known shape:
  a ring for head-direction cells in the thalamus, a torus for grid cells in entorhinal
  cortex (predicted by network models before it was measured), a line attractor for
  aggression in the hypothalamus, and hippocampal maps whose shape comes to match the
  enclosure. The ring and torus persist during sleep, when there is no behaviour. In a
  brain–computer-interface experiment, monkeys learned new mappings that stayed on the
  manifold far more easily than ones that required new activity patterns.
- **What shapes the manifold.** Intrinsic factors (connectivity, cell types, cortical
  layers, neuromodulators, glia) and extrinsic ones (the task). Simple lab tasks visit few
  states, which by itself lowers the measured dimension. Manifolds change over learning,
  development and evolution; the authors suggest a small skill reuses part of an existing
  manifold, while a very new one (a tonal language learned as an adult) needs a new one.
- **Proposals and open questions.** Use causal perturbations to validate, explore and
  alter a manifold, distinguishing pushes that stay on the manifold from ones that leave
  it. Is the manifold the right level of explanation? The authors argue yes, because many
  different low-level circuits produce the same population structure. Are manifolds of
  separate regions independent pieces, or one brain-wide object? Probably the latter,
  since regions drive each other. And which comes first, the manifold or the dynamics?
  Currently a manifold can only be estimated after the fact, from the paths it is meant to
  constrain.

## Why it's in the library

**It is the manifold hypothesis tested on data with a known answer.** The rest of this
section asks whether high-dimensional data lie near a low-dimensional manifold and how to
find it. Neuroscience has cases where the shape is known in advance (a ring for a
direction, a torus for a two-dimensional periodic position), so it is one of the few
fields where manifold-learning output can be checked against the truth.

**Its warnings carry over to any data set.** The intrinsic/embedding/ambient distinction
explains why PCA overestimates the dimension of curved data. The Swiss-roll comparison
shows that different manifold-learning methods give different answers on the same data,
and that noise breaks several of them. The authors also say plainly that running a
dimensionality-reduction method does not show that a manifold exists, and that what you
sample limits what you can recover: few conditions give a low-dimensional manifold whatever
the system.

**It links brains to network models.** Box 3 describes recurrent networks with low-rank
connectivity producing low-dimensional activity, the same object studied in deep networks
in [[cohen-chung-lee-sompolinsky-2020-separability-and-geometry-of-object-manifolds-in-deep-neural-networks]].

## Links

- [[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] — when the manifold
  hypothesis can be tested statistically at all
- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
  — data on several manifolds of different dimension, like the region- and
  behaviour-specific manifolds here
- [[levina-bickel-2004-maximum-likelihood-estimation-of-intrinsic-dimension]] — a
  classical estimator of the intrinsic dimension defined in Box 1
- [[coifman-lafon-2006]] — diffusion maps, one of the manifold-learning methods in Box 2
- [[cohen-chung-lee-sompolinsky-2020-separability-and-geometry-of-object-manifolds-in-deep-neural-networks]]
  — the geometry of object manifolds in artificial networks, from neuroscience-trained
  authors
- [[naitzat-zhitnikov-lim-2020-topology-of-deep-neural-networks]] — topology (Betti
  numbers) of data as it passes through a network, the topology/geometry distinction of
  Box 1
