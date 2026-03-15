# this is Rocj Paper Scissor game 
import random, sys

choices = {
    "R":"Rock",
    "P":"Paper",
    "S":"Scissor"
}

choice = list(choices.keys())

# these variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

print("ROCK, PAPER, SCISSORS")

while True: # the main game loop
    
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    

    computerChoice = random.choice(choice).upper()

    print("Enter your move: (R)ock (P)aper (S)cossprs or (Q)uit.")
    playerChoice = input("> ").upper()
    print(f"> {computerChoice}")

    if playerChoice == computerChoice:
        print("It is a Tie!")
        ties+=1
    elif (playerChoice == 'R' and computerChoice == 'S') or (playerChoice == 'S' and computerChoice == 'P') or (playerChoice == 'P' and computerChoice == 'R'):
        print("The player wins:)")
        wins+=1
    elif playerChoice == 'Q':
        sys.exit()
    else:
        print("The computer wins:(")
        losses+=1