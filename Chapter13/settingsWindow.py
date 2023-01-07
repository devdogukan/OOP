from settings import Settings
from tkinter import *

class SettingsWindow:
    def __init__(self, update) -> None:
        self.top = Toplevel()
        self.frame = Frame(self.top)
        self.update = update
        
        self.input = StringVar()
        entry = Entry(self.top, textvariable=self.input)
        entry.pack(padx=60, pady=30)
        
        self.option = IntVar()
        option1 = Radiobutton(self.top, value=1, text="Option 1", variable=self.option)
        option1.pack(padx=10, pady=10)
        option2 = Radiobutton(self.top, value=2, text="Option 2", variable=self.option)
        option2.pack(padx=10, pady=10)
        
        button = Button(self.frame, text="Apply Settings", command=self.submit)
        button.pack(pady=10)
        
        self.frame.pack(padx=10, pady=10)
        
    def submit(self):
        self.update(Settings(self.input.get(), self.option.get()))
        self.top.destroy()