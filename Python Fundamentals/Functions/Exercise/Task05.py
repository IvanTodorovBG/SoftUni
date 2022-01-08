numbers = [int(x) for x in input().split(" ")]

list_of_num = (list(filter(lambda x: x % 2 == 0, numbers)))

print(list_of_num)

