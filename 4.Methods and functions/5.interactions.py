#Simple guessing game
def shuffle_list(li):
    from random import shuffle
    shuffle(li)
    return li
def guess_game():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number between 0, 1 and 2: ")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("The guess is correct!!!")
    else:
        print("The guess is not correct!!!")
        print(mylist)
mylist=['','O','']
shuffled_list=shuffle_list(mylist)
guess=guess_game()
check_guess(shuffled_list,guess)