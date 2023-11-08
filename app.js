var express = require('express');
var path = require('path');

var app = express();

app.get('/', function(req, res){
  res.sendFile(path.join(__dirname, '/index.html'));
});
/*app.get('/data', function(req, res){
    var data = require('./data.json');
    res.json(data);
});*/
app.use(express.static('.'));
app.listen(3000, function() {
    console.log('Server running on port 3000!');
});
