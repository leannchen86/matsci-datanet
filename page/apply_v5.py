# v5: fold in the 19 Sep eval-principles check (4 reviewers + 4 skeptics)
import shutil, sys
P = sys.argv[1]
import os
B = P.replace('big-picture.html', 'big-picture.v4.bak.html')
if not os.path.exists(B): shutil.copy(P, B)
s = open(P, encoding='utf-8').read()

def rep(old, new_, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:80])
    s = s.replace(old, new_)

# ---------- hero + section header + footer
rep('everything so far, on one page · 18 Sep 2026', 'everything so far, on one page · updated 19 Sep 2026')
rep('five planners, then adversarial checkers · both headline claims got smaller',
    'five planners, then adversarial checkers · both headline claims got smaller · eval check added 19 Sep')
rep('and a five-agent fact-check of this page.',
    'a five-agent fact-check of this page, and a check of the plan against published evaluation principles (four reviewers, each attacked by a skeptic).')

# ---------- reco box: what the test does and does not decide
rep('The answer decides whether the “fair marking kit” is a tool other people need, or a fix and a test file for your own project. Both outcomes are useful and both are cheap.',
    'The answer decides whether the 2–3 week reusable marker is worth building, or whether a fix and a test file inside your own project is enough. Both outcomes are useful and both are cheap. Whether other people need such a marker is a separate question, answered by outside evidence, not by this table.')

# ---------- new block: eval check, right after the reco box
EVAL = '''  </div>

  <div class="bucket" id="evalcheck" style="margin-top:22px">Eval check · 19 Sep · is this evaluation work, and is it set up right?</div>
  <p class="note" style="margin:0 0 8px;color:var(--ink)"><b>Yes, this is evaluation work.</b> More exactly: checking the exams before trusting the scores. ML calls it benchmark auditing; measurement labs call it method validation. Every item below except the file rescue is a form of it. Test data is curated data, so this still sits inside your aim of better experimental data. Only the partner-lab item builds a new exam.</p>
  <p class="note" style="margin:0 0 12px">Four reviewers (ML benchmark science, measurement science, materials-ML benchmarks, test validity) scored the plan against <span class="num">56</span> published principles. Four skeptics then attacked the reviews. <b style="color:var(--ink)">All eight say: go ahead with the 40-row test, after about one hour of writing.</b> The tally: <span class="num">6</span> met, <span class="num">45</span> partly met, <span class="num">1</span> not yet relevant, <span class="num">4</span> rated broken. Of those 4 the skeptics downgraded two, threw out one (it rested on a misread paper) and upheld one: calling the weighed answer key “certain”. With nearly every row “partly”, the tally says little. The changes are the useful part, and they are already folded into the cards below.</p>

  <div class="tbl" style="margin-bottom:8px"><table>
    <thead><tr><th style="width:22%">Write down before opening the data · about 1 hour, one dated page</th><th>What the line says</th><th style="width:24%">ML twin</th></tr></thead>
    <tbody>
      <tr><td class="term">1 · Task card</td><td>Task: name the phases. One mark per scan, on the program’s top-ranked answer only. Three things above the table: the set rule (all true phases found, no extra phase), which answer is scored, and the sameness rule (strict = formula text equal; lenient = atom fractions within 0.10). Copied from your frozen plan and the Dara paper, not invented.</td><td>A metric spec</td></tr>
      <tr><td class="term">2 · Four bins</td><td>Spelling artifact / real chemistry / answer key or recipe suspect / unsure, needs a specialist. Labelled “sorted by a newcomer plus AI; draft until a specialist sees it”.</td><td>A label schema with an “unsure” class</td></tr>
      <tr><td class="term">3 · What is counted</td><td>Distinct (true formula, program formula) pairs, with rows and powders shown beside. The 40 scans come from 10 ingredients, so one artifact such as “LaO3” for La(OH)3 repeats across scans. The whole swing may rest on <span class="num">3 to 15</span> pairs.</td><td>Count independent samples, not near-duplicates</td></tr>
      <tr><td class="term">4 · Threshold K, yours</td><td>“Build the reusable marker if at least K distinct pairs are real chemistry.” Unsure is counted separately. K gates only the 2–3 week marker; the tricky-pairs table is built either way. A starting suggestion from me, not from the reviewers: K = 5.</td><td>Decision rule fixed before looking</td></tr>
      <tr><td class="term">5 · Two-line verdict</td><td>(a) What the table shows about <i>my</i> marker. (b) What outside evidence says about everyone else’s.</td><td>Internal vs external validity</td></tr>
      <tr><td class="term">6 · Honesty lines</td><td>This is a rule written before a recount, not a blind pre-registration: an earlier chat already read these misses as naming artifacts. The lenient rule was adjusted after seeing these scans (a hydrogen rule moved the pilot from 0.545 to 0.745), so its score here is in-sample. One benchmark, 20 powders from 10 ingredients: it measures nothing about other datasets. It can show “strict is too strict”, not “lenient is too loose”.</td><td>Disclose tuning on the test set</td></tr>
    </tbody>
  </table></div>

  <div class="tbl" style="margin-bottom:8px"><table>
    <thead><tr><th style="width:26%">Direction · what we said</th><th>What the review found</th></tr></thead>
    <tbody>
      <tr><td class="term">“Mostly spelling” means nobody else needs a marker</td><td>Does not follow. Spelling and hydrogen variants are exactly what other groups hit: one 2026 paper judges “same phase?” with a GPT-4 prompt, and the Dara paper states no sameness rule and ships no scorer. The 40-row test sizes the problem in your set-up only.</td></tr>
      <tr><td class="term">Weighed answers are certain</td><td>They are known to within ingredient purity, weighing error and any reaction during mixing. The Dara paper itself reports a real extra phase (a bismuth carbonate) in one of the 20 mixtures and left it out of scoring. Weighed mixtures are a floor test: failing is informative, passing is not proof.</td></tr>
      <tr><td class="term">A hidden weighed exam is the prize</td><td>The scarce thing is fresh, verified powders every round, plus a key holder who stays out of the ranking. That is lab work; from a desk it may be out of reach. Software has already been scored on contest mixtures after the fact (2019, 2021), so the novelty shrinks to a recurring hidden-recipe exam for phase-naming software on synthesis-type chemistry.</td></tr>
      <tr><td class="term">Thermoelectrics: “the exam is too easy”</td><td>It may be ill-posed, not only easy: a formula alone does not fix the sample (about 6% between labs on one specimen, 32.7% across papers). Run the by-formula split first as a kill test. At least two thermoelectric papers already split by composition, so the prior-art search moves before the private page.</td></tr>
      <tr><td class="term">Missing from the plan</td><td>How should an exam score “not sure” and ranked answers? For example accuracy against the share of scans answered. This is your own speciality (trust scores) and the most natural ML contribution. No item covers it yet.</td></tr>
      <tr><td class="term">When to answer the specialist question</td><td>Now. It costs nothing and contacts nobody. The ask itself goes out only once the table and a blind set of pairs exist.</td></tr>
    </tbody>
  </table></div>
  <p class="note" style="margin:0 0 6px"><b style="color:var(--ink)">Already right, leave alone:</b> test before build, shrunken headlines, “practice exam” vs “hidden exam” honesty, “may be out of our reach”, the do-not list, every outward step waiting for your yes, the “cannot tell” verdict with guard rows.</p>
  <p class="note" style="margin:0 0 6px"><b style="color:var(--ink)">Rejected as process theatre:</b> a decider line per item, stop rules for 2-day tasks, hashing the protocol, a datasheet on every file, an evaluation card per test, significance tests on hand-picked pairs, a web lookup of publication years.</p>
  <p class="note" style="margin:0 0 20px"><b style="color:var(--ink)">Still unverified, so not for public use:</b> which reference library the paper’s 38 of 40 used; whether the paper’s supplement spreadsheets really are on disk; several outside figures the reviewers saw only as search snippets. The reviewers called this the last check before the test starts.</p>

  <div class="tbl" style="margin-bottom:8px"><table>
    <thead><tr><th style="width:20%">Headline so far</th>'''
rep('''  </div>

  <div class="tbl" style="margin-bottom:8px"><table>
    <thead><tr><th style="width:20%">Headline so far</th>''', EVAL)

# ---------- set-up table footnote
rep('<p class="note" style="margin:0 0 18px">A pattern in our own measurements, not a field-wide fact.</p>',
    '<p class="note" style="margin:0 0 18px">A pattern in our own measurements, not a field-wide fact. All X-ray rows are fixed scans from one instrument, with the element list given to the program. The 11–13 of 20 gap probably flatters one program: that answer key is one expert’s reading, made with that program’s suggestions in view.</p>')

# ---------- steps
rep('Ends with one written line: “worth building a reusable marker” or “bug-fix and a test file for my project”.',
    'One hour of writing first: the rule, before the data. Ends with two lines: what the table shows about your marker, and what outside evidence says about everyone else’s.')
rep('Tricky-pairs table (unit tests for the marking rule), match table (simulated scans filed as measured), “tie or not?” function, a web-only look at harder public test sets.',
    'Tricky-pairs table (unit tests for the marking rule), match table (simulated scans filed as measured), “tie or not?” function, a web-only look at harder public test sets (can start on day 1; it needs nothing).')
rep('Re-run, print the seen/unseen breakdown, freeze one test list.',
    'Prior-art search first, then the by-formula kill test. Re-run, print the seen/unseen breakdown, freeze one test list.')

# ---------- rescue card
rep('the five-item corrections draft, and the thermoelectric data and scripts, each with a checksum.',
    'the five-item corrections draft, the thermoelectric data and scripts, and the finished negatives table (the 332-of-671 list, which had dropped off this list), each with a checksum. If the Dara paper’s supplement spreadsheets are on disk, note where.')

# ---------- 40-row card
rep('One table: the true formulas, the program’s formulas, and three marks per scan. Every row where the marks differ is hand-sorted into “spelling artifact” or “real chemistry disagreement”.',
    'A one-page rule is written first. Then one table: the true formulas, the program’s formulas, and three marks per scan. Every row where the marks differ is hand-sorted into four bins: spelling artifact, real chemistry, answer key or recipe suspect, unsure.')
rep('      <div><b>First hour</b>Count the scan files. The notes say 40, 41, 60, 61 and 70. If it is not 40, the 12 / 17 / 32 targets may not reproduce.</div>',
    '''      <div><b>Before the data opens (about 1 hour)</b>One dated page: the task card, the four bins, the counting unit (distinct formula pairs), your threshold K and the honesty lines. All six lines are in the eval check above.</div>
      <div><b>First hour</b>Count the scan files. The notes say 40, 41, 60, 61 and 70. If it is not 40, the 12 / 17 / 32 counts may not come back. Look on disk for the Dara paper’s own per-scan verdicts (the notes say its supplement spreadsheets are there; no new download). Check whether the 55-row pilot overlaps these 40 scans (double counting), and whether the hydrogen rule was added before or after your project’s 9 July 2026 freeze.</div>''')
rep('The table should reproduce 12, 17 and 32 of 40.', 'Recount 12, 17 and 32 of 40; any difference is a finding, not a failure.')
rep('      <div><b>Done when</b>Every differing row is sorted, the scan-file count is settled, and one written line gives the verdict.</div>',
    '''      <div><b>Extra columns (2–3 hours)</b>Powder id (20 powders) and scan time. Found / missed / extra counts under one named rule, plus one sentence read from the marker code: “an extra phase makes the scan wrong: yes or no”. A flag for the recipe with a documented off-recipe phase (the rows holding both Bi2O3 and Li2CO3). Settings: rule and code version, tolerance, program version, reference library and date, candidate cap; “unknown” where never saved. Disputed by / date / resolution. One lookup per distinct pair: which library entry sits behind the program’s formula.</div>
      <div><b>If the paper’s verdicts are on disk</b>Add them as a column, print the agreement and list the mismatches. Also settle 34 or 35 of 40 for the commercial program: the paper’s text reads 16 + 18 = 34, our notes say 35. The tie verdict does not change.</div>
      <div><b>Second sheet</b>Hand-sort the 18 rule-dependent rows among the 210 pilot rows with the same four bins, after checking they are not the same 40 scans. It covers the other failure direction: lenient too loose.</div>
      <div><b>Done when</b>Every differing row is sorted, the scan-file count is settled, and two written lines give the verdict: what the table shows about your marker, and what outside evidence says about everyone else’s.</div>''')
rep('      <div><b>If it says “mostly spelling”</b>You fix your own marker, keep a small test file, and the main effort moves to the thermoelectric and cross-cutting pieces. That is a cheap, informative failure.</div>',
    '      <div><b>If fewer than K pairs are real chemistry</b>The 2–3 week marker is not built; your own marker gets a fix and a small test file. It does not show that nobody else has the problem: spelling and hydrogen variants are what other groups hit too. The tricky-pairs table is built either way.</div>')

# ---------- tricky-pairs card
rep('so “disagrees”, not “wrong”.</div>', 'so “disagrees”, not “wrong”. These are unit-test results on hand-picked pairs, never error rates.</div>')
rep('“No runnable marker exists” rests on one unchecked search.',
    '“No runnable marker exists” is now a little firmer: a reviewer opened Dara’s public code on 19 Sep and saw runner scripts but no scorer. Still not an exhaustive search.')

# ---------- match table card
rep('      <div><b>Wording</b>“Identical to”, never “copied from”.',
    '      <div><b>Group by</b>Mixture or sample ID as well as file hash, so two scans of one powder count as one.</div>\n      <div><b>Wording</b>“Identical to”, never “copied from”.')

# ---------- tie function card
rep('A small function that prints an interval and “tie / not a tie” beside any score. Both scorers call it by default.',
    'A small function that prints an interval and one of three verdicts beside any score: not a tie, tie, too small to tell. Both scorers call it by default.')
rep('The 40 scans are really 20 powders, each scanned twice.',
    'The 40 scans are really 20 powders, each scanned twice, so it resamples powders (or papers), never rows, and prints n = 20.')
rep('      <div><b>Done when</b>The 38-vs-35 example returns “tie”.</div>',
    '      <div><b>Done when</b>The 38-vs-35 example (34 if the recount says so) returns “tie”. When the answer key is still a draft it also prints “key not verified; no ranking claim”.</div>')
rep('      <div><b>Checked?</b>Not by the skeptical checkers. It is plain statistics.</div>',
    '      <div><b>Checked?</b>Yes, in the 19 Sep eval check. Known statistics (Miller 2024, “Adding error bars to evals”); a local copy of a known method, no novelty claimed.</div>')

# ---------- web-only look card
rep('      <div><b>Why check first</b>The notes support',
    '      <div><b>Three more columns</b>Were the true phases given to the original entrants? Weight-percent range. Scan time. Plus a quarter-day table of which hard cases each set covers: tiny amounts, a weak scatterer beside a strong one, overlapping or same-structure pairs, poorly crystalline material, short scans.</div>\n      <div><b>Why check first</b>The notes support')

# ---------- TE small private card
rep('      <div><b>Done when</b>The same six numbers come back.',
    '''      <div><b>Before anything (1–2 hours on the web)</b>Prior-art search. At least two thermoelectric papers already split by composition (2024, 2026). Safe claim so far: we found none that holds out whole papers, publishes a frozen test list, or prints a best achievable score.</div>
      <div><b>Run first: the kill test</b>Split by formula, with a 1-nearest-neighbour baseline under every split. Written down before running: if “by paper” minus “by formula” sits inside the tie function’s interval, the full note shrinks to the frozen list plus the ceiling.</div>
      <div><b>Done when</b>The same six numbers come back.''')
rep('Paper IDs only; no rows from ESTM, the one source with no licence.</div>',
    'Paper IDs only; no rows from ESTM, the one source with no licence. ESTM is a separate hand-collected database, not a slice of the main one, so the list’s header says: any training row, from any database, whose paper is on this list breaks the rule. Re-plotted curves that cross papers are not removed; their count is unknown.</div>')

# ---------- N1 marker card
rep('Only if the 40-row test says “worth building”. Returns a tier instead of yes/no,',
    'Only if the 40-row test clears your threshold K. Default size is a fix inside your project (days); the reusable 2–3 week version also waits for one specialist’s reply. Returns a tier instead of yes/no,')
rep('<span class="chip xrd">X-ray</span><span class="chip">2–3 weeks</span><span class="chip yes">yes to change your project</span>',
    '<span class="chip xrd">X-ray</span><span class="chip">days · 2–3 weeks only with a specialist’s reply</span><span class="chip yes">yes to change your project</span>')
rep('      <div><b>Worth checking</b>Whether the installed program already ships its paper’s own marking script. If so, add it as one more rule beside the five already compared.</div>',
    '''      <div><b>Checked, confirm on day 1</b>A reviewer saw no marking script in Dara’s public code on 19 Sep. Confirm on the installed copy. If one exists, add it as one more rule beside the five already compared.</div>
      <div><b>Before design</b>Ask whether a “marking problem” is really “this measurement cannot tell them apart”. Dara’s own grouping of same-structure candidates may be the natural sameness rule.</div>
      <div><b>Guard tests</b>Adding a wrong phase never raises the score. A hydroxide and its oxide are never “same”. “Cannot tell” is its own share and never counts as correct, so the score is a range. Per-phase found / missed / extra sits beside the per-scan mark (others already do this, so it is not new). Settings and a version string print with every score.</div>
      <div><b>Open idea, your speciality</b>How should an exam score “not sure” and ranked answers? For example accuracy against the share of scans answered. No item in this plan covers it yet.</div>''')

# ---------- TE note, full version
rep('      <div><b>First, 1–2 hours on the web</b>Does a thermoelectric leakage audit already exist? Do 3–5 named papers really split at random? Nobody checked. If an audit exists, shrink to the frozen list.</div>',
    '      <div><b>Lead with</b>The best achievable score and the missing sample description; the split finding comes second. The task may be ill-posed, not only too easy: a formula alone does not fix the sample. The prior-art search moved earlier, to the small private version. A thermoelectric specialist’s read is a gate for publishing, not for the private run.</div>')

# ---------- practice exam card
rep('      <div><b>Limit</b>The answers are public, so this is a practice exam, never a hidden one.',
    '      <div><b>Report</b>Every band with its count, the lowest included but not as the headline. Per source set and X-ray type, never pooled. One frozen configuration. The detection floor quoted from each set’s own paper. State how long each set has been public and whether its file names spell the recipe: a tool or AI agent that reads file names is contaminated.</div>\n      <div><b>Limit</b>The answers are public, so this is a practice exam, never a hidden one.')

# ---------- noise ladder card
rep('Each rung needs an “includes / excludes” line.</div>',
    'Each rung needs an “includes / excludes” line. The published between-lab figure (about 6%, eight labs, one specimen) goes on as a labelled outside reference line, not a rung. The ladder becomes one figure inside the thermoelectric note.</div>')

# ---------- one short note (parked)
rep('<span class="chip">1–2 weeks, after the two halves hold</span><span class="chip yes">yes to publish</span>',
    '<span class="chip parked">parked: cite and apply</span><span class="chip">1–2 weeks, after the two halves hold</span><span class="chip yes">yes to publish</span>')
rep('      <div><b>Rule</b>Do not start it before the marker result and the thermoelectric note both hold up.</div>',
    '      <div><b>Rule</b>Do not start it before the marker result and the thermoelectric note both hold up.</div>\n      <div><b>Why parked</b>Checklists like this already exist (evaluation cards for materials ML, REFORMS, BetterBench). Cheaper: a six-line header on anything published. Claimed ability, data source, known label problems, split rule, metric, what a high score does not mean.</div>')

# ---------- specialist card
rep('“Here are 25 rows. Where am I wrong?” The smallest credible ask a newcomer can make.',
    'Blind first: about 25 pairs with three tick-boxes (same / different / depends) and no AI-drafted verdict in view, about 10 minutes. Then “where am I wrong?”. The smallest credible ask a newcomer can make.')
rep('as a held-out check that the rule was not tuned to the table.</div>',
    'as a held-out check that the rule was not tuned to the table. And one question: which of these distinctions would change a decision in your lab? The program’s maintainers are fine for a formula-text bug report, not for blessing the key.</div>')

# ---------- L2 card
rep('<div class="name">A small hidden weighed exam with one partner lab</div><div class="plain">The real missing ingredient: fresh test items whose answer comes from a balance, not from an analyst.</div>',
    '<div class="name">A one-off blind check with one partner lab</div><div class="plain">The real missing ingredient: fresh, verified powders whose recipe is hidden. The answer comes from a balance plus a purity check, not from an analyst.</div>')
rep('About 470–780 paired powders to separate two tools 5 points apart.</div>',
    'About 470–780 paired powders to separate two tools 5 points apart. A 30–60 powder version can estimate an error rate; it cannot rank tools. A standing exam needs new verified powders every round, which costs far more than 385 once.</div>')
rep('      <div><b>Honest limits</b>One lab gives certain answers but a one-instrument exam.',
    '''      <div><b>Rules it needs</b>The lab holds the key. File names and headers are random IDs. Your own tool enters unranked, because you are the organiser. The key gets its own check: scans of each ingredient lot, one independent chemistry check on a subset, re-scans of about 10%.</div>
      <div><b>What is new, stated carefully</b>Software has already been scored on contest weighed mixtures after the fact (2019, 2021). What still appears open is a recurring exam with hidden recipes for phase-naming software on synthesis-type chemistry. The main barrier is the cost of fresh, verified powders each round. An alternative worth weighing: offer scoring and statistics to an existing contest body (contacting one needs your yes).</div>
      <div><b>Honest limits</b>One lab gives answers known to within ingredient purity, weighing error and any reaction during mixing, on one instrument. Weighed mixtures are a floor test: failing is informative, passing is not proof for real reaction products, whose key would need a second kind of measurement (out of our reach for now).''')

# ---------- ask box
rep('No need to contact anyone before the week-2 sitting.',
    'Answering now costs nothing and contacts nobody. Nothing goes out until the 40-row table and the blind pairs exist (about the end of week 1), and you are the one who sends it. No reply after a fair wait is a result.')
rep('<div class="q">If no, or nobody replies in about two weeks, or the test says “mostly spelling”</div>',
    '<div class="q">If no, or nobody replies after a fair wait</div>')
rep('    <p><b>Two approvals to start.</b></p>',
    '    <p>The 40-row result no longer decides this fork. It decides only whether the 2–3 week marker gets built.</p>\n    <p><b>Three things to start.</b></p>')
rep('      <li>A yes to a working chat reading your two project folders, read only, with outputs written elsewhere.</li>',
    '      <li>A yes to a working chat reading your two project folders, read only, with outputs written elsewhere.</li>\n      <li>Your threshold K for the 40-row rule, picked before the data opens (my starting suggestion: 5).</li>')

# ---------- glossary
rep('Powders mixed at weighed amounts, then scanned. Truth comes from the scale, not an analyst.',
    'Powders mixed at weighed amounts, then scanned. Truth comes from the scale, not an analyst: known to within ingredient purity, weighing error and any reaction during mixing. A floor test, since passing it is not proof on real products.')

# ---------- trust table
rep('      <tr><td class="term">Uneven scrutiny</td>',
    '      <tr><td class="term">Eval-principles check · 19 Sep</td><td>Four reviewers and four skeptics: <span class="num">56</span> principles, <span class="num">106</span> skeptic rulings (25 held, 80 held with changes, 1 refuted). They read the plan and notes plus about 50 outside sources, some only as search snippets, and never opened your project folders. Several changes on this page are skeptics correcting reviewers.</td></tr>\n      <tr><td class="term">Uneven scrutiny</td>')
rep('Not checked: the tie function, the error notes, the noise ladder, the one short note, the suspect list.',
    'Not checked then: the tie function, the error notes, the noise ladder, the one short note, the suspect list (the 19 Sep eval check has since covered the tie function, the ladder and the short note).')

open(P, 'w', encoding='utf-8').write(s)
print('v5 ok', len(s))
