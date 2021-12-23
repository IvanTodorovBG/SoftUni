numbers = [int(num) for num in input().split(" ")]
count_of_numbers = int(input())

for num in range(count_of_numbers):
    min_num = min(numbers)
    numbers.remove(min_num)

print(", ".join([str(num) for num in numbers]))