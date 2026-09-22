# Optimization of Conditional Value-at-Risk

| | |
|---|---|
| **Authors** | R. Tyrrell Rockafellar; Stanislav Uryasev |
| **Year** | 2000 |
| **Type** | Paper — *Journal of Risk* 2(3) |
| **BibTeX** | `rockafellar2000optimization` |
| **Status** | To read |

## Key takeaway

CVaR (expected shortfall) can be minimised **without first computing VaR**, via an
auxiliary function that is convex in the decision variables. With scenarios the problem
becomes a linear program, so CVaR constraints can be carried inside an ordinary portfolio
optimisation at no real cost.

## Why it's here

The reference for turning "cap the tail" from a sentiment into a constraint. For the
single-leverage case there is a useful simplification worth stating explicitly: under
Gaussian returns `CVaR_alpha(f)` is **linear in `f`**, so a CVaR limit becomes a leverage
cap and the constrained optimum is just `min(f*, f_CVaR)` — a clean kink on the frontier.
Under empirical returns the cap binds considerably earlier, which is the point.
