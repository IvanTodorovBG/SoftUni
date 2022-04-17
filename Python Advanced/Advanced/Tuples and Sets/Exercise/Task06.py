n = int(input())
even_set = set()
odd_set = set()

for index in range(1, n + 1):

    name = input()
    ascii_value = 0

    for char in name:
        ascii_value += ord(char)

    ascii_value /= index
    ascii_value = int(ascii_value)

    if ascii_value % 2 == 0:
        even_set.add(ascii_value)
    else:
        odd_set.add(ascii_value)

if sum(even_set) == sum(odd_set):
    union = even_set.union(odd_set)
    print(", ".join([str(x) for x in union]))

elif sum(odd_set) > sum(even_set):
    print(", ".join([str(x) for x in odd_set]))

elif sum(odd_set) < sum(even_set):
    sym_dif = even_set.symmetric_difference(odd_set)
    print(", ".join([str(x) for x in sym_dif]))