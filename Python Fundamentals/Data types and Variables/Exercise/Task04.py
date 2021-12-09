n = int(input())

total_sum = 0

for x in range(1, n + 1):
    ascii_code = input()
    total_sum += ord(ascii_code)

print(f"The sum equals: {total_sum}")