# Day 3

"""
Make a game of rock, paper scissors against the computer. 
Algorithm
    Tell user to enter either rock,paper or scissors
    Get the response
    Generate a random number from 1 to 3 (1=rock,2=paper,3=scissors)
    Compare user selection and computer selection
    Display who wins.

Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score
    Make an enumerated variable type to store choices.
"""

import random
i = 1
comp_score, user_score = 0, 0
while(i):
    user = int(input("Enter\n 1. Rock\n 2. Paper\n 3. Scissors\n"))
    comp = random.randrange(1,3,1)
    if(user == 1 or user == 2 or user == 3):
        if(user == 1 and comp == 2 or user == 2 and comp == 3 or user == 3 and comp == 1):
            print("Computer wins!!!")
            comp_score += 1
        elif(user == 1 and comp == 3 or user == 2 and comp == 1 or user == 3 and comp == 2):
            print("User wins!!!")
            user_score += 1
        else:
            print("Tie")
    else:
        print("Invalid entry :(")
        break
    i = int(input("Enter 1 to continue and 0 to stop playing."))
print("Computer Score:",comp_score)
print("User Score:",user_score)