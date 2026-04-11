# ZooClasses (ComplexityBase) — Overview

## What This Is

ZooClasses is a machine-readable database of computational complexity classes, theorems relating them, and supporting references. It aims to be a structured, strongly-typed counterpart to the [Complexity Zoo](https://complexityzoo.net/Complexity_Zoo) wiki. The live viewer is deployed at [ohaithe.re/ZooClasses/](https://ohaithe.re/ZooClasses/) under the name **ComplexityBase**.

## Goals

1. **Machine-readability.** All data lives in JSON files with a consistent schema. Theorems have parseable `content` fields that a program can turn into inclusion/equality/separation edges in a class graph.

2. **Provenance.** Every edge in the Hasse diagram traces back to a named theorem with a bibliographic reference. Following a chain of inclusions should expose the *why*, not just the *what*.

3. **Strong typing of problem kinds.** The database distinguishes Language, Promise Problem, Function Problem, Optimization Problem, Parameterized Language, Sampling Problem, and more. Functors between these hierarchies are a long-term aspiration.

4. **Browsability.** A lightweight static site lets users explore the inclusion diagram, filter by properties, search classes, and drill into individual classes, theorems, and references.

## Current State (as of April 2026)

| Area | Status |
|------|--------|
| **Language classes & inclusions** | Substantial coverage. The diagram renders correctly when the Julia notebook has been run to produce `generated/langdata.json`. |
| **Parameterized classes** | Schema and some data exist; viewer support is minimal. |
| **Other problem types** | Present in `problem_types.json` and partially in `classes.json` but not yet surfaced in the diagram. |
| **Conjectures** | Stored in `conjectures.json` with an `implies` field, but the viewer only lists proved theorems. |
| **Problems** | `problems.json` has named computational problems with typed variants. Not consumed by any frontend page yet. |
| **Properties / filters** | Property tags (`quantum`, `circuit`, `nonuniform`, etc.) are defined and assigned to classes. The Hasse page has tri-state filter checkboxes for them. |
| **References** | `references.json` provides short keys (e.g. `Bor77`) that theorem pages resolve into descriptions and URLs. |
| **Tests / CI** | No automated tests. The only GitHub Action bumps the parent Pages repo's submodule pointer on push to `main`. |

## Key Design Decisions

- **No build step for the viewer.** HTML pages load JSON at runtime via `fetch` and render with vanilla JS + D3 + Bootstrap. This keeps the repo deployable as a plain static site.
- **Julia for graph computation.** The `Classes_Process.ipynb` notebook parses theorem content strings, builds a poset, computes transitive reductions, and writes `generated/langdata.json`. This is the only step that requires a local toolchain beyond a browser.
- **Theorem content is a mini-language.** Statements like `NC^1⊆L` or `{f}(f≥log)⟹(NSPACE(f)=coNSPACE(f))` are parsed by simple string splitting on Unicode relation characters. Parameterized (curly-brace) statements are deliberately skipped when the parser can't handle them yet.
