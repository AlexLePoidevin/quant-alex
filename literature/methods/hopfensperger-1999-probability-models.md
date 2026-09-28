# Probability Models (Data-Driven Mathematics)

| | |
|---|---|
| **Authors** | Patrick Hopfensperger, Henry Kranendonk, Richard L. Scheaffer |
| **Year** | 1999 |
| **Type** | **High-school curriculum module** — Dale Seymour / Addison Wesley Longman, 96pp |
| **Origin** | American Statistical Association, "A Data-Driven Curriculum Strand for High School", NSF Grant #MDR-9054648 |
| **PDF** | `hopfensperger-1999-probability-models.pdf` (in this folder) |
| **BibTeX** | `hopfensperger1999probmodels` |
| **Source** | [amstat.org](https://www.amstat.org/docs/default-source/amstat-documents/probabilitymodels.pdf) |
| **Status** | Reference — **pedagogy, not rigour** |

## What it is

**This is not a university text and should not be cited as one.** It is a 96-page
advanced-algebra teaching module with activity sheets, quizzes and tests, written for
high-school classrooms and field-tested in them. It contains no measure theory, no
convergence modes, no Berry–Esseen, and no proofs.

Nine lessons in three units:

**Unit I — Random variables and their expected values**
1. Probability and random variables
2. The mean as an expected value
3. Expected value of a function of a random variable
4. The standard deviation as an expected value

**Unit II — Sampling distributions of means and proportions**
5. The distribution of a sample mean
6. The normal distribution
7. The distribution of a sample proportion

**Unit III — Two useful distributions**
8. The binomial distribution
9. The geometric distribution

## Why it's in the library

**It is a tested blueprint for an argument this publication is about to make.** Read the
unit structure as an arc rather than a syllabus and it says: *a random variable is a
function with a distribution* → *its centre and spread are expectations* → **the mean of a
sample is itself a random variable with its own distribution** → *that distribution is
normal*. That is Article 1 of the foundations series almost exactly — T1 then T2 — and it
is the sequence rather than the content that is worth having. Somebody built this ordering,
put it in front of students, and revised it.

**Richard Scheaffer co-wrote this and the university text.** He is the third author of
[[wackerly-2008-mathematical-statistics]], was president of the American Statistical
Association, and spent a career on statistics education. That matters here: the
simplifications in this module are not the compromises of someone who does not know the
rigorous version — they are deliberate choices by the person who wrote it. When this book
drops something, the omission carries information about what is load-bearing for
understanding and what is load-bearing only for proof.

**Its method is the same one the series is committed to.** "Data-driven mathematics" means
every concept is introduced from real data rather than urns and dice. The foundations
roadmap independently arrived at the same rule — *a unit that ends on a coin flip should be
cut* — and this module is 96 pages of worked evidence that teaching probability from actual
data is possible at a far lower level of preparation than a quant audience brings.

**Lesson 5 is the one to read.** "The distribution of a sample mean" is the single hardest
idea to land in the whole block — the move from *a number computed from data* to *a
realisation of a random variable* — and this is a treatment of it that works on
sixteen-year-olds.

## What it will not do

It will not support the formal register the foundations series has committed to. It states
that sample means are approximately normal; it does not state the hypotheses under which
that is true, the mode of convergence, or the rate. For those, use
[[evans-rosenthal-2009-probability-and-statistics]] chapter 4 and
[[wackerly-2008-mathematical-statistics]] chapter 7. **Use this one for sequencing and
anchors, never for claims.**

## Links

- [[wackerly-2008-mathematical-statistics]] — same author (Scheaffer), the rigorous version
  of the same sequence
- [[evans-rosenthal-2009-probability-and-statistics]] — chapter 4 is what lessons 5–6 are a
  simplification of
