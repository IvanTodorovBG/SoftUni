number_of_cars = int(input())
cars_dict = {}
max_fuel = 75

for _ in range(number_of_cars):
    element = input().split("|")
    car = element[0]
    mileage = int(element[1])
    fuel = int(element[2])
    cars_dict[car] = {}
    cars_dict[car]['mileage'] = mileage
    cars_dict[car]['fuel'] = fuel

command = input()

while command != "Stop":

    command = command.split(" : ")
    order = command[0]
    car = command[1]

    if order == "Drive":
        distance = int(command[2])
        fuel = int(command[3])

        if cars_dict[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['fuel'] -= fuel
            cars_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]['mileage'] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")

    elif order == "Refuel":
        fuel = int(command[2])
        needed_fuel = max_fuel - cars_dict[car]['fuel']
        taken_fuel = min(needed_fuel, fuel)
        cars_dict[car]['fuel'] += taken_fuel
        print(f"{car} refueled with {taken_fuel} liters")

    elif order == "Revert":
        kilometers = int(command[2])
        cars_dict[car]['mileage'] -= kilometers
        if cars_dict[car]['mileage'] < 10000:
            cars_dict[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_cars_dict = dict(sorted(cars_dict.items(), key=lambda kvp: (-kvp[1]['mileage'], kvp[0])))

for kvp in sorted_cars_dict.items():
    print(f"{kvp[0]} -> Mileage: {kvp[1]['mileage']} kms, Fuel in the tank: {kvp[1]['fuel']} lt.")

