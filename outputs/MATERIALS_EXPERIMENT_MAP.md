# Materials experiments and Bay Area laboratory access

Updated 12 October 2026. This is the overview for choosing the next physical experiment. The common research objective is to connect preparation history with measured material performance, then test whether that additional history improves a prediction or experimental decision. A relevant material and an attractive measurement do not by themselves establish dataset value.

**Recommended near-term program: thermal-interface performance plus flow and stability measurements using the materials already owned.** Investigate copper plating and diamond access in parallel at the quotation stage. Wafer films and diamond growth remain separate specialist projects. This overview organizes the alternatives; it does not initiate them or replace an approved run card.

## Existing materials and completed work

For Taiwan alternatives to California wafer fabrication, see [Taiwan fabrication access and costs](copper-access-review/taiwan-fabrication-access.md): TSRI, NYCU, NTHU and NTU, including independent-user limits, published commercial fees and scheduled TSRI practical courses.

| Item | Recorded identity | Useful role |
| --- | --- | --- |
| Coarse alumina | McMaster 5092N124, catalog 45 microns | Ceramic filler |
| Fine alumina | McMaster 5092N131, catalog 4–7 microns | Second filler size for composition/packing comparisons |
| Silicone oil | Super Lube 56404, nominal 1000 cSt | Liquid matrix for non-curing pastes/suspensions |
| Commercial thermal paste | DOWSIL 340 | As-purchased comparison material, not a calibration standard |
| B001 | Completed practice batch and public record | Candidate exploratory specimen if the testing lab accepts its condition and history |

Alumina is **aluminum oxide, Al₂O₃**. It is distinct from aluminum metal and aluminum nitride (AlN). The catalog powder grades do not establish suitability as semiconductor-fab feedstock. The [manufacturer identifies the owned silicone product as PDMS oil](https://www.super-lube.com/product/super-lube-silicone-oil-1000-cst/); a cured pad requires a separately selected reactive resin system.

## Experiment choices

The rows are proposed study directions. “Access route” distinguishes operator-run services from user-operated facilities. No new provider has accepted the project or guaranteed a date.

| Material and added ingredients | Type of experiment and equipment | Goal and tangible output | Most practical paid route | Priority |
| --- | --- | --- | --- | --- |
| **Existing alumina + oil; DOWSIL reference** | Compare thermal impedance at measured thickness, pressure and temperature using a D5470-based TIM tester | Determine how well the paste transfers heat between a package and heat sink. Output: measured interface-performance curves linked to batch histories | **LongWin, Livermore:** engineer-run service or researcher reservation. Quote and specimen acceptance needed | **First application measurement** |
| **Same existing ingredients** | Vary one preparation/formulation factor; measure rheology, controlled dispensing/spreading and storage separation. Rotational rheometer, controlled force/dispensing fixture and imaging | Find a paste that both transfers heat and can be applied reproducibly. Output: flow/recovery curves and application/stability records | **Covalent, Sunnyvale:** named rheometer and paste service. **Zikon, Sunnyvale:** preparation/day-bench inquiry; specific tools require confirmation | **Best expansion without new chemistry** |
| **Existing alumina + NEW curable silicone base and curing agent** | Cast solid pad or encapsulant coupons; mixing/degassing, mold, specified curing setup, thermal and compression tests | Study filler loading versus thermal resistance, compressibility and void formation for package cooling/encapsulation | **Zikon** for approved preparation; **LongWin** accepts gap-pad testing, subject to dimensions. **AcmeBay, Palo Alto** is a preparation alternative with unconfirmed short-term terms | **Next material platform if desired** |
| **Existing oil and alumina suspensions** | Low-voltage dielectric spectroscopy with an impedance/LCR analyzer and a suitable liquid/paste cell | Measure permittivity and dielectric loss versus frequency, filler and storage history. Output concerns composite insulation, not a wafer gate dielectric | **No fast local provider/cell verified.** Scope with an electrical-materials specialist before buying equipment; do not substitute a four-point probe | **Optional, access unresolved** |
| **Copper + NEW seeded coupons and approved plating chemistry** | Electroplate copper; measure deposited thickness, roughness and electrical sheet resistance | Relate process conditions to a conductor used in packaging/interconnect fabrication. Output: coated coupons and deposition/measurement records | **Silicon Valley Wafer Plating, Santa Clara:** pilot runs and process teaching advertised. Hands-on participation and dates need confirmation; **Covalent** for selected metrology | **Best new fabrication inquiry** |
| **AlN + NEW oxidized-silicon substrates and facility supplies** | Reactive sputtering, thickness/crystal characterization, then suitable thin-film thermal measurement such as TDTR | Revisit the original question of thermally conductive insulating films made at low substrate temperature. Output: coated wafer pieces and thermal/structural data | **Hionix, San Jose:** AlN film service; **Covalent:** TDTR inquiry. **Stanford:** trained hands-on alternative. Exact process and stack need acceptance | **Commercial service may be faster than training** |
| **SiO₂ or silicon nitride + NEW wafer substrates** | Established PECVD process followed by thickness/uniformity characterization; electrical tests require an appropriate test structure | Learn actual dielectric/passivation-film fabrication. Output: coated wafer pieces; thickness alone does not prove dielectric quality | **Stanford Oxford PECVD**, with account and training; **Berkeley Marvell** backup. Hionix offers sputtered oxide/nitride films if a service specimen is sufficient, but this is a different process | **Useful learning, more onboarding** |
| **Purchased synthetic diamond + specialist surface treatment** | Compare a defined surface-treatment condition with a control; select electrical, wetting or optical measurement around one question | Study how surface preparation affects a chosen property, potentially for electronics or sensors. Output: treated specimens and measured differences | Ask **sp3/Seki** about treatment or referral; **Covalent** has relevant characterization services. **No hydrogen-termination service or complete fast workflow verified** | **Define one question before purchase** |
| **Synthetic diamond grown on NEW compatible substrates** | Diamond CVD, then Raman/microscopy/thickness measurements | Learn growth and relate process to film structure. Output: diamond-coated substrate; optical/structural checks alone do not establish thermal performance | **sp3, Santa Clara:** verified deposition service. **Seki, San Jose office:** demo inquiry; local reactor/visitor access unknown. **Stanford/Berkeley:** qualified shared-tool route | **Service feasible to inquire; hands-on unconfirmed** |
| **Copper + NEW diamond particles and controlled interface coatings** | Composite fabrication, porosity/interface characterization, suitable thermal and expansion measurements | Investigate heat-spreader performance and expansion compatibility with a chip package. Output: composite coupons and measured properties | **No fast local end-to-end route verified.** Published electrodeposition research is a lead, not an available service. Wafer-plating capability does not establish particle codeposition; a commercial plate is only a benchmark specimen | **Later specialist project** |

## Access evidence and timing

| Provider | Published facts relevant to scheduling | What the quote must settle |
| --- | --- | --- |
| [Zikon](https://www.zikon.com/lab.html), Sunnyvale | **$75–150/day** shared bench, scheduled equipment and basic orientation; advertises rheology, microscopy and wet chemistry | Individual admission, exact tools, process permission, supervision, waste and total cost. No CVD reactor verified |
| [LongWin](https://longwinusa.com/services/thermal-interface-material-test/), Livermore | TIM testing and researcher reservations; published typical turnaround about one week. Existing October 6 correspondence is summarized in the private-correspondence-derived status file as approximately one week testing plus one week reporting | Use a project-specific written completion date. Price, accepted specimen/container and data export remain unresolved. Test time of 2–4 hours/material is not booking lead time |
| [Covalent rheology](https://covalent.com/techniques/mechanical-testing/rheology/), Sunnyvale | Anton Paar MCR 302; liquids/pastes; typical **five business days** on the technique page. [General FAQ](https://covalent.com/faqs/) gives 5–7 business days for most in-house work and scoped rush options | Quote-only staffed analysis. Choose geometry for the actual particles/paste and confirm sample quantity. Do not assume user operation or apply the generic turnaround to every technique |
| [Silicon Valley Wafer Plating](https://www.waferplating.com/), Santa Clara | Small pilot runs, copper plating and process teaching | Quote, date, independent-customer acceptance, supervised participation and shareable process records |
| [Hionix films](https://hionix.com/pvd-films/), San Jose | Lists AlN, Al₂O₃, SiO₂, silicon nitride and metals. Majority of standard film services advertised under ten days; custom R&D can take longer | Exact substrate, temperature/process, characterization, records, total price and date. Film availability is not a promise to reproduce the Stanford paper |
| [sp3](https://sp3-cvd.com/wafers), Santa Clara | Diamond-on-silicon deposition service and standard wafers | Quote/date, custom runs and records. Neither hands-on training nor hydrogen termination is established |
| [Seki](https://sekidiamond.com/about-us/), San Jose office | Advertises R&D/demo facilities and process support | Where the demo reactor is, whether paid beginner sessions exist, and whether non-purchasing individuals are accepted |
| [AcmeBay](https://www.acmebay.net/incubator/), Palo Alto | Chemistry services and hood leasing | Day access, project support, tools and price. No published day rate or verified CVD |
| [Stanford external access](https://nanolabs.stanford.edu/access/external) / [Berkeley affiliates](https://nanolab.berkeley.edu/public/membership/affiliate/affiliate.shtml) | Shared fabrication infrastructure with formal account and tool qualification | Individual eligibility and full onboarding. Neither is a verified rapid beginner booking. Current fee details are in the linked access review below |

## Measurement and material boundaries

- [Covalent TDTR](https://covalent.com/techniques/thermal-analysis/time-domain-thermoreflectance-tdtr-analysis/) is a real listed service for thin-film/interface heat transport. Agree on sensitivity, substrate stack and transducer preparation before deposition. LongWin's cited TIM service lists apparent conductivity below 20 W/m·K; do not assume it measures intrinsic diamond or Cu/diamond conductivity.
- [Stanford Oxford PECVD](https://snfguide.stanford.edu/guide/equipment/oxford-plasma-pro-pecvd-ox-pecvd) lists oxide/nitride films. Buying a deposited specimen and learning to operate a reactor are separate services. Likewise, the owned alumina powder is not the precursor for an ALD gate dielectric.
- A [liquid dielectric fixture](https://www.keysight.com/us/en/product/16452A/liquid-test-fixture.html) illustrates the required measurement geometry; this discontinued product is a method reference, not a purchase recommendation. Filled paste suitability must be checked. Breakdown testing is a separate specialist task.
- Commercial [curable electronics silicones](https://www.dow.com/documents/11/11-3472-01-dowsil-tc-4605-thermally-conductive-encapsulant.pdf?iframe=true) establish the application of cured thermal encapsulants. Select a compatible base system for our proposed filler study rather than altering an already formulated commercial product indiscriminately.
- Hydrogen-terminated diamond has applications in [surface electrical conduction](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.85.3472) and [near-surface defect control](https://arxiv.org/abs/1011.5109). Pick the measurement first; these are distinct experiments. Surface analysis such as XPS is not a direct measurement of hydrogen coverage.

## Second check, 12 October: confirmed prices, corrections and additions

Added by a second assistant from an independent check: six researchers gathered options and two fact-checkers opened each provider's page. Nobody was contacted and no quote was requested. This check did not cover Zikon, AcmeBay or Silicon Valley Wafer Plating; their entries above stand as first written.

**The main finding.** Almost no provider says in writing that it takes an order from a private individual. LongWin's and Covalent's request forms both require a company or organisation name. Every route therefore starts with one question: "Do you accept an order from an individual paying by card?"

### Prices and times found on the provider's own page

| Need | Provider | Price | Time | Note |
| --- | --- | --- | --- | --- |
| Heat flow through pastes and pads | LongWin / MyHeatSinks, Livermore | By quote | Typical one week | A self-run half-day or full-day can also be booked; ask for both prices |
| X-ray diffraction of a powder | Lorad Chemical (mail-in) | $115 per sample | 4 to 5 business days from receipt | University of Washington testbeds: $60, time not published |
| Particle size of the two powders | Lorad Chemical | $110 per sample | 4 to 5 business days from receipt | Micromeritics: $385, or 2 to 4 days at +50% |
| Flow curve and yield stress of a paste | University of Washington testbeds (mail-in) | $170 basic, $340 advanced per sample | Not published | Covalent publishes no current price; its 2021 sheet shows $350 an hour and a $750 minimum per job |
| Surface checks at Covalent | Covalent, Sunnyvale | 2021 sheet: contact angle $250, surface chemistry (XPS) $365, diffraction $380 per sample | 5 to 7 business days; rush offered | Old prices, probably higher now; $750 minimum per job |
| Diamond plates | Element Six web store | Heat-spreader plate 10 x 10 x 0.30 mm $160; single crystal 3 x 3 x 0.25 mm $165 | In stock; dispatched within 4 working days | MTI lists a single crystal of the same size at $493 |
| Diamond powder | UKAM | $80 for 20 g of half-micron powder | Not stated | Coarser grades not checked |
| A ready-made film to hold and measure | MTI | 200 nm aluminium nitride on silicon, 10 x 10 mm, $198; thermal-oxide wafer $110 | "Email for lead time" | Comes with a spec sheet, not a run record |
| A film made to order | Hionix, San Jose | By quote | Under 10 days stated for most jobs | Returning the run record is not promised; ask for it in the quote. Silicon Valley Microelectronics also lists reactive aluminium nitride, by quote |
| Staff-run deposition with published rates | Utah Nanofab | Deposition $156 to $170 an hour, staff $150 an hour, $300 set-up | Not stated | Written for businesses |
| Kiln firing | Clay Planet, Santa Clara | $5 minimum | 3 weeks | To about 1290 C; the page covers clay only, and the schedule cannot be chosen |
| Heat flow in thin films or diamond | Laser Thermal (mail-in) | By quote | 2 to 3 weeks, or 3 days expedited | The clock starts after a consultation, a non-disclosure agreement and a proposal |
| Bulk heat conduction of a solid | TPRL (mail-in) | By quote | Not stated | The one test lab whose page says private individuals may order |

### Corrections to earlier notes in this repository

- **Thermal Engineering Associates, Santa Clara,** sells test hardware. No send-in testing service was found, so it is not a backup lab for paste testing.
- **Maker Nexus, Sunnyvale,** lists no kiln, furnace, oven or wet-chemistry area.
- **Stanford's fees changed on 1 September 2026:** $1,500 enrolment and $99 per person per month for a company, plus a retainer and overhead. An organisation must hold the account; set-up takes about 15 business days.
- **Hydrogen termination of diamond:** no company sells it with a price or a date. One research centre in Michigan states the capability as contract research.
- **Electrical insulation tests** are written for solid sheets and discs. Wet paste does not fit; test a cured pad instead.
- **Liquid metal:** no lab states that it accepts gallium.
- **Paste on a diamond plate:** the LongWin tester would see only the paste layers. A 0.3 mm diamond plate is below its measuring floor.

### Three more experiments with the materials already owned

Each mirrors a real step or problem in chip packaging and needs only a home bench.

| Experiment | What one run is | Why it is chip-related |
| --- | --- | --- |
| **Grease reliability** | Oil bleed from a weighed dab on filter paper; weight loss on baking; hot and cold cycling between glass slides to watch the paste creep out | This is how the industry qualifies thermal grease. It needs a small oven used for nothing else |
| **Silicone oil creep** | How far the oil spreads on copper, glass and circuit board over a week, and whether tape, glue and solder still stick afterwards | Silicone oil migrating onto bonding surfaces is a documented assembly problem. It also means silicone work must be kept apart from anything that has to bond or be coated later |
| **Lapping** | Fine alumina in water on a glass plate; mass removed from a copper or silicon piece per 100 strokes at two loads | Wafers are lapped with an alumina slurry after slicing. This is not the later chemical polishing step. Water is a new ingredient and needs the owner's sign-off |

Checked and dropped: firing the alumina into a substrate (the local kiln is far short of the industrial temperature), and silicone oil as a coolant (real products are twenty times thinner than the oil on hand).

## Recommended sequence and navigation

1. Scope **thermal performance plus rheology** as one program using existing ingredients. Choose one formulation or preparation variable; keep references and repeat preparations. Obtain specimen requirements and quotes before making the submission batches.
2. In parallel, request feasibility for **one copper-plating learning session** and **one diamond demonstration or surface-treatment project**. Select the next fabrication track based on a real date, complete cost and useful records.
3. If a solid object is the desired next output, consider **cured alumina–silicone coupons** after selecting the resin and test geometry. New chemistry is optional, not required for the current thermal result.
4. For any track, retain recipes, actual conditions, deviations, repeat runs and raw measurements. Test the added value of those histories prospectively; do not equate more logged fields with better models.

Operational references:

- [Paste completion checklist](thermal-paste-first-cycle/CHECKLIST.md) and [next-batch run card](thermal-paste-first-cycle/PASTE_TO_LAB_RUN_CARD.md).
- [B001 public release](../trajectory/releases/B001/README.md) and [process review](thermal-paste-first-cycle/B001_PROCESS_REVIEW.md).
- [Copper access and quotes](copper-access-review/README.md), [CVD access](copper-access-review/cvd-learning-access.md), [Cu/diamond research](copper-access-review/cu-diamond-research-lead.md).
- [Original AlN preparation](aln-first-cycle-preparation/README.md), including commercial fabrication and metrology alternatives. Its older dates and Stanford-first preference are historical planning context; no booking is created by this overview.

No purchase, outreach, booking or new experimental procedure was executed as part of this reorganization. The experiment records still require the checks in their respective run cards; owning ingredients does not close those checks.
