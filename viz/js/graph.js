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
						 .range([2, 10]);
	//Define X axis
	var xAxis = d3.svg.axis()
					  .scale(xScale)
					  .orient("bottom")
					  .ticks(5);

	//Define Y axis
	var yAxis = d3.svg.axis()
					  .scale(yScale)
					  .orient("left")
					  .ticks(5);
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
		})
	   .style("fill", "pink")

	   .on("mouseover", function(d) {
	   		//highlight color
	   		d3.select(this).style("fill", "aliceblue");
			//Get this bar's x/y values, then augment for the tooltip
			var xPosition = parseFloat(d3.select(this).attr("cx"));
			var yPosition = parseFloat(d3.select(this).attr("cy"));

			svg.append("text")
			   .attr("id", "tooltip")
			   .attr("x", xPosition)
			   .attr("y", yPosition)
			   .attr("text-anchor", "middle")
			   .attr("font-family", "sans-serif")
			   .attr("font-size", "11px")
			   .attr("font-weight", "bold")
			   .attr("fill", "red")
			   .text(d.join());


		})
		.on("mouseout", function() {
			//unhighlight
			d3.select(this).style("fill", "pink");
			//Remove the tooltip
			d3.select("#tooltip").remove();
			
		});

			
		//Create X axis
		svg.append("g")
			.attr("class", "axis")
			.attr("transform", "translate(0," + (h - padding) + ")")
			.call(xAxis);
		
		//Create Y axis
		svg.append("g")
			.attr("class", "axis")
			.attr("transform", "translate(" + padding + ",0)")
			.call(yAxis);
});



/*
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
*/
