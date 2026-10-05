# Plan

Updated 5 October 2026. This is the one live plan. [outputs/aln-first-cycle-preparation/](outputs/aln-first-cycle-preparation/README.md) is background: it was written for a single careful run at a different budget and is paused, not deleted.

## Decided

- **Goal.** Produce experimental materials data that people who train models would actually want: complete, checkable, with the failures left in.
- **Unit of data.** A trajectory, not a row: goal, plan, what was done, raw readings, interpretation, next decision, dead ends. Format and rules are in [trajectory/](trajectory/README.md). Each run also records a model prediction made without the campaign history and one made with it, so the release can show how much the history helps a model.
- **Expert.** For now an AI model is the expert. It writes a prediction before every run; the measured outcome scores it. A human expert comes later, when there is money and time.
- **Method.** By hand, full time. Speed and learning come before automation or scale.
- **Budget.** About $15,000 for this first step.
- **Release.** The first dataset is given away to test demand. What is public and what is held back gets decided before anything is released, because public data cannot later serve as a hidden test.

## First target: copper electroplating on a bench we control

Chosen 5 October 2026 by a comparison of twelve candidate targets and four strategies, scored by three independent judges. All three picked the same plan. It is a working decision with a hard gate on Friday 9 October.

**What gets made.** Copper is plated from an acid copper bath onto small metal panels in a standard test cell (a Hull cell), one freshly made bath per run. Each run varies the additive levels and the current. One run takes about half an hour, so a week gives dozens of decision cycles.

**What gets measured.** Where on the panel the deposit burns, how much of it is bright, and the defect class, from a scan of the panel. Two checks on every run: the deposited mass against the amount the current should have plated, and a fixed control bath every fifth run. A second, more rigorous label (resistance of a peeled copper strip against a reference) is added only if the first labels fail the noise gate.

**What it becomes.** A held-out prediction test: about 40 to 60 conditions fixed and anchored in advance, a third of them made three times in different sessions, about 100 scoreable runs, plus about 10 episodes in which a bath is deliberately spoiled and a model has to diagnose it from the panel. About 30% is released; the rest is held back, and held-back outcomes never go to a model.

**Why not the alternatives.** Thin-film AlN scored last: about one result per multi-week cycle and one or two thermal measurements for the whole budget. Hand-mixed thermal pastes scored a close second and are the fallback; they keep the heat-removal theme and make no liquid waste, but need three to four weeks to build and validate a tester first. Collecting other people's records scored third: nearly free, but nobody has a reason to hand records to us yet.

**Known weaknesses.** This leaves the heat-removal theme. Panel appearance is plating-shop evidence, not the feature-filling behaviour chip makers care most about. No case was found of an AI lab buying a hand-made dataset this small; the likeliest first users are groups that build model evaluations. No human expert is in the loop: all three judges recommended buying a few hours of a practising plater (about $1,000 to $2,500) to check technique and give a human baseline. That is left out for now by decision and revisited at the 18 October gate.

### Schedule

| When | What | Gate |
|---|---|---|
| Week 1, 5-11 Oct | No chemicals. Settle where the bench goes, who delivers the chemicals there, and a lawful route for the waste. Read every safety data sheet and write the procedure and hard limits. Write a one-page task card (input, output, metric) and test it on public data with three models. Order the kit that needs no decision. | **Fri 9 Oct:** no lawful waste route, or the lease or household rules it out, and no rented bench can start by 26 Oct: switch to thermal pastes before spending more than $3,000 |
| Week 2, 12-18 Oct | Shakedown runs that do not count. Then 12 control baths across three days and four extreme baths. | **Sun 18 Oct:** the spread between extreme baths must be at least 3 times the spread between repeats, for at least one label. If not, a week on technique; if still not by 25 Oct, change the label |
| Week 3, 19-25 Oct | Anchor the condition list, the split and the scoring rule. Freeze model predictions. First block of runs. Release a first public slice and open a blind round: publish conditions, invite predictions, measure afterwards. | **Sun 25 Oct:** if models are already inside the noise on most items, there is nothing to measure: switch to the diagnosis episodes |
| Week 4, 26 Oct-1 Nov | Second block of runs. | **Fri 30 Oct:** if about 25 messages have drawn no substantive reply, finish as a learning campaign and cap spending at $9,000 |
| Week 5, 2-8 Nov | Third block and the diagnosis episodes. Blind-round predictions close 8 Nov. | Zero outside prediction files is the first formal no |
| Week 6, 9-15 Nov | Run the blind-round baths, score, release. | **Sun 29 Nov:** decide: continue, change target, or stop |

### Budget

About $10,000 if the bench is at home, about $13,000 if a bench has to be rented. Roughly: plating kit and glassware $2,100; balance, scanner and meters $1,300; chemicals $900; safety equipment and waste disposal $1,000; one outside cross-check, model usage and shipping $2,300; contingency for the rest. About $2,600 is spent in week 1; the rest is released gate by gate. Most prices are from web listings, not quotes.

### Hard limits

Acid bought pre-diluted, never stronger than the procedure states. No heating, no cyanide, no hydrofluoric acid. Splash goggles always. A daily cap on wet work, never when exhausted, and someone knows when it is happening. Stop on any exposure needing more than rinsing, any spill outside the containment tray, or any waste container without a confirmed disposal route. Safety comes from the data sheets, the supplier and the county waste programme, not from a model.

## Do now

| # | Action | Done when |
|---|---|---|
| 1 | Rehearse the loop with `trajectory/traj.py` on any quick physical measurement (kitchen scale, multimeter), three runs across two sessions, marked as a rehearsal | `verify` passes: predictions logged first, one repeat in a different session |
| 2 | Settle the three facts behind the 9 October gate: bench location (single-family home, or a rented bench that accepts one person doing chemistry), chemical delivery to that address, and how the county classifies and accepts the waste | Each answered by a named person at the supplier, landlord or county programme |
| 3 | Check whether the Livermore thermal-testing lab answered the 24 September email | If it offers cheap tester access, thermal pastes become the first target |
| 4 | Write the one-page task card and try it on five example items with three models | Card and replies saved; shown to scientist contacts with the question "what number would change what you do?" |
| 5 | Decide whether this repository stays public, and review the two untracked folders under `outputs/` before committing them | Decision written here |

The rehearsal is first on purpose: the first real record matters more than any further desk work.

## Weekly review

Every Monday, seven numbers: runs completed, independent sessions, runs with a prediction logged before the outcome, exact repeats in a different session, spread between those repeats, dollars spent, and reactions from anyone outside the project. Runs completed is the one that must go up.
