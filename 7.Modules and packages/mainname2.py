import mainname
print("Top level in mainname2.py")
mainname.myfunc()

if __name__=='__main__':
    print("mainname2.py is being run directly!!")
else:
    print("mainname2.py has been imported!!!")