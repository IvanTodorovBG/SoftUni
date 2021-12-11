n = int(input())

tank_capacity = 255
liters_in_tank = 0

for x in range(1, n + 1):
    added_water = int(input())

    if liters_in_tank <= tank_capacity:
        liters_in_tank += added_water

        if liters_in_tank > tank_capacity:
            liters_in_tank -= added_water
            print(f"Insufficient capacity!")

print(liters_in_tank)






