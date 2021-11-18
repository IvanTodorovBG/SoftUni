max_n1 = int(input())
max_n2 = int(input())
max_n3 = int(input())
for num1 in range(2, max_n1 + 1, 2):
    for num2 in range(2, max_n2 + 1):
        N = False
        count = 0
        for i in range(2, (num2 // 2 + 1)):
            if num2 % i == 0:
                count = count + 1
                break
        if count == 0 and num2 != 1:
            N = True
            for num3 in range(2, max_n3 + 1, 2):
                if N:
                    print(f"{num1} {num2} {num3}")