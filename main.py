print(" welcome to Rock Paper Scissors")
print("_________________________________")

import random

while True:
    choices = ["R", "P", "S"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
         print("Wrong input")
         player = input("R, P, or S?: ").upper()

    if player == computer:
       print("computer: ",computer)
       print("player: ",player)
       print("Tie:")
    elif player == "R":
        if computer == "P":
           print("computer: ",computer)
           print("player: ",player)
           print("You Loss:")
        if computer == "S":
           print("computer: ",computer)
           print("player: ",player)
           print("You Win:")
    elif player == "S":
        if computer == "R":
           print("computer: ",computer)
           print("player: ",player)
           print("You Loss:")
        if computer == "P":
           print("computer: ",computer)
           print("player: ",player)
           print("You Win:")
    elif player == "P":
        if computer == "S":
           print("computer: ",computer)
           print("player: ",player)
           print("You Loss:")
        if computer == "R":
           print("computer: ",computer)
           print("player: ",player)
           print("You Win:")
           
    play_again = input("Play again? (Y/N): ").upper()
    
    if play_again != "Y":
        break
        
print("Bye, Thanks for playing!")