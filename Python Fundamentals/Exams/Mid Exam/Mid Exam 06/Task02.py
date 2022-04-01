chest = input().split("|")
command = input()

while command != "Yohoho!":

    command = command.split(" ")

    order = command[0]

    if order == "Loot":
        for loot in command[1:]:
            if loot not in chest:
                chest.insert(0, loot)

    elif order == "Drop":
        index = int(command[1])
        if 0 <= index < len(chest):
            chest.append(chest.pop(index))

    elif order == "Steal":
        count = int(command[1])
        stolen_items = chest[-count:]
        del chest[-count:]
        print(", ".join(stolen_items))
    command = input()

if not chest:
    print("Failed treasure hunt.")
else:
    sum_all_items = sum([len(x) for x in chest])
    count_of_items = len(chest)
    average_treasure_gain = sum_all_items / count_of_items
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
