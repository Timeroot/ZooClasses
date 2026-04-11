# ZooClasses (ComplexityBase) — Overview

## What This Is

ZooClasses is a machine-readable database of computational complexity classes, theorems relating them, and supporting references. It aims to be a structured, strongly-typed counterpart to the [Complexity Zoo](https://complexityzoo.net/Complexity_Zoo) wiki. The live viewer is deployed at [ohaithe.re/ZooClasses/](https://ohaithe.re/ZooClasses/) under the name **ComplexityBase**.

## Goals

1. **Machine-readability.** All data lives in per-entry markdown files with YAML frontmatter. Theorems have parseable `content` fields that a program can turn into inclusion/equality/separation edges in a class graph.

2. **Provenance.** Every edge in the Hasse diagram traces back to a named theorem with a bibliographic reference. Following a chain of inclusions should expose the *why*, not just the *what*.

3. **Strong typing of problem kinds.** The database distinguishes Language, Promise Problem, Function Problem, Optimization Problem, Parameterized Language, Sampling Problem, and more. Functors between these hierarchies are a long-term aspiration.

4. **Browsability.** A lightweight static site lets users explore the inclusion diagram, filter by properties, search classes, and drill into individual classes, theorems, and references.

## Current State (as of April 2026)

| Area | Status |
|------|--------|
| **Language classes & inclusions** | Substantial coverage (~111 classes, ~262 theorems). The Hasse diagram is computed client-side from `classes.json` + `theorems.json` — no offline build step needed. |
| **Parameterized classes** | 12 classes with data; the class detail page computes their poset on the fly. Not yet in the Hasse diagram. |
| **Other problem types** | Present in `problem_types.json` and partially in `data/classes/` (function, promise, sampling) but not yet surfaced in the diagram. |
| **Conjectures** | 7 conjectures stored with `implies`/`not_implies` fields, but the viewer only lists proved theorems. |
| **Problems** | 9 named computational problems with typed variants. Not consumed by any frontend page yet. |
| **Properties / filters** | Property tags (`quantum`, `circuit`, `nonuniform`, etc.) are defined and assigned to classes. The Hasse page has tri-state filter checkboxes for them. |
| **References** | 27 references with short keys (e.g. `Bor77`) that theorem pages resolve into descriptions and URLs. |
| **Tests / CI** | No automated tests. The only GitHub Action bumps the parent Pages repo's submodule pointer on push to `main`. |

## Key Design Decisions

- **No build step for the viewer.** HTML pages load JSON at runtime via `fetch` and render with vanilla JS + D3 + Bootstrap. The poset (inclusion graph, equivalence classes, covering relations) is computed entirely client-side in `process.js`.
- **One file per entry.** Classes, theorems, conjectures, references, and problems are each stored as individual markdown files with YAML frontmatter under `data/`. A Python script (`generate_json.py`) assembles them into the JSON files the frontend fetches.
- **Theorem content is a mini-language.** Statements like `NC^1⊆L` or `{f}(f≥log)⟹(NSPACE(f)=coNSPACE(f))` are parsed by simple string splitting on Unicode relation characters. Parameterized (curly-brace) statements are deliberately skipped when the parser can't handle them yet.

## Formatting Conventions for Theorem Content

- Useful relation characters: `⊂ ⊆ ⊃ ⊇ ⊈ ⊉ = ⟹ Ω Σ Π Δ`
- Avoid `≠`; prefer `⊂` or `⊈` instead. Break down a non-equality into directional non-containments.
- Avoid `∪` and `∩`; prefer writing separate `&&`-joined statements. E.g. `A⊆B&&A⊆C` instead of `A⊆B∩C`.
- Theorem `name` is human-readable (e.g. `P != NP`); `content` is the parseable statement (e.g. `P⊂NP`).
