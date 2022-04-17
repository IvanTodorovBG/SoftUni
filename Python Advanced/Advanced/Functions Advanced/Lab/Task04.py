def recursive_power(num, n):
    if n == 0:
        return 1
    else:
        return num * recursive_power(num, n - 1)


print(recursive_power(2, 10))