from collections import deque

pizza_orders = deque([int(el) for el in input().split(", ")])
employees = [int(el) for el in input().split(", ")]
total_pizza = 0

while pizza_orders and employees:

    if pizza_orders[0] <= 0 or pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue

    if pizza_orders[0] <= employees[-1]:
        total_pizza += pizza_orders[0]
        pizza_orders.popleft()
        employees.pop()

    elif pizza_orders[0] > employees[-1]:
        total_pizza += employees[-1]
        pizza_orders[0] -= employees[-1]
        employees.pop()

if employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")




