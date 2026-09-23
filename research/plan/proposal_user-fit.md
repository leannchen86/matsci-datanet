# Proposal through one lens: what fits THIS user

Written 2026-09-18 from the digested session files only. Nothing was re-measured. Nothing was sent, published or downloaded. Every number is copied from those files, with its denominator and the file it came from in brackets.

Two planned inputs were not available: the critic file did not exist, and the gaps file stops at gap 29 of a planned 50.

How sure each number is:
- [measured] = a session ran code on real files.
- [one checker] = found by a single agent in the XRD session and not re-verified.
- [opinion] = my reasoning.

Source names: `C16` = the XRD session's verification digest. `C15` = the late-updates digest. `C06` = the Periodic Labs session digest. `build list` = the ranked build list. `builds`, `storyline`, `glossary` = the three synthesis files.

---

## 1. Answer first

**Start with a fair marking kit for X-ray "name the ingredients" answers, grown out of your own project.** Keep the thermoelectric work to its two cheapest pieces.

Words used below, once:
- **Powder X-ray scan (XRD):** shine X-rays on a powder and get a 1-D curve of peaks, a fingerprint of the crystals inside.
- **Phase:** one distinct crystalline compound in the powder. "Phase identification" = naming the ingredients from the curve. In ML terms: multi-label classification where some true labels may be missing from the label set.
- **Dara / Jade:** an open program and a commercial program that do this naming.
- **dara-conform:** your own project. It adds honest confidence scores and an "I don't know" option on top of Dara.
- **Weighed mixture:** powders weighed out by hand and mixed, so the recipe is known for certain. It is the only kind of answer key here that does not rest on an analyst's opinion.
- **Reference library:** the catalogue of known crystal structures a program searches. One is open (COD); two are paid (ICSD, ICDD).
- **Thermoelectric (TE):** a material that turns heat into electricity. The main measured quantity is the Seebeck coefficient [voltage produced per degree of temperature difference].

---

## 2. Four facts that decide the fit

1. **The strongest new evidence came out of your own project files.** On the same 40 weighed-mixture scans, the same program scores 12 of 40, 17 of 40 or 32 of 40 depending only on the rule that decides whether a predicted ingredient "equals" the answer-key ingredient. The paper reports 38 of 40; that run used a paid reference library, so the last gap is not only the rule [measured; C16]. Across 210 pilot rows, 63 answers were credited under the loose rule, and 18 of those 63 (28.6%) would be marked wrong under the strict rule [measured; C16]. For scale: the published argument between the two programs is 38 of 40 versus 35 of 40, a gap of 7.5 points with an interval of 0.0 to 15.0 [measured; builds]. The marking rule moves the score more than the tools differ.
2. **Your project already names this as its fallback.** Its frozen plan says: if confidence scoring ships inside Dara, "shrink to the evaluation harness" [the marking and scoring code] (C16). The group that makes Dara has since published a trust score on top of it, called AIF [one checker; C16]. Whether that triggers the fallback is your call. Either way the marker is needed, because your own headline number depends on it.
3. **Neither existing rule is right, and a newcomer cannot fix it alone.** On 18 tricky cases the strict rule is wrong on 8 and the loose rule on 13. The loose rule treats Nb2O5 and Nb12O29 as one compound, and a hydroxide as a peroxide. The session's own tempting fix ("same symmetry group") would be wrong in at least 3 cases [measured; C16]. So the kit needs one practising diffraction specialist to check it. That is a feature: it is the smallest concrete reason to talk to a lab.
4. **The thermoelectric line has no such anchor for you.** It has more data (55,422 samples) and a built-in arithmetic check. But there is no project of yours there, no contact, and a second vocabulary to learn. Its record checker is sized at 1-3 months in the build list (1-2 weeks only for a narrow version) (builds). Its real hidden exam needs at least 3 measuring labs, and its spec still lacks 17 rules (builds).

One honest caveat on fact 1: part of that swing is a bug in your own project's marker, and your local set-up (open library, 80 candidates per search) is not the published one (C16). Say so up front. "My own number moved 20 points when I fixed my marker; here is the table" is a stronger opening from an outsider than "the field is wrong".

---

## 3. What makes a first public thing believable from an outsider [opinion]

| The first thing should be | Why |
|---|---|
| Small enough for an expert to check in ten minutes | Experts ignore big claims from strangers, but will look at 25 rows |
| Useful to the expert, not only to you | A marker and a file check save them work |
| Honest about your own mistakes first | "Here is what it changed in my project" earns the right to say "here is what is wrong in yours" |
| Reproducible by one command | It is the one thing an ML person can do better than most labs |
| Signed off by one insider, with disagreements shown | Borrowed credibility, and it shows you asked |
| Certain items only | One overclaim and later notes go unread |

A large benchmark, a "standard" or a long error list does the opposite of all six.

Your edge is exam design: marking rules, splits, test size, telling a real gap from noise. Materials people rarely have that, and ML people rarely have the chemistry. The best first contribution sits on that seam.

---

## 4. The candidates at a glance

| # | Candidate | Track | Effort | Data on disk? | Needs your yes for | Fit in one line |
|---|---|---|---|---|---|---|
| 1 | Fair marking kit (recommended) | XRD | first step: days; kit: 1-2 weeks | yes | publishing; contacting a specialist; any change inside your project | Your project's own fallback; evidence from your own files; teaches crystal chemistry one pair at a time |
| 2 | Clean your own file list, then a "check my file list" tool | XRD | days | yes | publishing the table or tool; any change inside your project | "What it changed for me" before "what is wrong with yours" |
| 3 | Two short error notes, certain items only | cross-cutting | days | yes | sending (you send personally); fetching source papers | First contact as a gift; forces you to learn what each field means |
| 4 | Fair-split maker with a leak report | cross-cutting (TE first) | 1-2 weeks | yes, but in a temporary folder | publishing only | Pure ML craft; least chemistry; the safe second line |
| 5 | Desk stage of a hard known-answer exam, plus a one-page lab request | XRD | desk: days; real exam: needs a partner lab, 3-12 months | partly | downloads; contacting a lab; buying powders | The only item where your lab and Mandarin/Taiwanese connections decide the outcome |

---

## 5. Each candidate

### Candidate 1 (recommended). A fair marking kit for "which ingredients are in this powder" answers

- **What is broken, for whom.** Every team that tests a phase-naming program must decide when a predicted ingredient "equals" the answer-key ingredient. The rule is unwritten and home-made, and it swings the score more than the gap between programs. Your own project is affected first.
- **Evidence.**
  - 12 / 17 / 32 of 40 for one program on the same 40 scans under three marking rules; paper reports 38 of 40 [measured; C16].
  - 18 of 63 credited answers (28.6%) depend on the rule [measured; C16].
  - Strict rule wrong on 8 of 18 tricky cases; loose rule wrong on 13 of 18 [measured; C16].
  - Most misses are naming artifacts: "LaO3" for La(OH)3, "Ni1.875O2" for NiO, "V4O9.93316" for V2O5 (C16).
  - Writing a formula in a different order (BiVO4 vs VBiO4) flips 3 of 20 of the commercial program's verdicts; an ingredient listed twice is still marked correct in 4 of 4 and 2 of 3 cases [measured; builds].
  - The standard open structure-comparison tool, at default settings, merges two truly different forms of quartz; a tolerance of 0.15 or less separates them [measured; builds].
  - 15 of 56 rows in your pilot results carry out-of-date loose-rule marks (64 stored vs 79 recomputed, out of 260) [measured; C16].
  - One public benchmark gives 30% of its mark to a language-model judge, and another uses a language-model judge outright [one checker; C16]. "No installable marker or rule card exists"; the ideas date to 1990 [one checker; C16].
- **What to build.** Three small things:
  1. A table of about 25 tricky pairs (answer-key name vs the program's answer), each with a one-line plain reason.
  2. A one-page rule card that returns a tier ("same", "same family, different form", "different", "cannot tell"), not a yes/no, because experts themselves dispute some cases.
  3. A small runner that marks any list of answers with the card and prints the score under each rule side by side.
- **First step this week (one person, at a desk).** In a new permanent folder, reading your project without changing it:
  1. Assemble the ~25 pairs from misses already found: the three naming artifacts above, the BiVO4 spelling case, Nb2O5/Nb12O29, WO3/W18O49, TiO2/Ti9O17, the two quartz forms, mirror-image quartz, the two Y2O3 symmetry groups, the listed-twice case.
  2. Run five markers on every pair: strict formula, loose formula, the structure tool at default, the structure tool at tolerance 0.15, the proposed tier.
  3. Re-mark the 40 weighed scans under each marker. Put the five scores in one table.
- **Effort.** First step: days. Whole kit: 1-2 weeks. Specialist sign-off: needs one contact.
- **Data on disk?** Yes per the corpus: the 40 mixture scans, 10 single-ingredient scans, the pilot results and an open reference library are on your machine, and Dara is installed (C16). A 21-pair starter script sits in the XRD session's temporary area (C16). The corpus gives five different file counts for the Dara set (40, 41, 60, 61, 70), so count first (builds).
- **Needs your yes.** None to build privately, as long as you are fine with your project being read, not changed. Yes needed to: change anything inside your project; publish the table or tool; contact a specialist.
- **Who benefits.** Your own project first. Then anyone running such a test, including teams that today mark answers with a language-model judge.
- **Why it is smart.** Specialists mark by eye, so they never needed a runnable rule. ML people need one and lack the chemistry. The kit is the entry ticket for any later hidden exam; without it that exam reproduces the 12-versus-32 problem. Each pair teaches you one real piece of crystal chemistry (same formula in different crystal forms, water-bearing compounds, off-ratio formulas). And "please look at these 25 rows and tell me where I am wrong" is the smallest credible request an outsider can make of a lab.
- **Biggest risk.** Three, all real. (a) Prior art: "nothing exists" rests on one checker. (b) A rule tuned on 25 hand-picked pairs can overfit them. (c) A marker is only as useful as the exam it marks, and the only certain exam on disk is 40 easy scans. Guards: tune on half the pairs and hold out the rest; ask the specialist for about 10 unseen pairs; size it as a small contribution and pair it with candidate 5.
- **Done looks like.** One command rebuilds the pair table and the five-score table from files on disk. On held-out pairs the tier rule is wrong less often than both current rules (today 8 of 18 and 13 of 18). One practising diffraction specialist has reviewed every row, and their disagreements are recorded, not hidden.

### Candidate 2. Clean your own file list first, then offer a tiny "check my file list" tool

- **What is broken, for whom.** Public collections of "measured" scans contain simulated scans and copies. People train and test on them without knowing, your project included.
- **Evidence.**
  - In one open collection (opXRD), all 499 files from one contributor have intensity values identical to files in a public mineral archive (RRUFF). 414 of the 499 are simulated but flagged "not simulated". The same group re-published 261 of them elsewhere as "experimental" [measured and re-hashed; C16]. This match is undisclosed and new.
  - By contrast, "1,702 of 3,019 RRUFF files labelled RAW are simulated" is stated in the files' own headers and already noted by others, so it is not news (C16).
  - 124 of 2,680 files are exact copies, in 61 groups [measured; C16].
  - Effect on your project is small: 0 of the 499 copied files are in it; 8 of its 200 RRUFF rows are suspect (2 in the pilot); 8 duplicate pairs; its filter searches for "calculat" and misses "computed" [measured; C16].
  - Eight papers use between 148 and 3,002 RRUFF "experimental" files without listing which ones [one checker; C16].
- **What to build.** Private part: run the check against your project's own 1,554-row file list (1,396 active; C16), fix the filter word, and confirm no copy sits on both the training and the test side (this risk is unchecked today; builds). Public part: the 499-row match table with neutral wording ("intensity values identical to RRUFF file X"), one column saying what each judgment rests on, and a tiny checker (input: a list of file ids; output: how many are simulated or copied).
- **First step this week.** Name a permanent folder and move the existing file list out of the temporary area. Run the private part. Write half a page: what changed in my own project.
- **Effort.** Days.
- **Data on disk?** Yes per the corpus. The finished list sits in a temporary area that can vanish (storyline).
- **Needs your yes.** Any change inside your project; publishing the table or checker.
- **Who benefits.** Your own results first; then anyone assembling a training set from these collections.
- **Why it is smart.** Saying honestly that the effect on your own project was small is itself a trust signal. The tool answers a question eight papers left open.
- **Biggest risk.** Low impact. The collection's only outside issue has been unanswered since March 2026 [one checker; C16]. Treat it as hygiene, not a headline.
- **Done looks like.** Your file list has zero known-simulated rows and zero copies across the train/test line. The checker gives the same counts on a second machine. The public part exists only after your yes.

### Candidate 3. Two short error notes that contain only certain items

- **What is broken, for whom.** Open records contain mistakes nobody reports. But the drafted error lists overclaim, and an outsider who overclaims once is ignored afterwards.
- **Evidence.**
  - Synthesis ledger (Precursor Genome: 1,035 robot-lab synthesis attempts with their scans). All 8 drafted counts reproduce, but only 5 items are certain, and about 30 of 1,035 samples (about 3%) hold a truly wrong stored value. Four drafted items must be withdrawn [measured; C16]. The earlier "28% carry an error" was already refuted; the strict count is 93 of 1,035 (build list).
  - That ledger's paper is still under review, so a public issue would be seen by its reviewers (C16).
  - Thermoelectric database (Starrydata: curves read off published figures). 8 wrong records found (Celsius stored as kelvin twice, a sign flip, a swapped curve and others), among 15 large disagreements in 361 comparisons [measured; build list]. It has a working corrections channel (C16). Caveat: no source paper was opened when these 8 were judged (build list).
- **What to build.** Two notes of at most one page. Every item carries the sample id, one line to reproduce it, and a tag: "the file contradicts itself", "the file contradicts the paper", or "a question". Plus one script that re-creates every item. The ledger note goes privately to the authors.
- **First step this week.** Read the ledger's paper and the 8 thermoelectric source papers. Cut both notes to certain items only. Hand the drafts to you; you decide and send personally.
- **Effort.** Days.
- **Data on disk?** Yes per the corpus; a five-item draft note exists in the XRD session's temporary area (C16). The older, longer draft still contains the four items to withdraw.
- **Needs your yes.** Sending anything; fetching source-paper PDFs; publishing a corrections file.
- **Who benefits.** The dataset owners and everyone downstream. You gain a first friendly contact on each side.
- **Why it is smart.** Five certain items beat fifty debatable ones. It is the shared first step of both the TE and the XRD line, so it costs nothing to the decision between them.
- **Biggest risk.** Being wrong in front of the authors or their reviewers. The cure: read the paper first and label questions as questions.
- **Done looks like.** Every item reproduces from one script. Zero items rest on a guess about intent. You have said yes or no to each note.

### Candidate 4. A fair-split ("fair exam") maker with a leak report

- **What is broken, for whom.** Test items are not really new to the model, so reported accuracy is too good.
- **Evidence.**
  - With a random split, the test sample's own paper is already in training 93.5% of the time. Median error on the Seebeck coefficient rises from 25.5% to 42.2% when whole papers are held out (12,222 samples, 3,015 papers) [measured; build list].
  - A plain lookup of the same composition (22.9% error) beats the ML baseline (29.4%), and even a lookup chosen with the answers known misses by 15.0% [measured; builds].
  - Matching paper ids as raw text finds 183 / 26 / 4 shared papers between three databases; after cleaning the ids the counts are 193 / 75 / 7 [measured; build list].
  - The right grouping differs by dataset: holding out a starting powder in the synthesis ledger drops the score from 0.53 to 0.42, while grouping by chemistry barely matters [measured; build list]. In a steel benchmark, 66 of 312 groups have a near-copy in another group [measured; build list].
- **What to build.** A tool that takes a table and a grouping key (paper, starting powder, or copy group) and writes the split, a leak report and a file list. Build on the existing open split tools; the new parts are the leak report and the cross-database paper matcher.
- **First step this week.** One command that reproduces the 25.5% to 42.2% table. Then run the same leak report, without changing anything, on your XRD file list.
- **Effort.** 1-2 weeks.
- **Data on disk?** Yes per the corpus, but the thermoelectric files sit in a temporary session folder; move them first. The paper-id cleaner is saved (build list).
- **Needs your yes.** None to build. Publishing needs a yes.
- **Who benefits.** Anyone training on literature-derived tables; your own project.
- **Why it is smart.** It is the most ML-native item in the corpus and needs the least chemistry, so it is the safest second line. It is also the honest bridge between the two lines: same tool, different grouping key.
- **Biggest risk.** A materials split tool already exists, so splitting itself is not new. The test labels are public literature values, so this gives a fair practice exam, never a hidden one (builds). The audience is ML-for-materials people, not domain experts.
- **Done looks like.** The split table reproduces exactly. The leak report's false-alarm rate is measured on shuffled data. Each dataset's grouping key is written down with the reason.

### Candidate 5. Desk stage of a hard known-answer exam, plus a one-page request for a partner lab

- **What is broken, for whom.** Scans with a certain answer are too few and too easy: 40 scans, and 38 of 40 versus 35 of 40 cannot be told apart [measured; builds]. Human and program answers differ on 316 of 343 scans in the largest open ledger, and all 1,216 human checks carry one editor id, so there is no independent answer key [measured; C16]. The AIF paper reports that this annotator reversed 83.3% of re-reviewed cases and that chemists agree pairwise only 35-70% of the time [one checker; C16].
- **Evidence for size.** Near 50% accuracy, about 385 separate powders are needed for a plus-or-minus 5 point estimate. Telling two tools 5 points apart needs about 470-780 paired powders (C16 arithmetic). Harder public weighed sets appear to exist: a round-robin set with 4 and 7 ingredients and minor ingredients at 1-5% by weight; 240 two-ingredient mixtures; a spiked series down to 0.12% by weight [one checker; C16]. None is on disk.
- **What to build at the desk.**
  1. The "replay test": rebuild the 40 mixtures by adding up single-ingredient scans, weighted for how strongly each compound absorbs X-rays, and check whether the program behaves as it did on the real mixtures. About 25 minutes of compute plus about a day of coding (C16). If it works, cheap practice exams become possible.
  2. A one-page request: what a partner lab would weigh, how many powders, how long each scan, what they get back.
- **First step this week.** Only after candidate 1's marker is frozen: run the replay test.
- **Effort.** Desk stage: days. Real exam: needs a partner lab, 3-12 months (build list).
- **Data on disk?** For the replay, yes (40 mixture and 10 single-ingredient scans). The harder public sets, no.
- **Needs your yes.** Downloading the harder public sets; contacting any lab; buying reference powders (past contest powders are listed at $250 per unit [one checker; C16]).
- **Who benefits.** Every team building such programs, and your project most of all: a confidence score can only be checked against answers that do not depend on an analyst.
- **Why it is smart.** Hidden, physically weighed answers are what a company with its own lab keeps private. A small outside team with one friendly lab can make them public. It needs one lab, one instrument and a balance, not the 3 or more labs the thermoelectric exam needs. The corpus names a Taiwanese powder-diffraction beamline and thesis library as possible routes (C06); nobody has been contacted.
- **Biggest risk.** Needs a lab. The replay may fail: added-up scans differ from real ones by about 4 times the counting noise, and 8 of the 10 single-ingredient scans are on a shifted grid (C16). A long-running human contest with weighed mineral powders already exists, so the new part is narrow: a standing, machine-marked test with hidden recipes and 4 or more ingredients (C16).
- **Done looks like.** A go / no-go on the replay with the numbers behind it, and a one-page request you are willing to send.

---

## 6. The one thing to start this week

Candidate 1's first step: the ~25 tricky-pair table and the 40 weighed scans re-marked under five rules, in a new folder, reading your project without changing it. It is your project's own written fallback, its evidence came from your own files, and it needs no lab, no download and no approval to begin.

Before anything else (half a day): name a permanent folder. Several inputs sit in temporary areas that can vanish (storyline).

## 7. Thermoelectric line vs XRD line: my view

**For this user, XRD first. The deciding reason is fit, not data volume.**

| Question | XRD line | Thermoelectric line |
|---|---|---|
| Is there a project of yours to build on? | Yes, and its frozen fallback is the recommended build | No |
| Where did the decisive evidence come from? | Your own pilot files (12 / 17 / 32 of 40) | Session experiments on public tables |
| Labs needed for the real hidden exam | One lab, one instrument | At least 3 labs; 17 rules still missing (builds) |
| Vocabulary to learn | One field, already started | A second field |
| Pure-desk value without any lab | Marker + file check: small but real | Fair-split maker + record checker: larger |

The two lines are not rivals in the first week: they share the first step (send the certain error items, after your yes) and the same shape afterwards (checker, fair exam, small benchmark) (storyline). So keep the thermoelectric line's two cheapest, most ML-native pieces, the 8-record note and the fair-split maker, and park its record checker and benchmark.

**When to switch:** if after about two weeks no diffraction specialist will look at 25 rows, or a proper prior-art check finds a working marker already exists, move the main effort to the fair-split maker and then the thermoelectric record checker.

## 8. Tempting things not to do

- A big benchmark or "standard" as the first public thing. The thermoelectric exam spec lacks 17 rules, has 22 major and 15 minor open review issues, and needs 3 or more labs (builds).
- Presenting the 12-to-32 swing as a field-wide finding. Part of it is your own marker's bug and a non-published set-up (C16). Lead with that.
- Writing the "same ingredient" rule without a specialist. The session's own "same symmetry group" idea was wrong in at least 3 cases (C16).
- Sending the error lists as drafted. Only 5 ledger items are certain (about 30 of 1,035 samples); four must be withdrawn; the paper is under review (C16).
- Announcing "56.4% of RRUFF raw files are simulated" as a discovery. The files say so themselves. The undisclosed part is the 499-file match (C16).
- Fixing unit errors automatically. Refuted: 85 of 266 fixable; wrong-fix rate 7.2% (interval 0-19%); 0 of 12 proven cases fixed (build list).
- Starting the thermoelectric record checker (1-3 months in the build list) before anything has shipped in the first field.
- A fifth round of experiments before shipping anything. Of 188 action items across the reports, only 11 had a first step and 8 a done test (build list).
- A new metadata or sample-history standard with no lab behind it. This is your own guardrail.
- Expert re-labelling (about 1,000 expert-hours; build list), or a test built on "the human overruled the program": on the big ledger a random guess scores 20.1% and a perfect method 21.8%, so there is nothing to win (C16).
- Using any public answers as a hidden test. Refuted. One public benchmark's 134 answers turned out to be public too (C16).
- Re-hosting reference files that derive from the paid structure database (C16).
- "More weighed mixtures" rather than harder ones. Refuted (builds).
- The computed-data side. Parked by your own decision (build list).

## 9. Everything that needs your explicit yes

- Any change inside your own project (reading it is assumed fine; say if not).
- Sending either error note (you send personally).
- Publishing the pair table, the rule card, the checker, the match table or a corrections file.
- Contacting a diffraction specialist or any lab.
- Any download: source papers for the error notes, the harder public weighed sets.
- Any purchase.
