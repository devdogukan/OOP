from typing import List
from person import Person
from baseparser import BaseParser
from csvparser import CsvParser 
from txtparser import TxtParser


def parse(parser:BaseParser, file_name:str):
    parser.read_file(file_name)
    parser.parse_file()
    return parser.person_list

def parse_files(file_list:List[str])->List[Person]:
    person_list:List[Person] = []
    txtparser = TxtParser() 
    csvparser = CsvParser()
    for file_name in file_list:
        file_extension = file_name.split('.')[1]
        if file_extension=='txt':
            person_list.extend(parse(txtparser,file_name))
        elif file_extension=='csv':
            person_list.extend(parse(csvparser,file_name))
    return person_list

def write_output(person_list = List[Person]): 
    for person in person_list:
        print(person) 

file_list = ['demo.txt','demo.json','demo.csv']
person_list = parse_files(file_list)
write_output(person_list)

"""
example output:

Person ID:987, Name:tarkan, Surname:tevetoglu
Person ID:654, Name:zeynep, Surname:sahin
Person ID:852, Name:kerem, Surname:uysal
Person ID:123, Name:ali, Surname:yilmaz
Person ID:234, Name:ayse, Surname:aslan
Person ID:345, Name:fatma, Surname:kaplan

"""
