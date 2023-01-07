from document import Document
from typing import List
from address import Address

class Person:
    
    def __init__(self) -> None:
        self.name:str = ''
        self.surname:str = ''
        self.documents:List[Document] = []
        self.address = Address()
        
    def add_document(self, title, author, category):
        new_doc = Document()
        new_doc.title = title
        new_doc.author = author
        new_doc.category = category
        
        self.documents.append(new_doc)
        
    def __str__(self) -> str:
        new_str = f'Name:{self.name}\nSurname:{self.surname}\n'
        new_str += str(self.address) + '\n'
        for doc in self.documents:
            new_str += '*' +str(doc) + '\n'
            
        return new_str