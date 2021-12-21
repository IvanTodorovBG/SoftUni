numbers = [int(i) for i in input().split(", ")]
count_of_beggars = int(input())
result = []

for current_beggar in range(count_of_beggars):

    beggar_sum = sum(numbers[current_beggar::count_of_beggars])

    result.append(beggar_sum)

print(result)

