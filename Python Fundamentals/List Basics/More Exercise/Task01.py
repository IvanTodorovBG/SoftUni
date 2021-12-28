numbers = [int(x) for x in input().split(", ")]

for number in numbers:
    if number == 0:
        numbers.remove(number)
        numbers.append(number)

print(numbers)