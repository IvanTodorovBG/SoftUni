needed_money = int(input())
x = input()
count = 0
cash = 0
card = 0
total_money = 0
cash_count = 0
card_count = 0
while x != "End":
    count += 1
    money = int(x)
    if count % 2 != 0:
        if money > 100:
            print("Error in transaction!")
        elif money <= 100:
            total_money += money
            cash += money
            cash_count += 1
            print("Product sold!")
    elif count % 2 == 0:
        if money < 10:
            print("Error in transaction!")
        elif money >= 10:
            total_money += money
            card += money
            card_count += 1
            print("Product sold!")
    if total_money >= needed_money:
        average_cs = cash / cash_count
        average_cc = card / card_count
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break
    x = input()
if x == "End":
    print("Failed to collect required money for charity.")



