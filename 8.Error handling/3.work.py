def ask():
    while True:
        try:
            num=int(input("Enter a number to be squared: "))
            result=num**2
        except:
            print("An error occured! Please try again!")
            continue
        else:
            print("Thank you, your number squared: {}".format(result))
            break
ask()