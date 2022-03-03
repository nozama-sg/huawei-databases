import json
from flask import request
from hctools import announcements

def announcementEndpointUpdate():
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    userId = obj['userId']
    tunnelUrl = obj['tunnelUrl']
    return json.dumps(announcements.announcementEndpointUpdate(userId, tunnelUrl))

def recordedMessage():
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    userId = obj['userId']
    text = obj['text']
    return json.dumps(announcements.recordedMessage(userId, text))