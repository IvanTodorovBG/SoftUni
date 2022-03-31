def collect(itm):
    if itm not in inventory:
        inventory.append(itm)


def drop(itm):
    if itm in inventory:
        inventory.remove(itm)


def combine_items(itm):
    itm = itm.split(":")
    old_item = itm[0]
    new_item = itm[1]
    if old_item in inventory:
        for ix, it in enumerate(inventory):
            if it == old_item:
                inventory.insert(ix + 1, new_item)


def renew(itm):
    if itm in inventory:
        inventory.remove(itm)
        inventory.append(itm)


inventory = input().split(", ")
command = input()

while command != "Craft!":

    command = command.split(" - ")
    order = command[0]
    items = command[1]

    if order == "Collect":
        collect(items)
    elif order == "Drop":
        drop(items)
    elif order == "Combine Items":
        combine_items(items)
    elif order == "Renew":
        renew(items)

    command = input()

print(", ".join([str(x) for x in inventory]))