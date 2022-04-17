def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    answer = []
    for func, func_args in args:
        result = func(*func_args)
        answer.append(result)
    return answer


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))