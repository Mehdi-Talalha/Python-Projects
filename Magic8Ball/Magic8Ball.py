import random

messages = [
    'it is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print("Ask a Yes or No question:")
input("> ")

print(messages[random.randint(0, len(messages) - 1)])