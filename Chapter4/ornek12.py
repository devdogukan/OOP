def susle(fonk):
    def wrapper():
        print('*'*10)
        fonk()
        print('-*'*10)
    return wrapper
        
def hello_word():
    print("Hello, World!")
    
suslu_hello_world = susle(hello_word)
suslu_hello_world()