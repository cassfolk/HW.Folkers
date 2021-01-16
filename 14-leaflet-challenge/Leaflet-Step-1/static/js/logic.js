function createMap(earthQuakes) {

    // Create the tile layer that will be the background of our map
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "light-v10",
      accessToken: API_KEY
    });
  
    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
      "Light Map": lightmap
    };
  
    // Create an overlayMaps object to hold the earthQuakes layer
    var overlayMaps = {
      "Earth Quakes": earthQuakes
    };
  
    // Create the map object with options
    var map = L.map("mapid", {
      center: [39.8283, -98.5795],
      zoom: 5,
      layers: [lightmap, earthQuakes]
    });
  
    // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);
}

  // https://stackoverflow.com/questions/37357755/assign-color-of-leaflet-circlemarker-to-range-of-values
function getColor(d) {
return d >= 90 ? '#FF6961' : 
    d >= 70 ? '#FFB54C' : 
    d >= 50 ? '#F8D66D' :
    d >= 30 ? '#7ABD7E' : 
    d >= 10 ? '#8CD47E' : 
    '#BFFF7F';
}

function createMarkers(response) {

    // console.log(response.features);

    // // Pull the "features" property off of response
    var features = response.features;
    // console.log(response.features);


    // Initialize an array to hold earth quake sites
    var earthQuakeSites = [];

    // Loop through the earthQuakeSites array
    for (var index = 0; index < features.length; index++) {
        var site = features[index];
        // console.log(site);

        var lon = site.geometry.coordinates[0];
        // console.log(lon);

        var lat = site.geometry.coordinates[1];
        // console.log(lat);

        var depth = site.geometry.coordinates[2];
        // console.log(depth);

        var size = +site.properties.mag;
        // console.log(size);

                            ///// SEE 02-04 for help!!!!!
                            // legend

        // Change default marker
        var geojsonMarkerOptions = {
            radius: size * 3,
            fillColor: getColor(depth),
            color: "black",
            weight: 1,
            opacity: 1,
            fillOpacity: 1,

            };

        // For each site, create a marker and bind a popup with the site's info
        var earthQuakeMarker = L.circleMarker([lat, lon], geojsonMarkerOptions)
            .bindPopup("<h1>" + site.properties.title + "<hr><h3>Depth: " + depth +"</h1></h3>");
        
    // Add the marker to the Sites array
    earthQuakeSites.push(earthQuakeMarker);

    }

    // Create a layer group made from the earth quake markers array, pass it into the createMap function
    createMap(L.layerGroup(earthQuakeSites));
}
  
  
  // Perform an API call to the Earth QUake API to get the information. Call createMarkers when complete
  d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson", createMarkers);
  