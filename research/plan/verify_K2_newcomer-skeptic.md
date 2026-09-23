# Verify K2 ("Real or simulated?" check list for open XRD files) - lens: newcomer feasibility and value skeptic

Status: notes by one checker. No web access. I read only files inside the scratchpad (C16, C15, builds, gaps, glossary/user model, build-list, merged plan, memory notes, one raw chat slice). I did not open the user's project folders, so every number about files on the user's machine is "as the files say", not re-run by me. Nothing was sent, downloaded, published or changed.

Words used: XRD = powder X-ray diffraction [a 1-D curve of peaks measured from a powder]. RRUFF = a university archive of mineral samples with XRD files. opXRD = a pooled open collection of XRD files from several labs. HKUST-B = one contributor folder inside opXRD. "Calculated pattern" = a curve simulated from a known crystal structure, not recorded on an instrument (synthetic vs real data). Hash = a fingerprint of a file's content.

## Verdict: HOLDS WITH CHANGES

It is doable, cheap and honest. But its value is modest, and the candidate text hides four things a newcomer would trip on. Treat it as a 2-4 day side deliverable that cleans the user's own file list and earns a little credibility. Do not present it as "the" next contribution.

## 1. Can the first step really be done this week with what is on disk?

Mostly yes, with one dependency that the candidate words too softly.

- The RAW DATA is in a permanent place. A memory note says the RRUFF zips and the opXRD slice sit in the user's own project data folder (downloaded 2026-07-09, git-ignored). The build list says "no approval needed" to read them.
- The SCRIPTS AND THE WORKING LIST are not. C16 lists seven scripts (re-derive headline counts, independent hash, join flags, the 200-row RRUFF check, conflicts, fingerprint) in another session's temporary area. The usable-files list is in a temporary area "that can vanish" (C15).
- The candidate says "needs your yes: none to build" but its first step starts "after the file rescue". The XRD session's own list of things that still need the user's yes includes "moving ... the verify2 outputs out of the temp area to a folder the user chooses". So step one does wait on one small yes (name a folder).
- This dependency is removable. Hashing intensity columns and reading header lines is about a day of work for an ML person. A clean-room rebuild that reads the data read-only and writes to a new folder needs no rescue and no yes. If it reproduces 499 of 499, 414, and 124 in 61 groups, that is a third independent replication, which is worth more than copying old scripts.

Time for one part-time person: 1-2 days for the small version below; up to a week for the full 7,183-row list. The candidate's "days (up to one week)" is fair.

## 2. Domain knowledge that would silently trip a newcomer

1. RAW versus PROCESSED files. RRUFF ships two versions of most scans. The headline "1,702 of 3,019" is about RAW files. The raw chat slice also records "PROCESSED 198 of 1,484". C16 says the user's project uses the PROCESSED files, not RAW. So a list keyed only on the RRUFF sample ID would be wrong for the user's own project. Key every row on sample ID + file type (RAW or PROCESSED) + content hash + snapshot date, and never copy a "calculated" status from one version to its sibling without saying so.
2. The total 7,183 equals 3,019 RAW + 1,484 PROCESSED + 2,680 opXRD files (my arithmetic on numbers in the files). So the "usable pool 1,683 of 7,183" counts the RAW and PROCESSED version of the same scan as two files. I could not find whether "1,600 after removing copies" collapses those sibling pairs. An exact-hash de-duplication would not, because processing changes the numbers. Until that is checked, do not call 1,600 a count of independent scans.
3. Keyword search on headers is fragile. The user's own filter searches "calculat" and misses "computed" (C16). All eight missed rows have IDs starting R25 (R250041, R250011, R250017, R250061, R250145, R250143, R250080, R250057). My inference, not a checked fact: newer RRUFF files use different header wording. Safer method: list every DISTINCT header line across the 4,503 RRUFF files (there will be few templates), classify each template once by hand, and store the template text in the evidence column.
4. The "not simulated" flag may be a default value. The same XRD session found that a field reading "manual" on all 1,216 checks in another dataset was simply the schema default, and retracted that error claim. Nobody in the files checked whether opXRD's is_simulated = False is also a default. Until that is checked, write "the is_simulated field reads False", not "deposited as not simulated".
5. "Identical" needs a written definition. The raw slice says: 499 of 499 identical on intensity values; 498 of 499 also identical on the angle axis; one file (pattern_323) differs on angles. Hash the PARSED numbers with fixed rounding, not the raw bytes (the two archives use different file formats). Store two hashes: intensity only, and angle + intensity.
6. The noise ("smoothness") test is the only part that is a domain judgment, and it is unsafe alone: of 29 files where header and noise test disagree, only 3 look calculated; most are real scans from one instrument type (C16). Keep it as a secondary note, never as the basis for a category.
7. One forced category hides facts. An HKUST-B row is at once "identical to a RRUFF file", "calculated" (414 of 499) and "unlabelled" (499 of the 501 unlabelled files). The other 85 of the 499 match RRUFF files that are measured, so they are real scans but still cross-archive duplicates. Use three separate fact columns (origin / identical-to / has a label) plus ONE derived category with a written priority order. Otherwise two people will get different counts.
8. "Calculated" is not "bad". RRUFF's calculated curves are declared in its own headers and are legitimate reference curves. A specialist will dismiss any wording that implies RRUFF hid something. Only the cross-archive match is new.
9. Coverage. The on-disk opXRD copy is 2,680 of 92,552 files, and it is the labelled folders, not a random sample. "Lower bound" is right; "representative" would be wrong.

## 3. Who exactly would use it, and how would they find it?

This is the weakest part of the candidate.

- Certain user: the user's own project. But the measured impact there is small: 0 HKUST-B rows, 8 of 200 RRUFF rows, 8 duplicate pairs (all inside one opXRD subset), on a list of 1,554 rows (1,396 active). The one question that still matters for the project is unchecked in the files: do any of the 8 duplicate pairs sit on both sides of its calibration / test split?
- Outside users: nobody is named in the files. No one has asked for this. The obvious route (an issue on the opXRD code page) is weak: the only outside issue there has been unanswered since March 2026 (C16). RRUFF's route is a contact form on a site that is mid-migration (C16).
- A logic gap: the premise is that eight papers did NOT keep file ID lists. A checker that takes ID lists cannot be run on those papers by an outsider. Only the authors could run it on their own folders. So the checker also needs a "point me at a folder of files" mode that matches by content hash, and it must accept messy inputs (bare sample ID, ID with suffix, or full file name).
- What would make one outside person care: one concrete result on a published benchmark. C15 says one 2026 benchmark uses 291 RRUFF samples. IF its file list is public, "N of those 291 are calculated patterns" is the kind of line people repeat. I could not check whether that list is public (no web). Fetching it would be a download and needs the user's yes.
- Without at least one discovery route the user approves (an issue, a small public repository, or a line in the user's own project README), outside value is close to zero. Say so plainly.

## 4. How does it fail, and is failure cheap and informative?

| Failure | Cost | What you learn |
|---|---|---|
| Temporary scripts are gone | about 1 extra day | Nothing lost; clean-room rebuild is a better replication anyway |
| Counts do not reproduce (say 497, not 499) | hours | Matching depends on parsing choices; must be settled before anything public. Informative |
| is_simulated = False turns out to be a default | hours | The "flagged not simulated" line softens to "the flag was never set". Still a valid finding, gentler message |
| Nobody outside uses it | days already spent | The user's own list is cleaner; honest result is "hygiene, not a lever" |
| The depositing group reacts badly | reputational | Avoidable: neutral wording, phrase it as a question, user sends it, only after web-checking the single-checker claims |

All failures are cheap. None is fatal. The most likely outcome is the fourth row.

## 5. Smallest shippable version (hours to 2 days) that still has value

Drop the full "usable pool" judgment from version 1. Ship only facts:
1. The 499-row HKUST-B to RRUFF match table (both hashes, the matched RRUFF ID and file type, and the matched file's header text).
2. The 61 exact-copy groups (124 files), worded "same pattern, different label text" where labels differ (C16 correction).
3. The header-template table for RRUFF: each distinct header line, its hand-assigned class, how many RAW and PROCESSED files carry it. Targets to reproduce: 1,702 of 3,019 RAW and 198 of 1,484 PROCESSED.
4. A checker of about 50 lines with two modes (ID list; folder of files).
5. A half-page note with coverage (2,680 of 92,552) and the snapshot date.
Private test: run on the user's 1,554-row list; reproduce the eight named RRUFF IDs (not just the count 8), 0 HKUST-B rows and 8 duplicate pairs; then answer the split-straddle question.

## 6. Would a domain expert take it seriously?

For the fact tables: yes. Hashes and header text need no materials judgment, and this is ordinary test-set de-duplication. For any "usable / not usable" verdict: no, not from a newcomer alone.

The ONE thing that would make them take it seriously: a short confirmation from the collection's maintainers or the depositing group that those 499 files did come from RRUFF (it turns "identical values" into confirmed provenance). That is outward-facing and needs the user's explicit yes; the user sends it. A private substitute: one practising diffraction person spends 15 minutes on about 10 rows (the 3-of-29 disputed files and a few of the 85 matched-to-measured files).

## 7. Checks on the load-bearing claims (from files only)

| Claim | Result | Note |
|---|---|---|
| 499 of 499 identical to RRUFF; 414 calculated, flag reads not simulated | confirmed in files | Main session recount + C16 independent re-hash. Extra detail: 498 of 499 also match on angles. Flag-as-default not checked anywhere |
| 261 re-published as "experimental"; eight papers, 148 to 3,002 files, no ID lists | partly | C16 only, one checker. The XRD session planned a fact-check; no result is recorded. Do not repeat publicly before a web check |
| RRUFF half (1,702 of 3,019) is already declared and already noted by a March 2026 paper | confirmed in files | The paper's statement itself is a single-checker finding |
| 124 of 2,680 copies in 61 groups; pool 1,683 of 7,183, then 1,600 | partly | Numbers match across files. Denominator mixes RAW + PROCESSED + opXRD; sibling handling not found |
| On-disk slice is 2,680 of 92,552 (88 MB of about 1.4 GB) | confirmed in files | The slice is the labelled folders, not a random sample |
| Impact on the user's project: 0 / 8 of 200 / 8 pairs | partly | C16 only; the eight IDs are listed; the definition of "suspect" is not in the files I read |
| "None to build" needs no yes | partly | True for a clean-room rebuild. The "rescue" route needs the user to name a folder |
| "Headers and hashes are facts, not opinions" | partly | True for hashes. Header search already missed "computed"; noise test unsafe alone |
| "Who benefits: anyone benchmarking..." | not found | No named outside user or discovery route in any file |

## 8. Things that need the user's explicit yes (unchanged, restated)

- Naming a permanent folder and moving files there.
- Publishing the tables, the checker or the note. RRUFF has no licence text: publish IDs and hashes only, never files.
- Any message to the collection's maintainers, the depositing group or RRUFF. The user sends it.
- Any download, including a benchmark's public file list or the full 1.4 GB release (listed not approved).
- Any change to the user's own project filter.

## 9. Overlap inside the user's own lists (so it is not built twice)

- Build B8 (release-file lint) already owns the "calculated file labelled RAW" check and the noise test.
- Build B2 (fair-split generator) already names "duplicate group plus cross-archive hash" as the grouping unit for XRD. K2's copy groups are exactly that input.
- The user's own project already drops header-calculated RRUFF files and the HKUST-B folder. K2's private gain there is the "computed" wording miss, the 8 duplicate pairs and the split-straddle check.
