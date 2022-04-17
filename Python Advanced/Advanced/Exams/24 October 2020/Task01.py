from collections import deque
jobs = deque([int(num) for num in input().split(", ")])
search_index = int(input())
clock_cycle = 0
ordered_numbers = sorted(list(set(jobs)))
total_cycles = 0
index_found = False

for current_number in ordered_numbers:
    indexes_of_current_number = [idx for idx, num in enumerate(jobs) if num == current_number]
    for index in indexes_of_current_number:
        total_cycles += current_number
        if index == search_index:
            index_found = True
            break
    if index_found:
        break

print(total_cycles)


