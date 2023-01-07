from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def noofsides(self):
        pass
    
class Triangle(Polygon):
    
    def noofsides(self):
        print("I have 3 sides")
        
class Pentagon(Polygon):
    
    def noofsides(self):
        print("I have 5 sides")
        
class Hexagon(Polygon):
    
    def noofsides(self):
        print("I have 6 sides")
        
class Quadriliteral(Polygon):
    
    def noofsides(self):
        print("I have 4 sides")
        
        
R = Triangle()
R.noofsides()

K = Quadriliteral()
K.noofsides()

P = Pentagon()
P.noofsides()

H = Hexagon()
H.noofsides()

