targets = [int(x) for x in input().split(" ")]
command = input()

while command != "End":

    command = command.split(" ")
    order = command[0]
    index = int(command[1])

    if order == "Shoot":
        if 0 <= index < len(targets):
            power = int(command[2])
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif order == "Add":
        if 0 <= index < len(targets):
            value = int(command[2])
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif order == "Strike":
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius
        if start_index >= 0 and end_index < len(targets):
            del targets[start_index:end_index+1]
        else:
            print("Strike missed!")

    command = input()

print("|".join([str(x) for x in targets]))