function processString(str) {
    if (!str) return '';
    return str
        .replace(/{lang:([^}]+)}/g, (match, p1) => `<a href="class.html?name=${encodeURIComponent(p1)}">${p1}</a>`)
        .replace(/{thm:([^}]+)}/g, (match, p1) => `<a href="theorem.html?name=${encodeURIComponent(p1)}">${p1}</a>`)
        .replace(/{ref:([^}]+)}/g, (match, p1) => `<a href="reference.html?name=${encodeURIComponent(p1)}">${p1}</a>`);
}
