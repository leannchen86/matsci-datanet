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

Changed 5 October 2026. Copper electroplating was the working choice for a few hours; it had been compared only against other copper plans. Once the home bench, a business delivery address and bookable time at the LongWin thermal laboratory were known, both routes were worked up in full and three independent reviewers all chose thermal pastes (about 40 against 30 out of 60). Their confidence is medium.

**What gets made.** Silicone oil plus ceramic powder, about 25 g per batch, mixed by hand to a fixed, timed protocol. Alumina first; boron nitride later, once a person has cleared its data sheet.

**What gets measured.** On every batch, the same day: mixing class, density (which gives trapped air), and how far a fixed dose spreads under a weight. A home thermal rig is built in parallel and judged a week later. LongWin's tester is the trusted reference for a small subset, two to four samples per booked day.

**Why this over copper.** The answer can be checked by someone else: thermal impedance has a standard method and an outside instrument. It stays on heat removal. It needs no acid and makes no liquid waste; the acid data sheet for the copper route calls for a fume hood, eyewash and safety shower, which a home bench does not have. And each batch is a real choice with a trade-off (conductivity against spreadability against the loading where mixing fails), which suits a trajectory.

**Known weaknesses.** More filler giving more conductivity is textbook, so models may already predict the thermal number; the test may have to rest on the mixing, air and spread results. Hand-mixed pastes sit below commercial ones, and the leading chip-to-lid interface is moving to metal. LongWin's fee is not published. The home rig is a beginner's build and unproven until it agrees with LongWin. No human expert is in the loop apart from the safety checks only a person can do.

**Fallback.** Copper electroplating. Nothing is bought for it now.

Sourcing, safety limits and the day-by-day plan are in [outputs/thermal-paste-first-cycle/](outputs/thermal-paste-first-cycle/README.md).

### Gates

| When | Test | If it fails |
|---|---|---|
| **Sun 18 Oct** | Control batches made on three different days agree (density within 2%, spread within 7%); deliberately extreme batches differ by at least 3 times that scatter on two labels; LongWin reads the reference paste within 15% of its published value and two control batches within 10% of each other; model predictions made without the campaign history miss by more than the scatter on at least one label | One week on technique and re-test on 25 Oct; fail again and switch to copper |
| **Sun 25 Oct** | Home thermal rig: control scatter within 10% and the same ranking as LongWin | Rent a needle-probe instrument for a week; if that also fails, the thermal label comes only from LongWin |
| **Fri 30 Oct** | Has anyone outside engaged with the task card? | If not, finish as a learning campaign and cap spending |
| **Sun 29 Nov** | Continue, change target, or stop | |

After the 25 October gate: a designed set of about 36 conditions, a third of them made three times in different sessions, with at least a third of all runs in goal-seeking campaigns (for example the highest conductivity that still spreads to a fixed diameter) where the reason for each choice is logged. Release and blind-round dates get set at that gate.

### Budget

Order now: about $1,430, or about $1,090 without the drill press and boron nitride. At risk before the first gate, with one LongWin day at a $1,000 cap: about $2,100 to $2,450. Six weeks: about $4,500 to $5,000 plus LongWin, capped at $4,000, so under about $9,000 in total. LongWin's real fee is unknown until asked.

## Do now

| # | Action | Done when |
|---|---|---|
| 1 | Phone LongWin and send the enquiry form: fee for a half day and a full day, earliest slot in 12 to 16 October, whether a first-time visitor may run the tester, sample quantity, raw files, permission to publish | Answers written down, or a named person and a callback time |
| 2 | Place the order-now list to the business address | Every order has a confirmation and a delivery date |
| 3 | Decide who drills and faces the two aluminium blocks: makerspace, friend, or buy the drill press | Route chosen |
| 4 | Rehearse the loop with `trajectory/traj.py` on any quick physical measurement, three runs across two sessions | `verify` passes: predictions logged first, one repeat in a different session |
| 5 | Arrange the checks only a person can do: respirator fit, heater wiring review, the boron nitride ventilation question, and telling the disposal route about the zinc oxide reference paste | Each has a named person and a date |
| 6 | Decide whether this repository stays public, and review the two untracked folders under `outputs/` before committing them | Decision written here |

## Weekly review

Every Monday, seven numbers: runs completed, independent sessions, runs with a prediction logged before the outcome, exact repeats in a different session, spread between those repeats, dollars spent, and reactions from anyone outside the project. Runs completed is the one that must go up.
