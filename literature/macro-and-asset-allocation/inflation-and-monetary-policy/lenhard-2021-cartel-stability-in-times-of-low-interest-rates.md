# Cartel Stability in Times of Low Interest Rates

| | |
|---|---|
| **Authors** | Severin Lenhard (Universität Bern) |
| **Year** | 2021 (version of November 2021) |
| **Type** | Working paper (SSRN 4016978), 54pp including appendices. An industrial-organisation theory model plus an empirical test on 114 cartels convicted by the European Commission between 1999 and 2016 |
| **PDF** | Local copy only (SSRN working paper, no open licence) |
| **BibTeX** | `lenhard2021cartel` |
| **Status** | Reference: the introduction gives the argument; the "Empirical Exercise" section (logit and Weibull survival models, Tables 2–3) gives the test |

## What it is

A model of how the level of interest rates changes firms' incentive to keep to a cartel,
and a test of its prediction on European cartel data.

- **Two opposing effects.** Low rates make firms more patient: future cartel profits
  are discounted less, so cheating for a one-off gain is less attractive. That is the
  standard argument, and it says low rates stabilise cartels. The paper adds a second
  channel: firms need borrowed capital to produce, so low rates make it cheap for a
  cheater to expand output and take its rival's customers. That makes cheating *more*
  attractive.
- **The model.** Two firms sell differentiated goods to consumers spread along a line
  (a Hotelling set-up), finance production on the bond market, and play the game
  repeatedly. Stability is measured as the gap between the market discount factor
  1/(1+r) and the minimum discount factor at which collusion survives. The first effect
  dominates when rates are low, the second when they are higher, so stability is
  U-shaped in the interest rate (and falls again at very high rates, where each firm is
  simply a local monopolist).
- **Data.** The Hellwig–Hüschelrath dataset: 615 firms in 114 cartels convicted by the
  European Commission between 1999 and 2016 (16,431 firm-quarter observations), matched
  to the euro-area long-term government bond yield deflated by inflation, with GDP per
  capita and economic sentiment as controls.
- **Results.** A logit model of the quarterly probability that a cartel breaks up, with
  a squared interest-rate term, gives coefficients of the predicted sign; they are
  significant only when GDP per capita is controlled for. A Weibull survival model of
  how long each firm stays in its cartel also gives a U-shape, and the Lind–Mehlum
  test for a U-shape rejects the alternative at the 1% level. Stability is lowest at a
  real rate of about 3%, with a confidence interval from about 2% to over 7%.
- **Reconciling earlier studies.** Hellwig and Hüschelrath found that low rates
  *shortened* cartels in the EU data; Levenstein and Suslow found the opposite in US
  data. The model says either sign can appear depending on which effect dominates, and
  notes that Levenstein and Suslow control for firms' outside capital, which removes the
  investment channel.

## Why it's in the library

**It is an example of a monetary-policy side effect outside financial markets.** Most of
this section is about what rates do to asset prices. This paper argues that a long period
of very low rates may also change firm behaviour (here, collusion) and that the effect is
not monotonic, so "low rates do X" can flip sign as rates rise.

**The empirical support is weak, and the paper says so.** The sample contains only
cartels that were caught (a selection bias the author cannot correct), cartel durations
may be understated, the macro variables are aggregate rather than firm-level, and the
estimated turning point is imprecise. The U-shape is also not robust to the form of
competition: the author's footnote reports that with price competition and
differentiated products, stability falls monotonically with the rate. Read it as a
theoretical mechanism with suggestive evidence, not an established result.

## Links

- [[bianchi-buchner-tamoni-2021-bond-risk-premia-with-machine-learning]] — another paper in this section on how macro conditions and interest rates feed through to expected returns
- [[cole-2017-volatility-and-the-alchemy-of-risk]] — a different argument that a long period of low rates and low volatility changes behaviour in ways that store up risk
