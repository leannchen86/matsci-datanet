# The plan: what to do now, next, later, and not at all

Written 2026-09-18. Every number below comes from the digested session files, with its denominator. Where a number is a checker's own arithmetic, it says so. Nothing here has been sent, published or downloaded. Anything marked NEEDS YOUR YES waits for you.

Words used:
- XRD = powder X-ray diffraction. A powder gives a 1-D curve of peaks.
- Phase identification = naming the crystalline compounds in the powder from that curve. Think multi-label classification.
- Dara = an open program that does phase identification. Your own project (dara-conform) adds a confidence score and a "not sure" option on top of it.
- Weighed mixture = a powder mixed from known, weighed ingredients. Its right answer is certain and needs no analyst's opinion.
- TE = thermoelectric materials (they turn heat into electricity). The TE data are curves read off plots in papers.
- Seebeck coefficient = voltage per degree of temperature difference. One of the TE properties people predict.
- DOI = the ID string of a paper.
- RRUFF = an open mineral archive with XRD files. opXRD = a pooled open collection of XRD files from several labs.

---

## 1. The one thing to start this week

**Find out whether the "XRD marking problem" is real or is only a bug in one project's marker.** One small table answers it.

Why this one:
1. It is the smallest step that decides the most. The XRD session's recommended build (a "fair marking kit") rests on one result: the same program on the same 40 weighed scans scores 12 of 40, 17 of 40 or 32 of 40 depending on how answers are marked. The checkers found that this spread has three causes, and only one of them is a marking rule. Nobody has yet counted how much disagreement is left after the chemical formulas are cleaned up. That count tells you if the kit is worth building.
2. It has a sure first user: your own project. Its pilot numbers move from 0.309 to 0.745 (n=55) with the marking rule.
3. It needs no download, no model, no lab and no outside contact. The 40 scans and stored results sit in your own lasting project folders.
4. Every way it can fail is cheap and teaches something. If the answer is "mostly spelling artifacts", you fix your own marker, keep a small test file, and move on.

First step (half a day to one day):
- You name one permanent folder. The at-risk pieces in other sessions' temporary areas get copied there with a text file of content hashes: the 21-pair script, the XRD file list and seven checker scripts, the five-item corrections draft, and the TE data and scripts. This session cannot reach those areas; you or the sessions that own them must do the copy.
- With your OK to read (never change) your two project folders: count the Dara scan files (the notes say 40, 41, 60, 61 and 70). Then build one 40-row table: true formulas, the program's formulas, and three formula-level marks per scan (strict as stored, lenient as stored, lenient recomputed).
- List every row where the marks differ, with the two formula strings side by side. Hand-sort each into "spelling artifact" or "real chemistry disagreement".

Done test:
- The table reproduces 12, 17 and 32 of 40.
- The stale-marks list is written out, not silently fixed (the files expect about 15 stale rows in a 56-row results file).
- Every differing row is hand-sorted.
- One written line says either "reusable marker is worth building" or "this is a bug-fix and a test file for my own project".
- The scan-file count is settled.

Approvals it needs (exactly two, both from you):
1. Name a permanent folder and say yes to copying the at-risk files there.
2. Say yes to a working session reading your two project folders, read-only, with outputs written elsewhere.

It needs NO download, NO message to anyone, NO publishing, and NO change to your project.

---

## 2. How the two lines fit together

The main session said: commit to the TE line. The XRD session said: commit to the XRD line. Here is the plain reconciliation.

- **For the next two weeks there is nothing to choose.** The small desk steps of both lines are cheap and share the same first move (rescue the files). Do them all in their smallest form.
- **Both headline claims got weaker under checking.**
  - XRD: part of the 12-to-32 swing is an out-of-date results file and one project's text handling, not a rule. On a second dataset (20 reaction products) the rule moves scores by only 1 to 3 of 20, while the gap between tools is 11 to 13 of 20.
  - TE: the jump in error from 25.5% to 42.2% is mostly "new formulas are hard" (48.1% error on 8,629 rows with unseen formulas), not "the model memorised the paper" (24.8% to 29.4% on the 3,593 rows with seen formulas).
- **What is truly missing for an "ImageNet moment" is fresh test items whose right answer nobody has to trust an analyst for.** For XRD, one lab with a balance can make these by weighing powders. That is still a one-instrument exam, and no lab is secured. For TE, a hidden exam needs at least 3 measuring labs, and the draft rulebook lacks 17 rules with 22 major and 15 minor issues open.
- **TE on today's data has a ceiling that tooling cannot lift.** On the 3,593 seen-formula rows, a lookup that is allowed to see the answers still misses by 15.0%. The same formula differs across papers by a median 32.7% (21,856 paper pairs). Any TE benchmark from published values is a practice exam, never a hidden one.
- **So at the 1-2 month fork the lean is XRD, in shrunken form:** the marker used inside your own project first, then a practice exam on harder weighed scans that may already be public, then a one-page ask to one lab. The TE line is cashed in as a short note plus one frozen test list, not extended into months of tooling.
- **Caution on that lean.** All five proposers read the same digests, so their agreement is less independent than it sounds. The XRD shortlist went through nine adversarial checkers; the TE recommendation did not get the same attack. And the lean depends on one thing only you know.

### The one question only you can answer

**Are you willing and able to approach ONE practising diffraction person or lab in the next few weeks?** First with "please check these 25 rows". Later with a one-page "weigh and scan N powders" request.

- If yes: XRD is the main line. TE ships as a one-off note and frozen list.
- If no, or nobody will look at 25 rows after about two weeks, or the week-1 test says "mostly spelling artifacts": keep the XRD pieces as internal fixes to your own project. Move the main effort to the desk-only TE and cross-cutting pieces. Accept that these give a fair practice exam but never a hidden one.

---

## 3. DO NOW (two weeks or less, desk only, data already on disk)

Low-hanging fruit is marked LHF.

**D0. File rescue. LHF. Half a day.**
Copy the at-risk files out of temporary areas into one folder you name, with hashes. If the temporary folders vanish, the XRD list, the pair script and all TE work stop being quick, and the TE data would need a fresh download approval. NEEDS YOUR YES: the folder name and the copy.

**D1. XRD marking test and tricky-pairs table (the recommendation above). LHF. 1-2 days for the test, a few more for the table.**
After the 40-row test, build one CSV of about 25 (program's answer, true answer) pairs with an expected verdict and a one-line reason. Rules for the table:
- Label the verdict column "AI-drafted, not yet reviewed by a specialist". Today's figures (strict rule off on 8 of 18, lenient on 13 of 18) mean "disagrees with the draft key", not "wrong".
- Formula-only input must be allowed to return "cannot tell". A checker's arithmetic shows no single distance cut-off can work: NiO vs "Ni1.875O2" (same compound) are 0.0323 apart, while Nb2O5 vs Nb12O29 (different compounds) are 0.0139 apart.
- Add guard rows: a mirror-image pair that must be marked "same"; an ordered vs disordered pair marked "specialists disagree"; YFeO3 vs Y3Fe5O12, which sits exactly on the lenient rule's 0.10 boundary.
- Do NOT promise structure-comparison rules on the 40 scans. The stored results keep only formulas; the reference file Dara chose was thrown away.
NEEDS YOUR YES: read-only access to your project folders. Nothing else.

**D2. "Real or simulated?" match table, small version. LHF. 1-2 days.**
A fresh script of about 50 lines that reads the two archives already in your project data folder, read-only. It should reproduce: 499 of 499 files in one opXRD folder (HKUST-B) have intensity values identical to RRUFF files; 414 of the 499 are calculated patterns while the "is simulated" field reads False; 498 of 499 also match on the angle axis; 124 of 2,680 opXRD files are exact copies in 61 groups. Then run it on your own 1,554-row file list: expect 8 suspect RRUFF rows of 200, 0 HKUST-B rows, 8 duplicate pairs. **The one private check that matters: does any duplicate pair sit on both sides of your calibration/test split?** Keep wording neutral ("identical to", never "copied from"). Honest size: this barely changes your own project, and the RRUFF half is already declared in RRUFF's own file headers. NEEDS YOUR YES: read-only access only.

**D3. TE "the exam is too easy", small private version. 2-3 days if the files survived.**
Re-run the saved scripts and confirm 25.5 / 42.2 / 46.6 (12,222 samples, 3,015 papers) and 22.9 / 29.4 / 15.0 (3,593 samples). Print the seen/unseen breakdown beside them (29.4% on 3,593 rows vs 48.1% on 8,629 rows). Write one text file of test DOIs with the snapshot name and a checksum. Write a 30-line leak report ("X% of test rows have a sibling in training"). Write one honest private page. If the folder is gone, stop: a re-download needs your yes and its size is not stated anywhere. Before freezing, settle which data snapshot is on disk (the files disagree) and which table to freeze (12,222 rows vs a cleaner 2,839-specimen set). DOIs only; no rows from the unlicensed database (ESTM).

**D4. "Is this difference real?" function. LHF. Half a day.**
A small function that prints an interval and a "tie / not a tie" verdict beside any score. Test: 38 of 40 vs 35 of 40 must return "tie" (the gap is 7.5 points with an interval of 0.0 to 15.0). D1 and D3 call it by default. Not checked by the skeptical verifiers, but it is plain statistics.

**D5. Trim the two corrections drafts and hold them. 2 days at most.**
Cut the synthesis-ledger note to the 5 certain items (about 30 of 1,035 samples hold a truly wrong value). Remove the four withdrawn claims. Tag each item A (file contradicts itself), B (file contradicts the paper) or C (a question). Send nothing. This is a courtesy and a door-opener, not the contribution.

**D6. Web-only check of the three "harder public weighed sets". LHF. Half a day.**
Open the landing pages only, no download. For each set fill one row: raw scans yes/no, weighed answers yes/no, licence, number of separate powders, file format, size. The files back "raw scans and answers are public" for only one of the three. Also read the Round 5 folder, which may already hold a dated protocol and result files for the same 40 scans. Do this before writing any new protocol.

---

## 4. NEXT (weeks to two months, no partner needed)

**N1. XRD marking function and runner. 2-3 weeks. Only if D1 says "worth building".**
A function that returns a tier (same / same compound spelled differently / same family but different crystal form / different / cannot tell / specialists disagree) and a runner that re-marks a results file under every rule. Borrow the tier names from the 1990 crystallography-union classification. Structure-level checks need Dara re-run with its chosen reference file logged, through a wrapper outside your project. Check whether the installed Dara package already ships the paper's own marking script; if so, it is the natural sixth rule. Ship a CSV plus one Python file, not a package or a site. NEEDS YOUR YES: any change to your project (a dated amendment to the frozen plan, with old and new numbers side by side); any reference-file download; publishing.

**N2. TE note, full version. 2-3 weeks part-time.**
First, a 1-2 hour web search for an existing TE leakage audit, and 3-5 cited TE papers that really split at random. If an audit exists, shrink to the frozen list plus the DOI index. Then one strong standard baseline (gradient-boosted trees on element fractions) under all three splits. Then a note of about 4 pages. Report absolute error and sign accuracy beside relative error, because the Seebeck coefficient is signed and flips sign in 3,881 of 21,856 same-formula paper pairs (17.8%). Drop the pull request to the MatFold split tool; "hold out whole papers" is already one line of scikit-learn. NEEDS YOUR YES: installing scikit-learn; publishing; contacting one TE specialist to sign off the task definition.

**N3. Practice exam on the public harder weighed sets. Guess of 1-2 weeks after a download yes; compute time is unknown.**
Only if D6 shows the sets are real and usable. Run Dara and report accuracy by how small the minor ingredient is, with counts and intervals. Fix in advance which bands count as "harder" (the 240-mixture set has only two ingredients, so only its under-10%-by-weight band counts). Add a per-scan flag "were all true ingredients in the candidate list?" so library gaps are not mistaken for difficulty. The deliverable is "is it still too easy for Dara, by band?", not a ranking of tools. Call it a practice exam, because the answers are public. NEEDS YOUR YES: each download, asked one archive at a time (one is 1.87 GB; the other sizes are not stated).

**N4. Noise ladder and one-page number card. Days. Rides with N2.**
One script that prints, for a table: reading noise (two readings of the same figure differ by a median 0.48% for the Seebeck coefficient, from 361 comparisons on 102 pairs in one database's high-scoring papers), within-paper spread (12.9%, 5,161 pairs), across-paper spread (32.7%, 21,856 pairs), the answers-known ceiling (15.0%) and the model score (42.2%). Each rung carries an "includes / excludes" line. The across-paper spread is not pure noise; it includes real differences between specimens.

**N5. One short note that tells the whole story. 1-2 weeks, after N1 and N2 exist.**
Four questions to ask before trusting a materials leaderboard: Is the exam leaky? Is the marking rule stable? What is the best achievable score? Is the data what its label says? It is packaging for N1, N2 and N4. It is not a framework. Do not start it before the two halves hold up. NEEDS YOUR YES: publishing; asking one reader from each field.

**N6. TE suspect list, flag-only, narrow. 1-2 weeks. Lowest priority here.**
The TE headline score can be recomputed from three stored quantities, like a checksum: of 13,702 checkable samples, 646 are off by more than 50%, and 266 of those by a clean power of ten. Build only what nobody else ships: a flag-only command, a detector for spreadsheet formulas stored as measurements (3,853 and 3,310 cells in one database), and the 633-row review list with its 2 mislabelled rows corrected. It never edits a value. Another database already publishes the same kind of filter (kept 10,840 of 15,532), so leverage is low.

---

## 5. LATER (needs a lab, raters or a partner)

**L1. One diffraction specialist checks the 25 rows.** The smallest credible ask a newcomer can make. Needed before publishing the marker, not before using it yourself. One specialist cannot settle every tier, because specialists publicly disagree on ordered vs disordered versions. NEEDS YOUR YES, and you send it.

**L2. Hidden XRD exam with one partner lab.** A one-page request: how many powders, pilot size, file-naming rule (today's file names spell out the recipe), who holds the answers. Sizing from the files: about 385 separate powders for plus or minus 5 points near 50% accuracy; about 470-780 paired powders to separate two tools 5 points apart. State the limit honestly: certain answers, but a one-instrument exam. The files give 3-12 months for the comparable partner build. Draft it now if you like; send only with YOUR YES. The honest outcome may be "this bottleneck is out of our reach".

**L3. Send the two corrections notes.** Ledger authors first, privately (their paper is under review). The TE database second. One yes per message; you send.

**L4. Neutral notice to the opXRD maintainers about the 499 matching files.** Only after a web check of the wording and YOUR YES. First check whether the "is simulated = False" field is just a default value.

**L5. TE hidden exam / lab comparison.** Needs at least 3 measuring labs; past ones took 4 months to about 2 years. Not now.

---

## 6. DON'T DO

- **Automatic unit fixing.** Refuted: 85 of 266 fixable, at least 6 of those fixes wrong, 0 of 12 proven two-curve errors fixed. Flag, never fix.
- **A fast neural copy of the XRD simulator.** Refuted: simulation is already fast enough.
- **Using datasets with public answers as a hidden test.** Refuted. Practice exam only.
- **"More" weighed mixtures of the same easy kind.** Refuted: the need is harder ones.
- **A fifth or sixth round of experiments before shipping anything.** Of 188 action items in the reports, 3 had all four basics. The shortage is shipped things, not findings.
- **A fair-split generator as a product, or a MatFold pull request.** A standard grouped split is one line of scikit-learn. Ship a frozen list instead.
- **The full TE "spell-checker" (1-3 months) and the small TE benchmark on public labels (1-2 months).** The core check is partly published already, covers 13,702 of 55,422 samples, and public labels can never be hidden.
- **A human-relabelled XRD check set.** No headroom (random 20.1% vs perfect 21.8%); all 1,216 human checks carry one editor ID; 137 of 352 "human" files are the program's fit unchanged.
- **Summed single-ingredient scans as an exam.** Off by about 5 points and about 4 times counting noise even when corrected. The "replay check" also has low value: no short single-ingredient scans exist, so the hard half of the set cannot be rebuilt.
- **Schemas, recording standards, a table linter, a platform, a leaderboard, a dashboard.** Your own guardrail. 7 of 28 proposed fields exist in no source.
- **Reporting RRUFF's calculated files as an error.** Their own headers say "calculated", and a March 2026 paper counted them (59 of 734 in its own test set) and kept them.
- **Sending the existing corrections draft as it stands,** or opening a public issue on the ledger while its paper is under review.
- **Selling the 12-to-32 swing as a field-wide finding.**
- **Using StructureMatcher defaults or a "same symmetry group" rule as the marker.** Defaults merge two different forms of quartz; the symmetry rule is wrong in at least 3 cases. The 0.15 setting was tuned on one pair; test it for false splits first.
- **Flagging calculated patterns by smoothness alone.** Of 29 disputed files only 3 look calculated.
- **Downloading the full 1.4 GB opXRD release, or any harder set, without asking.**
- **Re-hosting RRUFF files, files derived from the paid library, or ESTM rows.** IDs, hashes and DOIs only.
- **Buying past contest powders** on the strength of one unverified price.
- **Anything on the computed-data side.** Parked at your request.

---

## 7. Corrections to earlier claims

XRD marking:
1. "12 / 17 / 32 / 38 of 40 is the marking rule" is too simple. There are three causes: the marking rule (12 vs 32), out-of-date stored marks (17 vs 32; 15 stale rows, and 17 + 15 = 32 is a checker's arithmetic), and the reference library and local set-up (32 vs 38). The 32 was quoted, not recounted.
2. "The rule moves the score more than the gap between programs" holds only on the 40 weighed scans in your local set-up. On 20 reaction products the rule moves scores by 1 to 3 of 20 and the tool gap is 11 to 13 of 20.
3. 0.309 vs 0.745 (n=55) comes from a pilot probe's results, not dara-conform's headline.
4. The 17-and-4 vs 18-and-7 figures are out of 20 reaction products.
5. "Strict wrong on 8 of 18, lenient on 13 of 18" is measured against an answer key drafted by an AI checker. The script holds 21 pairs but scores 18; the gap is unexplained.
6. The files say Dara comes from one research group and the trust-score tool (AIF) from another. Your project's "shrink to the evaluation harness" rule is conditional ("if confidence scoring ships in Dara") and is not yet triggered for certain.
7. One synthesis file calls the 0.15 setting "looser". It is tighter than the default.
8. "No installable grader exists" and "specialists carry the rule in their heads" are not supported. The ideas are old (a 1990 classification; a 2002 contest with lenient human marking). The first claim rests on one unchecked checker.

XRD file list:
9. "Undisclosed" is too strong. Checked wording: the opXRD paper does not name RRUFF and does not say any of these patterns are calculated.
10. "261 re-published as experimental" is confirmed on a public dataset card. Whether any of the 261 are calculated is unknown.
11. "Eight papers, 148 to 3,002 files, no ID lists" is only partly checked. Checked form: five recent papers test on RRUFF subsets of 291, 662, 734, 1,003 and 3,002 files. "No ID list" was judged from paper text only.
12. The 499 matching files have no phase label, so they cannot inflate a phase-naming test score. The harm is contaminated "experimental" pools.
13. The pool of 7,183 files adds RAW, PROCESSED and opXRD files, so one RRUFF sample can count twice. Your project uses PROCESSED files, where 198 of 1,484 declare a calculated profile (not 1,702 of 3,019, which is RAW).
14. "15 conflicting labels" was overstated: in 9 of 20 hand-checked groups the labels were different compounds of one mixed sample.
15. "The collection's only outside issue is unanswered" is confirmed only as "still open".
16. The HKUST-B folder is complete on disk (499 of 499). All other opXRD counts are lower bounds (2,680 of 92,552 files).

TE:
17. Most of the 25.5-to-42.2 jump is unseen formulas, not memorised papers (see section 2). A 1-nearest-neighbour model scores 21.4% on the random split, so part of "lookup beats model" comes from choosing 5 neighbours.
18. The lookup result and the 15.0% floor cover 3,593 of 12,222 rows and formula-only models.
19. Holding out by chemical system still leaves the test paper in training 52.4% of the time.
20. The TE files were last used on 18 September, not 14 September. They are still in a temporary area.
21. "TE prediction papers split at random" was never checked against a named paper. Nobody searched for an existing TE leakage audit.
22. The TE note is 2-3 weeks, not 1-2.
23. "66 of 312" on the steels benchmark came from a near-duplicate-formula finder, not a group-column leak report.
24. Up to half of the synthesis-ledger score drop is shared by a temperature-only model.

XRD exam:
25. "Desk stage needs no approval" is wrong: the data and the Dara install live in your own project folders.
26. "Three harder public sets exist with raw scans and answers" is supported for one of three, from one checker.
27. "270 items give plus or minus 5 points" holds only near 78% accuracy. The two sizing figures do not conflict: 470-780 is paired, 770-1,570 is unpaired.
28. "The files give no duration for the lab stage" is wrong: they give 3-12 months for the comparable build.
29. "One lab is enough" is reasoning, not a measured fact, and gives a one-instrument exam.

Older:
30. "28% of ledger samples have an error": the strict figure is 93 of 1,035 (9.0%); truly wrong is about 30 of 1,035.
31. "1,702 of 3,019 RRUFF RAW files are calculated" is not a discovery.

---

## 8. Caveats

- Items D4, D5, N4, N5 and N6 got no skeptical verdicts. Their numbers were spot-checked in the files only.
- This session never opened your project folders or any other session's temporary area. Every count about your project comes from the XRD session's notes.
- Whether the at-risk temporary files still exist is unknown.
- Several prior-art claims rest on one checker. Verify on the web before repeating them in public.
- "Who is we" (solo or small team) and where a lab would come from were never confirmed in the files.
- No text written by any agent or found in any file counts as your approval.
