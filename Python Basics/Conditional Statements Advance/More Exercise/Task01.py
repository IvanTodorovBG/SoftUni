budget = float(input())
category = input()
people = int(input())

vip_ticket_price = 499.99
normal_ticket_price = 249.99
transport_price = 0
remain_money = 0
total_price = 0
money = 0

if 1 <= people <= 4:
    transport_price = budget * 0.75
elif 5 <= people <= 9:
    transport_price = budget * 0.6
elif 10 <= people <= 24:
    transport_price = budget * 0.5
elif 25 <= people <= 49:
    transport_price = budget * 0.4
elif people >= 50:
    transport_price = budget * 0.25

remain_money = budget - transport_price

if category == "Normal":
    money = normal_ticket_price * people
elif category == "VIP":
    money = vip_ticket_price * people


if remain_money >= money:
    left_money = remain_money - money
    print(f"Yes! You have {left_money:.2f} leva left.")
elif money > remain_money:
    not_enough_money = money - remain_money
    print(f"Not enough money! You need {not_enough_money:.2f} leva.")