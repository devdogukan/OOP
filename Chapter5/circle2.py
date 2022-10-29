from math import sqrt


class Circle:
    pi = 3.14159
    def __init__(self, radius) -> None:
        self._radius = radius  # instance variable
        
    @property
    def radius(self):
        """The radius property"""
        print('Radius Getter calisti')
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print('Radius Setter calisti')
        if value < 0:
            raise AttributeError('radius negatif olamaz!')
        else:
            self._radius = value

    @property # property
    def diameter(self):
        print('Diameter Getter Calisti')
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        print('dimater setter calisti')
        self.radius = value / 2
        
    @property
    def area(self): # method
        return self.pi * self.radius * self.radius
    
    @area.setter
    def area(self, value):
        self.radius = sqrt((value/self.pi))