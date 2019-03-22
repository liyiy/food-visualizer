console.log("AHHHHHHH");

$(function() {
  console.log('jquery is working!');
  createGraph();
  testThing();
});

function testThing() {
  var svgWidth = 500;
  var svgHeight = 300;
  var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight)
    .attr("class", "bar-chart");
}

function createGraph() {
  var width = 1000;
  var height = 800;
  var format = d3.format(",d");
  var color = d3.scale.category20();
  var sizeOfRadius = d3.scale.pow().domain([-100,100]).range([-50,50]);

  var bubble = d3.layout.pack()
    .sort(null)  // disable sorting, use DOM tree traversal
    .size([width, height])  // chart layout size
    .padding(1)  // padding between circles
    .radius(function (d) { return 20 + (sizeOfRadius(d) * 30); });

  var svg = d3.select("#chart").append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("class", "bubble");
}