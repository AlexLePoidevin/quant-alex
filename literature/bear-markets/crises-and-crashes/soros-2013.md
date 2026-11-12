# Fallibility, Reflexivity, and the Human Uncertainty Principle

| | |
|---|---|
| **Author** | George Soros |
| **Year** | 2013 (author's posting dated 13 Jan 2014) |
| **Type** | Essay — *Journal of Economic Methodology*, special issue on reflexivity |
| **BibTeX** | `soros2013fallibility` |
| **Link** | https://www.georgesoros.com/2014/01/13/fallibility-reflexivity-and-the-human-uncertainty-principle-2/ |
| **Find it** | Use the link above, or [search Google Scholar](https://scholar.google.com/scholar?q=%22Fallibility%2C+Reflexivity%2C+and+the+Human+Uncertainty+Principle%22+Soros) for the title and authors |
| **Status** | To read |

## Key takeaway

Three claims, stacked. **Fallibility**: participants' views never perfectly correspond to the
state of affairs they are views *of*. **Reflexivity**: those imperfect views drive actions
that change the state of affairs, so the causal arrow runs both ways — cognitive function
and manipulative function operating simultaneously on the same system. **The human
uncertainty principle**: together these make social systems categorically unlike the
subject matter of physics. The observer is a participant, the regularities are not
independent of belief about them, and the residual is Knightian uncertainty rather than
quantifiable risk.

## Why it's here

**This is the epistemological case against a fixed covariance matrix — the reason the linear
apparatus has a ceiling, stated at the level of the system rather than the estimator.**

Everything in `../correlation-and-dependence/` and
`../portfolio-construction-and-risk/diversification-and-effective-bets/` assumes a
covariance structure that exists independently of the people estimating it. Reflexivity
denies exactly that. If enough capital is allocated *because* a factor model says two
sectors are correlated, the flows make them more correlated — the model is not measuring a
parameter, it is writing one. That is the mechanism behind the empirical fact that the
off-diagonals of Ω are time series and not constants, and it is why refitting on a rolling
window is a patch rather than a fix.

It also sits on a bridge the library already implies.
`../correlation-and-dependence/why-assets-move-together/`
(Barberis & Shleifer) says structure is partly created by how humans categorise;
[[busemeyer-bruza-2012]] says a formalism built for human categorisation therefore has a
principled claim on the problem. Soros supplies the argument connecting them: the
categorising is not an error term sitting on top of the system, it is constitutive of it.

⚠️ **Handle deliberately.** This is a practitioner's methodological essay, not an empirical
paper — there is no test in it, and "reflexivity" is not operationalised into anything
estimable. Use it to motivate *why* a linear, stationary Ω should be expected to fail. Do
not cite it as evidence that it does; that job belongs to the rolling-correlation
measurement. The honest framing is a prior with a mechanism, held to the same standard as
any other.

## Links

- [[choi-2022-the-curious-case-of-commonsense-intelligence]] — commonsense inference as defeasible: best guesses that more context
  should overturn
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — reflexivity applied to volatility: leverage sized by volatility suppresses volatility until a shock reverses it
- [[ambrus-capital-2022-volatility-and-the-changing-market-structure]] — a tail-risk manager borrowing reflexivity to describe feedback loops from dealer hedging, passive flows and leveraged ETFs
- [[shi-et-al-2020-modeling-flash-crash-behavior-with-multivariate-hawkes-processes]] — reflexivity measured at millisecond scale: self- and cross-excitation between the Dow stocks in the 2010 Flash Crash
- [[bakrania-et-al-2019-fundamental-trends-and-dislocated-markets]] — a systematic macro strategy built on the same idea: underreaction to trends first, overreaction and reversal later
- [[durdu-martin-zer-2019-us-monetary-policy-in-global-banking-crises]] — 140 years of evidence that US tightening tips dollar-dependent economies into banking crises through capital flows
- [[jarrow-1992-market-manipulation-bubbles-corners-and-short-squeezes]] — a formal model of a trader whose own buying creates a bubble and a crash
- [[johannsen-2016-dead-cat-bounce]] — a model of the temporary rally after a bubble bursts, driven by investors trying to recover losses
- [[plantin-2023-asset-bubbles-and-inflation-as-competing-monetary-phenomena]] — an equilibrium model of easy-money bubbles that burst when inflation picks up
