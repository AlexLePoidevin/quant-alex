# The Influence of Ergodicity on Risk Affinity of Timed and Non-Timed Respondents

| | |
|---|---|
| **Authors** | Arne Vanhoyweghen; Brecht Verbeken; Cathy Macharis; Vincent Ginis (VUB) |
| **Year** | 2022 |
| **Type** | Paper — *Scientific Reports* 12. Open access |
| **DOI** | [10.1038/s41598-022-07613-6](https://doi.org/10.1038/s41598-022-07613-6) |
| **PDF** | `vanhoyweghen-et-al-2022.pdf` (in this folder) |
| **BibTeX** | `vanhoyweghen2022influence` |
| **Status** | Read |

## Key takeaway

**The experimental leg this folder was missing.** Everything else here is either advocacy
([[peters-2011]], [[peters-2019]]) or rebuttal ([[doctor-wakker-wang-2020]]); this is an
attempt to *measure* whether people behave as though they optimise a time-average growth
rate rather than an expected value.

Design: respondents repeatedly choose between two stochastic bets, trying to grow a starting
capital of 1,000. Two dynamics are run — **additive**, where ergodicity is not broken and the
two averages agree, and **multiplicative**, where they diverge. Each is run with and without
**time pressure**, on the dual-process premise that pressured choices reveal intuition.

The result is a clean interaction rather than a main effect, which is what makes it
interesting:

- In the **additive (ergodic)** setting, time pressure makes **no difference**. Nothing to
  detect, and nothing is detected — a useful internal control.
- In the **multiplicative (non-ergodic)** setting, the timed group is **significantly more
  likely to pick the growth-rate-optimal bet** (P = 0.042 in the n = 81 sample), and is
  significantly more risk-averse than the control (P = 7 × 10⁻⁵).

The authors' reading: choices that look "irrational" by expected value are closer to optimal
once you ask what happens to *one* participant over *many* rounds.

## Why it's here

It is the only piece in `06-ergodicity` that puts a number on the behavioural claim, and the
additive-versus-multiplicative contrast is the right experimental shape — the ergodic arm is
a built-in placebo. Two samples: n = 18 with 600 choices each, and n = 81 with 80 choices.

## Where it's weak

⚠️ **The incentive is a tournament, and a tournament is its own non-linearity.** Only the
**six** respondents with the highest end-capital received a cash prize. Under
winner-takes-the-top-six, maximising expected log wealth is *not* the optimal strategy —
you should take extra risk to raise the probability of finishing in the top six. So the
payoff structure rewards neither expected-value nor growth-rate optimisation, but variance.

In fairness, this cuts *toward* the null and not toward the finding: the tournament pushes
everyone to be more risk-seeking, while the reported effect is that timed respondents were
more risk-**averse**. The result survives a bias working against it, which strengthens it.
What it does contaminate is the *absolute* level — you cannot read "how growth-optimal were
they" from this design, only the between-group difference.

⚠️ **P = 0.042 on n = 81, split two ways.** The headline is barely inside the conventional
threshold, on roughly forty per arm, across two dynamics and two experiments. Any
multiplicity correction takes it out. The n = 18 study is a pilot, not evidence.

⚠️ **Time pressure is not a clean instrument for "intuition."** The inference rests on
dual-process theory, which is itself contested. Pressure also produces noise, fatigue and
satisficing, any of which could shift choices toward the safer bet with no growth-rate
reasoning involved. "More risk-averse under pressure" has a much duller explanation
available, and the paper cannot exclude it.

⚠️ **Descriptive, not normative — and this is the one that matters for how this folder uses
it.** Even taken at face value, the paper says people *behave* in a way that tracks growth
rates. It says nothing about whether they *should*. The open question posed by
[[samuelson-1979]] and given a closed form by [[merton-1969]] — which criterion ought to be
optimised, and at what risk aversion — is untouched by any amount of evidence about what
subjects do under time pressure. Do not let a behavioural result be read as settling a
decision-theoretic one.
