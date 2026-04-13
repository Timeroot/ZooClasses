"""Mark specific classes as concrete: false."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
classes_dir = 'data/classes/language'
targets = [
    'S_2-EXP\u2022P^NP',  # caged/joke class
    'coSPARSE',            # empty definition  
    'PIO',                 # function class (multi-bit output)
    'PLL',                 # TFNP function class
    'PODN',                # TFNP function class
    'SE',                  # FNP search problem class
]
for f in sorted(os.listdir(classes_dir)):
    path = os.path.join(classes_dir, f)
    with open(path, encoding='utf-8') as fh:
        content = fh.read()
    lines = content.split('\n')
    name_lines = [l for l in lines if l.startswith('name:')]
    if not name_lines:
        continue
    name = name_lines[0].replace('name:', '').strip().strip('"')
    if name in targets and 'concrete: false' not in content:
        # Insert concrete: false after the name line
        new_lines = []
        added = False
        for line in lines:
            new_lines.append(line)
            if line.startswith('name:') and not added:
                new_lines.append('concrete: false')
                added = True
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(new_lines))
        print('Marked concrete: false: ' + name)
