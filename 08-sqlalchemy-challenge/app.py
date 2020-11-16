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

    # Convert list of tuples into normal list
    last_12 = []
    for date, prcp in last_12_session:
        last_12_dict = {}
        last_12_dict["date"] = date
        last_12_dict["prcp"] = prcp
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
    last_12_temp = (session.query(Measurement.station, Measurement.tobs)
                .filter(Measurement.date > '2016-08-23')
                .filter(Measurement.station == 'USC00519281')
                .all())
    session.close()

    # Convert list of tuples into normal list
    last_12_temp_dict = list(np.ravel(last_12_temp))

    return jsonify(last_12_temp_dict)



if __name__ == "__main__":
    app.run(debug=True)
