document.addEventListener('DOMContentLoaded', function() {
    fetch('./langdata.json')
    .then(res => res.json())
    .then(_data => {
        data = _data;
        nodeNames = data.map(obj => obj["name"]);
        
        drawGraph();
    });
});

function getEqualCanonId(name){
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

//Draw the graph, given preferences about what to show
function drawGraph(){
        // Create the input graph
        g = new dagreD3.graphlib.Graph({ compound: true })
          .setGraph({})
          .setDefaultEdgeLabel(function() { return {}; });
        
        //Orient from bottom up
        g.graph().rankdir = "BT";
        
        //Do we show equal classes?
        var showEquals = document.getElementById("showEq").checked;
        
        //Do we show nonuniform classes?
        var showNU = document.getElementById("showNU").checked;

        // Here we're setting nodeclass, which is used by our custom drawNodes function
        // below.
        for(var classInfo of data){
            var name = classInfo["name"];
            var properties = classInfo["properties"];
            
            if(!showNU && properties.includes("nonuniform"))
                continue
                
            var classType = "type-normal";
            var equals = classInfo["equals"];
            if(equals === false){ //equal to some other canonical class
                if(!showEquals){
                    continue; //skip this one
                }
                classType = "type-equal-notcanon";
            } else if(equals.length > 0){ //equal to something else, is canonical
                if(showEquals)
                    classType = "type-equal-canon";
                //otherwise keep the same class
            }
            
            g.setNode(name, { label: name, class: classType, id: "class-"+name });
        }
        
        //Now create all the equals groupings
        if(showEquals) {
            for(var classInfo of data){
                var name = classInfo["name"];
                var properties = classInfo["properties"];
                
                if(!showNU && properties.includes("nonuniform"))
                    continue;
                
                var equals = classInfo["equals"];
                if(equals === false || equals.length == 0) {
                    continue;
                }
                
                var groupName = name+"-equals";
                g.setNode(groupName, { labelType:"html", label: "<b style='color:#a33'>Equal to "+name+"</b>", clusterLabelPos: 'top', class: "type-equal-group", id: "class-"+groupName });
                
                g.setParent(name, groupName);
                for(var eq of equals) {
                    g.setParent(eq, groupName);
                }
            }
        }

        //Set rounded corners for all class nodes
        g.nodes().forEach(function(v) {
            var node = g.node(v);
            // Round the corners of the nodes
            node.rx = node.ry = 5;
        });
        
        // Set up edges, no special attributes.
        for(var classInfo of data){
            var name = classInfo["name"];
            var properties = classInfo["properties"];
            
            if(!showNU && properties.includes("nonuniform"))
                continue
            
            for(var i in classInfo["children"]){
                var childName = classInfo["children"][i];
                var childId = nodeNames.indexOf(childName);
                if(childId == -1){
                    console.log("Couldn't find child ",childName," in classes");
                    continue;
                }
                var childInfo = data[childId];
                var childProperties = childInfo["properties"];
            
                if(!showNU && childProperties.includes("nonuniform"))
                    continue
                
                g.setEdge(name, childName, {curve: d3.curveBasis});
            }
        }
        
        // Create the renderer
        var render = new dagreD3.render();

        // Set up an SVG group so that we can translate the final graph.
        var svg = d3.select("#treeSvg");
        
        //Remove any existing SVG we've drawn
        d3.select("#treeSvg g").remove();
        
        var svgGroup = svg.append("g");

        // Run the renderer. This is what draws the final graph.
        render(d3.select("svg g"), g);
        
        //Set rounded corners for all group clusters        
        d3.selectAll('g.cluster rect').attr("rx",12); 

        // Center the graph
        var svgWidth = document.getElementById('treeDiv').offsetWidth;
        var svgHeight = document.getElementById('treeDiv').offsetHeight;
        sclZoom = Math.min(1, 0.95 * svgWidth / g.graph().width, 0.95 * svgHeight / g.graph().height);
        //var xCenterOffset = (svgWidth - g.graph().width) / 2 * sclZoom;
        svgGroup.attr("transform", "scale("+sclZoom+")");
        
        origHeight = (g.graph().height + 40) * sclZoom; //Save for later, not 'var'
        svg.attr("height", origHeight);
            
        var zoom = d3.zoom().on("zoom", function() {
            d3.event.transform.k *= sclZoom;
            svgGroup.attr("transform", d3.event.transform);
            d3.event.transform.k /= sclZoom;
            var zoomlevel = d3.event.transform.k;
            var newHeight = zoomlevel * origHeight;
            var minHeight = document.getElementById("svgDiv").offsetHeight;
            newHeight = Math.max(newHeight, minHeight);
            svg.attr("height", newHeight);
        });
        svg.call(zoom);
        
        d3.selectAll('g.nodes g.node').on('click', function(name) {
            setSelectedNode(name);
        });
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
