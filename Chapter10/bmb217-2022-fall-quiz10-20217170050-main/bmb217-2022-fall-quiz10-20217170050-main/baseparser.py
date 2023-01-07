from abc import ABC, abstractmethod
from typing import List
from person import Person

class BaseParser(ABC):

    def __init__(self) -> None:
        self.file_content:str = ''
        self.person_list:List[Person] = []
        
    def read_file(self, file_name:str):
        f = open(file_name, "r")
        self.file_content = f.read()

    def add_person(self,pid:str,name:str,surname:str):
        new_person = Person(pid,name,surname)
        self.person_list.append(new_person)
        
    @abstractmethod
    def parse_file(self):
        pass
    