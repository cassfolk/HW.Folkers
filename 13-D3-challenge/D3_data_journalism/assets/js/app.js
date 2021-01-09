// @TODO: YOUR CODE HERE!
var svgWidth = 900;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("https://raw.githubusercontent.com/cassfolk/HW.Folkers/master/13-D3-challenge/D3_data_journalism/assets/data/data.csv").then(function(healthData) {
    // console.log(healthData)
    
    // Step 1: Parse Data/Cast as numbers
    healthData.forEach(function(data){
        data.poverty = +data.poverty;
        data.healthcare = +data.healthcare;
        // console.log("State ", data.state)
        // console.log("Poverty ", data.poverty)
        // console.log("Healthcare ", data.healthcare)
      })
    
    // Step 2: Create scale functions
    var xLinearScale = d3.scaleLinear()
        .domain([(d3.min(healthData, d => d.poverty) -1), d3.max(healthData, d => d.poverty)])
        .range([0, width]);
    // console.log(xLinearScale);

    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(healthData, d => d.healthcare)])
        .range([height, 0]);
    // console.log(yLinearScale);

    // Step 3: Create axis functions
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);
    // console.log(bottomAxis);
    // console.log(leftAxis);

                
    // Step 4: Append Axes to the chart
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis)

    chartGroup.append("g")
        .call(leftAxis)
    
    //Step 5: Create Circles    
    var circleG = chartGroup.selectAll("g")
        .data(healthData)
        .enter()
        .append("g")
        .attr("transform", d => `translate(${xLinearScale(d.poverty)}, ${yLinearScale(d.healthcare)})`);


    var circlesGroup = circleG.append("circle")
        .attr("r", "15")
        .attr("class", "stateCircle")
        .attr("text", d => d.abbr);

    var circlesLables = circleG.append("text")
        .text(d => d.abbr)
        .attr('dy', 6)
        .attr("class", "stateText");

 

    // Step 6: Initialize tool tip
    var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([80, -70]) //offset from where it's initialized so it doesn't hover over the value itself
        .attr("class", "d3-tip")
        .html(function(d){
        return (`<strong>${d.state}</strong><br>Poverty: ${d.poverty}%<br>Healthcare: ${d.healthcare}%`);
    })

    // Step 7: Create tooltip in the chart
    chartGroup.call(toolTip);

    // Step 8: Create event listeners to display and hide the tooltip
    circlesLables.on("mouseover", function(data){
        toolTip.show(data, this);
    })
    .on("mouseout", function(data, index){
        toolTip.hide(data);
    })

    // Step 9: Create axes labels
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 30)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .attr("class", "aText")
        .text("Lacks Healthcare (%)");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "aText")
      .text("In Poverty (%)");
      


}).catch(function(error) {
    console.log(error);
});