try:
    f=open('testfile','w+')
    f.write("Write a test line!!")
except:
    print("All other exceptions!!")
finally:
    print("I always run!!")
    
def ask_for_int():
    while True:
        try:
          result=int(input("Enter a number: "))
        except:
          print("Whoops that's not a number!!")
          continue
        else:
            print("Yes thank you!!")
            break
        finally:
          print("This is the end of try/except/finally!!")
          print("I will always run at the end")
ask_for_int()