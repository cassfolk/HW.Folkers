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
    
    console.log(inputValueDate);
    console.log(inputValueCity);
    console.log(inputValueState);
    console.log(inputValueCountry);
    console.log(inputValueShape);

            // var answers = [{"datetime": inputValueDate, 
            //     "city": inputValueCity, 
            //     "state": inputValueState, 
            //     "country": inputValueCountry, 
            //     "shape": inputValueShape}];
            // console.log(answers);

    function filterByInputs(info) {
            // Trying to get a object with only the filled out values doesn't work
            // for (var i = 0; i < answers.length; i++) {
            //     if (answers.datetime !== "") {
            //         return info.datetime === inputValueDate;
            //     }
            //     if (answers.city !== "") {
            //         return info.city === inputValueCity;
            //     }
            //     if (answers.state !== "") {
            //         return info.state === inputValueState;
            //     }
            //     if (answers.country !== "") {
            //         return info.country === inputValueCountry;
            //     }
            //     if (answers.shape !== "") {
            //         return info.shape === inputValueShape;
            //     }
            // };
        
        /////////// THIS WORKS IF THE VALUES ARE LEFT BLANK AND FILLED FROM THE BOTTOM UP!!!!
        // if (inputValueDate === "" && inputValueCity === "" && inputValueState === "" && inputValueCountry === "") {
        //     return info.shape === inputValueShape;
        // }
        // else if (inputValueDate === "" && inputValueCity === "" && inputValueState === "") {
        //     return info.shape === inputValueShape && info.country === inputValueCountry;
        // }
        // else if (inputValueDate === "" && inputValueCity === "") {
        //     return info.shape === inputValueShape && info.country === inputValueCountry && info.state === inputValueState;
        // }
        // else if (inputValueDate === "") {
        //     return info.shape === inputValueShape && info.country === inputValueCountry && info.state === inputValueState && info.city === inputValueCity;
        // }
        // else {
        //     return info.datetime === inputValueDate;
        // }
        // };

        // testing testing 1 2 3 WORKS FOR FIRST VALUE FILTER
        // if (inputValueDate !== "") {
        //     return info.datetime === inputValueDate;
        // }
        // if (inputValueCity !== "") {
        //     return info.city === inputValueCity;
        // }
        // if (inputValueState !== "") {
        //     return info.state === inputValueState;
        // }
        // if (inputValueCountry !== "") {
        //     return info.country === inputValueCountry;
        // }
        // if (inputValueShape !== "") {
        //     return info.shape === inputValueShape;
        // }
        };


    var results = tableData.filter(filterByInputs);
    console.log(results);

    // Now for table
    results.forEach(function(fillTable) {
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
