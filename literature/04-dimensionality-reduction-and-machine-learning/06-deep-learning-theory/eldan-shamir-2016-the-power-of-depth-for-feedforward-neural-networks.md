# The Power of Depth for Feedforward Neural Networks

| | |
|---|---|
| **Authors** | Ronen Eldan, Ohad Shamir (Weizmann Institute of Science) |
| **Year** | 2016 |
| **Type** | Paper — *29th Annual Conference on Learning Theory* (COLT 2016), PMLR 49; arXiv:1512.03965v4 [cs.LG], 33pp including proofs |
| **PDF** | `eldan-shamir-2016-the-power-of-depth-for-feedforward-neural-networks.pdf` (in this folder) |
| **BibTeX** | `eldan2016power` |
| **Status** | Reference — read §1 (Theorem 1 and remarks) and the §2 proof sketch; §4 is the formal proof |

## What it is

A depth-separation theorem. It shows there is a simple function on ℝᵈ that a **3-layer
network of polynomial width** can approximate well, but that **no 2-layer network can
approximate beyond a constant error unless its width is exponential in d**. One extra layer
can be worth exponentially many neurons.

- **The question (§1).** Universal approximation says a wide enough 2-layer network can fit
  any continuous function, but the width needed may be exponential in the dimension. For
  networks of bounded size, should you go wide and shallow or narrow and deep?
- **Theorem 1.** For almost any standard activation (ReLU, sigmoid, threshold; Assumptions
  1–2 only ask that a 2-layer net can fit univariate Lipschitz functions and that σ grows at
  most polynomially) there is a distribution µ and a bounded function g such that g is
  expressible by a 3-layer net of width about d^{19/4}, while every 2-layer net of width at
  most c·e^{cd} has mean squared error at least a constant c.
- **The hard function is radial (§2).** g depends on the input only through ‖x‖. Three
  layers make this easy: the first layer builds x ↦ ‖x‖² as a sum of approximate squares, the
  next applies a univariate function to it. Two layers cannot compose like this.
- **Why two layers fail (§2).** A 2-layer net is a sum of ridge functions f_i(⟨v_i, x⟩). In
  Fourier space each ridge function lives on a line, so after smoothing by the input density
  the whole network's spectrum sits inside k thin tubes through the origin. In high
  dimension, k tubes cover an exponentially small fraction of a large sphere. The target is
  built as a random-sign sum of thin radial shells, which puts constant mass at high
  frequencies in every direction, so a sub-exponential number of tubes cannot catch it.
- **Few assumptions (Remarks 1–3).** No bounds on the 2-layer net's weights, activations
  may even differ across neurons, and the 3-layer construction has polynomially bounded
  weights and a poly(d) Lipschitz constant. Related work (Telgarsky 2015) gets separations
  only in one dimension with exponentially oscillating functions, or for Boolean circuits.

## Read with care

- **Expressivity, not learnability.** The theorem says a small 3-layer network exists; it
  says nothing about whether gradient descent finds it from data, or how many samples that
  would take.
- **A constructed, adversarial target.** The hard function is a carefully signed sum of thin
  shells under a specific oscillating input density. The authors conjecture, but do not
  prove, that a wider class of radial functions behaves the same.
- **Constant error, not failure.** Two-layer networks are shown to miss by a fixed constant
  in mean squared error. On noisy targets where the achievable error is already large, a
  constant gap may or may not matter.
- **Two versus three layers only.** It does not say how much further depth helps, and the
  exponential gap needs the input dimension d to be large.

## Why it's in the library

**It is the formal reason depth can beat width.** When choosing the shape of a small network
for tabular features, the instinct to add width rather than layers has a clear failure
mode: functions built by composition — a nonlinear function of a norm, a ratio, an
interaction of aggregated quantities — can need exponentially many neurons in one hidden
layer and only a modest number in two. The construction is also a recipe: if you believe the
target is a function of a few engineered aggregates, depth is how a network can build those
aggregates itself.

**Read it next to the tabular-data evidence.** Benchmarks on tabular problems find tree
ensembles still beat deep networks
([[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]],
[[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]]). This paper does
not contradict that: it concerns what a network can represent, not what it learns from a few
thousand noisy rows. Representational power is necessary, not sufficient, and on
low-signal data the extra capacity of depth is also extra room to fit noise.

**It is the counterpoint to the wide-network theory in this folder.** The NTK results
([[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]]) make very wide
networks behave like fixed kernel machines. Eldan and Shamir show what width alone cannot
buy: composition. Feature learning in the rich regime
([[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]]) is how a trained
network can actually exploit it.

## Links

- [[lee-et-al-2019-wide-neural-networks-of-any-depth-evolve-as-linear-models]] — the
  wide-network limit, where depth adds little beyond a fixed kernel
- [[karkada-2024-the-lazy-ntk-and-rich-mup-regimes-a-gentle-tutorial]] — the training regime
  in which a network can learn intermediate features of the kind this proof builds by hand
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] —
  expressive power is plentiful; generalisation is the harder question
- [[grinsztajn-oyallon-varoquaux-2022-why-do-tree-based-models-still-outperform-deep-learning-on-tabular-data]]
  — the empirical side: on tabular data, representational power is not the bottleneck
- [[shwartz-ziv-armon-2022-tabular-data-deep-learning-is-not-all-you-need]] — the same verdict
  from a benchmark of deep tabular models against boosted trees
- [[beyer-et-al-1999-when-is-nearest-neighbor-meaningful]] — another face of high-dimensional
  geometry: most of a sphere is far from any fixed set of directions
