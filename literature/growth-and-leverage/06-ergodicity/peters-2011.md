# Optimal leverage from non-ergodicity

| | |
|---|---|
| **Authors** | Ole Peters |
| **Year** | 2011 |
| **Type** | Paper — *Quantitative Finance* 11(11) |
| **BibTeX** | `peters2011optimal` |
| **Status** | To read |

## Key takeaway

Derives optimal leverage from the observation that GBM is **non-ergodic**: the
time-average growth rate of a single trajectory, `mu - sigma^2/2`, is not the
ensemble-average growth rate `mu`, and no amount of averaging across parallel worlds tells
an investor living one trajectory what will happen to them. Optimising the time average
recovers `f* = mu/sigma^2` with no utility function invoked at all.

## Why it's here

**The sharpest available framing of the article's hook**, and the one that explains why
`E[W]` can compound while `W → 0`: those are the two different averages, and only one of
them is the investor's. Getting `f*` without assuming a utility function is a genuinely
elegant result regardless of what one makes of the wider programme.
