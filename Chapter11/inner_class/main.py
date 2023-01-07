from person import Person
from document import Document

p1 = Person()
p1.name = 'Ayse'
p1.surname = 'Kaplan'
p1.address.city = 'Osmaniye'
p1.address.town = 'GOP'

doc1 = Document()
doc1.author = 'Can Kululu'
doc1.title = 'Derste Zulum'
doc1.category = 'Mistik Roman'

p1.documents.append(doc1)
p1.add_document('Ekonomi 1', 'Keynes', 'Ders Kitabi')

print(p1)