money_for_excursion = float(input())
money_on_hand = float(input())

pass_days = 0
spend_counter = 0

while money_on_hand < money_for_excursion:
    action = input()
    saved_spend_money = float(input())
    pass_days += 1
    if action == "save":
        money_on_hand += saved_spend_money
        spend_counter = 0
    elif action == "spend":
        money_on_hand -= saved_spend_money
        spend_counter += 1
        if money_on_hand < 0:
            money_on_hand = 0
    if spend_counter == 5:
        print("You can\'t save the money.")
        print(f"{pass_days}")
        break
if money_on_hand >= money_for_excursion:
    print(f"You saved the money for {pass_days} days.")