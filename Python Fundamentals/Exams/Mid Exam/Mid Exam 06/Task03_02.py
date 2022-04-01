def status(pirateship):
    count_sections = 0
    for section in pirateship:
        if section < (max_health * 0.2):
            count_sections += 1
    print(f"{count_sections} sections need repair.")


def repair(idx, hlth):
    pirate_ship[idx] += hlth
    if pirate_ship[idx] > max_health:
        pirate_ship[idx] = max_health


def defend(start, stop, dmg):
    for indx in range(start, stop + 1):
        pirate_ship[indx] -= dmg

        if pirate_ship[indx] <= 0:
            print("You lost! The pirate ship has sunken.")
            return False
    return True


def fire(war_shp, idx, dmg):
        war_shp[idx] -= dmg
        if war_shp[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            return False
        else:
            return True


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
            if not fire(war_ship, index, damage):
                lost = True
                break

    elif order == "Defend":
        start_index = int(command[1])
        stop_index = int(command[2])
        damage = int(command[3])

        if 0 <= start_index and stop_index < len(pirate_ship):

            if not defend(start_index, stop_index, damage):
                lost = True
                break

    elif order == "Repair":
        index = int(command[1])
        health = int(command[2])

        if 0 <= index < len(pirate_ship):
            repair(index, health)

    elif order == "Status":
        status(pirate_ship)

    command = input()

if not lost:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}")

