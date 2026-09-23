# Verifier notes: candidate K2 ("Real or simulated?" check list for open XRD files)

Lens: evidence and consistency. No web access. Only files inside the scratchpad were read. Nothing was sent, downloaded, published or changed.

Words used: **XRD** = powder X-ray diffraction [a 1-D curve of peaks measured from a powder]. **RRUFF** = an open mineral archive. **opXRD** = a pooled open collection of XRD files from several labs. **HKUST-B** = one contributor folder inside opXRD. **Hash** = a content fingerprint; two files with the same hash hold the same numbers.

Short names for sources: **C16** = digests/C16-xrd-session-verification.md; **C15** = digests/C15-late-updates.md; **C15-raw** = corpus/convos/C15_...part1of1.md; **C03-raw** = corpus/convos/C03_...part3of3.md (the main session's own recount of round 4); **build-list** = corpus/notes/FILE_build-list.md; **builds** = synth/builds.md; **late2** = late2.txt; **mem-xrd** = corpus/notes/mem_84cb7d_xrd-open-datasets.md.

## Verdict: holds, with changes

Every number in the candidate was found in the files with its denominator. No refuted idea is revived. The strongest claim (499 of 499) was confirmed three separate times. The weak spots are: (a) the first step depends on files in two temporary folders that I could not check and whose move needs the user's yes; (b) the HKUST-B files carry no answer label, so the "people test models on them" story is weaker than the problem statement implies; (c) three design details would break the candidate's own done-test unless fixed (overlapping categories, the noise test used alone, the unstated rule behind "8 of 200").

## Claim-by-claim check

| # | Claim | Result | Where found, denominator, later weakening |
|---|---|---|---|
| 1 | 499 of 499 HKUST-B files have intensity values identical to RRUFF files; 414 of the 499 are calculated but deposited as "not simulated" | confirmed | C03-raw line 934 (round-4 experiment, and the main session wrote "I confirmed 499/499"); C16 line 136 ("re-hashed independently"). So three confirmations, not two. Extra detail the candidate omits: 498 of 499 also match on the angle axis; one file (pattern_323) differs there. Wording "intensity values identical" is the exact wording C16 asks for. |
| 2 | "New and undisclosed" | partly | C16 line 149 says so, but C16 line 5 tags all prior-art findings as "single-agent, not yet independently re-verified". Partial independent support: an earlier session's source note says RRUFF is not a listed contributor to opXRD (C02-raw part 1 line 1860). A negative claim ("nobody disclosed it") needs a web check before it is said in public. The candidate caveats items 3 and 4 below this way but not this one. |
| 3 | The same group re-published 261 of them elsewhere as "experimental" | partly | C16 line 149 only. One checker. No denominator beyond "261 of those files" (i.e. of the 499). Candidate already marks it single-checker. |
| 4 | Eight papers use 148 to 3,002 RRUFF "experimental" files with no ID lists | partly | C16 line 150 only. One checker. The paper names are not in any file I could read. Candidate already marks it single-checker. |
| 5 | 124 of 2,680 opXRD files are exact copies, in 61 groups | confirmed | C03-raw line 934 (CNRS 42 files, EMPA 82; 0 across institutions); C16 line 137; build-list line 214. |
| 6 | Usable pool 1,683 of 7,183; 1,600 after removing copies; 353 state a wavelength, 352 from one institution | confirmed, with a denominator note | C03-raw line 934; build-list line 121; C16 lines 139-140. Note: 7,183 = 3,019 RRUFF RAW + 1,484 RRUFF PROCESSED + 2,680 opXRD (3,019 and 1,484 are in builds line 167). So one RRUFF sample can be counted twice, once as RAW and once as PROCESSED. The half-page note should say this. |
| 7 | 1,702 of 3,019 RRUFF "RAW" files are calculated; their own headers say so; a March 2026 paper already notes it | confirmed / partly | Count: C03-raw ("I recounted exactly"), build-list line 210, C16 line 135. "Not news": C16 lines 63 and 148; the March 2026 paper (AlphaDiffract, Argonne) is again a single-checker finding. |
| 8 | Noise test agrees with the header on 2,928 of 3,006 files (97.4%) | confirmed | C03-raw line 934 (also AUC 0.998); builds line 166. |
| 9 | Effect on the user's project: 0 HKUST-B rows; 8 of 200 RRUFF rows suspect (2 in the pilot); 8 duplicate pairs; filter searches "calculat" and misses "computed"; 1,554 rows, 1,396 active | confirmed as reported, not re-checked | C16 lines 142-146 and 241. Read by the XRD session only; this session is barred from opening the project. One cross-check: a different session read the project's inventory as about 1,554 = 56 + 352 + 946 + about 200 (C03-raw part 2 line 2686), which matches. Missing from every file: the RULE that makes those 8 rows "suspect". Only the 8 IDs are given. C16 line 146 adds that the project uses RRUFF PROCESSED files, not RAW; the PROCESSED base rate is 198 of 1,484 (C03-raw), not 1,702 of 3,019. |
| 10 | "15 conflicting labels" overstated; 9 of 20 hand-checked groups were different phases of one sample | confirmed | C16 line 141; builds section C does not list it but gaps.md marks it "refuted as worded". The 15 and the 20 look inconsistent but are not: 42 CNRS files in copies fit 20 CNRS groups, of which 15 carry different label text (my arithmetic from C03-raw: 42 + 82 = 124 files; 20 + 41 = 61 groups). |
| 11 | The 501 unlabelled files are almost all the same 499 files | confirmed | C16 lines 138 and 272 (499 of 501). C03-raw: HKUST-B label class is "no phase" for 499 of 499. |
| 12 | Smoothness alone is unsafe: of 29 disputed files only 3 look calculated | confirmed | C16 line 147. The 29 are the files where header and noise test disagree in the "header says measured, curve looks noise-free" direction (build-list line 80; r4 memory note line 41). Note gaps.md glosses them as "29 label conflicts", which is a different thing; the candidate's wording is the better one. |
| 13 | On-disk opXRD copy is 2,680 of 92,552 files; 88 MB slice of about 1.4 GB | confirmed, but the framing misleads a little | C16 line 18; mem-xrd line 17 (zip lists 1,400,997,733 bytes, occupies 88 MB); build-list line 229. See "Coverage" below. |
| 14 | Data on disk: RRUFF and the opXRD slice are in the user's own project folders, no approval needed | confirmed | build-list line 230; builds line 167. |
| 15 | The working list sits in a temporary area "that can vanish" | confirmed, and it is worse than stated | C15-raw line 290: the list (manifest.csv plus readme) is in ANOTHER session's scratchpad (round-4 experiments folder). C16 line 126: the seven checker scripts (rederive_headlines.py, hkustb_independent.py, join_flags.py, rruff200.py, independent_hash.py, conflicts.py, fingerprint.py) are in the XRD session's scratchpad. Two temporary places, two sessions. I could not check that either still exists. |
| 16 | Needs your yes: "none to build" | partly | True for reading the archives in place (late2 line 72-73: read-only use of the user's project folders is fine). But the first step starts with "after the file rescue", and moving files out of the temporary areas is listed as needing the user's yes (late2 line 449; builds section D, housekeeping). The candidate's approval line should list it. |
| 17 | Do not download the full 1.4 GB release | confirmed | late2 line 58 ("NOT approved"); builds section D. |
| 18 | Only outside issue on the collection unanswered since March 2026; RRUFF has no licence text | confirmed (single checker for the first) | C16 lines 151-152. "No licence found" for RRUFF also appears as a source finding in an earlier session (digests/R04.md line 49). |
| 19 | Effort "days (up to one week)" | confirmed, conditional | C16 line 300 puts "publish the 499-row match table plus a tiny check-your-file-list tool" in its "Days" bucket. The candidate's scope is wider (every file in both archives, five categories, six changes, a note). builds gives no effort for this item (X8). Days holds only if the rescue works; see change 1. |

## Does it revive anything refuted?

No. Checked against builds section C.
- It does not use the 41.4% multi-phase figure, the "15 conflicting labels" wording, public answers as a hidden test, or "more mixtures".
- It does not auto-fix anything; it labels.
- One near-miss: the noise test appears as a possible "what this rests on" value. C16 says a smoothness-only flag is unsafe (3 of 29). If any row's category rests on the noise test alone, that is the unsafe flag coming back under another name. See change 4.
- Guardrails: it is a CSV plus a small command-line tool, not a schema, platform or dashboard. Experimental data only. Outward steps are marked as needing a yes.

## Coverage: what "2,680 of 92,552" really means

The files say the full opXRD release has 92,552 patterns of which 2,179 are labelled (source finding, repeated in C02, C04, R03, R04). The on-disk slice is named "labelled slice" (C16 line 18; mem-xrd line 17) and holds 2,680 files of which 501 have no phase label. 2,680 minus 501 = 2,179. That is my arithmetic, not a statement in any file, but it fits: the slice looks like the whole labelled part of opXRD plus the unlabelled HKUST-B folder. If so:
- for people who need labelled files, the list may already be close to complete, which is better than "2,680 of 92,552" sounds;
- for the roughly 90,000 unlabelled files, the list says nothing at all.
The note should say both, after one offline check that the four extracted folders are the only labelled ones. "Every count is a lower bound" stays true.

## A weakness in the problem statement

The HKUST-B files have no phase label (499 of 499, C03-raw). Nobody can score a phase-naming model on a file that has no answer attached. So inside opXRD these 499 files cannot be "test items". The harm is different: they sit in a pool described as experimental and may be used for pre-training or for "simulated versus real" comparisons, and 261 were reportedly re-published as experimental elsewhere (single checker). The labelled-data harm comes from the RRUFF side, which is the half the candidate itself calls "not news". The candidate should state this plainly instead of "people test XRD models on files they believe are instrument measurements".

## Changes needed

1. Add the rescue to the approvals line. Moving the round-4 list and the seven checker scripts out of two temporary folders needs the user's yes and a folder name. Add a fallback: if either folder is gone, rebuild from the archives in the user's project folders (read-only); then call the effort "about a week", not "days".
2. Reword the problem for the HKUST-B half (see above): unlabelled files, so the risk is contaminated "experimental" pools and the reported re-publication, not contaminated test scores.
3. Fix the category design. One HKUST-B file is at once "identical to RRUFF file X", "calculated" (414 of 499) and "unlabelled" (499 of 499). Keep one yes/no column per fact, plus one "main category" picked by a written order of precedence. Otherwise "exactly one category per row" cannot be met honestly.
4. Never let the noise test set a category on its own. Make it an advisory column. For opXRD files outside HKUST-B there is no header to read, so rename "measured" to "no sign of calculation found"; it is not proof of measurement.
5. Carry rows for both RRUFF RAW and RRUFF PROCESSED files and say which is which. The user's project uses PROCESSED (198 of 1,484 declare a calculated profile); the headline 1,702 of 3,019 is RAW.
6. Write down the rule that makes a row "suspect". No file here states why those 8 of 200 rows are suspect, only their IDs. Without the rule (or the rescued rruff200.py / join_flags.py), the done-test "reproduces 8 of 200" cannot be run.
7. Make the checker print a "not covered by this list" count. By the project's own inventory about 408 of 1,554 rows (56 Dara plus 352 GPSS) come from neither archive.
8. Add the one private check that is still open and matters most to the user: do any of the 8 duplicate pairs sit on both the training and the test side? (C15 calls this the unchecked risk.) Put it in "done looks like".
9. In the coverage note, state the 7,183 make-up (RAW plus PROCESSED plus opXRD) and the labelled-slice point above.
10. Extend the "verify on the web before saying it in public" caveat to "undisclosed" and to the March 2026 paper, not only to "261" and "eight papers".
11. Record the angle-axis detail: 498 of 499 match on angles as well; pattern_323 does not.

## Smallest useful first step

With the user's yes to name one folder: copy the round-4 list and the seven checker scripts there with a text file of hashes. Then, reading the archives in place and changing nothing, produce only the 499-row match table (opXRD file, RRUFF file, hash, header says calculated yes/no, angle axis matches yes/no) and confirm it gives 499 rows, 414 calculated, 498 angle matches. That is the one part that is both new and triple-confirmed; everything else can be layered on after it reproduces.

## Prior art named in the files (none checked on the web by me)

- RRUFF's own file headers already declare calculated profiles (C16 line 148).
- AlphaDiffract (Argonne, March 2026) says RRUFF mixes calculated and measured patterns (C16 line 63; single checker; no link in the files).
- The user's own project already drops header-calculated RRUFF files and the HKUST-B folder (C15 line 11), which is why the private gain is small.
- opXRD paper, arXiv 2503.05577 (link appears in C02-raw part 1 line 1199): lists its contributors; RRUFF is not among them per an earlier session's note.
- RADAR-PD, arXiv 2605.12478: uses 291 RRUFF samples (C15 line 12; C16 line 56), so it is one likely user of such a checker.
- Inside this corpus: build B8 (file-only lint, wider scope, 2 weeks to 3 months) and build B2, whose leak report already names "duplicate group plus cross-archive hash" as the grouping unit for XRD (build-list line 42). K2 is the XRD data those two would consume, not a rival.
