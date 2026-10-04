# Stanford AlN public record audit

Draft v0.1 · 3 October 2026 · AI checked; human review pending

We completed a bounded reconstruction of one paper and its supplement. For 16 fixed, deliberately selected questions, the main article supplies 6 answers at the requested level; the supplement resolves 7 more; 3 remain unresolved. The unresolved items concern independent deposition repeats at the best-result recipe, that specimen's exact recipe, and a complete campaign ledger.

**The useful first result is a source-linked account of what can be reconstructed and where reconstruction must stop.** This is evidence of our research process. It does not yet show that anyone makes better experiments with expanded records, or that the authors will find our work useful.

## Read the result

- [Three short human checks](human-review.md) — the next task for the user.
- [Question-by-question evidence table](audit-table.md) — every candidate answer and exact source location.
- [Machine-readable evidence](evidence.json) — object level, value type, units, scope limits, absence review and review log.
- [Frozen questions](questions.json) — wording and recovery criteria fixed before this structured extraction.
- [Source manifest](manifest.json) — source and question checksums, page map and extraction provenance.
- [Computed results](results.json) and [analysis script](analyze.py) — reproduce the counts.
- [Research task board source](plan-board.fragment.html) — snapshot of the conversation's interactive plan, saved as an HTML fragment; host styling and state APIs are supplied by the conversation interface.

Primary source: Vaziri et al., *AlN: An Engineered Thermal Material for 3D Integrated Circuits*, DOI [10.1002/adfm.202402662](https://doi.org/10.1002/adfm.202402662). [Stanford-hosted article and supplement](https://poplab.stanford.edu/pdfs/Vaziri-AlNthermalMaterial3DICs-afm25.pdf). The publisher PDF and extracted text are kept locally under `sources/` and excluded from Git. Use the source restoration step below on a fresh checkout.

## What the reconstruction supports

Campaign methods and measurement preparation are recoverable. Some published plots and captions explicitly connect measurements. However, an explicit link from the best thermal result back to a complete, exact recipe was not located in this packet. We therefore retain campaign descriptions, specimen families, plotted observations and reported outcomes at their own levels.

This distinction matters to a potential data product: finding numerical values is insufficient if the system joins unrelated values into an invented experiment. Our proposed product requirement is that every relationship have its own evidence, just as each value does. That is an inference from this audit, not a demonstrated customer requirement.

The first concrete extraction trap is Q11: a main-article figure inset supplies information absent from the extracted text. Visual checking prevents falsely assigning that information to the supplement. This is a limitation of the extraction method, not a deficiency in the paper.

## Supported outline and the missing connection

| Object | Recoverable description | Link limit |
|---|---|---|
| Deposition campaign | Method, equipment and explored parameter ranges | A campaign range is not an individual run recipe |
| Standard specimen family | Substrate stack and measurement preparation | Do not merge with the separately described in-plane membrane family |
| Measurement protocol | Thickness methods, transducer and spatial repetition | Multiple positions are not independent deposition runs |
| Published outcomes | Reported thermal maximum and within-figure measurement relationships | Matching values or colors do not establish cross-figure specimen identity |
| Full experimental history | No complete run-indexed ledger located in this packet | Existence, accessibility and additional value of lab records remain unknown |

We did not digitize plots or create synthetic run rows. `null` in the evidence file means unresolved, not zero. Inferred or assumed model inputs must not become experimental measurements.

## How this was checked

The fixed corpus contains 18 physical PDF pages: main article 1–8, supplement cover 9 and supplement content 10–18. The local PDF is preserved byte-for-byte. Text was extracted with Poppler; relevant rendered pages were inspected because text extraction omits image labels. A separate AI pass checked Q01–Q13; another searched for counterevidence to the three unresolved links and inspected all figure-bearing pages. These are machine checks, not independent human validation.

The question authors had already seen the paper. This is an information-location audit, not a blinded test or formal preregistration. The questions were selected for this case; their counts must not be presented as a percentage of the experiment reproduced, a representative estimate across papers, or a measure of equal scientific value.

The classification convention counts only explicit requested information as recovered. Broader related information remains in a separate field. For example, a temperature bound does not answer a question requesting a typical stabilized range. This convention does not affect the division between 6 already-supported, 7 newly-supported and 3 unresolved questions if related prose is instead labeled partial.

Absence was assessed only inside this packet, including figures and captions. We did not inspect all cited papers, theses, repositories or laboratory records. Some answers could exist elsewhere. The paper's data-availability statement is not evidence that a complete campaign archive exists or is shareable. Counterexamples to a sweeping “no linked data” claim are retained in `evidence.json`.

## Reproduce the descriptive counts

On a fresh checkout, install Poppler (`pdftotext`; the original version is recorded in `manifest.json`), then restore the source from the public URL:

```sh
python3 outputs/aln-public-record-audit/fetch_source.py
```

This requires network access only if no local PDF is present. Alternatively supply `--pdf /path/to/existing.pdf`. The script checks both PDF and extracted-text hashes before saving anything; a changed upstream source or incompatible extraction causes it to stop without replacing the packet.

Then, from the repository root:

```sh
python3 outputs/aln-public-record-audit/analyze.py
```

The script verifies the frozen-question and source hashes, validates row coverage and source-page boundaries, then regenerates `results.json` and `audit-table.md`. It computes counts from reviewed classifications; it does not independently determine whether those classifications are scientifically correct. No external packages or network access are required to reproduce the counts.

## What happens after your short review

First, incorporate corrections while preserving the original question set and recording revisions. Reviewing three selected examples will not verify the remaining rows. Every answer used in any later scored model comparison must receive its own human check; ambiguous rows stay unscored. No controlled model comparison has run.

For the startup hypothesis, the important next uncertainty remains whether a missing link would change a real experimental decision. More polished extraction alone cannot resolve it. After the public-source draft is reviewed, we can prepare a narrowly framed question about that uncertainty for a researcher; sending it requires the user's explicit instruction. Paid deposition is not required to finish this proof of work.

No laboratory experiment, purchase, reservation, dataset-access agreement or outreach occurred during this audit. The derived audit and task-board snapshot are prepared for Git on 4 October 2026; original publisher source copies remain local. Human review is still pending.
