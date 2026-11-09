# Geometric Understanding of Deep Learning (2018 preprint)

| | |
|---|---|
| **Authors** | Na Lei, Zhongxuan Luo (Dalian University of Technology), Shing-Tung Yau, David Xianfeng Gu (Harvard) |
| **Year** | 2018 |
| **Type** | Preprint — arXiv:1805.10451 (v2, 31 May 2018), 22pp |
| **PDF** | `lei-et-al-2018-geometric-understanding-of-deep-learning.pdf` (in this folder; the arXiv copy) |
| **Link** | [arXiv:1805.10451](https://arxiv.org/abs/1805.10451) |
| **BibTeX** | `lei2018geometric` |
| **Status** | Reference — read in full |

## What it is

The first paper in the authors' geometric programme for deep learning. Its premise is that
deep learning works because natural high-dimensional data lie close to a low-dimensional
manifold. A network learns that manifold and the probability distribution on it.

- **Autoencoders as piecewise-linear charts.** A ReLU encoder cuts the input space into convex
  polyhedral cells and is affine on each one. The decoder rebuilds the data manifold as a
  polyhedral surface. On this view, denoising is projecting a noisy point onto the learned
  manifold. Projecting a noisy face onto a manifold learned from cat faces gives nonsense,
  which shows how specific to its data the learned manifold is.
- **Two complexity measures.**
  - The *rectified linear complexity of a network* is the most linear pieces it can produce,
    bounded by the product over layers of the number of cells each layer's hyperplanes can
    cut space into.
  - The *rectified linear complexity of an embedded manifold* is the fewest pieces any
    piecewise-linear encoder needs to flatten it without overlaps.
  - A network can encode a manifold only if its complexity is at least the manifold's.
- **For every fixed architecture there is a manifold it cannot encode.** The proof uses
  space-filling Peano-type curves, whose number of non-flattenable units grows as 4ⁿ⁺¹.
  Topology also limits what one encoder can do: if the latent image is simply connected, the
  manifold must be a topological disk, so an autoencoder learns either simple manifolds or one
  chart of a larger one.
- **Controlling the latent distribution with optimal transport.** Instead of a GAN-style
  contest, compute the Brenier potential (a solution to the Monge–Ampère equation) whose
  gradient carries a simple distribution onto the encoded data. Demonstrated by uniformly
  sampling a 3D surface through an area-preserving map.

## Why it's in the library

**It is the precursor of [[lei-et-al-2020-a-geometric-understanding-of-deep-learning]].**
This preprint sets out the manifold picture, the piecewise-linear capacity argument and the
optimal-transport idea. The 2020 journal paper develops the transport side into a full
generative model (AE–OT) and an explanation of mode collapse.

**The capacity argument is the geometric version of depth separation.** Counting linear
regions is the same lens as
[[eldan-shamir-2016-the-power-of-depth-for-feedforward-neural-networks]]. Here it is applied
to the data instead of the function: a manifold that is too folded, relative to the network,
cannot be flattened by it.

**Limits.** The bounds are worst-case counts, and the unencodable manifolds are constructed
(Peano curves), not found in real data. The experiments are illustrations on low-dimensional
surfaces (a Buddha mesh, a spiral, faces), with no benchmarks. The text reads as a working
draft.

## Links

- [[lei-et-al-2020-a-geometric-understanding-of-deep-learning]] — the published follow-up:
  optimal transport, mode collapse and the AE–OT model
- [[eldan-shamir-2016-the-power-of-depth-for-feedforward-neural-networks]] — depth and the
  number of linear pieces a network can represent
- [[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] — testing the
  hypothesis this paper takes as its starting point
- [[bengio-courville-vincent-2013-representation-learning-a-review-and-new-perspectives]] —
  autoencoders and manifold learning as representation learning
