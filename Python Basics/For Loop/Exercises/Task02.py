n = int(input())
import sys
max_num = -sys.maxsize
sum_numbers = 0

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_numbers += num

sum_others = sum_numbers - max_num

if max_num == sum_others:
    print("Yes")
    print(f"Sum = {sum_others}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum_others)}")

