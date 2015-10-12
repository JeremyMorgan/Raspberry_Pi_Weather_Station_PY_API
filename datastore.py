
import time

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='USERNAME', password='PASSWORD', database='weather')

cursor = mariadb_connection.cursor()


readings = [
    {
        'id': 1,
        'TempSensor1' : 1,
        'TempSensor2' : 2,
        'TempSensor3' : 3,
        'TempSensorAvg' : 1.5,
        'Humidity' : 22,
        'Pressure' : 33,
        'Altitude' : 44,
        'SeaLevelPressure' : 55,
        'Lux' : 66,
        'TimeStamp' : time.strftime("%c")
    }
]

def getReadings(amount):
    # This is where we will pull from:
    #
    # - Get readings (amount)
    # - Get last hour
    # - Get last day
    # - Get last 7 days
    #
    return readings

def addReading(reading):

    print reading.TempSensor1

    cursor.execute("INSERT INTO reading (TempSensor1,TempSensor2,TempSensor3,TempSensorAvg,Humidity,Pressure,Altitude,SeaLevelPressure,Lux,TimeStamp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())", (reading.TempSensor1,reading.TempSensor2,reading.TempSensor3,reading.TempSensorAvg,reading.Humidity,reading.Pressure,reading.Altitude,reading.SeaLevelPressure,reading.Lux))
    mariadb_connection.commit()
    return reading

