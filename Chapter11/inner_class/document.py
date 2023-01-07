class Document:
    
    def __init__(self) -> None:
        self.title:str    = ''
        self.author:str   = ''
        self.category:str = ''
        
    def __str__(self) -> str:
        return f'{self.title} {self.author} {self.category}'