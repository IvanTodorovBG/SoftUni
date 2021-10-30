capacity_stadium = int(input())
n = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(1, n + 1):
    sectors = input()
    if sectors == "A":
        sector_a += 1
    elif sectors == "B":
        sector_b += 1
    elif sectors == "V":
        sector_v += 1
    elif sectors == "G":
        sector_g += 1

sector_a_perc = sector_a / n * 100
sector_b_perc = sector_b / n * 100
sector_v_perc = sector_v / n * 100
sector_g_perc = sector_g / n * 100
all_fans_perc = n / capacity_stadium * 100

print(f"{sector_a_perc:.2f}%")
print(f"{sector_b_perc:.2f}%")
print(f"{sector_v_perc:.2f}%")
print(f"{sector_g_perc:.2f}%")
print(f"{all_fans_perc:.2f}%")
