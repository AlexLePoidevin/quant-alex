# Learning is Forgetting: LLM Training as Lossy Compression

| | |
|---|---|
| **Authors** | Henry C. Conklin, Tom Hosking, Tan Yi-Chern, Julian Gold, Jonathan D. Cohen, Thomas L. Griffiths, Max Bartolo, Seraphina Goldfarb-Tarrant (Princeton University; Cohere) |
| **Year** | 2026 |
| **Type** | Conference paper — ICLR 2026. arXiv:2604.07569v1 [cs.LG], 8 April 2026, 33pp |
| **Code** | https://github.com/hcoxec/soft_h |
| **PDF** | `conklin-et-al-2026-learning-is-forgetting.pdf` (in this folder) |
| **BibTeX** | `conklin2026learning` |
| **Status** | Reference |

## What it is

The paper treats a large language model as a *lossy compressor*. It tests the
**Information Bottleneck** (IB) theory of deep learning (Tishby & Zaslavsky 2015) on
transformers at scale for the first time.

**The framework.** An encoder maps input X to a representation Z, which is used to predict
a target Y. The IB looks for the representation that minimises

  F_β = I(X; Z) − β·I(Y; Z),

that is, the one that keeps as little about the input as possible (low *complexity*,
I(X;Z)) while keeping as much about the target as possible (high *expressivity*, I(Y;Z)).
Plotting the two against each other gives the *information plane*. The paper uses the
line I(X;Z) = I(Z;Y) as the bound on optimal compression: each bit kept about the input
buys one bit about the target. Its *optimality* statistic measures how close a model sits
to that line.

**The estimator.** Mutual information in a space with thousands of dimensions can't be
computed by binning. The authors normalise each hidden state onto the unit sphere and
soft-assign it, by a softmax over cosine similarities, to n random anchor points. They then
take the Shannon entropy of the averaged assignment, averaged over layers. Conditioning on
labels (token ids, n-gram context, preference labels) gives I(X; Z). The estimator is from
Conklin (2025), and it needs only one forward pass.

**Findings:**

1. **Two-phase training, as the IB predicts.** OLMo2 7B first *expands*: I(Y;Z) rises. Then
   it *compresses*: I(X;Z) falls and the model moves toward the bound. The switch happens as
   next-token loss saturates. Smol LM2 and Pythia show the same pattern (appendix D).
2. **Scale is needed to compress.** The 7B and 32B models reach the bound. The 1B model
   completes the expansion phase but then oscillates and drifts away from the bound.
3. **Models mostly encode local context.** Most information is at the token-to-4-gram level.
   Larger models devote more of it to context than to single tokens.
4. **Models from different families converge.** Across 47 open-weight models from 6
   families, final representations cluster at roughly the same point near the bound.
5. **Compression predicts performance.** Optimality is measured on generic C4 web text,
   never on benchmark data. The ratio of expressivity to complexity correlates with
   aggregate scores on MMLU-Pro, BBH, MATH, IFEval, GPQA and MuSR (r = 0.52). Complexity
   alone correlates *negatively* (r = −0.38) and expressivity alone not at all (r = 0.08).
   Mutual information with human-preference labels gives r = 0.76. Instruction following is
   the exception: compression of C4 doesn't predict it.

The authors suggest optimality could serve as a cheap **stopping or model-selection
criterion**, chosen without looking at the test distribution. They don't test this.

## Read with care

- **The bound is the loose one.** By the data-processing inequality, I(X;Z) = I(Z;Y) is only
  an upper envelope. The true IB frontier for a given p(X,Y) lies below it. "Approaching the
  bound" means approaching that line, not the exact optimum (footnote 1, appendix E.8).
- **Long contexts are approximated by n-grams.** Conditioning stops at 4-grams. Everything
  the model encodes beyond that is outside the measurement.
- **The performance correlations are cross-sectional and modest.** They cover 47 models,
  with parameter count partialled out in some panels. That supports association, not a
  recipe.
- **The compression phase is contested in the wider literature.** Saxe et al. (2019) tie it
  to the choice of nonlinearity, and Goldfeld et al. (2019) show generalisation without it.
  The paper cites both.
- **Minor inconsistency:** the preference result is reported as p < 0.001 in the
  introduction and p = 0.001 in §4.2.

## Why it's in the library

**It is the supervised counterpart of PCA.** PCA keeps the directions with the most
*variance*, whether or not they predict anything. The IB keeps the information in X that
is *relevant to a target*. This is the step past component analysis, manifold methods and QCML in this section,
which compress without reference to what will be predicted. For returns, the high-variance
directions (the market mode, sector modes) aren't necessarily the predictive ones. The
same distinction motivates IPCA and supervised autoencoders in
`../../factor-models-and-asset-pricing/machine-learning-factor-models/`.

**"Learning is forgetting" is the overfitting argument stated in information terms.** A
model that keeps more input information than the target needs has memorised noise. The
two-phase picture (fit, then compress) is the representation-level view of the
bias–variance trade-off. In the paper's results, lower complexity at equal expressivity
generalises better.

**A selection criterion that doesn't touch the evaluation data.** Measuring optimality on
generic data and then predicting held-out benchmark performance is the discipline any
backtest needs: choose by a property of the fitted model, not by its score on the window
it will be judged on. The authors propose this but leave it untested.

**Capacity sets the floor.** Small models can't compress. That fits with the intrinsic
dimension estimators in `../manifolds-and-intrinsic-dimension/`: how many dimensions
the data really has limits how small a useful representation can get.

## Links

- [[conklin-2026-i-am-myself-a-lossy-compression]] — the first author's plain-language blog
  companion; read it first
- [[ica]], [[kernel-pca]], [[hyvarinen-oja-2000]] — unsupervised compression, the baseline
  this paper's supervised criterion moves past
- [[levina-bickel-2004]], [[facco-et-al-2017]] — intrinsic dimension, the geometric
  counterpart of an information-theoretic compression measure
- [[coifman-lafon-2006]] — diffusion maps, another representation of data on a manifold
- [[gu-kelly-xiu-2021]], [[kelly-pruitt-su-2019]] — supervised compression of
  characteristics into return factors
- [[busemeyer-bruza-2012]] — a different cognitive-science model of representation (quantum
  probability); this paper comes from the Bayesian and compression side of the same field
- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] — LeCun's JEPA: predict in representation space, keep
  representations informative and the latent variable small
- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — the original account of forgetting when a network learns in sequence
- [[dohare-et-al-2024-loss-of-plasticity-in-deep-continual-learning]] — the opposite failure: a network that can no longer learn
