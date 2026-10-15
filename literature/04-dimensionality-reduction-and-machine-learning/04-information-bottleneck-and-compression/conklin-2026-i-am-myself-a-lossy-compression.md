# I Am, Myself, a Lossy Compression

| | |
|---|---|
| **Author** | Henry Conklin (Princeton; Peretsman Scully Postdoctoral Fellow for Natural and Artificial Minds) |
| **Year** | 2026 (15 May) |
| **Type** | Research blog post — Princeton AI Lab blog |
| **Link** | https://blog.ai.princeton.edu/2026/05/15/i-am-myself-a-lossy-compression/ |
| **BibTeX** | `conklin2026lossyblog` |
| **Status** | Explainer — cite [[conklin-et-al-2026-learning-is-forgetting]] instead |

## Key takeaway

The first author's plain-language companion to the ICLR paper. It contains no new
experiments; it builds the intuition the paper takes for granted:

- **Lossy versus lossless.** Zip and PNG keep everything; JPEG and MP3 throw information
  away for good. The design question is *what* to throw away, and a lossy codec answers it
  by being "opinionated about the receiver": it discards what human eyes and ears won't
  miss. Everyday examples include Morse code, vervet monkeys' three alarm calls (eagle,
  snake, leopard) and human memory, which keeps a few moments precisely and the rest as
  a general impression.
- **Compression is what makes generalisation possible.** Discarding detail maps
  functionally similar inputs close together, and "generalization behaviour is a function
  of representational geometry". The post grounds this in cognitive science: Shepard's
  universal law of generalisation, Tenenbaum & Griffiths' Bayesian version of it,
  exemplar and prototype models of categories.
- **Rate–distortion and the information bottleneck** are introduced informally, with the
  information plane (complexity against expressivity) and the bound that good compression
  sits near.
- **The source distribution matters.** A codec is tuned to its data. The internet is
  already a biased, noisy compression of human knowledge before an LLM compresses it
  again.
- **The training objective defines what counts as distortion.** For pre-training that is
  next-token prediction. Post-training (RLHF, DPO) "changes the codec": the same kind of
  weights, reorganised around a different target. That is the paper's preference-information
  result, stated conceptually.
- **The whole model is the unit of analysis**, not single circuits (Anderson, "More Is
  Different", 1972).

## Why it's here

It's the easiest way into the paper, and the clearest statement of the idea this folder
adds to the section. Every compression method encodes a choice about what to forget, and
that choice is set by the objective. PCA forgets low-variance directions; a predictive
model should forget whatever doesn't help predict the target. Read it before the paper.
Nothing here is load-bearing: the claims are supported in the paper, not in the post.

## Links

- [[conklin-et-al-2026-learning-is-forgetting]] — the paper: estimator, results and caveats
- [[busemeyer-bruza-2012]] — another cognitive-science account of how representations
  are structured
