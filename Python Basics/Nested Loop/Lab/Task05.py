destination = input()

while destination != "End":
    saved_money = 0
    budget = float(input())
    while saved_money < budget:
        money = float(input())
        saved_money += money
    else:
        print(f"Going to {destination}!")
    destination = input()