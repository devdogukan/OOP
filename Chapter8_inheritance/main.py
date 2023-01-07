from person import Person
from student import Student
from personel import Personel

def printm(person:Person):
    print(person.name, person.surname)
    
def yaz(str1:str):    # Tip zorlamasi bir yere kadar
    print(str1.name)

person1 = Person("Ahmet", "yilmaz", "12345", 2000)
#print(person1.name, person1.surname)

student1 = Student("Ali", "kilic", "11111", 2005,"010122", "Bil. Muh", 1)
#print(student1.name, student1.surname, student1.std_bolum, student1.std_class)

personel1 = Personel("Ayse", "Sahin", "22222", 2002, "554488", "bilgi islem")
#print(personel1.name, personel1.surname, personel1.sicil_no, personel1.department)

# print(person1.department)  AttributeError()

printm(person1)
printm(student1)
printm(personel1)
yaz(person1)