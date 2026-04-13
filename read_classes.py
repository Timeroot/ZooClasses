"""Quick utility to read class files by name."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
classes_dir = 'data/classes/language'
targets = ['CC^0', 'PARITY', 'AW[star].md', 'C_=AC^0', 'NC^0', 'PhP', 'SF', 'CLOG', 
           'mTC^0', 'mcoNL', 'FPT_nu', 'FPT_su', 'RPP', 'AxP', 'DisNP',
           'AW[P]', 'AW[SAT]', 'AlgP_poly', 'VC_or', 'TALLY', 'WAPP', 'LOGSNP',
           'XNLP', 'XP_uniform', 'para-P']
for f in sorted(os.listdir(classes_dir)):
    path = os.path.join(classes_dir, f)
    with open(path, encoding='utf-8') as fh:
        c = fh.read()
    name_line = [l for l in c.split('\n') if l.startswith('name:')]
    name = name_line[0].replace('name:', '').strip().strip('"') if name_line else f
    if name in targets or f.rstrip('.md') in targets or f in [t+'.md' for t in targets]:
        print('==' + name + ' (' + f + ')==')
        print(c[:500])
        print()
