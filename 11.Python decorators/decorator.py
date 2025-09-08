def func():
    return "Hello!"
greet=func
del func #--->Even after deleting the function nothing changes to our greet variable
print(greet())
#-----------------------------------------------
def hello(name='Jose'):
    print("The hello() function has been executed!!")
    
    def greetings():
        return "\tThis is the greetings() function being executed!!!"
   
    
    def welcome():
        return "\tThis is the welcome() function executed!!!"
    '''
    print(greetings())
    print(welcome())
    print("This is the end of the hello() method!!")
    '''
    print("I am going to return a function!!!")
    if name=='Jose':
        return greetings
    else:                #-----> This helps us to call the function declared in hello out of its scope!!!
        return welcome
   

my_new_func=hello('Jose') #---> Assignment of the hello function to our new variable!!!
print(my_new_func())
#---------------------------------------------------------------------
def cool():
    
    def super_cool():
        return "I am very cool!!!"
    return super_cool

extracool=cool()
print(extracool())
#---------------------------------------------------------------------

def hello():
    return "Hi Beni!!"
def other(some_other_func):
    print("Other codes run here!!!")
    print(some_other_func())
other(hello)
#--------------------------------------------------------------------
def new_decorator(func):
    
    def wrap_func():
        print("Some extra code before the original function!!")
        func()
        print("Some extra codes after the original function!!")    
    return wrap_func

def func_needs_decorator():
    print("I need to be decorated!!!")

@new_decorator
def func_needs_decorator():
    print("I need to be decorated!!!")
func_needs_decorator()
