Formatting prelude note:
 * Useful characters: ≤ ≥ ⊂ ⊆ ⊃ ⊇ ⊈ ⊉ = ⟹ Ω Σ Π Δ
 * Avoid ≠, prefer ⊂ or ⊈ instead. That is, whenever possible, break down a non-equality into two non-containments. This is distinct between the human-readable _name_ of a theorem and it's syntactic mathematical _content_; we call the conjecture `P != NP` for instance, but we state it as `P⊂NP`.
 * Avoid union ∪ and intersection ∩, prefer writing two logical statements instead. That is, instead of something like A ⊆ B ∩ C, write A ⊆ B and A ⊆ C. Statements like A ⊆ B ∪ C can't easily be decomposed this way ("everything in A is *either* in B or C"), but such statements are exceedingly rare in complexity theory.

First, `problem_types.json`: A sort of schematic file that defines what we mean by a "problem", as this can be a language, a promise problem etc. All complexity classes are assigned a "problem type" that they categorize.

Then `properties.json`: Certain properties we can flag classes as having or not, mostly for better display. Currently most classes are not tagged at all.

The file `classes.json` lists all the complexity classes. They are grouped first by problem type, then alphabetically.

Then, theorems are split into two files (with identical schema): `theorems.json` and `conjectures.json`. Theorems are given first in any "general form" (such as the time hierarchy theorem), then appropriate specializations to give reified relationships between complexity classes.