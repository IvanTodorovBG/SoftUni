def cupid(all_houses, house_idx):
    if all_houses[house_idx] == 0:
        print(f"Place {house_idx} already had Valentine's day.")
    else:
        all_houses[house_idx] -= 2
        if all_houses[house_idx] == 0:
            print(f"Place {house_idx} has Valentine's day.")
    return all_houses


houses = [int(i) for i in input().split("@")]

command = input()
house_index = 0

while command != "Love!":
    command = command.split(" ")
    number = int(command[1])

    house_index += number

    if house_index < len(houses):
        houses = cupid(houses, house_index)
    else:
        house_index = 0
        houses = cupid(houses, house_index)

    command = input()

print(f"Cupid's last position was {house_index}.")

if houses.count(0) == len(houses):
    print("Mission was successful.")
else:
    count_houses_non_zero = len([i for i in houses if i != 0])
    print(f"Cupid has failed {count_houses_non_zero} places.")
