from baseparser import BaseParser

class TxtParser(BaseParser):
    def __init__(self) -> None:
        super().__init__()
        
    def parse_file(self):
        for content in self.file_content.split("\n"):
            surname, name, id = content.split("-")
            self.add_person(id, name, surname)
