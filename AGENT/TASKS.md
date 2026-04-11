# Tasks & Planned Work

This document tracks improvements an AI agent can work on, organized by area. Items marked **(README TODO)** come from the project's own README wish list. Items marked **(DONE)** were completed in previous sessions.

---

## Recently Completed

- **(DONE)** Split monolithic JSON files into per-entry markdown (`convert_to_md.py`).
- **(DONE)** Write `generate_json.py` to reassemble markdown → `generated/*.json`.
- **(DONE)** Move poset computation from Julia notebook to client-side JS (`buildPosetFromTheorems` in `process.js`). The Julia notebook is now retired.
- **(DONE)** Update all HTML pages to fetch from `generated/` instead of `data/`.
- **(DONE)** Delete old `JSON_FORMATTING.md` (conventions now in AGENT/OVERVIEW.md).

---

## Zoo Import Cleanup (High Priority)

After bulk-importing classes and theorems from the Complexity Zoo wikitext, a number of issues need manual attention.

### Class Description Quality

Many class `.md` files ended up with truncated or nearly empty descriptions because the parser cut off mid-sentence (likely at an unhandled wiki markup construct), or because the Zoo's own text was very thin. Examples:

- `data/classes/language/P^NP[k].md` — body reads `"Equals P with 2^k-1 parallel queries to NP (i.e."` and cuts off there.
- `data/classes/language/AxP.md` — body just says it's usually called AP, with no actual definition of what the class *is*.

**Fix:** Go back through the scraped wikitext pages for each affected class, find the full text, and complete or rewrite the description field. Focus on classes that have no usable definition at all first.

### Parameterized-Family Classes

Several class files were created for *families* of classes parameterized by a function (e.g. `PrSPACE(f(n))`, `DSPACE(f(n))`-style entries). These shouldn't appear as concrete nodes in an inclusion diagram, but we still want to track them as documentation.

**Proposed fix:** Add a `concrete: false` flag to the YAML frontmatter of these family entries. The frontend should skip `concrete: false` classes when building the poset diagram, but still show them in the class list/search with a note like "this is a class family, not a single class."

Files to audit and tag `concrete: false` (non-exhaustive list, search for `f(n)` or similar in class names/bodies):
- `PrSPACE_f_n.md` (and anything else with `_f_n` or `_f_` in the name)
- Any class whose name contains an explicit function parameter
- Review `data/EXCLUDED.md` for classes that should have been caught here but were accidentally included

### Theorems Referencing Non-Existent or Renamed Classes

Some theorem files reference class names that were renamed, excluded, or never imported. For example, `AxP` was renamed from AP and isn't in the standard namespace; theorems about it may be mislinked.

**Fix:** After class cleanup is more complete, run a validation pass that checks every class name cited in a theorem's `content:` field against the actual set of class files. Report unresolved names.

### Theorem Content Encoding

A handful of theorem files use ad-hoc encodings (e.g. `&&` for "and" in `MAsub...&&MAsub....md`, `_poly` suffix for advice classes). These are functional but inconsistent with how `process.js` parses them.

**Fix:** Audit and normalize these to whatever convention `process.js` ends up adopting, once the parser is extended.

---

## Data Expansion

These are the most impactful tasks for the project's mission — a more complete database means a more useful tool.

- **Add more classes, theorems, and references.** The `TODO.md` file has several concrete leads (SBP inclusions, DCL ⊆ LIN, Adleman's theorem, Cai's theorem, etc.) that should be formalized into theorem markdown files with proper `content` and `ref` fields.
- **Formalize conjectures.** Many conjectures have `implies`/`not_implies` fields that the viewer doesn't expose yet. Ensuring those fields are consistently populated is still valuable for when the viewer catches up.
- **Wire up `problems.json`.** Named computational problems (3SUM, Factoring, etc.) with typed variants exist in the data but are invisible to the frontend. Adding a problems list page and a problem detail page would surface this data.

## Viewer Features (from README TODOs)

- **(README TODO) Edge provenance.** Click an edge in the Hasse diagram to see which theorem justifies it. Since edges are minimal (transitive reduction), it's always a single theorem. The poset builder could be extended to track proof chains.
- **(README TODO) Class comparison.** Select two classes and display what is known about their relationship, including a minimal set of theorems implying those relationships.
- **(README TODO) Other problem types in the diagram.** The data already tags classes by problem type; the diagram should let users toggle which types are visible. `buildPosetFromTheorems` already accepts a `classType` parameter.
- **(README TODO) Non-equality display.** Show which classes are known to be strictly different. UI design is open.
- **(README TODO) Hypothesis toggles.** Turn hypotheses on/off (e.g. "PH collapses") and re-render the diagram with the resulting implications.
- **(README TODO) Markdown/LaTeX rendering.** Class and theorem descriptions often contain LaTeX-style notation that currently renders as raw text.

## Parser & Pipeline Improvements

- **Expand the theorem content parser.** The current parser (in `process.js`) handles simple `A⊆B` and `A=B` clauses. Parameterized theorems (those with `{f}` binders and conditions like `f≥log`) are skipped. Supporting at least the common patterns would increase coverage.
- **Parse class definitions.** The README envisions definitions like `QMA = QIP[1]` or `NP = NTIME(n^O(1))` being machine-readable, enabling automatic derivation of more inclusions.
- **Expand `processString` link types.** `{prob:…}` and `{conj:…}` appear in data strings but `process.js` doesn't expand them into links yet. Adding those two cases is a small change.
- **Run `generate_json.py` in CI.** Currently it must be run locally. A GitHub Actions step could regenerate `generated/` on every push to ensure the JSON stays in sync.

## Code Quality & Developer Experience

- **Unify Bootstrap versions.** `hasse.html` loads Bootstrap 4.3.1 while the other pages use 5.3.0. Migrating `hasse.html` to 5.x would remove the inconsistency.
- **Add basic validation tests.** JSON schema validation for the data files, and checks that all cross-references (`related`, `properties`, `impliedby`, `{lang:…}` targets) resolve to real entries. This could run in CI.
- **Consistent naming.** The npm package is `ComplexityViewer`, the site says `ComplexityBase`, and the repo is `ZooClasses`. Not urgent, but worth aligning eventually.
- **Retire the Julia notebook.** `Classes_Process.ipynb` is now superseded by `process.js` and could be removed or archived. Similarly `testgraph.tex`.

## Stretch Goals

- **Properties on classes.** The README mentions tracking closure properties (complement, concatenation, intersection) and "low for itself." The `properties.json` schema can support this, but the data isn't there yet.
- **Uniformity annotations.** Distinguishing "nonuniform AC^1" from "logspace-uniform AC^1" in a structured way, including which uniformity notions are equivalent.
- **Relativized information.** Tracking which inclusions relativize, and which oracle separations are known, so the viewer could show "this edge holds relative to all oracles" vs. "there exists an oracle separating these."
