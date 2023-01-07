class Vector:
    def __init__(self, factor) -> None:
        self._coordinate = [0]*factor
        
    def __getitem__(self, index):
        return self._coordinate[index]
    
    def __setitem__(self, index, value):
        self._coordinate[index] = value
        
    def __len__(self):
        return len(self._coordinate)
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        
        result = Vector(len(self))
        
        for i in range(len(self)):
            result[i] = self[i] + other[i]
            
        return result
    
    def __mul__(self, factor):
        result = Vector(len(self))
        
        for i in range(len(self)):
            result[i] = self[i] * factor
            
        return result
    
    def __eq__(self, __o: object) -> bool:
        return self._coordinate == __o._coordinate
    
    def __ne__(self, __o: object) -> bool:
        return not self == __o
    
    def __str__(self) -> str:
        return "<" + str(self._coordinate)[1, -1] + ">"