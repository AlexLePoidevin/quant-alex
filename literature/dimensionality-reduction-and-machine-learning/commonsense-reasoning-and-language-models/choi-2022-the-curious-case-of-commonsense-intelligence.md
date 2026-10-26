# The Curious Case of Commonsense Intelligence

| | |
|---|---|
| **Author** | Yejin Choi (Paul G. Allen School of Computer Science & Engineering, University of Washington; Allen Institute for AI) |
| **Year** | 2022 |
| **Type** | Essay — *Dædalus* 151(2), Spring 2022, pp. 139–155 (issue on AI and society). Open access, CC BY-NC 4.0. DOI 10.1162/DAED_a_01906 |
| **PDF** | `choi-2022-the-curious-case-of-commonsense-intelligence.pdf` (in this folder) |
| **BibTeX** | `choi2022curious` |
| **Status** | Reference — a short, non-technical essay; read it in one sitting |

## What it is

A position essay on why common sense, trivial for people, has been so hard for AI, and why
the author thinks recent work with language models changes that. Its argument has four
parts.

- **Intuitive inference is generative, not a choice from a list.** Shown Shepard's *Terror
  Subterra* (two identical monsters in a tunnel), people instantly infer a chase, a hostile
  chaser and a frightened victim, and even "see" different expressions on identical faces.
  Those inferences are produced on the fly, without weighing the alternatives. Most ML
  benchmarks instead pose reasoning as **classification over a fixed set of labels**, which
  cannot cover an open-ended, compositional space of possible inferences.
- **Common sense is defeasible.** Every such inference can be overturned by more context
  (the monsters are friendly; they are practising a dance). A framework built to derive
  *true* conclusions, as formal logic is, rarely produces the useful, revisable ones.
- **Logic failed on scale, not on missing probabilities.** Logic-based systems need someone
  to supply the variables and rules, and hand-built ones stayed narrow and brittle. Putting
  probabilities on top of a small fixed rule set does not widen what it can describe. The
  essay argues for **language itself** as the representation: imprecise, but expressive
  enough.
- **Abduction over deduction.** Most everyday reasoning is abductive (Peirce): inventing the
  best explanation for a partial observation, which adds information that was not in the
  premises. The essay's example: Sherlock Holmes, described as deductive, is mostly
  abductive. Counterfactual reasoning is the close relative.

It then describes the author's group's systems as evidence:
- **DeLorean** — decoding with an ordinary left-to-right language model that also
  conditions on the *future* (by back-propagating into the output representation with the
  model fixed), for abductive and counterfactual text generation.
- **COMET**, trained on the **ATOMIC** knowledge graph (about 1.3 million everyday if-then
  facts written in plain language), which generalises to situations ATOMIC does not cover.
  The claim is that knowledge and reasoning form a continuum rather than separate things.
- **Symbolic knowledge distillation** — GPT-3 writing an ATOMIC-style knowledge graph that
  beats the human-written one on scale, quality and diversity.
- **Delphi** — a moral-judgment model trained on 1.7 million human judgments (80–92%
  agreement with human vetting vs 52.3% for GPT-3 off the shelf), with the author's own
  caveats about bias and that AI should not be a moral authority.

## Read with care

- **An essay, not a study.** The evidence is the author's own projects, described briefly;
  the numbers come from the cited papers and are not reproduced or compared here.
- **Dated by its moment.** Written around GPT-3, before instruction-tuned chat models. Some
  claims (that scale alone does not give common sense or values) read differently now, and
  should be checked against later work rather than taken as settled.
- **Delphi was controversial.** Its public demo drew criticism for confident, sometimes
  biased judgments. The essay acknowledges limitations but is not a neutral account.
- **Nothing on finance.** Its relevance here is by analogy, set out below.

## Why it's in the library

**Classification over fixed labels is a modelling choice, and it limits what can be said.**
Most return models are discriminative in exactly the essay's sense: pick a bucket, a rank,
a sign. That is right when the action is a choice among fixed options, such as long, short
or flat. It is the wrong frame when the useful output is an *explanation* — why a factor
stopped working, what a market move implies — where the space of answers is open.

**Market inferences are defeasible.** A regime call, a factor story, a reading of a price
move are all best guesses that more context should be allowed to overturn. A process that
treats them as established truths, rather than revisable hypotheses, is the failure the
essay describes. This is the same lesson as [[soros-2013]]: participants' views are
fallible and change what they are views of.

**Research is mostly abduction.** Proposing the explanation that would account for a
backtest result, then testing it, is abductive reasoning; the essay is a clear statement of
why that step cannot be reduced to deduction or to fitting a model. It is also why a strong
result should be met with the question "what else would explain this?" before it is
believed.

**Machine-written knowledge can beat human-written knowledge — on the measures chosen.**
Symbolic knowledge distillation is an early example of using a large model to generate
training data. The same idea, and the same need to check what the generated data actually
contains, applies to any language-model labelling of news, filings or transcripts.

## Links

- [[dawid-lecun-2023-introduction-to-latent-variable-energy-based-models]] — a different
  route to machine common sense: world models trained by self-supervised prediction rather
  than through language
- [[conklin-et-al-2026-learning-is-forgetting]] — what large language models keep and
  discard as they train
- [[busemeyer-bruza-2012]] — another account of how human reasoning departs from classical
  logic and probability
- [[soros-2013]] — fallible, revisable views as the normal condition of market participants
- [[zhang-et-al-2017-understanding-deep-learning-requires-rethinking-generalization]] — why
  generalisation beyond the training data is the hard question for neural models
