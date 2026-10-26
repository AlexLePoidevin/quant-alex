# Backpropagation Through Time For Networks With Long-Term Dependencies

| | |
|---|---|
| **Authors** | George Bird (University of Manchester; student preprint), edited by Maxim E. Polivoda (Bangor University) |
| **Year** | 2021 (v2, 18 April) |
| **Type** | Preprint — arXiv:2103.15589v2 [cs.LG], 9pp. Not peer reviewed; no experiments |
| **PDF** | `bird-2021-backpropagation-through-time-for-networks-with-long-term-dependencies.pdf` (in this folder) |
| **BibTeX** | `bird2021backpropagation` |
| **Status** | Reference — read §1 for the clear statement of the truncation problem and §2 for the recursion; treat §2.1.1 as speculation |

## What it is

A short note on how gradients are computed in recurrent networks. Its useful part is a plain
statement of **what truncated BPTT assumes**, and a forward-mode alternative that carries
gradient information through time instead of unrolling backwards.

- **The problem (§1).** To train an RNN exactly, every past step that influenced the current
  output must enter the gradient. Unrolled naively, cost and memory grow linearly with the
  number of steps.
- **Approximations (§1.1–1.2).**
  - A *0th-order* approximation ignores the recurrent path, which in effect treats the RNN
    as a feed-forward network.
  - *Nth-order* approximations backpropagate N steps.
  - **Truncated BPTT** splits the sequence into fixed partitions and updates once per
    partition. It holds parameters fixed inside the window and **assumes nothing outside
    the window matters**. Steps early in a window get even shorter effective memory.
- **The proposal (§2, Eqns 1–3).** Carry a sensitivity matrix forward with the forward
  pass, the *discrete forward sensitivity equation*:
  Δ_N = ∂R_N/∂P_N + (∂R_N/∂R_{N−1}) Δ_{N−1},
  where R is the recurrent state and P the parameters. The output gradient is then
  ∂Y_N/∂P_N + (∂Y_N/∂R_{N−1}) Δ_{N−1}. **The cost per step is constant in sequence length**,
  and parameters can be updated at every step.
- **Several recurrent loops (§2.1, Eqns 4–5).** For architectures like the LSTM, each loop
  gets its own Δ with cross terms between loops. An informal "recurrency-abstraction"
  argument (§2.1.1) claims half of those cross terms are zero.
- **Temporal gradient explosion (§2.2).** If the accumulated sum diverges, the forward
  dynamics are chaotic. Damping it fixes the problem but makes the method approximate again.
- **Derivation (§3).** Expands the full chain rule and rewrites it as the recursion above.

## Read with care

- **This is real-time recurrent learning.** The recursion is, in substance, RTRL (Williams
  & Zipser, 1989), which the note does not cite. RTRL's known cost applies: Δ has size
  (state width × number of parameters), and updating it each step costs roughly
  (state width)² × parameters. That is why practice uses truncated BPTT, or approximations
  of RTRL, for networks of any size.
- **"Exact" needs a qualifier.** If parameters change every step, Δ mixes Jacobians from
  older parameter values. The result is then also an approximation, as in standard RTRL.
- **No experiments.** The author says the benefits cannot yet be shown on current models.
  Nothing here measures speed, memory or learning quality.
- **§2.1.1 is not a theorem.** The intrinsic-dimension argument for dropping cross terms is
  informal and should not be relied on.

## Why it's in the library

**It names the assumption hidden in every recurrent model you fit.** Truncated BPTT over a
window of k steps means the model cannot learn credit assignment over more than about k
steps, whatever the hidden state could carry in principle. For an RNN over daily prices
trained on 20- or 60-day windows, that window is the real memory length. It is the same limit
that DRQN's 10-step unroll, R2D2's 80-step sequences and Agent57's doubled window run into.

**Forward-mode gradients suit online, streaming updates.** A model updated once per bar,
without storing and replaying the history, needs gradient information carried forward. The
recursion here is the starting point for that, and its cost explains why it is rarely used
directly.

**A reminder to check the literature behind a clean derivation.** The idea is sound but
old. Reading it against RTRL is a small exercise in the habit this library tries to build.

## Links

- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] — a
  10-step truncated unroll with a zero start state, and what it can and cannot learn
- [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]] —
  stored state and burn-in as practical fixes for truncation
- [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] — doubling the BPTT
  window improved long-horizon credit assignment
- [[dohare-sutton-mahmood-2021-continual-backprop-stochastic-gradient-descent-with-persistent-randomness]]
  — another look at what plain backprop lacks when learning never stops
- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] — when a
  fixed window of lags is enough
