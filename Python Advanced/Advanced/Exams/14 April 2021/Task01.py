pizza_orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]
pizzas_made = 0

for _ in range(len(employees)):
    if pizza_orders:
        if pizza_orders[0] <= 0:
            pizza_orders.pop(0)
            continue

        if pizza_orders[0] > 10:
            pizza_orders.pop(0)

        elif pizza_orders[0] <= employees[-1]:
            pizzas_made += pizza_orders[0]
            pizza_orders.pop(0)
            employees.pop(-1)

        elif pizza_orders[0] > employees[-1]:
            pizzas_made += employees[-1]
            pizza_orders[0] -= employees[-1]
            employees.pop(-1)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
