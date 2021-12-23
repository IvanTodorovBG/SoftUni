numbers = [int(x) for x in input().split(" ")]
n = int(input())

sorted_numbers = sorted(numbers)
to_delete = []
answer = []

for index in range(n):
    to_delete.append(sorted_numbers[index])

for num in numbers:
    if num not in to_delete:
        answer.append(num)


print(", ".join([str(x) for x in answer]))