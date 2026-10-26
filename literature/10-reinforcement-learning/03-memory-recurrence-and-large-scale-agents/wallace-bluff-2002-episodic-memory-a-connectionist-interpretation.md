# Episodic Memory: A Connectionist Interpretation

| | |
|---|---|
| **Authors** | J.G. Wallace, K. Bluff (Swinburne University of Technology, Hawthorn, Victoria) |
| **Year** | 2002 |
| **Type** | Conference paper — in J.R. Dorronsoro (ed.), *Artificial Neural Networks — ICANN 2002*, Lecture Notes in Computer Science 2415, pp. 265–270, Springer. 6pp |
| **Link** | https://doi.org/10.1007/3-540-46084-5_44 (Springer; no PDF filed here for copyright reasons) |
| **BibTeX** | `wallace2002episodic` |
| **Status** | Reference — a short position paper; read §2 and §5 |

## What it is

A theoretical sketch, with no model or experiments, of how **episodic memory** (a sequential
record of particular experiences) could turn into **semantic memory** (general knowledge)
in a connectionist system. It starts from the authors' earlier symbolic system and asks
which parts a neural network could do better, and which it struggles with.

- **The symbolic baseline, BAIRN (§2).** Knowledge is a network of nodes. Every node
  activation is logged to a single **time line**: a complete, ordered record of processing
  across parallel channels. Learning scans the time line for **consistently recurring
  segments**. One that recurs often and long enough becomes a new node; a weaker one is
  added to an existing node's experience list.
- **Thresholds everywhere (§2).** Partial matching needs a matching-index criterion. Promotion
  to semantic memory needs a consistency level above a critical threshold, which moves within
  a band depending on how consistent the environment has been.
- **Why connectionism (§3).** Noise tolerance and generalisation make recurring-pattern
  detection easier than exact symbol matching with hand-set thresholds. What is hard for a
  network is keeping a **comprehensive, time-ordered record of episodes**.
- **A speculative mechanism (§4).** Intracellular protein complexes ("hebbosomes", from
  Grant's work) as a way for single neurons to store episode records.
- **The data-volume problem and its answer (§5).**
  - In BAIRN, familiar stretches are replaced by a single token, so analysis focuses on
    **novel segments**.
  - Motivational and emotional processes select which episodes are **significant enough** to
    analyse.
  - The proposed brain analogue is a cascade: a full record in temporal cortex, an
    attenuated one in entorhinal cortex, and a **sparse code in the hippocampus**, where
    significance acts. Learning proceeds from simple to detailed versions, which the authors
    argue lets Hebbian learning handle problems such as XOR that it cannot learn directly.

## Read with care

- **Speculative and dated.** No simulations, no data and no testable predictions. The
  hebbosome mechanism is borrowed from early 2000s proteomics and is not established
  neuroscience.
- **Short.** Six pages, with BAIRN itself described elsewhere. Most claims point to other
  work.
- **Not machine learning in the modern sense.** There is no learning rule, loss or
  architecture to implement. Its value is conceptual.

## Why it's in the library

**It states the episodic-to-semantic problem in plain terms.** An agent, or a research
process, accumulates a long record of specific episodes and must decide which recurring
patterns deserve promotion to general rules. BAIRN's answer — compress the familiar,
promote only what recurs often and long enough above a threshold, and let significance
choose what to study — is a fair description of how a careful researcher should treat
backtest results and market episodes.

**Novelty and significance as filters.** Deep RL agents later used episodic memory in
just this role: [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] rewards
novelty measured against an episodic memory, and prioritised replay chooses what to learn
from by significance. This paper is an earlier, cognitive-science version of the same ideas.

**Fast episodic store, slow semantic store.** The hippocampus–neocortex division it leans on
is the same one used to explain catastrophic interference: learn new episodes quickly
without overwriting slowly built knowledge. That tension is central to models refitted on
non-stationary markets.

## Links

- [[badia-et-al-2020-agent57-outperforming-the-atari-human-benchmark]] — episodic-memory
  novelty as an exploration signal in a deep RL agent
- [[kapturowski-et-al-2022-human-level-atari-200x-faster]] — the episodic-memory-based
  exploration agent made data-efficient
- [[mccloskey-cohen-1989-catastrophic-interference-in-connectionist-networks]] — why a single
  network cannot simply store new episodes without damaging old knowledge
- [[khetarpal-et-al-2022-towards-continual-reinforcement-learning-a-review-and-perspectives]]
  — the modern framing of learning continually from a stream of experience
- [[hausknecht-stone-2015-deep-recurrent-q-learning-for-partially-observable-mdps]] — memory
  in a network as a learned hidden state rather than an explicit record
