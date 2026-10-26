# Trust Region Policy Optimization

| | |
|---|---|
| **Authors** | John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan, Pieter Abbeel (UC Berkeley, EECS) |
| **Year** | 2015 |
| **Type** | Paper — *Proceedings of the 32nd International Conference on Machine Learning* (ICML 2015), JMLR W&CP 37. arXiv:1502.05477v5 [cs.LG], 16pp including appendices |
| **PDF** | `schulman-et-al-2015-trust-region-policy-optimization.pdf` (in this folder) |
| **BibTeX** | `schulman2015trust` |
| **Status** | Reference — read §2–4 and §6 for the idea; §5 and App. C for the estimator and the conjugate-gradient step |

## What it is

Policy gradients tell you which way to move a policy, not how far. Too small a step wastes
samples; too large a step can collapse performance, and the next batch of data is then
collected by the broken policy. TRPO answers "how far" with **a KL-divergence trust region**:
maximise a local surrogate of the return, subject to the new policy staying close, on
average over states, to the old one.

- **The identity (§2, Eq. 1).** The return of a new policy equals the old return plus the
  new policy's expected advantage under the old policy's advantage function, summed along
  the new policy's trajectories. Replacing the new state distribution with the old one gives
  a **surrogate L** that matches the true objective to first order (Eq. 3–4).
- **Monotonic improvement (§3, Thm 1).** Extending Kakade & Langford's conservative policy
  iteration bound to general stochastic policies: η(new) ≥ L(new) − C · max-KL(old, new),
  with C = 4εγ/(1 − γ)². Maximising this lower bound at each step (Algorithm 1, a
  minorisation-maximisation scheme) **guarantees the true return never falls**, assuming
  exact advantages.
- **From penalty to constraint (§4).** The theoretical C gives tiny steps. TRPO instead
  maximises L subject to a hard constraint on **average KL ≤ δ** (Eq. 12). The max-KL
  version behaves similarly where it is tractable (cart-pole).
- **Estimation (§5).** Single-path: ordinary trajectories with Monte Carlo returns, usable on
  real systems. Vine: branch several rollouts from chosen states with common random numbers,
  lower variance but needs a resettable simulator.
- **The step (§6, App. C).** Linear approximation of L, quadratic approximation of the KL
  (the Fisher matrix, computed analytically as the KL Hessian), solve with conjugate
  gradients using Fisher-vector products, then a line search that enforces the constraint
  and improvement.
- **Connections (§7).** With a fixed penalty instead of a constraint it becomes the natural
  policy gradient; with an ℓ2 constraint, the vanilla gradient. **The difference that
  matters is enforcing δ at every update**, rather than fixing a step size.
- **Experiments (§8).** MuJoCo swimmer, hopper and walker with neural network policies, δ =
  0.01 throughout: both TRPO variants solve all tasks, while natural gradient with a tuned
  fixed step fails on hopper and walker, and CEM/CMA scale badly with parameter count. On
  seven Atari games from pixels, TRPO is competitive with DQN but not uniformly better.

## Read with care

- **The guarantee is for the idealised algorithm.** Monotonic improvement needs exact
  advantages and the max-KL penalty. The practical algorithm uses sampled advantages, an
  average-KL constraint and a quadratic approximation, so it "tends to" improve monotonically;
  it is not guaranteed.
- **Sample-hungry and on-policy.** Every update needs fresh rollouts from the current
  policy. That is affordable in simulation, much less so when each sample is a day of
  market data.
- **Thin statistics on Atari.** Each Atari game was run once (Table 1); the authors note large
  run-to-run variation and no error bars.
- **Superseded in practice.** PPO (Schulman et al. 2017) replaced the constrained solve with
  a clipped surrogate and is what most libraries use. The trust-region idea is what lasted.

## Why it's in the library

**It is the clearest statement of "do not let the model move too far per update".** In a
system retrained every day, the new model is fitted on data that overlaps almost entirely
with yesterday's. A trust region on the change in the *output distribution* — not the
parameters — is the principled way to stop a retrain from flipping a book because of noise.
The KL between yesterday's and today's ranking or weight distribution is a useful turnover
and stability diagnostic even outside RL.

**It measures step size in the right units.** The parameter-space step is meaningless when
the model is reparameterised; the KL between policies is not. The same reasoning applies to
any model whose output is a distribution over actions or ranks, including the Plackett–Luce
ranking losses used for cross-sectional selection.

**It is the background to later regularised methods.** Implicit KL regularisation between
successive policies is exactly what Munchausen RL turns out to do
([[vieillard-pietquin-geist-2020-munchausen-reinforcement-learning]]), and meta-gradient
methods adapt the step and objective online.

## Links

- [[silver-et-al-2014-deterministic-policy-gradient-algorithms]] — the deterministic,
  off-policy route to continuous-action policy gradients
- [[rajeswaran-et-al-2017-towards-generalization-and-simplicity-in-continuous-control]] —
  normalised natural gradient with linear policies, essentially TRPO's step without the
  line search
- [[haarnoja-et-al-2018-soft-actor-critic]] — off-policy alternative that names TRPO's
  sample cost as the problem to solve
- [[vieillard-pietquin-geist-2020-munchausen-reinforcement-learning]] — KL regularisation
  between successive policies, obtained implicitly
- [[fuhrer-tessler-dalal-2024-gradient-boosting-reinforcement-learning]] — PPO, TRPO's
  successor, run with gradient-boosted trees as the function class
- [[luketina-et-al-2022-meta-gradients-in-non-stationary-environments]] — adapting update
  hyperparameters online when the environment drifts
