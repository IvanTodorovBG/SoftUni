n = int(input())
num1 = ""
num2 = ""
num3 = ""
num4 = ""
for a in range(1111, 9999 + 1):
    num1 = str(a)[0]
    num2 = str(a)[1]
    num3 = str(a)[2]
    num4 = str(a)[3]
    if int(num1) != 0 and int(num2) != 0 and int(num3) != 0 and int(num4) != 0:
        if n % int(num1) == 0 and n % int(num2) == 0 and n % int(num3) == 0 and n % int(num4) == 0:
            print(f"{num1}{num2}{num3}{num4}", end=" ")










