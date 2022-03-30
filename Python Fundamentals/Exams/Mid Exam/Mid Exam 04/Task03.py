houses = [int(x) for x in input().split("@")]
command = input()
house_number = 0

while command != "Love!":
    command = command.split(" ")
    index_house = int(command[1])
    house_number += index_house

    if 0 <= house_number < len(houses):

        if houses[house_number] != 0:
            houses[house_number] -= 2
            if houses[house_number] == 0:
                print(f"Place {house_number} has Valentine\'s day.")

        else:
            print(f"Place {house_number} already had Valentine's day.")

    else:
        house_number = 0

        if houses[house_number] != 0:
            houses[house_number] -= 2
            if houses[house_number] == 0:
                print(f"Place {house_number} has Valentine\'s day.")

        else:
            print(f"Place {house_number} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {house_number}.")
if houses.count(0) == len(houses):
    print(f"Mission was successful.")
else:
    non_zero = []
    for x in houses:
        if x != 0:
            non_zero.append(x)

    print(f"Cupid has failed {len(non_zero)} places.")