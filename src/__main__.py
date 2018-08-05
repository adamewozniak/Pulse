from lib.controllers import controllers as controllers
import time

def main():
    while True:
        heartRate = controllers.getCurrentHeartRate()
        print(heartRate)
        print("bum bum")
        time.sleep(heartRate/60)


print(controllers.getCurrentHeartRate())


main()