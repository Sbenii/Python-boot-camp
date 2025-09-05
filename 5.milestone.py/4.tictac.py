from IPython.display import clear_output
def display_board(board):
    clear_output()
    for i in range(1,10,3):
        print('|'+board[i] + '|' + board[i+1] + '|' + board[i+2]+'|')
        print('|-|'+'-|'+'-|')
Tboard = ['X']*10
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