from collections import deque

chocolate = [int(num) for num in input().split(",")]
milk = deque([int(num) for num in input().split(",")])

milkshakes = 0
milkshakes_success = False

while chocolate and milk:

    current_chocolate = chocolate[-1]
    current_milk = milk[0]

    if current_chocolate <= 0 and current_milk <= 0:
        chocolate.pop()
        milk.popleft()
        continue

    if current_chocolate <= 0:
        chocolate.pop()
        continue

    elif current_milk <= 0:
        milk.popleft()
        continue

    if current_chocolate == current_milk:
        chocolate.pop()
        milk.popleft()
        milkshakes += 1
        if milkshakes == 5:
            milkshakes_success = True
            break

    else:
        milk.append(milk.popleft())
        current_chocolate -= 5


if milkshakes_success:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")
