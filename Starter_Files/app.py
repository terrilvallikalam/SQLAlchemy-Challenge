# Import dependencies and Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Define user route
@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/percipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"api/v1.0/start/end"
    )

# Define user route when user selects.......
@app.route("/api/v1.0/percipitation")
def percipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    prcp_values = list(np.ravel(results))
    return jsonify(prcp_values)

@app.route("/api/v1.0/stations")
def percipitation():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    station_names = list(np.ravel(results))
    return jsonify(station_names)


@app.route("/api/v1.0/tobs")
def percipitation():
    session = Session(engine)
    results = session.query(Measurement.station, func.count(Measurement.station)).\
                group_by(Measurement.station).\
                order_by(func.count(Measurement.station).desc()).all()
    session.close()
    TOBS = list(np.ravel(results))
    return jsonify(TOBS)

@app.route("/api/v1.0/start")
def percipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.station, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                group_by(Measurement.station).\
                filter(Measurement.date =='2017-01-01').all()
    session.close()
    start_date = list(np.ravel(results))
    return jsonify(start_date)

@app.route("/api/v1.0/start/end")
def percipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.station, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                group_by(Measurement.station).\
                filter(Measurement.date.between('2016-01-01', '2017-01-01').all()
    session.close()
    info = list(np.ravel(results))
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)