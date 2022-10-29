def sus(first, second, num):
    def deco(f):
        def wrapper(*args):
            for arg in args:
                print(first*num)
                f(arg)
                print(second*num)
        return wrapper
    return deco

@sus('*/*', '+++', 10)
def name(*args):
    for arg in args:
        print(arg)
        
name('Dre', 'Nihat', 'Memo', 'Zulfu')