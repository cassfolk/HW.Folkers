import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine=engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)

# HOME PAGE
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"These are the available routes:</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/< start ></br>"
        f"/api/v1.0/< start >/< end ></br>"
    )

# Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    """Perform a query to retrieve the data and precipitation scores"""
    sel = [Measurement.date,
        Measurement.prcp]

    last_12_session = (session.query(*sel)
    .filter(Measurement.date >= '2016-08-23')
    .filter(Measurement.date <= '2017-08-23')
    .all())

    session.close()

    last_12 = []

    for date, prcp in last_12_session:
        last_12_dict = {date: prcp}
        last_12.append(last_12_dict)
    

    return jsonify(last_12)


#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    """List all Stations"""
    stations = (session.query(Measurement.station)
    .group_by(Measurement.station)
    .all())

    session.close()

    # Convert list of tuples into normal list
    stations_dict = list(np.ravel(stations))

    return jsonify(stations_dict)

#Query the dates and temperature observations of the most active station for the last year of data.
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    """Query the dates and temperature observations of the most active station for the last year of data."""
    last_12_tobs_session = (session.query(Measurement.tobs, Measurement.station, Measurement.date)
                .filter(Measurement.date > '2016-08-23')
                .filter(Measurement.station == 'USC00519281')
                .all())

    session.close()

    last_12_tobs = []

    for tobs, station, date in last_12_tobs_session:
        last_12_tobs_dict = {}
        last_12_tobs_dict["tobs"] = tobs
        last_12_tobs_dict["station"] = station
        last_12_tobs_dict["date"] = date
        last_12_tobs.append(last_12_tobs_dict)

    return jsonify(last_12_tobs)

@app.route("api/v1.0/<start>/<end>")
                ##### HERE with start & end?
                ##### HERE with start & end?
                ##### HERE with start & end?
def date(start, end):
    """Return a JSON list of min temp, avg temp, and max temp for a given start or start-end range."""

    """Start only, calculate TMIN, TAVG, and TMAX for all dates <= to the start date."""
    # find <= start date
    session = Session(engine)
    
    sel = [func.min(Measurement.tobs), 
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)]

    start_session = (session.query(*sel)
                ##### HERE with start & end?
                ##### HERE with start & end?
                ##### HERE with start & end?
    .filter(Measurement.date <= start)
    .all())


    """Start & End, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive."""
    # find between start & end
    start_end_session = (session.query(*sel)
                ##### HERE with start & end?
                ##### HERE with start & end?
                ##### HERE with start & end?
    .filter(Measurement.date <= start)
    .filter(Measurement.date >= end)
    .all())
    
    session.close()
    
    
    # start only
    start_only = []

    for min, avg, max in start_session:
        start_dict = {}
        start_dict["min"] = min
        start_dict["avg"] = avg
        start_dict["max"] = max
        start_only.append(start_dict)
    
    # start end 
    start_end = []
    for min, avg, max in start_end_session:
        start_end_dict = {}
        start_end_dict["min"] = min
        start_end_dict["avg"] = avg
        start_end_dict["max"] = max
        start_end.append(start_end_dict)

                ##### HERE with start & end?
                ##### HERE with start & end?
                ##### HERE with start & end?
    if end == "":
        return jsonify()
    else:
        return jsonify(start_only)




if __name__ == "__main__":
    app.run(debug=True)
