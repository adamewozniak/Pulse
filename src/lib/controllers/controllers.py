import lib.api.controllers as API
import datetime

def getHourlyHeartRates():
    now = datetime.datetime.now()

    fromTime = str(now.hour - 1) + ":" + str(now.minute)
    toTime = str(now.hour) + ":" + str(now.minute)

    heartRates = API.getHeart({
        'date':'today',
        'detail-level':'1sec',
        'start-time': fromTime,
        'end-time': toTime
    })['activities-heart-intraday']['dataset']

    return heartRates

def getCurrentHeartRate():

    rates = getHourlyHeartRates()
    
    return rates[len(rates) - 1]['value']
