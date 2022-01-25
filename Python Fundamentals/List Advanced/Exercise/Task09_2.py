def check_index(tgs, idx):
    if 0 <= idx < len(tgs):
        return True
    else:
        return False


def check_start_end_index(tgs, start_idx, end_idx):
    if start_idx >= 0 and end_idx < len(tgs):
        return True
    else:
        return False


def do_shoot(tgs, idx, pwr):
    if check_index(tgs, idx):
        tgs[idx] -= pwr
        if tgs[idx] <= 0:
            tgs.remove(tgs[idx])


def do_add(tgs, idx, val):
    if check_index(tgs, idx):
        tgs.insert(idx, val)
    else:
        print("Invalid placement!")


def do_strike(tgs, idx, rad):
    start_index = idx - rad
    end_index = idx + rad
    if check_start_end_index(tgs, start_index, end_index):
        del tgs[start_index:end_index + 1]
    else:
        print("Strike missed!")


targets = [int(x) for x in input().split(" ")]
command = input()

while command != "End":

    command = command.split(" ")
    order = command[0]
    index = int(command[1])

    if order == "Shoot":
        power = int(command[2])
        do_shoot(targets, index, power)

    elif order == "Add":
        value = int(command[2])
        do_add(targets, index, value)

    elif order == "Strike":
        radius = int(command[2])
        do_strike(targets, index, radius)

    command = input()

print("|".join([str(x) for x in targets]))
