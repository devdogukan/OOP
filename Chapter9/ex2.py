from abc import ABC, abstractmethod

class Animal(ABC):   # Nesne uretilemez
    
    @abstractmethod
    def walk(self): pass
    
    @abstractmethod
    def run(self): pass

class Bird(Animal):
    def __init__(self) -> None:
        print("bird")
        
    def walk(self):
        print("walk")
    
    def run(self):
        print("run")

b1 = Bird()