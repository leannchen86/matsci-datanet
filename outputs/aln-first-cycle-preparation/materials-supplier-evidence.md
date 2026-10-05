# Thin-oxide silicon sourcing: actual listings and quote-ready specification

Checked **4 October 2026** against supplier primary sources. No inquiry, order, reservation or payment has been made. Advertised stock is not held inventory; prices below are listings, not delivered quotations.

**Concrete result:** no exact **14 nm thermal-SiO2/Si(100)** stock SKU was verified. There is a credible custom-quote route, one verified 10 nm product listing and a cheaper stock lead whose oxide thickness requires confirmation. For this adapted workflow pilot, 14 nm is the reference preference, not an automatically inviolable requirement. Any replacement needs the deposition/thermal providers' acceptance, measured oxide thickness and an explicit revised stack in the record.

## Shortlist

| Source and route | Verified material or service | Public price/quantity | Arrival October 8–12 |
|---|---|---|---|
| **UniversityWafer custom** — first exact-thickness inquiry | Custom thin thermal oxide, prototype quantities; published dry-oxide range spans 14 nm | **No 14 nm price or confirmed minimum**; general single-wafer sales do not guarantee a one-wafer custom furnace job | Unverified custom lead time; ask about existing 14–15 nm stock before requesting new growth |
| **UniversityWafer ID 3970** — economical stock lead requiring oxide confirmation | 100 mm Si(100), P-type, 1–10 Ω·cm, 500 µm, SSP. Indexed catalog description says **22.5 nm thermal oxide**, but the current product page omits oxide thickness; this is not yet a confirmed coating specification | **$48.40 per wafer**, current listing shows 25 available; coating thickness/tolerance, grade and wet/dry method need written confirmation | Plausible inquiry for expedited shipment, not confirmed delivery; dicing and certification may add time |
| **WaferPro custom**, San Jose | Dry thermal oxide **10–300 nm**, published target tolerance ±5% | **25-wafer minimum batch**; no exact 14 nm quote or verified stock SKU | Unknown; useful only if stock, a shared batch or a small-order exception exists |
| **Rogue Valley Microdevices PRD1025** — alternative thin-oxide stock | **10 nm dry thermal oxide ±30%**, both sides; 100 mm Si(100), P/B, >1 Ω·cm, 525±25 µm, SSP; film Certificate of Conformance | Store format **25 wafers for $1,773.75** ($70.95/wafer equivalent), not a verified $70.95 single-wafer order | Advertises **shipping in 1–2 days**, not arrival; ask for one-wafer split and confirmed California delivery |

Sources: [UniversityWafer custom oxide](https://www.universitywafer.com/Wafers_Services/Silicon/ThermalOxide.html), [published dry-oxide process range](https://www.universitywafer.com/Wafers_Services/Silicon/thermal_oxide.html), [UniversityWafer stock catalog, ID 3970](https://buy.universitywafer.com/collections/thermal-oxide), [WaferPro oxide specification](https://waferpro.com/silicon-wafers/silicon-thermal-oxide-wafers/), [RVM PRD1025 product](https://shop.roguevalleymicrodevices.com/shop/prd1025-100a-dry-thermal-oxide-5491).

### UniversityWafer: exact custom request plus a specific stock fallback

Use **800-713-9375**, **chris@universitywafers.com**, or the [custom oxide form](https://www.universitywafer.com/Wafers_Services/Silicon/ThermalOxide.html). The current [store contact page](https://buy.universitywafer.com/pages/contact-us) publishes that email. Some other company pages also publish chris@universitywafer.com; using the linked form avoids ambiguity.

The [ID 3970 product page](https://buy.universitywafer.com/products/100mm-thermal-oxide-wafer-id-3970) was successfully checked in the browser: it confirms the current listing, substrate specifications, price and quantity, but **does not display an oxide thickness or a filled product description**. On October 4, searches for `site:buy.universitywafer.com "3970" "225"` and `site:buy.universitywafer.com "22.5NM"` returned the supplier's [indexed catalog](https://buy.universitywafer.com/collections/thermal-oxide), marked crawled two weeks earlier, with ID 3970's description **“225A, 22.5NM, THERMAL WAFER”**. That indexed description is a lead, not verification of the currently offered lot's coating. Request written confirmation of oxide thickness, grade and availability before checkout. Do not substitute another cheap catalog wafer with scratches, haze or an unknown oxide.

UniversityWafer's shipping policy says overnight orders received after **3:30 p.m. Eastern** ship the next business day. That policy is relevant to an accepted stock order, not a promise that custom oxide or dicing can be finished that day. Its custom orders are described as nonrefundable/best-effort, so the written specification and acceptance terms matter. [Store shipping and return policy](https://buy.universitywafer.com/pages/contact-us).

### WaferPro: local, but quantity is the unresolved issue

Use **sales@waferpro.com**, **408-622-9129**, or its [quote form](https://waferpro.com/request-a-quote/). The form has a **Dry Thermal Oxide** selection and film-thickness field in **Å**: enter **140 Å**, not 14, for 14 nm. Request quotes for one, two and three matching wafers or equivalent approved coupons, explicitly asking whether existing stock or a split/shared batch avoids the published 25-wafer minimum. Company details must be truthful; optional company fields do not prove individual-customer acceptance. Listed prices for ordinary polished silicon elsewhere on its site do not price an oxide wafer.

### RVM: actual 10 nm SKU, with two limitations to resolve

Use **sales@roguevalleymicro.com**, **541-774-1900**, or its [quote form](https://roguevalleymicrodevices.com/request-a-quote/). Its [general service policy](https://roguevalleymicrodevices.com/working-with-us/) advertises no minimum order or spend, but PRD1025's actual online purchase format is a 25-wafer lot. Ask for split quantities of one, two and three; do not assume general marketing changes the SKU's checkout quantity. Its custom-oxidation page starts at **50 nm**, while this specific shop product is thinner. The SKU establishes a 10 nm offering; it does not establish exact 14 nm custom growth. [Custom oxidation ranges](https://roguevalleymicrodevices.com/wafer-services/thermal-oxidation/).

The nominal ±30% means a **7–13 nm** advertised range. A Certificate of Conformance may only certify that range; ask whether actual lot/wafer thickness mapping can be supplied. A bare certificate should not silently become a precise 10 nm model input.

## How to choose between exact and nearby oxide

- **14 nm:** request custom pricing and dated delivery, preferably from existing inventory or a shared run. Exact stock remains unverified.
- **15 nm:** a reasonable close alternative to ask suppliers about, but no purchasable 15 nm stock SKU was established in this search. Do not advertise it as available.
- **10 nm:** RVM provides a real listing, subject to its broad tolerance, lot quantity and measurement acceptance.
- **20 nm:** no small-quantity Si(100) stock SKU was verified. One catalog result used Si(111), so it was excluded rather than changing crystal orientation unnoticed.
- **22.5 nm:** ID 3970's indexed description makes it an inexpensive lead, but its current product page omits oxide thickness. First obtain written confirmation that this thickness actually applies to the offered lot. If confirmed, it preserves Si(100), changes oxide thickness and needs measured thickness evidence plus thermal-model approval.

The analytical reason to review a substitute is that oxide thermal resistance and its uncertainty enter the multilayer thermal model. Holding oxide conductivity fixed, oxide resistance scales with its thickness; that simple relationship does not predict how well the full TDTR fit can separate film and interface properties. Ask the analyst whether the **actual offered stack** supports the intended result. A nearby oxide can be appropriate for the adapted pilot; do not label it an exact reproduction. Do not add an oxide-thinning etch merely to make a nominal number match without a separate process decision.

## Quote-ready purchasing description

> Please quote **quantities of one, two and three matching 100 mm Si(100) wafers**, preferably from the same lot and oxide process. Our preferred starting inventory is two. Each wafer should be single-side polished on the intended deposition face, with nominal **14 nm (140 Å) thermally grown SiO2**. We initially need two or three same-run coupons, with usable cutting yield to be confirmed; final dimensions and dicing timing will be approved by our fabrication and thermal-measurement providers. Please state silicon thickness, dopant/resistivity, grade, oxide on one or both sides, growth method, lot identity, oxide-thickness tolerance and available measured thickness evidence. Do not substitute native oxide, deposited oxide, nitride or an SOI wafer.
>
> Please price the wafer, oxide processing if needed, actual thickness measurement/certificate, optional approved dicing, clean packaging, taxes and shipping separately. Requested California receipt is **October 8–12, 2026**; please give a committed ship date and delivery service, with and without dicing. If exact 14 nm cannot meet that window, list existing **10–25 nm thermal-oxide Si(100)** stock with actual thickness/tolerance and prices for quantities one, two and three. Alternatives are for review, not automatic substitution. Please confirm customer eligibility for our truthful applicant status.

For UniversityWafer append: **“Please also confirm ID 3970: the listed $48.40 per wafer and delivered quotes for one, two and three matching wafers. An indexed catalog description calls it 225 Å/22.5 nm thermal oxide, but the current product page does not state oxide thickness. Does 22.5 nm apply to the lot currently offered? Please provide actual coating specification, lot thickness evidence, condition/grade and earliest shipment.”**

For RVM append: **“Please quote one, two and three wafers split from PRD1025, rather than a 25-wafer lot, and clarify whether the certificate includes measured thickness or only the 100 Å ±30% acceptance range.”**

## Prepared action and remaining purchase blockers

The immediate sourcing action is a **two-option quotation**, exact 14 nm and named stock alternative, while Stanford reviews the holder and the analyst reviews the offered stack. It is unnecessary to wait for completed Stanford registration to prepare or, once authorized, send this request. The eventual order still needs a factual ship-to recipient/address, approved wafer/coupon format, accepted oxide/Si input uncertainties, total cost and a real delivery date.

The revised recommendation is **two matching research wafers**, one for initial work and one protected spare/future stock. Request prices for one, two and three; a third needs a specific follow-on use or purchasing advantage. A tool carrier is separate. **25 wafers are not the default**. Facility-stock material remains potentially faster, but no suitable Stanford stock has been verified. No supplier here has committed to October 8–12 delivery, and no ready-to-buy exact-14-nm price is established.
