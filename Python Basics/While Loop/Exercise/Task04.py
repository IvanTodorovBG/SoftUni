needed_steps = 10000
steps = input()

steps_counter = 0

while steps != "Going home":
    steps = int(steps)
    steps_counter += steps
    if steps_counter >= needed_steps:
        more_steps = steps_counter - needed_steps
        print("Goal reached! Good job!")
        print(f"{more_steps} steps over the goal!")
        break
    steps = input()
if steps == "Going home":
    last_steps = int(input())
    total_steps = steps_counter + last_steps
    if total_steps >= needed_steps:
        enough = total_steps - needed_steps
        print("Goal reached! Good job!")
        print(f"{enough} steps over the goal!")
    elif needed_steps > total_steps:
        not_enough = needed_steps - total_steps
        print(f"{not_enough} more steps to reach goal.")
