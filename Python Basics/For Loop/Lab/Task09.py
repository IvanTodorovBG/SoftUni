n = int(input())
sum_left = 0
sum_right = 0
for i in range(0, 2 * n):
    num = int(input())
    if i < n:
        sum_left += num
    else:
        sum_right += num

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(f"No, diff = {diff}")