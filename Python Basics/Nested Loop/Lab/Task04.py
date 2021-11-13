import sys
n1 = int(input())
n2 = int(input())
magic_number = int(input())
combination = 0
for x1 in range(n1, n2 + 1):
    for x2 in range(n1, n2 + 1):
        combination += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{combination} ({x1} + {x2} = {magic_number})")
            sys.exit()
if x1 + x2 != magic_number:
    print(f"{combination} combinations - neither equals {magic_number}")
