# Deep Learning Volatility: A Deep Neural Network Perspective on Pricing and Calibration in (Rough) Volatility Models

| | |
|---|---|
| **Authors** | Blanka Horvath, Aitor Muguruza, Mehdi Tomas |
| **Year** | 2021 (*Quantitative Finance* 21(1), 11–27; online October 2020). arXiv 1901.09647, January 2019 |
| **Type** | Paper, 32pp (arXiv v2, 22 August 2019) |
| **PDF** | `horvath-muguruza-tomas-2021-deep-learning-volatility.pdf` (arXiv version) |
| **BibTeX** | `horvath2021deep` |
| **Status** | Reference: §3.2 (network and grid design) and §4 (accuracy, calibration speed, SPX calibration) carry the results |

## What it is

A way to make slow option models usable for calibration: train a neural network, offline,
to reproduce the model's whole implied-volatility surface from its parameters, then
calibrate against the network instead of the slow pricer.

- **The "image" idea.** The network's output is not one option price but the entire
  surface on a fixed grid of 8 maturities × 11 strikes, like the pixels of an image. The
  authors argue this makes training more stable and the parameter-to-surface map easier
  to invert than training one option at a time.
- **Network.** Four hidden layers of 30 units with smooth ELU activations, so that
  gradients with respect to the parameters are reliable, about 6,800 weights in all.
- **Training data.** 80,000 random parameter sets (68,000 train, 12,000 test) for rough
  Bergomi and one-factor Bergomi, each with a piecewise-constant forward variance curve.
  Each surface is priced by Monte Carlo with 60,000 paths.
- **Accuracy.** Average relative error against Monte Carlo is well under 0.5%, with a
  standard deviation under 1%, which is within the Monte Carlo noise itself. The maximum
  relative error reaches 25% for some parameter sets.
- **Speed.** A full surface takes about 31 µs from the network against 0.3–0.5 s by Monte
  Carlo, a 9,000–16,000× speed-up. Calibration with Levenberg–Marquardt takes milliseconds.
- **Real data.** Rough Bergomi calibrated daily to SPX smiles, 2010 – March 2019. The
  Hurst exponent comes out at about 0.1–0.15, matching earlier rough-volatility estimates,
  and the fit is within about 0.2% of a brute-force Monte Carlo calibration most days.
- **Extensions.** Digital barrier options (absolute errors under 10bp), and a small
  classifier that tries to tell which model (Heston, Bergomi or rough Bergomi) generated
  a surface.

## Why it's in the library

Rough-volatility models fit the equity smile and its short-dated skew well but have no
closed-form prices, which kept them off trading desks. This paper is the standard
reference for removing that bottleneck: move the expensive pricing into an offline
training step and calibrate in milliseconds. It is the template for "neural network as a
fast pricer" work.

Points to keep in mind:

- **The network only learns the pricer it was trained on.** It is as good as the Monte
  Carlo behind it, and only inside the sampled parameter box and grid. Strikes or
  maturities off the grid need interpolation.
- **The headline error figures are measured on the training set** (Figures 6–7 say "across
  all training data"); the out-of-sample accuracy is asserted to be in the same range.
- **Gradients are a weak spot.** Differential evolution, which uses no gradients, beat
  Levenberg–Marquardt on real data, and the authors suspect the network's first
  derivatives are not accurate enough.

## Links

- [[carr-wu-2011-a-new-simple-approach-for-constructing-implied-volatility-surfaces]] — a
  different shortcut to fast surface calibration: model the implied volatilities directly
- [[carr-et-al-2019-model-free-pdes-for-implied-volatility]] — computing implied volatility
  quickly by solving PDEs instead of root-finding
- [[carr-madan-2014-joint-modeling-of-vix-and-spx-options]] — fitting SPX and VIX options in
  one model, the joint calibration that rough-volatility models are also used for
- [[monciaud-reghai-2021-singular-exotic-perturbation]] — pricing exotics under
  stochastic-local volatility, where fast calibration also matters
- [[lipton-sepp-2022-hybrid-method-for-pricing-barrier-options-with-stochastic-volatility]] —
  barrier options under stochastic volatility by a numerical method, the problem the
  network approximates in §4.3
