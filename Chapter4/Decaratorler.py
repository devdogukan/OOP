
import time

def deco(f):
    def wrapper(*args):
        baslangic = time.time()
        print(f'baslangic: \t {baslangic}')
        
        f(*args)
        
        bitis = time.time()
        print(f'bitis: \t {bitis}')
        print(f'gecen sure: \t {bitis-baslangic}')
    return wrapper

@deco
def fact(a):
    f = 1
    while a > 1:
        f *= a
        a = a - 1
    print(f)

fact(5)


'''
def deco(msg1, msg2):
    def ara_katman(f):
        def wrapper(*args):
            print(msg1)
            f(*args)
            print(msg2)
        return wrapper
    return ara_katman

@deco('sa', 'as')
def add(*args):
    print(sum(args))
    
add(5, 6)
'''

'''
def deco(f):
    def wrapper(*args):
        print('start')
        f(*args)
        print('end')
    return wrapper

@deco
def add(*args):
    print(sum(args))
    
add(5, 6)
'''

'''
def deco(f):
    def wrapper():
        print('start')
        f()
        print('end')
    return wrapper

def deneme():
    print('heyyooo')
    
deneme = deco(deneme)
deneme()

@deco
def heyyo():
    print('deneme')
heyyo()
'''

'''
def deneme():
    return 'heyoooo'

def test(f):
    print('test run')
    print(f())
    
test(deneme)
'''

'''
def deneme():
    print('Heyoo')
    def test():
        return 'cvsdvccvachv'
    return test

f = deneme()
print(f())
'''