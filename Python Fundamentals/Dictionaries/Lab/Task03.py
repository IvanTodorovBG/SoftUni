command = input()
inventory = {}

while command != "statistics":

    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in inventory:
        inventory[key] = value
    else:
        inventory[key] += value

    command = input()
print("Products in stock:")
for item in inventory:
    print("- " + f"{item}" + ": " + f"{inventory[item]}")
print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")
