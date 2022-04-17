numbers = [int(num) for num in input().split()]
rev_numbers = []

while numbers:
    rev_numbers.append(numbers.pop())

print(f"{' '.join([str(num) for num in rev_numbers])}")
