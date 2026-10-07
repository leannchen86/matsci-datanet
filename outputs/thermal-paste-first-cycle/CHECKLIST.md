# Thermal paste: what to do next

Updated Wednesday 7 October 2026. Two tracks run side by side:

- **LAB:** hand LongWin three samples: the bought reference paste, and two batches (A and B) of one home-mixed recipe, made separately. All of it is on this page.
- **EXP:** the experiments in [EXPERIMENTS.md](EXPERIMENTS.md). They do not wait for the lab.

Long versions: [BENCH_PROTOCOL.md](BENCH_PROTOCOL.md) (section 1) and [CALLS_AND_ORDERS.md](CALLS_AND_ORDERS.md). Those files call G1 "item 15", S5 "item 16" and S2 "item 05". Run every command from the top folder of the repository.

## Where things stand

- **Arriving Wednesday 7 October:** coarse alumina, fine alumina and the reference paste (McMaster, by 5 pm); silicone oil (Grainger San Jose, 2261 Ringwood Ave, open 7:30 am to 4 pm; go only after the ready notice).
- **Balance:** ordered, arrival date not confirmed. Check your order for its model, capacity and date.
- **LongWin:** wants its service form before quoting. Expect about two weeks from drop-off to a report. No appointment yet.
- **Do not buy:** more powder, another balance, or anything for the thermal rig.

## Today: nothing is opened

Not today, whatever arrives: opening either powder, or the rig check (N2).

- [ ] **G2. Send the LongWin form.** Fill it in from [the form guide](CALLS_AND_ORDERS.md#longwin-service-form-next-action). Call the samples "batch A" and "batch B"; ids follow. For thickness, pressure and temperature write "engineer to recommend". Ask for: price, which container to use, the earliest drop-off date, the measured data points as Excel, permission to publish naming the lab, and the price of an optional fourth sample. Also ask: is there a maximum sample age, and must the paste be fresh or stirred before loading; is the gap or the pressure set during the test; can they report the thickness reached at a stated pressure; what is their documented repeatability on greases.
- [ ] **G1. Start the handling review, one request for both tracks.** Read the safety data sheets for both powders, the oil and the reference paste. Pick a wipe-clean spot away from food, children and pets with no fan blowing across it. A balance draft shield is not dust control. If unsure, ask an industrial hygienist. Ticking this box means the review is started. It opens nothing.
  - [ ] **G1a, wet work (oil and reference paste).** Gloves, glasses, tray, both waste tubs, the reference-only tool. Phone the waste service about the zinc-oxide reference paste and write down how they take it. Then write down, with the date, whether this is enough to open the oil and the reference paste for the rig check (N2), or whether they wait for G1b. Tick only when the note says yes.
  - **G1b, powder.** Both powders stay sealed until this is settled for the step you are about to do. Settled means a written, dated yes to that step by name: a reviewer's if you use one, otherwise your own decision from the data sheets. Write down which, and which respirator. A no, or no answer yet, means the step is not done. Give the reviewer the real amounts: about 1.3 kg of powder over about 14 bench days, up to six hours a day, against about 55 g for the three batches here. Tick each line when it has its yes and the equipment is in hand:
    - [ ] the batch steps on this page (needed for B1, A and B);
    - [ ] many small powder additions to one cup; daily working tubs; oil added to dry powder and stirred; a dry blend tumbled in a lidded cup (needed for C1);
    - [ ] pouring powder through a funnel and tapping a cylinder (C2 only; if no, skip C2);
    - [ ] filling vials (settling stage 1).
- [ ] **N1. Order** three more bottles of the same oil in one purchase, asking for one lot; anything in the S3 kit you do not own, check weights first; and the small items in [What to buy](EXPERIMENTS.md#what-to-buy).
- [ ] **N4. Ask a second person** whether they can code cups and read photos blind. If nobody can, write down "unblinded".
- [ ] **S6. Set up the record.** Turn off location tagging on your phone camera. Print four [batch sheets](../../trajectory/batch-sheet.md). Mark a lidded box LAB for the first oil bottle. Start a paper tally for batch numbers: one line per cup, written B001, B002 and so on, with the date, LAB or EXP, and the log it goes in. B001 is the first practice batch; a number is never reused. Start six logs; all other commands are in [trajectory/README.md](../../trajectory/README.md):

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
- [ ] **N3. Take the first forecasts. This must be finished before either powder is opened for anything.** Decide two or three models. Follow [desk-test-prompts.md](../../trajectory/desk-test-prompts.md): fill its brackets from the labels and certificates, send its two prompts on their own, log the replies, attach the experiment page, then anchor, push and timestamp.
- [ ] **N5. When the three new oil bottles arrive.** Photograph each label and lot. Mark all three **EXP** and keep them apart from the LAB box. Record the lot in the registry as `LOT-OIL-2`. If they do not share one lot, stop: give each lot its own id and write down which lot is used for which experiment before any is opened.

## When the balance arrives

- [ ] **S3.** Gather the kit:
  - about ten lidded 60 mL plastic cups;
  - two powder scoops, one per powder, never swapped;
  - one mixing spatula, and one tool used only for the reference paste;
  - check weights near 2 g, 5 g and 20 g with a stated tolerance (the single weight that ships with a balance is not enough);
  - the protective equipment from G1, and alcohol for wipes;
  - labels, marker, wipes, a rimmed tray, a timer;
  - two waste tubs, labelled "reference paste" and "everything else".
- [ ] **S4.** Wash the cups and tools and dry them completely.
- [ ] **S5. Check the balance. It must pass before any batch.** Warm it up, level it and calibrate it as its manual says. Place and remove each check weight five times and write down all five readings. Then put the empty cup on the pan, tare, and repeat the 2 g check inside the cup. **Pass:** each reading's error plus the weight's stated tolerance is 0.010 g or less, and the five readings span 0.010 g or less. **Fail:** check draughts, the surface, level and warm-up, then repeat.
- [ ] **N2. Rig check on plain oil, then the reference paste** ([steps](EXPERIMENTS.md#c0-desk-forecasts-and-rig-check)). Needs S5 passed, the plates and weight, the new oil (N5), and G1a ticked. If you wrote under G1a that they wait, N2 waits for G1b. It is an EXP day: never on a day with a practice batch, A, B or packing, and never between A and B. Any day before the commissioning gate; it does not hold up anything else.

## First powder day: the practice batch

A LAB day. Needs S5 passed, the first G1b line ticked, and N3 done. It does not need the lab, the new oil or any experiment kit. Before you start, fill the oil, powder and balance brackets in [prompt-preamble.md](../../trajectory/prompt-preamble.md), write "not measured" in its density-measure and plate-load brackets, and save it as version 1.

- [ ] **B1. Practice.** Make one batch as below. If you could weigh, wet all the powder and keep to the times, write down the method exactly as you did it and save it in the registry as `docs/BP-v1.md`. If not, practise again under the next number.

Then one question: **has LongWin named the container, any age limit and a date?**

- **Yes:** B2 and B3 are your next two bench days, then pack (P1 to P5). The experiments follow.
- **No:** the experiments are next. Come back to B2 and B3 the day the lab answers.

**The experiments start at [C1](EXPERIMENTS.md#order-of-work)**, on any later bench day that begins with all five of these true: S5 passed; the second G1b line ticked; N5 done; N3 was finished before any powder was opened; B1 passed and the method is written. Never on the practice-batch day itself. C1 does not wait for the drop-off or the report.

## Make one batch

About 30 to 45 minutes.

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

1. Nothing is opened before its gate. Oil and reference paste: G1a ticked, or G1b settled. Powder: its G1b line ticked, and S5 passed.
2. Forecasts before powder (N3).
3. The practice batch is the first powder work for both tracks.
4. One track per bench day. Before anything is opened, write the date and LAB or EXP on the tally and at the top of every sheet used that day. Never both. Photographing a sealed archive or vial on its schedule is not bench work; do it on any day.
5. One oil per track. The first bottle is LAB: practice, A, B and any redo. The three new bottles are EXP. Only that day's oil is on the tray; the other stays shut in its box.
6. One number list. Every new cup takes the next number on the tally, whichever track it is. A and B take whatever numbers are next on the days they are made.
7. The lab goes first. When LongWin names the container and a date, A and B are the next two bench days; an experiment day gives way, but a day already started is not cut short. Pilot paste never goes into an experiment, and nothing learnt in the experiments changes the written pilot method.

## Batches for the lab

Made once LongWin has named the container, any age limit and a drop-off date, and the containers are in hand. Two bench days in a row, LAB oil, no experiment day between. Normally these are your next two bench days. One exception: if the drop-off is so far off that batch A would be older than the lab's age limit, or the lab asked for fresh paste, carry on with the experiments and make A three bench days before the drop-off and B the next day.

- [ ] **B2. Batch A.** Re-read the written method. Fresh ingredients.
- [ ] **B3. Batch B.** Fresh ingredients again, the next day. Never split A to make B.

## Pack and hand over

- [ ] **P1.** Use the container LongWin names. For A, then B: weigh the empty container with its lid; spoon in about **5 g** (LongWin needs about 1 mL, roughly 2.2 g); close it and weigh it again; write down both numbers. Label it with its batch id plus **-L1**. Wipe the spatula clean and dry between A and B.
- [ ] **P2.** Keep the rest of each batch sealed as an archive, labelled batch id plus **-A1**. Photograph each archive from the side at 1 hour and at 1, 3, 7 and 14 days, to record any oil separating.
- [ ] **P3.** Reference paste: photograph its label and lot. Add nothing to it. Move about 5 g into its own container with the reference-only tool. Label it **REF-L1**.
- [ ] **P4.** Optional fourth sample, only if LongWin quoted it: a second container from A. Then label all three home-made containers with plain codes (X1, X2, X3) and keep the key to batch ids in your own record.
- [ ] **P5.** Before the samples leave: log an AI forecast of the lab's numbers for each container. Run `python3 trajectory/traj.py verify paste-pilot`, then the same with `anchor`. Commit and push `trajectory/anchors.log`, timestamp that file with an outside service such as opentimestamps.org, and copy `trajectory/campaigns/` to a second disk.
- [ ] **P6.** Tell LongWin what is ready and agree the drop-off.
- [ ] **P7.** Deliver with the safety data sheets, a list of what each container holds, and each batch's age. Get a receipt and a result date.
- [ ] **A1.** When the report comes: save LongWin's files unchanged. Compare A with B only (not the warm-up batch from C1) and write down what you decide next.

Not on this page: density and spread on batches, more recipes, backup labs. Leave those parts of the batch sheet marked "not measured".
