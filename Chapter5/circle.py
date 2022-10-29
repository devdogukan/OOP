class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius
        
    @property
    def radius(self):
        """The radius property"""
        print('Getter calisti')
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print('Setter calisti')
        if value < 0:
            raise AttributeError('radius negatif olamaz!')
        else:
            self._radius = value