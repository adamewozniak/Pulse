from api import controllers as API


def getHeartRate():
    print(API.getHeart({
    'date':'today',
    'detail-level':'1sec',
    'start-time':'00:00',
    'end-time':'00:01'
}))