#Simple game of replacing a string in a given list
game_list=[1,2,3]
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)
def position_choice():
    choice='W'
    while choice not in ['0','1','2']:
        choice=input("Please enter a position you want to change from 0-2: ")
        if choice not in ['0','1','2']:
            print("Sorry the position you entered is incorrect!!!")
    return int(choice)
def replacement_choice(game_list,position):
    user_replacement=input("Enter a string to place at the position: ")
    game_list[position]=user_replacement
    return game_list
def game_on():
    choice='W'
    gameon=True
    while choice not in ['y','n']:
        choice=input("Do you want to continue playing? (y or n): ")
        if choice not in ['y','n']:
            print("Please choose between y or n: ")
    if choice=='y':
        gameon
        position_choice()
        print( replacement_choice(game_list,position))
        gameon=game_on()
    else:
        gameon=False
        print("Thanks for playing!!!")
display_game(game_list)
position=position_choice()
print(replacement_choice(game_list,position))
game_on()