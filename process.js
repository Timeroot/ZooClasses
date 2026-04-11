function processString(str) {
    if (!str) return '';
    return str
        .replace(/{lang:([^}]+)}/g, (match, p1) => `<a href="class.html?name=${encodeURIComponent(p1)}">${p1}</a>`)
        .replace(/{thm:([^}]+)}/g, (match, p1) => `<a href="theorem.html?name=${encodeURIComponent(p1)}">${p1}</a>`)
        .replace(/{ref:([^}]+)}/g, (match, p1) => `<a href="reference.html?name=${encodeURIComponent(p1)}">${p1}</a>`);
}

function createLinkList(container, items, urlGenerator) {
    if (items && items.length > 0) {
        container.innerHTML = '';
        items.forEach((item, index) => {
            const link = document.createElement('a');
            link.href = urlGenerator(item);
            link.textContent = item;
            container.appendChild(link);
            if (index < items.length - 1) {
                container.appendChild(document.createTextNode(', '));
            }
        });
    } else {
        container.textContent = 'None';
    }
}

// ── Poset computation from theorems ─────────────────────────────────────

// When multiple classes are equal, prefer these as the canonical representative.
const CANONICAL_FORMS = [
    "PSPACE","BPP","NC","L","NL","NLINSPACE","NC^0","QAC","RE","NEXP","SAC^1","coNQP"
];

const RELATION_RE = /[\u2282\u2286\u2283\u2287\u2288\u2289\u228A\u2260=]/;

/**
 * Parse theorem content strings and build the inclusion poset for a
 * given class type.  Returns an array in the same shape that the old
 * generated/langdata.json had:
 *
 *   { name, desc, children, equals, related, notes, properties }
 *
 * where `children` = immediate supersets (covering relation), and
 * `equals` = array of equal-class names (canonical) or false (non-canonical).
 */
function buildPosetFromTheorems(classes, theorems, classType) {
    const typeClasses = classes.filter(c => c.type === classType);
    const classNames = new Set(typeClasses.map(c => c.name));
    const allClassNames = new Set(classes.map(c => c.name));

    // ── 1. Parse theorems into direct ⊆ edges ──────────────────────────

    const directEdges = []; // [lhs, rhs] meaning lhs ⊆ rhs

    for (const thm of theorems) {
        const content = thm.content;
        if (!content || content.startsWith('{')) continue;

        for (let part of content.split('&&')) {
            part = part.trim();
            if (part.startsWith('{')) continue;

            const relMatch = part.match(RELATION_RE);
            if (!relMatch) continue;

            let rel = relMatch[0];
            let lhs = part.substring(0, relMatch.index).trim();
            let rhs = part.substring(relMatch.index + rel.length).trim();

            if (!allClassNames.has(lhs) || !allClassNames.has(rhs)) continue;
            if (!classNames.has(lhs) || !classNames.has(rhs)) continue;

            if (rel === '\u228A') rel = '\u2282';
            if (rel === '\u2283') { [lhs, rhs] = [rhs, lhs]; rel = '\u2282'; }
            if (rel === '\u2287') { [lhs, rhs] = [rhs, lhs]; rel = '\u2286'; }
            if (rel === '\u2289') { [lhs, rhs] = [rhs, lhs]; rel = '\u2288'; }

            if (rel === '\u2286') {          // ⊆
                directEdges.push([lhs, rhs]);
            } else if (rel === '=') {
                directEdges.push([lhs, rhs]);
                directEdges.push([rhs, lhs]);
            } else if (rel === '\u2282') {   // ⊂
                directEdges.push([lhs, rhs]);
            }
            if (rel === '\u2260') {          // ≠
                console.warn(`Theorem "${thm.name}": relation \u2260 should be replaced with \u2288 or \u2289.`);
            }
        }
    }

    // ── 2. Transitive closure via BFS ───────────────────────────────────

    const names = Array.from(classNames);
    const adj = new Map();
    for (const name of names) adj.set(name, new Set());
    for (const [lhs, rhs] of directEdges) adj.get(lhs).add(rhs);

    // reachable.get(x) = set of all y such that x ⊆ y (including x itself)
    const reachable = new Map();
    for (const start of names) {
        const reached = new Set([start]);
        const queue = [start];
        while (queue.length > 0) {
            const cur = queue.shift();
            for (const next of (adj.get(cur) || [])) {
                if (!reached.has(next)) {
                    reached.add(next);
                    queue.push(next);
                }
            }
        }
        reachable.set(start, reached);
    }

    // ── 3. Equivalence classes ──────────────────────────────────────────

    const canonicalRep = new Map();   // name -> its canonical representative
    const equivMembers = new Map();   // canonical -> [all members]
    const assigned = new Set();

    for (const name of names) {
        if (assigned.has(name)) continue;

        const eqClass = names.filter(other =>
            reachable.get(name).has(other) && reachable.get(other).has(name)
        );

        let canon = eqClass.find(n => CANONICAL_FORMS.includes(n));
        if (!canon) {
            eqClass.sort();
            canon = eqClass[0];
        }

        for (const member of eqClass) {
            canonicalRep.set(member, canon);
            assigned.add(member);
        }
        equivMembers.set(canon, eqClass);
    }

    // ── 4. Covering relation (children = immediate supersets) ───────────

    const canonicals = Array.from(equivMembers.keys());
    const canonChildren = new Map();

    for (const x of canonicals) {
        const children = [];
        for (const y of canonicals) {
            if (y === x) continue;
            if (!reachable.get(x).has(y)) continue;       // x ⊈ y
            if (reachable.get(y).has(x)) continue;         // x = y (shouldn't happen between distinct canonicals)

            // Is there a canonical z strictly between x and y?
            let hasIntermediate = false;
            for (const z of canonicals) {
                if (z === x || z === y) continue;
                if (reachable.get(x).has(z) && reachable.get(z).has(y) &&
                    !reachable.get(z).has(x)) {
                    hasIntermediate = true;
                    break;
                }
            }
            if (!hasIntermediate) children.push(y);
        }
        canonChildren.set(x, children);
    }

    // ── 5. Warnings ─────────────────────────────────────────────────────

    const minimals = canonicals.filter(x =>
        !canonicals.some(y => y !== x && reachable.get(y).has(x) && !reachable.get(x).has(y))
    );
    const maximals = canonicals.filter(x => canonChildren.get(x).length === 0);

    if (maximals.length !== 1) {
        console.warn(
            `Poset (${classType}): expected 1 maximal class (ALL), found ${maximals.length}: ${maximals.join(', ')}`
        );
    }
    if (minimals.length > 2) {
        console.warn(
            `Poset (${classType}): ${minimals.length} minimal classes: ${minimals.join(', ')}`
        );
    }

    // ── 6. Build output ─────────────────────────────────────────────────

    const result = [];
    for (const cls of typeClasses) {
        const name = cls.name;
        const canon = canonicalRep.get(name);
        const isCanonical = (canon === name);

        const entry = {
            name,
            desc:       cls.desc       || '',
            related:    cls.related    || [],
            notes:      cls.notes      || '',
            properties: cls.properties || [],
        };

        if (isCanonical) {
            entry.children = canonChildren.get(name) || [];
            entry.equals   = equivMembers.get(name).filter(n => n !== name);
        } else {
            entry.children = [];
            entry.equals   = false;
        }

        result.push(entry);
    }

    return result;
}
