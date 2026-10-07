# Thermal paste: what to do next

Updated Wednesday 7 October 2026. This page is the whole plan for the pilot. What comes after it is in [EXPERIMENTS.md](EXPERIMENTS.md). The long versions are in [BENCH_PROTOCOL.md](BENCH_PROTOCOL.md) (section 1) and [CALLS_AND_ORDERS.md](CALLS_AND_ORDERS.md). Those files call G1 "item 15", S5 "item 16" and S2 "item 05".

**Goal:** hand LongWin three samples: the bought reference paste, and two batches (A and B) of one home-mixed recipe, made separately.

## Where things stand

- **Arriving Wednesday 7 October:** coarse alumina, fine alumina and the reference paste (McMaster, by 5 pm); silicone oil (Grainger San Jose, 2261 Ringwood Ave, open 7:30 am to 4 pm; go only after the ready notice).
- **Balance:** ordered, arrival date not confirmed. Check your order for its model, capacity and date.
- **LongWin:** wants its service form before quoting. Expect about two weeks from drop-off to a report. No appointment yet.
- **Do not buy:** more powder, another balance, or anything for the thermal rig.
- **Do buy now:** three more bottles of the same oil in one purchase, and check they share a lot. The bottle on order covers the pilot only (about 17 batches).

## Start here, in this order

- [ ] **G2. Send the LongWin form.** Fill it in from [the form guide](CALLS_AND_ORDERS.md#longwin-service-form-next-action). For thickness, pressure and temperature write "engineer to recommend". Ask for: price, which container to use, a drop-off date, the measured data points as Excel, permission to publish naming the lab, and the price of an optional fourth sample. Also ask: is the gap or the pressure set during the test; is the paste stirred before loading; can they report the thickness reached at a stated pressure; what is their documented repeatability on greases.
- [ ] **G1. Settle powder handling.** Do not open either powder until this is done. Settled means: you have read the safety data sheets for both powders, the oil and the reference paste; you have a wipe-clean spot away from food, children and pets with no fan blowing across it; and you have safety glasses, gloves and whatever respirator the sheets or a reviewer call for. A balance draft shield is not dust control. If unsure, ask an industrial hygienist. Ask the same review to cover three later steps: filling and tapping a cylinder of dry powder, many small powder additions to one cup, and decanting each day's powder into small working tubs.
- [ ] Then S1 to S6 as things arrive.

## Set up (no powder needed)

- [ ] **S1.** Collect the oil and the parcels. Photograph every label and lot number before opening anything.
- [ ] **S2.** Read both powder certificates in full. The coarse one says 99.40% against 99.5% on the listing; write that down.
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
- [ ] **S6. Set up the record.** Turn off location tagging on your phone camera. Print four [batch sheets](../../trajectory/batch-sheet.md). Fill in the brackets in [prompt-preamble.md](../../trajectory/prompt-preamble.md). Start three logs; all other commands are in [trajectory/README.md](../../trajectory/README.md):

```sh
python3 trajectory/traj.py init registry --text "materials, equipment, method versions"
python3 trajectory/traj.py init paste-practice --text "practice batches"
python3 trajectory/traj.py init paste-pilot --text "batches A and B for the first lab submission"
```

Batch ids run in order and are never reused: **B001** is the first practice batch. A and B take the next two unused numbers (B002 and B003 if nothing is redone).

## Make one batch

About 30 to 45 minutes.

| Ingredient | Total | How it goes in |
|---|---|---|
| Silicone oil | 6.71 g | All at the start |
| Coarse alumina | 12.81 g | 4.27 g in each of three rounds |
| Fine alumina | 5.49 g | 1.83 g in each of three rounds |

1. Label the cup with the batch id. Fill in the top of a batch sheet. Get one AI model's forecast for this batch and log it before you start (prompt and rules in the preamble; note the model's name and version).
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

## Order of batches

- [ ] **B1. Practice.** If you could weigh, wet all the powder and keep to the times, write down the method exactly as you did it. If not, practise again under the next id.
- [ ] **B2. Batch A.** Fresh ingredients, the written method.
- [ ] **B3. Batch B.** Fresh ingredients again, on a different day if you can. Never split A to make B.

## Pack and hand over

- [ ] **P1.** Use the container LongWin names. For A, then B: weigh the empty container with its lid; spoon in about **5 g** (LongWin needs about 1 mL, roughly 2.2 g); close it and weigh it again; write down both numbers. Label it with its batch id plus **-L1**. Wipe the spatula clean and dry between A and B.
- [ ] **P2.** Keep the rest of each batch sealed as an archive, labelled batch id plus **-A1**. Photograph each archive from the side at 1 hour and at 1, 3, 7 and 14 days, to record any oil separating.
- [ ] **P3.** Reference paste: photograph its label and lot. Add nothing to it. Move about 5 g into its own container with the reference-only tool. Label it **REF-L1**.
- [ ] **P4.** Optional fourth sample, only if LongWin quoted it: a second container from A. Then label all three home-made containers with plain codes (S1, S2, S3) and keep the key to batch ids in your own record.
- [ ] **P5.** Before the samples leave: log an AI forecast of the lab's numbers for each container. Run `python3 trajectory/traj.py verify paste-pilot`, then the same with `anchor`. Commit and push `trajectory/anchors.log`, timestamp that file with an outside service such as opentimestamps.org, and copy `trajectory/campaigns/` to a second disk.
- [ ] **P6.** Tell LongWin what is ready and agree the drop-off.
- [ ] **P7.** Deliver with the safety data sheets and a list of what each container holds. Get a receipt and a result date.

## Afterwards

- [ ] **A1.** Save LongWin's files unchanged. Compare A with B and write down what you decide next.
- [ ] **A2.** Start the experiments in [EXPERIMENTS.md](EXPERIMENTS.md) at C1. They need the new oil in hand and the handling review extended as in G1.

## Beside the pilot (no powder)

Do these in any gap; none of them holds up the pilot. Steps are in [EXPERIMENTS.md, C0](EXPERIMENTS.md#c0-before-any-powder).

- [ ] **N1.** Buy the oil above and the small items in [What to buy](EXPERIMENTS.md#what-to-buy).
- [ ] **N2.** Check the spread rig on plain oil, then on the reference paste.
- [ ] **N3.** Take each model's first forecasts for the three experiments and log them.
- [ ] **N4.** Ask a second person whether they can code cups and read photos blind.

Not this round: density and spread on batches, more recipes, backup labs. Leave those parts of the batch sheet marked "not measured".
