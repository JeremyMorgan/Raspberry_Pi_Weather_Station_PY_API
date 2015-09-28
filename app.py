#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import datastore
import mysql.connector

##!flask/bin/python

from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

readings = [
    {
        'id': 1,
        'TempSensor1' : 10,
        'TempSensor2' : 20,
        'TempSensor3' : 30,
        'TempSensorAvg' : 15,
        'Humidity' : 34,
        'Pressure' : 1012,
        'Altitude' : 3.3,
        'SeaLevelPressure' : 394,
        'Lux' : 12.304,
        'TimeStamp' : time.strftime("%c")
    }
]

## AUTH STUFF ###

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

## Function to add URI to each requests
def make_public_reading(reading):
    new_reading = {}
    for field in reading:
        if field == 'id':
            new_reading['uri'] = url_for('get_reading', reading_id=reading['id'], _external=True)
        else:
            new_reading[field] = reading[field]
    return new_reading


## 404 handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

## Routes
## /weather/api/v1/readings  GET ALL
@app.route('/weather/api/v1/readings', methods=['GET'])
@auth.login_required
def get_tasks():
#   return jsonify({'readings': [make_public_reading(reading) for reading in readings]})
    return jsonify({'Readings': datastore.getReadings(2)})


@app.route('/weather/api/v1/readings/<int:reading_id>', methods=['GET'])
def get_task(reading_id):

    reading = [reading for reading in readings if reading['id'] == reading_id]

    if len(reading) == 0:
        abort(404)
    return jsonify({'reading': reading[0]})

@app.route('/weather/api/v1/readings', methods=['POST'])
def create_reading():
    if not request.json or not 'TempSensor1' in request.json:
        abort(400)
    reading = {

        "Altitude": request.json['Altitude'],
        "Humidity": request.json['Humidity'],
        "Lux": request.json['Lux'],
        "Pressure": request.json['Pressure'],
        "SeaLevelPressure": request.json['SeaLevelPressure'],
        "TempSensor1": request.json['TempSensor1'],
        "TempSensor2": request.json['TempSensor2'],
        "TempSensor3": request.json['TempSensor3'],
        "TempSensorAvg": request.json['TempSensorAvg'],
        "TimeStamp": "Sun Sep 27 17:07:11 2015",
        'id': readings[-1]['id'] + 1,
        #'description': request.json.get('description', ""),

    }
    readings.append(reading)
    return jsonify({'reading': reading}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
