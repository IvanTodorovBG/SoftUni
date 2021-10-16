n1 = int(input())
n2 = int(input())
operation = input()

total_amount = 0

if operation == "+":
    total_amount = n1 + n2
elif operation == "-":
    total_amount = n1 - n2
elif operation == "*":
    total_amount = n1 * n2
elif operation == "/" and n2 != 0:
    total_amount = n1 / n2
elif operation == "%" and n2 != 0:
    total_amount = n1 % n2

if operation == "+" or operation == "-" or operation == "*":
    if total_amount % 2 == 0:
        kind = "even"
    else:
        kind = "odd"
    print(f"{n1} {operation} {n2} = {total_amount} - {kind}")
elif operation == "/" and n2 != 0:
    print(f"{n1} / {n2} = {total_amount:.2f}")
elif operation == "%" and n2 != 0:
    print(f"{n1} % {n2} = {total_amount}")
elif n2 == 0:
    print(f"Cannot divide {n1} by zero")