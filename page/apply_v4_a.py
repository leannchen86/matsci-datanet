# Part A: hero, map, section 03 cards, dead ends, glossary, reports list
import shutil, sys
P = sys.argv[1]
shutil.copy(P, P.replace('big-picture.html', 'big-picture.v3.bak.html'))
s = open(P, encoding='utf-8').read()

def rep(old, new_, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:80])
    s = s.replace(old, new_)

# ---------- hero
rep('with <b>a test nobody could game</b>', 'with <b>a hidden-label test with fixed rules</b>')
rep('a test set and a marking rule that cannot be passed by memorising', 'a test set and a marking rule that reward more than memorising')
rep('Random splits put the same paper on both sides, like splitting by scan instead of by patient.',
    'Random splits test on formulas and papers the model has already seen, like splitting by scan instead of by patient.')

# ---------- map
rep('Both companies grade with AI judges tuned to agree with experts, not with physical outcomes. One headline score of 55.3% is best-of-7 on <span class="num">134</span> items; a single attempt scores about 36%. And <span class="num">332 of 671</span> published “failed” superconductors were never actually made.',
    'Both companies grade with AI judges tuned to agree with experts, not with physical outcomes. One company’s self-reported 55.3% is best-of-7 on a private <span class="num">134</span>-item test (a single attempt scores about 36%), and its lead over the best outside model is about 2 items: a tie. Separately, in one well-known paper’s list of failed superconductors, <span class="num">332 of the 671</span> entries we extracted were never actually made.')
rep('You said “experimental first”, so this stopped.', 'You pointed out that the focus is measured data, so the simulated-database builds were parked.')
rep('It comes with a built-in checksum and a measured lab-to-lab noise floor.',
    'A physics checksum works on 13,702 of them (one reported number can be recomputed from three others), and published multi-lab tests give a lab-to-lab noise floor of 6 to 19%.')
rep('Open data is small (about 1,400 scans with recipes) and has no independent answer key. Your own dara-conform project sits here.',
    'Open data is small: about 1,400 samples with both a recipe and a raw scan. Its only true answer key is 40 scans of powders mixed at known weights. Your own project, dara-conform (a trust score on top of an automatic phase-naming program), sits here.')
rep('You said the reports were “still a lot”. An audit agreed: of <span class="num">188</span> action items in them, only',
    'You said the report “still is a lot”. An audit agreed: of <span class="num">188</span> action items in the three reports audited, only')
rep('Error lists are ready but unsent.', 'Error lists are drafted but unsent; sending them needs your yes.')

# ---------- section 03, group 1
rep('<div class="what">thermoelectric records fail their own checksum by more than 50%. 266 of them are clean power-of-ten slips.</div>',
    '<div class="what">thermoelectric records fail their own checksum by more than 50%. The check is possible on 13,702 of 55,422 samples. 266 of the failures are clean power-of-ten slips.</div>')
rep('so you can recompute it and compare. A free validator.</div>',
    'so you can recompute it and compare. A free flag, not a fix. Another database already ships a similar filter.</div>')
rep('All 499 patterns in one folder of the opXRD collection have values identical to RRUFF files.',
    'All 499 patterns in one folder of opXRD (a pooled open collection of X-ray files from several labs) have values identical to RRUFF files.')
rep('Usable after cleaning: 1,683 of 7,183 files.</div>',
    'Usable after cleaning: 1,683 of the 7,183 files on disk. That total counts some RRUFF samples twice and holds only 2,680 of opXRD’s 92,552 files.</div>')
rep('''        <div class="big">~0.5% <small>vs 4.2%</small></div>
        <div class="what">Two teams reading the same published plots agree to about half a percent. But 15 of 361 shared records disagree by more than 10%.</div>
        <div class="ml">Reading numbers off plots is not the problem. Data-entry errors are.</div>''',
    '''        <div class="big">15 <small>of 361</small></div>
        <div class="frac"><i style="width:4.2%"></i></div>
        <div class="what">shared comparisons between two databases that read the same published plots differ by more than 10%. Typical disagreement is only 0.5 to 0.9%.</div>
        <div class="ml">Reading numbers off plots is not the problem. Those 15 look like record errors, judged without opening the papers. Scope: 102 sample pairs from one database’s high-scoring papers.</div>''')

# ---------- section 03, group 2
rep('<div class="what">median difference in the same measured property when two papers report the same chemical formula.</div>',
    '<div class="what">median difference in the Seebeck coefficient (voltage per degree) when two papers report the same chemical formula.</div>')
rep('each physical sample is a different image. Lab-to-lab noise on one shared sample is only 6%.</div>',
    'each physical sample is a different image. A published multi-lab test on one shared sample found only about 6% spread for this property.</div>')
rep('Re-scans more than 180 days apart changed their answer in 105 of 136 cases. Ageing and analysis drift cannot be told apart.',
    'Re-scans more than 180 days apart changed their fitted answer in 105 of 136 cases (77%), against 12 of 25 (48%) within 30 days. Exploratory: ageing and analysis drift cannot be told apart.')
rep('''        <div class="big">2.4%</div>
        <div class="frac"><i style="width:2.4%"></i></div>
        <div class="what">of RRUFF powder files state the X-ray wavelength used.</div>
        <div class="ml">Like audio files without a sample rate. Of 353 usable files that do state it, 352 come from one institution.</div>''',
    '''        <div class="big">71 <small>of 3,019</small></div>
        <div class="frac"><i style="width:2.4%"></i></div>
        <div class="what">RRUFF powder files (2.4%) state the X-ray wavelength used.</div>
        <div class="ml">Like audio files without a sample rate. Across the whole usable pool (RRUFF plus opXRD, 1,683 files) only 353 state it, and 352 of those come from one institution.</div>''')

# ---------- section 03, group 3
rep('''        <div class="what">of test samples under a random split come from a paper that is also in the training set.</div>
        <div class="ml">Samples from one paper are near-duplicates: same lab, same batch, small tweaks.</div>''',
    '''        <div class="what">of test papers under a random split also have samples in the training set. Only 40.4% of test formulas do.</div>
        <div class="ml">Samples from one paper are near-duplicates: same lab, same batch, small tweaks. The re-run should print this per sample as well as per paper.</div>''')
rep('''        <div class="what">X-ray side, same effect: the score drops when whole starting ingredients are held out.</div>
        <div class="ml">Macro-F1 (average per-class score) on the open recipe-plus-scan release.</div>''',
    '''        <div class="what">X-ray side, a similar pattern on 1,035 samples: the score drops when whole starting ingredients are held out (rerun: 0.49 → 0.39).</div>
        <div class="ml">Macro-F1 (average per-class score) on the largest open recipe-plus-scan release. Up to half of the drop also appears in a model that sees only temperature.</div>''')

# ---------- section 03, group 4
rep('<span class="lab">lenient match, recomputed</span>', '<span class="lab">lenient match, fresh marks (quoted, not recounted)</span>')
rep('One local set-up, measured by the X-ray session; on a second set of 20 scans the rule moves scores by only 1–3 of 20.</div>',
    'One local set-up, from the X-ray chat’s notes: 12 and 17 were recounted, 32 was not. On a second dataset (20 products of real reactions) the rule moves scores by only 1–3 of 20.</div>')
rep('And all 1,216 human checks carry a single editor ID. Machine vs one annotator, not a gold standard.',
    'All 1,216 checks marked “manual” carry a single editor ID, and 810 of them sit on automated fits. One annotator vs a machine, not a gold standard.')
rep('<div class="what">is the entire open set where the true answer is known by weighing the ingredients.</div>',
    '<div class="what">is the only set on disk where the true answer is known by weighing the ingredients.</div>')
rep('±5 points near 50% accuracy needs about 385 separate powders.</div>',
    '±5 points near 50% accuracy needs about 385 separate powders. At least one harder public set seems to exist; none has been fetched.</div>')
rep('''        <div class="what">is the noise on a 134-item company benchmark whose claimed lead is about 2 points.</div>
        <div class="ml">Separating that gap would need roughly 8,800 test items.</div>''',
    '''        <div class="what">is one standard error on a private 134-item company benchmark whose claimed lead is about 2 points.</div>
        <div class="ml">Their self-reported scores, our arithmetic. Separating that gap would need roughly 8,800 items per model.</div>''')
rep('Every number here came from running code on public files and was re-derived by an independent checker, except where a card names another source.',
    'Most numbers came from running code on public files, and many were re-derived by a second checker. Exceptions: the split table was run once; the X-ray marking numbers come from one chat’s notes on your local set-up (the 32 of 40 is quoted, not recounted); the 6% and the 134-item figures come from published or company sources.')

# ---------- dead ends
rep('Only <span class="num">85 of 266</span> got fixed, and <span class="num">7.2%</span> of fixes were wrong.',
    'Only <span class="num">85 of 266</span> got fixed, at least <span class="num">6</span> of those fixes were wrong, and it fixed <span class="num">0 of 12</span> proven errors.')
rep('<td>Its answers sit in a public file, with no licence and no scoring server.</td><td>Any hidden test needs new scans.</td>',
    '<td>The latest notes say its answers sit in a public file with no licence. Earlier notes said the opposite, and nobody re-checked.</td><td>Either way, a hidden test needs new scans.</td>')
rep('<td>Predict the gain from 10× more simulated data</td><td>The predicted gain is smaller than a 270-item test set can detect.</td>',
    '<td>Predict the gain from 10× more computer-calculated property data</td><td>The predicted gain (0.009–0.040 eV) is smaller than a test set of about 270 compounds can detect (about 0.08 eV).</td>')
rep('<td>“A closed lab made labels without public data”</td><td>You challenged it; it was withdrawn. Their inputs are unknown.</td>',
    '<td>A claim about which data a closed lab did or did not use</td><td>You challenged it; it was withdrawn. Their inputs are unknown.</td>')

# ---------- glossary: four more words
rep('<a href="#words">06 twelve words</a>', '<a href="#words">06 sixteen words</a>')
rep('<h2>Twelve words are enough</h2>', '<h2>Sixteen words are enough</h2>')
rep('''      <tr><td class="term">Known-answer test</td>''',
    '''      <tr><td class="term">Marking rule, marker</td><td>The rule that decides whether a program’s answer counts as correct, and the code that applies it. Strict = formula text must match exactly. Lenient = atom fractions within 0.10.</td><td>The metric and its implementation</td></tr>
      <tr><td class="term">Reference library</td><td>The catalogue of known compounds a program is allowed to pick from. Some are paid, some open.</td><td>The label vocabulary</td></tr>
      <tr><td class="term">Dara, dara-conform</td><td>Dara is an open program that names the phases in a scan. dara-conform is your project: a trust score on top of it.</td><td>A classifier, and calibrated confidence for it</td></tr>
      <tr><td class="term">RRUFF, opXRD</td><td>RRUFF is a long-standing open mineral archive with X-ray files. opXRD is a newer pooled collection of X-ray files from several labs.</td><td>Two public datasets, one partly inside the other</td></tr>
      <tr><td class="term">Known-answer test</td>''')

# ---------- reports list
rep('Parked when you said “experimental first”.', 'Parked when you pointed the work at measured data.')

open(P, 'w', encoding='utf-8').write(s)
print('part A ok', len(s))
