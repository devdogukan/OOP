def decorator(fonk):
    def wrapper():
        print("fonksiyon cagirilmadan once calisacaklar")
        fonk()
        print('fonsiyon cagirildiktan sonra calisicaklar')
    return wrapper

def fonk1():
    print("fonk1 calisti")
    
def fonk2():
    print("fonk2 calisti")
    
def fonk3():
    print("fonk3 calisti")
    
yeni_fonk1 = decorator(fonk1)
yeni_fonk2 = decorator(fonk2)
yeni_fonk3 = decorator(fonk3)

yeni_fonk1()
yeni_fonk2()
yeni_fonk3()