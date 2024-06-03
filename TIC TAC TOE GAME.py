#TIC TAC TOE GAME
import random


board=["-","-","-",
       "-","-","-",
       "-","-","-"]

current_player="X"
winner=None
isgameRunning=True


#printing the game board
def game_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('---------')
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def player_input():
    inp=int(input("enter a  number(1-9): "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=current_player
    else:
        print("already player in the spot")
    
#check for win or tie
def checkhorzontial(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True
    
def checkvertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
    
def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True
    
def checkTie():
    global isgameRunning
    if "-" not in board:
        game_board(board)
        print("it's a tie")
        isgameRunning=False

def checkwin():
    global isgameRunning
    if checkhorzontial(board) or checkvertical(board) or checkdiagonal(board):
        game_board(board)
        print(f"winner is {winner}")
        isgameRunning=False
        
        
#i didn't understood from switch to last of the code(calling)
    
#switch the player
def switchplayer():
    global current_player
    if current_player=="X":             #this is player_input condition check, if it is true then goes inside
        current_player="O"              #this is swapping of current_player to O and 
                                                              
    else:                               #going to computer_input() function for random generating
        current_player="X"
        
        
def computer_input():
    while  current_player=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchplayer()
        
    

#check for win or tie again
while isgameRunning:
    game_board(board)
    player_input()
    checkwin()
    checkTie()
    switchplayer()          #this function swaps player from X to O, but isgamerunning is still True
    if isgameRunning:       #so, it comes here
        computer_input()    #so,this function generate a random value for O and place it in the board and again it checks
        checkwin()           #not executed
        checkTie( )      #not executed
                             #goes to gameboard(board) again 
    
