# K1 check - lens: newcomer feasibility and value skeptic

Candidate: K1, "Tricky-pairs table and a small marking function for XRD answers".
Reader assumed: one ML person, new to materials, no lab, part-time.
Sources used: digests/C16, digests/C15, digests/C04-2of2, digests/R10, synth/builds.md, synth/gaps.md, synth/glossary_usermodel.md, plan/merged.md, late2.txt. synth/critic.md does not exist. No web. I did not open the user's own project or any folder outside this scratchpad.
Words: XRD = powder X-ray diffraction [a 1-D curve of peaks measured from a powder]. Phase = one crystalline compound in the powder. Marking rule = the code that decides whether a program's list of phases "matches" the true list. CIF = a text file describing one crystal structure [where each atom sits]; programs like Dara pick their answer from a library of such files.

## Verdict: HOLDS WITH CHANGES

The idea is sound and it is the right size. But the first step as written cannot be done fully "from stored files", the approvals line is too optimistic, and the headline number (12 to 32 of 40) is mostly a text-handling fault, not a field-wide dispute. The changes below keep it honest and make a first result possible in one or two days.

## 1. Can the first step really be done this week with what is on disk?

Partly. Three blockers a newcomer would hit on day one:

1. **The 21-pair script is not here.** I searched this scratchpad: no file with "tricky" in its name. C16 says it sits in the sibling XRD session's temporary folder. If that folder is gone, about 10 of the pairs can be rebuilt from text in C16 (Nb2O5/Nb12O29, WO3/W18O49, TiO2/Ti9O17, Ca3SiO5/Ca2SiO4, YFeO3/Y3Fe5O12, a hydroxide/peroxide pair, "LaO3"/La(OH)3, "Ni1.875O2"/NiO, "V4O9.93316"/V2O5, the Y2O3 symmetry trap). Cost of that fallback: about a day. Also unexplained: the script has 21 pairs, the scores are quoted on 18 cases.

2. **The stored results hold formulas only.** C16: the user's marker "compares formulas only, and Dara's choice of reference file is discarded before grading"; the stored columns are gt_phases and rank1_phases. Two of the five proposed rules use StructureMatcher [a function in the pymatgen library that compares two crystal structures, not two formulas]. It needs a CIF for the program's answer AND a CIF for the true answer. Neither is in the stored results. So "re-mark the 40 weighed scans under each of five rules from stored files" is not possible. Only the formula-level rules can be re-run from storage. The structure-level rules need Dara to be run again on the 40 scans with the chosen reference file written down. C16 lists exactly that ("log the chosen reference file") as a fix that needs the user's approval, or it needs a wrapper script kept outside the project.

3. **The "true answer" for a weighed mixture is a bottle label, not a crystal structure.** To use any structure-level rule, someone has to decide which crystal form was in each bottle. That is a materials judgement. The 10 single-ingredient scans on disk are the right evidence for it, but it is not a five-minute job for a newcomer.

Also: 12 and 17 of 40 were recounted by the XRD session's own script (C16 lines 250-254). 32 of 40 is a quotation from a results note (P1 RESULT.md), not a recount. "Reproducing 32 from stored files" is plausible (C16 says 79 lenient-correct when recomputed vs 64 stored, out of 260) but nobody has shown it.

What IS doable in one or two days: the pair table under the formula-level rules, and a 40-row table with three marks per scan (strict as stored, lenient as stored, lenient recomputed with the current code).

## 2. Approvals: the candidate says "none to build privately". Not quite.

- Copying the script to a permanent folder: builds.md section D lists "move files to a folder the user names" as waiting for a go-ahead.
- Reading the user's two project folders (dara-conform and the P1 probe): the XRD session did this read-only, but the standing rule is "do not modify anything under the user's github folder", and this workflow was told not to open them at all. Whoever does the first step needs the user's explicit OK for read-only access.
- The project's plan is frozen (pre-registered 2026-07-09, C15). Its marking rules are written in that frozen plan (C16 line 29-31). Changing the marker after seeing results is a deviation. It must be written down as a dated amendment, with old-rule and new-rule numbers reported side by side. A newcomer could easily "just fix the bug" and quietly break the pre-registration.

## 3. Domain knowledge that would silently trip a newcomer

1. **Formulas vs structures** (above). The single biggest trap.
2. **No composition cut-off can work.** My own arithmetic on formulas quoted in C16 (composition distance = sum of absolute differences of atom fractions, the same measure the lenient rule uses): NiO vs "Ni1.875O2" = 0.0323, and these SHOULD count as the same compound. Nb2O5 vs Nb12O29 = 0.0139 and TiO2 vs Ti9O17 = 0.0256, and these must NOT count as the same. The should-be-same pair is further apart than the must-be-different pairs. So tuning the threshold cannot fix the lenient rule. The function needs the identity of the reference file the program chose (or a hand-made alias list), and when it has formulas only it must be allowed to say "cannot tell". (The three distances in C16 - 0.0139, 0.0373, 0.0256 - all reproduce exactly by this arithmetic.)
3. **A pair that sits exactly on the boundary.** YFeO3 vs Y3Fe5O12 has distance exactly 0.1000 (my arithmetic), which is the lenient rule's cut-off for compounds with three or more elements (C16 line 31). Its verdict can flip on "less than" vs "less than or equal" or on floating-point rounding. Good tricky pair; bad surprise if unnoticed.
4. **"0.15" is a TIGHTER setting, not a looser one.** builds.md says "0.15 or less separates" the two quartz forms, which is right. gaps.md line 157 calls it "looser", which is wrong (from my background knowledge the pymatgen default is 0.3; check the function's docstring locally). The 0.15 value was chosen on ONE pair. Nobody has counted how many genuinely-same pairs a tighter setting wrongly splits. Test that on a handful of same-phase pairs before adopting it.
5. **The quartz example may look academic to a specialist.** Background knowledge, not from the corpus: the second quartz form exists only when hot, so it should not appear in a room-temperature scan. It is a fine unit test for the comparison function; it is a weak headline example.
6. **Cases the proposed tiers miss.** (a) Two different compounds whose patterns a powder scan cannot tell apart [same atomic arrangement, nearly the same spacing]. The corpus has a live example: 311 of 687 reference files in the robot-lab set are one custom id-less "spinel" file (builds X3). Mirror-image crystals are another case and are already handled (merge them; section C). (b) Ordered vs disordered versions of one crystal: experts publicly disagree (C16, Leeman vs A-Lab), so one specialist cannot settle it. It needs a "contested" label, not a verdict. (c) Ingredients that change in air before the scan. The La(OH)3 case in C16 hints at this; "the answer is certain" is slightly too strong for weighed mixtures.
7. **Missing hydrogen.** Open reference files often leave hydrogen atoms out, which is why La(OH)3 reads as "LaO3". Ignoring hydrogen fixes that but merges a hydroxide with a peroxide (C16). There is no blanket rule; it is case by case.
8. **Licences.** Reference files derived from the paid library (ICSD) must not be shipped (C16, builds X3). The public table can name open (COD) file numbers only.

## 4. Who exactly would use it, and how would they find it?

- **User zero: the user's own project.** This is real and immediate. Its reported accuracy is 0.309 strict vs 0.745 lenient at n=55 (C16; these are consistent with 17 of 55 and 41 of 55 by my arithmetic). Any confidence or "not sure" result built on those labels means little until the marker is settled. Small correction to the candidate: C16 attributes the 0.309 / 0.745 figures to the P1 probe's result note in a sibling folder, not to dara-conform's own headline.
- **Outside users: weak.** "Anyone comparing phase-naming programs" is not a user. Named candidates from the corpus: the Dara maintainers, the group behind the trust score on top of Dara (AIF), and the authors of the two 2026 benchmarks that use AI judges (RADAR-PD, XRDBench). There is no discovery channel: an unknown newcomer's package will not be found. The only realistic route is a direct, short message from the user to one of those groups, after a specialist has looked at the rows. All of that needs the user's yes. Until someone outside asks for it, do not build a package, a website or a leaderboard; a CSV plus one Python file is enough.
- So the honest value statement is: certain value to one project now; outside value only if one named group picks it up.

## 5. How does it fail, and is failure cheap and informative?

| Failure | Cost | What you learn |
|---|---|---|
| Script is gone | about 1 day to rebuild from C16 text | nothing lost but time |
| Stored results lack reference files (expected) | a re-run of 40 scans; C16 gives "about 25 minutes of compute" for a similar 40-mixture job | proves the "log the chosen reference file" fix is needed |
| After sane formula clean-up, sensible rules agree on nearly all 40 scans | 1-2 days | the 12-to-32 swing was one project's text-handling fault. Shrink K1 to a test file for the user's project and stop. This is the key kill test and it is NOT measured anywhere in the corpus |
| Specialist disagrees with many draft verdicts | calendar time only | the answer key was wrong; record the disagreements, they are the product |
| Nobody will look at 25 rows | 2 weeks of waiting | per merged.md section 4, XRD stays an internal fix and the main effort moves elsewhere |
| A proper web check finds a working marker already exists (for example inside the Dara or AIF code) | hours | use theirs as the baseline rule; K1 becomes "tests for their marker" |

Every failure is cheap and tells the user something. That is the best feature of K1.

## 6. Smallest shippable version (hours to days) that still has value

One CSV and one table, nothing else:
1. The pair CSV with three formula-level columns (strict, lenient, a cleaned-formula rule), the draft expected verdict, and a one-line reason. Mark the expected-verdict column "AI-drafted, not yet reviewed by a specialist". Say "disagrees with the draft key", not "wrong", for the 8-of-18 and 13-of-18 figures.
2. A 40-row table: for each weighed scan, the true formulas, the program's formulas, and the three formula-level marks. Confirm 12, 17 and 32. For every row where the marks differ, put the two formula strings side by side and hand-sort into "spelling artifact" vs "real chemistry disagreement". That single count decides whether K1 is a small library or a bug-fix.
3. Two lines of arithmetic showing no cut-off can work (point 2 in section 3).

This already serves as a regression test for the user's own marker. Structure-level columns come second, and only for pairs where both sides have an open reference file on disk.

## 7. Would a domain expert take it seriously?

- In favour: specialists know "correct" is fuzzy. A 2002 contest used lenient human grading, and a 1990 crystallography-union paper already defines levels of similarity (C16, single checker). A tiered verdict matches how they think.
- Against: they will say "nobody marks by raw formula text from a reference file; that is a bug". They are largely right about the 12-to-32 swing. They will also spot that the pairs were chosen by non-specialists: the quartz example is academic, and the really contested cases (indistinguishable compounds, ordered vs disordered, air-changed ingredients) are thin or missing.
- The one thing that would make them take it seriously: one named practising diffraction person who (a) checks the verdict column and (b) supplies about 10 pairs the builders have never seen, with tier names tied to the 1990 vocabulary instead of invented ones. A strong second: include the Dara paper's OWN marking rule as a sixth column if its evaluation script is inside the package already installed on disk (no download). Without that, 32 vs 38 of 40 cannot be interpreted at all.

## 8. Effort, re-estimated for a part-time newcomer

- Formula-level pair table and 40-scan table: 1-2 days (if the script survives and read access is granted).
- Structure-level columns plus the re-run with reference logging: about a week.
- Function, runner and tests: 2-3 weeks part-time rather than 1-2.
- Specialist: outside the user's control; plan for it to take weeks and do not block internal use on it.

## 9. Claim-by-claim

| Claim | Result | Note |
|---|---|---|
| 12 / 17 / 32 of 40, same program, same scans | partly | 12 and 17 recounted by the XRD session's script; 32 is quoted from a results note; single source (C16); not opened here |
| 18 of 63 (28.6%) of 210 rows depend on the lenient rule | confirmed | C16 lines 43-46 and 255-259. The 210 rows include sets whose "true answers" are themselves opinions, so this is rule sensitivity, not accuracy |
| Strict wrong on 8 of 18, lenient on 13 of 18; three false merges | partly | Figures as quoted; the three distances reproduce by arithmetic; but the answer key is AI-drafted, and 21 pairs vs 18 scored is unexplained |
| Second result (3 of 20; 17 vs 4; 18 vs 7; 4 of 4 and 2 of 3) | confirmed | C04-2of2 lines 26 and 31, R10 line 32. Different item set (20 reaction products); the 3 flips are the second tool's verdicts |
| StructureMatcher default merges two quartz forms; 0.15 separates | confirmed | builds line 300; R10 line 31 (RMS 0.169). 0.15 is tighter, tuned on one pair, false splits unmeasured |
| 15 of 56 stale marks (64 vs 79 of 260) | confirmed | C16 line 193, single source |
| "dara-conform headline 0.309 vs 0.745 at n=55" | partly | C16 places these in the P1 probe's result note, a sibling folder |
| Data on disk, no download | partly | Scans, results and Dara: yes per C16. The pair script is not in this scratchpad. Stored results lack reference-file identity |
| "None to build privately" | partly | needs a folder go-ahead, read access OK, and a dated amendment to the frozen plan before any relabel |
| "No installable grader or rule card exists" | not found | one checker, no web here; also unchecked whether Dara's own package holds the paper's marking script |
| "Shrink to the evaluation harness" fallback exists; trust score published | partly | quoted in C16 line 32; trust score is a single-agent finding |
| "The marker moves the score more than the gap between programs" | partly | true as arithmetic (20 of 40 vs 3 of 40), but most of the swing is text artifacts; the residual after clean-up is unmeasured |

Nothing in K1 revives a refuted item. It correctly keeps mirror-image crystals merged, avoids StructureMatcher defaults, and does not use public answers as a hidden test.
