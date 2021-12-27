day_events = input().split("|")
max_energy = 100
current_energy = 100
gained_energy = 0
coins = 100
loose = False

for day in day_events:

    event = day.split("-")[0]
    number = int(day.split("-")[1])

    if event == "rest":
        needed_energy = max_energy - current_energy
        gained_energy = min(needed_energy, number)
        current_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event == "order":
        if current_energy >= 30:
            current_energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print(f"You had to rest!")

    else:
        coins -= number
        if coins > 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            loose = True
            break

if not loose:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {current_energy}")

