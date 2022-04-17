numbers = [float(num) for num in input().split()]
unique_numbers = sorted(set(numbers), key=numbers.index)

for num in unique_numbers:
    print(f"{num} - {numbers.count(num)} times")

