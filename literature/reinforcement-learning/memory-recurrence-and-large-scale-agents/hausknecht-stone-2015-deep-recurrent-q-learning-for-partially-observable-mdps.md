# Deep Recurrent Q-Learning for Partially Observable MDPs

| | |
|---|---|
| **Authors** | Matthew Hausknecht, Peter Stone (Department of Computer Science, University of Texas at Austin) |
| **Year** | 2015 (arXiv v4, January 2017) |
| **Type** | Paper — AAAI 2015 Fall Symposium on Sequential Decision Making for Intelligent Agents. arXiv:1507.06527v4 [cs.LG], 7pp including appendices |
| **PDF** | `hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps.pdf` (in this folder) |
| **BibTeX** | `hausknecht2015deep` |
| **Status** | Reference — short; read all of it, including the conclusion's negative result |

## What it is

DQN plays Atari from a stack of the last four frames. Anything that needs memory beyond four
frames is invisible to it, so the game becomes a **partially observable MDP** (POMDP). This
paper asks the obvious question: **what if the network gets one frame per step and an LSTM
carries the history instead?**

- **Setting (§Partial Observability).** In a POMDP the agent sees an observation o drawn
  from the hidden state s. A Q-network fed o alone estimates Q(o, a), which can be
  arbitrarily far from Q(s, a). Recurrence is meant to narrow that gap by building a belief
  about s from the observation history.
- **Architecture (§DRQN Architecture, Fig. 2).** The minimal change to DQN: the first fully
  connected layer after the convolutions becomes an LSTM of the same size (512). Input is a
  single 84 × 84 frame. App. A reports that replacing that layer works much better than
  stacking the LSTM on top of it.
- **Training from replay (§Stable Recurrent Updates).** Two options:
  - *bootstrapped sequential updates* replay whole episodes and carry the hidden state
    forward, but break DQN's random-sampling assumption;
  - *bootstrapped random updates* start at a random point, unroll 10 steps, and **zero the
    hidden state** at the start.
  Both gave similar results, so all experiments use random updates with a zero start state.
  This is the choice [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]]
  later revisits.
- **Flickering Pong (§Flickering Atari Games).** Each frame is fully shown or fully blanked
  with probability ½. With one frame per step, convolutions cannot see velocity, so the
  LSTM has to integrate it. DRQN does this, and individual LSTM units fire on events such as
  a missed ball or a bounce (Fig. 3d). A 10-frame DQN with the same history also copes.
- **Standard Atari (Table 1).** On nine games DRQN roughly matches DQN: better on Frostbite
  and Double Dunk, clearly worse on Beam Rider.
- **Changing observability (Fig. 5).** Trained on full frames and tested on flickering
  ones, DRQN keeps more of its score than DQN at every flicker rate. Trained on flickering
  Pong, its score rises as observations become more complete.
- **The honest conclusion.** **Recurrence "confers no systematic benefit compared to
  stacking the observations in the input layer"** when learning. Its advantage is
  robustness when observation quality changes between training and evaluation.

## Read with care

- **Small and noisy evidence.** Nine games, a handful of runs, and score standard
  deviations often as large as the gaps between methods. Significance is tested with
  t-tests plus Benjamini–Hochberg, which is better than usual for the period.
- **The partial observability is synthetic.** Flickering is a clean, memoryless corruption.
  The paper itself notes that all 49 standard DQN games are close to fully observable given
  four frames, so the natural Atari results say little about memory.
- **Short memory only.** BPTT runs over 10 steps with a zero start state. The LSTM cannot
  learn dependencies much longer than that window, so "recurrent vs stacked" here really
  compares two ways of using the same 10-frame history.
- **Compute (App. B).** Unrolling is expensive: 30 steps with 10 stacked frames would have
  needed over 56 days for 10M iterations on their hardware.

## Why it's in the library

**Markets are partially observed by construction.** Prices, volumes and fundamentals are
observations of a hidden state (positioning, liquidity, risk appetite). The DRQN framing
states the problem cleanly: a model of Q(o, a), or of returns given features, is not the
model of the state, and the gap is what memory is supposed to close.

**Stacked lags versus a learned state is the same choice a quant makes.** Most return models
feed a fixed window of lagged features to a feed-forward or tree model, which is DQN's frame
stack. This paper's sober answer, that recurrence matches but does not beat stacking unless
observation quality shifts, is a useful prior before reaching for an RNN over price history.
It agrees with the evidence in
[[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]].

**Robustness to degraded inputs is the real argument.** Live data arrive late, stale or
missing in ways the training set did not show. DRQN's graceful degradation when frames are
dropped is the property worth testing for a sequence model, more than its in-sample score.

## Links

- [[kapturowski-et-al-2019-recurrent-experience-replay-in-distributed-reinforcement-learning]] —
  revisits the zero-start-state choice and fixes it with stored state and burn-in
- [[bird-2021-backpropagation-through-time-for-networks-with-long-term-dependencies]] — why a
  10-step truncated BPTT window limits what the LSTM can remember
- [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] — the recurrent
  Q-learning line at full scale
- [[elsayed-et-al-2021-do-we-really-need-deep-learning-for-time-series-forecasting]] — a
  lagged-window model often matches a sequence model, as here
- [[hall-rasheed-2025-survey-of-machine-learning-methods-for-time-series-prediction]] — the
  wider tree-versus-deep evidence for sequence data
