import abc

class AbstractClass(metaclass=abc.ABCMeta):  # Nesne uretilebilir
    
    @property
    @abc.abstractmethod
    def name(self):
        pass

class Test(AbstractClass):
    
    @property
    def name(self):
        return "a"


test = Test()
print(test.name)