// from data.js
var tableData = data;

// YOUR CODE HERE!
var button = d3.select("#filter-btn");
button.on("click", retrieveFilter);


function retrieveFilter() {
    // Clear out data & Keep page from refreshing
    var tbody = d3.select("tbody"); //must be defined up here for clear table to work
    tbody.html("");
    d3.event.preventDefault();

    // Take input data and store as inputValue
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    console.log(inputValue);
 
    // Filter dataset on the inputValue
    var filterDate = tableData.filter(info => (info.datetime === inputValue));
    console.log(filterDate);

    // Now for table
    filterDate.forEach(function(fillTable) {
              // console.log(fillTable); IT WORKS YAY

        // Add a row per filtered result
        var row = tbody.append("tr");

        // fill the table row values
        Object.entries(fillTable).forEach(function([key, value]) {
            // console.log(key, value); IT WORKS YAY
            
            // per row, add column elements
            var cell = tbody.append("td");

            // add data to column elements
            cell.text(value);
        })
    });
};
