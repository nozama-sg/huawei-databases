import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from flask import request
from hctools import healthInfo

def getHealthInformation(healthInfoType, frequency):
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    if healthInfoType not in ['heartRate', 'bloodOxygen', 'stepCount']:
        return {'status':300, 'error': 'Invalid Type of Health Information!'}
    if frequency not in ['day', 'week', 'month', 'year']:
        return {'status':300, 'error': 'Invalid Frequency for Health Information!'}
    userId = obj['userId']
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

    return json.dumps(healthInfo.getHealthInformation(healthInfoType, userId, firstDate, lastDate, frequency))

def updateHealthInformation(healthInfoType):
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    if healthInfoType not in ['heartRate', 'bloodOxygen', 'stepCount']:
        return {'status':300, 'error': 'Invalid Type of Health Information!'}
    value = obj['value']
    userId = obj['userId']
    return json.dumps(healthInfo.updateHealthInformation(healthInfoType, userId, value))
