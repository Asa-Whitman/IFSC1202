#coding by Asa Whitman
import math
from random import randint
print("Welcome to the Winners and Losers game! Player wins if the final number is even!")
gameround = 1
int(gameround)
playerscore = 0
compscore = 0
while gameround <= 5:
    print("round {:d}".format(gameround))
    playerinput = int(input("enter a number between 1 and 5: "))
    if playerinput < 1 or playerinput > 5:  #resets the current loop if the player doesnt input a correct number.
        print("invalid number!")
        continue
    else:
        compinput = randint(1, 5)
        print("player entered {:d}. computer entered {:d}.".format(playerinput, compinput))
    roundtotal = playerinput + compinput
    print("sum is {:d}".format(roundtotal))
    if roundtotal %2 != 0:
        print("Computer wins this round!")
        compscore += 1
    else:
        print("Player wins this round!")
        playerscore +=1
    gameround +=1    
print("player's score: {:d}".format(playerscore))
print("computer's score: {:d}".format(compscore))
if compscore > playerscore:
    print("computer won the game! better luck next time, player!")
else:
    print("Player wins!")