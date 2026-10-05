# First AlN cycle: source, register, prepare

Prepared **4 October 2026**. Working decision: **California; solo hands-on access at nano@stanford first; specialist testing elsewhere if needed; $15,000 total ceiling; desired completion before 25 October 2026.** These are planning constraints, not spending authorization. No application has been submitted, vendor contacted, sample ordered, or slot booked.

**Next action: resolve the Stanford applicant/billing entity and submit a truthful feasibility/intake request.** The live organization intake has been inspected. It requires organization details, a financial contact, a service agreement and a blanket purchase order of at least $10,000. It has no individual category. An unaffiliated-person route needs an answer from administration; do not invent an affiliation. [Stanford external access](https://nanolabs.stanford.edu/access/external), [live intake](https://app.smartsheet.com/b/form/019f3dfdaaee79419f917c0435fef40a).

**Parallel action: source materials and prepare the record workflow now.** The [materials order checklist](materials-order-checklist.md) lists proposed quantities, actual supplier listings, a carrier/handling plan and preparation completed. Supplier availability requests can proceed once contact is authorized; they do not depend on a completed Stanford account. Final orders still require approved dimensions and stack. The [lab traveler](lab-traveler-template.md) and local Git-ignored working-data folders are ready.

**Inventory revision:** request prices for one, two and three matching wafers; two is the recommended starting inventory, with the second held as spare/future stock. Quote a separate deposition repeat as an option, without adding it to the first-cycle commitment. [Independent repeats and additional papers](repeat-and-expansion-plan.md).

## The first purchase is an executable workflow

Aim for **one documented deposition, not an optimization campaign**: one agreed reactive-DC AlN recipe; two or three same-run Si(100)/approximately 14 nm thermal-SiO2 coupons; nominal 200 nm AlN; measured thickness and crystallographic alignment; an accepted Al transducer; TDTR on one coupon at three locations. Obtain measurement-provider acceptance before making the film. All sizes, tolerances and the actual recipe remain subject to technical review. [Detailed scope](research-scope.md).

The deliverable is the specimen plus its linked recipe, execution notes, raw scans, thermal traces, fit inputs and uncertainty. Poor material performance remains a valid outcome. This cycle establishes a usable collection workflow; it cannot establish the benefit of expanded archives or model-training value. Several coupons from one deposition are not independent experiments.

## Route and fallback

| Role | First route | Backup | Condition that must be answered |
|---|---|---|---|
| Deposition and learning | nano@stanford; discuss Lesker 1/2 with staff, then complete training | Hionix, San Jose; Utah staff service if California cannot accept | Is there an executable low-temperature reactive-DC recipe, an available Al target, suitable holders, and a slot? |
| Thickness, alignment and thermal measurement | Ask Covalent, Sunnyvale, to quote a coordinated XRR/XRD/TDTR package | Microsanj, Fremont, for thermal testing; Stanford/Covalent for structural work | Can the exact stack be measured with useful sensitivity, and can the required raw records be supplied? |
| Substrates | Selected fabrication facility supplies approved material | UniversityWafer custom quote; WaferPro only if minimum order is suitable | Approximately 14 nm thermal oxide, dimensions accepted across tools, actual thickness evidence, delivery date |

The Stanford tool listings establish Al and reactive nitrogen capability, not a validated high-conductivity AlN recipe. The paper used an AJA system, so a Lesker experiment would be an **adapted pilot**, not an exact reproduction. Hionix advertises AlN but has unconfirmed process/record-release details. Covalent advertises all three measurements, but a combined job and this stack are not yet accepted. [Fabrication evidence](research-us-fabrication.md), [measurement and substrate evidence](research-metrology-and-materials.md).

## Work one card at a time

| Card | Owner | Done when | Status |
|---|---|---|---|
| 01 — Applicant identity | You, assisted by AI | Legal applicant/entity, application name and email confirmed; individual eligibility queried if needed | **Needs your input** |
| 02 — Stanford feasibility | You + Stanford staff; AI prepares text | Staff identify tool, permissible recipe, current target and feasible access/training path | Draft ready |
| 03 — Thermal feasibility | You + testing provider; AI compares responses | Exact stack, dimensions, transducer owner, sensitivity and records accepted; dated quote | Draft ready |
| 04 — Select route by Oct 7 | You; AI assembles decision | A dated fabrication-to-testing path fits budget; otherwise activate paid backup or revise completion date | Pending replies |
| 05 — Complete registration/training | You + Stanford | Approved account, signed documents, required training and actual tool authorization | Intake inspected only |
| 06 — Buy approved substrates | You/fabricator | Correct stack and dimensions received with provenance; no unapproved substitution | Wait for 02–04 |
| 07 — Book bounded work | You + providers | Setup, training, run, metrology, data and contingencies fit a written stop-work limit | Unquoted |
| 08 — Run and record | You after qualification, or agreed operator | One run logged; sample IDs and deviations preserved | Not started |
| 09 — Measure and transfer | Providers + you | Thickness/texture before transducer; thermal result or documented inconclusive result | Not started |
| 10 — Close out | You + AI | Linked file package, assumptions and cost summary; next experimental decision stated | Not started |

## The deadline is conditional

The preferred route has sequential gates: account → safety/orientation → tool training → deposition → characterization. Stanford says account setup can take up to ten business days; thermal services elsewhere advertise roughly two to three weeks after sample receipt. Therefore October 25 cannot be treated as a reliable end-to-end completion date today. We need short, confirmed slots or an expedited commercial route. [Stanford account timing](https://nanolabs.stanford.edu/access/external/purchase-order), [Allen access sequence](https://nanolabs.stanford.edu/equipment/allensafety), [Microsanj turnaround](https://microsanj.com/advanced-packaging-3dhi/).

**October 7 is our decision checkpoint**, not a facility deadline: if there is no credible dated path, choose between paid fabrication while Stanford onboarding continues, or completing a documented intermediate milestone by October 25. Do not call an unfinished thermal measurement a completed cycle. [Dated schedule and budget controls](procurement-and-schedule.md).

## Working documents

Keep this README as the entry point. Use the following documents for current decisions; the research files retain supporting evidence and unverified leads.

| Decision or activity | Document to maintain |
|---|---|
| Quantities and material readiness | [Materials order checklist](materials-order-checklist.md) |
| Dates, budget and booking gates | [Procurement and schedule](procurement-and-schedule.md) |
| First-run technical requirements | [Experimental scope](research-scope.md) |
| Optional repeat runs and other papers | [Repeat and expansion plan](repeat-and-expansion-plan.md) |
| Applicant information and registration steps | [Stanford registration](stanford-registration.md) |
| Outbound message drafts | [Facility/testing inquiries](inquiry-drafts.md) and [current substrate request](materials-supplier-evidence.md) |
| In-lab recording | [Human-readable traveler](lab-traveler-template.md) and [JSON template](run-record-template.json) |

Supporting research and preparation:

- [Materials order checklist](materials-order-checklist.md), [supplier evidence](materials-supplier-evidence.md), [lab preparation evidence](lab-preparation-evidence.md) and [run/handoff sheet](lab-traveler-template.md).
- [Stanford registration worksheet](stanford-registration.md): actual forms, missing fields and ready project description.
- [Inquiry drafts](inquiry-drafts.md): administration, tool feasibility, commercial fabrication, measurement and substrate requests. Nothing sent.
- [Procurement, schedule and budget](procurement-and-schedule.md): ingredients, who supplies them, when to order, decision dates.
- [Technical scope](research-scope.md): coupon roles, measurement requirements and stop conditions.
- [Fabrication sources](research-us-fabrication.md), [metrology/materials sources](research-metrology-and-materials.md), [Taiwan backup](research-taiwan.md).
- [Run-record template](run-record-template.json): empty record structure, not experimental data.

Personal registration details, signed agreements, quotes and vendor files should live outside this public repository unless deliberately cleared for publication. These preparation files contain public research and unsubmitted drafts. The earlier [public-record audit](../aln-public-record-audit/README.md) remains separate; its human source review is still pending.
