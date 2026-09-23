# Verification of candidate K3 (TE "the exam is too easy") - lens: evidence and consistency

Verifier had no web access. Only files inside the scratchpad were read. Nothing outside it was opened, so "is the data still there" could NOT be checked directly.

## Verdict: HOLDS WITH CHANGES

Every number in the candidate was found in the files with its denominator. Nothing refuted is revived. The changes below are about (a) one unverified premise, (b) a wrong date on where the data lives, (c) a breakdown that is in the raw transcript but missing from the candidate and that a reviewer would ask for, (d) an optimistic effort figure, (e) two approvals that are not listed.

## Claim-by-claim check

| # | Claim | Result | Where found / note |
|---|---|---|---|
| 1 | 12,222 samples, 3,015 papers; random split: test paper in training 93.5%; median Seebeck error 25.5% / 42.2% / 46.6% | CONFIRMED | Raw table in corpus/reports/R07_thermoelectric-benchmark-spec.txt lines 256-260; digests C03-1of3 line 44, C03-2of3 line 28, R07 line 24; builds.md B2. Model = median of 5 nearest neighbours on element fractions, 5 folds by hash. Run once (builds B6: "done once"); I found no independent re-run of this table. The source table column is "Test paper in training", so the 93.5% unit is papers/rows of the S set; the re-run should print it both per paper and per sample. "Chemical families" in the candidate = "chemical system" in the files (same set of elements; 2,419 of them). |
| 2 | Lookup 22.9% beats kNN 29.4% on 3,593 samples; answers-known floor 15.0% | CONFIRMED | R07 report lines 262-269; digests C03-2of3 line 30 and R07 line 24 (so the 3,593 count IS in the digests, not only in the transcript). Extra facts the candidate leaves out: 3,593 is 29.4% of the 12,222 rows; on the same 3,593 rows the random-split kNN scores 24.8%; 1-nearest-neighbour under random split scores 21.4% vs 25.5% for 5 neighbours (C03-1of3 line 44), so part of "lookup beats model" is the choice k=5. |
| 3 | Same formula, different papers: median 32.7% over 21,856 paper pairs (647 compositions); opposite sign 3,881 (17.8%) | CONFIRMED | C03-2of3 line 29; gaps.md G12; raw transcript part2 line 450. |
| 4 | Shared DOIs raw 183 / 26 / 4, cleaned 193 / 75 / 7; "26 of 75" | CONFIRMED | C03-3of3 line 27; build-list line 41; builds.md B2; C15. Third number = teMatDb-ESTM and all-three, both 7 (C03-1of3 line 43). Normaliser is said to be saved with this as its regression test. |
| 5 | Synthesis ledger (1,035 samples): macro-F1 0.53 -> 0.42 (rerun 0.49 -> 0.39) when a starting chemical is held out | CONFIRMED, with a caveat the candidate drops | C03-3of3 line 44 (0.526 -> 0.415; 0.488 -> 0.394, 10/10 seeds). Build-list line 207 adds: "up to half the drop is shared by a temperature-only model". Forests were hand-written (no scikit-learn). |
| 6 | Steels benchmark: 66 of 312 groups have a near-copy in another group | CONFIRMED | C03-2of3 line 56; build-list line 146. "Near-copy" = composition within 0.1 wt%. |
| 7 | Only model is 5-NN; forests hand-written because scikit-learn missing; public answers so practice exam only | CONFIRMED | builds B6 "Gap"; r4 memory note line 37; builds T5 risk; section C lists "public answers as a hidden test split" as refuted and the candidate respects that. |
| 8 | MatFold exists, open licence, no by-paper split | PARTLY | Files say "Contribute a paper-group split type to MatFold (MIT)" (build-list line 43) and "GroupKFold and MatFold exist as tools. No TE task uses them" (gaps G16). No file shows anyone actually read MatFold's split list. Web check still needed. |
| 9 | "The TE files are still in the temporary folder (nobody has looked since 14 September)" | WRONG on the date, UNKNOWN on survival | The TE data was downloaded on 15-16 Sep in the main "data landscape" session (C03-1of3 timeline step 6; the snapshot is dated 2026-09-14, which is where the "14 September" label comes from). The files were read again on 18 Sep: Round 4 experiments w1 and w2 ran on Starrydata/teMatDb/ESTM "already on disk", and Round 5 experiments E2 and E3 were launched on them the same evening (C03-3of3 lines 22-34, 81). So last known use = 18 Sep, by a session that was still running. The folder is that session's temporary workspace; the transcript says it "is deleted when the session ends" (C03-1of3 line 63). I cannot look there (outside the scratchpad). |
| 10 | "Papers that predict TE properties split data at random" (problem statement) | NOT FOUND | No TE machine-learning paper is named or checked for its split method anywhere in the files. R07 G4 asserts it "hurts every published composition->property TE model claim" without a source. This premise carries the whole "who benefits" line. |
| 11 | "No shared fixed test list exists for this data" | PARTLY | Files: negative search only - "none was found, not proven absent"; Matbench has no TE task; JARVIS leaderboard has no experimental TE task (gaps G17; R07 F9). |
| 12 | Nobody has published a paper-grouped leakage result for TE | NOT FOUND (candidate says so itself) | Not checked anywhere in the corpus. |
| 13 | Data: 55,422 samples in largest DB; ESTM 5,205 rows, no licence; download size not stated | CONFIRMED | C03-1of3 lines 40-42; Starrydata and teMatDb are CC BY 4.0 (R07 line 96). I also found no download size for the Starrydata snapshot. |
| 14 | Effort 1-2 weeks (about 1 week if files survive) | PARTLY | Files: B2 alone = 1-2 weeks (main session: about 1 week); B6 baselines = 1-2 weeks on their own; the note (T7) is status "idea". K3 = a slimmed B2 + one piece of B6 + a note + a MatFold offer. 1 week matches only the B2 part. |
| 15 | Approvals: "None to build if files survived" | PARTLY | Missing: (i) installing scikit-learn or any model package is a download/install -> needs a yes (the candidate mentions it in the first step but not in the approvals line); (ii) copying files to a permanent folder needs the user to NAME a folder - offered three times, never answered (C02-2of2 line 64; builds section D "move files to a folder the user names"). Publishing items and the MatFold ask are correctly marked. |
| 16 | Revives a refuted idea? | NO | Planted-duplicate test is on DOIs, not the refuted curve-only replot detector. No auto-fixing. No hidden split from public answers. |

## The breakdown the candidate is missing (all numbers from the raw transcript, part2 lines 423-459, and the R07 table)

- Under the "whole papers held out" split, test samples whose exact composition also appears in a training paper: 29.4% error (n = 3,593). Test samples whose composition is new: 48.1% error (n = 8,629). The 42.2% headline is the blend.
- On those same 3,593 samples, the random split gives 24.8%. So like-for-like on "composition already seen", holding out the paper costs 24.8% -> 29.4%. Most of the 25.5 -> 42.2 jump sits in the 8,629 new-composition samples, where a random split lets the model copy from sibling samples of the same paper.
- Under the random split only 40.4% of test compositions are in training, but 93.5% of test papers are. Under the chemical-system split, the test paper is STILL in training 52.4% of the time. So "hold out by chemistry" does not hold out papers. This is a useful line for the note.
- "Lookup beats model" and the 15.0% floor apply to 3,593 of 12,222 rows (29.4%) only. For the other 8,629 there is nothing to look up.
A reviewer will ask for this table. It does not weaken the finding; leaving it out would.

## Changes needed before K3 goes into the plan

1. Fix the data-location sentence: last used 18 Sep by the still-running main session; temporary workspace that is deleted when that session ends; this session may not look there. First step = the user names a folder and asks the main session to copy the TE snapshot, baseline_300K.py, between_paper_spread (v2), the DOI normaliser and the per-sample prediction export there, with hashes.
2. Mark the premise "TE papers use random splits" as UNCHECKED and add a half-day reading check (how do 5-10 TE prediction papers that use Starrydata split their data?) plus the prior-art search, BEFORE writing the note. If a TE leakage audit already exists, the note shrinks to the frozen list.
3. Add the seen / unseen breakdown and the 52.4% line to the note's table; say the lookup result covers 29.4% of rows; report 1-NN next to 5-NN.
4. Effort: say 2-3 weeks for the full list, or keep "about 1 week" and cut scope to: re-run + breakdown + DOI index + frozen list v0. Strong baseline and note follow.
5. Approvals line: add "package install = yes" and "copy to a folder you name = yes".
6. Done-criteria: "reproduces 66 of 312" needs a near-duplicate-composition finder (0.1 wt% tolerance), which is more than the "group column" leak report described. Either add that mode or drop the criterion. Add the round-4 criteria the build list already requires: recall on real known pairs, and the grouping unit named per dataset.
7. Frozen list: pin the snapshot (dated 2026-09-14; saved snapshot has records up to 2020-09-30 per build-list line 34) with a file hash, write down the selection rule (Experiment samples, one value at 300 K, samples with two curves skipped, range screens), and FLAG (never fix) test papers that sit on the existing review queue (633 specimens from 230 papers) and the 8 known Starrydata record errors. Call it v0 of a practice exam.
8. Wording: "chemical families" -> "chemical system (same set of elements)".
9. Carry the caveat on the synthesis-ledger number: up to half the drop is shared by a temperature-only model.

## Prior art named in the files (no web check possible here)
- scikit-learn GroupKFold - does the grouped split itself.
- MatFold - materials split tool; files say MIT and propose adding a paper-group split; nobody read its split list.
- teMatDb "Sc-ZT" filter (arXiv 2505.19150) - prior art for the record checker, not for splits; shows this community does publish data-quality notes.
- Matbench / JARVIS-Leaderboard - no experimental TE task (negative search).
- The user's own TE Benchmark Spec (private page, section 3e) already holds the 25.5 / 42.2 / 46.6 table and the lookup table. The note is a rewrite of finished work, not new analysis.
- NOT in the files: any general materials-ML leakage paper (for example leave-one-cluster-out cross-validation). The note must cite that literature; it needs a web search.
