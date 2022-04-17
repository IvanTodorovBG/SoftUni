from collections import deque
bees = deque([int(x) for x in input().split()])
nectar_value = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectar_value and symbols:

    if bees[0] > nectar_value[-1]:
        nectar_value.pop()
    elif bees[0] <= nectar_value[-1]:

        if symbols[0] == "-":
            total_honey += abs(bees[0] - nectar_value[-1])
        elif symbols[0] == "+":
            total_honey += abs(bees[0] + nectar_value[-1])
        elif symbols[0] == "/" and nectar_value[-1] != 0:
            total_honey += abs(bees[0] / nectar_value[-1])
        elif symbols[0] == "*":
            total_honey += abs(bees[0] + nectar_value[-1])
        symbols.popleft()
        nectar_value.pop()
        bees.popleft()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if nectar_value:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_value])}")