# Inefficient Bubbles and Efficient Drawdowns in Financial Markets

| | |
|---|---|
| **Authors** | Michael Schatz (ETH Zurich), Didier Sornette (ETH Zurich; Swiss Finance Institute) |
| **Year** | 2020 (International Journal of Theoretical and Applied Finance 23(7), 2050047); the copy here is Swiss Finance Institute Research Paper 18-49, revised 5 April 2020, 57pp |
| **Type** | Theory paper (mathematical finance) |
| **PDF** | Not hosted in this repository (SSRN/SFI working paper with no open licence) |
| **Find it** | [doi.org/10.1142/S0219024920500478](https://doi.org/10.1142/S0219024920500478) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Inefficient+Bubbles+and+Efficient+Drawdowns+in+Financial+Markets%22+Schatz) |
| **BibTeX** | `schatz2020bubbles` |
| **Status** | Reference: §1 and §3 (the framework and the two bubble types), §2.1 (critique of rational-expectations bubbles), §6 (detection) |

## What it is

A general framework that defines a bubble as a market failure followed by a crash, instead
of as a price above fundamental value in an efficient market.

- **The decomposition.** A price path is split into three parts: an explosive
  *pre-drawdown process* that violates market efficiency (no-arbitrage), a *random crash
  time*, and the *drawdown* path afterwards. The 1987 Dow is the illustration.
- **Type-I bubble.** Both pieces are inefficient on their own, but the full price process
  is efficient: abnormally high returns before the crash are fair compensation for crash
  risk. This is the Blanchard (1979) and Johansen–Ledoit–Sornette view; a rational investor
  who knows the true dynamics stays invested.
- **Type-II bubble.** The price is inefficient during the run-up and returns to efficient
  levels at the crash (heterogeneous beliefs, overconfidence, noise trading with limits to
  arbitrage). A rational investor who knew this would eventually get out.
- **Critique of rational-expectations bubbles.** In discrete infinite time a bubble needs an
  infinite horizon and payoff that can never be verified, so tests rest on extra
  assumptions. The paper argues the same problem carries over to the finite-horizon
  "strict local martingale" definition used in continuous time, and cites Sornette et al.
  (2018): across more than 40 bubbles, volatility was more often low than high before the
  crash, so exploding volatility is not a reliable signal.
- **Unification.** Many existing models fit the framework: the log-periodic JLS model,
  growth-then-decline drift models, heterogeneous-belief and synchronisation-risk models.

## Why it's in the library

**It reframes what a bubble test should look for.** Instead of overvaluation, which runs
into the joint-hypothesis problem, it points to observable signs of inefficiency during the
run-up: accelerating (faster than exponential) prices, rising volume, herding. Explosive
dynamics must end, so they can be called a bubble without a model of fundamentals.

**It is a framework, not a test.** There is no data and no out-of-sample evidence; the
detection example in §6 is a sketch. The authors' own empirical bubble work (the JLS model)
is cited rather than evaluated here.

## Links

- [[gurkaynak-2008-econometric-tests-of-asset-price-bubbles]] — the joint-hypothesis problem with rational-bubble tests that this framework is built to avoid
- [[bashchenko-marchal-2020-deep-learning-for-asset-bubbles-detection]] — the strict-local-martingale definition of a bubble, which this paper criticises
- [[sarkissian-2019-statistical-mechanics-of-price-stabilization-and-destabilization]] — another physics-style model of how calm markets tip into crashes
- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — what prices do after the drawdown
- [[chiarella-he-zwinkels-2014-heterogeneous-expectations-in-asset-pricing]] — an estimated model with positive feedback from trend-followers
- [[cividino-westphal-sornette-2023-multiasset-financial-bubbles-in-an-agent-based-model]] — the same group's agent-based model of how herding creates bubbles that spread across several stocks
