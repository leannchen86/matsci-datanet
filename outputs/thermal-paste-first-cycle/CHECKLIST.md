# Thermal paste checklist

Work down the list in order. Tick a box only when its "done when" is true. Details, links and safety notes for every item are in [README.md](README.md). Nothing here has been ordered, booked or sent.

Commands are run from the repository root.

## 1. Calls and orders (day one)

Day one is paste orders and the LongWin call only. Two vendors are on Eastern time, so finish them before 11 am Pacific. Nothing for copper until every paste order has a confirmation.

### 1.1 Thermal labs: three phone calls, same day

Phone, do not use forms. Give your friend's company as the organisation: LongWin's forms require a company name and job title. Ask every lab the same six things: earliest date, price and whether a card is accepted, at least three thicknesses per paste, grams needed, whether the raw files are released, and whether you may publish naming the lab.

- [ ] **LongWin / MyHeatSinks, Livermore** (the standard method, walk-in or drop-off). Call +1 925-493-7064 (LongWin's own line) and +1 925-393-3330 (MyHeatSinks sales, same address). Also ask: a self-run half day or engineer-run testing of four dropped-off pastes, whichever is sooner; whether a first-time visitor may run the tester; hot face at or below 80 °C; whether a paste containing zinc oxide is allowed. If nobody answers live by Tuesday, go in person: 3167 Independence Drive, Livermore, Monday to Friday 9 to 5.
- [ ] **Thermal Engineering Associates, Santa Clara** (a different company with its own tester; samples can be hand-delivered). Call 650-961-5900. One question decides it: do you measure the thermal conductivity of a silicone grease for outside customers, at several thicknesses?
- [ ] **Analysis Tech, Wakefield MA** (mail-in; the tester's maker runs customer samples; published turnaround 1 to 2 weeks). Call (781) 245-7825 before about 1 pm Pacific. Get a quote moving now, in parallel with the local answers.

**Choosing.** The primary is whichever lab first confirms a date, three or more thicknesses, raw data, permission to publish and a price under $1,000 for the first session. The second lab is the next one to confirm the same things. Two labs measuring the same material is worth having: agreement between two instruments is evidence the numbers can be trusted.

**48-hour rule.** If neither local lab has given a date by the end of Wednesday 7 October, ship to Analysis Tech and ask Thermal Analysis Labs in Canada (+1 877-827-7623, closes 1 pm Pacific) for an expedited quote.

Other options, in the order found: PMIC in Corvallis OR ((541) 753-0607), Linseis in New Jersey (from 250 EUR per measurement, 2 to 3 weeks), Barnett Technical in Elk Grove CA (a different method; ask whether the instrument is on site). Stanford's shared labs have no thermal conductivity instrument and need about 15 business days of paperwork, so they are not an option for this.

**Done when:** each of the three labs has given a date and a price, or a named person and a callback time.

### 1.2 Orders, shipped to the business address

- [ ] **Amazon, one cart.** Links and exact products are in README.md under "Order now".
  - Balance, 0.01 g, 1 kg capacity
  - 2 oz cups with lids, stainless micro scoops, 10 mL syringes
  - 4 inch square glass plates (5 pack)
  - 500 g calibration weight
  - Lint-free wipes
  - Half-mask respirator, P100 filters, safety glasses, nitrile gloves
  - Room thermometer-hygrometer, 6 inch digital caliper
  - Thermocouple board, hub and cable (three items)
  - Cartridge heaters, 24 V 40 W, 6 mm
  - Bench power supply, 30 V 5 A
  - 120 mm liquid cooler and its 12 V power adapter
  - Digital micrometer, 0.001 mm
  - Wet-and-dry paper (400 to 3000 grit) and polyimide tape
- [ ] **Atlantic Equipment Engineers** (alumina). No cart button was found on the page, so phone (201) 828-9400. Order 2 lb of AL-602 (coarse) and 2 lb of AL-611 (fine). Ask for 2-day shipping, the AL-611 safety data sheet, and a particle-size certificate for both.
- [ ] **ScienceKitStore** (silicone oil, 1000 cSt, quarter gallon). Web order. This is the slowest parcel: ask for an expedited option and for the safety data sheet. Adding the 350 cSt oil now saves a second shipment later.
- [ ] **SkyGeek** (DOWSIL 340 reference paste, 142 g). Web order before 11 am Pacific for same-day dispatch, with a fast service. Ask whether its shipping class limits air freight.
- [ ] **Newark** (Omega thermocouples, type K, 30 gauge, pack of 5). Confirm stock before paying.
- [ ] **OnlineMetals** (1 inch square 6061 aluminium bar, 12 inch). Use the custom-cut option for two 40 mm pieces if someone else will face the ends.
- [ ] **LittleMachineShop** (polyester shim assortment, part 4304).
- [ ] Boron nitride can wait. It ships from Canada and is not used before the first gate.

**Done when:** every order has a confirmation and a delivery date. Write down any parcel with no date before Saturday 10 October.

### 1.3 Pick up locally

- [ ] 99% isopropyl alcohol (read its label and data sheet)
- [ ] A rigid stainless 1-teaspoon measure with a flat rim (the density cup)
- [ ] 100 g check weight
- [ ] Rimmed tray large enough for balance, cup and powder bag
- [ ] Two lidded waste tubs, airtight tubs and desiccant for opened powder, a closed metal or lidded container for oily wipes
- [ ] Labels and marker, zip bags, phone stand, printed millimetre grid, timer
- [ ] Ceramic tile (base for the rig), melamine foam sponges (insulation), 12 inch square of 1/4 inch float glass (lapping surface)
- [ ] Lever-nut connectors or a terminal block, a basic multimeter, a USB-C cable
- [ ] Insulated mug and stirrer (for comparing thermocouples)

### 1.4 Decisions and people

- [ ] Decide who drills and faces the two aluminium blocks: a makerspace, a friend with a shop, or buy the drill press and vise ($147). Put that work on a named day.
- [ ] Send the paste safety questions to a qualified person on their own: respirator type and fit, handling 25 g of alumina over a tray in this room, and vapour from the rig at or below 80 °C. Ask for an answer before powder is first opened. Whether to open powder without it is your decision with the data sheets in hand. The fine alumina stays closed until its own data sheet arrives.
- [ ] Book a respirator fit check with an occupational health provider.
- [ ] Find someone with electronics experience to look over the heater wiring before it is first powered.
- [ ] Tell your disposal route that the reference paste is 59 to 79% zinc oxide, and that its waste will be kept in a separate tub.

## 2. While parcels are in transit (desk work)

- [ ] **Rehearse the logging loop** on any quick measurement, three runs over two sittings.

```sh
python3 trajectory/traj.py init rehearsal-001 --text "REHEARSAL: weigh one level teaspoon of salt"
python3 trajectory/traj.py add rehearsal-001 plan --run R01 --text "level teaspoon, struck off with a knife" --data spoon=level --data _session=S1
python3 trajectory/traj.py add rehearsal-001 prediction --run R01 --author ai:MODEL-NAME --text "PASTE THE MODEL'S REPLY"
python3 trajectory/traj.py add rehearsal-001 action --run R01 --text "what you actually did"
python3 trajectory/traj.py add rehearsal-001 observation --run R01 --text "6.12 g" --data mass_g=6.12 --data _status=observed
python3 trajectory/traj.py verify rehearsal-001
```

  **Done when:** `verify` shows predictions logged before outcomes and one exact repeat in a different session.

- [ ] **Save and read the safety data sheets** for the alumina, the oil and the reference paste. Copy the hard limits from README.md onto one page and put it at the bench.
- [ ] **Test whether models already know the answers.** Write 15 paste recipes from the table in section 4. For each, ask three models (fresh conversation each, prompt in `trajectory/ai-expert-prompts.md`, no campaign log) to predict density, mixing class and spread diameter. Save every reply verbatim with the model name and version.

- [ ] Score those replies against what is already published: the reference paste at 0.67 W/mK and specific gravity 2.1, and the no-air densities in the recipe table. Three models agreeing with each other is not evidence that they are right.

  **Done when:** 45 predictions are saved and one table shows each model's error where a published value exists.

- [ ] **Outside contact, sent by you.** Once that table exists (about 12 to 13 October), send one short message, with the task card and the table, to each group that builds tests for models in chemistry and materials. One message per group. Say it is a proof of concept and ask two things: would you use this if it were ten times larger, and what would it have to contain? A specific answer to the second question is the signal that someone wants more.

- [ ] **Write the one-page task card:** what is given (the recipe fields), what must be predicted (mixing class, density, spread diameter; thermal impedance later), and how a prediction is scored against the scatter between repeats.
- [ ] **Check the thermal calculation** returns LongWin's published example:

```sh
python3 outputs/thermal-paste-first-cycle/thermal.py fit 0.01:0.787 0.02:1.200 0.03:1.523
```

  **Done when:** it prints 2.72 W/mK and 0.434 C-cm2/W.

## 3. Bench set-up (the day the starter kit arrives)

- [ ] Lay out the tray on a level, vibration-free surface with a cardboard draught shield round the balance.
- [ ] Check the balance with the 100 g and 500 g weights, three times each. **Done when:** every reading is within 0.03 g.
- [ ] Find the density cup's volume: tare the cup, fill it with water to the rim, strike it level, weigh. Repeat five times. Volume in mL is the water mass in grams divided by 0.998. **Done when:** the five volumes agree within 0.5%.
- [ ] Weigh the top glass plate and write its mass down. The load in the spread test is that plus 500 g.
- [ ] Set up the photo stand over the millimetre grid.
- [ ] Label the two waste tubs: "reference paste (zinc oxide)" and "everything else".
- [ ] Start the campaign:

```sh
python3 trajectory/traj.py init paste-001 --text "Find how filler loading and particle size set mixing limit, trapped air, spread and thermal impedance of hand-mixed alumina-silicone pastes"
```

## 4. One batch, step by step

Recipes for a 25 g batch. For any other recipe run `python3 outputs/thermal-paste-first-cycle/recipe.py --filler 45 --fine-share 30`.

| Recipe | Oil | Coarse alumina | Fine alumina | Density with no air |
|---|---|---|---|---|
| Control: 40 vol%, 30% fine | 6.71 g | 12.81 g | 5.49 g | 2.170 g/cm3 |
| Extreme 1: 30 vol%, coarse only | 9.08 g | 15.92 g | 0 | 1.870 g/cm3 |
| Extreme 2: 55 vol%, 30% fine | 4.17 g | 14.58 g | 6.25 g | 2.620 g/cm3 |
| Extreme 3: 40 vol%, fine only | 6.71 g | 0 | 18.29 g | 2.170 g/cm3 |
| Extreme 4: 50 vol%, coarse only | 4.91 g | 20.09 g | 0 | 2.470 g/cm3 |

The mixing times and the spread dose below are starting values. Adjust them during the shakedown, then freeze them in writing on Sunday 11 October.

**Before touching powder**

- [ ] Log the plan with every setting as a field.
- [ ] Get two model predictions (one without the campaign log, one with it) and log both.

```sh
python3 trajectory/traj.py add paste-001 plan --run R001 --text "Control recipe, first shakedown batch" \
    --data filler_vol_pct=40 --data fine_share_pct=30 --data oil_cst=1000 --data batch_g=25 \
    --data _session=S01 --data _lot=AL602-LOTNUMBER --data _chosen_by=human
python3 trajectory/traj.py add paste-001 prediction --run R001 --author ai:MODEL-NAME --data _context=cold < cold.md
python3 trajectory/traj.py add paste-001 prediction --run R001 --author ai:MODEL-NAME --data _context=warm < warm.md
```

**Make it**

- [ ] Respirator, glasses and gloves on. Note room temperature and humidity.
- [ ] First batch of every session: measure the reference paste's density and spread (steps below) before any batch of your own.
- [ ] Tare a labelled cup. Weigh in the oil. Write down the actual mass, not the target.
- [ ] Over the tray, spoon in the powder in three roughly equal portions. After each portion, fold with the spatula for 60 seconds, scraping the wall and base.
- [ ] After the last portion, mix for a further 3 minutes. Write down each powder's actual mass.
- [ ] Let it rest 2 minutes. Seal the powder bags back in their tubs.

**Measure it**

- [ ] **Mixing class.** Pick one: `flows` (levels on its own), `paste` (holds a peak, spreads easily), `stiff` (hard to spread), `will_not_wet` (dry clumps remain). The last is a result: log it and stop there.
- [ ] **Density.** Press paste into the tared density cup with the spatula so no pockets remain, strike it level, wipe the outside, weigh. Do this three times from the same batch. Density is mass divided by the cup volume. Trapped air in percent is (1 − measured density ÷ density with no air) × 100.
- [ ] **Spread.** Weigh 1.00 g of paste onto the centre of the lower glass plate. Lower the top plate flat, add the 500 g weight, start a 60 second timer. Photograph from above with the grid visible, then measure two diameters at right angles with the caliper. Do this twice.
- [ ] Keep the rest of the batch in its lidded, labelled cup. It is the sample for LongWin.
- [ ] Copy the photos into `trajectory/campaigns/paste-001/raw/` before logging them. Do not edit them afterwards.

**Log it and clean down**

```sh
python3 trajectory/traj.py add paste-001 action --run R001 --text "Oil 6.73 g, coarse 12.80 g, fine 5.50 g. Mixed 3 x 60 s then 3 min. No deviations." \
    --data oil_g=6.73 --data coarse_g=12.80 --data fine_g=5.50 --data room_c=21.5 --data humidity_pct=48
python3 trajectory/traj.py add paste-001 observation --run R001 --file raw/R001_spread_1.jpg --file raw/R001_spread_2.jpg \
    --text "Paste. Density fills 2.09, 2.10, 2.08 g/cm3. Spread 41.2 x 40.6 mm and 42.0 x 41.1 mm." \
    --data mix_class=paste --data density_g_cm3=2.09 --data spread_mm=41.2 --data _status=observed
python3 trajectory/traj.py add paste-001 decision --text "what you will do next and why"
```

- [ ] Wipe plates, spatula and cup with alcohol on a wipe. Damp wipes only for any stray powder; never sweep or blow.
- [ ] Wipes that touched the reference paste go in its own tub. Oily wipes go in the closed container.
- [ ] If a batch fails, start the observation text with the cause: `process`, `measurement`, `handling`, `equipment` or `unknown`.
- [ ] At the end of every bench session run `python3 trajectory/traj.py verify paste-001` and write down the number of late or forced entries. It goes in Monday's numbers.

## 5. Shakedown, then the gate runs

- [ ] **Shakedown (not counted), about 12 batches.** Control, 30, 50 and 55 vol%. Time weighing, mixing, density and spread separately. Find where hand mixing stops wetting the powder. Adjust the spread dose until the control lands between 30 and 50 mm.

  **Done when:** within one batch, the three density fills agree within about 1% and the two spreads within about 5%.

- [ ] **Freeze** the mixing protocol, the control recipe, the spread dose and the cup-fill method in a `note` entry.
- [ ] **Write the gate schedule:** 12 control batches and each of the four extremes made twice, in random order over three days. Log a plan entry for each with `_chosen_by=schedule`, then anchor it and push:

```sh
python3 trajectory/traj.py anchor paste-001
git add trajectory/anchors.log
git commit -m "Anchor the gate schedule"
git push
```

- [ ] Log both predictions for every gate run before the first one is made.
- [ ] **Three gate sessions.** Each starts with the reference paste, then four fresh control batches and the scheduled extremes. Keep one control cup from two different days for LongWin.

## 6. The home thermal rig (in parallel, judged a week later)

- [ ] Cut two 40 mm blocks from the bar. Each needs two 1.6 mm holes drilled to the centre line, 5 mm and 25 mm from the test face. The upper block also needs a 6 mm hole for the heater. Ask whoever drills them to face both ends flat and square.
- [ ] Lap each test face on wet-and-dry paper taped to the float glass, working up to the finest grit.
- [ ] Compare all thermocouples in one stirred mug of water, at room temperature and near 60 °C. Record each one's offset. **Done when:** they agree within 0.1 °C after correction.
- [ ] Seat the thermocouples in their holes with a trace of reference paste. Fold each stripped wire end double before clamping it in the board's terminal.
- [ ] Stack on the ceramic tile: cooler, lower block, three 2 × 2 mm shim tabs near the corners, paste, upper block with heater, insulation round the sides, a fixed weight on top. Measure each shim stack with the micrometer.
- [ ] Wire the heater through a thermal cut-out to the bench supply. Set the current limit. **Have the wiring checked by a person before first power-on.**
- [ ] First run on the reference paste at a 200 micrometre gap. Start near 10 W and raise it only while the hottest thermocouple stays below 80 °C. Stay with it the whole time.
- [ ] When the readings stop changing, compute the result:

```sh
python3 outputs/thermal-paste-first-cycle/thermal.py mount --hot 52.0 49.6 --cold 37.4 35.1
```

- [ ] Ten separate mounts of the reference paste. **Done when:** the scatter between mounts is computed. If it is above 15% by Friday 16 October, ask about renting the needle-probe instrument instead of slipping the schedule.

At about 10 W the temperature difference along each bar is only about 2 °C, so thermocouple offsets matter. If the two bars' heat flows differ by more than about 15%, check insulation and thermocouple seating before trusting the number.

## 7. Reference lab day

**One lot for every lab.** So that two labs measure the same material, make a transfer lot separate from the campaign batches: mix three control batches on one day by the frozen protocol, combine them and fold for a further 3 minutes (about 75 g). Log it as its own lot. Split it by alternating scoops into capped syringes with little headspace: about 30 g for the primary lab, 15 g for the second lab, 10 g for the home rig, 10 g kept sealed. Measure density three times on each portion before anything leaves; they should agree within about 1%. Label by id only, send reference paste from the same tube to every lab, and tell neither lab the other's result or any expected value.


- [ ] Before leaving, log model predictions for every number LongWin will measure.
- [ ] Take: the reference paste, two control cups from different days, one extreme, at least 30 g of each, labelled by run id only. Also spatulas, wipes, gloves, a USB stick and this list of questions.
- [ ] Measure the reference paste first. Time each material.
- [ ] Leave with the raw Excel files. Log them with `--file` and record the real fee and hours.

## 8. First gate, Sunday 18 October

- [ ] Make one table: label, scatter within a batch, scatter between days, range across the extremes, the ratio, and the models' error with and without the campaign log.
- [ ] Pass needs all four:
  1. Control batches across three days agree: density within 2%, spread within 7%.
  2. The extremes differ by at least 3 times that scatter on two labels.
  3. LongWin reads the reference paste within 15% of 0.67 W/mK and the two control batches within 10% of each other.
  4. The models' predictions made without the campaign log miss by more than the scatter on at least one label.
- [ ] Log the decision (pass, pending, one more week, or stop) and anchor it.

If item 3 has not happened yet, the decision is "process labels pass, LongWin pending".

## 9. Copper: desk work only

About 10 hours in total, spread over the week, and nothing bought. Copper is not bench work until the paste gate decision is logged. If pastes pass, copper stays a desk item until the 29 November review. If pastes fail twice, copper replaces them.

- [ ] **C1 (1 h).** Ask your household, your own landlord and insurer, and your friend's company whether each would accept corrosive (shipping class 8) chemicals and this work. Get the answers in writing.
- [ ] **C2 (1 h).** One disposal conversation covering both tracks. Describe the project truthfully and ask them to classify it. Paste track: solids containing zinc oxide, oily wipes. Copper track: about 25 L of liquid every two weeks, pH about 1, about 40 g/L copper.
- [ ] **C3 (1 h).** Write the copper questions for a qualified person on one page and ask for a fee quote: is this room's ventilation adequate for stirred, unheated, covered 267 mL baths; do a faucet eyewash and a household shower meet the data sheets; which gloves and face protection; acid mist in an occupied home; storage. Send it after the paste questions, never bundled with them.
- [ ] **C4 (2 h).** Open the published robot copper dataset (<https://zenodo.org/records/19520337>) and find out whether it holds a measured outcome for each run.
- [ ] **C5 (3 h).** Copper desk test with the same three models. Score it against that dataset if C4 says yes, otherwise against published thresholds. If nothing can be scored, log it as descriptive and draw no conclusion.
- [ ] **C6 (1.5 h).** Copper task card on the same template as the paste card.
- [ ] **C7 (1 h, the day after the paste gate decision).** Review: are C1 to C3 answered in writing, what is the quoted fee, does the fee plus about $3,300 fit a $4,200 ceiling, did C5 show that models get copper wrong. Write one decision.

No acid or other copper chemical is ordered or opened until a qualified person who has seen the room has answered in writing, the disposal route has accepted the real volumes, and the people who own or share the premises have agreed.
