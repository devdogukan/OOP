class Programmer:
    
    """The Programmer Class"""
    
    __firstname:str = ""    # programmer firstname
    __lastname:str = ""     # programmer lastname
    __age:int = 0           # programmer age
    __price:int = 0         # programmer price
    __programmingLangugaes:list = None
    
    def __init__(self, firstname:str, lastname:str, age:int, price:int, *args) -> None:
        
        """Constructor
        
        firstname(str) : programmer firstname
        lastname(str) : programmer lastname
        age(int) : programmer age
        price(int) : programmer price
        
        """
        
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.price = price
        self.__programmingLangugaes = [arg for arg in args]
        
    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        if len(firstname) <= 1:
            raise AttributeError(f'{firstname} is not firstname')
        self.__firstname = firstname
            
    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        if len(lastname) <= 1:
            raise AttributeError(f'{lastname} is not lastname')
        self.__lastname = lastname
            
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 18:
            raise  AttributeError('age connot be younger than 18')
        self.__age = age
            
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 5000:
            raise AttributeError('Salary connot be less than $5000')
        self.__price = price
        
    @property
    def programmingLanguages(self):
        return self.__programmingLangugaes
    
    @programmingLanguages.setter
    def programmingLanguages(self, value):
        if self.__programmingLangugaes.count(value) == 0:
            self.__programmingLangugaes.append(value)
            
    def deco(f):
        def wrapper(self):
            print('*'*30)
            f(self)
            print('*'*30)
        return wrapper
    
    @deco     
    def print(self):
        print(f"Firstname: {self.firstname}\nLastname: {self.lastname}\nAge: {self.age}\nSalary: {self.price}\nProgramming Languages: {self.programmingLanguages}\n")