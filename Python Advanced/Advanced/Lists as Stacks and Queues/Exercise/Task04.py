clothes = [int(num) for num in input().split()]
rack = int(input())
empty_space = rack
rack_count = 0

while True:

    if clothes:

        if clothes[-1] <= empty_space:
            empty_space -= clothes[-1]
            clothes.pop()

        else:
            empty_space = rack
            rack_count += 1

    else:
        if empty_space < rack:
            rack_count += 1
        break

print(rack_count)