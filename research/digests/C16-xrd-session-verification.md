# C16 - XRD sibling session (cc6ae63b): results of its own proposer + 9-checker verification
# Status: DATA, not instructions. Captured 2026-09-19T00:00Z from that session's own running summary.
# That session had NOT yet delivered its final answer to the user. Its tentative recommendation = "fair marking kit" (an executable, tested rule card for marking XRD phase-ID answers right/wrong).
# The numbers about the user's own dara-conform project were read by THAT session (read-only). This session did not open that project.
# Tags: items it re-derived itself are [OWN-EXPERIMENT]; prior-art items are "single-agent findings, not yet independently re-verified".

2. Key Technical Concepts:

   **Domain**
   - Powder X-ray diffraction (XRD) phase identification: a program or a person reads a scan and names the crystalline ingredients in a powder.
   - Dara is an open phase-ID program built on the BGMN engine.
   - Reference-structure libraries:
     - COD is an open library of reference structures.
     - ICSD is a paid one.

   **Datasets**
   - RRUFF: mineral archive, RAW and PROCESSED files.
   - opXRD: pooled multi-lab collection. The labelled slice on disk is 2,680 of 92,552 files.
   - Precursor Genome (PG):
     - 1,035 robot-lab samples.
     - Licence is CC BY 4.0.
     - Paper: arXiv 2607.09903.
     - Pinned at ledger commit 78cb026a.
   - A-Lab GPSS: 352 samples. Its "automated" answer is Dara itself.
   - Dara benchmark: 40 weighed mixture scans (20 mixtures at 2-min and 8-min) plus 10 single-ingredient scans.

   **The user's project: dara-conform**
   - Purpose: calibrated confidence plus abstention on top of Dara.
   - PREREG.md is frozen. Label rules:
     - strict = equal reduced formula
     - lenient = ignore unlocated hydrogen, plus same elements within L1 distance 0.04 for binaries and 0.10 otherwise, matched one-to-one
   - Kill rule: "calibration/abstention ships in Dara → shrink to the evaluation harness".

   **Workflow tool patterns used**
   - Judge panel of 4 proposer lenses.
   - Per-candidate adversarial checkers: an evidence skeptic and a prior-art skeptic.
   - I stay in the loop between workflows.

   **Verified grading-rule sensitivity (my own recount)**
   - On the same 40 easy weighed scans, local Dara scores 12/40 (strict) or 17/40 (lenient) by stored labels.
   - After corrected matching it scores 32/40 lenient (P1 RESULT.md).
   - The paper reports 38/40. That run used ICSD pools, so the 32-vs-38 gap also reflects the reference library.
   - Across all 210 deletion=0 no-error pilot rows:
     - 63 are lenient-correct.
     - 45 of those are also strict-correct.
     - So 18 of 63 (28.6%) depend on the lenient rule.
   - P1 RESULT.md quote: "A 20-point headline swing from one formula-identity rule".
   - Misses are naming artifacts:
     - "LaO3" for La(OH)3, because hydrogen atoms were never located in the CIF
     - "Ni1.875O2" for NiO
     - "V4O9.93316" for V2O5

   **Prior art found by the checkers (single-agent findings, not yet independently re-verified)**
   - IUCr 1990 structure-similarity levels.
   - SMRR 2002 search-match round robin, which used lenient human grading.
   - RADAR-PD: GPT-4 judge; arXiv 2605.12478; reports Dara at 84.8 min per sample.
   - XRDBench/AutoXRD:
     - arXiv 2609.00070
     - 30% LLM-judge weight
     - answers are public in the repo JSON
     - no licence
     - no scoring server
   - AlphaDiffract (Argonne, March 2026) says RRUFF mixes calculated and measured patterns.
   - AIF (LBNL, Advanced Science 2026):
     - Links: https://pmc.ncbi.nlm.nih.gov/articles/PMC13430547/, code at github.com/hackingmaterials/AIF, data at Zenodo 21141588.
     - A trust score on top of Dara.
     - The PG annotator reversed 83.3% of re-reviewed cases.
     - Chemists agree pairwise 35–70%.
     - Trust decisions aligned with experts in 77.6% of cases.
   - IUCr CPD QPA round robin (Madsen 2001, Scarlett 2002): 4- and 7-ingredient weighed mixtures, minor phases 1–5 wt%, raw scans and answers public.
   - Reynolds Cup:
     - biennial blind weighed-mineral contest
     - physical powders
     - human analysts
     - past powders are purchasable at $250 per unit
   - Szymanski 2023:
     - 240 weighed two-phase mixtures
     - minor phase at 2–20 wt%
     - Figshare 20029745, CC BY 4.0
   - Leon-Reina 2016: spiked series at 0.12–4.0 wt%, CC BY 4.0.
   - Doebelin 2020: semi-synthetic numerical mixing, built into Profex 4.1+, unstable at 1 wt% or less.
   - Codabench: free host with hidden answers and a 20-minute default compute cap, so entrants should upload answers rather than code.
   - Leeman et al. vs A-Lab: experts dispute whether ordered and disordered versions count as the same.

   **Physics of summing scans**
   - A naive weight-proportional sum misjudges the recipe by about 15 percentage points typically (worst 49).
   - An absorption-weighted sum brings that to about 5.
   - Compound absorption at 8 keV spans 8.4 (Li2CO3) to 261.0 (La(OH)3) cm²/g.
   - Summed scans still differ from real ones by about 4× counting noise.

   **Sizing**
   - 270 items give ±5 points only if accuracy is about 78% or higher.
   - Near 50% accuracy, about 385 separate powders are needed.
   - Separating two tools that are 5 points apart needs about 470–780 paired powders.

3. Files and Code Sections (SP = session scratchpad; R4 = the other session's scratchpad experiments folder; never quote these paths to the user):

   **Workflow 1 results (4 proposer lenses)**
   - Location: `…/subagents/workflows/wf_ad9681d5-db2/journal.jsonl`.
   - Extracted via a Python script to tool-results/ba2gega2j.txt and read in full.
   - Recommendation by lens:
     - Quick-wins: real-or-simulated index.
     - Leverage: real-or-simulated label, pointed first at dara-conform.
     - Fit: hard known-answer test, with corrections sent in the same week.
     - Contrarian: shared grading rulebook first, with the clean list as a quick win.
   - Traps named across the lenses:
     - auto-fixing units: wrong-fix rates of 7.23% and 11.2%, and 85/266 fixable
     - building a benchmark now
     - the thermoelectric spec
     - a metadata standard with no lab behind it
     - expert relabelling, at about 1,000 expert-hours
     - the detectors that failed
     - more downloads
     - a fifth round of experiments before shipping anything

   **Workflow 2**
   - Script: `…/workflows/scripts/verify-next-contribution-shortlist-wf_31202e82-b45.js` (run wf_31202e82-b45, task w9q83woj1).
   - Args: mem, sp, out=SP/verify2, r4, github, py.
   - Agents: 9.
   - Output schema fields: candidate, lens, verdict, checks[], prior_art[], new_facts[], changes_needed[], smallest_useful_first_step, plain_summary.
   - Results:
     - SP/verify2/all_results.json (all 9 results)
     - journal at …/subagents/workflows/wf_31202e82-b45/journal.jsonl
     - human-readable dumps at tool-results/bi488d6le.txt and tool-results/bea264wm8.txt
   - Agent outputs on disk:
     - SP/verify2/c1_clean_list…/: rederive_headlines.py, hkustb_independent.py, join_flags.py, rruff200.py, independent_hash.py, conflicts.py, fingerprint.py
     - SP/verify2/c2_error_reports_evidence/certain_items.md: five-item polite note with sample ids and reproduce lines
     - SP/verify2/c3_grading_rules_evidence/tricky_pairs.py: 21 pairs
     - SP/verify2/c4_known_answer_test_evidence/: sum_vs_real2.py, scan_headers.py
     - SP/verify2/c5_combined/: gpss_counts.py, gpss_sets.py, pg_counts.py, pg_full_table_baseline.p…

   **Workflow 2 verdict details**
   - **c1 clean list: holds_with_changes.**
     - All headline counts reproduce:
       - 1,702/3,019
       - 499/499 HKUST-B matches, re-hashed independently, of which 414 are calculated
       - 124/2,680 duplicates in 61 groups
       - 501 unlabelled, of which 499 are HKUST-B, so the same problem counted again
       - usable pool 1,683 → 1,600 after de-duplication
       - 353 with a wavelength, 352 of them from CNRS
     - "15 conflicting labels" overstates the problem. 9 of 20 hand-checked CNRS groups were different phases of one multi-phase sample.
     - Impact on dara-conform is small:
       - 0 HKUST-B rows.
       - 8 of 200 RRUFF rows are suspect (2 of them in the pilot): R250041, R250011, R250017, R250061, R250145, R250143, R250080, R250057.
       - 8 duplicate pairs, all inside opXRD-CNRS.
     - dara-conform uses the PROCESSED files, not RAW. Its filter greps for "calculat" and misses "computed".
     - A smoothness-only flag is unsafe. Of 29 conflicts, only 3 look calculated, and most are real scans from one instrument type.
     - The RRUFF calculated status is declared in the file headers, so it is not news.
     - The HKUST-B↔RRUFF match is undisclosed and new. The same group re-published 261 of those files elsewhere as "experimental".
     - Eight papers use between 148 and 3,002 RRUFF "experimental" files with no ID lists.
     - RRUFF documents Cu wavelength once for the whole site, and it has no licence text.
     - Correction routes: opXRD's GitHub issues, where the only outside issue has been unanswered since March 2026; RRUFF's contact form, with the site mid-migration.
     - Changes needed:
       - add a basis-of-evidence column
       - make categories non-overlapping
       - state coverage
       - use the neutral wording "intensity values identical to RRUFF file X"
       - key rows on RRUFF ID plus content hash plus snapshot date
       - ship a tiny checker (input: a list of IDs; output: how many are calculated or duplicated)
   - **c2 error reports: holds_with_changes.**
     - All 8 counts reproduce, but only 5 items are certain:
       1. a stale target copy in 9 samples, with the 7 lead samples folded in as the same defect
       2. 19 negative XRD specimen masses
       3. 2 negative recovered masses, plus a request to define "recovered"
       4. weight_percent holds fractions where the schema comment shows 45.2
       5. hydrate formula vs formula_clean, as a README request
     - About 30 of 1,035 samples (about 3%) hold a truly wrong stored value.
     - Retract these:
       - "method reads manual" is an error (it is the schema default)
       - the 20 orphan files (18 are leftovers of dropped precursors)
       - the SiO2 #180 item (the count does not reproduce)
       - "not a furnace effect"
     - Read the PG paper first, and tag each item:
       - A = the file contradicts itself
       - B = the file contradicts the paper (for example, the paper says a 1-hour hold where the file has 231 at 4 hours, and the paper says doses are within 0.2% where about a third miss that)
       - C = a question
     - Ship a reproducer script. Publish the corrections as the user's own sidecar file, which CC BY 4.0 permits.
     - The PG paper is still under review, so a public issue would be visible to its reviewers.
     - Rank of the other owners: Starrydata second (it has a working fixes channel), opXRD third, RRUFF dropped as an errata target.
   - **c3 grading rules: holds_with_changes.**
     - matching.py compares formulas only, and Dara's choice of reference file is discarded before grading.
     - On 18 tricky cases, the strict rule gets 8 wrong and the lenient rule gets 13 wrong.
     - The lenient rule merges hydroxide with peroxide. It also merges these pairs:

       | Pair | L1 distance |
       |---|---|
       | Nb2O5 = Nb12O29 | 0.0139 |
       | WO3 = W18O49 | 0.0373 |
       | TiO2 = Ti9O17 | 0.0256 |
       | Ca3SiO5 / Ca2SiO4 | not reported |
       | YFeO3 / Y3Fe5O12 | not reported |

     - 15 of 56 P1 rows in raw_signals.csv carry stale lenient labels: 64 stored vs 79 recomputed, out of 260.
     - About 250 of 590 checkable scans have two or more crystal forms on offer, but there are 0 proven wrong marks from crystal form.
     - A "same space group" rule would itself be wrong in at least 3 cases, for example Y2O3 #199/#206.
     - No installable grader or rule card exists. Present this as the "first executable, tested card", not as a new taxonomy.
     - Return a tier, not a yes/no.
     - It needs sign-off from one practising diffraction specialist.
     - First step: publish a CSV of about 25 pairs with the verdict from each of:
       - strict formula
       - lenient formula
       - StructureMatcher at default settings
       - StructureMatcher at stol 0.15
       - the proposed tier
   - **c4 known-answer test: holds_with_changes.**
     - All 10 single-ingredient scans and all 40 mixture scans are on disk, and Dara is installed.
     - 8 of the 10 singles sit on a shifted grid with longer counting, and there are no short single-ingredient scans.
     - The novelty is narrow: a standing machine-scored test with hidden recipes, on hundreds of measured mixtures with 4 or more ingredients.
     - Local Dara 1.1.12 with COD pools capped at 80 is not the published set-up.
     - First step: the replay test.
       - Rebuild the 40 mixtures as absorption-weighted sums.
       - Freeze the scorer beforehand.
       - Compare with stored outcomes in direction-probes/P1-dara-miscalibration/results/.
       - Cost: about 25 minutes of compute plus about a day of coding.
     - Before that, run Dara on the public harder weighed scans (IUCr CPD, Leon-Reina). That needs download approval.
     - Hidden-recipe hygiene: the file names currently spell out the recipe.
   - **c5 human-check set: weakened.**
     - GPSS: 124/352 counts only scans where the phase count differs. Comparing the phase lists gives about 150. 137 of 352 human files are the program's fit left unchanged.
     - PG: 316/343 has no headroom. Random scores 20.1% and a perfect method 21.8%.
     - A fuller PG table has 1,151 scans (354 positives). There, the trivial rule "the program named one phase" already scores about 50%.
     - It is already dara-conform milestone M3, and it overlaps with AIF.
     - Don't re-host the GPSS CIFs, which are ICSD-derived.

   **Round-5 folders**
   - R4 contains v1–v4 folders from another session, dated 2026-09-18 and unverified. v1_xrd_known_answer_dara_gpss holds PREREG.md and metrics_*.json.

   **Published page**
   - File: SP/build/site/xrd-curation-experiments.html, Version 3.
   - It contains the erroneous line "XRDBench, which keeps its answers with the evaluator." This must be corrected: the answers are in the public repo JSON, there is no scoring server and no licence.
   - Republish using the same file path, and omit the favicon.

   **dara-conform (read-only)**
   - Files:
     - code/matching.py
     - code/build_manifest.py
     - code/ingest/parse_rruff.py
     - code/ingest/parse_opxrd_labels.py
     - data/manifest.csv
     - results/raw_signals.csv
     - PREREG.md
   - data/manifest.csv: 1,554 rows, 1,396 active.
   - results/raw_signals.csv: 332 rows on disk, 300 of them parsed.
     - Relevant columns: gt_phases, rank1_phases, correct_strict, correct_lenient, source_stratum, deletion, error.
   - Related file: ~/github/direction-probes/P1-dara-miscalibration/RESULT.md.
     - Accuracy moved from 0.545 to 0.745 after the hydrogen-reconciliation rule.
     - Precursor mixtures scored 0.80 (32/40) lenient.
     - At n=55, lenient is 0.745 and strict is 0.309.

   **My verification script (run read-only with `.venv/bin/python -B`)**
   - It counted the P1-precursor deletion=0 rows:
     - 40 rows
     - 12 strict-correct
     - 17 lenient-correct
     - 0 errors
   - It counted all deletion=0 no-error rows:
     - 210 rows
     - 63 lenient-correct
     - 45 of those strict-correct
     - so 18 depend on the lenient rule

   **Memory directory**
   - It now includes curation-experiments-r4-verdicts.md.
   - No new memory has been written this segment.

4. Errors and fixes:
   - **XRDBench error on the published page:** the page says XRDBench "keeps its answers with the evaluator". The prior-art checker found that the answers are published in the repo JSON, which matches my own memory note. Not fixed yet; correct it and republish.
   - **Earlier PG claims partly overstated:**
     - The "9.0% strict wrong values" figure needs a caveat: only about 30 of 1,035 samples hold a value that no owner could call intentional.
     - Several draft errata items need retraction or softening.
     - Not yet reflected in ERRATA_DRAFT.md. That file is another session's, and editing it is not mine to do without asking.
   - **"15 duplicate groups with conflicting labels" overstates error.** Use the wording "same pattern, different label text".
   - **The 501 unlabelled files are almost entirely the same 499 HKUST-B files.** That is one problem counted three ways, so avoid double-counting in the final answer.
   - **Output too large for inline display, twice.** Resolved by reading the persisted tool-results files with Read, using offset for the second page, and with a targeted grep.
   - **No user corrections this segment.** The key user feedback is unchanged: the reports are too jargon-heavy and the next step is unclear.

5. Problem Solving:
   - Completed:
     - Workflow 1 (proposals) and Workflow 2 (adversarial verification).
     - My own recount of the grading-rule sensitivity from the user's own pilot results.
   - Draft final synthesis, not yet delivered:
     - **Big picture in plain words.**
       - Many groups build programs that read X-ray scans of powders and name the ingredients.
       - Nobody can reliably say which program is better, for four reasons.
     - **Gaps:**
       1. The "right answers" are mostly one person's or one program's opinion.
          - 316 of 343 scans differ between human and program.
          - A single editor ID is on all 1,216 checks.
          - AIF reports that the annotator reversed 83.3% of re-reviewed cases and that chemists agree 35–70% of the time.
       2. The rule for marking an answer right is unwritten and swings scores more than the gap between tools.
          - The same program on the same 40 scans scores 12, 17 or 32 out of 40 by three ways of marking, and the paper reports 38.
          - 18 of 63 credited answers depend on which rule is used.
       3. Public scan collections are partly not what they say.
          - 1,702/3,019 RRUFF "RAW" files are calculated, which RRUFF declares itself.
          - 499 opXRD files match RRUFF files and are undisclosed. 414 of them are calculated but flagged as not simulated.
          - 1,600 usable scans remain out of 7,183.
       4. Scans with certain (weighed) answers are too few and too easy: 40 scans, 38/40 vs 35/40 cannot be told apart.
       5. Nobody records the history of a sample between making it and scanning it.
     - **Solutions by effort:**
       - Days:
         - Publish the 499-row HKUST-B↔RRUFF match table plus a tiny "check your file list" tool (needs the user's yes to publish).
         - Send a 2–5 item polite note to the PG authors (needs the user's yes; read their paper first).
         - Make two small fixes in dara-conform: log the chosen reference file, and relabel at analysis time (needs the user's approval).
       - Weeks:
         - Build the fair marking kit: about 25 tricky pairs, a rule card with tiers, and a runner. This is the recommended contribution.
       - Needs a partner lab:
         - Build a hard weighed-answer hidden exam of about 385 or more powders.
         - Desk first step: the replay test.
         - First run the already-public harder weighed scans (needs download approval).
     - **Skip:**
       - auto-fixing units
       - a new metadata standard
       - expert relabelling
       - the human-overrule test set
       - the thermoelectric benchmark
       - more downloads
       - a fifth round of experiments before shipping anything
   - Why I recommend the marking kit:
     - It has the strongest evidence, which comes from the user's own project.
     - It needs no lab, no permission and no downloads to start.
     - It is a prerequisite for scoring any future exam.
     - It fits the dara-conform pre-registered fallback, "shrink to the evaluation harness", which AIF may be triggering.
     - It appears unbuilt. The ideas themselves are old (IUCr 1990), and what is missing is a runnable, tested version.
     - It needs sign-off from one practising specialist.

## Later status lines from that session
- 23:51Z: corrected one sentence on the published XRD Curation Experiments page (now Version 4): XRDBench answers are PUBLIC (repo JSON, no licence, no scoring server), so its 134 cases cannot serve as a hidden test.
- Its short plain-language answer was drafted and under review by six checkers; not yet delivered.
