from collections import deque
n = int(input())
all_pumps = deque()
win = False

for _ in range(n):
    pump = input()
    all_pumps.append(pump)

for index in range(n):

    total_fuel = 0
    win_number = 0

    for current_pump in all_pumps:
        current_pump = current_pump.split(" ")
        amount_fuel = int(current_pump[0])
        distance = int(current_pump[1])
        total_fuel += amount_fuel

        if total_fuel >= distance:
            total_fuel -= distance
            win_number += 1
            if win_number == len(all_pumps):
                print(index)
                win = True
                break

        else:
            all_pumps.append(all_pumps.popleft())
            break
    if win:
        break
