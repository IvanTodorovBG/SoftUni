n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    numbers = float(input())
    if numbers % 2 == 0:
        p1 += 1
    if numbers % 3 == 0:
        p2 += 1
    if numbers % 4 == 0:
        p3 += 1

p1_perc = p1 / n * 100
p2_perc = p2 / n * 100
p3_perc = p3 / n * 100

print(f"{p1_perc:.2f}%")
print(f"{p2_perc:.2f}%")
print(f"{p3_perc:.2f}%")