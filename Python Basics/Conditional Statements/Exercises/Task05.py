budget = float(input())
statistics = int(input())
price_for_cloths = float(input())

decor = budget * 0.1
costs_for_cloths = statistics * price_for_cloths

if statistics > 150:
    costs_for_cloths = costs_for_cloths - costs_for_cloths * 0.10

expences = decor + costs_for_cloths

if expences > budget:
    lack = expences - budget
    print(f"""Not enough money!
Wingard needs {lack:.2f} leva more.""")
elif expences <= budget:
    left_money = budget - expences
    print(f"""Action!
Wingard starts filming with {left_money:.2f} leva left.""")