import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Climate Data!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&#60;start&#62;<br/>"
        f"/api/v1.0/&#60;start&#62;/&#60;end&#62;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    year_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_date).all()
    session.close()

    all_precip = {}
    for date, precip in year_data:
        all_precip[date] = precip
       
    return jsonify(all_precip)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Station).all()
    session.close()
    
    all_stations = []
    for station in stations:
        all_stations.append(station.station)

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def temps():
    session = Session(engine)
    tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281', Measurement.date >= year_date).all()
    session.close()

    all_temps = []
    for x in tobs:
        all_temps.append(x)
    
    return jsonify(all_temps)


@app.route("/api/v1.0/<start>")
def get_date(start):
    session = Session(engine)
    temp_values = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    results = []
    for x in temp_values:
        results.append({
            "Min":x[0],
            "Average":x[1],
            "Max":x[2]
        })

    return  jsonify(results)


@app.route("/api/v1.0/<start>/<end>")
def get_dates(start, end):
    session = Session(engine)
    temp_values2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    session.close()

    results1 = []
    for x in temp_values2:
        results1.append({
            "Min":x[0],
            "Average":x[1],
            "Max":x[2]
        })

    return jsonify(results1)


if __name__ == "__main__":
    app.run(debug=True)