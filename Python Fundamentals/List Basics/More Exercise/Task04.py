numbers = [int(x) for x in input().split(" ")]
middle = int(len(numbers) / 2)

left_racer = numbers[:middle]
right_racer = numbers[middle + 1:]
right_racer.reverse()

time_left = 0
time_right = 0

for current_time in left_racer:
    if current_time != 0:
        time_left += current_time
    else:
        time_left = time_left - (time_left * 0.2)

for current_time in right_racer:
    if current_time != 0:
        time_right += current_time
    else:
        time_right = time_right - (time_right * 0.2)

if time_left > time_right:
    print(f"The winner is right with total time: {time_right:.1f}")
else:
    print(f"The winner is left with total time: {time_left:.1f}")