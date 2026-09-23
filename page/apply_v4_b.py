# Part B: section 04 (what to build next)
import sys
P = sys.argv[1]
s = open(P, encoding='utf-8').read()

def rep(old, new_, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:80])
    s = s.replace(old, new_)

# ---------- (a) recommendation box
rep('<h3>Start with a one-day test, not a build:', '<h3>Start with a one-to-two-day test, not a build:')
rep('<p>One 40-row table answers it. The answer decides',
    '<p>One 40-row table answers it. (“Marking” is the scoring rule that decides whether a program’s answer counts as correct: the metric.) The answer decides')
rep('Nobody has counted what is left once formula spelling is cleaned up.</li>',
    'Nobody has counted what is left once formula spelling is cleaned up (the same compound written as a different string, such as “Ni1.875O2” for NiO).</li>')
rep('Your project’s pilot numbers move from 0.309 to 0.745 (55 scans) with the marking rule alone.</li>',
    'A pilot probe beside your project scores 0.309 under strict marking and 0.745 under lenient marking (n = 55).</li>')
rep('The 40 scans and stored results already sit in your own project folders.</li>',
    'The 40 scans and stored results already sit in your own project folders. It needs two yeses from you: a folder name for the rescue copy, and read-only access to those folders.</li>')

# ---------- (b) before/after table
rep('Three causes: the rule (<span class="num">12 vs 32</span>), out-of-date stored marks (<span class="num">17 vs 32</span>), a different reference library (<span class="num">32 vs 38</span>). On a second set of 20 scans the rule moves scores by only <span class="num">1–3 of 20</span>, while the tools differ by <span class="num">11–13</span>.',
    'Three causes: the rule (<span class="num">12 vs 32</span>), out-of-date marks saved by older scoring code (<span class="num">17 vs 32</span>), a different reference library and local set-up (<span class="num">32 vs 38</span>). The 32 was quoted from notes; the test recounts it. On a second dataset (20 products of real reactions, not weighed mixtures) the rule moves scores by only <span class="num">1–3 of 20</span>, while the two programs differ by <span class="num">11–13</span>.')
rep('The harm is a contaminated “measured” pool. Smaller, still real.',
    'The harm: anyone training or calibrating on “measured” scans is partly using simulated ones without knowing. Smaller, still real.')

# ---------- (c) "what survives": paragraph -> small table
start = s.index('  <p class="note" style="margin:0 0 18px"><b style="color:var(--ink)">What survives, and ties every thread together:</b>')
end = s.index('</p>', start) + len('</p>')
s = s[:start] + '''  <p class="note" style="margin:0 0 8px"><b style="color:var(--ink)">What survives:</b> how an exam is set and marked can move a score as much as the contestants differ. We saw it in three set-ups and not in one.</p>
  <div class="tbl" style="margin-bottom:6px"><table>
    <thead><tr><th style="width:26%">Set-up</th><th style="width:36%">Gap between contestants</th><th>Effect of the exam itself</th></tr></thead>
    <tbody>
      <tr><td class="term">X-ray, 40 weighed scans</td><td><span class="num">38 vs 35</span> of 40: a tie</td><td>Marking rule: <span class="num">12 vs 32</span> of 40</td></tr>
      <tr><td class="term">X-ray, 20 reaction products</td><td><span class="num">11–13</span> of 20</td><td>Marking rule: <span class="num">1–3</span> of 20. The pattern does not hold here.</td></tr>
      <tr><td class="term">Thermoelectrics</td><td>Lookup <span class="num">22.9%</span> vs 5-neighbour model <span class="num">29.4%</span> error, on the 3,593 seen-formula rows</td><td>Split choice: <span class="num">25.5% → 42.2%</span> error</td></tr>
      <tr><td class="term">Company 134-item test</td><td>Lead of about <span class="num">2</span> points</td><td>One standard error: <span class="num">±4.3</span> points (their scores, our arithmetic)</td></tr>
    </tbody>
  </table></div>
  <p class="note" style="margin:0 0 18px">A pattern in our own measurements, not a field-wide fact.</p>''' + s[end:]

# ---------- (e) steps
rep('Tricky-pairs table, the 499-file match table, the “tie or not?” function, a web-only look at harder public test sets.',
    'Tricky-pairs table (unit tests for the marking rule), match table (simulated scans filed as measured), “tie or not?” function, a web-only look at harder public test sets.')
rep('freeze one test list. Trim the two error notes and hold them.',
    'freeze one test list. Trim the two draft error notes (one X-ray dataset’s authors, the thermoelectric database) and hold them.')

# ---------- (d) thermoelectrics or X-ray
start = s.index('  <p class="note" style="margin:0 0 18px"><b style="color:var(--ink)">Thermoelectrics or X-ray?</b>')
end = s.index('</p>', start) + len('</p>')
s = s[:start] + '''  <p class="note" style="margin:0 0 18px"><b style="color:var(--ink)">Thermoelectrics or X-ray?</b> Both lines share the same cheap first steps, so nothing needs choosing for two weeks. After the week-2 sitting the provisional lean is X-ray, in small form: a lab can weigh out known mixtures and get ground truth with no human annotator, while every thermoelectric value is already published, so that line can only be a practice exam. Provisional because no lab is secured, one lab means a one-instrument exam, and the thermoelectric side was checked less hard. The deciding question is in the amber box below.</p>''' + s[end:]

# ---------- (f) rescue card
rep('out of other sessions’ temporary areas into one folder you choose, with a checksum file.',
    'out of the other chats’ temporary areas into one folder you choose, with a checksum file. (Each Claude chat has its own temp folder.)')
rep('This session cannot reach those areas. You, or the sessions that own the files, do the copy. Whether the files still exist is unknown.',
    'This chat cannot reach those areas. Easiest: tell each of the other two chats (main and X-ray) to copy its working files to the folder. Whether the files still exist is unknown.')

# ---------- (g) marking-test card
rep('<div><b>The three marks</b>Strict as stored, lenient as stored, lenient recomputed. The table should reproduce',
    '<div><b>First hour</b>Count the scan files. The notes say 40, 41, 60, 61 and 70. If it is not 40, the 12 / 17 / 32 targets may not reproduce.</div>\n      <div><b>The three marks</b>Strict as stored, lenient as stored, lenient recomputed. Strict = the formula text must match exactly. Lenient = atom fractions within 0.10 (sum of absolute differences). “As stored” = verdicts saved by older scoring code. “Recomputed” = scored again today. The table should reproduce')
rep('the scan-file count is settled (the notes say 40, 41, 60, 61 and 70), and one written line gives the verdict.',
    'the scan-file count is settled, and one written line gives the verdict.')
rep('a dated amendment to your frozen plan,', 'a dated amendment to your project’s frozen (pre-registered) plan,')

# ---------- (h) tricky-pairs card
rep('<div class="tags"><span class="chip xrd">X-ray</span><span class="chip">a few days</span><span class="chip go">low-hanging</span></div>',
    '<div class="tags"><span class="chip xrd">X-ray</span><span class="chip">a few days</span><span class="chip yes">needs read-only OK</span><span class="chip yes">after the rescue</span><span class="chip go">low-hanging</span></div>')
rep('<div><b>The number</b>On 18 hand-built pairs the strict rule disagrees',
    '<div><b>The number</b>The script holds 21 hand-built pairs and scores 18 (the gap is unexplained); the target is about 25. On those 18 the strict rule disagrees')
rep('<div><b>Why no threshold can work</b>NiO and',
    '<div><b>Why no threshold can work</b>Distance = sum of absolute differences of atom fractions, the measure the lenient rule uses. NiO and')
rep('A mirror-image pair that must be “same”. An ordered vs disordered pair marked “specialists disagree”.',
    'A mirror-image pair (left- and right-handed versions of one crystal, identical in a powder scan) that must be “same”. An ordered vs disordered pair (same atoms, arranged neatly or shuffled) marked “specialists disagree”.')
rep('<div><b>Honest limits</b>The ideas are old',
    '<div><b>Honest limits</b>On the 40 scans only formula-level marking is possible; the stored results kept no crystal-structure choice. The ideas are old')

# ---------- (i) match-table card
rep('reads the two archives already in your project data, read only,',
    'reads the two archives already in your project data (RRUFF, an open mineral archive, and opXRD, a pooled open collection from several labs), read only,')
rep('124 of 2,680 opXRD files are exact copies, in 61 groups.',
    '124 of the 2,680 opXRD files on disk are exact copies, in 61 groups (the full collection has 92,552, so a lower bound).')
rep('Does any duplicate pair sit on both sides of your calibration/test split? Expected on your list: 8 suspect rows of 200,',
    'Does any duplicate pair sit on both sides of your split between calibration scans (used to tune the trust score) and test scans? Expected on your list: 8 suspect (possibly calculated) rows among its 200 RRUFF rows,')

# ---------- (j) tie-function card
rep('38 vs 35 of 40 is a 7.5-point gap with an interval of 0.0 to 15.0: a tie. The 40 scans are really 20 powders, each scanned twice. A 134-item test cannot separate 55% from 53%.',
    '38 vs 35 of 40 is a 7.5-point paired gap with an interval of 0.0 to 15.0. It touches zero, so the two cannot be separated. The 40 scans are really 20 powders, each scanned twice. On one company’s 134-item test one standard error is about ±4.3 points (our arithmetic on their reported scores), so 55.3% vs about 53% is a tie.')

# ---------- (k) web-only card
rep('<div class="plain">Harder weighed mixtures may already be public. Open the landing pages only,',
    '<div class="plain">Harder weighed mixtures may already be public: an international contest set with 4- and 7-ingredient mixtures, a set of 240 two-ingredient mixtures, and a series with one ingredient added at 0.12–4.0% by weight. Open the landing pages only,')
rep('<div><b>Also read</b>The X-ray session’s round-5 folder may already hold a dated protocol for the same 40 scans. Extend that one; do not write a second.</div>',
    '<div><b>Also read (needs your read-only OK)</b>An earlier X-ray chat’s folder for a known-answer test on the same 40 scans may already hold a dated protocol and result files (unverified). Extend that one; do not write a second.</div>')
rep('<div><b>Say up front</b>If the hard bands hold',
    '<div><b>Say up front</b>Bands = buckets by how small the smallest ingredient’s share is. If the hard bands hold')

# ---------- (l) thermoelectric small card
rep('<div><b>Done when</b>25.5 / 42.2 / 46.6 and 22.9 / 29.4 / 15.0 come back identical. The test list',
    '<div><b>Done when</b>The same six numbers come back. Median error by split: random 25.5%, papers held out 42.2%, chemical systems held out 46.6%. On the seen-formula rows: lookup 22.9%, 5-neighbour model 29.4%, answer-seeing floor 15.0%. The test list')
rep('Paper IDs only; no rows from the unlicensed database.', 'Paper IDs only; no rows from ESTM, the one source with no licence.')

# ---------- (m) error-notes card
rep('<div class="plain">A courtesy and a door-opener, not the contribution. Cut to the certain items. Send nothing.</div>',
    '<div class="plain">One note to the authors of the largest open recipe-plus-scan dataset (X-ray), one to the thermoelectric database. A courtesy and a door-opener, not the contribution. Cut to the certain items. Send nothing.</div>')
rep('<div><b>The numbers</b>Recipe-plus-scan release: 5 certain items; about 30 of 1,035 samples hold a truly wrong value. Four drafted claims are withdrawn first.</div>',
    '<div><b>The numbers (first note only)</b>5 certain items; about 30 of 1,035 samples hold a truly wrong value. Four claims we drafted earlier are deleted first.</div>')

# ---------- (n) marking-function card
rep('If so it is the natural sixth rule.', 'If so, add it as one more rule beside the five already compared.')

# ---------- (o) noise ladder
rep('Cleaner plot-reading would buy almost nothing.', 'Cleaner plot-reading looks like a small part of the gap.')
rep('<div><b>Honest limits</b>The across-paper rung includes real differences between samples, not only noise. The 15.0% rung covers the 3,593 seen-formula rows and formula-only models.',
    '<div><b>Honest limits</b>The 0.48% rung is 361 comparisons on 102 pairs from one database’s high-scoring papers. The across-paper rung includes real differences between samples, not only noise. The 15.0% rung (the same formula genuinely differs across papers) covers the 3,593 seen-formula rows and formula-only models.')

# ---------- (p) send-notes card
rep('The two error notes (recipe-plus-scan authors first, privately) and a neutral notice about the 499 matching files.',
    'The two trimmed error notes: recipe-plus-scan authors first and privately (their paper is under review), the thermoelectric database second. Plus a neutral notice about the 499 matching files.')

# ---------- (q) hidden TE exam
rep('The draft rulebook still lacks 17 rules and has 22 major issues open.',
    'Our draft rules for such an exam (in the Thermoelectric Benchmark Spec) still lack 17 rules and have 22 major issues open.')

# ---------- (r) tempting, but do not
rep('Every value is already published, so it cannot be hidden, and the 15.0% floor caps what a formula-only model can show.',
    'Every value is already published, so it cannot be hidden. And on the 3,593 of 12,222 rows with seen formulas, even a lookup that sees the answers misses by 15.0%.')
rep('About 1,000 expert-hours; and random guessing scores 20.1% against 21.8% for a perfect method. Nothing to win.',
    'On those labels random guessing scores 20.1% against 21.8% for a perfect method. All 1,216 “manual” checks carry a single editor ID, and 137 of 352 “human” files are the program’s fit unchanged. Nothing to win.')
rep('Of 188 action items in the reports, 3 had the basics.',
    'Of 188 action items in three reports, only 3 said what, how, first step and done test.')

# ---------- (s) ask box
rep('later with a one-page “weigh and scan N powders” request.</p>',
    'later with a one-page “weigh and scan N powders” request. No need to contact anyone before the week-2 sitting.</p>')
rep('A yes to a working session reading your two project folders', 'A yes to a working chat reading your two project folders')
rep('if confidence scoring ships in Dara, shrink to the evaluation harness.',
    'if confidence scoring ships in Dara (the open phase-naming program your project builds on), shrink to the evaluation harness.')
rep('So the rule is not triggered for certain.</p>',
    'So the rule is not triggered for certain. Your call: does AIF count as “ships in Dara”? Read literally it does not, but it is your rule.</p>')

# ---------- (t) trust table
rep('had already been attacked by nine checkers in its own session.', 'had already been attacked by nine checkers in its own chat.')
rep('This session never opened your project folders or another session’s temporary area. Every count about your project comes from the X-ray session’s notes.',
    'This chat never opened your project folders or another chat’s temporary area. Every count about your project comes from the X-ray chat’s notes.')
rep('The fifth experiment round in the main session, and the X-ray session’s own final write-up.',
    'The fifth experiment round in the main chat, and the X-ray chat’s own final write-up.')
rep('      <tr><td class="term">Uneven scrutiny</td>',
    '      <tr><td class="term">Fact-check of this page</td><td>Five more agents checked <span class="num">224</span> statements on this page against the notes and raised <span class="num">95</span> points. 3 statements were plainly wrong (“scans” should be “samples”; “the entire open set” should be “the only weighed set on disk”; “one-day” should be “one-to-two-day”). Most of the rest were missing scope or jargon. One suggested fix was itself wrong and was not applied.</td></tr>\n      <tr><td class="term">Uneven scrutiny</td>')

open(P, 'w', encoding='utf-8').write(s)
print('part B ok', len(s))
import re
for m in re.finditer(r'session', s):
    a = max(0, m.start() - 60); print('SESSION:', s[a:m.end() + 40].replace('\n', ' '))
for m in re.finditer(r'DFT', s):
    a = max(0, m.start() - 60); print('DFT:', s[a:m.end() + 40].replace('\n', ' '))
