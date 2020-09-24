# FLASK_APP=app.py FLASK_ENV=development flask run
import pymongo
from flask import Flask, request
from flask_cors import CORS

import BE.database as dbService

app = Flask(__name__)
CORS(app)

@app.route("/query/data", methods=["GET"])
def query_data():
    station = request.args.get('station')
    month = request.args.get('month')
    year = request.args.get('year')
    result = dbService.getmonth(station, month, year)
    return {"result" : result}

@app.route("/find/station", methods=["GET"])
def list_station():
    result = dbService.listStation()
    return {"result": result}

@app.route("/find/dmy", methods=["GET"])
def list_dmy():
    DayMonthYear = request.args.get('DayMonthYear')
    result = dbService.listDuplicate(DayMonthYear)
    result.sort()
    return {"result": result}