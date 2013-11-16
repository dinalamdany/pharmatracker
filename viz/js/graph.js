d3.text("data/fake_data.csv", function(datasetText) {
	//Width and height
	var w = 500;
	var h = 100;
	var padding = 20;

	var dataset = d3.csv.parseRows(datasetText);

	//Create scale functions
	var xScale = d3.scale.linear()
						 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
						 .range([padding, w - padding * 2]);

	var yScale = d3.scale.linear()
						 .domain([0, d3.max(dataset, function(d) { return d[2]; })])
						 .range([h - padding, padding]);

	var rScale = d3.scale.linear()
						 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
						 .range([2, 5]);

	//Create SVG element
	var svg = d3.select("body")
				.append("svg")
				.attr("width", w)
				.attr("height", h);

	svg.selectAll("circle")
	   .data(dataset)
	   .enter()
	   .append("circle")
	   .attr("cx", function(d) {
	   		return xScale(d[1]);
	   })
	   .attr("cy", function(d) {
	   		return yScale(d[2]);
	   })
	   .attr("r", function(d) {
	   		return rScale(d[1]);
	   });
	   
	svg.selectAll("text")
	   .data(dataset)
	   .enter()
	   .append("text")
	   .text(function(d) {
	   		return d[1] + "," + d[2];
	   })
	   .attr("x", function(d) {
	   		return xScale(d[1]);
	   })
	   .attr("y", function(d) {
	   		return yScale(d[2]);
	   })
	   .attr("font-family", "sans-serif")
	   .attr("font-size", "11px")
	   .attr("fill", "red");
});