n = int(input())
num = 0
average = 0
for x in range(1, n + 1):
    numbers = int(input())
    num += numbers
    average = num / n
print(f"{average:.2f}")
