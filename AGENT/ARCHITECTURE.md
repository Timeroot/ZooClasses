# Architecture

## Repository Layout

```
ZooClasses/
├── data/                      # Canonical source-of-truth JSON database
│   ├── classes.json           # Complexity classes (name, type, desc, properties, …)
│   ├── theorems.json          # Proved theorems with parseable content
│   ├── conjectures.json       # Conjectured relationships (same schema as theorems + extras)
│   ├── references.json        # Bibliography (short key → description + URLs)
│   ├── properties.json        # Tags for classes (quantum, circuit, nonuniform, …)
│   ├── problem_types.json     # Problem-type definitions (Language, Promise Problem, …)
│   ├── problems.json          # Named computational problems with typed variants
│   └── JSON_FORMATTING.md     # Editorial conventions for the JSON files
│
├── generated/                 # NOT in repo — produced by the notebook
│   ├── langdata.json          # Language-class poset for the Hasse viewer
│   ├── paramlangdata.json     # Parameterized-class poset (not yet consumed)
│   └── references.json        # Copy of references (notebook artifact)
│
├── Classes_Process.ipynb      # Julia notebook: parses theorems → builds poset → writes generated/
│
├── index.html                 # Landing page ("ComplexityBase" hub)
├── hasse.html                 # Interactive inclusion diagram (D3 + dagre-d3)
├── classlist.html             # Filterable table of all classes by problem type
├── class.html                 # Single-class detail page (?name=…)
├── thmlist.html               # Table of proved theorems
├── theorem.html               # Single-theorem detail page (?name=…)
├── reflist.html               # Reference index
├── reference.html             # Single-reference detail page (?name=…)
├── about.html                 # Goals / attribution
│
├── main.js                    # Client-side logic for hasse.html (graph rendering)
├── process.js                 # Shared link-expansion helpers ({lang:…}, {thm:…}, {ref:…})
├── app.js                     # Minimal Express dev server (serves static files on :3000)
│
├── package.json               # npm: d3 + express
├── testgraph.tex              # Example TikZ graph output from the notebook
├── .github/workflows/main.yml # CI: bumps submodule pointer in the GitHub Pages repo
├── .gitignore
├── README.md
└── TODO.md                    # Informal research notes and paper links
```

## Data Model

### Classes (`data/classes.json`)

Each entry represents a complexity class:

```json
{
  "name": "BPP",
  "type": "Language",
  "desc": "Bounded-Error Probabilistic Polynomial Time …",
  "properties": ["turing", "complement"],
  "related": ["RP", "coRP", "ZPP"],
  "notes": "…"
}
```

- `type` must match a name in `problem_types.json`.
- `properties` must be names from `properties.json`.
- `related` is an informal cross-reference list of other class names.

### Theorems & Conjectures (`data/theorems.json`, `data/conjectures.json`)

Same core shape:

```json
{
  "name": "Sipser–Lautemann theorem",
  "content": "BPP⊆Σ2P∩Π2P",
  "ref": "https://en.wikipedia.org/wiki/Sipser%E2%80%93Lautemann_theorem",
  "impliedby": "…",
  "priority": 3
}
```

- `content` is the machine-parseable statement. Uses Unicode relation characters (⊆, ⊇, =, ⊊, ⊋, ≠). Parameterized statements wrap parameters in `{f}` and are joined with `&&`.
- `ref` can be a URL, prose, or a key into `references.json`.
- `impliedby` names another theorem this one follows from; the notebook walks `impliedby` chains to compute proof priority.
- `priority` optionally overrides the computed priority (lower = simpler/earlier).

Conjectures additionally use `implies`, `not_implies`, `desc`, and may reference conjectures/theorems via `{conj:…}` or `{thm:…}`.

### References (`data/references.json`)

```json
{
  "name": "Bor77",
  "desc": "Borodin, 1977. …",
  "url": ["https://…"]
}
```

### Properties (`data/properties.json`)

```json
{ "name": "quantum", "desc": "Uses quantum computation." }
```

### Problem Types (`data/problem_types.json`)

```json
{
  "name": "Language",
  "desc": "A decision problem …",
  "isalso": [["Promise Problem", "Every language is a promise problem with …"]]
}
```

### Problems (`data/problems.json`)

Named computational problems (e.g. 3SAT, Factoring) with multiple typed variants. Not yet wired to the frontend.

## Processing Pipeline

### 1. Julia Notebook (`Classes_Process.ipynb`)

The notebook is the **compiler** that turns the JSON database into viewer-ready data:

1. Loads all JSON files from `data/`.
2. Validates that cross-references (properties, related classes) are consistent.
3. Builds a `LangPoset` — a directed graph of class names where edges carry a `KnownType(valid, proof, priority)`.
4. Iterates `theorems.json`, parsing each `content` string:
   - Splits on `&&`.
   - Finds a single Unicode relation character per clause.
   - Normalizes direction (⊇ → swapped ⊆, etc.).
   - Calls `add_leq!`, `add_equals!`, or `add_notleq!` to update the poset.
   - Skips parameterized (`{…}`) statements it can't handle yet.
5. Computes equivalence classes, picks canonical representatives, and finds covering relations (immediate children in the Hasse diagram).
6. Writes `generated/langdata.json` (and `paramlangdata.json` for parameterized classes).

### 2. Client-Side Link Expansion (`process.js`)

Runs in the browser. Expands inline references in description strings:

- `{lang:ClassName}` → link to `class.html?name=ClassName`
- `{thm:ThmName}` → link to `theorem.html?name=ThmName`
- `{ref:RefKey}` → link to `reference.html?name=RefKey`

`{prob:…}` and `{conj:…}` appear in data but are **not yet expanded** by this script.

## Frontend Viewer

### Hasse Diagram (`hasse.html` + `main.js`)

- Fetches `generated/langdata.json`.
- Builds equivalence classes; optionally expands or collapses equal classes.
- Computes transitive closure (BFS), then draws only the transitive **reduction** over visible nodes.
- Renders with **dagre-d3** (layered DAG layout) inside an SVG with pan/zoom.
- Tri-state property filter checkboxes (neutral / must-have / must-not-have); `nonuniform` defaults to "excluded."
- Clicking a node shows its description, related classes, and links in a side panel.

### List & Detail Pages

- **classlist.html** — all classes from `classes.json`, filterable by problem type.
- **class.html** — merges static data from `classes.json` with structural data (children, subsets, equals) from `generated/langdata.json`.
- **thmlist.html** — proved theorems only (not conjectures).
- **theorem.html** — resolves `ref` against `references.json` when possible.
- **reflist.html / reference.html** — bibliography index; backlinks found by searching for `{ref:Key}` across all data.

### Tech Stack

- Bootstrap (4.3.1 on `hasse.html`, 5.3.0 elsewhere — minor inconsistency).
- D3 v5 + dagre-d3 + graphlib-dot from CDN.
- No bundler, no build step — plain static HTML.

## Deployment

- The site is served as static files from the GitHub Pages repo `Timeroot/Timeroot.github.io`, where this repo is included as a **git submodule**.
- The GitHub Action in `.github/workflows/main.yml` triggers on push to `main` and bumps the submodule pointer in the Pages repo, then commits and pushes.
- `generated/langdata.json` must be produced locally by running the Julia notebook before the site is fully functional. It is **not** generated by CI.
