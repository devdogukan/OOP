from person import Person

class Personel(Person):
    
    def __init__(self, name, surname, tcno, birthYear, sicil_no, departmant) -> None:
        super().__init__(name, surname, tcno, birthYear)
        self.sicil_no   = sicil_no
        self.department = departmant