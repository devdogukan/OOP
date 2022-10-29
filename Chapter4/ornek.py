def fonk1():
    print('fonk1 called')
    
def fonk2(ilk_arguman):
    print('fonk2 called')
    print(f'ilk arguman: {ilk_arguman}')
    
def fonk_topla2(a, b):
    toplam = a+b
    print('fonk_topla2 calisti')
    print(f'ilk arguman {a}')
    print(f'ikinci arguman {b}')
    print(f'toplam {toplam}')
    
def fonk_topla3(a, b, c):
    toplam = a+b+c
    print('fonk_topla3 calisti')
    print(f'toplam {toplam}')
    
fonk1()
fonk2('1. arguman')
fonk_topla2(3, 5)
fonk_topla3(6, 4, 2)
