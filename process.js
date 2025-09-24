function processString(str) {
    if (!str) return '';
    return str
        .replace(/{lang:([^}]+)}/g, (match, p1) => `<a href="class.html?name=${encodeURIComponent(p1)}">${p1}</a>`)
        .replace(/{thm:([^}]+)}/g, (match, p1) => `<a href="theorem.html?name=${encodeURIComponent(p1)}">${p1}</a>`)
        .replace(/{ref:([^}]+)}/g, (match, p1) => `<a href="reference.html?name=${encodeURIComponent(p1)}">${p1}</a>`);
}

function createLinkList(container, items, urlGenerator) {
    if (items && items.length > 0) {
        container.innerHTML = ''; // Clear existing content
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
