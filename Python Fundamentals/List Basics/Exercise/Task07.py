names_gifts = input().split(" ")
command = input()

while command != "No Money":
    command = command.split(" ")

    if command[0] == "OutOfStock":
        if command[1] in names_gifts:
            for index, item in enumerate(names_gifts):
                if item == command[1]:
                    names_gifts[index] = "None"

    if command[0] == "Required":
        if 0 <= int(command[2]) < len(names_gifts):
            names_gifts[int(command[2])] = command[1]

    if command[0] == "JustInCase":
        names_gifts.pop()
        names_gifts.append(command[1])

    command = input()

gifts = " ".join([str(i) for i in names_gifts if i != "None"])
print(gifts)



