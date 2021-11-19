n = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a+b == c+d and n % (a+b) == 0:
                    print(f"{a}{b}{c}{d}", end=" ")


