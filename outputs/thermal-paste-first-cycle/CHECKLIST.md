# Thermal paste: what to do next

Updated Friday 9 October 2026. **Current priority: finish the paste-to-lab comparison using existing ingredients.** The complete recipe and procedure are in [PASTE_TO_LAB_RUN_CARD.md](PASTE_TO_LAB_RUN_CARD.md), method PASTE-P2-v1. It supersedes the B001 preparation instructions below for new batches.

- **LAB, active:** hand LongWin the bought reference paste and two independently made batches (A and B) of one recipe. The next batch can also be the first exploratory lab specimen under the run card's predeclared process criteria; an extra disposable practice batch is not mandatory.
- **EXP, deferred for this milestone:** [EXPERIMENTS.md](EXPERIMENTS.md), cured silicone composites and home rig construction. Their tasks below remain future plans, not current purchases or prerequisites.

Long versions: [BENCH_PROTOCOL.md](BENCH_PROTOCOL.md) (section 1) and [CALLS_AND_ORDERS.md](CALLS_AND_ORDERS.md). Those files call G1 "item 15", S5 "item 16" and S2 "item 05". Run every command from the top folder of the repository.

## Where things stand

- **First learning-only practice batch:** B001 preparation and final weighing are complete per operator reports. Its [raw record and four original photographs](../../trajectory/releases/B001/README.md) are public with authorization. The [process review](B001_PROCESS_REVIEW.md) and [next run card](PASTE_TO_LAB_RUN_CARD.md) are written. The chosen next arrangement is cup-only additions with a separately preweighed spatula/rest. Dry rehearsal, numerical balance checks and the actual handling setup remain unconfirmed. The written method is prospective, not an executed or validated procedure.
- **Materials received, per operator:** coarse alumina, fine alumina, reference paste and silicone oil. Product identities and labels reported checked; full lot-certificate reconciliation remains open.
- **Balance received:** Bonvoisin-branded, reported 500 g capacity and 0.001 g readability. Manual calibration with the supplied 200 g weight is reported complete. See S5-P for the practice-only cover-off exception; small-mass accuracy is unverified.
- **LongWin:** wants its service form before quoting. Expect about two weeks from drop-off to a report. No appointment yet.
- **Do not buy:** more powder, another balance, or anything for the thermal rig.

## Preparation requirements

For the active lab comparison, complete G2, the applicable G1b handling review, S5 numerical balance checks and the dry rehearsal in B1. S5-P is still only a learning-practice exception. N3 records earlier forecasts; it does not supply a blind forecast of a changed method. Save any new forecast being evaluated before its outcome, explicitly stating that B001 is known. The later rig check (N2) has separate requirements.

- [ ] **G2. Send the LongWin form.** Fill it in from [the form guide](CALLS_AND_ORDERS.md#longwin-service-form-next-action). Call the samples "batch A" and "batch B"; ids follow. For thickness, pressure and temperature write "engineer to recommend". Ask for: price, which container to use, the earliest drop-off date, the measured data points as Excel, permission to publish naming the lab, and the price of an optional fourth sample. Also ask: is there a maximum sample age, and must the paste be fresh or stirred before loading; is the gap or the pressure set during the test; can they report the thickness reached at a stated pressure; what is their documented repeatability on greases.
- [ ] **G1. Start the handling review, one request for both tracks.** Read the safety data sheets for both powders, the oil and the reference paste. Pick a wipe-clean spot away from food, children and pets with no fan blowing across it. A balance draft shield is not dust control. If unsure, ask an industrial hygienist. Ticking this box means the review is started. It opens nothing.
  - [ ] **G1a, wet work (oil and reference paste).** Gloves, glasses, tray, both waste tubs, the reference-only tool. Phone the waste service about the zinc-oxide reference paste and write down how they take it. Then write down, with the date, whether this is enough to open the oil and the reference paste for the rig check (N2), or whether they wait for G1b. Tick only when the note says yes.
  - **G1b, powder.** Both powders stay sealed until this is settled for the step you are about to do. Settled means a written, dated yes to that step by name: a reviewer's if you use one, otherwise your own decision from the data sheets. Write down which, and which respirator. A no, or no answer yet, means the step is not done. Give the reviewer the real amounts: about 1.3 kg of powder over about 14 bench days, up to six hours a day, against about 55 g for the three batches here. Tick each line when it has its yes and the equipment is in hand:
    - [ ] the batch steps on this page (needed for B1, A and B);
    - [ ] many small powder additions to one cup; daily working tubs; oil added to dry powder and stirred; a dry blend tumbled in a lidded cup (needed for C1);
    - [ ] pouring powder through a funnel and tapping a cylinder (C2 only; if no, skip C2);
    - [ ] filling vials (settling stage 1).
- [ ] **N1, deferred EXP purchases.** Three more oil bottles and the expanded [experiment kit](EXPERIMENTS.md#what-to-buy) wait. For the active lab comparison, fill only missing items in the new run card, including borrowed or purchased documented-tolerance check weights. The existing oil and powders are sufficient for the two planned 25.01 g batches, subject to the actual remaining amount.
- [ ] **N4, optional/deferred.** A second person can code cups and read photos blind for a later study. This is not needed to prepare the current pair; record the current observations as unblinded.
- [ ] **S6. Set up the record.** Turn off location tagging on your phone camera. Print the new run card and two [batch sheets](../../trajectory/batch-sheet.md). Keep the first oil bottle labeled LAB. Continue the existing paper batch-number tally; never reuse B001 or another assigned number. Reuse the registry and paste-pilot logs for the current pair, preserving the existing practice log. The initialization examples below are only for logs that do not yet exist; the expanded EXP logs can wait. Commands are documented in [trajectory/README.md](../../trajectory/README.md):

```sh
python3 trajectory/traj.py init registry --text "materials, equipment, method versions"
python3 trajectory/traj.py init paste-practice --text "practice batches"
python3 trajectory/traj.py init paste-pilot --text "batches A and B for the first lab submission"
python3 trajectory/traj.py init paste-commission --text "rig check, first forecasts, commissioning days"
python3 trajectory/traj.py init paste-limit --text "mixing-limit titrations, experiments 1 and 2"
python3 trajectory/traj.py init paste-settle --text "settling vials, experiment 3"
mkdir -p trajectory/campaigns/registry/docs trajectory/campaigns/paste-commission/prompts
```

## When parcels land: still sealed

- [ ] **S1.** Collect the oil and the parcels. Photograph every label and lot number before opening anything. Mark the oil bottle **LAB** and put it in its box.
- [ ] **S2.** Read both powder certificates in full. The coarse one says 99.40% against 99.5% on the listing; write that down.
- [x] **N3. First forecasts saved, 8 October.** GPT-6.1-sol and GPT-6-astra each returned a first response to both desk prompts in separate fresh contexts. Original responses, exact sent prompts and the experiment-page/formula snapshots are preserved in the private commission log; its hash is pushed in commit `8f156b8`. A separate first forecast for practice B001 is also preserved. Unknown certificate, size-distribution and surface-treatment details were explicitly stated as unknown, a documented departure from the original completed-certificate prerequisite. Model requests are recorded; resolved deployment versions and a separate memory setting are not exposed by the interface. An [OpenTimestamps receipt](../../trajectory/timestamps/first-forecasts-8f156b8.anchors.log.ots) has been saved for the [immutable anchor snapshot](../../trajectory/timestamps/first-forecasts-8f156b8.anchors.log); it contains pending calendar attestations, not yet a verified Bitcoin timestamp. No batch preparation outcome had been reported when these forecasts were recorded. This completes forecast collection, not the handling or balance checks.
- [ ] **N5. When the three new oil bottles arrive.** Photograph each label and lot. Mark all three **EXP** and keep them apart from the LAB box. Record the lot in the registry as `LOT-OIL-2`. If they do not share one lot, stop: give each lot its own id and write down which lot is used for which experiment before any is opened.

## When the balance arrives

- [ ] **S3.** Gather the kit:
  - two matching lidded mixing vessels chosen by dry rehearsal, one rigid tool rest and the lab's accepted submission containers; use existing suitable items;
  - two powder scoops, one per powder, never swapped;
  - one mixing spatula, and one tool used only for the reference paste;
  - check weights near 2 g, 5 g and 20 g with a stated tolerance (the single weight that ships with a balance is not enough);
  - the protective equipment from G1, and alcohol for wipes;
  - labels, marker, wipes, a rimmed tray, a timer;
  - two waste tubs, labelled "reference paste" and "everything else".
- [ ] **S4.** Wash the cups and tools and dry them completely.
- [ ] **S5. Check the balance. Required for A/B and the expanded experiments; see the learning-only practice exception below.** Warm it up, level it and calibrate it as its manual says. Place and remove each check weight five times and write down all five readings. Then put the empty cup on the pan, tare, and repeat the 2 g check inside the cup. **Pass:** each reading's error plus the weight's stated tolerance is 0.010 g or less, and the five readings span 0.010 g or less. **Fail:** check draughts, the surface, level and warm-up, then repeat.
- [ ] **S5-P. Learning-only practice exception, agreed 8 October.** A practice batch may use manual calibration with the supplied 200 g weight while small-mass accuracy remains unverified. Record five repeated readings and empty-pan zero returns in the intended cover configuration; the provisional screen is a range of 0.010 g or less and zero returns within +/-0.010 g. A report of completing the steps without the numbers is not a numerical pass. If the removable clear cover causes inconsistent readings, a stable cover-off configuration may be used consistently for practice; document the reason and do not disable ventilation required for powder handling. Label the record "PRACTICE—accuracy of small additions not yet verified." This does not complete S5 or authorize A/B or expanded experiments. G1b, N3 and separate dry powder tools still apply. Source observations and completion reports belong in the local registry and practice logs.
- [ ] **N2. Rig check on plain oil, then the reference paste** ([steps](EXPERIMENTS.md#c0-desk-forecasts-and-rig-check)). Needs S5 passed, the plates and weight, the new oil (N5), and G1a ticked. If you wrote under G1a that they wait, N2 waits for G1b. It is an EXP day: never on a day with a practice batch, A, B or packing, and never between A and B. Any day before the commissioning gate; it does not hold up anything else.

## Before the next paste batch

A LAB day using [PASTE-P2-v1](PASTE_TO_LAB_RUN_CARD.md). An intended comparison batch needs S5 passed, the first G1b line completed, separate dry powder scoops, a successful dry rehearsal and the lab's preparation/packaging instructions. Density and plate-spread measurements are not planned. Complete any forecast prompt with the actual method and materials; preserve it before the relevant outcome.

- [ ] **B1. Dry rehearsal and prospective method.** Rehearse cup-only weighing, the spatula/rest arrangement and tool reach without powder. Select the vessel/tool configuration and save PASTE-P2-v1 with those details before the intended pair. Read the entire card first. B002, if that ID is free, can be both method confirmation and the first exploratory specimen when the predeclared process criteria are met. A stiff or poorly performing paste is not excluded for that reason. Preserve any deviations and revise the method before another run if needed. Never overwrite B001 or relabel it as A/B.

**B001 storage and recommended next rehearsal after its first observations:**

- Keep B001 as a practice archive: capped, upright, in labeled secondary containment, at stable indoor room temperature away from food, sunlight and heaters. Do not refrigerate, heat, dilute or remix it for storage. Record the actual storage start and temperature if measured. The oil maker specifies cool, dry, ventilated storage in its [SDS, section 7](https://www.super-lube.com/wp-content/uploads/2025/06/SDS_Super_Lube_Silicone_Oil-EN-sds.pdf); this supports a provisional short-term storage choice, not a validated shelf life for the homemade paste.
- On the following day, photograph the closed jar from the side before disturbing it and note any visible separated layer. Record when the observation occurs; changes in aged B001 are not a fresh-batch repeat. Do not call this an automatic timed settling test.
- **Review interpretation:** the residue calculations in [section 6](B001_PROCESS_REVIEW.md#6-second-independent-review-9-october) are sensitivity scenarios. They do not establish how much early material was stranded or that residue had no effect on B001. Message-entry intervals also do not establish active mixing or rest durations.
- **Next action is dry rehearsal.** The selected revision uses a cup-only ingredient tare and a separately preweighed rigid rest plus spatula, as specified in the new card. Do not mix this with the earlier candidate of weighing the spatula inside the cup. Check stable placement, tool reach, no external contacts and numerical repeat/zero readings.
- After readiness and laboratory preparation requirements are complete, make fresh B002 under the new card, then a fresh independent repeat if its method remains unchanged. Retain the intended recipe; do not thin B001 or change new ingredient targets solely because B001 felt stiff. Do not infer residue composition or add compensating ingredients from a total-mass difference.
- B001 remains a practice archive. It may be quoted/tested as an **additional exploratory specimen** if accepted, with its original preparation, age and balance limitations disclosed; it is not part of the new matched pair.

Then one question: **has LongWin named the container, any age limit and a date?**

- **Yes, and readiness checks complete:** B2 and B3 are the next preparation sessions, then pack (P1 to P5).
- **No:** complete dry checks, the service form and records while waiting. No additional material system or expanded powder campaign is required to keep this milestone moving.

**When the expanded experiments are resumed**, their separate prerequisites in [C1](EXPERIMENTS.md#order-of-work) still apply. Completing this new run card does not silently approve that larger handling scope.

## Make one batch

**Historical B001 baseline only. For the next batch use [PASTE_TO_LAB_RUN_CARD.md](PASTE_TO_LAB_RUN_CARD.md).** The revised card accounts for the tool/rest residue and supersedes the blade-cleaning instruction below. B1 remains open until dry rehearsal and method details are recorded.

Original planning estimate: 30 to 45 minutes, not validated by B001. Record actual hands-on time separately from logging.

| Ingredient | Total | How it goes in |
|---|---|---|
| Silicone oil | 6.71 g | All at the start |
| Coarse alumina | 12.81 g | 4.27 g in each of three rounds |
| Fine alumina | 5.49 g | 1.83 g in each of three rounds |

1. Take the next number on the tally and label the cup with it. Fill in the top of a batch sheet. Get one AI model's forecast for this batch and log it before you start (prompt and rules in the preamble; note the model's name and version).
2. Protective equipment on. Work on the tray.
3. Put the empty cup on the balance, no lid, no tool. Write down its mass. Tare. Add **6.71 g** of oil slowly, straight from the bottle or with a clean dropper used only for oil. Write down the actual reading.
4. Tare again. With the coarse scoop, held low over the cup, add **4.27 g** coarse powder. Write the actual reading. Close the pail.
5. Tare again. With the fine scoop, add **1.83 g** fine powder. Write the actual reading. Close the pail.
6. Take the cup off the balance. Fold and scrape for **60 seconds**: bottom, walls, back to the centre. Scrape the spatula clean into the cup and rest it on its own spot.
7. Put the cup back on the balance without the spatula, let the reading settle, then repeat steps 4 to 6. Do this twice.
8. Mix for **3 more minutes** the same way. Scrape the spatula into the cup. Put the lid on and rest it **2 minutes**.
9. Open it, lift the spatula once from the centre, photograph the paste with its id, and write down what you see: does it level, hold a peak, feel stiff, or still show dry powder?
10. Close and store upright. Finish the batch sheet, photograph it, and type it into the log the same day. Wipe the spatula clean with alcohol on a wipe, not in the sink. Put the wipes in the waste tub and let the spatula dry fully before the next batch.

**Rules while mixing**

- Aim to land within 0.02 g of each target. If you overshoot, write the real number and carry on. Do not take any back out.
- Never weigh with the spatula in the cup.
- Spilled something? Stop and write it down. Do not sweep it back in.
- Never put a used tool into the powder pails or the oil bottle.
- Damp-wipe any stray powder. No sweeping, no blowing, no household vacuum. Nothing down the drain.
- A batch that goes wrong keeps its id and its record. Start again under the next id.

## Rules for running two tracks

1. Nothing is opened before its gate. Oil and reference paste: G1a ticked, or G1b settled. Powder: its G1b line ticked, and S5 passed; S5-P is an alternative only for learning-only practice. N3 remains required before any powder work.
2. Forecasts before powder (N3).
3. The practice batch is the first powder work for both tracks.
4. One track per bench day. Before anything is opened, write the date and LAB or EXP on the tally and at the top of every sheet used that day. Never both. Photographing a sealed archive or vial on its schedule is not bench work; do it on any day.
5. One oil per track. The first bottle is LAB: practice, A, B and any redo. The three new bottles are EXP. Only that day's oil is on the tray; the other stays shut in its box.
6. One number list. Every new cup takes the next number on the tally, whichever track it is. A and B take whatever numbers are next on the days they are made.
7. The lab goes first. When LongWin names the container and a date, A and B are the next two bench days; an experiment day gives way, but a day already started is not cut short. Pilot paste never goes into an experiment, and nothing learnt in the experiments changes the written pilot method.

## Batches for the lab

Make once LongWin has named the container, conditioning/age instructions and drop-off date, with containers and readiness checks complete. Prefer consecutive preparation sessions/days using LAB oil, scheduling within its age instructions. Record different sample ages. If no appointment is available yet, finish desk/dry preparation rather than automatically starting the deferred experiments.

- [ ] **B2. Batch A.** Follow PASTE-P2-v1 from fresh ingredients, tentatively B002. It may also confirm the method under the predeclared criteria. Record deviations before deciding whether a new method is needed; poor appearance/performance alone does not disqualify it.
- [ ] **B3. Batch B.** Fresh ingredients again, tentatively B003, using the same actual method and observations. Never split A to make B. If the method changes, report that fact and do not claim an exact repeat pair.

## Pack and hand over

- [ ] **P1.** Use the container LongWin names. For A, then B: weigh the empty container with its lid; spoon in about **5 g** (LongWin needs about 1 mL, roughly 2.2 g); close it and weigh it again; write down both numbers. Label it with its batch id plus **-L1**. Wipe the spatula clean and dry between A and B.
- [ ] **P2.** Keep the rest of each batch sealed as an archive, labelled batch id plus **-A1**. Photograph each archive from the side at 1 hour and at 1, 3, 7 and 14 days, to record any oil separating.
- [ ] **P3.** Reference paste: photograph its label and lot. Add nothing to it. Move about 5 g into its own container with the reference-only tool. Label it **REF-L1**.
- [ ] **P4.** Optional fourth sample, only if LongWin quoted it: a second container from A. Then label all three home-made containers with plain codes (X1, X2, X3) and keep the key to batch ids in your own record.
- [ ] **P5.** Before the samples leave: log an AI forecast of the lab's numbers for each container. Run `python3 trajectory/traj.py verify paste-pilot`, then the same with `anchor`. Commit and push `trajectory/anchors.log`, timestamp that file with an outside service such as opentimestamps.org, and copy `trajectory/campaigns/` to a second disk.
- [ ] **P6.** Tell LongWin what is ready and agree the drop-off.
- [ ] **P7.** Deliver with the safety data sheets, a list of what each container holds, and each batch's age. Get a receipt and a result date.
- [ ] **A1.** Save LongWin's files unchanged. Compare A with B **and both with the measured DOWSIL reference**, using actual thickness/pressure/temperature, reloads and uncertainty as specified in the new card. Report all submitted outcomes, including loading failures and deviations. Keep any B001 result separate from the new pair.

Not on this page: density and spread on batches, more recipes, backup labs. Leave those parts of the batch sheet marked "not measured".
