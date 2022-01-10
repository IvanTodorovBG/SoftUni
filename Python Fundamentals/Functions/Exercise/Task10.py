number = int(input())


def perfect_number(num):
    sum_digits = 0
    for i in range(1, num):
        if num % i == 0:
            sum_digits += i

    if sum_digits == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(number))