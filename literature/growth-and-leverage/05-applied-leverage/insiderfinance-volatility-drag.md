# Understanding Volatility Drag: A Stochastic Approach to Leveraged Investing

| | |
|---|---|
| **Author** | Not established — see below |
| **Year** | Not established |
| **Type** | Practitioner blog post — InsiderFinance Wire (Medium publication) |
| **Link** | https://wire.insiderfinance.io/understanding-volatility-drag-a-stochastic-approach-to-leveraged-investing-0561a623c00b |
| **BibTeX** | `insiderfinance_voldrag` |
| **Status** | **To read — not retrieved** |

## Key takeaway

**Unread.** The host returns HTTP 403 to automated requests, so nothing below is a summary
of the actual text. From the title, it covers the Itô route to `g = μ − σ²/2` and applies it
to leveraged products — the same ground as [[avellaneda-zhang-2010]] and
[[return-stacked-2025]], at lower authority than either.

## Why it's here

**As a sample of the popular explanation, not as a source.** The primaries for everything
this post can contain are already in this folder: [[shreve-2004]] for the derivation,
[[avellaneda-zhang-2010]] for the `½L(L−1)σ²T` leveraged-ETF result,
[[booth-fama-1992]] for the diversification side, [[kelly-1956]] and [[merton-1969]] for
sizing. Nothing here is load-bearing.

What a piece like this is *useful* for is calibration: it is roughly the version of the
argument a reader arrives with. [[return-stacked-2025]] earned its place by getting the
attribution right where most popular treatments get it wrong — worth checking whether this
one does the same, or whether it repeats the "volatility eats your returns" framing that
[[hughson-stutzer-yung-2006]] documents as standard practice and that is wrong for the
unlevered case.

## Where it's weak

⚠️ **I could not read it, and the note must not be cited.** 403 Forbidden on fetch. Author,
date and content are all unestablished. Status stays *To read*.

⚠️ **Tertiary by construction.** A blog restatement of a textbook result, in a folder that
already holds the textbook. Per house rule 5, if the result needed is `g = μ − σ²/2`,
derive it — it is four lines of Itô — rather than cite a Medium post for it.

⚠️ **Unrefereed, and the topic attracts a specific error.** Volatility drag is routinely
described as a "tax" that "erodes" capital. It is not: `E[S_T] = S₀e^{μT}` holds exactly,
and `−σ²/2` is a mean-median gap. A post reaching for "stochastic approach" in its title may
well get this right; many do not. **Verify before repeating anything from it.**

> **To upgrade this note:** paste the text in and it can be read properly, evaluated, and
> moved to *Read* — or dropped, if it turns out to add nothing the primaries do not.
