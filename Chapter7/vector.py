class Vector:
    """Represent a vector in a multidimensional space"""
    
    def __init__(self, d) -> None:
        """Create d dimensional vector of zeros"""
        self._coords = [0]*d
        
    def __len__(self):
        """Return the dimension of thr vector"""
        return len(self._coords)
    
    def __getitem__(self, j):
        """"""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        
        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = self[i] + other[i]
            
        return result
    
    def __mul__(self, factor:float):
        result = Vector(len(self))
        
        for i in range(len(self)):
            result[i] = self[i] * factor
            
        return result
    
    def __contains__(self, other):
        for i in range(len(other)):
            if other[i] != 0:
                if self._coords.count(other[i]) != 1:
                    return False
        return True
    
    def __eq__(self, other) -> bool:
        return self._coords == other._coords
    
    def __ne__(self, other) -> bool:
        return not self == other  # use __eq__
    
    def __str__(self) -> str:
        return "<" + str(self._coords)[1:-1] + ">"