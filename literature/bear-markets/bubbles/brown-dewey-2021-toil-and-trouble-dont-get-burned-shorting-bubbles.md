# Toil and Trouble, Don't Get Burned Shorting Bubbles

| | |
|---|---|
| **Authors** | Aaron Brown (New York University), Richard Dewey (Royal Bridge Capital) |
| **Year** | 2021 (version dated 11 February 2021) |
| **Type** | Working paper, SSRN 3782759, 11pp. A practitioner case study built from interviews, traders' internal research and press accounts |
| **PDF** | Not hosted in this repository (SSRN download, no open licence) |
| **Find it** | [doi.org/10.2139/ssrn.3782759](https://doi.org/10.2139/ssrn.3782759) · or [search Google Scholar](https://scholar.google.com/scholar?q=%22Toil+and+Trouble%2C+Don%27t+Get+Burned+Shorting+Bubbles%22+Brown) |
| **BibTeX** | `brown2021shorting` |
| **Status** | Reference: §4 (the scenario model and the latent risks), §5 (the alternative trades) and §7 (why short sellers did not stop the bubble) carry the argument |

## What it is

A look back, ten years on, at the "short subprime" trade of 2005–2008: buying credit default
swaps (CDS) on pools of subprime mortgages. The question is why so few well-informed
traders took a trade that turned out to pay about ten times the money risked, and why the
ones who did take it did not stop the bubble. The authors say some of the trading history
comes from conversations and press reports they could not verify.

- **One trader's model.** A macro fund trader who looked at the trade in 2006 put the
  carrying cost at 1.5% to 8% a year depending on the securities shorted, and laid out four
  spread scenarios: tighten to zero (10% probability, −6%), tighten by half (40%, −3%),
  unchanged, and sell off 15–30 points (50%, +22.5%). He judged the expected value very
  attractive and still passed, for lack of expertise in the securities. The exhibit as
  printed does not add up: the "unchanged" row has zero probability next to a +20% P&L, and
  50% × 22.5% is 11.25%, not the 12.5% shown.
- **The risks that kept traders out.**
  - *Timing.* 2004-vintage subprime eventually defaulted at 12%, the 2005 vintage at 30% and
    the 2006 vintage at 60%, so waiting improved the bet. Nobody knew when defaults would
    start, and five-year CDS were too long to carry for most funds.
  - *Negative carry.* Premiums had to be paid every month or quarter, at a time when
    falling volatility had already been draining anyone who was long volatility.
  - *Government rescue.* A bailout of homeowners or banks could have saved the bonds.
  - *Complexity.* Some investors concluded that even the banks and rating agencies did not
    understand the securities.
  - *The instrument.* CDS are illiquid over-the-counter contracts paid on dealer marks.
    Long after the trade was clearly winning, dealers' marks still required the shorts to
    post more collateral. And the winnings were owed by banks that might fail in exactly the
    scenario being bet on.
- **Why the trade appeals.** It turns a small stake into a large payoff. The authors use a
  racing example: a 30-to-1 horse with a 10% chance and a 1.2-to-1 favourite with a 90%
  chance have the same expected value, but the long shot's standard deviation per $1 bet is
  $9 against $0.36. People prefer the positively skewed bet, which is the favourite–long-shot
  bias.
- **Why it paid more than expected.** "Performance convexity": once defaults rose, almost no
  account was allowed to buy downgraded subprime, so losses compounded. "Credit convexity":
  losses jumped non-linearly once tranches were breached. Some shorts also chose which
  mortgages went into the pools they insured.
- **Other ways to express the same view.** Magnetar reportedly bought high-yielding CDO
  equity tranches and used the carry to pay for protection on the AAA tranches, a
  positive-carry structure. Others waited and bought the wreckage: the AAA ABX.HE index lost
  70% from 2005 to 2009 and gained 120% from 2009 to 2013. The paper cites a Soros team
  reportedly earning over 30% a year on about $1bn, PIMCO's Income Fund growing from $223m
  to $121bn (2009–2018, about 12% a year), Tepper's 120% in 2009 on bank stocks, and rates
  options bought ahead of Fed cuts. Before the crisis Lehman CDS cost 28bp, Bear Stearns
  30bp and AIG 22bp.
- **Afterwards.** The traders who shorted subprime have had mixed records since. Those who
  bought after the crash have done better.
- **Why shorts did not stop the bubble.** One illiquid, one-off bet does not change the
  marginal price once the market absorbs it. Regulation and ratings kept supplying buyers.
  And bubbles have many causes, so leaning against one is expensive and uncertain.

## Why it's in the library

**Being right about a crash is not the same as making money from it.** The paper's point is
trade construction: time horizon, carry, liquidity, sizing and who pays you if you win. The
same carry problem shows up for any crash hedge, from long VIX positions to rolled index
puts.

**Buying after the crash can beat shorting before it.** The cleanest gains in the subprime
story came from buying distressed assets in 2009. That links the paper to the evidence on
what markets do after very large falls.

**It is an essay, not a study.** The evidence is a handful of famous traders, chosen with
hindsight, with returns taken from interviews and press reports. The one quantitative
exhibit has arithmetic errors. Read it for the list of risks, not for the numbers.

## Links

- [[goetzmann-kim-2018-negative-bubbles-what-happens-after-a-crash]] — what markets do after
  a fall of 50% or more: the evidence behind "buy after the crash"
- [[johannsen-2016-dead-cat-bounce]] — a model of the rebound after a bubble bursts
- [[jarrow-1992-market-manipulation-bubbles-corners-and-short-squeezes]] — why a large trader
  can keep prices away from value: corners, squeezes and manipulated bubbles
- [[bashchenko-marchal-2020-deep-learning-for-asset-bubbles-detection]] — an attempt to spot
  bubbles before they burst, the step this paper says is only half the problem
- [[mackenzie-spears-2014-formula-that-killed-wall-street]] — the Gaussian copula used to
  price the CDO tranches at the centre of this trade
- [[szado-2020-portfolio-diversification-potential-of-long-vix-futures-and-options]] — the
  carrying cost of a crash hedge, measured for long VIX positions
- [[ambrus-capital-2025-marketing-vs-math-solutions-based-vs-alpha-focused-tail-risk-hedging]]
  — why rule-based crash hedges bleed between crises
- [[quinn-turner-2025-who-wins-and-loses-in-a-bubble-british-bicycle-mania]] — the long side of a historical mania: who sold before the crash and who was left holding
