class Person:
    """Person Class Defination"""
    _name:str = ""          # Person name
    _age:int = 0            # Person age
    _birth_day:int = 0      # Person birth day
    _weight:int = 0         # Person weight
    _height:int = 0         # Person height
    _bmi:int = 0            # Person bmi
    _bmi_status:str = ""    # Person bmi status
    
    def __init__(self, name:str, age:int, weight:int, height:int):
        """Constructor

        Args:
            name (str): Person name
            age (int): Person age
            weight (int): Person weight (in kg)
            height (int): Person height (in cm)
        """
        
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height
        self._birth_day = 2022 - self._age
        self.calculate_bmi()
        self.check_bmi()
        
    def calculate_bmi(self):
        
        self._bmi = self._weight / (self._height/100)**2
        
        return self._bmi
    
    def check_bmi(self):
        
        if self._bmi < 18.5:
            self._bmi_status = "UNDER WEIGHT"
        elif 18.5 <= self._bmi < 25:
            self._bmi_status = "NORMAL WEIGHT"
        elif 25 <= self._bmi < 30:
            self._bmi_status = "OVER WEIGHT"
        elif 30 <= self._bmi < 35:
            self._bmi_status = "OBESE (CLASS 1)"
        elif 35 <= self._bmi < 40:
            self._bmi_status = "OBESE (CLASS 2)"
        elif 40 <= self._bmi: 
            self._bmi_status = "OBESE (CLASS 3)"
            
        return self._bmi_status
    
    def print(self):
        print(f"Name: {self._name}\nAge: {self._age}\nBirthday: {self._birth_day}\nWeight: {self._weight}\nHeight: {self._height}\nBMI: {self._bmi} - {self._bmi_status}")