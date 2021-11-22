money_1 = int(input())
money_2 = int(input())
money_5 = int(input())
price = int(input())

for a1 in range(money_1 + 1):
    for a2 in range(money_2 + 1):
        for a3 in range(money_5 + 1):
            if ((a1 * 1) + (a2 * 2) + (a3 * 5)) == price:
                print(f"{a1} * 1 lv. + {a2} * 2 lv. + {a3} * 5 lv. = {price} lv.", end=" ")
                print()
