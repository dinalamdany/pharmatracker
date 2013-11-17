d3.text("data/fake_data.csv", function(datasetText) {
	//Width and height
	var w = 600;
	var h = 300;
	var padding = 50;

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

   	   .attr("fill", function(d) {
   	   			if(d[3] == "R"){
   	   				return "red";
   	   			}
   	   			else if(d[3] == "D"){
   	   				return "blue";
   	   			}
				else{
					return "green";
				}
		   })

	   //.style("fill", "pink")

	   .on("mouseover", function(d) {
	   		//highlight color
			//Get this bar's x/y values, then augment for the tooltip
			var xPosition = parseFloat(d3.select(this).attr("cx"));
			var yPosition = parseFloat(d3.select(this).attr("cy"));

			svg.append("text")
			   .attr("id", "tooltip")
			   .attr("x", xPosition)
			   .attr("y", yPosition)
			   .attr("text-anchor", "middle")
			   .attr("font-family", "serif")
			   .attr("font-size", "14px")
			    //.attr("font-weight", "bold")
			   .attr("fill", "black")
			   .text(d.join(" "));
		})

		.on("mouseout", function() {
			//unhighlight
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
		
		//X axis Label
		svg.append("text")
		    .attr("class", "x label")
		    .attr("text-anchor", "end")
		    .attr("x", w - 20)
		    .attr("y", h - 5)
		    .text("income per capita, inflation-adjusted (dollars)");

		//Y axis Label
	    svg.append("text")
		    .attr("class", "y label")
		    .attr("text-anchor", "end")
		    .attr("y", 0)
		    .attr("dy", ".75em")
		    .attr("transform", "rotate(-90)")
		    .text("life expectancy (years)");

		 //Title
		svg.append("text")
		        .attr("x", (w / 2) - padding)             
		        .attr("y", 20)
		        .text("Hello Title")
});










