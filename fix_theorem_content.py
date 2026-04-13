"""
fix_theorem_content.py

Apply systematic name substitutions to theorem YAML content/name fields
where old-style class names are used.

Run once; re-running is safe (substitutions are idempotent).
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

THEOREMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "theorems")

# Ordered list of (pattern, replacement) applied to content (and name where name == content).
# Using raw substrings (no word boundary issues) but careful ordering avoids over-substitution.
SUBS = [
    # Advice class suffixes: do longer matches first to avoid partial matches
    ("NEXP_poly", "NEXP/poly"),
    ("NE_poly",   "NE/poly"),
    ("NL_poly",   "NL/poly"),
    ("UL_poly",   "UL/poly"),
    ("NP_poly",   "NP/poly"),
    ("PP_poly",   "PP/poly"),
    ("EXP_poly",  "EXP/poly"),
    ("FNL_poly",  "FNL/poly"),
    ("\u2295L_poly", "\u2295L/poly"),   # ⊕L_poly → ⊕L/poly
    ("BQP_qpoly", "BQP/qpoly"),
    ("P_poly",    "P/poly"),            # after NP_poly, NE_poly etc.
    ("L_poly",    "L/poly"),            # catch remaining _poly
    # Dot-notation classes
    ("BP_dot_NP", "BP\u2022NP"),        # BP•NP
    ("BP_dot_L",  "BP\u2022L"),         # BP•L
    ("ZP_dot_L",  "ZP\u00b7L"),         # ZP·L
    # Sharp-P oracle — longer match first
    ("P_SharpP1", "P^SharpP[1]"),
    ("P_SharpP",  "P^\u0023P"),         # P^#P
    # Polynomial hierarchy
    ("S2P",       "S_2P"),
    ("\u03a32",   "Sigma_2P"),          # Σ2 → Sigma_2P
    ("\u03a02",   "\u03a0_2P"),         # Π2 → Π_2P
    ("\u03942",   "\u0394_2P"),         # Δ2 → Δ_2P
    # Equal-class notations
    ("C_eqAC^0",  "C_=AC^0"),
    ("coC_eqP",   "coC_=P"),
    ("BC_eqP",    "BC_=P"),
    # Class name corrections
    ("ACKERMANN", "Ack"),
    ("AW[star]",  "AW[*]"),
    ("1NAuxPDA_p","1NAuxPDA^p"),
    ("NAuxPDA_p", "NAuxPDA^p"),
    ("MIPns",     "MIP^ns"),
    # Polylog bracket forms
    ("IP_polylog_", "IP[polylog]"),
    ("AM_polylog_", "AM[polylog]"),
    # P^NP[log] shorthand
    ("P_NP_log_",  "P^NP[log]"),
    # Uniform NC^1
    ("NC^1_uniform_", "NC^1"),
    # DP class (rename in content only; class file will also be renamed separately)
    # (handled by class file rename, not content fix)
]

def apply_subs(text):
    for old, new in SUBS:
        text = text.replace(old, new)
    return text

fixed = 0
for fname in sorted(os.listdir(THEOREMS_DIR)):
    if not fname.endswith('.md'):
        continue
    path = os.path.join(THEOREMS_DIR, fname)
    with open(path, encoding='utf-8') as f:
        original = f.read()
    
    # Parse YAML frontmatter
    if not original.startswith('---'):
        continue
    end = original.find('\n---', 3)
    if end < 0:
        continue
    frontmatter = original[3:end]
    body = original[end+4:]
    
    # Apply subs to frontmatter lines with content: or name:
    lines = frontmatter.split('\n')
    new_lines = []
    changed = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('content:') or stripped.startswith('name:'):
            new_line = apply_subs(line)
            if new_line != line:
                changed = True
                line = new_line
        new_lines.append(line)
    
    if not changed:
        continue
    
    new_fm = '\n'.join(new_lines)
    new_content = f'---{new_fm}\n---{body}'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  Fixed: {fname}")
    fixed += 1

print(f"\nFixed {fixed} theorem file(s).")
