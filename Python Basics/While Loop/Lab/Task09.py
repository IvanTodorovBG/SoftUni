width = int(input())
length = int(input())
height = int(input())
n = input()

free_space = width * length * height
used_space = 0
left_space = 0
while n != "Done":
    boxes = int(n)
    used_space += boxes
    left_space = free_space - used_space
    if used_space >= free_space:
        not_enough_space = used_space - free_space
        print(f"No more free space! You need {not_enough_space} Cubic meters more.")
        break
    n = input()
if n == "Done":
    print(f"{left_space} Cubic meters left.")
