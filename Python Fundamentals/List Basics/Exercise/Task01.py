command = input().split(" ")

numbers = []

for num in command:
    if int(num) >= 0:
        numbers.append(-int(num))
    else:
        numbers.append((abs(int(num))))

print(numbers)