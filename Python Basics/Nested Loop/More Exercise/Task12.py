m = int(input())
count = 0
magic = False
password = 0
for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if (a < b and c > d) and ((a * b) + (c * d)) == m:
                    count += 1
                    if count == 4:
                        magic = True
                        password = f"{a}{b}{c}{d}"
                    print(f"{a}{b}{c}{d}", end=" ")

if magic:
    print()
    print(f"Password: {password}")
else:
    print()
    print(f"No!")






