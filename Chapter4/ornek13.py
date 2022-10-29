def susle(fonk):
    def wrapper():
        print('*'*10)
        fonk()
        print('-*'*10)
    return wrapper

@susle    
def hello_world():
    print("Hello, World!")
    
hello_world()
