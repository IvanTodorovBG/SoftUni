factor = int(input())
n = int(input())

numbers = []

for x in range(1, (n * factor) + 1):

    if x % factor == 0:
       numbers.append(x)

print(numbers)