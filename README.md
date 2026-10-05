# matsci-datanet

Working archive for a research line with one question behind it: **what would it take to get an "ImageNet moment" for experimental materials data?**

The short answer the work arrived at: you need two things, and the field is missing both. **Trusted labels** (measurements you can believe) and **a fair exam** (a benchmark that measures what it claims to). Most of the effort here goes into the second one, because it turns out to be the part a person can actually test from a desk.

**Status as of 22 Sep 2026:** research and planning are complete and have been audited. The first hands-on experiment has not started yet. Nothing here is published or peer reviewed. Several claims are explicitly marked unverified and should not be repeated without checking them first.

## Start here

For the **October 2026 AlN pilot**, start with the [preparation plan](outputs/aln-first-cycle-preparation/README.md). It indexes materials sourcing, Stanford registration, budget and schedule, experiment scope, inquiry drafts, and record templates. The earlier [Stanford public-record audit](outputs/aln-public-record-audit/README.md) provides the desk-research baseline. Real working records and private administration files are excluded from Git.

For the earlier materials-data research archive:

Open `page/big-picture.html` in a browser. It consolidates 16 research sessions and 10 earlier reports into one page and is the entry point to everything else.

Note: that file is at local Version 5. The published copy is still at Version 4.

## The reports

Ten earlier reports fed the big-picture page. They live as published pages on claude.ai and are **private to the author's account**, so the links below will not open for anyone else.

| Report | What it covers |
|---|---|
| [Materials Record Wall](https://claude.ai/artifact/6VxduLQ5tjW1KqRCgTMFGc) | What a single materials record actually contains, field by field |
| [Record Wall Debrief](https://claude.ai/artifact/GpSntEXMyK6hw9znGTvxAV) | What the record wall exercise changed |
| [Toward a Materials ImageNet](https://claude.ai/artifact/TP5hW9Hdh56scE6LQV2NwC) | The central argument about labels and exams |
| [Materials ImageNet Debrief](https://claude.ai/artifact/WLmZGmNU3k87iizhuMSbJs) | Self critique of that argument |
| [Discovered Materials Data Gaps](https://claude.ai/artifact/NA5N4ym6w5pQMF8NrJb8Wb) | Gap analysis of a public materials effort |
| [Discovered Materials Debrief](https://claude.ai/artifact/RHyiTnskp6Ad4dTCUamecJ) | Follow up to the above |
| [Thermoelectric Benchmark Spec](https://claude.ai/artifact/5RN8Fu5o9AFQgQw64x2mp6) | A proposed benchmark for thermoelectric property prediction |
| [DFT vs Experiment Debrief](https://claude.ai/artifact/5L2YyZsjLzVkhvjHr1cnm4) | Why computed and measured values disagree |
| [Recursion in Materials AI](https://claude.ai/artifact/GvUexcJ37BA6dh4JuyGCET) | Models trained on model output |
| [XRD Curation Experiments](https://claude.ai/artifact/4NnMSiSzcGE7qHTJj3dMgS) | Hands-on experiments on X-ray diffraction data |

## What is in here

| Directory | What it holds |
|---|---|
| [`outputs/aln-first-cycle-preparation/`](outputs/aln-first-cycle-preparation/README.md) | Current AlN pilot preparation: sourcing, access, scope, schedule, budget, inquiry drafts and blank record templates |
| [`outputs/aln-public-record-audit/`](outputs/aln-public-record-audit/README.md) | Reproducible audit of information in the Stanford AlN paper and supplement; human source review remains pending |
| `page/` | The consolidated big-picture page, its three earlier versions, and the Python scripts that edited it |
| `research/digests/` | 33 files compressing 16 research sessions (C01 to C16) and the 10 reports (R01 to R10) into a uniform template |
| `research/plan/` | The decision layer. Five independent proposal lenses, a merged shortlist, and eight adversarial checks against it |
| `research/eval-audit/` | A 12-agent audit of the plan against 56 published evaluation principles, with every ruling in `result.json` |
| `research/fact-checks/` | Five fact-checking passes over the page text |
| `research/synthesis/` | The narrative spine, a 50-entry gap ledger, and a glossary written for a newcomer |
| `src/` | The scripts that built the corpus from raw session transcripts |

## Jargon, once

- **XRD (X-ray diffraction)**: you shine X-rays at a powder and read the pattern of bounced beams to work out which compounds are in it.
- **Phase identification**: naming those compounds. The task this project mostly tests.
- **Thermoelectric**: a material that turns a temperature difference into voltage. The other candidate test bed.
- **Weighed mixtures**: powders made by weighing known ingredients, so the correct answer comes from a balance rather than from a person's judgment. This is the closest thing available to a reliable answer key.

## The next step

A one to two day test, not a build: mark 40 X-ray scans of weighed mixtures by hand, compare against what the software said, and sort every disagreement into one of four bins (naming artifact, real chemistry disagreement, suspect answer key, unsure).

Before any data is opened, about an hour of rules gets written down: what counts as a correct answer, what counts as two names meaning the same compound, and a threshold agreed in advance. The audit in `research/eval-audit/` is the check that this test is set up honestly, and it says to proceed.

## Honesty notes

- The answer key for weighed mixtures is **not certain**. It is known to within ingredient purity, weighing error, and whatever reacted during mixing.
- Several supporting figures were seen only as search snippets and are flagged as unverified in the notes. Open the sources before repeating them.
- Findings marked `[OPINION]` in the digests are judgments formed during the work, not established facts.

## Deliberately not in this repo

Raw session transcripts and the assembled corpus are excluded. They contain a pasted API key, personal names, contact addresses, and local machine paths. The digests in `research/digests/` are the provenance layer kept instead. See `.gitignore`.
