import random

imogies = {
    'r' : "🪨",
    'p' : "📄",
    's' : "✂️"
}

choices = ['r', 's', 'p']

while True:
    computer = random.choice(choices)

    user = input("Enter (r/p/s): ")
    if user not in choices:
        print("Invalide input")

    if computer == user:
        print("tie")
    elif user == 'r' and computer == 's' or user == 's' and computer == 'p' or user == 'p' and computer == 'r':
        print(f"The player WIN {imogies[user]}  > {imogies[computer]}")
    else:
        print(f"The computer win {imogies[computer]}  > {imogies[user]}")