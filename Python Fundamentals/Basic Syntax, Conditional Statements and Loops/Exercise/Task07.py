divisor = int(input())
boundary = int(input())

for x in range(boundary, 1, -1):
    if x % divisor == 0:
        print(x)
        break
