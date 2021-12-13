num = int(input())

is_a_Prime = False

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            is_a_Prime = True
            break

if is_a_Prime:
    print("False")
else:
    print("True")