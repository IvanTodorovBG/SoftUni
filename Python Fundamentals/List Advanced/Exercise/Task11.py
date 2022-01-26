inventory = input().split(", ")
command = input()

while command != "Craft!":

    command = command.split(" - ")

    order = command[0]

    if order == "Collect":
        item = command[1]
        if item not in inventory:
            inventory.append(item)

    elif order == "Drop":
        item = command[1]
        if item in inventory:
            inventory.remove(item)

    elif order == "Combine Items":
        combined_items = command[1].split(":")
        old_item = combined_items[0]
        new_item = combined_items[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)

    elif order == "Renew":
        item = command[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join([str(x) for x in inventory]))







