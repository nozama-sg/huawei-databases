import json
from flask import request
from hctools import bluetooth 
from datetime import datetime, timedelta, date 

def locationUpdate():
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    userId = int(obj['userId'])
    roomName = obj['roomName']
    return json.dumps(bluetooth.locationUpdate(userId, roomName))

def currentLocation():
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    userId = int(obj['userId'])
    return json.dumps(bluetooth.currentLocation(userId))

def getBluetoothInformation(frequency):
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    userId = int(obj['userId'])
    if frequency not in ['day', 'week', 'month', 'year']:
        return {'status':300, 'error': 'Invalid Frequency for Health Information!'}

    lastDate = datetime.strptime(obj['date'], '%Y-%m-%d')
    lastDate = lastDate + timedelta(hours=23, minutes=59, seconds=59)
    firstDate = lastDate
    if frequency == 'day':
        firstDate = firstDate -  timedelta(days=1)
    elif frequency == 'week':
        firstDate = firstDate - timedelta(days=7)
    elif frequency == 'month':
        firstDate = firstDate - relativedelta(months=1)
    elif frequency == 'year':
        firstDate = firstDate - relativedelta(years=1)
    else:
        return {'status':300, 'error': 'Invalid Frequency for Health Information!'}

    return json.dumps(bluetooth.getBluetoothInformation(userId, firstDate, lastDate, frequency))
    


