import abc
from abc import ABC, abstractmethod

class Parent(ABC):
    
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
    
class Child(Parent):
    
    @property
    def geeks(self):
        return "child class"
    
try:
    r = Parent()
    print(r.geeks())
except Exception as err:
    print(err)
    
r = Child()
print(r.geeks)
