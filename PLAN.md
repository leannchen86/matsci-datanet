# Plan

Updated 5 October 2026. This is the one live plan. The first target is hand-mixed thermal pastes. [outputs/aln-first-cycle-preparation/](outputs/aln-first-cycle-preparation/README.md) is background: it was written for a single careful run at a different budget and is paused, not deleted.

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

**What gets measured.** On every batch, the same day: mixing class, density (which gives trapped air), and how far a fixed dose spreads under a weight. A home thermal rig is built in parallel and judged a week later. LongWin's tester is the trusted reference for a small subset, two to four samples per booked day.

**Why this over copper.** The answer can be checked by someone else: thermal impedance has a standard method and an outside instrument. It stays on heat removal. It needs no acid and makes no liquid waste; the acid data sheet for the copper route calls for a fume hood, eyewash and safety shower, which a home bench does not have. And each batch is a real choice with a trade-off (conductivity against spreadability against the loading where mixing fails), which suits a trajectory.

**Known weaknesses.** More filler giving more conductivity is textbook, so models may already predict the thermal number; the test may have to rest on the mixing, air and spread results. Hand-mixed pastes sit below commercial ones, and the leading chip-to-lid interface is moving to metal. LongWin's fee is not published. The home rig is a beginner's build and unproven until it agrees with LongWin. No human expert is in the loop apart from the safety checks only a person can do.

**Fallback, and why not both.** Copper electroplating. Running both at the bench was checked and rejected: there is no scenario in which both are run before the 29 November review inside the budget, and the constraint on copper is written sign-off from people (a qualified person on ventilation and eyewash, the disposal route, the premises), not hours. Until the paste gate decision is logged, copper is about 10 hours of desk work with nothing bought; the steps are in section 9 of the checklist.

**What this first cycle is for.** It is a proof of concept, not the dataset. It is small on purpose. It has to show two things: that records made this way are good (repeatable, checkable, complete), and that someone outside wants more of them. If both hold, the next step is to scale; the cost and hours per record measured here set the price of doing so. The likeliest first audience is people who build tests for frontier models.

Start with [CHECKLIST.md](outputs/thermal-paste-first-cycle/CHECKLIST.md), the single completion tracker for the first sample submission. [CALLS_AND_ORDERS.md](outputs/thermal-paste-first-cycle/CALLS_AND_ORDERS.md) contains supplier scripts and specifications; [BENCH_PROTOCOL.md](outputs/thermal-paste-first-cycle/BENCH_PROTOCOL.md) preserves detailed procedures and the later study. [README.md](outputs/thermal-paste-first-cycle/README.md) contains the technical background and candidate equipment. The smaller density measure and 0.001 g balance require shakedown validation; final gate-batch size depends on the selected lab's sample requirement.

### Gates

| When | Test | If it fails |
|---|---|---|
| **Sun 18 Oct** | Control batches made on three different days agree (density within 2%, spread within 7%); extremes differ by at least 3 times that scatter on two labels; the selected reference lab documents QC/uncertainty and measures two independent controls under matched conditions against the proposed 10% repeatability threshold; cold model error exceeds scatter on at least one label | Process gate can be recorded with reference measurement pending. Technique failure gets one week and a 25 Oct re-test; a second failure triggers the conditional copper review |
| **Sun 25 Oct** | Home thermal rig: control scatter within 10% and the same ranking as LongWin | Rent a needle-probe instrument for a week; if that also fails, the thermal label comes only from LongWin |
| **Fri 30 Oct** | Has anyone outside engaged with the task card? | If not, finish as a learning campaign and cap spending |
| **Sun 29 Nov** | Continue, change target, or stop | |

After the 25 October gate: a designed set of about 36 conditions, a third of them made three times in different sessions, with at least a third of all runs in goal-seeking campaigns (for example the highest conductivity that still spreads to a fixed diameter) where the reason for each choice is logged. Release and blind-round dates get set at that gate.

### Budget

First cart: approximately $569–698 for ingredients and the density/spread kit, before PPE, freight, tax, handling review and lab fees. The initial staffed-test quote target is $1,000; it is not a published fee or a confirmed package. Rig parts and an optional second lab need separate quotes/decisions. The overall first-step budget remains about $15,000; update the forecast from actual quotes before committing larger work.

## Do now

| # | Action | Done when |
|---|---|---|
| 1 | Phone LongWin, Thermal Engineering Associates and Analysis Tech using the call guide. Confirm staffed scope, sample masses, eligibility, data/publication terms, receipt/result dates and price. A second lab is separately priced and optional | Each has given a quote or a named person and a callback time |
| 2 | Order the four materials and density/spread kit, shipped to your own address; defer rig hardware until design review | Every order has a confirmation and delivery estimate |
| 3 | Decide who drills and faces the two aluminium blocks: makerspace, friend, or buy the drill press | Route chosen |
| 4 | Rehearse the loop with `trajectory/traj.py` on any quick physical measurement, three runs across two sessions | `verify` passes: predictions logged first, one repeat in a different session |
| 5 | Arrange the checks only a person can do: respirator fit, heater wiring review, the boron nitride ventilation question, and telling the disposal route about the zinc oxide reference paste | Each has a named person and a date |
| 6 | Decide whether this repository stays public, and review the two untracked folders under `outputs/` before committing them | Decision written here |

## Adopted direction: experiments that test a mental model

Decided 7 October 2026 by the project owner and the new team member. The detailed programme is being designed and reviewed; it will replace this section's last list when it is ready.

**What changes.** After the pilot, the work is no longer a repeatability study followed by a grid of recipes. Each experiment starts from two competing pictures of how the paste behaves, each committed in advance to a number the other contradicts, with inputs measured separately first where possible. An experiment whose outcome an expert or a model would state confidently beforehand is not worth running.

**What is being collected.** Outcomes that come out the same when repeated but that a forecast gets wrong. Noise is not that: it cannot be learned and scores zero.

**What does not change.** The pilot goes first, exactly as on the one-page checklist. It proves the lab route and starts the lab's two-week clock; it is logistics, and nothing about it tests a model. Its two batches are not turned into two arms of a test: one batch per arm cannot separate a real difference from ordinary scatter, and the lab's thermal number is the measurement least affected by how a paste was made. The trajectory stays the unit of data, with forecasts logged before outcomes.

**How the trajectory's value is tested.** Not by varying a process setting on purpose: a planned setting is just another column in a table. The test is a forecast made from a plain table of earlier rows against a forecast made from the full log. The gap is the measured value of the trajectory.

**Care with causes.** Randomised run order, repeats on different days, matched mixing work between arms, photos read blind, and the threshold for "a real difference" fixed before the first batch. A supportable claim is "the outcome depends on the route under these conditions". A statement of why needs its own evidence.

**Candidate experiments under review** (not yet selected):

1. Is the recipe enough? Reach the same final recipe by two routes and see whether the outcome matches.
2. Predict the blend from the parts: measure how each powder packs alone, predict the best coarse-to-fine ratio and how far it can be loaded, then test it.
3. Does it settle or hold? One picture predicts the coarse powder sinks at a calculable rate; the other predicts no settling above some loading.

**Limits.** Published effect sizes come from other pastes; nobody has measured hand-mixed alumina in silicone oil, so a null result is possible and is still a result. That model builders want this kind of record is a hypothesis to put to them directly.

## Weekly review

Every Monday, seven numbers: runs completed, independent sessions, runs with a prediction logged before the outcome, exact repeats in a different session, spread between those repeats, dollars spent, and reactions from anyone outside the project. Runs completed is the one that must go up.
