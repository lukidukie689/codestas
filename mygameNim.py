
"""
Game of Nim from Python for Everyone 3rd edition
"""

from random import seed, randint

"""
main() written by: Joseph Adams

This main function is the game play driver for Game of NIM.
"""

def main():                     # definition of main program
    seed()                      # initialize the random number generator for the game play

    # -------------------------------------------------------
    # INPUT - to randomize the game play
    # -------------------------------------------------------
    ballCount = randint(10, 100)# randomly generate the amount of balls to play
    turn = randint(0,1)         # randomly generate who goes first (0) player (1) computer
    mode = randint(0,1)         # randomly generate mode of computer (0) smart (1) stupid

    # -------------------------------------------------------
    # PROCESS - play the game of NIM taking turns
    # -------------------------------------------------------
    print("***** Game of NIM Starts *****")
    while ballCount > 0:        # if there are still balls left, then keep playing
        print("\t\tBall count:", ballCount)
        if turn == 0:           # player turn
            print("\n\tPLAYER TURN")
            ballCount= ballCount-(playerTurn(ballCount))
            turn = 1            # switch the turn 1 - for computer turn next
        else:                   # computer turn
            if mode == 0:       # computer smart mode
                print("\n\tCOMPUTER TURN - Mode: Smart")
                ballCount=ballCount-(computerSmart(ballCount))
            else:               # computer hard mode
                print("\n\tCOMPUTER TURN - Mode: Stupid")
                ballCount=ballCount-(computerStupid(ballCount))
            turn = 0            # switch the turn 0 - for player turn next
        # TODO: ballCount needs to be updated for each turn
                
    # -------------------------------------------------------
    # OUTPUT - The player who takes the last ball loses.
    # once the ballCount goes to 0, the turn switches, so it is the other
    # player then that wins
    # -------------------------------------------------------
    print("\t\tBall count:", ballCount)
    if turn == 0 and ballCount == 0:
        print("\n***** GAME of NIM Winner! PLAYER *****\n\n")
    else:
        print("\n***** Game of NIM Winner! COMPUTER *****\n\n")

        
def playerTurn(ballCount):
    ballsTaken= int(input("How many balls do you wish to take?")
    if ballsTaken<1:
            ballsTaken=int(input("Must take at least one. How many balls do you wish to take?"))
    
    elif ballsTaken> ballCount/2:
        if ballCount==1:
            ballsTaken=1
        elif ballCount==2:
            print("Must take one.")
            ballsTaken=1
            
        else:
            ballsTaken= int(input("Cannot take more than half. How many balls do you wish to take?"))
    return ballsTaken


def computerStupid(ballCount):
    if ballCount==1:
        ballsTaken=1
    elif ballCount==2:
         ballsTaken=1
    else:
        ballsTaken= randint(1, ballCount//2)
    return ballsTaken
    
def computerSmart(ballCount):
    if ballCount>63:
        ballsTaken=ballCount-63
    elif ballCount>31 and ballCount<63:
        ballsTaken= ballCount-31
    elif ballCount>15 and ballCount<31:
        ballsTaken=ballCount-15
    elif ballCount>7 and ballCount <15:
        ballsTaken=ballCount-7
    elif ballCount>3 and ballCount<7:
        ballsTaken=ballCount-3
    else:
        if ballCount==1:
            ballsTaken=1
        elif ballCount==2:
            ballsTaken=1
        else:
            ballsTaken= randint(1, ballCount//2)
    return ballsTaken
    
    
    

main()          # execution of main program
