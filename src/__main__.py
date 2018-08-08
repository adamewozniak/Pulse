from lib.controllers import controllers as controllers
import time

def main():
    while True:
        heartRate = controllers.getCurrentHeartRate()
        for i in range(100):
            controllers.performHeartAction()
            time.sleep(60/heartRate)

main()