from tkinter import *

class PersonForm:
    def __init__(self) -> None:
        self.top = Toplevel()
        self.frame = Frame(self.top)
        
        self.tckid = StringVar()
        self.name = StringVar()
        self.surname = StringVar()
        
        
        
        self.frame.pack(padx=10, pady=10)