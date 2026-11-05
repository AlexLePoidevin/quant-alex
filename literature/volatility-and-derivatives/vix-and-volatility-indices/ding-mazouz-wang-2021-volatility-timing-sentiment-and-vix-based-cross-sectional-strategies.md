# Volatility Timing, Sentiment, and the Short-Term Profitability of VIX-Based Cross-Sectional Trading Strategies

| | |
|---|---|
| **Authors** | Wenjie Ding, Khelifa Mazouz and Qingwei Wang (Cardiff Business School; ZEW) |
| **Year** | 2021 (published version); the copy here is an undated working paper |
| **Type** | Journal article, *Journal of Empirical Finance* 63, 42–56 (2021). Data: US common stocks (CRSP/Compustat) and daily VIX, roughly 1990–2018 |
| **PDF** | Local copy only (working paper of an Elsevier article) |
| **BibTeX** | `ding2021vixtiming` |
| **Status** | Reference: Tables 1–3 and 5 carry the results |

## What it is

A study that treats the VIX as a daily investor-sentiment gauge and uses it to switch
between two kinds of stock: those most exposed to sentiment and those least exposed.

- **Which stocks are sentiment-prone.** Following Baker and Wurgler, decile portfolios
  are sorted on ten characteristics: size, age, volatility, profitability, dividends,
  tangibility, R&D, book-to-market, external financing and sales growth. Small, young,
  volatile, unprofitable, non-paying firms count as sentiment-prone; their opposites as
  sentiment-immune.
- **The short-run sign is negative.** Regressing next-day returns of the prone-minus-immune
  spread on yesterday's VIX gives negative coefficients, significant for 6 of 16 spreads
  overall and 11 of 16 when the VIX is low. Low VIX (high sentiment) is followed by
  sentiment-prone stocks doing better the next day. The authors read this as momentum
  from delayed arbitrage (Abreu and Brunnermeier): arbitrageurs ride mispricing until
  enough of them act together.
- **The switching rule.** Hold the sentiment-immune decile when VIX is at least 10% above
  its average of the previous 25 days; otherwise hold the sentiment-prone decile. No
  shorting is needed.
- **Reported results.** Annual returns of about 21% to 40% against −2% to 26% for always
  holding the long-short spread, with Sharpe ratios of 1.1 to 2.7 (highest for switching
  between the smallest and largest size deciles). Alphas stay positive after CAPM,
  Fama–French, momentum, reversal, mispricing and q-factor adjustments. Break-even
  costs exceed 50 bp per trade, and the size strategy trades about every eight days.

## Why it's in the library

**It reconciles two facts about the VIX.** A high VIX predicts higher returns over months
(fear is paid for), but this paper finds the opposite sign over one day, concentrated in
the stocks most driven by sentiment. Both can hold if sentiment pushes prices further
before they correct.

**The headline returns need heavy discounting.** The best strategies switch daily between
equal-weighted extreme deciles, where the smallest stocks have stale prices and bid-ask
bounce that inflate next-day predictability. The signal threshold and the 25-day window
were also looked at among several alternatives. The paper's own numbers move between
sections: the introduction gives 22–42% returns, Table 2 gives 21–40%. The value-weighted
version is weaker, and the market-timing tests show the size strategy is largely timing
the market. Treat the sign of the effect as the finding, not the size.

## Links

- [[barberis-shleifer-wurgler-2005]] — sentiment and comovement: stocks that share
  investors move together beyond fundamentals
- [[fama-french-2015]] — the five-factor model used to risk-adjust the strategy
- [[carhart-1997]] — the momentum factor added as a control
- [[fassas-hourvouliades-2019-vix-futures-as-a-market-timing-indicator]] — a VIX-based
  signal for the index rather than the cross-section
- [[osterrieder-et-al-2019-the-vix-volatility-index-a-very-thorough-look]] — what the VIX
  actually measures
