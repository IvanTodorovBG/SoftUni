n = int(input())
n_2 = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_2(n_2):
    if n_2 == 0:
        return 1
    else:
        return n_2 * factorial(n_2 - 1)


number_one = factorial(n)
number_two = factorial_2(n_2)

result = number_one / number_two
print(f"{result:.2f}")
