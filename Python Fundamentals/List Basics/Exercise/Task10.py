command = input().split("|")

energy = 100
coins = 100
clear_event = True

for current_command in command:
    current_command = current_command.split("-")

    event = current_command[0]
    number = int(current_command[1])

    if event == "rest":
        needed_energy = 100 - energy
        gained_energy = min(number, needed_energy)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        coins -= number
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            clear_event = False
            break

if clear_event:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

