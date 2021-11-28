name = input()

for i in range(len(name)):
    for j in range(-1, i - (i - 1)):
        print(name[i], end="")