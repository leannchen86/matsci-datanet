# matsci-datanet

Working archive for a research line with one question behind it: **what would it take to get an "ImageNet moment" for experimental materials data?**

The short answer the work arrived at: you need two things, and the field is missing both. **Trusted labels** (measurements you can believe) and **a fair exam** (a benchmark that measures what it claims to). Most of the effort here goes into the second one, because it turns out to be the part a person can actually test from a desk.

**Status as of 12 Oct 2026:** thermal-paste practice batch B001 has been prepared and its selected records/photos published in this repository. External thermal results are not yet recorded. Copper, wafer-film and diamond experiments are being compared as possible next projects; access and dates are not secured. Research judgments and unverified claims remain labeled in the supporting files.

## Start here

**Start with the [materials experiment and laboratory access map](outputs/MATERIALS_EXPERIMENT_MAP.md)** (12 Oct 2026) for the big picture: existing-material experiments, copper and wafer films, diamond, available facilities and unresolved access. It organizes the choices without starting every project.

For the next paste submission, use the [completion checklist](outputs/thermal-paste-first-cycle/CHECKLIST.md) and [run card](outputs/thermal-paste-first-cycle/PASTE_TO_LAB_RUN_CARD.md). [PLAN.md](PLAN.md) holds the broader experimental-data plan. The unit of data is a whole experimental trajectory, logged with the tool in [trajectory/](trajectory/README.md); [B001's public release](trajectory/releases/B001/README.md) preserves the completed practice history.

The paused **AlN pilot** has a [preparation plan](outputs/aln-first-cycle-preparation/README.md) indexing sourcing, Stanford registration, budget, scope, inquiry drafts and record templates. Its original schedule is historical. The [Stanford public-record audit](outputs/aln-public-record-audit/README.md) provides the desk-research baseline. Private administration and unapproved raw records remain excluded from Git; the selected B001 release is an explicitly authorized exception for experimental records.

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
| [`outputs/MATERIALS_EXPERIMENT_MAP.md`](outputs/MATERIALS_EXPERIMENT_MAP.md) | Current overview of materials, experiments, goals and practical paid access routes |
| [`outputs/thermal-paste-first-cycle/`](outputs/thermal-paste-first-cycle/CHECKLIST.md) | Paste submission checklist, run card, sourcing history and B001 process review |
| [`outputs/copper-access-review/`](outputs/copper-access-review/README.md) | Copper, flexible labs, CVD and diamond access research |
| [`trajectory/`](trajectory/README.md) | Experimental-history logging and authorized public releases |
| [`outputs/aln-first-cycle-preparation/`](outputs/aln-first-cycle-preparation/README.md) | Paused AlN preparation: sourcing, access, scope, historical schedule, budget and templates |
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

## Earlier desk research next step

The following XRD task belongs to the earlier research archive. The current physical-experiment choices and paste submission are linked above.

A one to two day test, not a build: mark 40 X-ray scans of weighed mixtures by hand, compare against what the software said, and sort every disagreement into one of four bins (naming artifact, real chemistry disagreement, suspect answer key, unsure).

Before any data is opened, about an hour of rules gets written down: what counts as a correct answer, what counts as two names meaning the same compound, and a threshold agreed in advance. The audit in `research/eval-audit/` is the check that this test is set up honestly, and it says to proceed.

## Honesty notes

- The answer key for weighed mixtures is **not certain**. It is known to within ingredient purity, weighing error, and whatever reacted during mixing.
- Several supporting figures were seen only as search snippets and are flagged as unverified in the notes. Open the sources before repeating them.
- Findings marked `[OPINION]` in the digests are judgments formed during the work, not established facts.

## Deliberately not in this repo

Raw session transcripts and the assembled corpus are excluded. They contain a pasted API key, personal names, contact addresses, and local machine paths. The digests in `research/digests/` are the provenance layer kept instead. See `.gitignore`.
