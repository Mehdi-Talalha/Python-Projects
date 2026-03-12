Height = int(input("Height: "))

if Height < 2 or Height > 8:
    print("invalide Hight")

for i in range(Height):
    print(" " * (Height - 1), end='')
    print("#" * i, end="")
    print("#" * i)

    Height = Height - 1
