from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups.popleft() - bottle

    if cup > 0:
        cups.appendleft(cup)
    else:
        wasted_water += abs(cup)

if bottles:
    print(f'Bottles: {" ".join([str(x) for x in bottles])}')
else:
    print(f'Cups: {" ".join([str(x) for x in cups])}')

print(f'Wasted litters of water: {wasted_water}')