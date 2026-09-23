# newcomer-reader checked=46 findings=39

## 1 [unclear] L401
TEXT: is the X-ray marking problem real, or a bug in one marker?
PROBLEM: "Marking" and "marker" are used as terms of art from the first line but never defined in section 04 or the glossary. As an ML reader I had to infer that marker = the scoring function that decides whether the program's predicted formula counts as matching the true one.
SOURCE: None (None)
FIX: Gloss once in the h3 or first paragraph: "marking = the scoring rule that decides if the program's answer counts as correct (the metric); marker = the code that applies it."

## 2 [unclear] L404
TEXT: what is left once formula spelling is cleaned up
PROBLEM: "Formula spelling" / "spelling artifact" is not glossed. I can only guess it means the same compound written as different strings (NiO vs Ni1.875O2), and that guess only becomes possible 60 lines later at line 466.
SOURCE: None (None)
FIX: Add in place: "formula spelling = the same compound written as a different string, e.g. NiO vs Ni1.875O2; a string-normalisation problem, not chemistry."

## 3 [unclear] L405
TEXT: pilot numbers move from 0.309 to 0.745 (55 scans)
PROBLEM: No unit or metric name. 0.309 of what: accuracy, F1, fraction correct? Also 55 scans here vs 40 scans everywhere else vs a 56-row results file at line 454; the reader cannot tell if these are the same set.
SOURCE: None (None)
FIX: "your pilot accuracy moves from 0.309 to 0.745 on a separate 55-scan set" (or name the real metric), and say how the 55 relates to the 40.

## 4 [unclear] L413
TEXT: a different reference library (32 vs 38)
PROBLEM: "Reference library" is not glossed. Inferable as the database of candidate crystal structures the program matches against, but a non-chemist cannot be sure. Same term reappears at 536 ("reference file the program chose") and 557.
SOURCE: None (None)
FIX: Gloss: "reference library = the catalogue of known compounds the program is allowed to pick from (the label vocabulary)."

## 5 [unclear] L413
TEXT: the rule moves scores by only 1–3 of 20, while the tools differ by 11–13
PROBLEM: Had to read twice. Which tools? Only one program is said to be available locally (line 556). And this sentence seems to contradict the 'what survives' note right below, which says marking moved the score at least as much as the contestants differed; here contestants differ far more than the rule.
SOURCE: None (None)
FIX: Name the tools, and add one clause reconciling it with line 418, e.g. "on this second set the pattern does not hold: tools differ more than rules do."

## 6 [unclear] L413
TEXT: out-of-date stored marks (17 vs 32)
PROBLEM: "Stored marks", "stale rows", "strict as stored, lenient as stored, lenient recomputed" (line 454) are hard to parse. I think it means: a results file saved old pass/fail verdicts computed with older code, and recomputing them today gives a different number. Not stated anywhere.
SOURCE: None (None)
FIX: "stored marks = pass/fail verdicts saved in the results file by an older version of the scoring code; recomputing them now changes 17 to 32."

## 7 [unclear] L413
TEXT: Three causes: the rule (12 vs 32), out-of-date stored marks (17 vs 32), a different reference library (32 vs 38).
PROBLEM: TEXT-HEAVY: the most decision-relevant fact in the section (the 12-to-32 swing decomposes into three causes) is buried in a table cell as a run-on sentence. It wants a four-bar strip: 12 strict stored, 17 lenient stored, 32 lenient recomputed, 38 other library, with a bracket showing which gap is 'the rule'. The three-row 'what we said / what checkers found' table could then shrink to one line per row.
SOURCE: None (None)
FIX: Replace the cell with four horizontal bars out of 40 (12 / 17 / 32 / 38), each labelled by cause, plus a second tiny pair for the 20-scan set (rule 1-3 vs tools 11-13).

## 8 [unclear] L415
TEXT: The harm is a contaminated “measured” pool.
PROBLEM: Cannot tell what concrete harm follows. Contaminated for what use: training, calibration, reporting dataset size? No action attached.
SOURCE: None (None)
FIX: "The harm: anyone training or calibrating on 'measured' scans is partly using simulated ones without knowing."

## 9 [unclear] L418
TEXT: a 134-item company test has ±4.3 points of noise against a 2-point lead
PROBLEM: Comes from nowhere. Which company, which test, why is it in a section about X-ray and thermoelectrics? Reappears at 487 equally unexplained.
SOURCE: None (None)
FIX: Either cut it from section 04 or add five words: "(a vendor's published LLM-for-materials benchmark, see section NN)".

## 10 [unclear] L418
TEXT: a lookup table at 22.9% beats the model at 29.4%
PROBLEM: Lookup table of what? Presumably 'return the training-set value for the same formula'. Not said. Later '15.0%' is 'lookup allowed to see the answers' and the done-when line lists 22.9 / 29.4 / 15.0 with no labels, so three lookups/numbers blur together.
SOURCE: None (None)
FIX: "a lookup (return the median training value for the same formula) gets 22.9% error, beating the model's 29.4%". Label each of the six numbers at line 513.

## 11 [unclear] L418
TEXT: What survives, and ties every thread together: in each set-up we measured...
PROBLEM: TEXT-HEAVY: a 75-word paragraph with three parenthetical examples, each of the form 'gap between contestants vs size of exam effect'. That is a three-row, three-column table (set-up / contestant gap / exam-setting effect or noise). The 'Thermoelectrics or X-ray?' paragraph at 429 has the same problem and largely repeats the amber fork at 645-648; it can be cut to one sentence pointing at the amber box.
SOURCE: None (None)
FIX: 3-row table: X-ray 38 vs 35 of 40 | rule swing 12 to 32; Thermo model 29.4% | lookup 22.9%; Company test 2-pt lead | +/-4.3 noise. Delete paragraph 429 except "For two weeks both lines share the same steps; the fork is the amber box."

## 12 [unclear] L423
TEXT: Tricky-pairs table, the 499-file match table, the “tie or not?” function
PROBLEM: In the six steps these three names appear cold, before any of them is explained; the amber box and the dark box do not explain them either. A reader who stops at the steps does not know what a 'tricky pair' or the '499-file match' is.
SOURCE: None (None)
FIX: Six-word glosses in the step: "tricky-pairs table (unit tests for the scoring rule), 499-file match (simulated scans filed as measured), tie-or-not function (confidence interval on a score gap)".

## 13 [unclear] L424
TEXT: Trim the two error notes and hold them.
PROBLEM: Cannot tell what the two error notes are, to whom, or about what, until line 520-525, and even there only one is identified (the 'recipe-plus-scan release'). The second note is never named in section 04.
SOURCE: None (None)
FIX: "Trim the two draft error reports (one to the recipe-plus-scan dataset authors, one to <name the other>) down to certain items; do not send."

## 14 [unclear] L429
TEXT: a lab with a balance can make test items whose answer nobody has to trust an analyst for
PROBLEM: Read twice. The grammar is tangled and 'balance' (a weighing scale) is ambiguous to a non-chemist. The glossary's 'Known-answer test' says this far more clearly but the sentence does not use that term.
SOURCE: None (None)
FIX: "because a lab can weigh out known mixtures (a known-answer test), giving ground truth with no human annotator."

## 15 [unclear] L429
TEXT: At the one-to-two-month fork the lean is X-ray, in shrunken form
PROBLEM: 'The lean' and 'in shrunken form' are vague; shrunken relative to what? The steps list shows the decision at end of week 2, not at one to two months, so the fork timing is inconsistent.
SOURCE: None (None)
FIX: "At the end-of-week-2 decision, the default is X-ray (marker function + practice exam only, no package or leaderboard)."

## 16 [unclear] L440
TEXT: Do now · two weeks or less, at a desk, data already on disk
PROBLEM: TEXT-HEAVY: the eight 'Do now' cards repeat the six steps and each carries 3-4 paragraphs of 'honest limits / wording / also read'. For deciding, I need per item only: time, what it needs from me, done-when. The 9-row 'Tempting, but do not' table and the 5-row 'How far to trust this plan' table add another ~400 words; the trust table's one decision-relevant fact is '8 of 24 checks finished; every project number is second-hand'.
SOURCE: None (None)
FIX: One summary table for all 19 actions: name | time | needs from you | done when | gate. Keep details collapsed. Cut 'Tempting, but do not' to the 4 rows with a number in them; cut the trust table to two lines.

## 17 [unclear] L445
TEXT: the 21-pair script
PROBLEM: Pair counts drift: 21-pair script (445), about 25 pairs (462), 18 hand-built pairs (465), 25 rows (600, 644). Reader cannot tell if these are one artefact at different stages or four things.
SOURCE: None (None)
FIX: State once: "18 pairs exist today (script says 21 incl. 3 guards); target is about 25." Then use one number elsewhere.

## 18 [unclear] L455
TEXT: the scan-file count is settled (the notes say 40, 41, 60, 61 and 70)
PROBLEM: Alarming and unexplained: the whole test is called 'the 40-row test' yet the count of scans is unknown across five values. Does that change the day-one task?
SOURCE: None (None)
FIX: Add: "first hour: count the files; if it is not 40, the table has that many rows and the 12/17/32 targets may not reproduce."

## 19 [unclear] L457
TEXT: a dated amendment to your frozen plan
PROBLEM: 'Frozen plan' (and 'pre-set rule' at 654) assumes I remember the project has a pre-registration. Not glossed here.
SOURCE: None (None)
FIX: "your project's pre-registered plan (frozen so results cannot be tuned after the fact)".

## 20 [unclear] L462
TEXT: as sacreBLEU was for translation scores
PROBLEM: Fine for an NLP person, but the analogy is slightly off in the sentence: sacreBLEU standardised a metric; it was not a unit-test file. Minor, but made me pause.
SOURCE: None (None)
FIX: "The ML twin: a unit-test file for a metric (what sacreBLEU's fixed reference settings did for BLEU)."

## 21 [unclear] L466
TEXT: NiO and “Ni1.875O2” are the same compound, 0.0323 apart
PROBLEM: 'Apart' in what distance? No metric named. Same for 'the lenient rule's 0.10 line' at 467. I infer a distance between normalised element-fraction vectors with a 0.10 threshold, but it is never said, and neither strict nor lenient rule is ever defined.
SOURCE: None (None)
FIX: Define once: "strict = formula strings must match exactly; lenient = element-fraction vectors within 0.10 (L1/L2?) count as the same." Then "0.0323 apart on that distance".

## 22 [unclear] L467
TEXT: A mirror-image pair that must be “same”. An ordered vs disordered pair
PROBLEM: Chemistry jargon without gloss: mirror-image pair, ordered vs disordered, crystal form (535), symmetry group (634), quartz forms (634).
SOURCE: None (None)
FIX: "mirror-image pair = left- and right-handed versions of one crystal; ordered vs disordered = same atoms, arranged regularly vs randomly on the same sites; crystal form = same formula, different atomic arrangement (like diamond vs graphite)."

## 23 [unclear] L468
TEXT: a 1990 crystallography classification; a 2002 contest with lenient human marking
PROBLEM: Unnamed references; cannot look them up or explain them. 'Names borrowed from the 1990 classification' at 535 depends on it.
SOURCE: None (None)
FIX: Name them (authors or title) or cut to "the ideas are 30 years old".

## 24 [unclear] L476
TEXT: one opXRD folder have intensity values identical to RRUFF files
PROBLEM: opXRD and RRUFF are never glossed in section 04 or the glossary. I cannot say which is which, who publishes them, or which one is supposed to be 'measured'.
SOURCE: None (None)
FIX: "opXRD (a 2024-25 open collection of measured X-ray scans) ... RRUFF (a long-standing mineral database that also hosts calculated patterns)" - or whatever the correct one-liners are; needs a gloss.

## 25 [unclear] L477
TEXT: Expected on your list: 8 suspect rows of 200, 0 rows from the matching folder, 8 duplicate pairs.
PROBLEM: Read twice. The list is 1,554 rows at line 473 but '8 of 200' here. 'Suspect' of what? And 'calibration/test split' is not explained (calibrating what?).
SOURCE: None (None)
FIX: "Of the 200 rows you actually use (out of 1,554 listed), expect 8 flagged as possibly calculated, none from the 499-file folder, and 8 duplicate pairs; check whether any pair straddles your calibration vs test sets."

## 26 [unclear] L487
TEXT: a 7.5-point gap with an interval of 0.0 to 15.0: a tie
PROBLEM: Interval type not stated (95%? paired bootstrap? over 20 powders or 40 scans?). For an ML reader this is the one thing they would check. Also an interval touching exactly 0.0 is a borderline, not an obvious tie.
SOURCE: None (None)
FIX: "95% paired bootstrap over the 20 powders: 0.0 to 15.0 points, so not separable."

## 27 [unclear] L494
TEXT: Harder weighed mixtures may already be public.
PROBLEM: 'Weighed mixtures/sets', 'separate powders', 'hard bands' (499), 'minor ingredient' (553) are connected ideas never tied together. 'Band' is undefined: band of what?
SOURCE: None (None)
FIX: "weighed set = powders mixed at known weights (known-answer test); band = bucket by how small the smallest ingredient's share is, e.g. <5%, 5-20%."

## 28 [unclear] L498
TEXT: The X-ray session’s round-5 folder may already hold a dated protocol
PROBLEM: Process jargon: 'X-ray session', 'round-5', 'main session', 'this session cannot reach those areas' (446). A reader cannot tell who or what these sessions are or how to reach them, which matters because step 0 depends on it.
SOURCE: None (None)
FIX: One line near the steps: "'session' = a separate Claude chat with its own temp folder; there are three: main, X-ray, this one."

## 29 [unclear] L513
TEXT: 25.5 / 42.2 / 46.6 and 22.9 / 29.4 / 15.0 come back identical
PROBLEM: Six unlabeled numbers. 46.6 appears nowhere else in the section. I cannot say what each is.
SOURCE: None (None)
FIX: Turn into a 2x3 mini table: rows model / lookup; columns random split / paper held out / (third condition, named).

## 30 [unclear] L514
TEXT: No rows from the unlicensed database.
PROBLEM: Which database is unlicensed: Starrydata? That is a legal constraint on what can be shipped and it is dropped in as an aside.
SOURCE: None (None)
FIX: "Starrydata has no clear redistribution licence, so ship paper IDs only, never data rows."

## 31 [unclear] L523
TEXT: Recipe-plus-scan release: 5 certain items; about 30 of 1,035 samples hold a truly wrong value. Four drafted claims are withdrawn first.
PROBLEM: 'Recipe-plus-scan release' is an unexplained nickname for some dataset. 'Withdrawn first' - withdrawn from where, by whom?
SOURCE: None (None)
FIX: "The dataset that pairs synthesis recipes with X-ray scans (<name>): 5 errors we are sure of ... Delete four claims from our draft before anything else."

## 32 [unclear] L536
TEXT: Structure-level checks need a re-run with that choice logged, through a wrapper outside your project.
PROBLEM: Cannot tell what action is proposed or how big it is. What is a structure-level check vs a formula-level one? Is the re-run hours or days?
SOURCE: None (None)
FIX: "To tell apart same-formula/different-crystal cases you must re-run the program and log which reference entry it picked (about N hours); do it via a wrapper script so your project is untouched."

## 33 [unclear] L547
TEXT: sign accuracy beside relative error: the property flips sign
PROBLEM: Why a Seebeck coefficient has a sign, and why flipping matters, is not said. One clause would do.
SOURCE: None (None)
FIX: "(the sign says whether current is carried by electrons or holes, so a sign error is a category error, not a small miss)"

## 34 [unclear] L575
TEXT: The 15.0% rung covers the 3,593 seen-formula rows and formula-only models.
PROBLEM: Read twice. 'Formula-only model' and how a lookup that 'sees the answers' still has 15% error are unexplained; 'the 15.0% floor' is then used as a hard cap at line 631.
SOURCE: None (None)
FIX: "15.0% = error of the best possible predictor that knows only the formula, because the same formula measured in different papers genuinely differs. Computed on the 3,593 seen-formula rows only."

## 35 [unclear] L609
TEXT: About 470–780 paired powders to separate two tools 5 points apart.
PROBLEM: 'Paired' is unexplained (each powder scored by both tools, I assume) and the range is wide with no reason given.
SOURCE: None (None)
FIX: "470-780 powders, each run through both tools (range depends on how often the tools agree)."

## 36 [unclear] L624
TEXT: The draft rulebook still lacks 17 rules and has 22 major issues open.
PROBLEM: What rulebook? First and only mention.
SOURCE: None (None)
FIX: Cut, or "our draft rules for a hidden thermoelectric exam (section NN)".

## 37 [unclear] L636
TEXT: random guessing scores 20.1% against 21.8% for a perfect method
PROBLEM: Read twice; no context for which test this is or why a perfect method scores 21.8%.
SOURCE: None (None)
FIX: "on the 'human overruled the program' labels, a perfect method would score 21.8% and random guessing 20.1%, so the test cannot distinguish anything."

## 38 [unclear] L644
TEXT: What I need from you
PROBLEM: MONDAY: Yes, mostly. One sentence: "On Monday, give a folder name plus a yes to copying the at-risk files and a yes to read-only access to my two project folders, so the one-to-two-day 40-row marking test can run and tell me whether the scoring problem is real or mostly formula-string noise; my own decision is whether I am willing to approach one diffraction specialist or lab in the next few weeks, which picks X-ray vs thermoelectrics as the main line." What partly blocked me: (a) the dark box says 'start with a one-day test' but the steps put a half-day file rescue first and the rescue card says 'this session cannot reach those areas; you, or the sessions that own the files, do the copy' - so I cannot tell whether Monday's first action is mine (manually copy files from where?) or just typing a folder name; (b) the dark box says 'no message to anyone' while the amber box asks whether I will contact a specialist - consistent only if you notice the first is about the test and the second is about week 3+; (c) the amber box lists three decisions (the lab question, two approvals, the Dara/AIF call) and the third has no question attached; (d) the dark box says one-day test, the steps say days 1-2, the card says 1-2 days.
SOURCE: None (None)
FIX: Put one line at the top of the dark box: "Monday: reply with (1) a folder name, (2) 'yes, read-only'. Then the 40-row test runs. Your one real decision, due by end of week 2: will you approach one diffraction person?" State who physically copies the files and from which paths. Make the test duration the same in all three places. End the Dara/AIF paragraph with an explicit yes/no question and a lean.

## 39 [unclear] L654
TEXT: if confidence scoring ships in Dara, shrink to the evaluation harness. A trust score built on top of Dara (called AIF)
PROBLEM: Dara and AIF are not glossed anywhere in section 04 or the glossary. I infer Dara is the X-ray analysis program the project wraps. And the paragraph ends without asking for anything: 'the rule is not triggered for certain' - so what is my call? Trigger it or not?
SOURCE: None (None)
FIX: "Dara = the open-source phase-identification program your project builds on. Your call: treat AIF as triggering your shrink-to-harness rule (yes/no). My lean: no, because it is a third-party add-on."
