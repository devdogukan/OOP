class WriteError(Exception):
    pass

class Circle:
    __pi = 3.1415
    def __init__(self, r):
        self.__r = r
       
    @property
    def rc(self):
        return self.__r
    
    @rc.setter
    def rc(self, r):
        if r >= 0:
            self.__r = r
        #raise WriteError('mf vmf v ')
    
    @rc.deleter
    def rc(self):
        del self.__r
            
c1 = Circle(5)
print(c1.rc)
c1.rc = -1
print(c1.rc)
c1.rc = 12
print(c1.rc)
del c1.rc