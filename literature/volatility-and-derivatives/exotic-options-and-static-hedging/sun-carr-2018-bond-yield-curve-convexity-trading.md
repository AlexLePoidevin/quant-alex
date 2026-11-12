# Bond Yield Curve Convexity Trading

| | |
|---|---|
| **Authors** | Jian Sun (Fudan University), Peter Carr (NYU Tandon) |
| **Year** | 2018 (dated 16 August 2018) |
| **Type** | Working paper, SSRN 3232697, 10pp |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [ssrn.com](https://ssrn.com/abstract=3232697) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Bond+Yield+Curve+Convexity+Trading%22+Sun) |
| **BibTeX** | `sun2018convexity` |
| **Status** | Reference: §1 (the three-bond argument and Theorem 1) is the whole result |

## What it is

A short no-arbitrage argument for why the yield curve is usually concave (it flattens
as maturity grows) instead of convex. The argument uses a three-bond butterfly, not a
term-structure model.

- **The trade.** Buy short- and long-maturity zero-coupon bonds and sell an
  intermediate one (maturities T1 < T2 < T3). The weights are T3 − T2, T3 − T1 and
  T2 − T1. That makes the position cost nothing and have zero duration.
- **It is long convexity.** If all yields move by the same amount, the position's
  value after the move is never negative. This follows from the exponential function
  being convex (Jensen's inequality), whatever the size or sign of the move. A
  duration-neutral butterfly gains from any parallel shift.
- **Carry decides whether it is an arbitrage.** As time passes, each bond earns its
  own yield. If the three yields are convex in maturity, the butterfly's carry is also
  non-negative. It then gains from moves and from time and never loses, which is an
  arbitrage. So, under parallel moves, yields cannot be convex in maturity. They must
  be concave: the belly of the curve has to yield more than the straight line between
  the wings, which pays for the convexity the butterfly holds.
- **Non-parallel moves.** If yields move in fixed proportions l1, l2, l3 instead of
  equally, the same argument applies to the points (l_i T_i, y_i) instead of (T_i, y_i).
- **What is claimed but not shown.** The summary says the same conclusion holds for
  swap curves "with much more careful derivation". That derivation is not in the
  paper. The theorem statements are also inconsistent about wording: Theorem 1 says
  convex yields admit an arbitrage, and Theorem 2 says concave points do. The proof of
  Theorem 2 uses convexity, so "concave" in its statement looks like a typo.

## Why it's in the library

**It is the bond-market version of "convexity has a price".** Every option-pricing
argument in this section says a position that gains from movement in either direction
must pay for it somewhere: in time decay for an option, in carry here. The concave yield
curve is the market charging for the convexity of long-dated bonds. That links curve
shape to rate volatility, as Litterman, Scheinkman and Weiss (1991) found empirically.

**It is a static argument.** The result needs no model of how rates move, only the
assumption of parallel (or proportional) shifts. That is the same style as static
replication of options from a strip of vanillas, which is why it is filed with the
static-hedging papers.

**The assumption is the weak point.** Real curve moves are not parallel. Level, slope
and curvature move separately, and the paper only extends the result to fixed
proportional moves. Read it as the reason concavity is the normal shape, not as a
trading rule. Butterfly P&L in practice depends on curvature changes, which the
argument rules out.

## Links

- [[carr-lorig-2015-robust-replication-of-barrier-style-claims]] — another Carr paper that gets pricing from static positions and minimal assumptions on the dynamics
- [[rbc-gam-2014-optionality-understanding-callable-bonds]] — convexity and optionality in bonds from the investor side
