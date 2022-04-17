from collections import deque

jobs = deque([int(num) for num in input().split(", ")])
searched_index = int(input())
clock_cycles = 0
cycle = 1
won = False

while True:

    for idx, num in enumerate(jobs):
        if cycle == num:
            clock_cycles += num
            if idx == searched_index:
                print(clock_cycles)
                won = True
                break
    if won:
        break
    cycle += 1

