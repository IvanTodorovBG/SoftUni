houses = [int(x) for x in input().split("@")]
command = input()
index = 0

while command != "Love!":

    command = command.split(" ")
    order = command[0]
    length = int(command[1])
    index += length

    if 0 <= index < len(houses):

        if houses[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            houses[index] -= 2
            if houses[index] == 0:
                print(f"Place {index} has Valentine's day.")
    else:

        index = 0

        if houses[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            houses[index] -= 2
            if houses[index] == 0:
                print(f"Place {index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {index}.")

valentines_day = houses.count(0)
fail_house = len(houses) - valentines_day

if fail_house != 0:
    print(f"Cupid has failed {fail_house} places.")
else:
    print("Mission was successful.")
