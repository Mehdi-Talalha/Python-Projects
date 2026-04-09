target = 32
low = 0
high = 1000
count = 0

guess = (low + high) // 2

while guess != target:
    if guess < target:
        low = guess
    else:
        high = guess
    guess = (low + high) // 2
    count += 1

print("conte: ", count)
print("answer: ", guess)