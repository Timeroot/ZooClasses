import os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
classes_dir = 'data/classes/language'
targets = {
    '3SUM-hard', 'AmpP-BQP', 'FPL', 'FPR', 'K', 'LogFew', "MA'", 'MM', 'MPC', 'ModP',
    'NLO', 'SZK_h', 'NISZK_h', 'PKC', 'PLF', 'PLL', 'PL_1', 'PIO', 'PINC', 'PSK', 
    'PTAPE', 'PT_1', 'PermUP', 'PQUERY', 'R_HL', 'CNP', 'CP',
    'coSPARSE', 'coUCC', 'AW[*]', 'naCQP', 'NPMV_t-sel', 'NPSV_t-sel',
    'EQP_K', 'BPP_tt', 'P_hash_NP', 'TREE-REGULAR',
    'HeurPP', 'S_2E',
}
for f in sorted(os.listdir(classes_dir)):
    path = os.path.join(classes_dir, f)
    with open(path, encoding='utf-8') as fh:
        c = fh.read()
    lines = c.split('\n')
    name_line = [l for l in lines if l.startswith('name:')]
    name = name_line[0].replace('name:', '').strip().strip('"') if name_line else f
    if name in targets:
        print('== ' + name + ' ==')
        print(c[:400])
        print()
