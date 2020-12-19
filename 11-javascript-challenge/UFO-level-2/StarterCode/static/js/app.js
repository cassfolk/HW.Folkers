var tableData = data;

// YOUR CODE HERE!
var button = d3.select("#filter-btn");
button.on("click", retrieveFilter);


function retrieveFilter() {
    // Clear out data & Keep page from refreshing
    var tbody = d3.select("tbody"); //must be defined up here for clear table to work
    tbody.html("");
    d3.event.preventDefault();

    // Take input data and store as inputValues
    var inputElementDate = d3.select("#datetime");
    var inputValueDate = inputElementDate.property("value");

    var inputElementCity = d3.select("#city");
    var inputValueCity = inputElementCity.property("value");

    var inputElementState = d3.select("#state");
    var inputValueState = inputElementState.property("value");

    var inputElementCountry = d3.select("#country");
    var inputValueCountry = inputElementCountry.property("value");

    var inputElementShape = d3.select("#shape");
    var inputValueShape= inputElementShape.property("value");

    var results = tableData.filter(function(filterdBy) {
        return (filterdBy.datetime===inputValueDate || !inputValueDate) && 
                    (filterdBy.city===inputValueCity || !inputValueCity) &&
                    (filterdBy.state===inputValueState || !inputValueState) &&
                    (filterdBy.country===inputValueCountry || !inputValueCountry) &&
                    (filterdBy.shape===inputValueShape|| !inputValueShape)
        });
    console.log("Results: ", results);

    // Now for table
    results.forEach(function(fillTable) {

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
