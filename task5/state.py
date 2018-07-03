from abc import ABCMeta, abstractmethod
import time


class State (metaclass=ABCMeta):
    
    @abstractmethod
    def work(self, road):
        pass
    
    
class DayAuto(State):

    def work(self, road):
        road.timeLast = time.time()
        time.sleep(road.secGreen)
        for light in road.lights:
            if light.type == "TRAFFIC":
                light.nextPosition()
                
        time.sleep(road.secYellow)
        road.nextPosition()
                
        road.timeLast = time.time()
        time.sleep(road.secRed)
        for light in road.lights:
            if light.type == "TRAFFIC":
                light.nextPosition()
                
        time.sleep(road.secYellow)
        road.nextPosition()
        

class NightAuto(State):

    def work(self, road):
        for light in road.lights:
            if light.type == 'FOOTER':
                light.indexColor = light.colors.index('RED')
            elif light.type == 'TRAFFIC':
                light.indexColor = light.colors.index('YELLOW')
