# On the Impossibility of an AI Mathematician Being Both Autonomous and Useful

| | |
|---|---|
| **Author** | Kharen Musaelian (Qognitive, Inc.) |
| **Year** | 2025 |
| **Type** | Working paper — Qognitive, 5–6pp. Not peer-reviewed. First circulated 30 July 2025 as *On the Impossibility of AI Passing a Modified Birch Test*; revised and retitled 11 August 2025 |
| **Link** | Revised version, [archived copy](https://web.archive.org/web/20260615202433/https://www.qognitiveai.com/papers/Birch_Test_paper.pdf); no longer listed on qognitiveai.com |
| **PDF** | Not hosted in this repository (the 30 July draft) |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22On+the+Impossibility+of+an+AI+Mathematician+Being+Both+Autonomous+and+Useful%22+Musaelian) for the title and authors |
| **BibTeX** | `musaelian_ai_mathematician` |
| **Status** | Reference — read in full (both versions) |

## What it is

A short argument that no Turing machine can do mathematics that is both autonomous and
useful. It responds to the *Birch test* proposed by He and Burtsev (*Nature*, 2024), which
asks an AI mathematician to produce work that is interpretable, autonomous and non-trivial.
Musaelian folds "interpretable and non-trivial" into one word, "useful".

- **The set-up.** A "robot mathematician" is a Turing machine that derives results and
  halts only when it has found something useful. Halting is the autonomy condition: if it
  printed everything, a human would have to sift the output.
- **The step that carries the argument.** To avoid running forever, the robot would need an
  "anticipation machine" that predicts whether a given robot will halt. The paper then
  stipulates that a machine which proves some robot never halts has itself produced a
  useful result, so it is also a robot.
- **The proof.** With that stipulation, Turing's diagonal argument for the halting problem
  goes through: no machine can decide halting for every robot and input, so any robot can
  run forever without a human to reset it.
- **Objections answered.** Can a robot be useful most of the time? Can it be designed to
  halt? Is "useful" doing any work? (The paper says yes: replace it with "green" and the
  self-reference step fails.) Do time limits help? (No: a chain of restarted machines is
  one machine.)
- **The August revision.** It renames the robot an "autonomous Turing machine" that
  launches theorem-generating sub-machines and checks each with a "detection machine" for
  usefulness, and it requires the set of robots to be recursively enumerable. It adds a
  sixth objection: usefulness may only be definable outside mathematics, as truth is in
  Tarski's theorem. The author agrees, and notes that in that case the detection machine
  cannot exist and the conclusion follows without the rest of the argument.
- **The conclusion.** The argument covers only Turing machines. Musaelian suggests human
  mathematicians succeed because they are closer to analog devices with uncountably many
  states, following Penrose, and that mathematics will keep needing humans.

## Why it's in the library

**It states the philosophy behind the QCML programme.** The 2024 position paper,
[[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]], argues that
models built on classical probability cannot form concepts or judge relevance. This paper
makes the same claim about computation itself: a discrete machine cannot judge whether its
own output is worth anything, and the suggested way out is a continuous, analog
representation. That is the motivation for representing data as states in a Hilbert space.

**The proof is the halting problem; the conclusion rests on the stipulation.** Everything
hinges on declaring that a proof of non-halting is "useful". Granting it shows only that no
single machine can predict, for every robot, whether it will ever find something. It does
not show that a robot rarely or never finds something, only that success cannot be
guaranteed in advance. The same limit applies to a human mathematician, who also cannot
decide halting, so the argument separates people from machines only if one also accepts
the analog-mind claim, which the paper offers as a suggestion, not a result. The author's
own sixth objection shows how much depends on how "useful" is defined.

**It is philosophy, not evidence.** There are no experiments, and the paper is unpublished.
It is filed here as the founder's stated view, to read alongside the technical papers.

## Links

- [[musaelian-et-al-2024-quantum-cognition-machine-learning-ai-needs-quantum]] — the
  position paper making the parallel claim about classical probability
- [[abanov-et-al-2025-quantum-geometry-of-data]] — the continuous Hilbert-space
  representation that the "analog device" argument points towards
- [[busemeyer-bruza-2012]] — quantum models of human judgement, the cognitive foundation of
  the programme
