def user_choice():
    choice='Wrong'
    acceptable_values=range(0,10)
    within_range=False
    while choice.isdigit()== False or within_range==False:
        choice=input("Enter a number between 0-10: ")
        if choice.isdigit()==False:
            print("Sorry that's not a digit!!")
        if choice.isdigit()== True:
            if int(choice) in acceptable_values:
                within_range= True
            else:
                print("You are out of acceptable range!!!")
                within_range= False
    return int(choice)
print(user_choice())