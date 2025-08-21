let equivalenceClasses = new Map();

function getEqualCanonId(name){
    if (!data) return -1; // Handle case where data might not be loaded yet

    var origId = nodeNames.indexOf(name)
    if(origId == -1){
        return -1;
    }
    if(data[origId].equals === false){
        for(var other of data){
            var otherEq = other.equals;
            if(otherEq === false) //not canonical
                continue;
            if(otherEq.indexOf(name) === -1) //not equal
                continue;
            //equal!
            return nodeNames.indexOf(other.name);
        }//didn't find anything equalling it...
        return -1;
    } else {
        return origId;
    }
}

function buildEquivalenceClasses() {
    equivalenceClasses.clear();
    for (const classInfo of data) {
        const canonId = getEqualCanonId(classInfo.name);
        if (canonId === -1) continue;

        if (!equivalenceClasses.has(canonId)) {
            equivalenceClasses.set(canonId, []);
        }
        equivalenceClasses.get(canonId).push(classInfo);
    }
}

function getFilteredData(showEquals, propertyFilters) {
    const initialFilteredNames = new Set(
        data.filter(classInfo => {
            const properties = classInfo.properties || [];
            for (const prop in propertyFilters) {
                const state = propertyFilters[prop];
                if (state === 'yes' && !properties.includes(prop)) return false;
                if (state === 'no' && properties.includes(prop)) return false;
            }
            return true;
        }).map(d => d.name)
    );

    const finalData = [];
    if (showEquals) {
        // When showing equals, we iterate through the equivalence classes
        for (const [canonId, members] of equivalenceClasses.entries()) {
            const matchingMembers = members.filter(member => initialFilteredNames.has(member.name));
            if (matchingMembers.length > 0) {
                finalData.push(...matchingMembers);
            }
        }
    } else {
        // When not showing equals, we also iterate through equivalence classes
        for (const [canonId, members] of equivalenceClasses.entries()) {
            const matchingMembers = members.filter(member => initialFilteredNames.has(member.name));
            if (matchingMembers.length > 0) {
                const canonicalClass = data[canonId];
                const canonicalIsMatching = matchingMembers.some(m => m.name === canonicalClass.name);

                if (canonicalIsMatching) {
                    // Prefer the canonical representative if it matches the filter
                    finalData.push(canonicalClass);
                } else {
                    // Otherwise, pick the first available matching member
                    finalData.push(matchingMembers[0]);
                }
            }
        }
    }
    return finalData;
}

//Draw the graph, given preferences about what to show
function drawGraph() {
    const propertyFilters = {};
    document.querySelectorAll('#propertyCheckboxes input[type="checkbox"]').forEach(checkbox => {
        propertyFilters[checkbox.dataset.property] = checkbox.dataset.state;
    });

    const showEquals = document.getElementById("showEq").checked;
    const filteredData = getFilteredData(showEquals, propertyFilters);
    const filteredNames = new Set(filteredData.map(d => d.name));

    g = new dagreD3.graphlib.Graph({ compound: true })
        .setGraph({})
        .setDefaultEdgeLabel(() => ({}));
    g.graph().rankdir = "BT";

    for (const classInfo of filteredData) {
        const name = classInfo.name;
        let classType = "type-normal";
        if (showEquals) {
            if (classInfo.equals === false) {
                classType = "type-equal-notcanon";
            } else if (classInfo.equals && classInfo.equals.length > 0) {
                classType = "type-equal-canon";
            }
        }
        g.setNode(name, { label: name, class: classType, id: "class-" + name });
    }

    if (showEquals) {
        for (const [canonId, members] of equivalenceClasses.entries()) {
            const membersInFilter = members.filter(m => filteredNames.has(m.name));
            if (membersInFilter.length > 1) {
                const canonClassName = data[canonId].name;
                const groupName = canonClassName + "-equals";
                g.setNode(groupName, { labelType: "html", label: `<b style='color:#a33'>Equal to ${canonClassName}</b>`, clusterLabelPos: 'top', class: "type-equal-group", id: "class-" + groupName });
                membersInFilter.forEach(member => g.setParent(member.name, groupName));
            }
        }
    }

    g.nodes().forEach(v => {
        const node = g.node(v);
        if (node) {
            node.rx = node.ry = 5;
        }
    });

    for (const classInfo of filteredData) {
        const name = classInfo.name;
        for (const childName of classInfo.children || []) {
            if (!filteredNames.has(childName)) continue;
            const childInfo = data[nodeNames.indexOf(childName)];
            g.setEdge(name, childName, { curve: d3.curveBasis });
        }
    }

    const render = new dagreD3.render();
    const svg = d3.select("#treeSvg");
    d3.select("#treeSvg g").remove();
    const svgGroup = svg.append("g");
    render(d3.select("svg g"), g);

    d3.selectAll('g.cluster rect').attr("rx", 12);

    const svgWidth = document.getElementById('treeDiv').offsetWidth;
    const svgHeight = document.getElementById('treeDiv').offsetHeight;
    const sclZoom = Math.min(1, 0.95 * svgWidth / g.graph().width, 0.95 * svgHeight / g.graph().height);
    svgGroup.attr("transform", `scale(${sclZoom})
    `);
    const origHeight = (g.graph().height + 40) * sclZoom;
    svg.attr("height", origHeight);

    const zoom = d3.zoom().on("zoom", function () {
        const transform = d3.event.transform;
        transform.k *= sclZoom;
        svgGroup.attr("transform", transform);
        transform.k /= sclZoom;
        const newHeight = Math.max(transform.k * origHeight, document.getElementById("svgDiv").offsetHeight);
        svg.attr("height", newHeight);
    });
    svg.call(zoom);

    d3.selectAll('g.nodes g.node').on('click', setSelectedNode);
}

d3.select('#plusButton').on('click', function() {
  // code to show more nodes based on their priority
});
d3.select('#minusButton').on('click', function() {
  // code to hide some nodes based on their priority
});

//Given a piece of text (description, whatever), format it nicely with our pseudo-markdown
//for inter-topic links.
function processText(str){
    //make http://...XXX/ strings clickable.
    const httpRegex = /https?:[^ ]+[^.,)( ]/gi;
    const httpReplacement = "<a href='$&' target='_blank'>$&</a>";
    str = str.replaceAll(httpRegex, httpReplacement);
    //make {lang:XXX} hyperlinks
    const langRegex = /{lang:([^}]+)}/gi;
    const langReplacement = "<a href='#' onclick='setSelectedNode(\"$1\");'>$1</a>";
    str = str.replaceAll(langRegex, langReplacement);
    //fix whitespace
    str = "<p>"+str.replaceAll(/\n/gi,"</p><p>")+"</p>";
    return str
}

selectedNode = null;
function setSelectedNode(name){
    var origId = nodeNames.indexOf(name);
    if(origId == -1){
        //do nothing, just keep the old selection
        return;
    }

    var showEquals = document.getElementById("showEq").checked;
    var highlightId = showEquals ? origId : getEqualCanonId(name);
    var highlightName = nodeNames[highlightId];
    
    var newSelection = document.getElementById("class-"+highlightName);
    if(newSelection == null){
        //do nothing, just keep the old highlight
    } else {
        if(selectedNode != null){
            selectedNode.classList.remove("selectedNode");
        }
        
        //Change color by giving it a class
        selectedNode = newSelection;
        selectedNode.classList.add("selectedNode");
    }
    
    //Show text
    var classInfo = data[origId];
    
    var plainDesc = classInfo["desc"];
    var htmlDesc = "<h1>"+name+"</h1>";
    
    htmlDesc += "<div><h3>Description</h3>"+processText(plainDesc)+"</div>";
    
    //Add "related" links
    var related = classInfo.related;
    if(related.length > 0) {
        htmlDesc += "<div><h3>Related classes</h3><ul>";
        for(var rel of related) {
            htmlDesc += "<li><a href='#' onclick='setSelectedNode(\""+rel+"\");'>"+rel+"</a></li>";
        }
        htmlDesc += "</ul></div>";
    }
    
    d3.select('#detailsDiv').html(htmlDesc);
}

function searchFunction() {
  var searchValue = document.getElementById('searchBar').value;
  setSelectedNode(searchValue);
  /*var node = d3.selectAll('.node');
  node.style('stroke', function(d) {
    console.log(d);
    if (d.label === searchValue) return 'blue';
    else return 'black';
  });*/
}

// Collect all unique properties after loading data
var allProperties = [];

document.addEventListener('DOMContentLoaded', function() {
    fetch('./generated/langdata.json')
    .then(res => res.json())
    .then(_data => {
        data = _data;
        nodeNames = data.map(obj => obj["name"]);
        allProperties = Array.from(
            new Set(
                data.flatMap(obj => obj.properties || [])
            )
        );
        buildEquivalenceClasses();
        createPropertyCheckboxes();
        drawGraph();
    });
});
/**
 * Create three-state checkboxes for each property and add them to the page.
 * Each checkbox cycles through: neutral (default), yes (checked), no (indeterminate).
 */
function createPropertyCheckboxes() {
    const container = document.getElementById('propertyCheckboxes');
    if (!container) return;
    container.innerHTML = ''; // Clear any existing

    allProperties.forEach(prop => {
        // Create label and checkbox
        const label = document.createElement('label');
        label.style.marginRight = '1em';
        label.style.userSelect = 'none';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.dataset.property = prop;
        
        checkbox.checked = false;
        checkbox.indeterminate = true; // Neutral state
        checkbox.dataset.state = 'neutral'; // Track state: 'neutral', 'yes', 'no'

        //initialize `nonuniform` to `false`
        if (prop == 'nonuniform') {
            checkbox.checked = false;
            checkbox.indeterminate = false;
            checkbox.dataset.state = 'no';
        }

        // Cycle state on click: neutral -> yes -> no -> neutral
        checkbox.addEventListener('click', function(e) {
            // Let the browser handle the initial state change, then adjust.
            let state = this.dataset.state;
            if (state === 'neutral') {
                // Default click on 'indeterminate' makes it 'checked'. This is our 'yes' state.
                this.dataset.state = 'yes';
            } else if (state === 'yes') {
                // Default click on 'checked' makes it 'unchecked'. This is our 'no' state.
                this.dataset.state = 'no';
            } else { // state === 'no'
                // Default click on 'unchecked' makes it 'checked'. We want 'neutral'.
                // So we override the browser's default action here.
                this.checked = false;
                this.indeterminate = true;
                this.dataset.state = 'neutral';
            }
            drawGraph(); // Redraw graph with new filters
        });

        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(' ' + prop));
        container.appendChild(label);
    });
}