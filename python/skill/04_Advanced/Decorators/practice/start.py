#start decorator

def start(func):
    def wrapper():
         print("Function started")
         func()
    return wrapper

@start
def hello():
    print("Hellow from function")

hello()