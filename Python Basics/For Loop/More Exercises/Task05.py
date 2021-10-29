n = int(input())

score = 0
count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
invalid_numbers = 0

for i in range(1, n + 1):
    num = int(input())
    if 0 <= num <= 9:
        score += num * 0.2
        count_0_9 += 1
    elif 10 <= num <= 19:
        score += num * 0.3
        count_10_19 += 1
    elif 20 <= num <= 29:
        score += num * 0.4
        count_20_29 += 1
    elif 30 <= num <= 39:
        score += 50
        count_30_39 += 1
    elif 40 <= num <= 50:
        score += 100
        count_40_50 += 1
    elif num > 50:
        score /= 2
        invalid_numbers += 1
    else:
        score /= 2
        invalid_numbers += 1

count_0_9_perc = count_0_9 / n * 100
count_10_19_perc = count_10_19 / n * 100
count_20_29_perc = count_20_29 / n * 100
count_30_39_perc = count_30_39 / n * 100
count_40_50_perc = count_40_50 / n * 100
invalid_numbers_perc = invalid_numbers / n * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {count_0_9_perc:.2f}%")
print(f"From 10 to 19: {count_10_19_perc:.2f}%")
print(f"From 20 to 29: {count_20_29_perc:.2f}%")
print(f"From 30 to 39: {count_30_39_perc:.2f}%")
print(f"From 40 to 50: {count_40_50_perc:.2f}%")
print(f"Invalid numbers: {invalid_numbers_perc:.2f}%")