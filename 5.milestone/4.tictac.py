from IPython.display import clear_output
def display_board(board):
    clear_output()
    for i in range(1,10,3):
        print('|'+board[i] + '|' + board[i+1] + '|' + board[i+2]+'|')
        print('|-|'+'-|'+'-|')
#-----------------------------------------------
def player_input():
    marker=''
    while marker not in ['X','O']:
        marker=input("Player one choose between O or X: ")
        player1=marker
    if player1=='O':
            player2='X'
    else:
            player2='O'
    return(player1,player2)
#-----------------------------------------------
def place_marker(board,marker,position):
    board[position]=marker
#-----------------------------------------------
def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark)or
            (board[4]==board[5]==board[6]==mark)or
            (board[7]==board[8]==board[9]==mark)or
            (board[1]==board[4]==board[7]==mark)or
            (board[2]==board[5]==board[8]==mark)or
            (board[3]==board[6]==board[9]==mark)or
            (board[1]==board[5]==board[9]==mark)or
            (board[3]==board[5]==board[7]==mark))
#-----------------------------------------------   
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player1'
    else:
        return 'Player2'
#-----------------------------------------------
def space_check(board,position):
    return board[position]==' '
#-----------------------------------------------
def full_board_check(board):
    for i in range (0,10):
        if space_check(board,i):
            return False
        else:
            return True
#-----------------------------------------------
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position from 1-9: "))
    return position
def rematch():
    choice=(input("Rematch? y or n: "))
    return choice=='y'
#-----------------------------------------------
print("Welcome to the TIC TAC TOE!!")
while True:
    Tboard = [' ']*10
    player1_marker,player2_marker=player_input()
    
    turn =choose_first()
    print(turn+'will go first!!!')
    
    play_game=input("Ready to play? y or n: ")
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn=='Player1':
            display_board(Tboard)
            position=player_choice(Tboard)
            place_marker(Tboard,player1_marker,position)
            if win_check(Tboard,player1_marker):
                display_board(Tboard)
                print("Player 1 won!!!!")
                game_on=False
            else:
                if full_board_check(Tboard):
                    display_board((Tboard))
                    print("It is a draw!!")
                    game_on=False
                else:
                    turn='Player2'
        else:
            display_board(Tboard)
            position=player_choice(Tboard)
            place_marker(Tboard,player2_marker,position)
            if win_check(Tboard,player2_marker):
                display_board(Tboard)
                print("Player 2 won!!!!")
                game_on=False
            else:
                if full_board_check(Tboard):
                    display_board((Tboard))
                    print("It is a draw!!")
                    game_on=False
                else: turn='Player1'
            
    if not rematch():
        break