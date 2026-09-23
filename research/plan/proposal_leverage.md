# Leverage proposal: what would other people actually pick up and use?

Lens: LEVERAGE. The question I asked of every idea: would it change how OTHER people test their models, and would an unknown newcomer realistically get it adopted? One-off analyses score low on this lens, however good they are. Reusable exam parts score high.

Every number below comes from the session files and carries its denominator and its source in brackets. Anything that faces outward (publishing, sending, downloading, contacting) is marked **NEEDS YOUR YES**. Nothing has been sent, published or downloaded. I read files only inside the session scratch area and did not open your own project folders.

Source short names:
- `storyline` = synth/storyline.md
- `builds` = synth/builds.md
- `gaps` = synth/gaps.md (only partly written when I read it; it stops at gap 29)
- `C15` = digests/C15-late-updates.md (the main session's thermoelectric recommendation)
- `C16` = digests/C16-xrd-session-verification.md (the X-ray session's nine-checker review)
- `build-list` = corpus/notes/FILE_build-list.md

---

## The two-line picture

You want "trusted labels + a fair exam" for measured (not simulated) materials data. The things that made ImageNet, CASP [the protein field's recurring blind contest] and GLUE [the language-model test suite] work were small and boring: **a fixed list of test items, one written marking rule that everybody runs the same way, and a way to tell a real win from luck.** None of them was adopted because of a report.

Your own files already say this: ImageNet had about 6% wrong validation labels and model rankings still held, so "a fixed, fair protocol mattered more than perfect labels" (`storyline`, chapter 2).

So through this lens the right contribution is **an exam part that others reuse**, not a cleaned dataset and not another analysis.

---

## Honest adoption barriers for an unknown newcomer

1. **No name, no lab.** Materials people will not take marking rules for X-ray answers from an ML newcomer unless a practising specialist has signed them off. The X-ray session's own review says exactly this (`C16`).
2. **Data owners are slow or silent.** The open X-ray collection's only outside issue has been unanswered since March 2026; the mineral pattern library has only a contact form and its site is mid-migration (`C16`).
3. **Nobody has asked for any of this.** No named outside user exists in the files for any thermoelectric or X-ray tool. (I looked; I could not find one.)
4. **A standalone note or a new leaderboard by an unknown gets ignored.**

What follows from that, and what I applied to every candidate:
- **Attach to a tool people already use**, rather than launching a new site. For splits that is MatFold [an existing open tool that makes train/test splits for materials data]. For X-ray marking that is your own project first, then the open phase-naming program Dara and the standard crystal-structure library pymatgen.
- **Make adoption a one-line act:** load a list, call one function, quote one version string in a paper. The ML parallel is sacreBLEU: a small scoring script with a version string that papers quote, which ended years of incomparable translation scores.
- **Lead with one striking number from their world.**
- **Get one specialist co-signer** before publishing anything that encodes domain judgment.
- **Be your own first user.** Your project dara-conform [your add-on that gives the Dara program a confidence score and a "not sure" option] is a real first user for three of the five candidates below.

---

## Candidates, ranked by leverage

### 1. A fair marking kit for X-ray phase-naming answers (X-ray line) -- RECOMMENDED START

**What is broken.** Many groups build programs that read an X-ray powder scan [a 1-D fingerprint curve of a powder] and name the ingredients [called "phases": each distinct crystalline compound in the powder]. There is no written, shared rule for when a named ingredient "counts as right". Each project writes its own marker, each marker has its own quirks, and the choice of rule moves the score more than the gap between tools.

**Evidence.**
- Same program, same 40 weighed scans [powders mixed from known weighed ingredients, so the answer is certain]: 12 of 40 right under a strict rule, 17 of 40 under a lenient rule, 32 of 40 after the matching was corrected. The published figure is 38 of 40; that run used a paywalled reference library, so part of the 32-versus-38 gap is the library, not the marking (`C16`).
- The gap between the two tools being compared on those scans is smaller than that swing: 38 of 40 versus 35 of 40, paired difference 7.5 points with an interval of 0.0 to 15.0 (`builds`).
- Across 210 error-free pilot rows, 63 answers are credited under the lenient rule; 18 of those 63 (28.6%) lose credit under the strict rule (`C16`).
- On 18 deliberately tricky cases, the strict rule is wrong on 8 and the lenient rule is wrong on 13. The lenient rule treats different compounds as the same, for example Nb2O5 with Nb12O29 (`C16`).
- A second, independent result set shows the same thing: spelling one formula two ways (BiVO4 versus VBiO4) flips 3 of 20 verdicts; marking by exact text gives tool A 17 right and tool B 4, marking by chemical make-up gives 18 and 7; an ingredient listed twice is still marked right in 4 of 4 and 2 of 3 cases (`gaps`, `builds`).
- The obvious library fix is also unsafe out of the box: pymatgen's structure comparer at default settings calls alpha-quartz and beta-quartz the same (they separate only at a tighter tolerance setting of 0.15 or less), and a simple "same symmetry group" rule is wrong in at least 3 cases (`builds`, `C16`).
- The vacuum is visible: two 2026 X-ray benchmarks fall back on a chatbot as judge (one gives it 30% of the score, another uses GPT-4). The review found "No installable grader or rule card exists" (`C16`; prior-art items were each found by a single checker and not re-verified).

**What to build.** Three small things shipped as one installable package:
1. A test file of about 25 tricky (predicted name, true name) pairs, each with the expected verdict and a one-line reason.
2. One marking function that returns a **tier, not a yes/no**: exact match / same compound, different spelling / same family but different crystal form / same elements only / wrong. People can then report a strict score and a family-level score side by side, the way vision papers report top-1 and top-5. This sidesteps the need for the whole field to agree on one rule, which it does not (experts publicly dispute whether ordered and disordered versions of a crystal count as the same, `C16`).
3. A runner that re-marks a results file under every rule and prints the table.

**Why it is the high-leverage one.** It is a scoring rule, and every future X-ray exam needs one first, including any you build. The field is busy right now (at least four new 2026 works appear in `C16`'s prior-art list), so there are people to adopt it. You already own the first user (dara-conform) and the evidence came from your own pilot. It also matches your own written fallback rule, "calibration/abstention ships in Dara → shrink to the evaluation harness" (`C16`); a trust score on top of Dara was published in 2026 by the Dara group, so that fallback may already apply. Whether it does is your call.

**First step this week (no approval needed).** Write the 25-pair file and run the five existing ways of marking over it (strict formula, lenient formula, structure comparer at defaults, structure comparer at the tighter setting, proposed tier), on results already stored. Output: one CSV and one 40-scan re-marking table.

**Effort.** Days for the table; 1 to 2 weeks for the package. Specialist sign-off adds calendar time you do not control.

**Data on disk.** Yes per the files: the 40 mixture scans, 10 single-ingredient scans, the pilot results and the Dara program are all on your machine (`C16`). No download.

**Needs your yes.** Nothing to build it. Changing dara-conform itself: your approval. Contacting one diffraction specialist for sign-off: **NEEDS YOUR YES (contact)**. Publishing the package: **NEEDS YOUR YES (publish)**.

**Biggest risk.** The ideas are old (a 1990 crystallography-union classification; `C16`), so the contribution is "first runnable, tested version", which is modest. And without a specialist's name it may not be trusted. Present it as a tested card, not a new taxonomy.

**Done looks like.** (a) The tier function gets 25 of 25 on the test file and each of the four older rules has a recorded lower score. (b) The 40-scan table exists with one row per rule. (c) One named specialist has reviewed the expected verdicts. (d) `pip install` works and it prints a version string. (e) dara-conform uses it.

---

### 2. A fair-split list and leak report for thermoelectric data, offered to an existing tool (thermoelectric line)

**What is broken.** Models that predict thermoelectric properties [how well a material turns heat into electricity] from literature-mined data are tested with random splits. Samples from the same paper land on both sides, so the exam is far too easy.

**Evidence.**
- With a random split, the test sample's paper is already in training 93.5% of the time. Median error on the Seebeck coefficient [the voltage a material gives per degree of temperature difference] is 25.5% with a random split, 42.2% when whole papers are held out, and 46.6% when whole chemical families are held out (12,222 samples, 3,015 papers; `storyline`, `builds`).
- Matching papers across the three databases is itself error-prone: careful cleaning of paper identifiers finds 193 / 75 / 7 shared papers between the database pairs, where naive text matching finds 183 / 26 / 4 (`builds`).
- The right thing to hold out differs by dataset. In a synthesis ledger of 1,035 samples, holding out a starting chemical drops the score from 0.53 to 0.42. In a well-known steels benchmark, 66 of 312 groups have a near-duplicate in another group (`builds`).
- No blind thermoelectric test was found, and the standard materials benchmark suite has no thermoelectric task (`builds`; a negative search, so "none found", not "proven absent").

**What to build.** Only what existing tools lack: (1) the paper-identifier cleaner, (2) a **frozen list** of which papers are in the test set (ImageNet shipped a fixed list, not a split-making program), (3) a small leak report that, for any table with a group column, prints "X% of test items have a sibling in training", (4) an offer of a "hold out whole papers" split type to MatFold.

**Why it is smart.** It is the most quotable number in your files, the data is on disk, and there is a ready adoption channel (a contribution to a tool people already use). The leak report generalises beyond thermoelectrics to any literature-mined table.

**First step this week.** Re-run the three-way split table from the saved identifier cleaner with one command, and add one strong standard baseline. Today the headline rests on a nearest-neighbour model using chemical formula only, and a plain lookup (22.9%) already beats it (29.4%, 3,593 samples; `gaps`). If the jump survives a strong baseline, freeze the list.

**Effort.** 1 to 2 weeks.

**Data on disk.** Yes per the files, but in a temporary session folder from 14 September that can vanish (`builds`). Copying it somewhere safe is step zero; you need to name the folder.

**Needs your yes.** Installing standard ML packages locally (confirm). Publishing the list or note: **NEEDS YOUR YES (publish)**. A pull request to MatFold: **NEEDS YOUR YES (publish/contact)**.

**Biggest risk.** No shared thermoelectric exam exists, so adopters are scattered; I could not find in the files how many groups train on this data. And the jump may shrink under a strong baseline, which is worth knowing before anything is built on it.

**Done looks like.** One command regenerates the three error numbers; the frozen list is a plain file of paper identifiers with a checksum; the leak report runs on a second dataset and reproduces 66 of 312; MatFold maintainers have answered (yes or no).

---

### 3. A "check your test files" list for X-ray benchmarks (X-ray line)

**What is broken.** Papers that test X-ray models on "experimental" scans are partly testing on computer-generated ones without knowing, and some test files are copies of each other.

**Evidence.**
- All 499 of 499 patterns from one contributor to the open X-ray collection match files in the mineral pattern library; 414 of those 499 are calculated but were deposited flagged "not simulated". The same group re-published 261 of them elsewhere as "experimental". This is undisclosed and new (`C16`).
- Eight papers use between 148 and 3,002 of the library's "experimental" files without listing which ones (`C16`).
- 124 of 2,680 collection patterns are exact duplicates in 61 groups. The usable pool of measured, labelled scans is 1,683 of 7,183 files, 1,600 after removing duplicates (`C16`, `storyline`).
- Not news, so do not lead with it: 1,702 of 3,019 library "RAW" files are calculated, but their own headers say so (`C16`).
- Your own project is only lightly hit: 0 of the 499 rows, and 8 of 200 library rows suspect; its filter looks for the word "calculat" and misses "computed" (`C16`).

**What to build.** The 499-row match table with a "how we know" column and neutral wording ("intensity values identical to library file X"), keyed on library ID + content fingerprint + snapshot date; plus a tiny checker: give it a list of file IDs, it returns how many are calculated, duplicated or copied. Ship it inside the same package as candidate 1, so there is one install and one thing to cite.

**First step this week.** Regenerate the table and checker from files on disk and run it on dara-conform's own file list; it should reproduce "8 of 200" and "0 of 499".

**Effort.** Days.

**Data on disk.** Yes per the files, but the working list sits in a temporary area that can vanish (`storyline`). Copy it first.

**Needs your yes.** Publishing the table and checker: **NEEDS YOUR YES (publish)**. A neutral notice to the collection's maintainers: **NEEDS YOUR YES (send)**.

**Biggest risk.** It reads as an accusation; keep wording neutral and evidence per row. The on-disk copy of the collection is an 88 MB slice, not the full 1.4 GB release (`builds`), so state coverage plainly.

**Done looks like.** A stranger can run one command on a list of IDs and get three counts; the table has 499 rows each with a basis-of-evidence entry; the run on your own project matches the numbers above.

---

### 4. "Is this difference real?" printed by every scorer (cross-cutting)

**What is broken.** Papers and companies announce wins that are inside the noise, and nobody states the noise.

**Evidence.**
- X-ray: 38 of 40 versus 35 of 40 has an interval of 0.0 to 15.0 points, a tie (`builds`). A company's private 134-item test has an uncertainty of about ±4.3 points, so 55.3% versus about 53% is a tie; resolving that gap would need about 8,800 items per model (`storyline`).
- X-ray sizing: 270 items give ±5 points only if accuracy is about 78% or higher; near 50% accuracy about 385 separate powders are needed; separating two tools 5 points apart needs about 470 to 780 paired powders (`C16`). (An earlier file gives different sizing figures, about 770 and 1,570, `gaps`; use the later verified ones and say which assumption is used.)
- Thermoelectric: two databases reading the same printed figure differ by a median of 0.48% to 0.91% depending on the property (361 comparisons, 102 pairs); labs measuring the same specimen differ by 6%, 8%, 11% and 19% across the four properties (published round robin, cited in `builds`); the same formula in different papers differs by a median of 32.7% (21,856 paper pairs); even an answer-knowing lookup misses by 15.0%; models are at 42.2% (`builds`, `gaps`).

**What to build.** Not a note. A small function that both scorers (candidates 1 and 2) call by default, so every score prints with its interval, a "tie / not a tie" verdict, and the relevant floor and ceiling next to it. Plus a one-page card with the numbers above.

**First step this week.** Write the function and the card from numbers already measured. No new experiments.

**Effort.** Days.

**Data on disk.** Nothing new needed.

**Needs your yes.** None to build. Publishing: **NEEDS YOUR YES (publish)**, as part of candidates 1 and 2.

**Biggest risk.** Misuse of the reading-noise figure as a marking tolerance. Your files are explicit that it is a lower bound, that the quality score should be scored separately, and that a median metric should be used (`builds`).

**Done looks like.** Running either scorer on two result files prints the interval and verdict; the card's numbers each carry a denominator and a source; the 38-versus-35 example returns "tie".

---

### 5. The hard known-answer X-ray exam: desk stage now, hidden stage with a partner (X-ray line)

**What is broken.** This is the only candidate that creates **trusted labels**, the other half of your goal. Almost all "right answers" for X-ray scans are one analyst's or one program's opinion: human and program fits differ on 316 of 343 scans, and a single editor ID sits on all 1,216 human checks (`storyline`). The only analyst-free answers on disk are 40 easy weighed scans where the program already gets 38.

**What to build, in stages.**
- Desk, no approval: a one-page frozen protocol (which sets, which marker version from candidate 1, which breakdowns, what "still too easy" means). Then a replay check: rebuild the 40 mixtures from single-ingredient scans and see whether the stored outcomes repeat (about 25 minutes of compute plus about a day of coding, `C16`). Summed scans are a check only, never an exam: even the better summing method misjudges the recipe by about 5 points, and summed scans differ from real ones by about 4 times counting noise (`C16`).
- After a download yes: run on harder weighed sets that may already be public (an international round robin with 4- and 7-ingredient mixtures and minor ingredients at 1 to 5% by weight; 240 weighed two-ingredient mixtures, open licence; a spiked series at 0.12 to 4.0% by weight, open licence; `C16`, each found by one checker, not re-verified). This is "harder", not "more", so it does not revive the refuted idea. Because these answers are public it is a **practice exam**, never a hidden one.
- With a partner lab: a hidden set sized from candidate 4's table, hosted on a free contest site that keeps answers private (entrants upload answers, not code, because of a 20-minute compute cap; `C16`). File names must not give away the recipe; today they spell it out (`C16`).

**Effort.** Desk stage: days to 1-2 weeks. Hidden stage: needs a partner lab; the files give no duration for this, and the comparable thermoelectric round robins took 4 months to about 2 years (`builds`), so plan in many months.

**Needs your yes.** **Download of three archives (one is 1.87 GB; sizes of the other two are not in the files). All three are listed in the session notes as "not approved" so far (late2.txt), so this is a fresh, specific ask, one archive at a time. Any lab contact. Any purchase.**

**Biggest risk.** No lab says yes. Candidates 1 and 4 are what make the ask credible: a lab is far likelier to weigh powders for someone who already ships the marker and the sizing table.

**Done looks like (desk stage).** Protocol frozen and dated before any run; one table of accuracy by minor-ingredient band with counts and intervals; a stated verdict on whether the pooled public sets can separate tools at all.

---

## The one thing to start this week

Write the 25-pair tricky-answers table and run the five marking rules over it. It needs no download and no approval, it uses evidence from your own project, and it is the part every later X-ray exam (yours or anyone's) has to have first. The only decision I would put to you now is small: may one diffraction specialist be asked to look at the 25 expected verdicts?

---

## How to reconcile "thermoelectric line" versus "X-ray line"

It is not really a choice of subject. Both sessions found the same kind of lever: **an exam part others can reuse**. The thermoelectric line's best piece is a split (candidate 2). The X-ray line's best piece is a marking rule (candidate 1). The thermoelectric "spell-checker" is lower leverage through this lens: another database already publishes the same physics check (it kept 10,840 of 15,532 samples, `builds`), automatic fixing was refuted, and it improves one owner's records rather than how everyone tests.

So: take one reusable piece from each line, and put the long-run build on the X-ray side. The deciding reason is the path to a real fair exam:
- **X-ray:** trusted answers can be made by one lab with a balance (weigh powders, scan them), and harder weighed sets may already be public. The field is active in 2026, its marking is visibly unsettled (chatbot judges), and you already own a first user.
- **Thermoelectric:** a hidden exam needs at least 3 labs, 17 rules are still missing and 22 major review issues are open (`storyline`), and even perfect labels leave a 15.0% miss from formula alone. Cash the finding in as a 1-to-2-week artefact; do not extend it for months.

Order: tricky-pairs table this week (no approvals) → the file checker alongside it (days) → thermoelectric split list and leak report (1 to 2 weeks, on-disk data) → marking kit published with a specialist's sign-off → practice exam on public weighed sets → hidden exam with a partner.

---

## Traps: tempting things NOT to do

- **Launching your own leaderboard or platform.** An unknown newcomer's site has no pull; the collection's only outside issue has sat unanswered since March 2026 (`C16`). Contribute to tools people already use.
- **A small thermoelectric benchmark on public labels (the 1-to-2-month plan).** Every label is a published figure, so nothing is hidden; between-paper spread is 32.7% and the answer-knowing floor is 15.0% (`gaps`). The build list itself calls it a development set, not a blind test (`builds`).
- **The thermoelectric blind round now.** 17 missing rules, 22 major and 15 minor open issues, needs at least 3 labs, no pilot lab or cost estimate (`storyline`).
- **Automatic unit fixing.** Refuted: 85 of 266 fixable, measured wrong-fix rate 7.2% (interval 0 to 19%), fixed 0 of 12 proven cases (`storyline`).
- **Using public answers as a hidden test** (the synthesis ledger, the sister dataset, the Dara set, or the 134-case 2026 X-ray benchmark, whose answers sit in a public file with no licence and no scoring server; `C16`). Refuted.
- **"More" weighed mixtures of the same easy kind.** Refuted; the need is harder ones (errors sit in the 2-minute scans; `builds`).
- **Training a network to imitate the X-ray simulator.** Refuted; simulating a pattern already takes about 0.3 ms (`storyline`).
- **Expert relabelling of hard scans.** About 1,000 expert-hours, and chemists agree with each other only 35 to 70% of the time in the 2026 trust-score paper (`builds`, `C16`).
- **The "human overruled the program" test set.** Random guessing scores 20.1% and a perfect method 21.8%, so there is no room to show anything; one editor ID on all 1,216 checks (`C16`).
- **A big error-report campaign as the strategy.** Only 5 of 8 drafted items for the synthesis ledger are certain, about 30 of 1,035 samples hold a truly wrong value, its paper is still under review, and the mineral library's calculated files are already declared (`C16`). Send a short courteous note if you wish; it is a courtesy, not the contribution.
- **A new metadata standard, schema or handling-history format.** No lab is behind it, and you ruled this out as a default.
- **A fifth round of experiments before shipping anything.** Of 188 action items across the reports, 3 had all of how / owner / first step / done test (`storyline`). The shortage is shipped artefacts, not findings.
- **Reviving the simulated-data (Materials Project) side** because it has the only outside request. You parked it.

---

## What I could not find

- Any named outside user asking for these tools.
- A count of how many published models train on the thermoelectric database (this sets the ceiling on adoption of candidate 2).
- File sizes for two of the three public weighed-scan archives.
- Independent confirmation of the prior-art items (each came from one checker).
- A consistent count of the Dara benchmark files (notes say 40, 41, 60, 61 or 70; `builds`).
- How long a partner-lab weighed exam would take; the files give no figure.
