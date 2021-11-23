days = int(input())
hours = int(input())

total_price = 0
count = 0

for day in range(1, days + 1):
    count += 1
    day_price = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        day_price += price
        total_price += price
    print(f"Day: {count} - {day_price:.2f} leva")
print(f"Total: {total_price:.2f} leva")