# Materials and preparation — the next actions

Updated **4 October 2026**. This is a proposed small bill of materials and work list, not a placed order. **Sourcing inquiries and preparation can run in parallel with Stanford registration.** Registration need not finish before a supplier discusses availability; final purchases require accepted specifications and a receiving plan.

## Small bill of materials

Quantities are our proposed initial scope, subject to the operator's review. AlN is produced in the sputtering tool; we are not buying AlN powder or a bulk AlN ceramic.

| Item | Initial quantity / specification | Source and next action | Buy/release when |
|---|---|---|---|
| Research substrate | **Two matching wafers recommended; quote quantities 1, 2 and 3.** Si(100), polished deposition face, approximately 14 nm thermal SiO2. Use W01 for initial coupons and preserve W02 as spare/future stock. 100 mm is a quotation starting point, not final holder approval; coupon yield is unconfirmed | First ask Stanford about suitable stock. In parallel, use the [prepared supplier request](materials-supplier-evidence.md) for exact-thickness and available-stock options | Fabricator and thermal analyst accept the offered stack, wafer/coupon dimensions, thickness evidence and arrival date |
| Carrier wafer / holder | **One accepted carrier** if using coupons; Lesker manuals describe full 4- or 6-inch substrates | Ask trainer to identify facility stock, material, size, mounting and temperature implications. Do not assume the research wafer and carrier are interchangeable | Staff select the actual mount; no speculative custom-holder purchase |
| Coupon preparation | Cutting enough area for A/B and optional C, with traceable parent positions | Quote supplier cutting versus trained facility preparation. Decide before/after-deposition cutting with both providers | Holder size, cleanliness route and surface protection are agreed |
| Sample containers | **Three labeled coupon cases**, plus the supplier's whole-wafer shipping case | Prefer facility/measurement-provider cases. If unavailable, qualify a commercial carrier with the receiver | Coupon size and surface-contact/removal requirements are known |
| Handling and notes | **One appropriate clean tweezer and one approved notebook**, only if not already provided; compatible outer labels | Stanford stockroom/onboarding first. Use approved paper/device in the cleanroom | Staff specify what the user should own; no generic cleanroom kit needed in advance |
| Sputter materials | Facility-approved **Al target, Ar and N2**, approved mounting/cleaning consumables | Facility supplies; confirm current installed target, condition and charges | Part of the selected run/tool scope; do not separately buy cylinders, chemicals or an AlN target |
| Thermal transducer | **One coating service** on primary coupon A; nominal 80 nm Al subject to analyst approval | Prefer the thermal provider, with thickness evidence included | Thickness/texture work finished and transducer requirements accepted |
| Calibration reference | **Only if required by the chosen thermal analyst** | Have that provider identify/supply the reference and coordinate coating | Included in its accepted measurement plan and quote; a spare research coupon is not automatically a calibration reference |

Sources for facility supplies and carrier requirements are in [lab-preparation-evidence.md](lab-preparation-evidence.md). A and B both receive AlN in the same deposition; **B remains without the Al transducer**, rather than remaining a bare oxide substrate.

## Substrate decision to make this week

1. **Request exact 14 nm first**, preferably existing inventory or a shared oxide run. No exact-stock item, custom price or delivery has yet been confirmed.
2. **Get a specific stock alternative at the same time.** UniversityWafer's [ID 3970 page](https://buy.universitywafer.com/products/100mm-thermal-oxide-wafer-id-3970) currently shows **$48.40 each, 25 available**, 100 mm Si(100), 500 µm, SSP, 1–10 Ω·cm. An indexed catalog description associated it with **22.5 nm oxide**, but the live product page and product-data description do **not** confirm oxide thickness. Get written lot confirmation before calling this a qualified thin-oxide alternative. Price excludes optional cutting, measurement, shipping and tax.
3. **Use another supplier if quantity/timing is better.** RVM's [PRD1025](https://shop.roguevalleymicrodevices.com/shop/prd1025-100a-dry-thermal-oxide-5491) is a real **10 nm dry-oxide** product, but its online format is a **25-wafer lot for $1,773.75** with ±30% oxide tolerance. Request split quantities of one, two and three plus actual thickness evidence; do not purchase the full lot as the default. WaferPro is another custom source, also subject to its published 25-wafer batch minimum or an exception.
4. **Review any substitute with the analyst.** A nearby oxide thickness may be appropriate for this adapted pilot. That is a design decision to record, not an invisible substitution or a reason to improvise an oxide-thinning process. Keep the original approximately 14 nm baseline until a revised stack is accepted.

For October 8–12 receipt, obtain a written dispatch date, shipping service and cutting/certification timing. “Available” is not a held wafer, and dispatch is not arrival. Ask about undiced delivery as a separate option, because cutting may govern lead time. Detailed supplier contacts, evidence and inquiry wording are in [materials-supplier-evidence.md](materials-supplier-evidence.md).

## Packaging source if the labs cannot supply cases

[Ted Pella's semiconductor carriers](https://www.tedpella.com/storage-boxes-bags_html/semiconductor-storage.aspx) cover whole circular wafers. As a price benchmark, product **1395-40** is a 100 mm single-wafer carrier sold in a **pack of ten for $204.45**; that is not a $20.45 one-case purchase and is not a confirmed coupon holder. Prefer a supplied case to buying an unnecessary ten-pack.

[Gel-Pak Gel-Boxes](https://www.gelpak.com/gel-box/) immobilize pieces by backside contact; compatibility and retention need selecting for the actual specimen. A [vacuum-release tray](https://www.gelpak.com/wp-content/uploads/2022/10/2019_Gel-Pak_8_Page_Brochure_RevB.pdf) requires a suitable release arrangement and is not interchangeable with every gel box. Ask the receiving lab which product it accepts. Do not place the measured film face against gel, foam or tape unless the measurement provider explicitly approves that preparation.

These are fallback sources, not recommended purchases yet. Obtain the receiver's packing instructions before dispatch, maintain parent/coupon IDs and include a contents manifest.

## Preparation already completed

The [repeat and expansion plan](repeat-and-expansion-plan.md) explains the revised two-wafer recommendation and optional follow-on runs. Extra inventory does not authorize extra deposition or measurement charges.

- [x] Defined the first-cycle stack and coupon roles, with unknowns separated from paper values.
- [x] Prepared a [human-readable run and handoff sheet](lab-traveler-template.md), including planned versus observed settings, temperature evidence, deviations and outcomes.
- [x] Reserved a consistent naming convention: ALN-001-W01 parent wafer, R01 deposition, A/B/(C) specimens. All are **planned**, not physical samples.
- [x] Created the local `private-records/cycle-001/` workspace with folders for administration, substrates, deposition, structural measurements, transducer, thermal data, analysis, handoffs and closeout; copied the empty JSON record template.
- [x] Added a Git ignore rule for that working-data folder and verified it. This prevents ordinary accidental staging; it is not encryption or a backup.
- [x] Prepared actual supplier questions and a shortlist of laboratory reading, handling and carrier requirements.

## Work to finish before the first lab session

| Action | Owner | Evidence of completion |
|---|---|---|
| Obtain substrate availability and total delivered quotes | User authorizes contact; AI prepares/compares | Exact specification, quantity, lot evidence, price and committed delivery |
| Confirm installed Al target, approved recipe and carrier | Stanford trainer + user | Staff response and selected tool/recipe/mount |
| Confirm useful measurement of the offered stack | Thermal analyst | Accepted dimensions and layer-input/sensitivity plan, including transducer/reference ownership |
| Read selected tool and handling manuals; complete actual qualification | User | Personal training records; AI can explain concepts and prepare notes |
| Agree what instrument files can be exported | User + trainer/providers | Example file types/units and named owner for native data, exports and fit inputs |
| Rehearse the record workflow using dummy labels | User + AI | Every mock sample and file can be traced; rehearsal material clearly marked synthetic and kept separate |
| Choose approved private backup storage | User | Location and successful restore/check of a harmless dummy file; no third-party upload assumed |
| Arrange delivery/collection and sample return | User + providers | Named receiving contact, actual address, appointment/cutoff, packing instructions |

Keep materials/oxide/cutting within the existing **$1,000 substrate-preparation allowance** unless the complete budget is revised. Containers/transport are already within the miscellaneous allowance; do not add them above the $15,000 ceiling. Published prices are reference points, not an accepted order.
