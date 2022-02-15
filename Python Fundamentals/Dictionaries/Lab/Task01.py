command = input().split(" ")
bakery = {}

for current_index in range(0, len(command), 2):
    key = command[current_index]
    value = command[current_index + 1]
    bakery[key] = int(value)
print(bakery)

