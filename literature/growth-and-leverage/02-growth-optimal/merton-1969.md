# Lifetime Portfolio Selection under Uncertainty: The Continuous-Time Case

| | |
|---|---|
| **Authors** | Robert C. Merton |
| **Year** | 1969 |
| **Type** | Paper — *Review of Economics and Statistics* 51(3) |
| **BibTeX** | `merton1969lifetime` |
| **Status** | To read |

## Key takeaway

Continuous-time portfolio choice for an investor with CRRA utility. The optimal risky
fraction is **constant through time** and equal to

```
f* = (mu - r) / (gamma * sigma^2)
```

where `gamma` is relative risk aversion. Kelly is the special case `gamma = 1` (log
utility). Half-Kelly is `gamma = 2`.

## Why it's here

**The generalisation most treatments of Kelly omit, and it changes the argument.**
Fractional Kelly is usually presented as a prudential fudge — "full Kelly is too wild, so
halve it". Merton shows it is the exact solution for an investor who is simply more
risk-averse than log. That reframes the practical advice as a statement about preferences
with a closed form, instead of a rule of thumb. Read before writing anything about
fractional Kelly.
