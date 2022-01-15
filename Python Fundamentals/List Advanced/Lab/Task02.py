wagons = int(input())
command = input()

wagons_list = []

for current_wagon in range(wagons):
    wagons_list.append(0)

while command != "End":
    command = command.split(" ")
    order = command[0]

    if order == "add":
        people = int(command[1])
        wagons_list[-1] += people

    elif order == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons_list[index] += people

    elif order == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons_list[index] -= people

    command = input()

print(wagons_list)
