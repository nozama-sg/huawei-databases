import mysql.connector 
from pprint import pprint
from datetime import datetime
from calendar import monthrange
from password import SQL_PASSWORD

mydb = mysql.connector.connect(
  host="192.168.0.27",
  user="root",
  password=SQL_PASSWORD,
  database='healthData'
)

mycursor = mydb.cursor()

''' https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/ '''
def number_of_days_in_month(year, month):
    print(year,month)
    return monthrange(year, month)[1]

def getHealthInformation(healthInfoType, userId, firstDate, lastDate, frequency):
    healthInfoType = healthInfoType.lower()
    firstDateString = firstDate.strftime("%Y-%m-%d, %H:%M:%S")
    lastDateString = lastDate.strftime("%Y-%m-%d, %H:%M:%S")
    sqlCommand = f"SELECT value,timestamp FROM `{healthInfoType}` WHERE timestamp BETWEEN '{firstDateString}' AND '{lastDateString}' AND userId = {userId}"
    mycursor.execute(sqlCommand)
    result = mycursor.fetchall() 
    pprint(result)
    data = {}

    maxValue = 0
    if frequency == 'day': maxValue = 24
    elif frequency == 'week': maxValue = 7
    elif frequency == 'month': maxValue = number_of_days_in_month(lastDate.year, lastDate.month)
    else: maxValue = 12
    if frequency in ['day', 'week']:
        ''' 0 to 23 hours '''
        ''' 0 to 6 days of week '''
        for i in range(maxValue): data[i] = []
    else:
        ''' 1 to 31 days of month '''
        ''' 1 to 12 months of year '''
        for i in range(1, maxValue+1): data[i] = []
    
    for entry in result:
        target = 0 
        value = entry[0]
        timestamp = entry[1]
        if frequency == 'day':target = timestamp.hour
        elif frequency == 'week': target = timestamp.weekday()
        elif frequency == 'month': target = timestamp.day
        elif frequency == 'year': target = timestamp.month

        data[target].append(value)

    processedData = []
    for i in data:
        id = i
        values = data[i]
        if len(values) == 0:
            processedData.append({'y': 0, 'x': i})
        else:
            processedData.append({'y': int(sum(values)/len(values)), 'x': i})
    return processedData

def updateHealthInformation(healthInfoType, userId, value):
    healthInfoType = healthInfoType.lower()
    sqlCommand = f"INSERT INTO `{healthInfoType}` (userId, value, timestamp) VALUES ({userId}, {value}, CURRENT_TIMESTAMP)"
    mycursor.execute(sqlCommand)
    mydb.commit()
    return {'status': 200}

