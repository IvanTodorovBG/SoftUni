houses = [int(x) for x in input().split("@")]
command = input()

index = 0

while command != "Love!":
    command = command.split(" ")

    jump = command[0]
    length = int(command[1])

    if jump == "Jump":
        index += length
        if index >= len(houses):
            index = 0

        if houses[index] == 0:
            print(f"Place {index} already had Valentine's day.")

        elif houses[index] > 0:
            houses[index] -= 2
            if houses[index] == 0:
                print(f"Place {index} has Valentine's day.")

    command = input()

failed = len(houses) - houses.count(0)

print(f"Cupid's last position was {index}.")

if failed == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")