from task5.road import Road
from task5.state import NightAuto, DayAuto
from task5.light import LightFooter, LightTraffic
import threading


def menu ():
    global closeThr
    while True:
        command = int(input("0-exit, 1-getInfo"))
        if command == 0:
            closeThr = True
            break
        if command == 1:
            print(road.getInfo())

        
def workInThread ():
    global road
    global closeThr
    while not closeThr:
        road.work()

        
# init
nightState = NightAuto()
dayState = DayAuto()
road = Road(dayState, 10, 5, 10)

lightF1 = LightFooter("GREEN")
lightT1 = LightTraffic("RED")
road.add(lightF1)
road.add(lightT1)

# thread to work
closeThr = False
t1 = threading.Thread(target=workInThread)
t1.start()

menu()

