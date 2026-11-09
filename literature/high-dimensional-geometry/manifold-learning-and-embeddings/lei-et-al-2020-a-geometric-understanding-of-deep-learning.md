# A Geometric Understanding of Deep Learning

| | |
|---|---|
| **Authors** | Na Lei, Dongsheng An, Yang Guo, Kehua Su, Shixia Liu, Zhongxuan Luo, Shing-Tung Yau, Xianfeng Gu (Dalian, Stony Brook, Wuhan, Tsinghua, Harvard CMSA) |
| **Year** | 2020 (online January 2020) |
| **Type** | Paper — *Engineering* 6(3), 361–374 (2020), doi:10.1016/j.eng.2019.09.010. It builds on the authors' 2018 preprint [[lei-et-al-2018-geometric-understanding-of-deep-learning]] (similar title, different content) and arXiv:1809.05964 (latent-space OT) |
| **PDF** | `lei-et-al-2020-a-geometric-understanding-of-deep-learning.pdf` (in this folder; the published version, open access under CC BY-NC-ND 4.0) |
| **Link** | [Engineering (open access)](https://doi.org/10.1016/j.eng.2019.09.010) |
| **BibTeX** | `lei2020geometric` |
| **Status** | Reference — read in full |

## What it is

An optimal-transport (OT) reading of generative adversarial networks, built on the
**manifold distribution hypothesis**: a class of natural data concentrates near a
low-dimensional manifold in the high-dimensional input space. On this view a generator does
two separate jobs:
- **Manifold learning:** a decoding map from a latent space onto the data manifold.
- **Distribution transformation:** moving simple noise (Gaussian or uniform) to the right
  distribution on that manifold. This second job is exactly an OT problem.

Three claims follow from classical OT theory (Brenier, Monge–Ampère regularity):
- **Generator and discriminator should cooperate, not compete.** With squared-distance cost,
  the generator's optimal map is the gradient of a convex (Brenier) potential, and the
  discriminator's Kantorovich potential is a closed-form function of it. Once one is
  optimal, the other follows without training.
- **Mode collapse is structural.** When the target distribution has several separate pieces,
  or a non-convex support, the optimal transport map is discontinuous on a "singularity
  set". ReLU networks can only represent continuous maps, so training either fails to
  converge, locks onto one piece (mode collapse), or covers all pieces but also generates
  points in the gaps between them (unrealistic samples).
- **The OT step can be solved exactly.** In the semi-discrete case it is a convex
  optimisation with an explicit Hessian, solved by (quasi-)Newton steps on a GPU, with one
  unknown per training sample and discontinuities detected from the geometry of the solution.

From this they build the **AE–OT model**: an autoencoder learns the manifold, then an
explicit OT map in the latent space carries uniform noise onto the encoded data. The
experiments cover MNIST, Fashion-MNIST, CIFAR-10 and CelebA:
- **2D grid test:** AE–OT recovers all modes, where GAN and PacGAN do not.
- **Visible singularity:** interpolating across a singularity on CelebA gives a face with
  one blue eye and one brown, which the authors read as evidence that the encoded data's
  support is non-convex.
- **Benchmarks:** FID and precision–recall scores competitive with or better than the GANs
  benchmarked by Lucic et al. and non-adversarial models such as GLANN.

## Why it's in the library

**It is a concrete use of the manifold hypothesis.** It turns "data lie near a
low-dimensional manifold" ([[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]])
into a specific prediction about where generative models fail. It reaches the same
conclusion as
[[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]],
from the transport side: a continuous network cannot cleanly map one connected noise
distribution onto data made of separate pieces.

**The decomposition is reusable.** Splitting "learn the shape" from "move the mass" keeps
the hard non-convex part (the autoencoder) apart from a part with guarantees (the convex
OT step). The same split appears in latent-variable and energy-based models
([[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]]).

**Limits.** The OT guarantees cover only the latent-space transport. The autoencoder,
which carries the manifold learning, has no guarantees, and the authors leave that "half of
the black box" to future work. The experiments use small autoencoders on downsampled
CIFAR-10 (25,000 images) and CelebA (10,000 images). The CelebA FID beats the other models
only after two convolutional layers were added. The singularity-detection threshold is set
by hand per dataset (0.68–0.75).

## Links

- [[brown-et-al-2022-the-union-of-manifolds-hypothesis-and-its-implications-for-deep-generative-modelling]]
  — the same disconnected-support argument for why generative models struggle
- [[fefferman-mitter-narayanan-2016-testing-the-manifold-hypothesis]] — whether the
  manifold distribution hypothesis this paper starts from actually holds
- [[coifman-lafon-2006]] — diffusion maps, another way of working on the data manifold
- [[bronstein-bruna-cohen-velickovic-2021-geometric-deep-learning-grids-groups-graphs-geodesics-and-gauges]]
  — the broader geometric programme for deep learning
- [[khalid-et-al-2026-a-survey-of-theory-grounded-interpretability-for-deep-neural-networks]]
  — survey that files this paper's OT view under manifold-based interpretability
- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] — latent-variable
  generative models, the family the AE–OT model belongs to
- [[lei-et-al-2018-geometric-understanding-of-deep-learning]] — the 2018 preprint: manifold
  picture, piecewise-linear capacity bounds and the first optimal-transport proposal
