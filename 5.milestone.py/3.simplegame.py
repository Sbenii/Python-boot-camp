game_list=[0,1,2,3,4]
def display(mli):
    print("Here is the current list: ")
    print(mli)
display(game_list) 
def gamer_choice():
    choice='Wrong choice'
    while choice not in ['0','1','2','3','4']:
        choice=input("Pick a position in (0,1,2,3,4) : ")
        if choice not in ['0','1','2','3','4']:
            print("Sorry invalid input!!!")
    return int(choice)
print(gamer_choice())
def replacement(game_list,position):
    user_replacemet=input("Enter a replacement for your position")
    