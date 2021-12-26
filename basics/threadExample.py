from time import *
from threading import Thread


def runLeds(delay):
    while True:
        print("Leds on")
        sleep(delay)
        print("Leds OFF")
        sleep(delay)


def runSwitch(delay):
    while True:
        print('..........Switch on')
        sleep(delay)
        print("..........Switch OFF")
        sleep(delay)


ledThread = Thread(target=runLeds, args=(5,))
switchThread = Thread(target=runSwitch, args=(1,))

ledThread.daemon = True
switchThread.daemon = True


ledThread.start()
switchThread.start()
while True:
    pass