tic=[' ']*10


#This function displays the tictactoe board
def display_board(tic):
    print(' '+tic[7]+'|'+tic[8]+'|'+tic[9])
    print('-------')
    print(' '+tic[4]+'|'+tic[5]+'|'+tic[6])
    print('-------')
    print(' '+tic[1]+'|'+tic[2]+'|'+tic[3])


#This function asks the player choices for symbol
def player_choice(board):
    pl1='wrong'
    # greeting
    print('Welcome To TicTacToe !!')
    while not (pl1=='o' or pl1=='x'):
        pl1=input('Hello Player1! Please choose -x- or -o- : ')
        print('Choose the correct input')
    if pl1=='x':
        pl2='o'
        print('\n Player1 : x \n Player2 : o')
    elif pl1=='o':
        pl2='x'
        print('\n Player1 : o \n Player2 : x')
    else:
        print('!!! Wrong Choice !!!')
    
    print('\n Lets Play !!!\n \n \n')
    inp_choice(board,pl1,pl2)


# This function asks the player to enter the position where they want their symbol
def inp_choice(tic,pl1,pl2):
    print('Choose a position (1-9) : ')
    winner=False
    while winner!=True:
        inp1=int(input('Player-1 : '))
        tic[inp1]=pl1
        display_board(tic)
        #VALIDATE IF THE PLAYER HAS WON OR NOT
        winner=bool(validate_result(tic))
        if winner:
            print('CONGRATS Player1 !!You Won')
            break
        inp2=int(input('Player-2 : '))
        tic[inp2]=pl2
        display_board(tic)
        winner=bool(validate_result(tic))
        if winner:
            print('CONGRATS Player2 !!You Won')
        # i+=1
    print('\n \n######## GAME OVER #########\n \n \n')
    play_again()



#This function will validate if the user won the game & return the name of the winner and winning status
def validate_result(tic):
    winner=False
    if ((tic[7]==tic[8]==tic[9]=='x') or 
    (tic[4]==tic[5]==tic[6]=='x') or 
    (tic[1]==tic[2]==tic[3]=='x') or 
    (tic[7]==tic[4]==tic[1]=='x') or 
    (tic[7]==tic[5]==tic[3]=='x') or 
    (tic[5]==tic[8]==tic[2]=='x') or 
    (tic[3]==tic[6]==tic[9]=='x') or 
    (tic[1]==tic[5]==tic[9]=='x')):
        winner='x' 
        return winner 
    elif ((tic[7]==tic[8]==tic[9]=='o') or 
    (tic[4]==tic[5]==tic[6]=='o') or 
    (tic[1]==tic[2]==tic[3]=='o') or 
    (tic[7]==tic[4]==tic[1]=='o') or 
    (tic[7]==tic[5]==tic[3]=='o') or 
    (tic[5]==tic[8]==tic[2]=='o') or 
    (tic[3]==tic[6]==tic[9]=='o') or 
    (tic[1]==tic[5]==tic[9]=='o')):
        winner='o'
        return winner 
    else:
        return winner

def play_again():
    inp=input('Do you want to play again (Y or N): ').upper()
    if inp=='Y':
        tic=[' ']*10
        player_choice(tic)
    else:
        print('\n\nBYE-BYE')



display_board(tic)   
player_choice(tic)
