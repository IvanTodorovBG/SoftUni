n = int(input())
sum_odd = 0
sum_even = 0
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    diff = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {diff}")