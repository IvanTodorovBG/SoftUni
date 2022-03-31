dungeons_rooms = input().split("|")

health = 100
bitcoins = 0
room_counter = 0
fail = False

for room in dungeons_rooms:
    command = room.split(" ")
    order = command[0]
    room_counter += 1

    if order == "potion":
        potion_amount = int(command[1])
        necessary_health = 100 - health
        healed = min(necessary_health, potion_amount)
        health += healed
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif order == "chest":
        coins = int(command[1])
        bitcoins += coins
        print(f"You found {coins} bitcoins.")

    else:
        monster = command[0]
        monster_attack = int(command[1])

        if health > 0:
            health -= monster_attack

            if health <= 0:
                print(f"You died! Killed by {monster}.")
                print(f"Best room: {room_counter}")
                fail = True
                break

            print(f"You slayed {monster}.")

        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_counter}")
            fail = True
            break

if not fail:
    print(f"""You've made it!
Bitcoins: {bitcoins}
Health: {health}""")