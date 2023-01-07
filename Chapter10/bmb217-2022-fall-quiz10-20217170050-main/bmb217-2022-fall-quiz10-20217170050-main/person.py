class Person:

    def __init__(self,pid:str, name:str, surname:str) -> None:
        self.pid = pid
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'Person ID:{self.pid}, Name:{self.name}, Surname:{self.surname}'
 