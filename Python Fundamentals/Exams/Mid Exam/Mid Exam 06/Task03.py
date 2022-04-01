pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health = int(input())
command = input()
lost = False

while command != "Retire":

    command = command.split(" ")
    order = command[0]

    if order == "Fire":
        index = int(command[1])
        damage = int(command[2])

        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                lost = True
                break
        if lost:
            break
    if lost:
        break

    elif order == "Defend":
        start_index = int(command[1])
        stop_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index and stop_index < len(pirate_ship):

            for idx in range(start_index, stop_index + 1):
                pirate_ship[idx] -= damage

                if pirate_ship[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break
            if lost:
                break
        if lost:
            break
    if lost:
        break

    elif order == "Repair":
        index = int(command[1])
        health = int(command[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif order == "Status":
        count_sections = 0
        for section in pirate_ship:
            if section < (max_health * 0.2):
                count_sections += 1
        print(f"{count_sections} sections need repair.")

    command = input()

if not lost:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}")