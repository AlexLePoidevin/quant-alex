# Coherent Measures of Risk

| | |
|---|---|
| **Authors** | Philippe Artzner; Freddy Delbaen; Jean-Marc Eber; David Heath |
| **Year** | 1999 |
| **Type** | Paper — *Mathematical Finance* 9(3) |
| **BibTeX** | `artzner1999coherent` |
| **Status** | To read |

## Key takeaway

Four axioms a risk measure ought to satisfy — monotonicity, translation invariance,
positive homogeneity and **subadditivity**. VaR fails subadditivity: the VaR of a combined
portfolio can exceed the sum of the parts', so the measure can penalise diversification.
CVaR satisfies all four.

## Why it's here

Why the constraint in `rockafellar-uryasev-2000` is written on CVaR rather than VaR.
Worth one sentence in the article: a risk limit that punishes diversification is
particularly perverse here, because reducing portfolio variance is the *only* lever that
touches the drag term at all.
