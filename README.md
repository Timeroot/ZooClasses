## See [live version](https://ohaithe.re/ZooClasses/)

This aims to be a machine-readable version of the [ComplexityZoo](https://complexityzoo.net/Complexity_Zoo). The Complexity Zoo is a Wiki maintained by many, so it will likely always be more complete and well-researched than this is. "Machine-readable" is deliberately left slightly ambiguous, but the principle is that when more of the information is stored in a more structured form, it can be synthesized and browsed more efficiently.

For example: a simple [Hasse diagram](https://en.wikipedia.org/wiki/Hasse_diagram) can indicate which classes are contained within one another, but this might not make it obvious why an inclusion is known. For instance, it might not be obvious why BP•L[^bpl] should be contained in ZPP<sup>NP</sup>. If each edge is labelled with a reference to a theorem, then one can in follow the connections that BP•L ⊆ BPP ⊆ ZPP<sup>NP</sup>, two nontrivial theorems. If this is carried out naively, then the "proof" that P ⊆ PSPACE might be incredibly complicated, so there should be some kind of precedence where weaker/simpler theorems are known first.

Beyond merely tabulating inclusions of languages, tracking implications (P=NP → P=PH, circuit derandomization, P=promise-RP → P=BPP, etc.) lets one quickly explore different pictures of the world. Going beyond languages, one can consider promise problems, parameterized problems, optimization problems, counting problems, distributional problems... as other hierarchies, often with natural functors between them. In that sense, this database also aims to be "strongly typed" in the sense of carefully distinguishing these types of problems.

This repo is live [here](https://ohaithe.re/ZooClasses/). Currently, it is limited to showing the language classes, their transitive reduction of inclusions, and the definitions of the classes. Equal classes can be shown or hidden, and the diagram can be searched. The inclusion diagram is derived from the theorems in the database. For instance,

```
{"name":"Immerman–Szelepcsényi theorem",
 "ref":"https://en.wikipedia.org/wiki/Immerman%E2%80%93Szelepcs%C3%A9nyi_theorem",
 "content":"{f}(f≥log)⟹(NSPACE(f)=coNSPACE(f))"
},

{"name":"NC^1⊆L",
 "content":"NC^1⊆L",
 "ref":"Proved in {ref:Bor77}"
},
```

Each theorem has a human-readable name, a reference (which can be a name in the reference database, or otherwise any string), and a machine-parseable `content`.

The TODO list for the viewer is mostly a question of which data is present that needs to be shown to the user:

 * Reasoning for each edge: click on an edge to see which theorem gave this edge. Since edges are minimal, it will always be a single theorem.
 * Comparing of other classes: select two classes and see what is known about their relationship with each other, including a minimal set of theorems implying those relationships.
 * Other problem types: showing/hiding parameterized problems, promise problems, etc.
 * Nonequality: Show which classes are known to be nonequal. Not clear what the best way to show this is.
 * Hypotheses: Turn off/on hypotheses (e.g. collapse of PH) and render the resulting diagram.
 * Markdown: Rendering Markdown and LaTeX in HTML descriptions.
 
The TODO list for the parser is mostly about tracking more kinds of data and parsing wider sets of theorems; and preparing the data for the viewer, such as calculating minimal sets of theorems. I would also like to add a parser for language definitions. Several languages have definitions, like NP is `NTIME(n^O(1))` and we could define `QMA = QIP[1]`, and one could even imagine defining something like `QIP[k] = Interactive[Verifier=BQP, Message=QuantumState[Size=n^O(1)], Messages=k]`. This would enable more automatic interpretation of theorems.

The TODO list of the database is of course mostly focused on adding more data: more classes, more theorems, more references. But some things that are not present at all that I would like to add:
 * Properties: Marking classes with properties such as "closed under complement", "concatenation", "intersection"; "low for itself"; and so on.
 * Uniformity data: Some way to annotate that "this is nonuniform AC^1, but _this_ is logspace-uniform AC^1" in a useful way, to annotate which types of uniformity are equivalent, and then a way to render this information.
 * Relativized information: Some way to incorporate which inclusions relativize, and what oracles exist/often/almost always create separations between classes.

[^bpl]: BP•L is _Bounded-Error Probabilistic L with Two Way Access to Randomness_, see [the Zoo](https://complexityzoo.net/Complexity_Zoo:B#bpdotl)
