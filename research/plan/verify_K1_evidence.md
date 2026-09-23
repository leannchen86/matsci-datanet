# Verifier notes for K1 (tricky-pairs table + marking function for XRD answers)

Lens: EVIDENCE AND CONSISTENCY. No web access. Files only. Nothing outside the scratchpad was opened.
Short names: C16 = digests/C16-xrd-session-verification.md; builds = synth/builds.md; gaps = synth/gaps.md; late2 = late2.txt; C04-2 = digests/C04-2of2.md; R10 = digests/R10.md; h6-note = corpus/notes/mem_84cb7d_xrd-h6-handedness-verdict.md; datasets-note = corpus/notes/mem_84cb7d_xrd-open-datasets.md.
synth/critic.md did not exist when this was written.

## Verdict: HOLDS WITH CHANGES

Every number in the candidate was found in the files with its denominator. No refuted idea is revived. The data sit in a lasting folder (the user's own project folders), not a temporary one; only the 21-pair script is in another session's temporary area. But the write-up has one internal contradiction, one wrong attribution, one over-general sentence and two approvals it does not state.

## Claim-by-claim

| # | Claim | Result | Where / note |
|---|---|---|---|
| 1 | Same program, same 40 weighed scans: 12 of 40 strict, 17 of 40 lenient, 32 of 40 after corrected matching; paper says 38 of 40 with a paid library | confirmed (second-hand) | C16 lines 40-42, 250-254; late2 lines 456-458. The 12 and 17 were recounted by the XRD session's own script from stored labels (40 rows, 0 errors). The 32 was NOT recounted; it is a quote from a result file in the user's probe folder. C16 is the only source; this session never opened the project. |
| 1b | Reading of 17 vs 32 | partly | C16 line 193: 15 of 56 rows carry out-of-date lenient marks (64 stored vs 79 recomputed). 17 + 15 = 32 (my arithmetic, not stated in the files). So 17-vs-32 looks like an out-of-date results file, not a different rule. The real rule effect is 12 vs 32. The candidate's risk section half-says this; the headline should say it plainly. |
| 2 | Published gap 38 of 40 vs 35 of 40 = 7.5 points, interval 0.0 to 15.0 | confirmed | builds line 192; C04-2 line 31; R10 line 28. Own recount of the paper's files; bootstrap over mixtures, 10,000 resamples; verdict "inconclusive". |
| 3 | 18 of 63 lenient-correct answers (28.6%), among 210 rows, depend on the lenient rule | confirmed | C16 lines 43-46 and 255-259. Recounted by the XRD session itself. 210 = rows with deletion=0 and no error, out of 332 rows on disk (300 parsed). |
| 4 | On 18 tricky cases strict is wrong on 8, lenient on 13; false merges Nb2O5/Nb12O29 (0.0139), WO3/W18O49 (0.0373), TiO2/Ti9O17 (0.0256) | confirmed, single checker | C16 lines 182-191. Two caveats. (a) The script has 21 pairs (C16 line 128) but the result is quoted on 18; the files do not explain the other 3. (b) The "expected verdict" column was written by an AI checker, not a specialist, so 8 of 18 and 13 of 18 are measured against an unchecked answer column. The three named merges are safe: they are different chemical formulas. |
| 5 | Misses are spelling artifacts ("LaO3", "Ni1.875O2", "V4O9.93316") | confirmed | C16 lines 48-51; recounted by the XRD session itself. |
| 6 | Formula order flips 3 of 20 verdicts; exact-text 17 and 4 vs composition 18 and 7; listed-twice answers marked right 4 of 4 and 2 of 3 | confirmed | C04-2 lines 26, 31; R10 line 32; builds line 299; gaps line 154. Denominator missing in the candidate: the 17/4 and 18/7 are out of 20 reaction products (not the weighed scans). The 3 of 20 flips are all tool B's (Jade's) verdicts. |
| 7 | StructureMatcher defaults merge the two quartz forms; site tolerance 0.15 or less separates them | confirmed | builds line 300; h6-note (RMS 0.169; reference files COD 1011097 vs 1011200; checked by 5 adversarial agents, none refuted). Re-runnable: the files and the Python environment are in the user's own project folder. Note gaps line 157 calls 0.15 "looser"; builds and the h6-note say "or less", i.e. tighter. Use "tighter". |
| 7b | A "same symmetry group" rule is wrong in at least 3 cases | confirmed, single checker | C16 line 195 (example Y2O3 #199 / #206). |
| 8 | 15 of 56 rows stale (64 stored vs 79 recomputed, out of 260) | confirmed, single checker | C16 line 193. The denominator 260 is not explained anywhere (the file has 332 rows, 300 parsed, 210 clean). |
| 9 | "dara-conform headline accuracy at n=55: 0.309 strict vs 0.745 lenient" | partly | Numbers confirmed (C16 line 247). Attribution loose: they come from the pilot probe's result file (direction-probes / P1), which gaps line 153 calls "that project's pilot", not dara-conform's headline. Arithmetic is self-consistent: 17 of 55 = 0.309, 41 of 55 = 0.745. |
| 10 | "No installable grader or rule card exists"; one 2026 benchmark gives an AI judge 30%; another uses GPT-4 as judge | confirmed as a single-agent finding | C16 lines 53-62, 196. late2 lines 426-432 show the XRD session itself still had "no existing grader" on its to-fact-check list. The candidate labels this correctly. |
| 11 | About 250 of 590 checkable scans offered two or more crystal forms; 0 proven wrong marks from crystal form | confirmed, single checker | C16 line 194. |
| 12 | The project's frozen plan has the rule "shrink to the evaluation harness" | partly | C16 line 32 has the rule, but it is CONDITIONAL: it fires if "calibration/abstention ships in Dara". C16 line 321 only says the trust-score paper "may be triggering" it. The candidate's "why smart" states it as the project's fallback without the condition. |
| 13 | "The Dara group has published a trust score on top of Dara" | partly / attribution not supported | The files say Dara is from the Ceder group (digests/C11 line 95) and the trust-score tool (AIF) is from the Jain group, code under "hackingmaterials" (C16 lines 64-69; gaps line 201). Same institution, different groups, per the files. A separate tool built on top of Dara is not the same as "ships in Dara". Web check still needed. |
| 14 | "The marking rule moves the score more than the difference between programs" (problem statement) | partly | True on the 40 weighed scans in the user's local set-up (rule: 12 vs 32; tools: 38 vs 35). NOT true on the second dataset: on 20 reaction products the rule moves tool A by 1 of 20 and tool B by 3 of 20, while the gap between tools is 13 of 20 (exact text) or 11 of 20 (composition). Narrow the sentence. |
| 15 | "Nobody has done it because specialists carry the rule in their heads" | not found / partly contradicted | No source. C16 line 83 says specialists publicly DISAGREE on whether an ordered and a disordered version of a crystal count as the same. So there is no single rule in their heads, and one specialist's sign-off will not settle that tier. |

## Does it revive anything refuted? No.
- It uses the public 40 scans as a worked example, not as a hidden test (the refuted use).
- It keeps the refuted "mirror-image merge is a bug" reading out: the quartz pair it adds is the two temperature forms (alpha / beta), not the left- and right-handed copies. Guard: add one left/right pair whose expected verdict is "same", because powder XRD cannot tell them apart (builds section C, h6-note).
- It does not ask for more weighed mixtures, a simulator, or unit fixing.

## Is the data really on disk?
- 40 mixture scans, 10 single-ingredient scans, installed Dara: yes per C16 line 206. The datasets-note says the Dara files are in the user's probe folder: 70 scan files plus spreadsheets. 20 reaction scans + 40 mixture scans + 10 singles = 70 (my arithmetic; it would explain the "70"; "41", "60" and "61" stay unexplained). Count first, as the candidate says.
- Stored results and the matching code: in the user's two project folders (C16 lines 232-247). These are lasting folders, not temporary.
- The 21-pair script: only in the OTHER session's temporary area (C16 line 128). It is not in this scratchpad (searched; not found). If it is gone, about 12 pairs can be rebuilt from text alone: the 3 named merges, Ca3SiO5/Ca2SiO4, YFeO3/Y3Fe5O12, hydroxide/peroxide, LaO3/La(OH)3, Ni1.875O2/NiO, V4O9.93316/V2O5, Y2O3 #199/#206, BiVO4/VBiO4, alpha/beta quartz.
- Reference structure files for every pair: NOT established. The quartz files are local. Whether files for Nb12O29, W18O49, Ti9O17 and the rest are in the local pools is not stated. If not, fetching them is a download and needs a yes.

## Internal contradiction in the first step
The first step says: re-mark the 40 weighed scans under all five rules, two of which compare crystal structures. C16 line 181 says the project's marker "compares formulas only, and Dara's choice of reference file is discarded before grading". So the stored results cannot be re-marked by a structure rule. Doing so needs either a fresh Dara run that logs the chosen reference file (outside the project), or a change to the project (C16 line 302 lists "log the chosen reference file" as needing the user's approval). The true answers for the weighed powders also carry no crystal form. Fix: in week 1 the 40-scan table uses formula-level rules only (strict, stored lenient, recomputed lenient, the new tier at formula level). Structure rules run only on the pair table, where the two reference files are named.

## Approvals: stated vs missing
Stated correctly: change to the project, contact a specialist, publish.
Missing:
1. Read access to the user's two project folders. Earlier sessions read them read-only, but this workflow was told not to open them. The working session needs the user's OK (or the user runs the script).
2. Moving the 21-pair script out of the temporary area to a folder the user names is on the XRD session's own "needs the user's yes" list (late2 line 449; builds section D, housekeeping). The merged plan's header says this; the K1 card says "None to build privately".
3. Any single reference-file fetch for the pair table (see above).
4. The optional AI-judge run costs money and is the user's call (the merged plan says so; the candidate JSON does not).

## Effort check
builds X3 gives "Effort: n.s." (not stated). C16 puts the kit in its "Weeks" bucket. "Days for the table, 1-2 weeks for the function and runner" fits that bucket but is the proposers' own estimate, not a corpus number. With the fixes above (formula-level rules on the 40 scans; structure rules only on pairs with local files) "days" stays believable.

## Changes needed (short)
1. Split the 12/17/32/38 story into three causes: rule (12 vs 32), out-of-date stored marks (17 vs 32), reference library and set-up (32 vs 38).
2. Narrow "moves the score more than the gap between programs" to the 40-scan local set-up; show the 20-reaction-product case where it does not.
3. Drop structure rules from the 40-scan table in week 1; keep them on the pair table.
4. Fix the group attribution of the trust-score tool and state the fallback rule as conditional and undecided.
5. Add the missing approvals (read access, moving files, any reference-file fetch, paid AI-judge calls).
6. Say who wrote the expected-verdict column (an AI checker) and explain 18 vs 21 pairs after the rescue.
7. Add a left/right-handed pair with verdict "same" and an ordered/disordered pair with verdict "specialists disagree".
8. Relabel the 0.309 / 0.745 figures as the pilot probe's, n = 55.
9. Replace "specialists carry the rule in their heads" with what the files support: the ideas are old (1990 classification, 2002 round robin with lenient human marking) and specialists disagree on some cases.

## Smallest useful first step
With the user's OK to read the two project folders: one read-only script that (a) counts the Dara scan files, (b) reproduces 12 of 40 and 17 of 40 from the stored marks and 32 of 40 by re-running the project's current lenient rule on the stored answer text, (c) lists the rows whose stored and recomputed marks differ (expected 15). Output: one small table and the list. No structure comparison, no change to the project, nothing sent.
