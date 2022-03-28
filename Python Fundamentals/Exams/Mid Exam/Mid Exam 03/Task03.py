def shoot(idx):
    power = int(command[2])
    if 0 <= idx < len(targets):
        targets[idx] -= power
        if targets[idx] <= 0:
            del targets[idx]


def add(idx):
    value = int(command[2])
    if 0 <= idx < len(targets):
        targets.insert(idx, value)
    else:
        print("Invalid placement!")


def strike(idx):
    radius = int(command[2])
    start_index = idx - radius
    end_index = idx + radius
    if start_index >= 0 and end_index < len(targets):
        del targets[start_index:end_index + 1]
    else:
        print("Strike missed!")


targets = [int(x) for x in input().split(" ")]
command = input()

while command != "End":

    command = command.split(" ")
    order = command[0]
    index = int(command[1])

    if order == "Shoot":
        shoot(index)
    if order == "Add":
        add(index)
    if order == "Strike":
        strike(index)

    command = input()

print("|".join([str(x) for x in targets]))