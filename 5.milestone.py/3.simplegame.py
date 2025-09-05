game_list=[0,1,2,3,4]
def display(mli):
    print("Here is the current list: ")
    print(mli)
def gamer_choice():
    choice='Wrong choice'
    while choice not in ['0','1','2','3','4']:
        choice=input("Pick a position in (0,1,2,3,4) : ")
        if choice not in ['0','1','2','3','4']:
            print("Sorry invalid input!!!")
    return int(choice)
print(gamer_choice())
def replacement(game_list,position):
    user_replacemet=input("Enter a replacement for your position: ")
    game_list[position]=user_replacemet
    return game_list
print(replacement(game_list,1))
def gameon_choice():
    choice='Wrong choice'
    while choice not in ['y','n']:
        choice=input("Do you want to continue playing? (y or n): ")
        if choice not in ['y','n']:
            print("Sorry, please choose y or n")
    if choice=='y':
        return True
    else:
        return False
game_on=True
game_list=[0,1,2,3,4]
while game_on:
    display(gameon_choice)
    position=gamer_choice()
    game_list=replacement(game_list,position)
    display(game_list)
    game_on=gameon_choice()
