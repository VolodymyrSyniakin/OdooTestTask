from abc import ABCMeta, abstractmethod


class Light(metaclass=ABCMeta):
       
    @abstractmethod   
    def nextPosition (self):
        pass
        
    @abstractmethod
    def getInfo(self):
        pass

                
class LightFooter (Light):
    handOn = False
    type = str()
    indexColor = int()
    colors = tuple()
    
    def __init__(self, color):
        self.colors = ("RED", "GREEN")
        self.indexColor = self.colors.index(color)
        self.type = 'FOOTER'
        
    def nextPosition (self):
        if not self.handOn:
            if self.indexColor == len(self.colors) - 1:
                self.indexColor = 0
            else:
                self.indexColor += 1
        pass
    
    def getInfo(self):
        return str (' [type: ' + self.type + ' state: ' + self.colors[self.indexColor] + ']')

    
class LightTraffic(Light):
    handOn = False
    type = str()
    indexColor = int()
    colors = tuple()
    
    def __init__(self, color):
        self.color = color
        self.colors = ("RED", "YELLOW", "GREEN", "YELLOW")
        self.indexColor = self.colors.index(color)
        self.type = 'TRAFFIC'
    
    def nextPosition (self):
        if not self.handOn:
            if self.indexColor == len(self.colors) - 1:
                self.indexColor = 0
            else:
                self.indexColor += 1
    
    def getInfo(self):
        return str (' [type: ' + self.type + ' state: ' + self.colors[self.indexColor] + ']')
