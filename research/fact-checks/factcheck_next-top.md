# factcheck:next-top checked=62 findings=18

## 1 [wrong] L401
TEXT: Start with a one-day test
PROBLEM: Inconsistent with the page's own step and chip ("days 1-2", "1-2 days") and with the plan (half a day to one day for the first step, 1-2 days for the test, plus a half-day rescue before it).
SOURCE: First step (half a day to one day) ... D1 ... 1-2 days for the test (plan/plan.md:27,76)
FIX: "Start with a one-to-two-day test, not a build"

## 2 [overstated] L405
TEXT: Your project's pilot numbers move from 0.309 to 0.745 (55 scans) with the marking rule alone.
PROBLEM: "alone" is added by the page and unsupported: the same section says the strict-vs-lenient swing is mixed with stale stored marks and text handling. Source gives only 'strict 0.309 vs lenient 0.745 at n=55' from a pilot probe's result note in a sibling folder, not the project's headline (correction 3). '55 scans' as the unit is also not stated in the source (n=55).
SOURCE: 0.309 vs 0.745 (n=55) comes from a pilot probe's results, not dara-conform's headline. (plan/plan.md:23,166; plan/verify_K1_evidence.md:25)
FIX: "A pilot probe beside your project scores 0.309 under strict marking and 0.745 under lenient marking (n = 55)."

## 3 [rule] L406
TEXT: No download, no model, no lab, no message to anyone.
PROBLEM: The recommendation box lists everything the step does NOT need but omits that it needs exactly two approvals from the user (a folder name plus the copy, and read-only access to the two project folders). Read alone, the box implies it is free to start. Plan section 1 states the two approvals explicitly.
SOURCE: Approvals it needs (exactly two, both from you): 1. Name a permanent folder and say yes to copying the at-risk files there. 2. Say yes to a working session reading your two project folders, read-only (plan/plan.md:39-43)
FIX: Add a fourth bullet: "It needs exactly two yeses from you: a folder name for the rescue copy, and read-only access to your two project folders."

## 4 [overstated] L413
TEXT: a different reference library (32 vs 38)
PROBLEM: Source attributes 32 vs 38 to the reference library AND the local set-up, and notes the 32 was quoted, not recounted, and that 17 + 15 = 32 is a checker's arithmetic. Page presents three clean causes as settled.
SOURCE: the reference library and local set-up (32 vs 38). The 32 was quoted, not recounted. (plan/plan.md:164 (correction 1))
FIX: "a different reference library and local set-up (32 vs 38). The 32 itself was quoted from notes, not yet recounted; the 40-row test recounts it."

## 5 [unclear] L413
TEXT: On a second set of 20 scans
PROBLEM: Wrong description of what the 20 are. They are 20 reaction products (a different, harder kind of sample), not just 'a second set of scans'; the distinction from weighed mixtures is the point.
SOURCE: On a second dataset (20 reaction products) the rule moves scores by only 1 to 3 of 20 (plan/plan.md:53,165,167)
FIX: "On a second dataset (20 products of real reactions, not weighed mixtures)"

## 6 [overstated] L418
TEXT: in each set-up we measured, how the exam is set and marked moved the score at least as much as the contestants differed
PROBLEM: Overstated and contradicted by the table directly above (line 413). Correction 2 says the claim holds only on the 40 weighed scans in the local set-up; on the 20 reaction products the rule moves scores 1-3 of 20 while the tool gap is 11-13 of 20, i.e. the contestants differed far MORE than the marking.
SOURCE: "The rule moves the score more than the gap between programs" holds only on the 40 weighed scans in your local set-up. On 20 reaction products the rule moves scores by 1 to 3 of 20 and the tool gap is 11 to 13 of 20. (plan/plan.md:165 (correction 2); plan/plan.md:53)
FIX: "in several set-ups we measured (not all: on the 20 reaction products the tools differed far more than the marking rule did), how the exam is set and marked moved the score about as much as the contestants differed"

## 7 [overstated] L418
TEXT: thermoelectrics: a lookup table at 22.9% beats the model at 29.4%
PROBLEM: Missing denominator and scope. The result covers only the 3,593 of 12,222 test rows whose formula was seen, and only formula-only models; the 'model' is a 5-nearest-neighbour baseline, and a 1-nearest-neighbour scores 21.4% on the random split, so part of 'lookup beats model' is the choice of 5 neighbours (corrections 17 and 18). Also 29.4% doubles as '3,593 is 29.4% of 12,222' - a known trap.
SOURCE: The lookup result and the 15.0% floor cover 3,593 of 12,222 rows and formula-only models. A 1-nearest-neighbour model scores 21.4% on the random split, so part of 'lookup beats model' comes from choosing 5 neighbours. (plan/plan.md:184-185; plan/verify_K3_newcomer-skeptic.md:16,38)
FIX: "on the 3,593 of 12,222 test rows with a seen formula, a plain lookup (22.9% error) beats a simple 5-nearest-neighbour model (29.4%); part of that gap comes from the choice of 5 neighbours"

## 8 [overstated] L429
TEXT: the lean is X-ray, in shrunken form, because a lab with a balance can make test items whose answer nobody has to trust an analyst for
PROBLEM: Omits the plan's cautions on this lean: no lab is secured, it would be a one-instrument exam, 'one lab is enough' is reasoning not a measured fact (correction 29), and the thermoelectric recommendation did not get the same adversarial attack as the X-ray shortlist, so the comparison is lopsided. Section header says 'after adversarial checking' without that asymmetry.
SOURCE: That is still a one-instrument exam, and no lab is secured. ... The XRD shortlist went through nine adversarial checkers; the TE recommendation did not get the same attack. (plan/plan.md:55,58,198)
FIX: Add: "No lab is secured, one lab gives a one-instrument exam, and the thermoelectric side was checked less hard than the X-ray side, so treat the lean as provisional."

## 9 [rule] L462
TEXT: Tricky-pairs table with a draft answer key ... chips: X-ray / a few days / low-hanging
PROBLEM: Required approval not shown. Plan D1 says this item NEEDS YOUR YES (read-only access to the project folders), and the verify note adds that the 21-pair script it builds on sits in another session's temporary area, so it also depends on the rescue. The page shows no 'needs read-only OK' or 'after the rescue' chip, unlike its neighbours.
SOURCE: NEEDS YOUR YES: read-only access to your project folders. / Moving the 21-pair script out of the temporary area to a folder the user names is on the 'needs the user's yes' list. (plan/plan.md:82; plan/verify_K1_evidence.md:47-51)
FIX: Add chips "needs read-only OK" and "after the rescue" (the 21-pair script is in a temporary area; if it is gone about 12 pairs can be rebuilt from text).

## 10 [unclear] L462
TEXT: Tricky-pairs table (whole item)
PROBLEM: Omits the plan's explicit guard: do NOT promise structure-comparison rules on the 40 scans, because the stored results keep only formulas and the reference file the program chose was thrown away. Without it the item reads as if any marking rule can be run on the stored results.
SOURCE: Do NOT promise structure-comparison rules on the 40 scans. The stored results keep only formulas; the reference file Dara chose was thrown away. (plan/plan.md:81; plan/verify_K1_evidence.md:45)
FIX: Add to Honest limits: "On the 40 scans only formula-level marking is possible; the stored results kept no crystal-structure choice."

## 11 [unclear] L465
TEXT: On 18 hand-built pairs
PROBLEM: Drops the unexplained gap: the script holds 21 pairs but scores only 18 (correction 5). The page itself calls it 'the 21-pair script' at line 445, so a reader sees 21 and 18 with no explanation.
SOURCE: The script holds 21 pairs but scores 18; the gap is unexplained. (plan/plan.md:168 (correction 5))
FIX: "On the 18 pairs the script scores (it holds 21; the gap of 3 is unexplained)"

## 12 [unclear] L473
TEXT: reproduces the 499-file match ... opXRD folder ... RRUFF files
PROBLEM: opXRD and RRUFF are used in this section with no plain gloss nearby (they are glossed only back at lines 291-297 in another section). 'calibration/test split' at line 477 is also unglossed for the X-ray project context. Check they are in the twelve-word glossary; if not, gloss here.
SOURCE: RRUFF = an open mineral archive with XRD files. opXRD = a pooled open collection of XRD files from several labs. (plan/plan.md:13)
FIX: "...in one folder of opXRD (a pooled open collection of X-ray files from several labs) ... identical to files in RRUFF (an open mineral archive)"

## 13 [overstated] L476
TEXT: 124 of 2,680 opXRD files are exact copies, in 61 groups
PROBLEM: Denominator reads as if 2,680 is the whole collection. It is only the part on disk: 2,680 of 92,552 files, so every opXRD count except the 499-file folder is a lower bound (correction 16).
SOURCE: The HKUST-B folder is complete on disk (499 of 499). All other opXRD counts are lower bounds (2,680 of 92,552 files). (plan/plan.md:181 (correction 16))
FIX: "124 of the 2,680 opXRD files on disk (the full collection has 92,552, so this is a lower bound) are exact copies, in 61 groups"

## 14 [unclear] L477
TEXT: 8 suspect rows of 200
PROBLEM: Missing what the 200 is a count of. Source: 8 suspect RRUFF rows of 200 (the RRUFF rows in the 1,554-row list), not 200 of anything else.
SOURCE: expect 8 suspect RRUFF rows of 200, 0 HKUST-B rows, 8 duplicate pairs (plan/plan.md:85)
FIX: "8 suspect rows among the 200 RRUFF rows of your 1,554-row list"

## 15 [unclear] L487
TEXT: A 134-item test cannot separate 55% from 53%.
PROBLEM: No statement of whose test or what the ±4.3 is (one standard error, the checker's own arithmetic). Also the 55% figure is a best-of-7 score with a learned selector (single attempt about 36%), so presenting 55 vs 53 as like-for-like is loose. Line 418 calls it 'a 134-item company test' with '±4.3 points of noise' - it is a standard error, not an interval.
SOURCE: a 134-item test gives about ±4.3 points standard error [OWN-EXPERIMENT arithmetic] ... 55.3% ... is best-of-7 with a learned selector; a single attempt is about 36% (synth/glossary_usermodel.md:210,232)
FIX: "On one company's 134-item X-ray test, one standard error is about ±4.3 points (our arithmetic), so its 55.3% vs a rival's ~53% is a tie."

## 16 [rule] L493
TEXT: data-f="free" ... chip "nothing needed" ... Also read: The X-ray session's round-5 folder may already hold a dated protocol
PROBLEM: Marked as needing nothing from the user, but the 'Also read' half requires opening another session's / the user's project folder, which needs the user's OK. Only the landing-page half is free. Correction 25 says 'desk stage needs no approval' is wrong.
SOURCE: (1) with the user's OK to read their project folders, count the Dara files and read the Round 5 dated protocol and metric files; (2) open the three landing pages on the web (plan/verify_K4_evidence.md:81; plan/plan.md:194 (correction 25))
FIX: Keep 'nothing needed' for the landing pages only; add to 'Also read': "needs your read-only OK; that folder's contents are unverified". Or move the round-5 read into the 40-row marking test item.

## 17 [unclear] L498
TEXT: The X-ray session's round-5 folder
PROBLEM: "round-5" is internal session jargon with no gloss; a reader does not know what round 5 is. Also the claim that it holds a dated protocol is flagged 'unverified' in the source, which the page softens only with 'may'.
SOURCE: C16 says the other session's folder already 'holds PREREG.md and metrics_*.json', dated 2026-09-18 and unverified. (plan/verify_K4_evidence.md:37,52)
FIX: "An earlier X-ray session's folder for a known-answer test on the same 40 scans may already hold a dated protocol and result files (unverified)."

## 18 [unclear] L523
TEXT: Trim the two error notes ... Recipe-plus-scan release: 5 certain items
PROBLEM: Title and summary say two notes, but the body gives numbers and instructions for only one (the synthesis-ledger note); the second note is never identified. 'Recipe-plus-scan release' is a new label for what the rest of the material calls the synthesis ledger; unglossed here.
SOURCE: D5. Trim the two corrections drafts and hold them. Cut the synthesis-ledger note to the 5 certain items (plan/plan.md:93-94)
FIX: Name both drafts in one line each, and say which one the 5-item / 30-of-1,035 figures belong to (the dataset of synthesis recipes with their X-ray scans).
