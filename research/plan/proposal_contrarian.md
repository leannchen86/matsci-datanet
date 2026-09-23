# Contrarian proposal: what is wrong with both recommendations, and what to do instead

Lens: CONTRARIAN. My job was to attack the two existing recommendations and the ranked build list, then say what I would do instead. Every number below comes from the session files and carries its denominator and its source file in brackets. Anything that faces outward (sending, publishing, downloading, contacting, buying) is marked **NEEDS YOUR YES**. Nothing here has been sent, published or downloaded.

Source-file short names used below:
- `storyline` = synth/storyline.md
- `builds` = synth/builds.md
- `gaps` = synth/gaps.md (only partly written when I read it)
- `C15` = digests/C15-late-updates.md (what the main session recommended)
- `C16` = digests/C16-xrd-session-verification.md (the XRD session's own nine-checker review)
- `build-list` = corpus/notes/FILE_build-list.md
- `late2` = late2.txt (what is and is not approved)

---

## The short version

1. **The ingredient that is actually missing for an "ImageNet moment" is a pool of fresh test items whose right answer is known without trusting any analyst.** Both recommendations mostly build tooling around old public labels. Tooling is not that ingredient.
2. **For thermoelectrics [materials that turn heat into electricity] that ingredient cannot be made from a desk.** For X-ray powder patterns [a 1-D fingerprint curve of a powder] it is much cheaper: someone weighs known powders together and scans the mix. One lab can do that, and some harder weighed sets may already be public.
3. **So I would shrink both recommendations.** Thermoelectrics becomes one short write-up plus one frozen list of which papers go in the test set. The X-ray "fair marking kit" becomes a days-long piece done first inside your own project, followed by the step both sessions skipped: pooling the public known-answer scans.
4. **"Send the error lists" is a courtesy, not a contribution.** Do it in one day, with one exception that is genuinely new (499 copied files, below).

---

## Attack 1: the thermoelectric line (error lists, then "spell-checker", then fair-exam generator, then benchmark)

The main session's reason: it is the only area with a large dataset, a physics equation that checks records, and three overlapping databases (`C15`). All true. Here is what that reasoning leaves out.

**1a. The core of the "spell-checker" already exists.**
The check recomputes the quality score zT from the three measured curves, like a checksum. Another database, teMatDb, already publishes exactly this filter; it kept 10,840 of 15,532 samples (`builds`, `gaps` G1). The new part would be catching errors in one extra curve (power factor). But that curve is itself the prime suspect in 133 of 245 cases, 54.3% (`builds`, `gaps` G2), so it cannot act as the referee.

**1b. The checker can only produce a to-do list for someone else.**
Automatic fixing was tested and refuted: only 85 of 266 power-of-ten errors could be fixed, at least 6 of those fixes look wrong, and the rule fixed 0 of 12 proven two-curve errors (`builds` section C, `gaps` G2). What remains is a review queue of 633 specimens in 230 papers (`builds`). Clearing it means opening 230 papers. No source paper has been opened so far (`gaps` G1), and downloading them is not approved (`late2`).

**1c. The checksum covers a minority of the data.**
It was run on 13,702 of 55,422 samples (`gaps` G1), because the two curves it needs exist for only 52.4% and 47.9% of experimental samples (`build-list`).

**1d. The "fair-exam generator" is a finding, not a product.**
The finding is strong: median error on the Seebeck coefficient [the voltage a material gives per degree of temperature difference] goes from 25.5% with a random split to 42.2% when whole papers are held out, on 12,222 samples from 3,015 papers (`storyline`). But the tool is a standard grouped split (scikit-learn's GroupKFold) plus an existing open tool called MatFold (`builds`). The genuinely new code is a cleaner for paper identifiers: it found 75 shared papers where naive matching found 26 (`C15`, `builds`). ImageNet itself shipped a fixed list of test images, not a split-making program. A frozen list of paper identifiers is smaller and easier for others to adopt.

**1e. The headline rests on a weak model.**
The only baseline is a 5-nearest-neighbour model on chemical formula alone (`builds`), and the forests were hand-written because scikit-learn was missing (`build-list`). A plain lookup table (22.9%) already beats it (29.4%) (`storyline`). Before anyone leans on "25.5% to 42.2%", it needs one properly strong baseline.

**1f. A thermoelectric benchmark on existing data has a hard ceiling, and it is not blind.**
- The same formula measured in different papers differs by a median of 32.7% (`storyline`).
- An oracle that already knows the answers still misses by 15.0% using formula alone (`storyline`).
- 7 of 28 specimen-description fields exist in no source; density is filled in 2.5% of records (`storyline`).
- The build list itself calls the packaged result a fair development benchmark, "not a blind test" (`builds`).
- Every value in the database is a published figure, so any test label is already in everyone's training pool (`builds`).

**1g. A truly hidden thermoelectric exam needs labs, plural.**
It needs at least 3 pilot labs; past round robins [many labs measuring the same specimen] took from 4 months to about 2 years; scoring with 7 or fewer labs and no certified reference is described as generally not recommended (`builds`). No pilot lab, cost estimate or funding route exists (`builds`). This is the honest "inaccessible without a lab" case.

**1h. No one has asked for it.**
The only documented outside request anywhere on the build list (a Matbench issue) sits on the computed-data side you parked (`builds`). I am not reviving it. The lesson is only this: the thermoelectric tooling has no named user.

**Verdict on the thermoelectric line:** the experiments are done and worth writing up. Months of tooling on top of them is not justified.

---

## Attack 2: the X-ray "fair marking kit"

The XRD session's claim: how you mark an answer right or wrong swings the score a lot, so publish a fair marking kit (`C16`).

**2a. Much of the swing is a bug in one project's grader, not a field-wide finding.**
On the same 40 easy weighed scans, the local run scores 12 of 40 under a strict rule, 17 of 40 under a lenient rule, and 32 of 40 after the matching was corrected; the published figure is 38 of 40 (`C16`). But the local grader compares chemical formulas only and throws away which reference entry the program picked, and the local setup (open reference library capped at 80 candidates) is not the published configuration (`C16`). So part of the gap is setup, not marking.

**2b. The errors seen are spelling artifacts.**
"LaO3" for La(OH)3, "Ni1.875O2" for NiO, "V4O9.93316" for V2O5 (`C16`). The heavier machinery, about crystal forms of the same formula, addresses 0 proven wrong marks, even though about 250 of 590 checkable scans had more than one crystal form on offer (`C16`). A simple "same symmetry group" rule would itself be wrong in at least 3 cases (`C16`).

**2c. The ideas are old.** They date to a 1990 crystallography-union classification; what is missing is only a runnable, tested version (`C16`). That is a fair contribution, but a small one. Size it as such.

**2d. It is gated on a specialist you do not have.** The session's own review says it needs sign-off from one practising diffraction specialist (`C16`). A newcomer publishing marking rules without that has an adoption problem.

**2e. A marker is only as useful as the exam it marks.** The only analyst-free answer key on disk is 40 easy weighed scans. On those the open program scores 38 of 40 and the commercial one 35 of 40 (`storyline`), so there is almost no room left to show anything.

**Verdict:** keep it, shrink it to days, use it first inside your own project, and do not wait for sign-off to use it internally.

---

## Attack 3: "send the error lists". Contribution or courtesy?

Courtesy. Item by item (`C16`, `builds`):
- **Synthesis ledger (the "PG" dataset):** only 5 of 8 drafted items are certain; about 30 of 1,035 samples hold a truly wrong stored value; 4 drafted items must be retracted first. Its paper is still under review, so a public issue would be seen by its reviewers.
- **Mineral pattern library (RRUFF):** 1,702 of 3,019 "RAW" files are calculated, but the file headers already say so, and an Argonne paper (March 2026) already says the library mixes calculated and measured patterns. The XRD session's own review says this "is not news" and dropped RRUFF as a target. It has only a contact form and its site is mid-migration.
- **Open X-ray collection (opXRD):** its only outside issue has sat unanswered since March 2026.
- **Thermoelectric database (Starrydata):** 8 wrong curves in a snapshot of 55,422 samples. It does have a working fixes channel.
- **Two other tables (HTEM, MPEA):** cannot take fixes at all; MPEA was archived in November 2024.

**The one exception that is new:** 499 patterns in the open X-ray collection are copies of mineral-library files; 414 of those 499 are calculated but were deposited flagged "not simulated"; the same group re-published 261 of them elsewhere as "experimental"; and eight papers use between 148 and 3,002 of the library's "experimental" files without listing which ones (`C16`). That is test-set contamination other people can act on. It deserves one neutral notice plus a tiny "check your file list" script. Everything else: one day, then stop.

---

## Attack 4: the ranked build list as a whole

- **It is ordered by what is easy and on disk, not by who would use the result.** An earlier audit found only 3 of 188 action items had all four basics filled in, and only 8 were software builds (`storyline`).
- **The table linter has no user.** Its main test table is archived and cannot take fixes, and the meaning of a blank cell is recoverable for only 25.6% of cells. The build list itself says a linter flags ambiguity but cannot recover meaning, and the milestone was untouched as of Round 4 (`builds`).
- **The file-header proposals are a schema pitch to an owner who is not answering** (see Attack 3), and you ruled out defaulting to schemas.
- **The items that would matter most need labs:** the X-ray known-answer set (about 1,000 expert-hours, a partner, 3 to 12 months) and the thermoelectric label kit (at least 3 pilot labs) (`builds`).
- **The human-versus-software disagreement set looks big but has no headroom.** Humans and software differ on 316 of 343 scans, but random guessing scores 20.1% and a perfect method 21.8%; all 1,216 human checks carry one editor ID; and in a sister dataset the "automated" answer is the same program being tested, with 137 of 352 "human" files being the program's fit left unchanged (`C16`, `storyline`).
- **The process problem:** ten reports, four finished experiment rounds and a fifth still running, and, as far as the files show, no installable tool and no message sent (`C16`, `builds` section D). Every outward step waits on a yes that has never been asked for in a small, specific form.

---

## What is honestly out of reach without a lab

- A hidden thermoelectric exam (at least 3 labs, months to years).
- The specimen details that explain the 32.7% between-paper spread; 7 of 28 fields were never written down anywhere.
- Handling history for X-ray samples; 0 of 115 field paths in the synthesis ledger record it (`storyline`).
- A large hidden X-ray exam: about 385 separate powders if accuracy sits near 50%, and about 470 to 780 paired powders to separate two tools that are 5 points apart (`C16`).

But the two are not equally out of reach. The X-ray version needs one lab, one instrument and a balance. You said your assets include lab relationships. "Needs a partner" is not "impossible"; it means the ask has to be small and exact.

---

## What both sessions missed

**Harder known-answer X-ray scans may already be public** (`C16`, prior-art list; each item was found by a single checker and NOT independently re-verified):
- An international round robin with 4- and 7-ingredient weighed mixtures, minor ingredients at 1 to 5% by weight, raw scans and answers public.
- 240 weighed two-ingredient mixtures with the minor ingredient at 2 to 20% by weight, open licence, 1.87 GB archive (`late2`).
- A spiked series with the added ingredient at 0.12 to 4.0% by weight, open licence.

The session's earlier count of "only 167 hard patterns exist, 270 needed" counted analyst-labelled scans from two datasets (157 of 1,035 and 10 of 352) (`builds`). It did not count these weighed sets at all. Pooling them turns part of "needs a lab" into "needs a download yes". This is harder along the axes that matter (small minor ingredient, more ingredients), so it is not the refuted "more easy mixtures" idea.

**It also matters for your own project.** dara-conform [your project: a confidence score and a "not sure" option on top of the open phase-naming program Dara] learns partly from labels that are circular (see the last bullet of Attack 4), and the human annotator of the synthesis ledger reversed 83.3% of re-reviewed cases according to the AIF paper (`C16`). Weighed scans are the only labels that do not inherit an analyst's opinion.

**And a decision nobody has put to you.** AIF, a trust score on top of Dara, was published in 2026 by the same group that makes Dara (`C16`). Your own pre-registered rule says: "calibration/abstention ships in Dara → shrink to the evaluation harness" (`C16`, `late2`). If AIF counts as that, then an X-ray evaluation harness is not a new direction. It is the fallback you already committed to. Only you can make that call.

---

## What I would do instead (five pieces, smallest first)

### 1. A marking function plus about 25 tricky pairs, used inside your own project first (X-ray, days)
- **Problem:** the same 40 results score 12, 17 or 32 out of 40 depending on the marking rule (`C16`), so no score from the current grader can be trusted, including dara-conform's.
- **Build:** one test file of about 25 (predicted name, true name) pairs with the right verdict for each, drawn from the cases already found: 3 spelling artifacts, 6 pairs the lenient rule wrongly merges (for example Nb2O5 with Nb12O29), and the 3 symmetry-group traps (`C16`). One tiered marking function that passes the file. One table: the 40 weighed results re-marked under all five rules.
- **First step this week:** write the 25-pair file and run the five existing rules over it, in the scratch area, on stored results only. No download, no change to your repo.
- **Done when:** the tiered function gets 25 of 25, each of the older rules gets a recorded lower score, and the 40-scan table exists with one row per rule.
- **Needs your yes:** nothing to build it. Changing dara-conform itself, or publishing the file, **NEEDS YOUR YES**. Specialist sign-off is needed before publishing, not before using.
- **Risk:** it turns out to be mostly a fix to your own grader. That is still worth days, and it is the precondition for piece 2.

### 2. A known-answer practice exam pooled from public weighed scans (X-ray, 1 to 2 weeks after a yes)
- **Problem:** the only analyst-free answer key on disk is 40 easy scans where the program already gets 38 (`storyline`).
- **Build:** pool the 40 on disk with the three public weighed sets above; freeze the marker from piece 1 before looking; run Dara; report accuracy by how small the minor ingredient is and by number of ingredients.
- **First step this week (no download):** write the one-page frozen protocol: which sets, which marker version, which breakdowns, and what result would count as "still too easy". Then ask you for the download.
- **Done when:** one table of accuracy by minor-ingredient band with counts and error bars, plus a stated verdict on whether the pool separates tools at all.
- **Needs your yes:** **download of the three archives (one is 1.87 GB; the other two sizes are not stated in the files)**. Publishing the result is a separate yes.
- **Risk:** the prior art is unverified and may be in awkward formats, or the scans may still be too easy. It is a practice exam, never a hidden one, because the answers are public.

### 3. Thermoelectrics: publish the finding, not the toolchain (1 to 2 weeks)
- **Build:** a short note with three results that are already measured: the jump from 25.5% to 42.2% when papers are held out; the 32.7% between-paper spread and 15.0% oracle miss; a plain lookup beating the model. Plus one frozen split file (lists of paper identifiers) and one strong baseline added. Optionally offer the paper-grouping split to the existing MatFold tool.
- **First step this week:** add one strong baseline under the same frozen split and see whether the jump survives. If scikit-learn is still missing, installing it is a local environment change to confirm with you.
- **Done when:** the note fits in 4 pages, every number regenerates from one command, and the split file is a plain list anyone can load.
- **Needs your yes:** **publishing the note or split file; any pull request to MatFold.**
- **Risk:** the jump shrinks under a strong baseline. That would also be worth knowing before building a benchmark on it.

### 4. A one-day courtesy batch plus one contamination notice (cross-cutting, days)
- **Build:** the 499-row match table with a basis-of-evidence column and neutral wording, plus a tiny script that checks a list of file IDs against it. Separately: the 8 thermoelectric curves through that database's fixes channel; a private 5-item note to the synthesis-ledger authors (not a public issue while their paper is under review).
- **First step this week:** regenerate the 499-row table and the checker from files on disk and draft the three messages. Draft only.
- **Done when:** three drafts sit in a folder you choose, each under one page, each with a reproducer.
- **Needs your yes:** **everything outward. You send it, not me.**
- **Risk:** no reply (one owner has been silent since March 2026). That is why it gets one day, not a strategy.

### 5. A one-page lab ask for a small hidden weighed exam (X-ray, needs a partner)
- **Build:** one page a lab can say yes or no to: how many powders, which ingredient bands, scan settings, file naming that does not give away the recipe (the current names spell it out, `C16`), who holds the answers, and the sizing table (about 385; about 470 to 780). Include the option of buying past powders from a blind mineral contest at a listed $250 per unit (`C16`, unverified; buying is your decision per `late2`).
- **First step this week:** draft the page only. No contact.
- **Done when:** a materials person you trust can read it in 5 minutes and name the cost.
- **Needs your yes:** **any contact, any purchase.**
- **Risk:** no lab says yes. Pieces 1 and 2 make the ask far more credible, which is why they come first.

---

## The one thing to start this week

Piece 1. It needs no download and no approval, it is finished in days, it fixes a real fault in your own project's scoring, and pieces 2 and 5 cannot be trusted without it. While it runs, the only decision I would put to you is one small yes: the download for piece 2.

---

## How to reconcile "thermoelectrics" versus "X-ray"

Choose by the cheapest path to the missing ingredient, which is fresh test items with an analyst-free right answer.
- **X-ray:** one lab weighing powders can make them, and some may already be public. You also have an unfair advantage here: your own project, the program installed, and the scans on disk.
- **Thermoelectrics:** at least 3 labs, months to years, and a 15.0% ceiling from formula alone even with perfect labels.

So the X-ray line wins, but in a shrunken form (pieces 1, 2, 5), and the thermoelectric work is cashed in as a short note (piece 3) rather than extended for months. The main session is right that thermoelectrics has the most data and the cleanest physics check. It is wrong that this makes it the place to build, because more tooling on public labels does not produce a fair exam.

---

## Traps: tempting things not to do

- **Automatic unit fixing.** Refuted: 85 of 266 fixable, at least 6 wrong, 0 of 12 proven cases fixed (`builds`).
- **The 1-to-2-month thermoelectric benchmark on public labels.** The build list itself says it is not a blind test; ceiling of 15.0% oracle miss and 32.7% between-paper spread (`storyline`, `builds`).
- **A split generator as a product.** It is GroupKFold plus an existing tool; ship a frozen list instead (`builds`).
- **The table linter.** Archived source, blanks recoverable 25.6%, no user (`builds`).
- **Header-field proposals and a handling-history standard.** Schema pitches to silent owners; 0 of 115 field paths record handling today and no lab is behind it (`storyline`, `C16`).
- **Treating error lists as strategy.** About 30 of 1,035; 8 of 55,422; one target already "not news" (`C16`).
- **Expert relabelling of hard scans.** About 1,000 expert-hours; experts agree pairwise only 35 to 70% per the AIF paper (`builds`, `C16`).
- **The human-overrule test set.** Random 20.1% versus perfect 21.8%; one editor ID on all 1,216 checks (`C16`, `storyline`).
- **Using the public 134-case X-ray benchmark as a hidden test.** Its answers are public, it has no licence and no scoring server (`C16`).
- **Summed "synthetic mixtures" as a stand-in for real ones.** Even the better summing method is off by about 5 points on the recipe, and summed scans differ from real ones by about 4 times counting noise (`C16`). Fine as a replay check, not as an exam.
- **Gating the marking function on specialist sign-off before using it internally.** Sign-off matters for publishing, not for fixing your own grader.
- **A fifth experiment round before shipping anything.** The main session's own words: "We have run enough experiments" (`C15`).
- **Reviving the parked computed-data side** because it has the only outside request. Your guardrail says experimental first.

---

## What I could not find

- Any evidence of a named outside user for the thermoelectric checker or split tool.
- File sizes for two of the three public weighed-scan archives.
- Independent confirmation of the prior-art items in "What both sessions missed"; each came from one checker.
- Whether AIF formally "ships in Dara". It is from the same group and sits on top of Dara; whether that triggers your rule is your call.
- A consistent count of the Dara benchmark files (notes say 40, 41, 60, 61 or 70; `builds` section E).
