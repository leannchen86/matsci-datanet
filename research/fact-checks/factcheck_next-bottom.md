# factcheck:next-bottom checked=46 findings=12

## 1 [unclear] L537
TEXT: it is the natural sixth rule
PROBLEM: 'Sixth' presumes the reader knows there are five marking rules; nothing in this card says so, and the tier list just above has six tiers, inviting confusion between tiers and rules.
SOURCE: if so, it is the natural sixth rule (plan/plan.md:104)
FIX: If so, add it as one more marking rule beside the five already compared.

## 2 [overstated] L574
TEXT: Cleaner plot-reading would buy almost nothing.
PROBLEM: Overstated. The 0.48% reading-noise figure comes from 361 comparisons on 102 pairs in one database's high-scoring papers only; the same check found more than 10% disagreement in 15 of 361. The page gives scope limits for two other rungs but not for this one.
SOURCE: median 0.48% ... from 361 comparisons on 102 pairs in one database's high-scoring papers / more than 10% disagreement in 15 of 361 (4.2%) (plan/plan.md:113; synth/builds.md:246; synth/storyline.md:299)
FIX: Add to Honest limits: 'The 0.48% rung is 361 comparisons on 102 pairs from one database's top-scoring papers; 15 of 361 still differ by more than 10%.' Soften to 'Cleaner plot-reading looks like a small part of the gap.'

## 3 [unclear] L616
TEXT: The two error notes (recipe-plus-scan authors first, privately)
PROBLEM: Drops the reason and the second recipient: the plan says the first note goes privately because those authors' paper is under review, and the second goes to the thermoelectric database; also the plan forbids sending the existing draft as it stands (must be trimmed to the 5 certain items first).
SOURCE: Ledger authors first, privately (their paper is under review). The TE database second. / Don't: sending the existing corrections draft as it stands (plan/plan.md:129, :150)
FIX: The two trimmed error notes: recipe-plus-scan authors first and privately (their paper is under review), the thermoelectric database second; plus a neutral notice about the 499 matching files.

## 4 [overstated] L631
TEXT: the 15.0% floor caps what a formula-only model can show
PROBLEM: Missing scope required by correction 18: the 15.0% floor was measured only on the 3,593 seen-formula rows of 12,222, not on the whole benchmark.
SOURCE: The lookup result and the 15.0% floor cover 3,593 of 12,222 rows and formula-only models. (plan/plan.md:185 (correction 18))
FIX: ...and on the 3,593 of 12,222 rows with seen formulas, even a lookup that sees the answers misses by 15.0%.

## 5 [overstated] L636
TEXT: About 1,000 expert-hours
PROBLEM: The 1,000 expert-hour figure in the sources is for the combined known-answer hidden set plus multi-rater pilot (3 experts per pattern, with a lab), not for expert re-labelling alone; and it is not in the final plan's don't-do entry, which instead cites one editor ID on all 1,216 human checks and 137 of 352 'human' files being the program's fit unchanged.
SOURCE: B11 (known-answer + multi-rater together): 'about 10^3 expert-hours; 3-12 months' / plan: No headroom (random 20.1% vs perfect 21.8%); all 1,216 human checks carry one editor ID; 137 of 352 'human' files are the program's fit unchanged. (plan/verify_K4_evidence.md:35; synth/storyline.md:276; plan/plan.md:146)
FIX: Random guessing scores 20.1% against 21.8% for a perfect method, all 1,216 human checks came from one person, and 137 of 352 'human' files are the program's fit unchanged. Nothing to win.

## 6 [unclear] L638
TEXT: Of 188 action items in the reports, 3 had the basics.
PROBLEM: Count is of items having ALL FOUR basics; 'had the basics' drops what is being counted and the basics are never named.
SOURCE: Of 188 action items in the reports, 3 had all four basics. (plan/plan.md:143)
FIX: Of 188 action items in the reports, only 3 had all four basics (name them in a few words, e.g. who, what, when, how to check).

## 7 [unclear] L654
TEXT: if confidence scoring ships in Dara ... A trust score built on top of Dara (called AIF)
PROBLEM: 'Dara' and 'AIF' are used with no gloss in this box (Dara is not explained anywhere in lines 529-686; elsewhere in the region the page says 'the program'). Inconsistent naming for a newcomer. Check that Dara is in the end glossary; if not, gloss here.
SOURCE: Dara = an open program that does phase identification. (plan/plan.md:8)
FIX: ...if confidence scoring ships in Dara (the open phase-naming program your project builds on)...

## 8 [unsupported] L662
TEXT: 8 of 24 finished; 16 stalled
PROBLEM: Unsupported in the source files. Eight verification notes exist (K1 x2, K2 x3, K3 x2, K4 x1) and all say 'holds with changes', but no source states a total of 24 planned or 16 stalled; plan.md section 8 only says five items got no skeptical verdicts.
SOURCE: Items D4, D5, N4, N5 and N6 got no skeptical verdicts. Their numbers were spot-checked in the files only. (plan/ directory listing; plan/plan.md:208)
FIX: Keep only if the orchestrator log backs 24; otherwise: '8 adversarial checks finished, covering four of the nine items; the rest did not run.'

## 9 [unclear] L676
TEXT: 7.2% of fixes were wrong
PROBLEM: Missing denominator and interval, and inconsistent with line 633 of the same page and with the final plan, which both say 'at least 6 of those fixes wrong'. The 7.2% is a low-confidence rate (interval 0 to 19%). Also omits the strongest refutation: 0 of 12 proven cases fixed.
SOURCE: Refuted: 85 of 266 fixable, at least 6 of those fixes wrong, 0 of 12 proven two-curve errors fixed. / measured wrong-fix rate 7.2% (interval 0 to 19%) ... low confidence (plan/plan.md:139; plan/proposal_leverage.md:201; synth/glossary_usermodel.md:168)
FIX: Only 85 of 266 got fixed, at least 6 of those fixes were wrong, and it fixed 0 of 12 proven errors.

## 10 [overstated] L681
TEXT: Its answers sit in a public file, with no licence and no scoring server.
PROBLEM: Overstated. The corpus explicitly disagrees on whether XRDBench answers are public; this is listed as an unresolved contradiction, not a settled fact.
SOURCE: XRDBench answers: the XRD report and memory notes say the evaluator keeps them; the late XRD-session notes say they are in a public JSON with no licence; the ImageNet report says 'published answers'. / 'The corpus disagrees on whether XRDBench answers are public' (synth/builds.md:754 and :330)
FIX: The latest notes say its answers sit in a public file with no licence (earlier notes said the opposite; not re-checked). Either way, a hidden test needs new scans.

## 11 [unclear] L682
TEXT: Predict the gain from 10× more simulated data ... smaller than a 270-item test set can detect
PROBLEM: Mismatch of what it is about. The source is about 10x more computed (DFT) property data for property prediction, measured in eV against a test set of about 270 compounds. Sitting between X-ray rows, 'simulated data' and '270-item' reads as simulated X-ray patterns, and collides with the unrelated '270 items give +/-5 points' X-ray sizing figure.
SOURCE: The predicted gain from 10x more DFT (0.009-0.040 eV) is below what a test set of about 270 compounds can detect (about 0.08 eV) (synth/storyline.md:91; synth/builds.md:453)
FIX: Predict the gain from 10× more computer-calculated property data | The predicted gain (0.009-0.040 eV) is smaller than a test set of about 270 compounds can detect (about 0.08 eV).

## 12 [rule] L683
TEXT: “A closed lab made labels without public data”
PROBLEM: Rule: the banned phrasing 'without public data' appears on the page, even though it is quoted as a withdrawn claim. A skimming reader still sees the assertion.
SOURCE: Do not say a lab did something 'without public data'. (task rule list)
FIX: Idea column: 'A claim about what data a closed lab did or did not use' | 'You challenged it; it was withdrawn. Their inputs are unknown.'
