# Thermal paste: what to do next

Updated Tuesday 6 October 2026, late evening. This page is the whole plan. The long versions are in [BENCH_PROTOCOL.md](BENCH_PROTOCOL.md) (bench method, section 1) and [CALLS_AND_ORDERS.md](CALLS_AND_ORDERS.md) (scripts and the LongWin form guide). Numbers in brackets are the old item numbers those files refer to.

**Goal:** hand LongWin three samples: the bought reference paste, and two batches (A and B) of one home-mixed recipe, made separately.

## Where things stand

- **Arriving Wednesday 7 October:** coarse alumina, fine alumina and the reference paste (McMaster, by 5 pm); silicone oil (Grainger San Jose, 2261 Ringwood Ave, pick up only after the ready notice); the 0.001 g balance (check your order for its date).
- **LongWin:** wants its service form before quoting. Needs about 1 mL of each sample. About one week to test plus one week to report. No appointment yet.
- **Do not buy:** more powder, more oil, another balance, or anything for the thermal rig.

## Three things that gate everything

- [ ] **G1. Powder handling [15].** Do not open either powder until your workspace, dust control and protective equipment are settled. Everything in "Set up" below can be done without powder.
- [ ] **G2. LongWin form [17].** Fill it in and send it. Ask for: price, which container to use, a drop-off date, the measured data points as Excel, permission to publish naming the lab, and the price of an optional fourth sample.
- [ ] **G3. Balance check [16].** It must pass (step S5) before you weigh a recipe.

## Set up (no powder needed)

- [ ] **S1.** Collect the oil and the parcels. Photograph every label and lot number before opening anything. [18]
- [ ] **S2.** Read both powder certificates in full. The coarse one says 99.40% against 99.5% on the listing; write that down. [05]
- [ ] **S3.** Gather the kit: about ten lidded 60 mL plastic cups, two powder scoops (one per powder, never swapped), one mixing spatula, one tool used only for the reference paste, labels, marker, wipes, a rimmed tray, two waste tubs, a timer. [13]
- [ ] **S4.** Wash the cups and tools and dry them completely.
- [ ] **S5.** Check the balance. Warm it up and level it as its manual says. With check weights of about 2 g, 5 g and 20 g, place and remove each one five times and write down all five readings. Do one more check with the empty cup on the pan. **Pass:** every reading is within 0.010 g of the weight, and the five readings are within 0.010 g of each other.
- [ ] **S6.** Turn off location tagging on your phone camera. Print four [batch sheets](../../trajectory/batch-sheet.md). Fix the ids: **B001** practice, **B002** batch A, **B003** batch B. [27]

## Make one batch

About 30 to 45 minutes. The same steps for the practice batch, A and B.

| Ingredient | Total | How it goes in |
|---|---|---|
| Silicone oil | 6.71 g | All at the start |
| Coarse alumina | 12.81 g | 4.27 g in each of three rounds |
| Fine alumina | 5.49 g | 1.83 g in each of three rounds |

1. Label the cup with the batch id. Fill in the top of a batch sheet. Save the model's forecast for this batch before you start (prompt in [prompt-preamble.md](../../trajectory/prompt-preamble.md)).
2. Protective equipment on. Work on the tray.
3. Put the empty cup on the balance, no lid, no tool. Write down its mass. Tare. Add **6.71 g** of oil. Write down the actual reading.
4. Tare again. With the coarse scoop, held low over the cup, add **4.27 g** coarse powder. Write the actual reading. Close the pail.
5. Tare again. With the fine scoop, add **1.83 g** fine powder. Write the actual reading. Close the pail.
6. Take the cup off the balance. Fold and scrape for **60 seconds**: bottom, walls, back to the centre. Scrape the spatula clean into the cup and rest it on its own spot.
7. Repeat steps 4 to 6 twice more. That is three rounds in all.
8. Mix for **3 more minutes** the same way. Scrape the spatula into the cup. Put the lid on and rest it **2 minutes**.
9. Open it, photograph it with its id, and write down what you see: does it level, hold a peak, feel stiff, or still show dry powder? Note any dry pockets, bubbles or oil separating.
10. Close and store upright. Finish the batch sheet, photograph it, and type it into the log the same day.

**Rules while mixing**

- Tare fresh before every addition. Never weigh with the spatula in the cup. Never mix on the balance.
- Overshot an addition? Write the real number and carry on. Do not take any back out.
- Spilled something? Stop and write it down. Do not sweep it back in.
- Never put a used tool into the powder pails or the oil bottle.
- Damp-wipe any stray powder. No sweeping, no blowing, no household vacuum. Nothing down the drain.
- A batch that goes wrong keeps its id and its record. Start again under the next id.

## Order of batches

- [ ] **B1. Practice (B001) [20].** If you could weigh, wet all the powder and keep to the times, write down the method exactly as you did it. If not, practise again under a new id.
- [ ] **B2. Batch A (B002) [21].** Fresh ingredients, the written method.
- [ ] **B3. Batch B (B003) [23].** Clean and fully dry the spatula first. Fresh ingredients again, on a different day if you can. Never split A to make B.

## Pack and hand over

- [ ] **P1.** Use the container LongWin names. For each one, weigh the empty container with its lid, fill it, weigh it sealed, and write down the difference.
- [ ] **P2.** Put about **5 g** of A in one container and about 5 g of B in another. LongWin needs about 1 mL, which is roughly 2.2 g. Label them **B002-L1** and **B003-L1**.
- [ ] **P3.** Keep the rest of each batch sealed as an archive: **B002-A1**, **B003-A1**.
- [ ] **P4.** Reference paste: photograph its label and lot. Add nothing to it. Move about 5 g into its own container with the reference-only tool. Label it **REF-L1**.
- [ ] **P5.** Optional fourth sample, only if LongWin quoted it: a second container filled from A, under a neutral label.
- [ ] **P6.** Before the samples leave: save the model's forecast of the lab's numbers, then run `verify` and `anchor`, push, and copy `trajectory/campaigns/` to a second disk. [28]
- [ ] **P7.** Tell LongWin what is ready and agree the drop-off. [22]
- [ ] **P8.** Deliver with the safety data sheets and a list of what each container holds. Get a receipt and a result date. [25]

## Afterwards

- [ ] **A1.** Save LongWin's files unchanged. Compare A with B and write down what you decide next. [26]

Later, not now: the thermal rig, the density and spread measurements, more recipes, backup labs ([10], [11]) unless LongWin falls through.
