def pop(x, y):
    total = 1
    for i in range(abs(y)):
        total = total * x

    if y < 0:
        return 1/total

    return total

print("result:")
print(pop(2, -3))