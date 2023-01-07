class Address:
    
    def __init__(self) -> None:
        self.city:str = ''
        self.town:str = ''
        
    def __str__(self) -> str:
        return f'{self.city} {self.town}'