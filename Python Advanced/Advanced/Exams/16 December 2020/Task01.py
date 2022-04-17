males = [int(x) for x in input().split(" ")]
females = [int(x) for x in input().split(" ")]
matches = 0

while True:

    if females and males:

        if females[0] <= 0:
            females.pop(0)
            continue
        elif females[0] % 25 == 0:
            females.pop(0)
            if females:
                females.pop(0)
            continue

        if males[-1] <= 0:
            males.pop(-1)
            continue
        elif males[-1] % 25 == 0:
            males.pop(-1)
            if males:
                males.pop(-1)
            continue

        if females[0] == males[-1]:
            matches += 1
            females.pop(0)
            males.pop(-1)
        else:
            females.pop(0)
            males[-1] -= 2

    else:
        break

print(f"Matches: {matches}")

if males:
    males.reverse()
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
