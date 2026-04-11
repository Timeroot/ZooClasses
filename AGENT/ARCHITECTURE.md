# Architecture

## Repository Layout

```
ZooClasses/
├── data/                         # Canonical source-of-truth (one markdown file per entry)
│   ├── classes/                   #   Complexity classes, in subfolders by problem type
│   │   ├── language/              #     e.g. BPP.md, NP.md, P.md, …
│   │   ├── parameterized/         #     e.g. FPT.md, W[1].md, …
│   │   ├── function/              #     e.g. FNP.md, #P.md, …
│   │   ├── promise/               #     e.g. PromiseBPP.md, PromiseQMA.md, …
│   │   └── sampling/              #     e.g. IQP.md, DQC1S.md
│   ├── theorems/                  #   Proved theorems (e.g. Sipser–Lautemann theorem.md)
│   ├── conjectures/               #   Conjectures (e.g. P!=NP.md)
│   ├── references/                #   Bibliography (e.g. Bor77.md)
│   ├── problems/                  #   Named computational problems (e.g. 3SUM.md)
│   ├── properties.json            #   Tags for classes (small, stays as JSON)
│   └── problem_types.json         #   Problem-type definitions (small, stays as JSON)
│
├── generated/                     # Assembled by generate_json.py from data/
│   ├── classes.json               #   All classes in one array
│   ├── theorems.json              #   All theorems in one array
│   ├── conjectures.json           #   All conjectures in one array
│   ├── references.json            #   All references in one array
│   ├── problems.json              #   All problems in one array
│   ├── properties.json            #   Copied from data/
│   └── problem_types.json         #   Copied from data/
│
├── generate_json.py               # Reads data/**/*.md → writes generated/*.json
├── convert_to_md.py               # One-off: converted old monolithic JSON → per-entry markdown
│
├── index.html                     # Landing page ("ComplexityBase" hub)
├── hasse.html                     # Interactive inclusion diagram (D3 + dagre-d3)
├── classlist.html                 # Filterable table of all classes by problem type
├── class.html                     # Single-class detail page (?name=…)
├── thmlist.html                   # Table of proved theorems
├── theorem.html                   # Single-theorem detail page (?name=…)
├── reflist.html                   # Reference index
├── reference.html                 # Single-reference detail page (?name=…)
├── about.html                     # Goals / attribution
│
├── main.js                        # Client-side logic for hasse.html (graph rendering)
├── process.js                     # Shared: link expansion + poset computation from theorems
├── app.js                         # Minimal Express dev server (serves static files on :3000)
│
├── Classes_Process.ipynb           # Legacy Julia notebook (retired; logic now in process.js)
├── package.json                   # npm: d3 + express
├── testgraph.tex                  # Example TikZ graph from the old notebook
├── .github/workflows/main.yml    # CI: bumps submodule pointer in the GitHub Pages repo
├── .gitignore
├── README.md
└── TODO.md                        # Informal research notes and paper links
```

## Data Model

### Classes (`data/classes/<type>/`)

Each `.md` file has YAML frontmatter and a markdown body:

```yaml
---
name: BPP
related:
  - PromiseBPP
  - ZPP
  - RP
properties:
  - turing
---
Bounded error Probabilistic Polynomial time. …
```

- The subfolder determines the problem type (`language/` → Language, `parameterized/` → Parameterized Language, etc.).
- `related` is an informal cross-reference list of other class names.
- `properties` must be names from `data/properties.json`.
- A `## Notes` section in the body becomes the `notes` field in JSON.

### Theorems & Conjectures (`data/theorems/`, `data/conjectures/`)

```yaml
---
name: Sipser–Lautemann theorem
content: "BPP⊆Σ2&&BPP⊆Π2"
ref: "https://en.wikipedia.org/wiki/…"
priority: 2
---
```

- `content` is the machine-parseable statement. Uses Unicode relation characters (⊆, ⊇, =, ⊊, ⊂, ⊈, ⊉). Parameterized statements wrap parameters in `{f}` and are joined with `&&`.
- `ref` can be a URL, prose, or a key into `references.json` (e.g. `{ref:Bor77}`).
- `impliedby` names another theorem this one follows from.
- `priority` optionally sets the proof "depth" (lower = simpler/earlier).
- Conjectures additionally use `implies`, `not_implies`, and may have a `desc` in the body.

### References (`data/references/`)

```yaml
---
name: Bor77
url:
  - "https://doi.org/10.1137/0206054"
---
A. Borodin. On relating time and space to size and depth, SIAM J. Computing 6:733-744, 1977.
```

### Problems (`data/problems/`)

Named computational problems with a `## Variants` section listing typed variants (each with `### id`, `- **Type:**`, `- **Description:**`, and optional notes).

## Processing Pipeline

### 1. Markdown → JSON (`generate_json.py`)

Run `python generate_json.py` to assemble per-entry markdown files into the JSON arrays the frontend expects. Outputs go to `generated/`. Also copies `properties.json` and `problem_types.json` as-is.

### 2. Client-Side Poset Computation (`process.js`)

`buildPosetFromTheorems(classes, theorems, classType)` runs in the browser on page load:

1. Filters classes by type, collects their names.
2. Parses each theorem's `content`: splits on `&&`, finds Unicode relation characters, normalizes direction.
3. Builds direct ⊆ edges, then computes transitive closure via BFS.
4. Identifies equivalence classes (mutual reachability) and picks canonical representatives from a preference list.
5. Computes covering relations (children = immediate supersets with no intermediate canonical class).
6. Logs warnings for unexpected minimals/maximals.
7. Returns data in the same shape the old `langdata.json` had: `{ name, desc, children, equals, related, notes, properties }`.

### 3. Client-Side Link Expansion (`process.js`)

`processString(str)` expands inline references in description strings:

- `{lang:ClassName}` → link to `class.html?name=ClassName`
- `{thm:ThmName}` → link to `theorem.html?name=ThmName`
- `{ref:RefKey}` → link to `reference.html?name=RefKey`

`{prob:…}` and `{conj:…}` appear in data but are **not yet expanded**.

## Frontend Viewer

### Hasse Diagram (`hasse.html` + `main.js`)

- Fetches `generated/classes.json` and `generated/theorems.json`.
- Calls `buildPosetFromTheorems` to compute the Language poset client-side.
- Builds equivalence classes; optionally expands or collapses equal classes.
- Computes transitive closure (BFS), then draws only the transitive **reduction** over visible nodes.
- Renders with **dagre-d3** (layered DAG layout) inside an SVG with pan/zoom.
- Tri-state property filter checkboxes (neutral / must-have / must-not-have); `nonuniform` defaults to "excluded."
- Clicking a node shows its description, related classes, and links in a side panel.

### List & Detail Pages

- **classlist.html** — all classes, filterable by problem type.
- **class.html** — merges static class data with poset data (children, subsets, equals), computed on the fly for the class's problem type.
- **thmlist.html** — proved theorems only (not conjectures).
- **theorem.html** — resolves `ref` against `references.json` when possible.
- **reflist.html / reference.html** — bibliography index; backlinks by searching for `{ref:Key}` across data.

### Tech Stack

- Bootstrap (4.3.1 on `hasse.html`, 5.3.0 elsewhere).
- D3 v5 + dagre-d3 + graphlib-dot from CDN.
- No bundler, no build step — plain static HTML.

## Deployment

- The site is served as static files from the GitHub Pages repo `Timeroot/Timeroot.github.io`, where this repo is included as a **git submodule**.
- The GitHub Action in `.github/workflows/main.yml` triggers on push to `main` and bumps the submodule pointer in the Pages repo, then commits and pushes.
- `generate_json.py` must be run locally after editing markdown files, and `generated/` committed. There is no CI step for this yet.
