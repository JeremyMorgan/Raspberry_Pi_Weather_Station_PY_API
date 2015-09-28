
import time

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
    return readings

