first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_numbers():
    sum_num = first_num + second_num
    return sum_num


def subtract():
    diff = sum_numbers() - third_num
    return diff


def add_and_subtract():
    return sum_numbers() and subtract()


print(add_and_subtract())