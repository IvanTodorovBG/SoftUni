from collections import deque
total_food = int(input())
orders = deque([int(num) for num in input().split()])

if orders:
    print(max(orders))

while True:
    if orders:
        if orders[0] <= total_food:
            total_food -= orders[0]
            orders.popleft()
        else:
            break
    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(num) for num in orders])}")
