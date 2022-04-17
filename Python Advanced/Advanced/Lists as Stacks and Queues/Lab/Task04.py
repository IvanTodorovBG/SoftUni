from collections import deque
queue = deque()

water = int(input())
element = input()

while element != "Start":

    queue.append(element)

    element = input()

command = input()

while command != "End":

    if "refill" in command:
        command = command.split(" ")
        amount = int(command[1])
        water += amount

    else:
        liters = int(command)
        if liters <= water:
            water -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{water} liters left")

