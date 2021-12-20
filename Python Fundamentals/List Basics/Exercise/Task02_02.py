factor = int(input())
count = int(input())

multiples_list = [x * factor for x in range(1, count + 1)]

print(multiples_list)