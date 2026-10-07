# Plan

Updated 7 October 2026. This is the one live plan. The first target is hand-mixed thermal pastes. [outputs/aln-first-cycle-preparation/](outputs/aln-first-cycle-preparation/README.md) is background: it was written for a single careful run at a different budget and is paused, not deleted.

## Decided

- **Goal.** Produce experimental materials data that people who train models would actually want: complete, checkable, with the failures left in.
- **Unit of data.** A trajectory, not a row: goal, plan, what was done, raw readings, interpretation, next decision, dead ends. Format and rules are in [trajectory/](trajectory/README.md). Each run also records a model prediction made without the campaign history and one made with it, so the release can show how much the history helps a model.
- **Expert.** For now an AI model is the expert. It writes a prediction before every run; the measured outcome scores it. A human expert comes later, when there is money and time.
- **Method.** By hand, full time. Speed and learning come before automation or scale.
- **Budget.** About $15,000 for this first step.
- **Release.** The first dataset is given away to test demand. What is public and what is held back gets decided before anything is released, because public data cannot later serve as a hidden test.

## First target: hand-mixed thermal pastes

Changed 5 October 2026. Copper electroplating was the working choice for a few hours; it had been compared only against other copper plans. Once the home bench and LongWin's advertised testing service were identified, both routes were worked up in full and three independent reviewers all chose thermal pastes (about 40 against 30 out of 60). Their confidence is medium. No laboratory slot is confirmed.

**What gets made.** Silicone oil plus ceramic powder, about 25 g per batch, mixed by hand to a fixed, timed protocol. Alumina first; boron nitride later, once a person has cleared its data sheet.

**What gets measured.** On every batch, the same day: mixing class, density (which gives trapped air), and how far a fixed dose spreads under a weight. A home thermal rig is built in parallel and judged a week later. LongWin's tester is the trusted reference for a small subset, two to four samples per booked day. After the pilot, what is made and measured changes; see [Adopted direction](#adopted-direction-experiments-that-test-a-mental-model).

**Why this over copper.** The answer can be checked by someone else: thermal impedance has a standard method and an outside instrument. It stays on heat removal. It needs no acid and makes no liquid waste; the acid data sheet for the copper route calls for a fume hood, eyewash and safety shower, which a home bench does not have. And each batch is a real choice with a trade-off (conductivity against spreadability against the loading where mixing fails), which suits a trajectory.

**Known weaknesses.** More filler giving more conductivity is textbook, so models may already predict the thermal number; the test may have to rest on the mixing, air and spread results. Hand-mixed pastes sit below commercial ones, and the leading chip-to-lid interface is moving to metal. LongWin's fee is not published. The home rig is a beginner's build and unproven until it agrees with LongWin. No human expert is in the loop apart from the safety checks only a person can do.

**Fallback, and why not both.** Copper electroplating. Running both at the bench was checked and rejected: there is no scenario in which both are run before the 29 November review inside the budget, and the constraint on copper is written sign-off from people (a qualified person on ventilation and eyewash, the disposal route, the premises), not hours. Until the paste gate decision is logged, copper is about 10 hours of desk work with nothing bought; the steps are in section 9 of the checklist.

**What this first cycle is for.** It is a proof of concept, not the dataset. It is small on purpose. It has to show two things: that records made this way are good (repeatable, checkable, complete), and that someone outside wants more of them. If both hold, the next step is to scale; the cost and hours per record measured here set the price of doing so. The likeliest first audience is people who build tests for frontier models.

Start with [CHECKLIST.md](outputs/thermal-paste-first-cycle/CHECKLIST.md), the single completion tracker for the first sample submission. [CALLS_AND_ORDERS.md](outputs/thermal-paste-first-cycle/CALLS_AND_ORDERS.md) contains supplier scripts and specifications; [BENCH_PROTOCOL.md](outputs/thermal-paste-first-cycle/BENCH_PROTOCOL.md) preserves detailed procedures and the later study. [README.md](outputs/thermal-paste-first-cycle/README.md) contains the technical background and candidate equipment. The smaller density measure and 0.001 g balance require shakedown validation; final gate-batch size depends on the selected lab's sample requirement.

### Gates

| When | Test | If it fails |
|---|---|---|
| **About a week after the pilot is packed** (was Sun 18 Oct) | Commissioning, a gate on measurement quality: balance check passed; plain oil spreads within 5% of the calculated curve; mixing-limit scatter 0.015 or less over 12 titrations; tapped powder density within 2% over three fills; a second person tells reference paste from reference crumb in coded photos. Model forecast error is reported as a number per target, not as pass or fail | Fix the method and repeat before any threshold is trusted. A second failure triggers the conditional copper review |
| **When the lab report arrives** | The reference lab documents QC/uncertainty and measures the two independent pilot batches under matched conditions against the proposed 10% repeatability threshold | Ask the lab about its repeatability on greases; decide whether a second lab is worth a quote |
| **Paused** (was Sun 25 Oct) | Home thermal rig. The experiments below make no thermal claim and send nothing further to the lab | Revisit at the 29 November review |
| **Fri 30 Oct** | Has anyone outside engaged with the task card? | If not, finish as a learning campaign and cap spending |
| **Sun 29 Nov** | Continue, change target, or stop. Also decide whether to run a designed set of recipes, using what the three experiments show about where a recipe row is and is not enough | |

The 18 October date could not be met as written: the balance has no arrival date and the handling review is open. If the pilot is packed later than about 23 October, the last settling readings fall after the 29 November review.

### Budget

First cart: approximately $569–698 for ingredients and the density/spread kit, before PPE, freight, tax, handling review and lab fees. The initial staffed-test quote target is $1,000; it is not a published fee or a confirmed package. Rig parts and an optional second lab need separate quotes/decisions. The overall first-step budget remains about $15,000; update the forecast from actual quotes before committing larger work.

## Do now

| # | Action | Done when |
|---|---|---|
| 1 | Phone LongWin, Thermal Engineering Associates and Analysis Tech using the call guide. Confirm staffed scope, sample masses, eligibility, data/publication terms, receipt/result dates and price. A second lab is separately priced and optional | Each has given a quote or a named person and a callback time |
| 2 | Order the four materials and density/spread kit, shipped to your own address; defer rig hardware until design review | Every order has a confirmation and delivery estimate |
| 3 | Paused with the home rig: decide who drills and faces the two aluminium blocks | Route chosen |
| 4 | Rehearse the loop with `trajectory/traj.py` on any quick physical measurement, three runs across two sessions | `verify` passes: predictions logged first, one repeat in a different session |
| 5 | Arrange the checks only a person can do: respirator fit, heater wiring review, the boron nitride ventilation question, and telling the disposal route about the zinc oxide reference paste | Each has a named person and a date |
| 6 | Decide whether this repository stays public, and review the two untracked folders under `outputs/` before committing them | Decision written here |

## Adopted direction: experiments that test a mental model

Decided 7 October 2026 by the project owner and the new team member. The selected programme, with every step, is in [EXPERIMENTS.md](outputs/thermal-paste-first-cycle/EXPERIMENTS.md). Nothing in it has been run.

**What changes.** After the pilot, the work is no longer a repeatability study followed by a grid of recipes. Each experiment starts from competing pictures of how the paste behaves, each committed in advance to a number the others contradict, with inputs measured separately first. An experiment whose outcome an expert or a model would state confidently beforehand is not worth running.

**What is being collected.** Outcomes that come out the same when repeated but that a forecast gets wrong. Noise is not that: it cannot be learned and scores zero.

**What does not change.** The pilot goes first, exactly as on the one-page checklist. It proves the lab route and starts the lab's two-week clock; it is logistics, and nothing about it tests a model. Its two batches are not turned into two arms of a test. The trajectory stays the unit of data, with forecasts logged before outcomes.

**The three experiments.** All sit at the mixing limit: the highest powder loading at which hand kneading still gives one glossy paste. Effects are largest there, and the result is a weighed amount found by adding one ingredient in small steps.

| # | Question | Competing pictures | Fixed in advance |
|---|---|---|---|
| 1 | Is the mixing limit one number or a window? Reach it by adding oil to powder and by adding powder to oil, on coarse, fine and the blend | The limit belongs to the recipe; or kneading packs any powder denser; or only fine powder clumps; or a crumbled mass will not re-wet | The sign and size of the gap for each powder. A gap counts at 0.03 in loading, 3 standard errors, same sign on three days |
| 2 | Can the blend's limit be predicted from each powder measured alone? | Fines act like coarse lumps and nothing is gained; or fines fill the gaps between coarse grains | Two formulas with no fitted number. One score: how far the blend lands from the first prediction (0) towards the second (1) |
| 3 | Left standing, does the coarse powder sink or is it held? | Grains fall separately at a calculable rate; or sticky fines form a skeleton that carries the weight above some fines content | The settling schedule and the holding threshold, both computed from single-powder vials before any blend vial is made |

**Before them: commissioning.** A check of the spread rig on plain oil, dry packing of each powder, and twelve practice-then-counted titrations. Every threshold above rests on how repeatable the mixing limit is, and nobody has measured that yet.

**How the trajectory's value is tested.** Not by these experiments: a planned route or composition is just another column in a table. The test is a forecast made from a plain table of earlier rows against a forecast made from the full log. The gap is the measured value of the trajectory.

**Care with causes.** Randomised run order, repeats on three separate days, matched strokes between arms, photos read blind by a second person, and the threshold for "a real difference" fixed before the first run. A supportable claim is "the outcome depended on the route on this bench". A statement of why needs its own evidence. A picture that survives is "not rejected", not confirmed.

**Cost.** About 14 bench days over four to five weeks from the day the pilot is packed. Three more bottles of oil from one lot and about $75 to $145 of small items (estimates). No lab fee.

**Limits.** All three could come back as the textbook answer or as "no difference larger than X"; that would be recorded as a bound, and the project would then say that on this bench a recipe row is enough for these labels. One operator, one lot of each ingredient. No thermal data comes out of this. That model builders want this kind of record is still a hypothesis to put to them directly.

**Still to decide** (project owner):

1. Is a second person available to code the cups and read the photos blind? Without one, Experiment 1's classes are reported as unblinded.
2. How many forecasting models: two or three.
3. If every model's first, unprompted forecast already matches one picture for an experiment, drop that experiment or run it labelled "textbook if confirmed"? Suggested: apply this to Experiment 3 only; Experiments 1 and 2 share their inputs and run regardless.

## Weekly review

Every Monday, seven numbers: runs completed, independent sessions, runs with a prediction logged before the outcome, exact repeats in a different session, spread between those repeats, dollars spent, and reactions from anyone outside the project. Runs completed is the one that must go up.
