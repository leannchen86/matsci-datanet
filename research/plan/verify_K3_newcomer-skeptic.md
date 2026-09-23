# Verify K3 (Thermoelectric "the exam is too easy": short note, one frozen test list, a leak report) - lens: newcomer feasibility and value skeptic

Status: notes by one checker. No web access. I read only files inside this session's scratchpad (storyline, builds, gaps, C15, C16, the build list, the merged plan, three raw chat slices of the 14 September session, one report text). The thermoelectric data and scripts live in ANOTHER session's temporary folder, which I am not allowed to open, so I could not check that they still exist and I re-ran nothing. Every number below is "as the files say", with its source. Nothing was sent, downloaded, installed, published or changed.

Words used. Thermoelectric (TE) = a material that turns a temperature difference into a voltage. Seebeck coefficient (S) = how many volts you get per degree of temperature difference; it can be positive or negative. DOI = the permanent ID of a paper. Starrydata / teMatDb / ESTM = three open tables of TE measurements that people read off the plots in published papers. Random split = shuffle all rows, then cut into train and test. Paper-grouped split = all rows from one paper go to the same side (scikit-learn calls this GroupKFold). Chemical-system split = all rows made of the same set of elements go to the same side. kNN = nearest-neighbour model (predict from the most similar training rows). Composition = the chemical formula only. Specimen = the actual piece of material that was measured.

## Verdict: HOLDS WITH CHANGES

The core is sound and cheap: the numbers are in the files, the scripts are described as "one command", and the message is one an ML person can defend. But the candidate text (a) overstates how much of the jump is "leakage", (b) has one wrong and one unsupported claim, (c) leans on a tool route (MatFold) that probably does not fit, and (d) names no real user. Shrink it to a 2-3 day private version first; decide about the rest after a one-hour prior-art search that someone with web access must do.

## 1. Checks on the candidate's claims

| # | Claim | Result | Note |
|---|---|---|---|
| 1 | 93.5%, and 25.5 / 42.2 / 46.6 on 12,222 samples from 3,015 papers, 5-nearest-neighbour model only | confirmed | Raw chat slice of the 14 September session: median relative error on S 0.255 random, 0.422 paper-grouped, 0.466 chemical-system; 12,222 rows; 93.5% of test papers also in training under the random split. Same slice: a 1-nearest-neighbour model scores 21.4% on the random split (BETTER than 5-NN, a sign of copying a sibling row) and "always guess the training median" scores about 94%. |
| 2 | Lookup 22.9% beats model 29.4% on 3,593 samples; answers-known floor 15.0% | confirmed | Same session, second slice: lookup 0.2288, 5-NN 0.2944, answers-known 0.1501, n 3,593 samples from 1,703 papers. |
| 2b | "The 3,593 count is only in the transcript, not in the synthesis files" | wrong (harmless) | It is in gaps.md item G12 and in the TE benchmark report text. |
| 3 | Shared papers 183 / 26 / 4 by raw text, 193 / 75 / 7 after cleaning | confirmed | builds B2 and gaps G15. The cleaning function is named in the file inventory (te_common.py). |
| 4 | MatFold exists, is openly licensed, has no by-paper split | partly | The build list says MatFold is MIT-licensed and proposes contributing a paper-group split. Nothing in the files checks what MatFold accepts as input. From my own memory (NOT web-checked): MatFold is built around tables of crystal structures and splits by structure, composition, chemical system, symmetry and element. A plot-digitised table that has only a formula and a DOI is a poor fit. |
| 5 | "The TE files are still in the temporary folder; nobody has looked since 14 September" | partly / second half wrong | "14 September" is the day that session STARTED. The build list says Round 4 ran on these same TE files on 2026-09-18, so they existed today. But the folder is under the system's temporary area, and I could not look. Whoever owns that session must check. |
| 6 | Nobody has published a paper-grouped leakage result for TE data | not found | Not checked anywhere. gaps G16 says only "GroupKFold and MatFold exist; no TE task uses them", and G17 says its search was "not proven absent". See section 7 for what I would search first. |
| 7 | Problem statement: "TE prediction papers split data at random" | not found | I found no named TE paper in the files that is shown to use a random split. The whole note rests on this premise. It is probably true, but the note needs 3-5 cited examples, which needs web access. |
| 8 | 32.7% median difference for the same formula across 21,856 paper pairs (647 compositions); opposite sign in 3,881 pairs (17.8%) | confirmed | gaps G12. 3,881 / 21,856 = 17.8%. |
| 9 | Synthesis ledger 0.53 to 0.42 (rerun 0.49 to 0.39); steels 66 of 312 | confirmed, with a caveat the candidate dropped | Build list: "up to half the drop is shared by a temperature-only model". So at most about half of that drop is the leak. |
| 10 | "No yes needed to build if the files survived" | partly | The environment is "Python 3.14.6 with pandas and numpy (no sklearn)". A strong baseline needs an install (a download). Copying files out of the temporary area needs the user to name a folder; that offer was made earlier and never answered (storyline). |

## 2. The number the candidate does not show (most important finding)

The same script output that gives 42.2% also splits it in two:

- test rows whose formula ALSO appears in some training paper: 29.4% error (n 3,593);
- test rows whose formula appears in NO training paper: 48.1% error (n 8,629).

And on those same 3,593 rows, the 5-NN model scores 24.8% with the random split and 29.4% with the paper-grouped split.

Plain reading: when the formula is still available in training, holding out the paper costs about 5 points (24.8 to 29.4). Most of the headline jump from 25.5 to 42.2 comes from the 8,629 rows (70.6% of 12,222) whose formula the model has never seen. That is still a real and useful result ("random splits hide how badly models do on new formulas"), but it is NOT "the model memorised the paper". A reviewer will find this in an hour. The note must print this two-row breakdown itself and word the headline accordingly.

Small trap: "29.4%" appears twice with different meanings: 3,593 of 12,222 rows is 29.4%, and the 5-NN error on those rows is also 29.4%. Write both with their units every time.

Also: the 15.0% "floor" is measured only on those 3,593 rows and only for models that see the formula alone. It says nothing about the other 8,629 rows, and it is not a floor for a model that is also told how the specimen was made.

## 3. Can the first step really be done this week?

Yes IF the folder is still there; otherwise no.

- What the files say exists: baseline_300K.py (usage: one command with the raw data folder and an output folder), between_paper_spread.py (one command; it asserts that its kNN numbers equal the saved baseline to 12 decimal places), saved row files (12,222 rows for S, 12,158 for resistivity), a results file, and the DOI cleaner. If they survive, regenerating the table is minutes, not days.
- What blocks "this week":
  1. Nobody in this session can see that folder. The owning session or the user has to look. 5 minutes.
  2. Copying to a permanent place needs the user to name a folder. One sentence from the user.
  3. scikit-learn is missing. Installing it is a download, so it needs a yes. Python 3.14 is very new; heavier materials packages (the build list names MODNet) may not install on it at all. That is my inference, not a checked fact. Plan for "scikit-learn only".
  4. "One strong standard baseline" is not defined in the candidate. Define it now as: gradient-boosted trees (or a random forest) from scikit-learn on the vector of element fractions. That needs one install. Anything a materials person would call standard (hand-made element features, or a composition neural network) needs more installs; treat it as optional row two.
- Honest effort for one part-time person: 2-3 days for the small version in section 6. The full K3 (strong baseline under three splits, planted-duplicate test with a false-alarm rate, steels check, 4-page note) is more like 2-3 weeks part-time than the stated 1-2.

## 4. Domain knowledge that would silently trip a newcomer

1. S has a sign. The sign says whether current is carried by electrons or by "holes", and it can flip with a fraction of a percent of an added element. The files show this: opposite sign in 3,881 of 21,856 same-formula paper pairs (17.8%). A relative-error metric on a signed quantity that passes near zero behaves badly. Report three things side by side: median relative error, median absolute error in microvolts per degree, and how often the predicted sign is right. I did not see the last two in the slices I read.
2. One paper is usually a "doping series": the same base material with a small added amount stepped through 5-10 values. That is WHY sibling rows are near-copies. The note should say this in one sentence, because every TE reader knows it and will check that you do.
3. Holding out papers does not fully stop leaks. The same lab publishes the same specimens in several papers. The files' attempt to detect re-plotted curves was REFUTED (51 of 272 hits against 38-57 on shuffled nulls), so there is no working detector. Say so as a stated limit; do not try to revive the detector. The paper-grouped number is therefore still optimistic, by an unknown amount.
4. The task is "S at 300 K" (room temperature) only, with an interpolation rule (use two bracketing points no more than 60 K apart, else a point within 5 K). TE people care most about high temperature, where these materials are used. Expect the question "why 300 K?". Answer honestly: most rows have it, and it is a practice task.
5. Silent row loss. The script drops 1,267 rows whose formula it cannot parse, 696 rows with more than one S curve, 11,535 rows with no S near 300 K, and 62 out-of-range rows (raw chat slice; the starting count after keeping only measured rows is printed by the script but I did not record it). Formulas that fail to parse are not random: they tend to be composites and "x = 0.02"-style names. Print the funnel in the note.
6. The test labels themselves contain mistakes. The main session's estimate is about 1 in 25 curves badly wrong (C15); one comparison found 15 of 361 repeat readings more than 10% apart. A frozen test list freezes those errors too. Ship it as "v0, known label-error rate about 4%", and never silently fix values (automatic fixing is on the refuted list).
7. Which snapshot? The files disagree: one slice says the Starrydata snapshot is dated 2026-09-14 with matching checksums; the build list says the saved snapshot holds records only up to 2020-09-30, and that the database's own README warns that sample IDs repeat across papers in snapshots published 2026-04-01 to 2026-09-08 (untested). This must be settled BEFORE freezing anything, because a frozen list is only meaningful relative to a named snapshot. Freezing at the DOI level (not the row level) makes the list survive new snapshots: "these DOIs are test; everything else is training".
8. Which table? builds notes a cleaner set of 2,839 specimens from 870 DOIs as the intended development set, while all headline numbers are on 12,222 rows. Pick one for v0. I would freeze on the 12,222-row Starrydata set (one source, open licence, script exists) and leave ESTM out entirely (no licence).
9. Matching the same material across databases by formula is fragile (match rates 74.9% / 59.5% / 34.0% depending on the tolerance; builds B2). Keep K3 to DOI matching only.

## 5. Who exactly would use it, and how would they find it?

This is the weakest part.

- Named users in the files: none. The candidate itself says the files do not say how many groups train on this data. "Authors and reviewers of TE prediction papers" is a category, not a person.
- MatFold route: weak. If my memory of MatFold is right (not web-checked), a by-paper split for formula-only tables is outside what it does, and "hold out whole papers" is already one line of scikit-learn. The maintainers could fairly answer "use GroupKFold". Drop item (5) from the build, or reduce it to a question asked only after the user's yes.
- Better routes, all outward-facing, all need the user's yes: (a) a short preprint; (b) asking the Starrydata curators to link a recommended test list from their own page (C16 notes Starrydata "has a working fixes channel"); (c) proposing a TE task to an existing public leaderboard (gaps G17: neither of the two leaderboards searched has an experimental TE task).
- A certain, inward use: any later TE work by this user (the "spell-checker", the ceiling card K5) needs this split and this leak report anyway. That alone justifies the 2-3 day version. It does not justify two weeks of polish for an audience nobody has identified.
- The leak report ("X% of test items have a sibling in training") is the most reusable piece, including on the user's own XRD project, where C15 lists "exact duplicates straddling train/test" as an unchecked risk.

## 6. How does it fail, and is failure cheap and informative?

| Failure | Cost | What you learn |
|---|---|---|
| Folder is gone | 5 minutes to find out | A re-download needs the user's yes; its size is not stated in the files. The TE line gets more expensive, which matters for the TE-vs-XRD decision. |
| Prior-art search finds the same audit already published | 1-2 hours (needs web) | The note shrinks to "here is a frozen list and the floor"; still useful inside, much less outside. Do this BEFORE writing. |
| Strong baseline shrinks the jump | 1-2 days | Informative either way. The lookup-beats-model and floor results do not depend on it. |
| The two-row breakdown (section 2) changes the story | 0 days; the numbers already exist | The honest headline becomes "most test formulas are new, and models are bad at new formulas". |
| It is published and nobody uses it | weeks, and silent | NOT informative: you cannot tell "not useful" from "not found". This is the real risk. Agree one small signal in advance, e.g. one TE modelling author answers "would you report on this list? yes/no" (contact needs the user's yes). |

## 7. Would a domain expert take it seriously?

As written by an outsider with a 5-NN model: politely, no. With three changes: yes, as a useful small note.

1. One practising TE person (or a Starrydata curator) signs off one page: the task definition (S at 300 K, the interpolation rule, the metric, how sign is handled), the grouping unit (paper vs lab), and the wording of the 15.0% floor ("formula alone does not pin down the specimen": carrier density, how it was pressed and heated, measuring direction). This is the single thing that buys credibility. Asking anyone is outreach: needs the user's yes.
2. 3-5 cited TE prediction papers that really use random splits on these tables, plus a stated search for prior leakage audits. Things I would check first, all from my own memory and NOT verified: the ESTM dataset paper (Na and Chang, 2022) already tested prediction on unseen material groups; "leave one cluster out" cross-validation (Meredig and co-authors, 2018) made the general point for materials; a dataset-redundancy paper ("MD-HIT", 2023) made it for near-duplicates; Kapoor and Narayanan (2023) list leakage cases across sciences.
3. The honest label: "practice exam". The answers are published values, so it can never be a hidden exam (using public answers as a hidden split is on the refuted list).

## 8. Smallest shippable version (2-3 days, private, no install, one small yes)

1. Owning session or user: check that the TE folder of the 14 September session still exists. If yes, user names a permanent folder; copy scripts, saved rows, results file and DOI cleaner there.
2. Re-run the two one-command scripts; confirm 25.5 / 42.2 / 46.6 and 22.9 / 29.4 / 15.0 come back identical.
3. From the existing paper-grouped folds, write one text file: the test DOIs, the snapshot name, the file checksums of the raw data, and a SHA-256 of the list itself. Re-run; checksum must match.
4. Write the leak report as a 30-line function on pandas only: given a table, a split column and a group column, print "X% of test rows have a sibling in training". Run it on the three splits.
5. One private page: the three-way table, the two-row seen/unseen breakdown, the 1-NN-beats-5-NN line, the lookup and floor lines, the row-loss funnel, the known limits (same-lab leak, label errors, 300 K only, practice exam only).

Everything after that (install + strong baseline, steels check, planted duplicates, 4-page note, any publishing or contact) waits for the prior-art search and the user's yes.

## 9. Changes needed to the candidate

1. Fix claim 5: files were in use on 2026-09-18; still temporary; someone who is allowed must look. Fix claim 2's aside (3,593 is in gaps G12).
2. Add the seen/unseen breakdown (29.4% on 3,593 vs 48.1% on 8,629; 24.8% to 29.4% on the seen rows) and reword the headline so it does not claim the whole jump is paper memorising.
3. Do a 1-2 hour TE-specific prior-art search (web; not possible for me) BEFORE writing the note; collect 3-5 cited random-split examples or drop the premise sentence.
4. Drop or demote the MatFold pull request. Ship a GroupKFold recipe plus the frozen DOI list instead.
5. Define the strong baseline concretely (scikit-learn gradient-boosted trees on element fractions) and mark the install as needing a yes. Do not promise MODNet on Python 3.14.
6. Settle the snapshot question (2026-09-14 vs records-to-2020-09-30) and choose one table (12,222 rows vs 2,839 specimens / 870 DOIs) before freezing. Freeze at DOI level. No ESTM rows, ESTM DOIs only.
7. Fix the done-criterion "leak report reproduces 66 of 312 on steels": that result is a near-duplicate-formula check, which the simple sibling-in-group report in item (3) cannot produce. Either add a formula-distance option or drop the criterion.
8. Add absolute error and sign accuracy next to relative error; print the row-loss funnel.
9. State the limits in the note: same-lab leakage is not removed (detector refuted, do not revive), about 4% of test labels are badly wrong (never auto-fix), floor holds for formula-only inputs on the seen rows only, practice exam never hidden.
10. Add one specialist sign-off on the one-page task definition as a done-criterion. Outreach, publishing the note / DOI index / list, and any install or re-download: each needs the user's explicit yes.
11. Re-estimate effort: 2-3 days for the private version; 2-3 weeks part-time for the full K3.
