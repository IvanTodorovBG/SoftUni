x = input()
total = 0

while x != "NoMoreMoney":
    money = float(x)
    if money > 0:
        total += money
        print(f"Increase: {money:.2f}")
        x = input()
    elif money < 0:
        print("Invalid operation!")
        break

print(f"Total: {total:.2f}")