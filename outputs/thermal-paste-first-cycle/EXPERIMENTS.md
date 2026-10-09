# Experiments beside the pilot

Selected 7 October 2026. Nothing here has been run. The pilot's steps are unchanged and stay on [CHECKLIST.md](CHECKLIST.md). The experiments do not wait for the pilot to be packed. This page takes over from sections 5, 6 and 8 of [BENCH_PROTOCOL.md](BENCH_PROTOCOL.md).

**What this is.** Three small experiments. Each sets named pictures of how the paste behaves against each other, and each picture commits to a number before the run. All three sit at the mixing limit, where differences are largest and the result is a weighed amount.

**What it is not.** Proof that a trajectory beats a table. Each experiment changes a route or a composition on purpose, and a table column can hold that. The trajectory's value is tested only by the comparison in [Forecasts](#forecasts).

Every number marked *placeholder* is an illustration with made-up inputs. The real prediction is the same formula fed with inputs measured on this bench, logged before the run it predicts. The formulas are fixed in [predict.py](predict.py). Run every command on this page from the top folder of the repository.

## Words used

- **Loading:** the share of the paste's volume that is powder. 0.40 is 40 vol%; a change of 0.01 is 1 vol%. `python3 outputs/thermal-paste-first-cycle/predict.py loading --powder 12.00 --oil 2.40` gives it from two weighings; `python3 outputs/thermal-paste-first-cycle/predict.py oil --powder 12.00 --loading 0.52` gives the oil for a chosen loading.
- **Titration:** adding one ingredient in small weighed steps until the paste changes state.
- **Endpoint:** after 60 counted strokes, one per second, slow press-and-smear, the whole charge is one glossy body that closes over a spatula cut within 10 seconds and shows no matt patch when pressed.
- **Mixing limit:** the highest loading that still passes the endpoint. It is the midpoint between the last pass and the first fail.
- **Dry side:** start with powder and add oil until it passes. **Wet side:** start with oil and add powder until it fails.
- **Blend:** coarse and fine powder together. *x* is the fine share of the powder; the pilot recipe has x = 0.30.

## Order of work

**C1 may start on any bench day that begins with all five of these already true.** The day a practice batch passes is a LAB day, so it cannot also be C1. The day you run C1 is day 0.

1. The balance check (checklist S5) has passed.
2. The handling review (checklist G1b) is settled and allows, by name, the steps you are about to do: many small powder additions to one cup, working tubs, oil added to dry powder and stirred, and a dry blend tumbled in a lidded cup. Any condition it sets, such as a respirator, is in place. If it says no to any of these, C1 does not start and the plan goes back to the project owner.
3. The three new oil bottles are in hand, their lots are recorded, and they are marked EXP (checklist N5).
4. Both first forecasts (`E12-DESK` and `E3-DESK`, from every model) were logged, anchored, pushed and timestamped outside before either powder was opened.
5. A practice batch (checklist B1) has passed and its method is written down.

Not on the list: the pilot being packed, any reply from the lab, the rig check, or the second person's reading. The last two are needed at the commissioning gate. If the lab has already named a container and a date when the practice batch passes, batches A and B take the next two bench days, they are packed, and C1 comes next. That is an order, not a sixth condition: C1 does not wait for the drop-off or the report. The bench rules for running both are on the [checklist](CHECKLIST.md#rules-for-running-two-tracks).

- [ ] **C0a.** First forecasts, at the desk, with this page and `predict.py` attached to the log. Before either powder is opened for anything, the practice batch included.
- [ ] **C0b.** Rig check on plain oil and the reference paste. No powder. Any day before the commissioning gate; it does not hold up C1.
- [ ] **C1 to C4.** Commissioning: four powder days in week 1.
- [ ] **Settling stage 1.** Set up on the first experiment day after C1 that the vials are in hand and the handling review has said yes to filling vials. Its 14-day clock is the longest in the programme.
- [ ] **Commissioning gate.** All five checks pass. Compute and log every prediction.
- [ ] **Block.** Six titration days over weeks 2 and 3, not consecutive. Experiments 1 and 2 share them.
- [ ] **Part B.** Three short days, only if Experiment 1 finds a gap.
- [ ] **Settling stage 2** and its day-7 reading, weeks 4 and 5.
- [ ] **Write-up** in the claim wording given under each experiment.

About 14 bench days over four to five weeks.

## C0. Desk forecasts and rig check

**C0a. First forecasts (the desk test).** Needs only the parcel labels. Send each forecasting model the two prompts in [desk-test-prompts.md](../../trajectory/desk-test-prompts.md). They contain none of this page. In the same sitting, copy this page and `predict.py` into the `paste-commission` log's `raw/` folder and attach them to a `note` entry, so the thresholds are fixed in the record. Log, anchor, push and timestamp before either powder is opened for anything, the practice batch included: the pilot recipe is itself one of the things being forecast.

**C0b. Rig check.** Needs the balance check passed, the plates and weight, the new oil, and wet-work handling allowed in writing (checklist G1a ticked, or G1b settled if you wrote that it waits). An EXP day, any time before the commissioning gate.

1. **Oil between plates.** Weigh the top glass plate and the 500 g weight separately. If the weight is at or over the balance's capacity, do not weigh it; record its stated mass and tolerance. Use the new oil (EXP). Put 0.50 mL of oil (0.485 g) at the centre of the lower plate, lower the top plate flat, and photograph from above, with a ruler or millimetre grid under the lower plate, at 30, 60 and 300 seconds. Compare the diameters with `python3 outputs/thermal-paste-first-cycle/predict.py squeeze --plate <plate grams>`. **Pass:** within 5% of the "with capillary pull" column (for an 80 g plate, *placeholder*: 62, 69 and 92 mm). Diameters below the "plain viscous" column mean a tilted or bowed plate or a timing fault; fix that first.
2. **Reference paste between plates.** Two loads (plate; plate plus 500 g) by two doses (0.5 and 2.0 mL), two runs of each, order drawn at random, photos at 30 and 300 seconds. This shows how a real paste stops spreading. No experiment below scores a spread number. Use the reference-only tool. Wipe the plates with alcohol and never wash them at the sink. Every wipe, glove and scraping goes in the reference-paste tub. Log the date the tube was first opened.

## Commissioning, week 1

| Day | What you do | Pass |
|---|---|---|
| **C1** | One fresh pilot-recipe batch on the new oil, by the method written after the practice batch. It is a warm-up: not a third pilot batch, not compared with A and B, not sent to the lab. Then practise one dry-side and one wet-side titration on coarse powder (not counted). Then make the two reference cups described below the table. | All ten reference photos sorted correctly (judged at the gate, not on the day). If not, fix lighting and framing and retake. |
| **C2** | Dry packing in a 100 mL stoppered cylinder: coarse, fine and blend, three fresh fills each. Pour through a funnel from a fixed height, read the volume, then tap from a 10 mm drop in blocks of 100 until two readings agree within 1 mL. Record every reading. | Three tapped fills agree within 2%. |
| **C3, C4** | Twelve dry-side titrations: three coarse and three fine each day, interleaved. | Scatter of the limit is 0.015 or less. If not, change step size, strokes or lighting and repeat. |

**C1 reference cups.** Take L, your own bench call of the coarse dry-side limit from today's practice cup. Make two fresh cups of 12.00 g coarse powder: a known paste at loading L minus 0.03 and a known crumb at L plus 0.05 (oil for each from `predict.py oil`; for L = 0.55, *placeholder*, 2.71 g and 1.95 g). Add the oil in 0.20 g steps, 60 strokes after each. Check that the first passes the endpoint and the second fails; if not, log it and move that cup 0.02 further from L. Take five photos of each with the same lighting and framing as titration photos. Give the ten photos shuffled code names and keep the key. The second person sorts them without the key; this may trail the bench by a few days. If there is no second person, do not sort them yourself: keep them as references and write down "unblinded".

C2's cylinder work is more open-powder handling than the pilot, and its funnel pour departs from the project's own limit of never pouring powder from height. So does adding oil to dry powder. Both need the handling review's yes by name. If it says no to the cylinder, skip C2; only the packing-memory picture in Experiment 1 loses its number. If it says no to adding oil to dry powder, no dry-side titration is run, C1 does not start, and the plan goes back to the project owner.

**Commissioning gate.** Balance check passed; oil within 5% of the curve (C0b); reader separates paste from crumb (needs the second person, or a written decision to report as unblinded); tapped density within 2%; limit scatter 0.015 or less. Every detection limit on this page assumes a scatter of 0.01, which is a guess until C4.

**Then, at the desk:** compute every prediction from the measured inputs, log and anchor them with the models' second forecasts. No blend is titrated before that entry exists. No scouting.

## How to run one titration

Every cup is at one scale: 12.00 g of powder (dry side) or 2.50 g of oil (wet side). Hold the cup by the rim. Use a metronome (a phone app will do). Write each cup on its own ruled page: cup id, date, EXP, powder, direction, empty-cup mass, then one line per step with the balance reading of that addition alone, the strokes, the photo number and your call. Photograph the page when the cup is finished and type it into the log the same day.

**Dry side.**
1. Weigh 12.00 g of powder into the cup. For a blend weigh coarse and fine separately (x = 0.30: 8.40 g and 3.60 g), put the lid on and tumble 100 turns. Never scoop from a pre-mixed jar; the two powders sift apart.
2. Add oil in 0.20 g steps, 60 strokes after each, until the mass first forms one lump.
3. Then 0.05 g steps (each moves the loading by about 0.005). Photograph every step.
4. When you judge it has passed, carry on three more steps so the reader's boundary lies inside the photos.

**Wet side.**
1. Weigh 2.50 g of oil into the cup.
2. Add powder in three rounds of 3.0 g (fine alone: 2.0 g), 60 strokes after each.
3. Then 0.50 g steps until it first holds a peak, then 0.25 g steps (about 0.005 each). For a blend each step is coarse then fine, weighed separately (0.175 g and 0.075 g). Photograph every step.
4. A fail counts only if it still fails after 120 more strokes with nothing added. If it passes, carry on.

**Both.** Do not add up the oil or powder until you have called the endpoint. The spatula is never wiped or scraped on the rim; when it is out of the cup it lies on its own rest, and "rest + spatula" is weighed clean before the cup and again at the end. At the end weigh the cup too: the cup's gain plus the spatula's gain should match the additions within 0.05 g. No powder or crumb may sit on the wall above the paste when you judge a step. The limit that counts is read from coded photos by the second person, who does not know the powder, the direction or the prediction.

## Experiment 1. Is the mixing limit one number or a window?

**Question.** Does the same powder reach the same limit from the dry side and from the wet side? W = dry-side limit minus wet-side limit.

| Picture | What it says | Predicted W for coarse, blend, fine |
|---|---|---|
| **State** | The limit belongs to the recipe; how you got there does not matter | Below 0.03 for all three |
| **Packing memory** | Kneading a damp mass packs grains dense; folding powder into liquid leaves them loose. True of any powder | Positive for all three. W = tapped minus poured packing of that powder from C2, no fitted number (*placeholder*: +0.09), with a band of at least 0.03 |
| **Clump** | Only the fine powder travels as clumps that hold oil; kneading breaks them and stirring does not | Coarse below 0.03; blend 0.03 or more; fine at least as large as the blend |
| **Trapping** | A mass that has been crumbs keeps dry lumps or air and does not re-wet | Minus 0.03 or lower where there are fines |

The names label patterns of signs. They are not established causes. Coarse powder alone is what separates packing memory from clump.

**Runs.** Six block days. Order within each day is drawn beforehand.

- P days (three): coarse dry, fine dry, blend dry, blend wet, coarse wet.
- Q days (three): coarse dry, fine dry, fine wet, and Experiment 2's three blends.

**A gap counts for a powder only if all four hold:** W is 0.03 or more in size; it is at least 3 standard errors, using scatter pooled over the whole block; it has the same sign on each of the three days; and the wet-side fail held after the extra strokes. A negative W needs one extra dry-side run at 180 strokes per step that reproduces it.

**What it can detect.** At a scatter of 0.01, a true gap of 0.04 is caught about nine times in ten and 0.03 half the time. At 0.02, about 0.065 is needed.

**Part B, only if the blend's gap counts.** Three short days, four cups a day, 12 g of powder each, at the recipe in the middle of the window. DRY route: all the powder, oil in three equal portions, 120 strokes after each. WET route: all the oil, powder in three equal portions, 120 strokes after each. Same strokes, same number of additions, same clock time. Two controls each day: the wet route at 0.03 below the wet-side limit (must be a paste) and the dry route at 0.03 above the dry-side limit (must be crumbs). If either misbehaves, that day is reported and not counted. The route pictures predict paste by the dry route and crumbs by the wet route on three days of three. The alternative, that the gap came from stepping, predicts the same class by both.

**Wording if a gap is found.** "For powder P, by this protocol, the highest loading that passed was X when oil was added to powder and Y when powder was added to oil; same sign on three days of three. One operator, one lot. We have not shown why."

**Wording if not.** "The two limits agreed within plus or minus Z (90% interval); a window narrower than 0.03 is not excluded."

**Why it is not textbook.** A formulator would guess that kneading gets more fine powder in. Nobody can call whether coarse powder alone shows a gap, how wide it is, or whether one recipe made directly gives two classes. The two people who proposed the test predicted opposite signs.

## Experiment 2. Predict the blend from its parts

**Question.** Given the limit of each powder alone, how far can a blend be loaded?

| Picture | What it says | Formula |
|---|---|---|
| **No gain** | Hand-mixed fines act like lumps as big as the coarse grains. Each powder keeps its own oil demand and the demands add. No blend beats coarse alone | 1/L = (1 − x)/Lc + x/Lf |
| **Gap filling** | Fine grains sit in the gaps between coarse grains, less two crowding effects that depend on the size ratio | Published packing model ([source](https://ar5iv.labs.arxiv.org/html/1006.4215)), size ratio from the labels, 45/5.5 = 8.2 |

Lc and Lf are the means of the six C3 and C4 titrations of each powder. Neither formula is tuned to the result. Run `python3 outputs/thermal-paste-first-cycle/predict.py blend --lc <Lc> --lf <Lf>` and log its output.

*Placeholder* with Lc 0.55 and Lf 0.40:

| x | No gain | Gap filling |
|---|---|---|
| 0.15 | 0.521 | 0.600 |
| 0.30 | 0.494 | 0.622 |
| 0.50 | 0.463 | 0.537 |
| 0.70 | 0.436 | 0.472 |

At x = 0.30 that is 3.00 g of oil against 1.78 g on 12 g of powder, about eight times the guessed endpoint scatter.

**The one number.** G = (measured limit at x = 0.30 − no-gain value) / (gap-filling value − no-gain value). No gain says 0. Gap filling says 1.

- **G at 0.7 or above**, and the blend at least 0.03 above coarse alone: no gain rejected.
- **G at 0.3 or below:** gap filling at the label size ratio rejected.
- **Between:** both rejected as stated. The size ratio that would fit is reported as a description, labelled "fitted", not as a test passed.

**The band.** "45 micrometres, 325 mesh" is a sieve limit, not a measured size, so 8.2 is a declared assumption. A size ratio of 4 moves the gap-filling value at x = 0.30 from 0.622 to 0.581, and 2 moves it to 0.531 (`--ratio 4`). Log these with the prediction. A measured ratio from the certificates or a microscope is a second, separately named forecast.

**Runs.** The x = 0.30 dry-side runs are on the P days. x = 0.15, 0.50 and 0.70 are on the Q days, one of each per day. Coarse alone and fine alone are titrated again every day; if either has moved more than 0.015 from its input value, also report the prediction recomputed from that day's values and say which changed. The prediction logged first stays the registered one.

**Wording.** "With inputs measured on each powder alone in the same weeks, the 30% blend wet to L, which is G of the way from the no-gain line to the gap-filling prediction. The data are consistent with rule Y; that does not show Y's mechanism."

**Why it is not textbook.** The direction is textbook: a blend near 25 to 35% fines packs better than either powder and falls short of the ideal. The size of the gain is not. The formula was checked on dry spheres of 40 micrometres and up, and untreated hand-mixed fines may clump. A G near 0 or near 1 would be the surprise. If the models' logged intervals covered G, the experiment is counted as textbook.

## Experiment 3. Does it settle or hold?

**Question.** Left standing, does the coarse powder sink through the paste, and at what fines content does it stop?

| Picture | What it says |
|---|---|
| **Separate grains** | Every grain falls through the oil, slowed by its neighbours. Coarse grains fall through a "liquid" of fines plus oil. Everything settles, on a schedule that can be calculated |
| **Network** | Untreated fine grains stick to one another and above some concentration form a skeleton that carries weight. It holds the coarse grains only if it is strong enough for everything above the base, so a taller column needs more fines |

A third forecast is the formulator's: "a 40 vol% paste with fines shows little in a week".

**Stage 1, one half-day, on the first experiment day after C1 that the vials are in hand.** Needs the handling review's yes to filling vials. Narrow clear capped vials of one type (about 12 mm inside), filled gently within 10 minutes of mixing, stood against a ruler where the temperature is steady, and not moved.

- Coarse alone at loadings 0.20 (two vials from two separate batches), 0.30 and 0.40, columns 28 mm tall. Photos at 1, 2, 4, 8 and 24 hours. The top of the cloudy zone gives the settling speed and how fast it slows with loading.
- Fine alone at loadings 0.05, 0.10, 0.15, 0.20, 0.25 and 0.30, columns 28 mm; plus 10 mm columns of 0.05 and 0.15 from the same batches. Photos at 1 hour and 1, 3, 7, 10 and 14 days: height of clear oil, height of sediment, clear or cloudy.

**Desk step, day 10 to 14.** From the coarse vials, the separate-grains picture gives the time for each blend's top layer to lose its coarse grains. From the fine vials that settled into a sediment, the network picture gives a strength at each concentration (the weight the sediment carries at its base) and so the fines share at which a blend of a given height holds. Log both, with the models' forecasts, before any blend vial is made. If the dilute fine vials show no distinct sediment by day 14, the network picture has no number and that is reported.

*Placeholder:* separate grains says every blend loses 28 to 53% of its top-layer density in 7 days, the pilot recipe about half. One assumed point for the network gives a holding threshold at a fines share near 0.26 to 0.28 in a 28 mm column and 0.19 to 0.20 in a 10 mm one, with the pilot recipe holding in neither.

**Stage 2, one half-day.** Blends with coarse powder at 0.25 of the volume. The fines share is counted within the fines-plus-oil part (the pilot recipe is 0.167). Five levels of it, 0.05 apart, that bracket the predicted threshold, 28 mm columns. A second, separately made batch on another day for the two levels either side of it. The pilot recipe from two separate batches, each in a 10 mm and a 40 mm column. Photos at 1 hour and 1, 3 and 7 days. At day 7 draw the top third of each vial into a 3 mL needle-free syringe to a mark and weigh it, then probe the bottom.

**Definitions, fixed now.** Holds: top-third density within 10% of the starting value and under 1 mm of clear oil at 7 days. Settles: a drop of 25% or more. Between is "partial" and rejects neither picture.

**The one comparison.** Is there a level at which blends change from settles to holds, confirmed in both batches either side, and is it within one level of the network prediction?

**Stop rule, written now.** If stage 1 shows the fines do not stick (they settle at the single-grain rate into a dense cake), settling everywhere is the textbook answer. Stage 2 is then cut to the pilot-recipe vials and reported as textbook.

**Wording.** "Above a fines share of about X, top-layer density stayed within 10% for 7 days in n independent batches, where the calculation from single-powder vials predicted a fall of 25% or more; below X it fell. Vials of this width, one lot, one operator." Not supportable: "a network forms". Fines thickening the oil more than assumed would look the same.

**Why keep it.** It is the most predictable of the three in outline, and costs two half-days. It also answers an open point in the pilot: whether a sample changes during two weeks on the lab's shelf.

## Forecasts

Three moments. Each is logged and anchored before the first outcome it concerns.

1. **Desk test, before either powder is opened.** The open question only: the materials as labelled, the procedure, what will be measured. No pictures, no numbers from this page. This measures whether a model can already call the outcome.
2. **After commissioning.** The same questions plus a calibration card: the measured single-powder limits and their scatter, the dry packing, the plate results, the single-powder vial readings.
3. **During the work.** A forecast from table rows only (recipe, direction, route, outcomes so far) against a forecast from the full log. **The gap between these two is the only measured value of the trajectory over a table.**

**What is asked.** Experiment 1: both limits for each powder with 80% intervals, and the class by each route at a mid-window recipe. Experiment 2: the limit at x = 0, 0.15, 0.30, 0.50, 0.70 and 1 with intervals. Experiment 3: clear-oil height at 7 days for each fine vial, top-layer density change at 7 days for each blend and for the pilot recipe at both heights, and the fines share at which blends stop settling.

**Rules.** First reply only, never regenerate, memory and web search off, prompts saved. Forecasts are taken once per condition, not before each cup. Score every reply, never the best of several. Only forecasts logged before an experiment's first outcome count as cold; days 2 and 3 repeat a known answer and are scored as repeatability. The programme gives about eight to ten independent targets, so the result is reported as "k misses in N targets chosen because they looked hard", not as a statement about model ability.

## Rules for claims

- **Write it down first.** Question, the one readout, the one comparison, the threshold and the rule for excluding a reading are logged and anchored before the first run.
- **One cup or vial made separately is one piece of evidence.** Steps, photos and two vials from one batch are not repeats.
- **Three non-consecutive days, every arm on each day, order drawn beforehand.** Same sign on three days alone is a one-in-four coincidence.
- **A real difference** is at least 3 standard errors from this programme's own pooled scatter and at least the minimum size: 0.03 in loading, a class change read blind, or holds against settles.
- **Anything judged by eye** is read from coded photos by someone who does not know the arm. Report how often the reader and the bench call agreed.
- **A null is a bound,** "smaller than X", never "no effect".
- **Say what was changed and what was seen.** "The outcome depended on the route on this bench" is supportable. "Clumps broke" or "a network formed" is a claim about cause and needs its own test. A picture that survives is "not rejected", not confirmed.
- **Before each experiment** record what a formulator would say and what the models forecast. If either was right, say so and count it as textbook.
- **Nothing is dropped.** Failed cups and excluded readings stay in the log with the rule that excluded them. Any change to this page after the first counted run is a dated deviation.
- **A claim that passes** is confirmed by a fresh run on another day before it is repeated to anyone outside.

## Records

- Every titration cup and every mini-batch takes the next batch id on the one counter. Vials are `B041-V1`, `B041-V2`. Each titration step is an `observation` entry under its cup's id.
- Each condition's forecasts are `prediction` entries under a run id for the condition, for example `E2-X30`. At the start of each cup, log one `prediction` entry under the cup's id with `--data _forecast_run=E2-X30`, so the log shows which anchored forecast the cup is scored against.
- Three logs, started at set-up (checklist S6): `paste-commission`, `paste-limit` (the block and Part B) and `paste-settle`.
- Numbers come from one paper tally at the bench, because the tool checks ids only within one log. A bench day is a LAB day or an EXP day, never both (scheduled photos of sealed archives and vials excepted). All oil on EXP days is from the new lot.
- This page and `predict.py` are attached to the `paste-commission` log with the first forecasts (C0a). If either changes before C1, attach the new copy the same way and anchor again.
- Before the commissioning gate no condition run exists. The C3 and C4 cups carry `--data _forecast_run=E12-DESK`. The C1 practice and reference cups are scored against nothing: they carry `--data _forecast_run=none --data _excluded="C1 practice, not counted"`. The C1 warm-up batch goes in `paste-commission` and takes its own model forecast first, as in step 1 of "Make one batch".
- Every session note carries room temperature, humidity and the minutes each pail was open. Powders are drawn each day from small sealed working tubs so the stock pails open once a day.

## What to buy

All prices are estimates except the oil.

| Item | For | About |
|---|---|---|
| Three bottles of the same oil, one purchase, one lot | Everything on this page (EXP). The bottle already bought is LAB: the practice batch, A, B and any redo only | $60 |
| 100 mL stoppered graduated cylinder, powder funnel, rubber pad | C2 | $30 |
| About 30 clear capped vials near 12 mm inside, three 3 mL needle-free syringes | Experiment 3 | $25 |
| About 70 more lidded 60 mL cups, a few small lidded tubs | One cup per titration; working tubs | $20 |
| Two 4 inch glass plates and a 500 g weight, if not already bought | C0b | $40 |
| Fine-tip disposable pipettes for oil, a ruler or printed millimetre grid, a room thermometer with humidity, if not already owned | Small oil steps and the rig-check dose; the scale in photos; session notes | $20 |
| Optional: USB microscope | Sizing the coarse powder for Experiment 2 | $30 |

Counted oil is about 231 g of the 343 g in three bottles. Powder is about 1.3 kg of the 4.5 kg on hand. No lab fee.

## Needs a second person

Coding cups and vials, drawing run orders and shelf positions, and reading every photo blind. Without that, each class in Experiment 1 is a judgement by someone who knows the prediction, and is reported as such.

## Left out, and why

- **Fines first against coarse first.** Its own proposer predicted no difference.
- **Spread diameter as a score.** A 5% change in diameter is a 28% change in the stress at which the paste yields; too blunt.
- **Trapped air from density.** The small measure reads to 1 to 3% per fill; a crumbly paste cannot be filled without gaps.
- **Detour to a stiff paste and back; one master curve.** Predictions were borrowed from other materials or did not follow from their sources.
- **Kept for later, if a gap is found:** powder in, oil back, powder in again in one cup, with a strokes-only control; and switching one recipe between crumb and paste.
- **Water and humidity.** No new ingredient is used anywhere here.

## Risks

- All three could come back textbook or null. Each would be a stated bound worth recording, and the project would then say that on this bench a recipe row carries these labels.
- Every threshold assumes a scatter of 0.01 that nobody has measured. At 0.02 the plan needs more days or coarser claims.
- The endpoint is judged by a beginner who is learning during the first 30 or so runs. Blind reading covers the class, not the bench decisions about when to switch steps or stop.
- It is heavy work, and the first estimate was too low. By this page's own step rules a coarse cup takes about 30 steps (1,800 strokes) and a fine cup about 40 (2,400), not 1,100 strokes. Five or six cups a day is unproven: time one weigh-and-record cycle in the next practice batch and count the steps in the C1 practice cups, then set the number of cups per day (corrected 9 October). If a block day runs past six hours, drop x = 0.70, where the two rules are too close to separate.
- The coarse powder's size is a sieve limit, so Experiment 2 can tell "ratio 2 or less" from "4 or more" and little finer.
- One operator, one lot of each ingredient, one room.
- The endpoint's "closes over a cut within 10 seconds" clause has never been tried on a known paste, and the first practice batch held its ridges at loading 0.40. It is checked on the next practice batch before C1; see [the B001 review, section 6.2](B001_PROCESS_REVIEW.md#62-where-this-review-differs-from-sections-1-to-5).
- No thermal data comes out of this, and nothing new goes to the lab.
- Sources: four were opened and checked when the programme was assembled (the packing formula, a second coefficient set, the settling exponents, the network load balance). The rest were opened by reviewers and not re-checked.
