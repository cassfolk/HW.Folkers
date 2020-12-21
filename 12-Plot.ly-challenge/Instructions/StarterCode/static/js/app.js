    // TRYING things for getIntoRows
    //return rows.map(function(row) {
    //                     // for (var i =0; i < row.length; i++) {
    //                     //     rows.map(function(row) {
    //                     //         return row[index];
    //                     //     });
    //                     // };
    //     return rows.map(function(row){
    //         return row[index];
    //     });
    //     // return row[index];
    // });

function getIntoRows(rows) {
    return rows.map(function(row) {
        return row;
    });
};


function avoidNumbers(row) {
    for (var i = 0; i < row.length; i++) {
        var info = row[i];
        return info;
    };
};


d3.json("samples.json").then((importedData) => {
    // console.log("importData: ", importedData);
    var data = importedData;

    // Navigating json so you can extract variables
    var samplesRow = getIntoRows(data.samples);
    // console.log("samplesRow ", samplesRow);
    var sampleObjects = avoidNumbers(samplesRow);
    // console.log("sampleObjects ", sampleObjects);
    var metadataRow = getIntoRows(data.metadata);


    //Variables to plot
    var otuIds = getIntoRows(sampleObjects.otu_ids);
    var sampleValues = getIntoRows(sampleObjects.sample_values);
    var otuLabels = getIntoRows(sampleObjects.otu_labels);
    // console.log("otuIds ", otuIds);

    //Variables for dropdown
    var names = importedData.names; // for dropdown menu
    

    /////////////// FINSIH YOU FOOL!!!!!!
    // console.log("metadataRow ", metadataRow);
    // console.log("Names: ", names);
    var sel = document.getElementById('selDataset');
    for (var i = 0; i < names.length; i++) {
        var opt = document.createElement('option');
        opt.innerHTML = names[i];
        opt.value = names[i];
        sel.appendChild(opt);
    }
    var menuIndex = NEED HELP HERE


    // if (sel ==== names.findIndex(names => names === sel ) {
    //     // === metadataRow.index
    //     var list = d3.select("#sample-metadata");
    //     list.append("dd").text(`Id: 950`);
    //     list.append("dd").text(`ethnicity: Cacausian`);
    //     list.append("dd").text(`gender: F`);
    //     list.append("dd").text(`age: 25`);
    //     list.append("dd").text(`location: Beaufort`);
    //     list.append("dd").text(`bbtype: 1`);
    //     list.append("dd").text(`wfreq: 1`);
    // };
    
    // var dropDown = d3.select("#selDataset");
                ///see 15.02.09 for dropdown
                /// if names index === (metadataRow index) then fill list
                //// IF FREAKING NULL PUT NULL
    // Demographic Ino formatting


    // BAR
    // BAR
        // Sort the data array using sampleValues the
        // data.sort(function(a, b) {
        //     return parseFloat(b.sampleValues) - parseFloat(a.sampleValues);
        // });

        // // // Slice the top 10 objects for plotting
        // data = data.slice(0, 10);

        // // // Reverse the array due to Plotly's defaults
        // data = data.reverse();

        // // // Trace1 for the Data
        // var trace1 = {
        //     x: otuIds,
        //     y: sampleValues,
        //     text: otuLabels,
        //     // name: ,
        //     type: "bar",
        //     orientation: "h"
        // };

        // // // data   
        // // var chartData = [trace1];

        // // // Apply the group bar mode to the layout
        // var layout = {       
        //     margin: {
        //     l: 100,
        //     r: 100,
        //     t: 100,
        //     b: 100
        //     }
        // };

        // // // Render the plot to the div tag with id "plot"
        // Plotly.newPlot("bar", trace1, layout);
});
