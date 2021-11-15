n = int(input())
count = 0
for a in range(1, n + 1):
    for b in range(1, a + 1):
        count += 1
        print(f"{count}", end= " ")
        if count == n:
            break
    print()
    if count == n:
        break
