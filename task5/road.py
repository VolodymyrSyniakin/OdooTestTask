from task5.state import State
import time
from task5.light import Light
from task5 import state


class Road(Light):
   
    timeLast = time.time()
    
    lights = set()
    state
    
    secGreen = int()
    secYellow = int()
    secRed = int()
    
    def __init__ (self, state: State, secGreen=180, secYellow=10, secRed=60):
        self.state = state
        self.secGreen = secGreen
        self.secYellow = secYellow
        self.secRed = secRed
    
    def add (self, light):
        self.lights.add(light)
        
    def remove (self, light):
        for i in self.lights:
            if i == light:
                self.lights.remove(light)
       
    def nextPosition (self):
        for light in self.lights:
            light.nextPosition()
    
    def getInfo(self):
        timeNow = time.time()
        info = 'Next change: ' + str (timeNow - self.timeLast) + 'sec; '
        for light in self.lights:
            info += light.getInfo()
        return info
    
    def work (self):
        self.state.work(self)
        
