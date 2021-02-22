# Import Dependencies
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station


# Create App
app = Flask(__name__)


# Define Endpoints and List Available Routes

@app.route("/")
def home():
    return """
    <h1>Welcome to the Hawaii Climate Analysis API!</h1><br/>
    <h2>Available Routes:</h2><br/>
        /api/v1.0/precipitation<br/>
        /api/v1.0/station<br/>
        /api/v1.0/tobs<br/>
        /api/v1.0/start=YYYY-MM-DD<br/>
        api/v1.0/start=YYYY-MM-DD/end=YYYY-MM-DD;
    """


# Precipitation Route

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    target_date = dt.date(2017, 8, 23)
    delta = dt.timedelta(days=365)
    query_data = target_date - delta

    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > query_data).order_by(Measurement.date.desc()).all()
    session.close()

    precipitation_list = []
    for i in range(len(results)):
        precipitation_dict = {}
        precipitation_dict[results[i][0]] = results[i][1]
        precipitation_list.append(precipitation_dict)

    return jsonify(precipitation_list)


# Stations Route
@app.route("/api/v1.0/station")
def station():
    session = Session(engine)
    results = session.query(Station.name).all()
    session.close()

    station_ = list(np.ravel(results))

    return jsonify(station_)

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)