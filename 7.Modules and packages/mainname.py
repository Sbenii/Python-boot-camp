def myfunc():
    print("myfunc() in mainname.py")
print("Top level")
if __name__=='__main__':
    print("mainname.py is being run directly!!")
else:
    print("mainname.py has been imported!!!")