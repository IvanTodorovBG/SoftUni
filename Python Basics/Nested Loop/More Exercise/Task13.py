start_1 = int(input())
start_2 = int(input())
stop_1 = int(input())
stop_2 = int(input())

for num1 in range(start_1, (start_1 + stop_1) + 1):
    for num2 in range(start_2, (start_2 + stop_2) + 1):
        N = False
        count = 0
        for i in range(2, (num2 // 2 + 1)):
            if num2 % i == 0:
                count = count + 1
                break
        if count == 0 and num2 != 1:
            N = True
        M = False
        count = 0
        for i in range(2, (num1 // 2 + 1)):
            if num1 % i == 0:
                count = count + 1
                break
        if count == 0 and num1 != 1:
            M = True
            if N and M:
                print(f"{num1}{num2}")




