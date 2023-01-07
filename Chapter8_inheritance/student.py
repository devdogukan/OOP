from person import Person

class Student(Person):
    
    def __init__(self, name, surname, tcno, birthYear, std_no, std_bolum, std_class) -> None:
        super().__init__(name, surname, tcno, birthYear)
        self.std_no     = std_no
        self.std_bolum  = std_bolum
        self.std_class  = std_class