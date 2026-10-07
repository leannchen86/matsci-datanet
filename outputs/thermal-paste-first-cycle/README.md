# Thermal paste first cycle: sourcing and prep plan

Original plan prepared 5 October 2026; order status updated 6 October. McMaster ingredients and one Grainger oil bottle are ordered, the user reports ordering a balance, and LongWin has replied to the initial email. Receipt, balance checks, a completed service request, quote and appointment remain pending. See CHECKLIST.md for the current state. The older equipment catalogue and calendar below describe the broader study, not an additional shopping list for the first submission. Historical vendor checks and prices are dated; LongWin's fee still requires a quote.

**Start with [CHECKLIST.md](CHECKLIST.md), the single completion tracker for the first submission.** It lists the calls, purchases, preparation and handoff actions for the first submission, which has no fixed date, and the rules for running the experiments beside it. Consult [CALLS_AND_ORDERS.md](CALLS_AND_ORDERS.md) for supplier scripts and specifications, and [BENCH_PROTOCOL.md](BENCH_PROTOCOL.md) for detailed procedures and the later repeatability study. The equipment catalogue and original calendar below provide background; dates depend on actual delivery, handling review and laboratory acceptance. `recipe.py` gives ingredient masses and `thermal.py` does the thermal calculations.

## What this is

For the first small submission, use the [hands-on run sheet](BENCH_PROTOCOL.md#1-hands-on-run-sheet-for-the-first-submission): practice, independent A and B, and the commercial reference. Home density/spread measurements are optional at this stage and the thermal rig is deferred. The broader measurement programme below is later work, not a requirement to finish before preparing the first specimens.

Hand-mixed thermal pastes: silicone oil plus ceramic powder (alumina first, boron nitride later), about 25 g per batch, mixed by spatula to a fixed, timed protocol. No acids, no solvents beyond alcohol on wipes, no liquid waste.

Four things are measured on every batch at home, the same day:

1. **Mixing class.** Whether the powder wets and what the paste is like at the fixed protocol. The loading where hand mixing fails is a result.
2. **Density** in a small fixed-volume cup, compared with the calculated density, which gives the percentage of trapped air.
3. **Squeeze-spread.** A fixed mass of paste between two glass plates under a 500 g weight for 60 seconds; the diameter is read from a photo. This stands in for viscosity.
4. **Thermal impedance** on a small home rig (two aluminium bars, a heater, a cooler, a fixed gap). This label comes second: it is built in parallel and judged a week after the others.

The selected independent laboratory supplies the thermal reference measurements. LongWin in Livermore is the first quote request; its service lists ASTM D5470-based testing and about 2–4 hours per material. Obtain a quote for a commercial comparator and two separately mixed control batches; do not assume all three fit into one day. DOWSIL's published value is a typical property rather than a calibration certificate.

Copper electroplating stays the named fallback. Nothing is bought for it now.

## Reference labs

Call LongWin, Thermal Engineering Associates and Analysis Tech in parallel using the [call guide](CALLS_AND_ORDERS.md). MyHeatSinks is an alternate contact for the same Livermore lab, not a second independent laboratory. Prices, individual eligibility and October dates require direct confirmation. No suitable bookable grease-conductivity service at Stanford has been confirmed for this deadline.

## Equipment catalogue

The first cart is specified in [CALLS_AND_ORDERS.md](CALLS_AND_ORDERS.md): about $569–698 for materials and the density/spread kit before PPE, freight, tax, consultation and testing. The older roughly $1,430 estimate covered candidate thermal-rig parts and other items as well; do not order this whole catalogue. Finalize the rig's mechanical and electrical design before purchasing its assembly.

- **LongWin / MyHeatSinks session on the LW-9389 tester (reference only)**
  - Vendor: MyHeatSinks / LongWin North America Laboratory, 3167 Independence Drive, Livermore CA
  - Price: Not published. Reviewers' cap: decline above $1,000 for the first session (a cap, not a quote)
  - Lead time: Not published. Engineer-run turnaround 'typically one week' (https://longwinusa.com/services/thermal-interface-material-test/, opened)
  - Link: <https://myheatsinks.com/thermal-laboratory/>
  - Note: Engineer-run and self-service routes are listed. [Booking page](https://longwinusa.com/contact/booking/) lists Monday–Friday 9–5; that does not establish walk-in access. Sample quantity, fee and individual eligibility require confirmation. The repo's earlier outreach log shows a 24 Sep email awaiting response; this guide does not verify a mailbox or establish a booking.
- **Alumina, coarse (AL-602, 360 grit, 12-40 micrometres, HP white fused), 2 lb**
  - Vendor: Atlantic Equipment Engineers (micronmetals.com), Upper Saddle River NJ
  - Price: $23.07/lb at 1-2 lb, so $46.14
  - Lead time: 'In Stock for Immediate Shipping', UPS or FedEx. Ships from New Jersey: ground to California is about 5 business days (my estimate), so ask for 2-day
  - Link: <https://micronmetals.com/product/aluminum-oxide-powder-fused-3/>
  - Note: Opened. 1 lb minimum. Safety data sheet opened and it covers AL-602 (density 3.97 g/cm3, use this for the void calculation). I saw price tiers but no cart button in the page text, so the order may have to be placed by phone, (201) 828-9400 (number from the data sheet). Shipping cost not shown; I budget $45 for 2-day on both alumina grades (estimate).
- **Alumina, fine (AL-611, 1200 grit), 2 lb**
  - Vendor: Atlantic Equipment Engineers
  - Price: $23.07/lb at 1-2 lb, so $46.14
  - Lead time: 'In Stock for Immediate Shipping'; same shipment as AL-602
  - Link: <https://micronmetals.com/product/aluminum-oxide-powder/>
  - Note: Opened. Page says white fused, 99% min, '1200 grit', no micron range and no safety data sheet link. The supplier's data sheet I opened lists AL-602/603/604/605/610/612 and does not name AL-611. Ask for the AL-611 data sheet and a particle-size certificate with the order; do not open the bag before the data sheet arrives.
- **Hexagonal boron nitride, 5 micrometre average, 98%, 1 lb (MK-hBN-500)**
  - Vendor: Lower Friction = M.K. Impex Corp, Mississauga, Ontario, Canada
  - Price: $54.00 per lb; shipping and any duty or brokerage not shown (I budget $30, estimate)
  - Lead time: 'Usually ships in 1-2 business days', but from Canada (https://lowerfriction.com/contact-us/, opened). US duty-free treatment for low-value parcels was suspended on 29 Aug 2025 (https://www.cbp.gov/sites/default/files/2025-08/factsheet_suspension_of_duty-free_de_minimis_treatment.pdf, snippet), so allow 1-2 weeks (estimate)
  - Link: <https://lowerfriction.com/hexagonal-boron-nitride-powder-5-micron/>
  - Note: An earlier draft treated this as a domestic 1-2 day item; it is a cross-border shipment. Not needed for the 18 Oct gate if the boron nitride extreme is dropped (see fixes). Its data sheet (opened) asks for mechanical exhaust or a fume hood: stays sealed until a person clears that.
- **Silicone oil 1000 cSt (AK1000, CAS 63148-62-9), quarter gallon**
  - Vendor: ScienceKitStore (ships from New Jersey)
  - Price: $42.00; shipping not shown (I budget $20, estimate)
  - Lead time: In stock; ships same day, but the vendor's policy says 3-10 business days to a US address (https://sciencekitstore.com/shipping-policy, opened). Expect about 13 Oct by ground (estimate)
  - Link: <https://sciencekitstore.com/silicone-fluid-1000-cst>
  - Note: Confirm expedited delivery, the applicable SDS and available lot/viscosity documentation. The current page does not establish a COA policy. About 6–8 g of oil per typical 25 g control batch is a calculation, not a measured dispensing result.
- **Reference paste: DOWSIL 340 heat sink compound, 142 g tube**
  - Vendor: SkyGeek
  - Price: $59.43; shipping not shown (I budget $15, estimate)
  - Lead time: Physical stock and actual arrival must be confirmed. Guaranteed same-day dispatch during 7 am–2 pm Eastern is an optional $25 add-on; delivery is a separate service and charge.
  - Link: <https://skygeek.com/dow-corning-dc340-5oz-silicone-compound-5-oz.html>
  - Note: Opened. Replaces Ellsworth, which still shows 'on backorder' today at $68.34 (opened). SkyGeek lists it as UN3077 class 9; ask whether that limits air shipping. Other checks: Amazon listing 'currently unavailable' (opened); Aerospheres shows 18 in a California warehouse at $53.31 but also a 120-day lead time (opened, inconsistent); Aircraft Parts Supply shows $16.25 on sale with no stock status (opened, do not rely on it). Dow's own page gives 0.67 W/mK and specific gravity 2.1 (https://www.dow.com/en-us/pdp.dowsil-340-heat-sink-compound.01015443z.html, opened).
- **Balance, 0.001 g**
  - Vendor: U.S. Solid, JFDBS00057-500G / USS-DBS57-5, 500 g capacity.
  - Price: $184.99 advertised; confirm delivery.
  - Link: <https://ussolid.com/products/u-s-solid-500-x-0-001g-analytical-balance-1-mg-digital-precision-balance-lab-scale-html>
  - Note: Paired with the smaller density measure to preserve sample mass. Manufacturer specifies ±0.002 g repeatability; includes draft shield and 500 g calibration weight. Validate performance at actual working masses. Weigh the plate and spread load separately; their combined mass exceeds capacity.
- **Mixing cups with lids, spatulas, syringes**
  - Vendor: Amazon
  - Price: 2 oz cups with lids, 50 count $3.00; 15 stainless micro scoops $9.99 (ASIN B07HHWCNB9); 10 mL luer-slip syringes, 20 pack $8.79 (ASIN B07MVWQVKF). Total $21.78
  - Lead time: Listings showed next-day delivery with Prime
  - Link: <https://www.amazon.com/dp/B0D6SNKHR7>
  - Note: Search listings opened, product pages not opened. One lidded cup per batch, labelled with the run id, doubles as the retained sample for LongWin. Stiff paste will not draw into a syringe: fill from the back with a spatula, or dose the spread test by mass.
- **Glass plates for the squeeze-spread test**
  - Vendor: Amazon: CleverDelights 4 inch square glass tiles, 5 pack (ASIN B08BW5SV2K)
  - Price: $25.99
  - Lead time: In stock; listing showed next-day with Prime
  - Link: <https://www.amazon.com/dp/B08BW5SV2K>
  - Note: Product page opened: 4 x 4 x 1/8 inch, both sides flat. The top plate's own mass (about 80 g, my estimate) adds to the 500 g load: weigh it and record the total.
- **500 g weight for the spread test**
  - Vendor: Amazon: Bonvoisin 500 g class M1 calibration weight (ASIN B09S3BLS5Q)
  - Price: $11.99
  - Lead time: Listing showed delivery Wed 7 Oct
  - Link: <https://www.amazon.com/dp/B09S3BLS5Q>
  - Note: Search listing opened only. Keep the balance's own calibration weight clean and separate from this one.
- **Wipes and isopropyl alcohol**
  - Vendor: Amazon (wipes); a local pharmacy for the alcohol
  - Price: Kimwipes 4 boxes $28.95; 99% isopropyl alcohol 32 oz $13.99 (ASIN B00DT52Y98)
  - Lead time: Wipes: listing showed Wed 7 Oct. Alcohol: listing showed no delivery date
  - Link: <https://www.amazon.com/dp/B07Z5Q8NL5>
  - Note: Search listings opened only. Buy the alcohol locally and read its label and data sheet; I opened no data sheet for it.
- **Respirator, glasses, gloves**
  - Vendor: Amazon
  - Price: 3M 6200 half facepiece, medium $21.31; 3M 2091 P100 filters, 3 pairs $24.00; 3M Virtua CCS safety glasses $13.39 (ASIN B00AEXKR4C); nitrile gloves, 100 count $6.99. Total $65.69
  - Lead time: Respirator product page: in stock, delivery Thu 8 Oct shown; others next-day with Prime on the listings
  - Link: <https://www.amazon.com/dp/B002XJMKHW>
  - Note: Respirator product page opened; the rest are search listings. 'Medium' is a placeholder: size and fit must be confirmed by a person (see safety corrections). The DOWSIL 340 data sheet names an organic vapour cartridge, not a particle filter, if the paste is heated without enough ventilation: 3M 60921 OV/P100 pair is $24.59 (ASIN B00BT2SWTE, search listing). Buy it only if the person reviewing the rig says so.
- **Room thermometer-hygrometer and digital caliper**
  - Vendor: Amazon
  - Price: TempPro TP50 $10.99; 6 inch digital caliper $21.98 (ASIN B08Y8M54M9). Total $32.97
  - Lead time: Listings showed next-day with Prime
  - Link: <https://www.amazon.com/dp/B01H1R0K68>
  - Note: Search listings opened only. Added: an earlier draft records room temperature as a field but listed nothing to measure it, and both powder data sheets say the powders take up moisture. The caliper reads two perpendicular spread diameters directly.
- **Thermocouple logger (cheapest credible)**
  - Vendor: Amazon, sold by Phidgets Inc.: TMP1101_1 4x Thermocouple Phidget plus HUB0002_1 VINT Hub (USB-C) plus 60 cm Phidget cable
  - Price: $49.99 + $49.99 + $3.99 = $103.97 ($40 + $40 direct from Phidgets in Calgary: https://www.phidgets.com/?prodid=1215 and https://www.phidgets.com/?prodid=1289, opened)
  - Lead time: Board product page: in stock, ships from Amazon. Hub and cable listings showed next-day with Prime
  - Link: <https://www.amazon.com/dp/B0BY8KZ9LC>
  - Note: Replaces the $519 Pico TC-08 for the first build. Maker's page (opened): 4 inputs, types J/K/E/T, 0.04 C resolution for type K, screw terminals, macOS and Python supported, hub required, no USB cable included. Limits: four channels only (two per bar, none spare for ambient); the terminals are specified for 16-26 AWG, so fold the thin thermocouple wire ends double. A DATAQ DI-2008 is $599 (snippet), so it is not a cheaper option.
- **Thermocouples**
  - Vendor: Newark: Omega 5TC-TT-K-30-36 (type K, 30 AWG, 36 inch, stripped leads, pack of 5)
  - Price: $102.85 per pack of 5; shipping not shown (I budget $10, estimate)
  - Lead time: Stock not shown on the search page I opened; confirm before ordering
  - Link: <https://www.newark.com/search?st=5TC-TT-K-30-36>
  - Note: An earlier draft's part, 5TC-TT-T-36-36, is $118.98 at Newark with 91 in stock (opened), not $85.90; it has stripped leads, and 36 AWG wire (0.13 mm) is fragile for a beginner. 30 AWG is sturdier and still fits a 1.6 mm hole. If a TC-08 is bought later it needs the plug version, 5SRTC-TT-T-30-36, about $136 (snippet). Cheapest alternative: Phidgets TMP4103_0, type K, 28 AWG, PTFE, bare leads, $5 each (https://www.phidgets.com/?prodid=727, opened), but it ships from Canada.
- **Meter bars: 6061 aluminium square bar, 1 inch x 12 inch**
  - Vendor: OnlineMetals
  - Price: $17.46 per foot (an earlier draft said $14.95); shipping not shown (I budget $15, estimate)
  - Lead time: Not shown on the page
  - Link: <https://www.onlinemetals.com/en/buy/aluminum/1-aluminum-square-bar-6061-t6511-extruded/pid/1116>
  - Note: Opened in a browser (the plain fetch was refused). A 'Custom Cut' option exists. Saw-cut ends are not flat or square: see missing items.
- **Cartridge heater, 24 V 40 W, 6 x 20 mm**
  - Vendor: Amazon: RANIT 4-pack (ASIN B0DLV7T2GF); or Filastruder, E3D heater cartridge
  - Price: $10.49 for 4 (Filastruder: $3.49 each, in stock, https://www.filastruder.com/products/e3d-heater-cartridge, opened)
  - Lead time: Amazon page: 'Only 7 left', Wed 7 Oct with Prime
  - Link: <https://www.amazon.com/dp/B0DLV7T2GF>
  - Note: Both pages opened. An earlier draft pointed at digikey.com with no product. These are 3D-printer parts with no safety listing that I could see. A 6 mm cartridge needs a 6 mm hole, not the 1/4 inch bit an earlier draft names (0.35 mm oversize).
- **Bench power supply, 30 V 5 A with current limit**
  - Vendor: Amazon: NICE-POWER 30 V 5 A (ASIN B0C69NHPKD)
  - Price: $34.59 (an earlier draft guessed $90)
  - Lead time: In stock; listing showed next-day with Prime
  - Link: <https://www.amazon.com/dp/B0C69NHPKD>
  - Note: Product page opened: display resolution 0.1 V and 0.01 A. That is about 1% on the power reading at 17 V, 1.2 A (my calculation), acceptable only as a cross-check on the bar-gradient heat flow. A Korad KA3005D is $125-136 (snippet) if a better readout is wanted after the gate.
- **Cold side: 120 mm all-in-one liquid cooler plus mains power for it**
  - Vendor: Amazon: Thermalright Aqua Elite 120 V3 (ASIN B0CL91749Q) and Delinx 12 V fan power adapter with splitter (ASIN B0BLMF8GMC)
  - Price: $33.89 + $14.99 = $48.88
  - Lead time: Both product pages: in stock; next-day with Prime on the listings
  - Link: <https://www.amazon.com/dp/B0CL91749Q>
  - Note: Both pages opened. An earlier draft omitted that a PC cooler has no mains plug: pump and fan need a 12 V fan-header supply. The adapter page says it suits 2/3/4-pin fans and pumps; I did not confirm the pump's connector on the cooler page. The Noctua NV-PS1 I checked first is 'currently unavailable' on Amazon (opened). Unverified: whether the pump housing may carry the clamp load when the block sits upside down.
- **Gap spacers (shim tabs)**
  - Vendor: LittleMachineShop, Pasadena CA: part 4304, polyester shim assortment, seven 5 x 5 inch sheets, 0.0005-0.005 inch
  - Price: $19.95 (same item is $49.57 on Amazon); shipping not shown (I budget $8, estimate)
  - Lead time: In stock; ships from Pasadena
  - Link: <https://littlemachineshop.com/products/product_view.php?ProductID=4304>
  - Note: Opened. An earlier draft asked for polyester at 0.004, 0.008 and 0.012 inch. The common colour-coded assortments switch from polyester to vinyl at 0.0075 inch and above (https://www.precisionbrand.com/product-category/plastic-color-coded-shim/, opened); vinyl softens near the rig's hot-face temperature (my judgement, no source opened). Use polyester only: one 0.004 inch tab for about 100 micrometres, two stacked for about 200, and 0.005 + 0.005 + 0.002 for about 300. Measure every stack with the micrometer.
- **Micrometer, 0-25 mm, 0.001 mm**
  - Vendor: Amazon: SHAHE digital micrometer (ASIN B07ZQ4WW24)
  - Price: $32.99
  - Lead time: In stock; listing showed next-day with Prime
  - Link: <https://www.amazon.com/dp/B07ZQ4WW24>
  - Note: Product page opened. An earlier draft named no product. Shars 303-2401 is out of stock (opened). Mitutoyo 293-340-32 is $175 with delivery 13-15 Oct (search listing): not needed before the gate.
- **Lapping paper and tape**
  - Vendor: Amazon
  - Price: Wet-and-dry sheets 400-3000 grit, 12 sheets $8.99; polyimide tape 4-pack $9.99 (ASIN B072Z92QZ2). Total $18.98
  - Lead time: Listings showed next-day with Prime
  - Link: <https://www.amazon.com/dp/B0F6THV3F2>
  - Note: Search listings opened only. Flat backing: a 12 x 12 inch piece of 1/4 inch float glass from a local glass shop (no page opened, about $15, estimate), or the Woodriver 9 x 12 inch granite plate, $79.98 with delivery 13 Oct (search listing). Insulation: melamine foam sponges from a supermarket (no page opened, about $8, estimate).
- **Drilling the blocks**
  - Vendor: Amazon: WEN 4206T 8 inch benchtop drill press (ASIN B08ZVWRZR9) and WEN DPA423 3 inch drill press vise (ASIN B09Q4PG9GB)
  - Price: $123.76 + $23.50 = $147.26, plus bits, centre punch and cutting fluid from a hardware shop (about $20, estimate)
  - Lead time: Drill press page: in stock, next-day with Prime
  - Link: <https://www.amazon.com/dp/B08ZVWRZR9>
  - Note: Drill press page opened; vise is a search listing. The WEN 4208T is sold out at WEN ($117.27, https://wenproducts.com/products/wen-4208t-2-3-amp-8-inch-5-speed-benchtop-drill-press, opened). Do not order until the Tuesday decision: a makerspace or a friend's shop makes this $0. A machining service was not priced by me (an earlier draft's $150-300 and 5-10 days is its estimate).

### Small things to pick up locally

- A small density measure: the 1/4-teaspoon member of a Vollrath 47118 set is a nominal 1.25 mL candidate. Water-calibrate its actual volume and validate filling during shakedown; it is not a certified density cup. Three fresh fills preserve far more of a 25 g batch than the previous 5 mL measure. See the call guide for the complete mass budget.
- A 100 g check weight (no page opened, about $8, estimate) in addition to the 500 g one, so the balance is checked at two loads at the start of every session, plus a cardboard draught shield and a level, vibration-free spot.
- A fixed way to photograph the spread: phone stand, ruler or printed millimetre grid under the lower plate, and a timer for the 60 s hold.
- Run-id labels and a marker, one lidded cup per batch, zip bags and a small box for carrying retained samples to Livermore.
- Airtight tubs and desiccant for opened powder bags. Both powder data sheets say the material takes up moisture; damp powder changes both the weighed recipe and the density label.
- One scoop per powder, a powder funnel, and a rimmed tray big enough for balance, cup and powder bag together.
- Two lidded waste tubs, not one: one for anything that touched DOWSIL 340 (59-79% zinc oxide) and one for everything else.
- A USB-C cable for the logger hub (none included) and a way to clamp hair-thin thermocouple wire in screw terminals (fold the stripped end double, or small ferrules).
- Mains power for the cooler's pump and fan (now on the list) and leads from the bench supply to the heater: lever-nut connectors or a terminal block, and a basic multimeter to check the supply's volt and amp display.
- A thermal cut-out in series with the heater and a non-combustible base such as a ceramic tile. Unverified part; choose it with the person who reviews the wiring.
- If drilling at home: a drill-press vise (now on the list), centre punch, cutting fluid, about ten spare 1/16 inch bits, a 6 mm bit, a deburring tool and clamps to fix the press to the bench.
- A way to get flat, square test faces. Saw-cut bar ends are neither; hand lapping from a saw cut is slow and tends to round the face (my judgement). Ask whoever cuts or drills the blocks to face both ends, or buy the bar custom-cut and budget an evening of lapping on glass. A 10-20 micrometre face error is 5-10% of a 200 micrometre gap.
- An alignment guide so the two bars sit on one axis every time: a length of angle stock or a V-block lined with insulation (no page opened).
- Tweezers and a scalpel for cutting 2 x 2 mm shim tabs; cut about 20 sets, because tabs get contaminated with paste.
- An insulated mug and a stirrer for comparing all thermocouples in one water bath, at room temperature and again near 60 C.
- For laboratory submission: the lab's confirmed grams per specimen and accepted containers, with SDSs and preparation/storage records. Do not assume 30 g or attempt to retain that amount from a 25 g batch.
- Shipping and sales tax. No vendor page I opened showed shipping to California; my total uses estimates for these.
- A backup of trajectory/campaigns/. The README says that folder is ignored by Git and is not backed up.

## Buy only after the first gate

- **Silicone oil 350 cSt (AK350), quarter gallon**
  - Vendor: ScienceKitStore
  - Price: $22.00 (an earlier draft guessed about $40)
  - Lead time: In stock; same 3-10 business day policy
  - Link: <https://sciencekitstore.com/silicone-fluid-350-cst>
  - Note: Opened. Not used before the gate. Adding it to the 1000 cSt order saves a second shipment; that is the only reason to buy it now.
- **Pico USB TC-08 logger (an earlier draft's choice)**
  - Vendor: Newark (also Mouser, TEquipment)
  - Price: $519.00
  - Lead time: Newark: not in stock, 'Manufacturer Standard Lead Time: 5 week(s)' (opened). Mouser: 276 in stock at $519 (snippet). Saelig page refused my request
  - Link: <https://www.newark.com/pico-technology/usb-tc-08/datalogger-usb-thermocouple-8/dp/02M0855>
  - Note: Buy only if the home rig passes on 25 Oct and four channels prove limiting. It needs miniature thermocouple plugs (https://www.picotech.com/data-logger/tc-08/thermocouple-data-logger, opened); an earlier draft paired it with stripped-lead thermocouples that do not plug in.
- **Vacuum degassing kit**
  - Vendor: BVV
  - Price: $255.00
  - Lead time: 'Delivery takes between 2-4 business days'
  - Link: <https://shopbvv.com/products/best-value-vacs-1-5-gallon-tall-stainless-steel-vacuum-chamber-and-v4d-4cfm-two-stage-vacuum-pump-kit>
  - Note: Opened. Pump option is 3 CFM single-stage or 4 CFM two-stage. Buy only if density shows more than about 2-3% voids.
- **Spherical alumina**
  - Vendor: Goodfellow
  - Price: From $218.00
  - Lead time: 'Approx. 2 weeks leadtime'
  - Link: <https://www.goodfellow.com/usa/alumina-spherical-powder-group>
  - Note: Opened. Particle sizes are behind a selector I did not operate.
- **Imported bench tester of the D5470 type (Xiangyi TCM-HF)**
  - Vendor: Xiangyi, made-in-china.com listing
  - Price: $2,000-5,000 listed
  - Lead time: One month, plus freight
  - Link: <https://labxiangyi.en.made-in-china.com/product/BXFQEoHdrgrv/China-Thermal-Conductivity-Tester-heat-flow-method-ASTM-D5470-Mil-I-49456A.html>
  - Note: Opened. Desktop version weighs 60 kg. Quality, duty and mains voltage unverified. Consider only if LongWin proves costly and the route passes both gates.

## Optional or fallback

- **Hexagonal boron nitride, US-shipped alternative (-5 micron, 99.0%, 1 lb)**
  - Vendor: Sandblasting Abrasives (sandblastingabrasives.com)
  - Price: $99.00 per lb
  - Lead time: '1-3 business days plus transit'; ship-from location not stated
  - Link: <https://sandblastingabrasives.com/products/hexagonal-boron-nitride-powder-order-page-781>
  - Note: Opened. Use only if the Canadian shipment stalls. No safety data sheet on the page: request it before ordering. MSE Supplies 9-12 micrometre 99% is $523.95 per 500 g, 'order upon request' (https://www.msesupplies.com/products/mse-pro-99-purity-hexagonal-boron-nitride-h-bn-powder-9-12-um, opened): too slow and expensive for now.
- **Stopgap 1000 cSt silicone oil for technique practice only**
  - Vendor: Amazon (treadmill lubricant, '100% Silicone Oil, 4 oz 1000 cSt', ASIN B08SBTYKS8)
  - Price: $8.98 per 4 oz
  - Lead time: Listing showed next-day delivery with Prime
  - Link: <https://www.amazon.com/dp/B08SBTYKS8>
  - Note: Search listing opened, product page not opened; no data sheet seen. Buy two only if the record-lot oil has no delivery date before Sat 10 Oct. Runs made with it are rehearsal runs with their own _lot and never enter the gate.
- **Second reference paste: Arctic MX-4**
  - Vendor: Arctic
  - Price: $10.99 list
  - Lead time: Not shown
  - Link: <https://www.arctic.de/us/MX-4/ACTCP00002B>
  - Note: Opened: no conductivity published (density 2.50 g/cm3, 31,600 poise). Leave it out for now: it has no published value to check against and the reviewers ruled out drifting into bought pastes.
- **Needle-probe instrument rental (fallback bulk-conductivity label)**
  - Vendor: EXI USA: METER TEMPOS
  - Price: $40 per day plus $60 preparation; shipping and insurance extra; replacement value $5,500
  - Lead time: Not stated; no minimum period stated
  - Link: <https://www.exiusa.com/item/tempos-thermal-properties-analyzer>
  - Note: Opened. Sensors listed: KS-3 (0.02-2.0 W/mK), TR-3 (10 cm, 0.1-4.0), SH-3 (dual needle), RK-3 (6 cm thick needle, 0.1-6.0), all plus or minus 10%. The page does not say which sensors come with a rental: ask for RK-3 or TR-3. Trigger: the home rig does not repeat DOWSIL 340 within 15% by Fri 16 Oct.
- **Zinc oxide powder (ZN-601)**
  - Vendor: Atlantic Equipment Engineers
  - Price: Quote only
  - Lead time: In stock
  - Link: <https://micronmetals.com/product/zinc-oxide-powder/>
  - Note: Opened. Excluded by the reviewers. Do not order.
- **Aluminium nitride powder (AL-501)**
  - Vendor: Atlantic Equipment Engineers
  - Price: $146.73/lb at 1-2 lb
  - Lead time: In stock
  - Link: <https://micronmetals.com/product/aluminum-nitride-powder/>
  - Note: Opened. Excluded by the reviewers. Do not order.
- **Planetary vacuum mixer (MTI MSK-PCV-300-LD)**
  - Vendor: MTI Corporation
  - Price: Quote only
  - Lead time: Not stated
  - Link: <https://mtixtl.com/products/msk-pcv-300-ld>
  - Note: Opened: 90 kg, 208-240 V. Capital equipment; outside this step.

## Do not buy

- Clamp with load cell and display: I could not read product pages on this site and found no single verified part. With shim hard stops the load only has to seat the bars. For the first build use a fixed dead weight on a guided insulating block and record its mass; add a load cell only if remount scatter points at load.
- Rotational viscometer (NDJ-8S): Not re-opened. DOWSIL 340 is listed at 542,000 mPa.s (Dow page, opened) and MX-4 at 31,600 poise (Arctic page, opened), at or beyond this instrument's range. Do not buy; the squeeze-spread test stands in.

## Hard limits

- Open powder only over the tray with the respirator on. Spoon it into the oil; never pour from height. Clean up with damp wipes only. Two steps in [EXPERIMENTS.md](EXPERIMENTS.md) depart from this: adding oil to dry powder, and pouring powder through a funnel into a cylinder. Neither is done unless the handling review (checklist G1b) gives a written yes to that step by name. This exception was proposed on 7 October 2026 and is not yet approved by the owner or a reviewer; until it is, the limit stands as written.
- Boron nitride stays sealed until a person has cleared the ventilation line on its data sheet and the supplier has confirmed the particle size of the lot.
- Nothing goes down a drain.
- Everything that touched the reference paste (DOWSIL 340, which is 59 to 79% zinc oxide) goes in its own labelled tub.
- Oily wipes go in a closed container, not a loose pile.
- Rig hot face at or below 80 °C. Current limit set, a thermal cut-out in series with the heater, a non-combustible base, and never left powered unattended.
- No aluminium nitride, no metal powders, no nano grades, no loose zinc oxide.

### Things only a person can do

- Confirm respirator type and fit (a fit check by an occupational health provider; the listed size is a guess).
- Look over the heater wiring before first power-on (someone with electronics experience).
- Clear the boron nitride ventilation question (the supplier or an industrial hygienist).
- Tell the disposal route about the zinc oxide paste and the two figures in the safety notes below.
- Call LongWin and make the booking.

### Safety notes from the data sheets

- Boron nitride, exact product (M.K. Impex data sheet for MK-hBN-xxx, revised 01/03/2020, opened: https://lowerfriction.com/content/SDS%20MK-hBN-xxx%20new.pdf). It is not classified as hazardous and lists reproductive toxicity as 'no data available', so an earlier draft's worry about a reproductive classification does not appear on this sheet; 'no data' is not a clearance. The sheet also says 'Use mechanical exhaust or laboratory fumehood to avoid exposure' and 'Provide appropriate exhaust ventilation at places where dust is formed'. A home bench has neither. This is the same kind of open question that counted against copper, and none of the three judges saw it. Boron nitride stays sealed until the supplier or an industrial hygienist tells the person what is acceptable at home.
- Same boron nitride sheet: it describes the form as 'powder, nano particles'. It is one generic sheet for the vendor's whole range, including nano grades, while the product is sold as 5 micrometre average. The reviewers ruled out nano grades; ask the vendor for the particle-size distribution of this lot before opening it. The sheet also says 'the chemical, physical, and toxicological properties have not been thoroughly investigated'.
- Same sheet, respirator and clean-up: it says respiratory protection is 'not required' and suggests N95 for nuisance dust, and it says to 'Sweep up and shovel' spills. An earlier draft's P100 half-mask and damp-wipe rule are stricter; keep them. The alumina sheet supports the damp-wipe rule ('Do not dry clean dust covered objects and floors').
- Alumina, exact product (Atlantic Equipment Engineers data sheet for AL-602/603/604/605/610/612, opened: https://drive.google.com/file/d/1u1kXo9a-jdLvaacGNPTszO_1IQEFNoXS/view). An earlier draft quotes only the OSHA limits (15 mg/m3 total, 5 mg/m3 respirable; confirmed at https://www.cdc.gov/niosh/npg/npgd0021.html, opened). The product sheet also lists a much lower guideline, TLV 1 mg/m3 as respirable aluminium, states 'May cause damage to organs through prolonged or repeated exposure', and says 'Use only in well ventilated areas' and 'Suitable respiratory protective device recommended' without naming a type. A person must choose the respirator type; the sheet does not.
- The same alumina sheet does not list AL-611, the fine grade, and the AL-611 product page has no data sheet link (https://micronmetals.com/product/aluminum-oxide-powder/, opened). The fine grade is the dustier one. Get its own sheet before opening it.
- Alumina disposal: the sheet says both 'Smaller quantities can be disposed of with household waste' and 'Residual materials should be treated as hazardous'. These conflict; the person's disposal route decides, not the sheet and not a model.
- DOWSIL 340 (Dow data sheet, issue date 07/02/2026, version 8.0, opened: https://webaps.ellsworth.com/edl/Actions/GetLibraryFile.aspx?document=3071&language=en). Zinc oxide is 59-79% of the paste. An earlier draft called the aquatic hazard a search result; the sheet states it directly: zinc oxide is 'very highly toxic to aquatic organisms on an acute basis', 'DO NOT DUMP INTO ANY SEWERS, ON THE GROUND, OR INTO ANY BODY OF WATER', and transport class UN 3077, class 9, marine pollutant.
- DOWSIL 340 waste in California: the state's table of persistent and bioaccumulative toxic substances lists 'Zinc and/or zinc compounds' at 5,000 mg/kg total and 250 mg/L soluble (22 CCR 66261.24, https://www.law.cornell.edu/regulations/california/22-CCR-66261.24, opened). A paste that is 59-79% zinc oxide is far above 5,000 mg/kg. I am not the authority on classification; give these two numbers to the disposal route and keep every wipe, cup and glove that touched DOWSIL 340 in its own labelled tub. Amount in two weeks: well under 100 g of paste plus wipes (estimate).
- Heated paste and the respirator: the DOWSIL 340 sheet says 'Vapor from heated material may cause respiratory irritation', lists formaldehyde among decomposition products, and says that when handling at elevated temperature without sufficient ventilation one should use an air-purifying respirator with an 'Organic vapor cartridge'. A P100 filter is a particle filter. An earlier draft's hazard list has no entry for vapour from the heated rig. Run the rig with real ventilation and a low hot-face temperature, and have a person decide whether an organic-vapour cartridge is needed.
- Silicone oil: the vendor page has no data sheet link and says to 'Refer to the SDS' (https://sciencekitstore.com/silicone-fluid-1000-cst, opened); request it. A data sheet for the same substance from another maker (Clearco PSF-1,000cSt, CAS 63148-62-9, dated 15 Oct 2014, opened: http://www.clearcoproducts.com/pdf/msds/pure-silicone/MSDS-PSF-1,000cSt%20Pure%20Silicone%20Fluid.pdf) says 'When heated to temperatures above 150 degrees C in the presence of air, product can form formaldehyde vapors'. Add a hard limit an earlier draft lacks: the home rig's hot face is set at or below 80 C, and LongWin (whose tester reaches 180 C) is asked to run at 80 C or below.
- Same Clearco sheet: spills 'even in small quantities, may present a slip hazard'. An earlier draft marked the slip hazard as its own observation; it is now sourced. The sheet adds a point an earlier draft misses: 'Dispose of saturated absorbent or cleaning materials appropriately, since spontaneous heating may occur'. Oil-soaked wipes go into a closed container, not a loose pile; confirm the container with the disposal route.
- Flash point: the vendor page gives '> 314 C' for the 1000 cSt oil; the Clearco sheet gives above 120 C closed cup and above 250 C open cup. Use the lower figure until the vendor's own sheet arrives.
- Respirator fit: OSHA's rule for workplaces requires a medical evaluation and a fit test before a tight-fitting respirator is used (29 CFR 1910.134 (e) and (f), https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.134, opened). The rule binds employers, not a person at home, but it is the standard that 'a person confirms fit' should mean: a fit test by an occupational health provider, not a model's or a listing's say-so. The size I listed (medium) is a guess.
- Heater runaway (my calculation, not from an authority): one 40 mm aluminium block holds about 63 J per kelvin. If contact or cooling is lost, 20 W raises it about 19 C a minute and 40 W about 38 C a minute, so it passes 150 C in roughly 4-7 minutes. The heater and the $35 supply are hobby parts with no safety listing that I saw. Set the current limit, fit a thermal cut-out, never leave it powered unattended, and have a person with electronics experience look at the wiring before first power-on.
- Isopropyl alcohol: neither an earlier draft nor I opened a data sheet. Read the one for the bottle bought and keep it away from the heater.
- Not checked by me: the Materion aluminium nitride sheet and the aluminium metal powder sheet cited in an earlier draft. Both materials are excluded, so nothing depends on them.

## Day by day to the first gate

### Tue 6 Oct

1. Make the three lab quote calls using CALLS_AND_ORDERS.md. Request staffed multiple-thickness testing, quantities and data/publication terms. Target sample readiness around 15 Oct and results by 23 Oct, conditional on preparation. Ask for both full scope and a useful reduced scope if the quote exceeds the initial $1,000 target.
2. Place the first cart from CALLS_AND_ORDERS.md to your own address after delivery confirmation. Request applicable SDSs and existing lot records. Confirm SkyGeek stock and any dispatch surcharge. Defer the thermal-rig assembly until design review.
3. Decide who drills and faces the two aluminium blocks: makerspace, friend, or buy the drill press.
4. Save the data sheets already available: alumina (AL-602), boron nitride, DOWSIL 340.
5. traj.py rehearsal, session 1: two runs of any quick measurement, prediction logged before each.

**Done when:** LongWin's answers, or a named person and a callback time, are written down. Every order has a confirmation with a delivery date; any item with no date before Sat 10 Oct is listed. Drilling route is chosen. Three data sheets are saved. Rehearsal has two runs with predictions first.

### Wed 7 Oct

1. Read the data sheets. Write the one-page procedure and hard limits: powder opened only over the tray with the respirator on; spooned into oil, never poured from height; damp wipe only; boron nitride stays sealed until a person clears its ventilation line; nothing down a drain; DOWSIL 340 waste in its own tub; oily wipes in a closed container; rig hot face at or below 80 C; heater never unattended.
2. Person-only tasks: arrange a respirator fit check; send the boron nitride ventilation question to the supplier or an industrial hygienist; tell the disposal route about the 59-79% zinc oxide paste.
3. Cold desk test: 15 paste items (recipes with density, mixing class and spread to predict, plus LongWin conductivity for DOWSIL 340 and the control), three models, replies saved verbatim with model versions.
4. Rehearsal session 2: one run repeating a session-1 condition. Run `verify`.
5. Unpack the balance; check it with the 100 g and 500 g weights.

**Done when:** Procedure is saved. 45 predictions are stored. `verify` passes on the rehearsal with one cross-session repeat. Balance reads both weights within 0.03 g, three times each.

### Thu 8 Oct

1. Write the one-page task card: inputs (recipe fields), outputs (mixing class, density, spread diameter; thermal impedance later), metric.
2. Write the analysis script and test it on LongWin's published grease example.
3. Set up the bench: tray, labels, waste tubs, draught shield, photo stand with scale. Find the density cup's volume from five water fills.
4. `init` the campaign with the goal text.
5. If only stopgap oil and no record-lot materials are in hand: at most three practice batches, logged as rehearsal with their own _lot, timing every step.

**Done when:** Script returns 2.72 W/mK and 0.434 C-cm2/W. Task card is saved. The five cup volumes agree within 0.5%. The campaign exists and `verify` passes on it.

### Fri 9 Oct

1. Record LongWin's answer; phone again if there is none.
2. If the record-lot alumina and oil have arrived: first shakedown session. DOWSIL 340 density and spread first, then the control at 40 vol% and one batch at 30 vol%. Plan, then cold and warm predictions, then mix. Three cup fills and two spreads per batch.
3. If they have not arrived: write down which parcel is missing and its tracking date, and do the rig's cutting and drilling instead.

**Done when:** Either three batches are logged with predictions first and the DOWSIL 340 density reads within 5% of 2.0-2.1 g/cm3 (my proposed check), or the blocking parcel is named with a date.

### Sat 10 Oct

Shakedown, not counted. Control fresh, plus 50 and 55 vol%. Find where hand mixing stops wetting the powder and log it as a result. Time weighing, mixing, density and spread separately. Settle the spread dose so the control lands at about 30-50 mm. Two hours on the rig if parts are in: face and lap the block ends, seat the thermocouples.

**Done when:** At least eight shakedown batches exist in total. Per-step times are recorded. Within one batch, cup fills agree within about 1% and spreads within about 5%; if not, the cause is written down.

### Sun 11 Oct

1. Control fresh once more plus any repeat needed.
2. Freeze in writing: the timed mixing protocol, the control recipe, the spread dose, the cup-fill method.
3. Write the gate schedule: 12 controls and the four alumina-only extremes made twice, in random order across three days, each with _session, _lot and _chosen_by=schedule. Run `anchor`.
4. Log cold and warm predictions for every gate run.

**Done when:** About 12 shakedown batches in total. A note entry holds the frozen protocol and recipe. The anchor hash is in anchors.log. Every gate run has two predictions and no outcome.

### Mon 12 Oct

Gate session 1. DOWSIL 340 density and spread first. Four fresh control batches and extremes 1 and 2, in the anchored order. Raw photos and balance readings attached. Keep one control cup, lidded and labelled, as a LongWin sample. Afternoon: assemble the rig stack if parts are in.

**Done when:** Six runs are logged with action, observation and raw files. The reference is inside its shakedown range. Any failed batch starts with its cause class.

### Tue 13 Oct

Gate session 2. Reference first, four fresh controls, extremes 3 and 4. Afternoon: compare all thermocouples in one stirred water bath at room temperature and near 60 C; record the offsets. A person looks over the heater wiring before first power-on.

**Done when:** Six more runs are logged. Thermocouple offsets are recorded and agree within 0.1 C after correction. The wiring review is noted with the reviewer's name.

### Wed 14 Oct

Gate session 3. Reference first, four fresh controls, all four extremes made again fresh. Keep a second control cup (a different day from Monday's) and one extreme for LongWin. Rig: first powered run on DOWSIL 340 at a 200 micrometre shim gap, current limit set, attended throughout; measure time to steady state.

**Done when:** Twelve controls across three days and each extreme made twice on different days. Settling time is recorded, or the reason the rig did not run is.

### Thu 15 Oct

LongWin day if a slot was offered (otherwise whichever weekday they gave; the displaced bench work moves to Fri or Sat). Log model predictions for each LongWin number beforehand. Measure DOWSIL 340, control from Monday, control from Wednesday, one extreme if time allows. Time each material. Take the raw Excel files. If there is no slot this week: rig commissioning with neat oil and a glass slide instead.

**Done when:** Raw files are attached in traj.py with the real hours per material and the real fee. Or a decision entry states that the LongWin part of the gate is pending, with the booked date.

### Fri 16 Oct

Rig commissioning: ten separate mounts of one paste (DOWSIL 340) at 200 micrometres; three mounts of neat oil; one glass slide. Compute the remount scatter. Decision: if DOWSIL 340 does not repeat within 15%, the person enquires about the needle-probe rental (RK-3 or TR-3 needle) for the following week.

**Done when:** Remount scatter is computed and logged as exploration. A decision entry says 'rig continues' or 'rental enquiry made'.

### Sat 17 Oct

Analysis only. For density and spread: day-to-day scatter of the 12 controls; range across the four extremes divided by that scatter; within-batch scatter. Cold and warm model error against the measured values for each label. LongWin: DOWSIL 340 against 0.67 W/mK and the two controls against each other. Catch up any displaced session.

**Done when:** One table exists: label, within-batch scatter, day-to-day scatter, extreme range, ratio, cold model error, warm model error.

### Sun 18 Oct (first gate)

Decide and log. Pass needs all of:
(a) control scatter across the three days at or below 2% for density and 7% for spread;
(b) extremes differ by at least 3 times the repeat scatter on two labels;
(c) the selected reference lab's QC and uncertainty are documented, and the independent controls are assessed under matched conditions against the proposed 10% repeatability threshold; the datasheet's typical DOWSIL value is context, not a certified calibration threshold;
(d) cold model error exceeds repeat scatter on at least one label.
If (c) has not happened yet, the decision is 'process labels pass, anchor pending'. Fail on (a) or (b): one week on technique and re-test on 25 Oct; fail again: copper. The home thermal label is judged on 25 Oct, not today. Run `anchor`.

**Done when:** A decision entry states pass, pending, one more week, or stop, with the four numbers beside their thresholds, and the anchor is written.

## Second gate, Sunday 25 October

The home thermal rig is judged here: control scatter at or below 10%, and the same ranking as LongWin on the shared samples. If the rig does not repeat the reference paste within 15% by Friday 16 October, the fallback is a rented needle-probe instrument for a week, not a slipped schedule.

## What would send this back to copper

- LongWin refuses an unaffiliated beginner, has no slot before about 26 October, or costs far above the cap, **and** neither the home rig nor the rented probe gives a repeatable thermal number by 25 October.
- Control batches mixed on different days cannot be made to agree after a week on technique.
- Three models' predictions made without any campaign history already fall inside the day-to-day scatter on every label. Then there is nothing to measure.
- Fewer than three fully logged batches per bench day in week 2.

## Not verified

- LongWin's fee, hours, booking lead time and whether a first-time visitor may run the tester.
- The home rig is a design drawn up for this plan, not copied from a validated build.
- Several small items were seen only in search listings, and shipping costs are estimates.
- Whether hand-mixed batches repeat well enough is exactly what the first gate tests.
