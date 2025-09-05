from IPython.display import clear_output

def display_board(board):
    clear_output()
    for i in range(0,9,3):
        print('|'+board[i] + '|' + board[i+1] + '|' + board[i+2]+'|')
        print('|-|'+'-|'+'-|')
board = [' ']*9
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
def place_marker(board,marker,position):
    while position not in range (0,9):
        position=int(input("Enter where you want to put your marker: "))
    board[position]=marker
    return position
p=place_marker(board,marker='',position='')
place_marker(board,"#",position)
display_board(board)

    
