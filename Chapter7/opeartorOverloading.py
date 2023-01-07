class Sum:
    def __init__(self,a) -> None:
        self.a = a
        
    def __add__(self, b):
        return self.a + b.a
    
    def __str__(self) -> str:
        return f"{self.a}"
    
    def __repr__(self) -> str:
        return "Class of Sum"
    
a = Sum(5)
b = Sum(6) 
print(a+b)
print(a)
print(Sum)