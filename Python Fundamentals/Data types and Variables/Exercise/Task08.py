group_size = int(input())
total_days = int(input())

coins = 0
days_counter = 0

for x in range(total_days):
    days_counter += 1
    if days_counter % 10 == 0:
        group_size -= 2
    if days_counter % 15 == 0:
        group_size += 5
    coins += (50 - (group_size * 2))
    if days_counter % 3 == 0:
        coins -= group_size * 3
    if days_counter % 5 == 0:
        coins += group_size * 20
        if days_counter % 3 == 0:
            coins -= group_size * 2

coins_per_companion = coins / group_size

print(f"{group_size} companions received {int(coins_per_companion)} coins each.")