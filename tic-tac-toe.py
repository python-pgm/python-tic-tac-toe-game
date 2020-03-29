## Game Rule ##
def game_rule():
    print('\nGAME RULES')
    print('------------')
    print('    1. This is a TWO player game.')
    print('    2. In this game, two tables will be shown side by side.')
    print('    3. Table on the left is a REFERENCE chart to understand position value of each cell in actual PLAYER BOARD')
    print('    4. Table on the right is the actual PLAYER BOARD in which each player''s entries will be reflected.')
    print('    5. From the two players, one player will be chosen randomly to play first.')
    print('    6. The first player to place their markers in three consecutive cells, ')
    print('       either horizontally, vertically or diagonally will WIN the game!!! ')
    
def clear_screen():
    os.system('cls|clear' if os.name == 'nt' else 'clear')

## Printing the Board and Position Information ##
def print_board(entry):

    clear_screen()
    print('\n')
    print('-- Position Chart --\t\t<== Player Board ==>\n')
    #print(' '*3 + '-'*13 + '\t\t' + ' '*3 + '-'*13)
    print(' '*3 + '  1 | 2 | 3  ' + '\t\t' + ' '*3 + '  ' + entry[1]+' | '+entry[2]+' | '+entry[3] + '  ')
    print(' '*3 + '-'*13 + '\t\t' + ' '*3  + '-'*13)
    print(' '*3 + '  4 | 5 | 6  ' + '\t\t' + ' '*3 + '  ' + entry[4]+' | '+entry[5]+' | '+entry[6] + '  ')
    print(' '*3 + '-'*13 + '\t\t' + ' '*3  +  '-'*13)
    print(' '*3 + '  7 | 8 | 9  ' + '\t\t' + ' '*3 + '  ' + entry[7]+' | '+entry[8]+' | '+entry[9] + '  ')
    #print(' '*3 + '-'*13 + '\t\t' + ' '*3  +  '-'*13)
    print('\n')

## Selecting a random first player to play first ##
def choose_first_player(player_list):
    selection = random.randint(0,1)
    return player_list[selection]

## Randomly chosen player making a choice of marker ##
def marker_choice(selected_player,player_choice):
    
    success = False
    
    while success == False:
        selected_player_choice = input('\n' + selected_player + ', will you prefer "X" or "O" as your marker ?  ').upper()
        if selected_player_choice in ['X','O']:
            success = True
        else:
            print('Not a valid marker choice. Please make a choice from available markers')

    other_player = [ player for player in list(player_choice.keys()) if player != selected_player ][0]
    other_choice = [ choice for choice in ['X','O'] if choice != selected_player_choice ][0]
    
    player_choice[selected_player] = selected_player_choice
    player_choice[other_player] = other_choice
    
    #print('\n')
    #print('Thanks for the input.')
    #print('Marker Selection : {} has chosen "{}". So {} will be using "{}"'.format(selected_player,
    #        selected_player_choice,other_player,other_choice))
    return player_choice

## Entering  selected Marker at position of choice ## 
def place_marker(board,player,choice):
    
    success = False
    
    while success == False:
        pos = int(input('{} : Enter the poistion at which you would like to mark "{}" : '.format(player,choice)))
        #print('Chosen Position : {}'.format(pos))
    
        if board[pos] not in ['X','O']:
            board[pos] = choice
            success = True
        else:
            print('This position is not emply. Please chose another position from table shown !!!')
    
    print_board(board)
    return board

## Check if there are anymore free spaces in Board ##
def check_free_position(board):  
    return ' ' in board.values() 

##  Checking if Player (based on Marker) WON !!! ##
def win_check(board,marker):
    
    if ( (board[1] == marker and board[2] == marker and board[3] == marker) or
         (board[4] == marker and board[5] == marker and board[6] == marker) or
         (board[7] == marker and board[8] == marker and board[9] == marker) or
         (board[1] == marker and board[4] == marker and board[7] == marker) or
         (board[2] == marker and board[5] == marker and board[8] == marker) or
         (board[3] == marker and board[6] == marker and board[9] == marker) or
         (board[1] == marker and board[5] == marker and board[9] == marker) or
         (board[3] == marker and board[5] == marker and board[7] == marker) ):
        return True
    else:
        return False

## Replay Function ##
def replay():
    return input('Would you like to play the game again ? (Yes/Y/yes/y) : ').lower().startswith('y')


## Main Function ##
import os
import random

while True:
    board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}     # A blank dictionary represending player board
    markers = ['X','O']                                                 # Only possible Markers

    print('\n\n<========== Welcome to Tic Tac Toe Game ==========>')
    game_rule()
    print_board(board)


    if not input('Are you ready to play this game (Y/N)? ').lower().startswith('y'):
        print('Sure.Please come back anytime you feel like playing Tic Tac Toe. Cheers !!!')
        exit()

    print_board(board)
    print('\n')
    player_1 = input('Player 1  - Please Enter Your Name : ')
    player_2 = input('Player 2  - Please Enter Your Name : ')

    player_choice = {player_1: ' ', player_2: ' '}                      # Dictionary mapping player against their marker
    player_list = list(player_choice.keys())                            # Getting list of player from player_choice dictionary

    print_board(board)
    selected_player = choose_first_player(player_list)
    print('\n\nWelcome {} and {}. In this round {} will be playing first'.format(player_1,player_2,selected_player))


    player_choice = marker_choice(selected_player,player_choice)
    other_player = [ player for player in player_list if player != selected_player ][0]

    print_board(board)
    print('Thank for input. Marker Selection : {} has chosen "{}". So {} will be using "{}"'.format(selected_player,
            player_choice[selected_player],other_player,player_choice[other_player]))

    input('We are good to start playing the game. Hit ENTER to continue..... ')

    print_board(board)
    while check_free_position(board):
        board = place_marker(board,selected_player,player_choice[selected_player])
        if win_check(board,player_choice[selected_player]):
            print_board(board)
            print('='*20)
            print('Congratulation {} !!!. You won this game.'.format(selected_player))
            print('='*20)
            break
        selected_player = [ player for player in player_list if player != selected_player ][0]

    if not check_free_position(board) and not win_check(board,'X') and not  win_check(board,'O'):
        print('WOW !! you both are equally good. This is a DRAW match')

    
    if not replay():
        print('Thank You for playing Tic Tac Toe')
        break